from package import Pelt

def sum(a,b):
    return a + b

Pelt.describe([
    [ sum(5,5),10 ],
    [ sum(13,12),25, "SUM OF NUMBERS" ]
])