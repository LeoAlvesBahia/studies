import decimal
import math
from decimal import Decimal
# region contexts
"""
The Decimal class should be used when we need the precision that floats
can't provide. When we import the decimal module, it comes with some
default settings that can be accessed and modified. The decimal module
also implements a context manager which we can use to create a secondary
set of settings which won't interfere with the global settings.
Something to keep in mind while changing the settings from the context
is that the precision affects the mathematical operations but it does
not affect the constructor.
"""
decimal_context = decimal.getcontext()
print('Global context')
print(decimal_context)


decimal_context.prec = 2
decimal_context.rounding = decimal.ROUND_HALF_UP
decimal.setcontext(decimal_context)
print('Modified global context')
print(decimal.getcontext())

# Setting the context as the default back
decimal.setcontext(decimal.DefaultContext)
print('Global context back to default')
print(decimal.getcontext())

print('Decimal instanced as float')
x = Decimal(1.25)
print(x)
print('Decimal instanced as string')
x = Decimal('1.25')
print(x)
print('Decimal instanced as float')
y = Decimal(1.35)
print(y)
print('Decimal instanced as string')
y = Decimal('1.35')
print(y)
# Creating a local context with previously modified context from decimal
with decimal.localcontext(decimal_context):
    print('Rounding using local context with ROUND_HALF_UP')
    print(round(x, 1))
    print(round(y, 1))
    print(decimal.getcontext())

print('Rounding using global context with ROUND_HALF_EVEN')
print(round(x, 1))
print(round(y, 1))
print(decimal.getcontext())

with decimal.localcontext(decimal_context) as d_ctx:
    """
    One thing to keep in mind about the prec attribute from the context
    is that it evaluates considers the total number of digits of a
    number.
    If we want to keep always x numbers of decimals places after a
    certain number we should use other ways to to this, like the
    quantize() method and it will apply the round method chose from the 
    context.
    """
    a = Decimal('1.23456789')
    b = Decimal('9.87654321')
    print(a)
    print(b)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(decimal.getcontext())
    d_ctx.prec = 14
    print((a + b).quantize(Decimal('0.00')))
    print((a - b).quantize(Decimal('0.00')))
    print((a * b).quantize(Decimal('0.00')))
    print((a / b).quantize(Decimal('0.00')))
# endregion
# region operations
"""
When using Decimal class we should use the operations from it since if
we use the operations from math module it will cast it to float and the
precision from the Decimal class will be lost.
"""
x = 0.01
x_dec = Decimal('0.01')

print(f'{math.sqrt(x):.25f}')
print(f'{math.sqrt(x_dec):.25f}')
print(f'{x_dec.sqrt():.25f}')

print(f'{(math.sqrt(x) * math.sqrt(x)):.25f}')
print(f'{(math.sqrt(x_dec) * math.sqrt(x_dec)):.25f}')
print(f'{(x_dec.sqrt() * x_dec.sqrt()):.25f}')
# endregion
