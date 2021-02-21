from pelt import Pelt

tester = Pelt()

def sum(a,b):
    return a + b


"""

tester.test( 50-5, 40 )



tester.describe(
    [
        sum(10,20),
        30,
        "Suma de dos numeros"
    ],
    [
        sum(20, 50),
        70
    ],
    text="HOLA"
)

"""
tester.help()