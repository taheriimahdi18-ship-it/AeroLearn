"""Independent numerical and input-contract tests for dynamic pressure."""

import math
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from decimal import Decimal
from fractions import Fraction
from io import StringIO

from aerolearn.aerodynamics.dynamic_pressure import dynamic_pressure


class DynamicPressureTests(unittest.TestCase):
    """Verify SI reference values, validation, and floating-point behavior."""

    def _assert_value(
        self,
        density: object,
        speed: object,
        expected: float,
        max_ulps: int = 0,
    ) -> float:
        """Check a finite float result and silence, with an explicit tolerance."""
        stdout = StringIO()
        stderr = StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            actual = dynamic_pressure(density, speed)

        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")
        self.assertIs(type(actual), float)
        self.assertTrue(math.isfinite(actual))
        self.assertGreaterEqual(actual, 0.0)
        if max_ulps:
            self.assertLessEqual(
                abs(actual - expected),
                max_ulps * math.ulp(expected),
            )
        else:
            self.assertEqual(actual, expected)
        if expected == 0.0:
            self.assertEqual(math.copysign(1.0, actual), 1.0)
        return actual

    def _assert_error(
        self,
        density: object,
        speed: object,
        expected_type: type[Exception],
        expected_message: str,
    ) -> None:
        """Check the exact exception class and message without console output."""
        stdout = StringIO()
        stderr = StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            with self.assertRaises(expected_type) as caught:
                dynamic_pressure(density, speed)

        self.assertIs(type(caught.exception), expected_type)
        self.assertEqual(str(caught.exception), expected_message)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")

    def test_reference_values(self) -> None:
        """Compare hand-derived SI values and independent exact-float oracles."""
        reference_cases = (
            ("standard_density_100_m_s", 1.225, 100.0, 6125.0, 4),
            ("standard_density_50_m_s", 1.225, 50.0, 1531.25, 4),
            ("integer_inputs", 2, 3, 9.0, 0),
            ("fractional_inputs", 0.5, 0.5, 0.0625, 0),
        )
        for name, density, speed, expected, max_ulps in reference_cases:
            with self.subTest(case=name):
                self._assert_value(density, speed, expected, max_ulps)

        oracle_cases = (
            ("decimal_fractions", 0.1, 0.3),
            ("nonbinary_density_and_speed", 1.225, 123.456),
            ("tiny_density_large_speed", 1e-250, 1e150),
            ("large_density_tiny_speed", 1e250, 1e-100),
            ("small_normal_pressure", 1e-200, 1e-40),
            ("large_normal_pressure", 1e200, 1e50),
        )
        for name, density, speed in oracle_cases:
            with self.subTest(case=name):
                # The oracle uses exact rationals for the converted float inputs,
                # independently of the production exponent-scaling strategy.
                exact_density = Fraction.from_float(float(density))
                exact_speed = Fraction.from_float(float(speed))
                expected = float(exact_density * exact_speed**2 / 2)
                self._assert_value(density, speed, expected, max_ulps=4)

    def test_zero_boundaries(self) -> None:
        """Accept mathematical zero boundaries and normalize signed zeros."""
        cases = (
            ("zero_density", 0.0, 100.0),
            ("zero_speed", 1.225, 0.0),
            ("both_zero", 0.0, 0.0),
            ("negative_zero_density", -0.0, 100.0),
            ("negative_zero_speed", 1.225, -0.0),
            ("both_negative_zero", -0.0, -0.0),
            ("integer_zeros", 0, 0),
        )
        for name, density, speed in cases:
            with self.subTest(case=name):
                self._assert_value(density, speed, 0.0)

    def test_density_and_speed_scaling(self) -> None:
        """Check linear density scaling and quadratic speed scaling."""
        cases = (
            ("double_density", 2.5, 8.0, 80.0, 2.0),
            ("half_density", 0.625, 8.0, 20.0, 0.5),
            ("double_speed", 1.25, 16.0, 160.0, 4.0),
            ("triple_speed", 1.25, 24.0, 360.0, 9.0),
        )
        for name, density, speed, expected, factor in cases:
            with self.subTest(case=name):
                baseline = self._assert_value(1.25, 8.0, 40.0)
                actual = self._assert_value(density, speed, expected)
                self.assertEqual(actual, factor * baseline)

    def test_rejects_unsupported_types(self) -> None:
        """Reject implicit conversions, booleans, and numeric subclasses."""

        class IntSubclass(int):
            """An integer subclass outside the exact built-in type contract."""

        class FloatSubclass(float):
            """A float subclass outside the exact built-in type contract."""

        class IntLikeMeta(type):
            """A metaclass that claims equality with the built-in int type."""

            def __eq__(cls, other: object) -> bool:
                return other is int

        class IntImpostor(metaclass=IntLikeMeta):
            """An unsupported type that can defeat equality-based type checks."""

            def __lt__(self, other: object) -> bool:
                return False

            def __float__(self) -> float:
                return 2.0

        invalid_values = (
            ("metaclass_impostor", IntImpostor()),
            ("true", True),
            ("false", False),
            ("string", "1.225"),
            ("none", None),
            ("complex", 1 + 0j),
            ("decimal", Decimal("1.225")),
            ("fraction", Fraction(49, 40)),
            ("list", [1.225]),
            ("dictionary", {"value": 1.225}),
            ("integer_subclass", IntSubclass(1)),
            ("float_subclass", FloatSubclass(1.225)),
        )
        for parameter in ("density_kg_m3", "speed_m_s"):
            for name, value in invalid_values:
                with self.subTest(case=f"{parameter}_{name}"):
                    density, speed = (
                        (value, 50.0)
                        if parameter == "density_kg_m3"
                        else (1.225, value)
                    )
                    self._assert_error(
                        density,
                        speed,
                        TypeError,
                        f"{parameter} must be a built-in int or float "
                        "(bool is not accepted).",
                    )

    def test_rejects_negative_and_nonfinite_values(self) -> None:
        """Reject invalid values before attempting risky integer conversions."""
        invalid_values = (
            ("negative_integer", -1),
            ("negative_float", -0.5),
            ("negative_subnormal", -float.fromhex("0x1p-1074")),
            ("huge_negative_integer", -(10**400)),
            ("nan", math.nan),
            ("positive_infinity", math.inf),
            ("negative_infinity", -math.inf),
        )
        for parameter in ("density_kg_m3", "speed_m_s"):
            for name, value in invalid_values:
                with self.subTest(case=f"{parameter}_{name}"):
                    density, speed = (
                        (value, 50.0)
                        if parameter == "density_kg_m3"
                        else (1.225, value)
                    )
                    self._assert_error(
                        density,
                        speed,
                        ValueError,
                        f"{parameter} must be finite and non-negative.",
                    )

    def test_validates_inputs_before_zero_shortcut(self) -> None:
        """Validate density fully, then speed, before returning a zero result."""
        invalid_values = (
            ("boolean", True, TypeError,
             "must be a built-in int or float (bool is not accepted)."),
            ("negative", -1, ValueError, "must be finite and non-negative."),
            ("nan", math.nan, ValueError, "must be finite and non-negative."),
            ("infinity", math.inf, ValueError, "must be finite and non-negative."),
            ("huge_integer", 10**400, OverflowError,
             "is outside the supported float range."),
        )
        for parameter in ("density_kg_m3", "speed_m_s"):
            for name, value, error_type, message_suffix in invalid_values:
                with self.subTest(case=f"zero_with_{parameter}_{name}"):
                    density, speed = (
                        (value, 0.0)
                        if parameter == "density_kg_m3"
                        else (0.0, value)
                    )
                    self._assert_error(
                        density, speed, error_type, f"{parameter} {message_suffix}"
                    )

        order_cases = (
            ("density_type_before_speed_value", True, -1.0, TypeError,
             "density_kg_m3 must be a built-in int or float (bool is not accepted)."),
            ("density_value_before_speed_type", -1.0, True, ValueError,
             "density_kg_m3 must be finite and non-negative."),
            ("density_range_before_speed_type", 10**400, None, OverflowError,
             "density_kg_m3 is outside the supported float range."),
            ("density_range_before_speed_value", 10**400, math.nan, OverflowError,
             "density_kg_m3 is outside the supported float range."),
            ("density_value_before_speed_range", -(10**400), 10**400, ValueError,
             "density_kg_m3 must be finite and non-negative."),
            ("density_nonfinite_before_speed_type", math.nan, False, ValueError,
             "density_kg_m3 must be finite and non-negative."),
        )
        for name, density, speed, error_type, message in order_cases:
            with self.subTest(case=name):
                self._assert_error(density, speed, error_type, message)

    def test_integer_conversion_limits(self) -> None:
        """Accept finite conversions and report parameter-specific overflow."""
        accepted_cases = (
            ("large_integer_density", 2**1023, 2.0**-511, 1.0),
            ("large_integer_speed", 2.0**-1074, 2**1023, 2.0**971),
            ("maximum_exact_float_integer", int(sys.float_info.max), 1.0,
             sys.float_info.max / 2.0),
            ("rounded_integer_conversion", 2**53 + 1, 2.0, 2.0**54),
        )
        for name, density, speed, expected in accepted_cases:
            with self.subTest(case=name):
                self._assert_value(density, speed, expected)

        rejected_cases = (
            ("overflowing_density_finite_exact_result", 2**1024, 2.0**-600,
             "density_kg_m3"),
            ("huge_density_tiny_speed", 10**400, 1e-200, "density_kg_m3"),
            ("overflowing_speed_finite_exact_result", 2.0**-1074, 2**1024,
             "speed_m_s"),
            ("huge_integer_speed", 1.225, 10**400, "speed_m_s"),
        )
        for name, density, speed, parameter in rejected_cases:
            with self.subTest(case=name):
                self._assert_error(
                    density,
                    speed,
                    OverflowError,
                    f"{parameter} is outside the supported float range.",
                )

    def test_avoids_intermediate_overflow_and_underflow(self) -> None:
        """Check exact exponent identities that defeat naive multiplication."""
        cases = (
            ("speed_square_overflows", 2.0**-1000, 2.0**1000, 2.0**999),
            ("reference_speed_square_overflows", 1.0, 2.0**512, 2.0**1023),
            ("halving_density_underflows", 2.0**-1074, 2.0**537, 0.5),
            ("speed_square_underflows", 2.0**1000, 2.0**-600, 2.0**-201),
            ("reference_speed_square_underflows", 2.0**1023, 2.0**-600,
             2.0**-178),
        )
        for name, density, speed, expected in cases:
            with self.subTest(case=name):
                self._assert_value(density, speed, expected)

    def test_preserves_normal_and_subnormal_boundaries(self) -> None:
        """Preserve exact endpoint cases and positive rounded subnormals."""
        minimum_subnormal = float.fromhex("0x1p-1074")
        largest_subnormal = sys.float_info.min - minimum_subnormal
        cases = (
            ("maximum_density", sys.float_info.max, 1.0,
             sys.float_info.max / 2.0),
            ("maximum_result", sys.float_info.max / 2.0, 2.0,
             sys.float_info.max),
            ("minimum_normal_result", 2.0 * sys.float_info.min, 1.0,
             sys.float_info.min),
            ("minimum_normal_from_small_speed", 2.0, 2.0**-511,
             sys.float_info.min),
            ("subnormal_from_minimum_normal_density", sys.float_info.min, 1.0,
             sys.float_info.min / 2.0),
            ("largest_subnormal_result", 2.0 * largest_subnormal, 1.0,
             largest_subnormal),
            ("minimum_subnormal_result", 2.0**-1073, 1.0,
             minimum_subnormal),
            ("minimum_subnormal_from_small_speed", 2.0, 2.0**-537,
             minimum_subnormal),
            ("subnormal_halfway_rounds_to_even", 3.0 * minimum_subnormal, 1.0,
             2.0 * minimum_subnormal),
            ("subnormal_rounds_to_positive_minimum", minimum_subnormal, 1.5,
             minimum_subnormal),
            ("small_speed_rounds_to_positive_minimum", 1.5, 2.0**-537,
             minimum_subnormal),
            ("tiny_density_nonzero_subnormal_result", minimum_subnormal, 2.0,
             2.0 * minimum_subnormal),
        )
        for name, density, speed, expected in cases:
            with self.subTest(case=name):
                self._assert_value(density, speed, expected)

    def test_rejects_unrepresentable_results(self) -> None:
        """Distinguish final overflow from plain ArithmeticError underflow."""
        cases = (
            ("overflow_from_speed", 2.0, 2.0**512, OverflowError,
             "dynamic pressure exceeds the supported float range."),
            ("overflow_from_density", 2.0**1023, 2.0, OverflowError,
             "dynamic pressure exceeds the supported float range."),
            ("half_minimum_subnormal_rounds_to_zero", 2.0**-1074, 1.0,
             ArithmeticError,
             "dynamic pressure underflows to zero for positive inputs."),
            ("small_speed_half_minimum_rounds_to_zero", 1.0, 2.0**-537,
             ArithmeticError,
             "dynamic pressure underflows to zero for positive inputs."),
            ("tiny_positive_result_rounds_to_zero", 1.0, 2.0**-600,
             ArithmeticError,
             "dynamic pressure underflows to zero for positive inputs."),
        )
        for name, density, speed, error_type, message in cases:
            with self.subTest(case=name):
                self._assert_error(density, speed, error_type, message)


if __name__ == "__main__":
    unittest.main()
