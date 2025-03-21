import add #importing add module

print(add.adder(10,20))
print(add.adder(30,40))


# or we can use the following code
from add import adder #importing adder function from add module
from add import * #importing all functions from add module
print(adder(10,20))
