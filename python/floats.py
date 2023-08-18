import math
from typing import Union

# region equity
"""
With decimals, we have the problem with infinite numbers such as
π = 22/7 = 3.1415926535...
So this number we can not write it on its exact value, just an
approximation of its value. With binary numbers, we also have this
problem.
Take the example of 1/10, this, in decimal we can represent as 0.1, and
it is the exact value, but in binary we can represent it as
0.0001100110011..., so we do not have an exact value for it as this
number goes on infinitely. Because of it, we do not have an exact value
for this number using computers since computers work with binary
numbers.
In any programming language, we don't have infinite numbers. All numbers
are finite. Even if, in reality, the number is infinite, with computers,
they need to be represented, so they need to be finite.
"""

print(f'{0.1:.25f}')

x = 0.1 + 0.1 + 0.1
y = 0.3

print(x == y)
print(f'{x:.25f}')
print(f'{y:.25f}')

# When sending to round, it virtually stores 0.3, meaning it is saving
# 0.2999999999999999888977698 in memory and not the sum of 0.1. So this
# is not a good option to fix the problem.
x = round(0.1 + 0.1 + 0.1, 5)
y = round(0.3, 5)

print(x == y)
print(f'{x:.25f}')
print(f'{y:.25f}')

"""
We have one good way to compare this, taking the difference (Δ) between
two values and checking if this difference is smaller than our
tolerance (`ε`).
With that in mind the condition to `a` be equal to `b` is that the
absolute difference from the values (|`a` - `b`| or fabs(`a` -`b`)) is
smaller than our tolerance (`ε`).
The formula:
ε > 0;
a = b if |a - b| < ε;

This formula can be used with two types of value for the tolerance (ε),
a absolute value or a relative value, but we have a problem when the
difference (Δ) changes from close to zero to far from zero and vice
versa.

With absolute tolerance we have the problem that as the magnitude of the
number increases the tolerance don't, so what would be considered close
on a smaller number is not considered close on a larger number.
With relative tolerance we have the problem that to numbers close to
zero it, probably, never works since the relative tolerance will always
be lesser than the number itself.

To solve this problem we can combine to the options and get the number
that is further away from zero as the tolerance (ε).
The function `isclose` from math module has this solution already
implemented. With this function the default value to `rel_tol` is 1e-9
and default value to `abs_tol` is 0, so if you do not specify the value
to abs_tol you are using only relative tolerance.

The use case for all these three examples should be used as the
necessity. One example is comparing monetary values, you would only
use the `abs_tol` from the function with the value of 1e-3 so the cents
will be checked, if you use `rel_tol` with this value, for greater
numbers (take 30000 for example) $30 will be in the range of the
comparison so this $30 will not count for the equity.
"""
print('--------------------------Absolute tolerance--------------------------')
EPSILON = 1e-15

x = 0.1 + 0.1 + 0.1
y = 0.3
delta = math.fabs(x - y)

print(delta < EPSILON)
print(f'{delta:.25f}')
print(f'{EPSILON:.25f}')

print('-----------------------------------')
a = 10000.1 + 10000.1 + 10000.1
b = 30000.3
delta2 = math.fabs(a - b)

print(delta2 < EPSILON)
print(f'{delta2:.25f}')
print(f'{EPSILON:.25f}')

print('--------------------------Relative tolerance--------------------------')
x = 1e-10
y = 0

relative_tolerance = 1e-3  # = 0.001 = 0.1%
EPSILON = relative_tolerance * max(math.fabs(x), math.fabs(y))

delta = math.fabs(x - y)

print(delta < EPSILON)
print(f'{delta:.25f}')
print(f'{EPSILON:.25f}')

print('--------------------------Combined tolerance--------------------------')
x = 1e-10
y = 0

relative_tolerance = 1e-3  # = 0.001 = 0.1%
absolute_tolerance = 1e-5
EPSILON = max(relative_tolerance * max(math.fabs(x), math.fabs(y)),
              absolute_tolerance)

delta = math.fabs(x - y)

print(delta < EPSILON)
print(f'{delta:.25f}')
print(f'{EPSILON:.25f}')

print('-----------------------isclose function-----------------------')

print(math.isclose(a=10000.01 + 10000.01 + 10000.01, b=30000.03,
                   rel_tol=1e-3, abs_tol=1e-3))
print(math.isclose(a=0.01 + 0.01 + 0.01, b=0.03,
                   rel_tol=1e-3, abs_tol=1e-3))

print(math.isclose(a=10000.01 + 10000.01 + 10000.01, b=30040.03,
                   rel_tol=1e-3, abs_tol=1e-3))
print(math.isclose(a=0.01 + 0.01 + 0.01, b=0.04,
                   rel_tol=1e-3, abs_tol=1e-3))
# endregion
# region rounding
"""
We use the round built-in function to round the number to a specified
precision. The first argument being the number to be rounded and the
second argument being the precision. To round at a float precision we
use positive precision and to round at integer precision we use a
negative precision. Using 0 as precision (or not specifying) our
precision will be at the unit position of the integer.

When it come to ties the round function uses the Banker's Rounding that
rounds to the nearest value with an even digit.
E.g., 0.5 with precision 0 will be rounded to 0.
E.g., 1.5 with precision 0 will be rounded to 2.
E.g., 2.5 with precision 0 will be rounded to 2.

It is basically used to avoid biases. Taking the example from above, if
we average those numbers we can take the reason behind this.
No rounding: 0.5 + 1.5 + 2.5 / 3 = 1.5
Rounding away from zero: 1 + 2 + 3 / 3 = 2
Banker's Rounding: 0 + 2 + 2 / 3 = 1.3333...

Using last one the value become more closer from the real one, taking
account the amount of transactions, so it is less biased. But if is
needed to round away from zero you can use Decimal class from decimal
module or write your own function.
"""
print(round(10.26, 1))
print(round(10053, -1))


def round_integers_away_from_zero(number: Union[int, float]) -> int:
    """
    In this function, we copy the sign from the number to 0.5, and we
    add it to the number, and we truncate the resulting value using the
    int constructor.
    This is a good function to round integers away from zero that works
    properly with negative and positive numbers.
    """
    return int(number + math.copysign(0.5, number))


print(round_integers_away_from_zero(-12.5))

"""
Since we have the problem of infinite representations with floats, round
may run into issues. If exact representations are needed, using the
Decimal class is recommended since there has multiple rounding
techniques.
"""
print(round(1.85, 1))
print(f'{round(1.85, 1):.25f}')

print(round(1.95, 1))
print(f'{round(1.95, 1):.25f}')
# endregion
