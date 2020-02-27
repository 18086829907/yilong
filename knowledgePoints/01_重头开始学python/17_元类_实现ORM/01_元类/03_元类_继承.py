class A:
    num1 = 100
    num2 = 200

A1 = type('A1', (A,), {})

help(A1)