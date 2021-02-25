from os import name
from pelt import Pelt as p

def sum(a,b):
    return a + b


#p.test(sum(10,20),20)

"""
p.describe([
    [
        sum(10,20),
        30,
        "Suma de dos numeros"
    ],
    [
        sum(20, 50),
        70
    ],
    [
        20 - 30,
        0,
        "Other Test"
    ]
])
"""