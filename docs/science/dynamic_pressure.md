# Dynamic pressure: scientific and numerical contract

## Equation, quantities, and SI units

The public scalar calculation is

\[
q = \frac{1}{2}\rho V^2.
\]

| Symbol | Quantity | Input/output unit |
| --- | --- | --- |
| `rho` | Local fluid mass density | kg/m³ |
| `V` | Local bulk speed magnitude in the chosen reference frame | m/s |
| `q` | Dynamic pressure | Pa |

Dimensional analysis gives

\[
[q] = (\mathrm{kg\,m^{-3}})(\mathrm{m^2\,s^{-2}})
     = \mathrm{kg\,m^{-1}\,s^{-2}}
     = \mathrm{N\,m^{-2}} = \mathrm{Pa}.
\]

Dynamic pressure is a kinetic-energy-per-volume scale. Both inputs must describe
the same local flow state. For aircraft applications, use air-relative speed
rather than ground speed when wind is present. Freestream dynamic pressure uses
the corresponding freestream density and speed. The function supplies no default
density and infers no altitude, temperature, pressure, or Mach number.

The definition is useful in compressible and viscous flows as well as
incompressible flows; NASA explicitly distinguishes that general use from its
simple incompressible derivation. It does not alone compute a force, a pressure
distribution, or a flow solution. See
[NASA Glenn: Dynamic Pressure](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/dynamic-pressure/).

## Distinguishing pressure quantities

| Quantity | Meaning |
| --- | --- |
| Static pressure, `p` or `p_s` | Local thermodynamic pressure. |
| Dynamic pressure, `q` | The defined quantity `rho * V² / 2`. |
| Stagnation/total pressure, `p_t` | Pressure obtained by bringing a specified local flow state to rest isentropically. |
| Impact pressure | A Pitot/stagnation-to-static pressure difference, generally different from `q` in compressible flow. |

The familiar relation `p_t = p_s + q` is the incompressible Bernoulli relation.
A sufficient set of conditions is steady, inviscid, incompressible flow along a streamline,
negligible elevation change, and no heat or shaft-work contribution. A common
constant across different streamlines needs additional conditions, such as
irrotational flow. These restrictions apply to that pressure relation, not to
the definition of `q`. See
[NASA Glenn: Bernoulli's Equation](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/bernoullis-equation/).

For explanation only, a calorically perfect gas gives

\[
q = \frac{\gamma}{2}pM^2,
\qquad
\frac{p_t}{p} =
\left(1 + \frac{\gamma-1}{2}M^2\right)^{\gamma/(\gamma-1)},
\]

where the second relation assumes isentropic stagnation. Thus `p_t - p` generally
differs from `q`; their leading low-Mach terms agree. A low-Mach approximation
depends on the acceptable error, not an exact cutoff in the dynamic-pressure
definition. This API does not calculate Mach number or stagnation pressure. See
[NASA Glenn: Isentropic Flow Equations](https://www.grc.nasa.gov/www/k-12/airplane/isentrop.html).

A Pitot-static instrument measures pressures. Its incompressible interpretation
has limitations. In supersonic flow a shock ahead of the probe changes total
pressure, so the measured Pitot pressure is not simply the upstream stagnation
pressure. Shock and instrument corrections are outside this calculation. See
[NASA Glenn: Pitot-Static Tube](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/pitot-static-tube-speedometer/)
and [NASA Glenn: Normal Shock Wave Equations](https://www.grc.nasa.gov/www/k-12/airplane/normal.html).

## Public API and usage

Canonical import and signature:

```python
from aerolearn.aerodynamics.dynamic_pressure import dynamic_pressure

# Signature: dynamic_pressure(density_kg_m3: float, speed_m_s: float) -> float
pressure_pa = dynamic_pressure(density_kg_m3=1.225, speed_m_s=100.0)
# pressure_pa is approximately 6125 Pa; no fixed decimal rounding is applied.

exact_binary_case_pa = dynamic_pressure(2, 3)  # 9.0 Pa
zero_pa = dynamic_pressure(-0.0, 100.0)  # positive float 0.0
```

Use the repository root as the working directory. No package installation is
required. The function returns a finite nonnegative built-in `float`, including
accepted nonzero subnormal results. It performs no printing, user input, file
access, unit conversion, or mutation of global state. The console banner and
`main.py` remain independent of this scientific API.

## Input validation and exact exceptions

Only exact built-in `int` and `float` objects are accepted. `bool` is rejected,
despite being an `int` subclass in Python. Strings, `None`, complex numbers,
`Decimal`, `Fraction`, containers, and all numeric subclasses are rejected.
The type annotations do not authorize other numeric protocols or conversions.
The implementation checks type identity, not overloaded class equality.

Validation completes for `density_kg_m3` first, then for `speed_m_s`. For each
parameter, the order is exact-type check, negativity check, conversion of a
nonnegative built-in integer to `float` if needed, then the finiteness check.
Negative integers are therefore rejected before conversion, including integers
too large in magnitude to convert to a finite float. Negative infinity is
negative and non-finite; either property maps to the same `ValueError` message.

In the table below, replace `P` with the complete parameter name
`density_kg_m3` or `speed_m_s`.

| Condition | Exact exception class | Complete message |
| --- | --- | --- |
| Unsupported type | `TypeError` | `P must be a built-in int or float (bool is not accepted).` |
| Negative input, NaN, or infinity | `ValueError` | `P must be finite and non-negative.` |
| Nonnegative integer cannot convert to a supported finite float | `OverflowError` | `P is outside the supported float range.` |
| Scaled calculation overflows or produces a non-finite result | `OverflowError` | `dynamic pressure exceeds the supported float range.` |
| Positive validated inputs produce a result rounded to zero | Plain `ArithmeticError` | `dynamic pressure underflows to zero for positive inputs.` |

Plain `ArithmeticError` means the exception's exact class is `ArithmeticError`,
not its subclass `OverflowError`. Messages include the final period.

Both parameters are validated before any zero shortcut. For example:

| Call | Required outcome |
| --- | --- |
| `dynamic_pressure(0.0, True)` | `TypeError`: `speed_m_s must be a built-in int or float (bool is not accepted).` |
| `dynamic_pressure(0.0, float("inf"))` | `ValueError`: `speed_m_s must be finite and non-negative.` |
| `dynamic_pressure(-1, "bad")` | `ValueError`: `density_kg_m3 must be finite and non-negative.` |
| `dynamic_pressure(True, -1)` | `TypeError`: `density_kg_m3 must be a built-in int or float (bool is not accepted).` |
| `dynamic_pressure(-(2**1024), 0.0)` | `ValueError`: `density_kg_m3 must be finite and non-negative.` |
| `dynamic_pressure(2**1024, 0.0)` | `OverflowError`: `density_kg_m3 is outside the supported float range.` |

All valid zero cases, including input `-0.0`, return positive float `0.0`.
Accepting zero density is an explicit mathematical boundary convention; it does
not assert the existence of a continuum fluid state in a vacuum. Speed is a
magnitude, so negative speeds are invalid even though a signed velocity
component can be negative in a different API.

## Floating-point strategy and limitations

Nonnegative integers are converted to floats before calculation. Integers need
not be exactly representable: conversion can round large integers. The accepted
integer domain is those values whose conversion yields a finite float; it is
not an arbitrary-precision integer calculation. This input limit applies even
when multiplying by a sufficiently small speed would make the mathematical
final result representable.

For positive validated floating-point inputs, `math.frexp` gives

```text
rho = m_rho * 2**e_rho
V   = m_v   * 2**e_v
q   = ((m_rho * m_v) * m_v) * 2**(e_rho + 2*e_v - 1)
```

Each positive mantissa is at least `0.5` and below `1.0`. The implementation
uses the fixed multiplication order `(m_rho * m_v) * m_v`, then one
`math.ldexp` scaling step. The bounded mantissa product avoids premature
overflow from squaring a large speed and premature underflow from squaring a
small speed or halving a tiny density. See the official
[`math.frexp`](https://docs.python.org/3.14/library/math.html#math.frexp) and
[`math.ldexp`](https://docs.python.org/3.14/library/math.html#math.ldexp)
documentation.

The final scaling can still overflow or round a positive value to zero; the
exceptions above make these outcomes explicit. A nonzero subnormal result is
accepted, without a guaranteed relative precision. There is no fixed decimal
rounding and no `Fraction` fallback in production.

This is ordinary finite-precision arithmetic, not an exactly rounded or
arbitrary-precision evaluation. Input conversion and the two multiplications
can round. Very near the largest finite value or the zero/subnormal boundary,
these roundings can affect the final value and whether overflow or underflow is
reported. The contract does not classify every exact real result at those
endpoints using unlimited precision. Four-ULP checks on selected normal cases
are verification tolerances, not a universal error bound. See
[Python's floating-point limitations](https://docs.python.org/3.14/tutorial/floatingpoint.html)
and [`sys.float_info`](https://docs.python.org/3.14/library/sys.html#sys.float_info).

## Independent reference and boundary cases

The following values are independently derived specification targets, not an
execution log. Normal decimal reference values may require the approved
four-ULP tolerance because decimal inputs such as `1.225` first round to binary
floats. Exactly representable binary cases use exact comparison.

For example, nominal density `1.225 = 49/40` gives
`(49/80) * 10000 = 6125 Pa` at `100 m/s`, and
`(49/80) * 2500 = 1531.25 Pa` at `50 m/s`. These are independent rational
derivations, not values obtained by calling the production function.

| Density, kg/m³ | Speed, m/s | Expected dynamic pressure, Pa | Purpose |
| --- | --- | --- | --- |
| `1.225` | `100` | Approximately `6125` | Ordinary engineering reference. |
| `1.225` | `50` | Approximately `1531.25` | Independent decimal reference. |
| `2` | `3` | `9` | Exact integer reference. |
| `0.5` | `0.5` | `0.0625` | Exact fractional binary reference. |
| `0` | `100` | Positive `0.0` | Zero-density boundary. |
| `1.225` | `0` | Positive `0.0` | Zero-speed boundary. |
| `1.25` | `8` | `40` | Scaling baseline. |
| `2.5` | `8` | `80` | Doubling density doubles `q`. |
| `0.625` | `8` | `20` | Halving density halves `q`. |
| `1.25` | `16` | `160` | Doubling speed multiplies `q` by four. |
| `1.25` | `24` | `360` | Tripling speed multiplies `q` by nine. |

The boundary table assumes the intended IEEE 754 binary64 environment, with
53 significant binary digits and smallest normal value `2**-1022`. Define
`s = 2**-1074`, the smallest positive subnormal float, and
`F = sys.float_info.max`, the largest finite float. Negative powers here denote
exact real powers of two used to specify representable float inputs, not
integer exponentiation in production code.
For density `2**a` and speed `2**b`, the reference exponent is `a + 2*b - 1`.

| Density | Speed | Expected outcome | Purpose |
| --- | --- | --- | --- |
| `1` | `2**512` | `2**1023` | Avoid intermediate square overflow. |
| `2**1023` | `2**-600` | `2**-178` | Avoid intermediate square underflow. |
| `s` | `2` | `2*s` | Avoid premature underflow from halving density. |
| `F/2` | `2` | `F` | Preserve the largest finite endpoint in this exact case. |
| `2` | `2**-511` | `2**-1022` | Preserve the smallest positive normal float. |
| `2` | `2**-537` | `s` | Preserve the smallest positive subnormal float. |
| `3*s` | `1` | `2*s` | Exact `1.5*s` rounds to even subnormal `2*s`. |
| `1.5` | `2**-537` | `s` | Exact `0.75*s` rounds to nonzero `s`. |
| `2` | `2**512` | Result `OverflowError` | Exact mathematical result is `2**1024`. |
| `1` | `2**-537` | Plain `ArithmeticError` | Exact `2**-1075` rounds to zero at the half-subnormal tie. |
| `1` | `2**-600` | Plain `ArithmeticError` | Exact positive `2**-1201` rounds to zero. |
| Integer `2**1024` | `2**-600` | Density input `OverflowError` | Conversion fails even though the mathematical final value `2**-177` is finite. |

Selected non-boundary floating-point checks use an independent `Fraction`
oracle in tests: convert each accepted float to its exact rational value,
evaluate the defining equation using rational arithmetic, and compare the
float result with the stated tolerance. This does not reuse the production
mantissa/exponent algorithm. Reference values, scaling invariants, validation
order, complete exception messages, positive zero, and the absence of stdout
and stderr output are separate test obligations.

## Validity, verification, and acceptance

Physical validity and numerical representability are separate. This scalar
model uses ordinary nonrelativistic continuum-fluid interpretation and cannot
detect inconsistent units, an inappropriate reference frame, an unrealistic
supplied density, rarefied-flow effects, or measurement error. Finite accepted
inputs are not a guarantee that a proposed physical state is realizable.

Numerical verification checks implementation behavior against independent
arithmetic references, boundary cases, and invariants. It does not constitute
experimental validation against measured flow data, establish sensor accuracy,
or certify an operational aerospace tool. No experimental validation or
operational certification is claimed.

Actual execution environments, results, and acceptance gates belong in
[`PROJECT_STATUS.md`](../../PROJECT_STATUS.md). Windows M2 testing, published
M2 CI verification, and owner acceptance must be evidenced separately before
the milestone is closed. The historical `lesson1.py` draft is unavailable in
the approved baseline and is not validation evidence for this implementation.
