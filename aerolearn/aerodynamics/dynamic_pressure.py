"""Compute scalar dynamic pressure from local density and relative flow speed."""

import math


def _validated_float(value: float, parameter_name: str) -> float:
    """Validate one exact built-in numeric value before converting it to float."""
    if type(value) is not int and type(value) is not float:
        raise TypeError(
            f"{parameter_name} must be a built-in int or float "
            "(bool is not accepted)."
        )
    if value < 0:
        raise ValueError(f"{parameter_name} must be finite and non-negative.")

    try:
        converted = float(value)
    except OverflowError:
        raise OverflowError(
            f"{parameter_name} is outside the supported float range."
        ) from None

    if not math.isfinite(converted):
        raise ValueError(f"{parameter_name} must be finite and non-negative.")
    return converted


def dynamic_pressure(density_kg_m3: float, speed_m_s: float) -> float:
    """Return dynamic pressure in pascals using q = 0.5 * density * speed**2.

    Args:
        density_kg_m3: Local mass density in kg/m^3.
        speed_m_s: Relative flow-speed magnitude in m/s for the same flow state.

    Exact built-in int and float values are accepted; bool and numeric subclasses
    are rejected. Density is validated before speed, including negativity before
    integer conversion. Both inputs must be finite and nonnegative after float
    conversion. Integer conversion can round. There are no default densities or
    unit conversions.

    Returns:
        A finite float in Pa. Valid zero inputs, including signed zero, return
        positive 0.0 after both inputs are validated. Nonzero subnormals are
        accepted. This function performs no input/output operations.

    Raises:
        TypeError: An argument is not an exact built-in int or float.
        ValueError: An argument is negative or non-finite.
        OverflowError: An integer cannot convert to float, or the computed
            scaled result overflows or is non-finite.
        ArithmeticError: The computed result is zero despite positive inputs.

    Scaling avoids intermediate exponent overflow and premature underflow.
    Mantissa multiplication still rounds; correctly rounded results and exact
    classification near floating-point endpoints are not guaranteed. Dynamic
    pressure is not generally a Pitot or stagnation-minus-static pressure.
    See docs/science/dynamic_pressure.md for assumptions and limitations.
    """
    density = _validated_float(density_kg_m3, "density_kg_m3")
    speed = _validated_float(speed_m_s, "speed_m_s")

    if density == 0.0 or speed == 0.0:
        return 0.0

    density_mantissa, density_exponent = math.frexp(density)
    speed_mantissa, speed_exponent = math.frexp(speed)
    mantissa_product = (density_mantissa * speed_mantissa) * speed_mantissa
    exponent = density_exponent + 2 * speed_exponent - 1

    try:
        pressure = math.ldexp(mantissa_product, exponent)
    except OverflowError:
        raise OverflowError(
            "dynamic pressure exceeds the supported float range."
        ) from None

    if not math.isfinite(pressure):
        raise OverflowError("dynamic pressure exceeds the supported float range.")
    if pressure == 0.0:
        raise ArithmeticError(
            "dynamic pressure underflows to zero for positive inputs."
        )
    return pressure
