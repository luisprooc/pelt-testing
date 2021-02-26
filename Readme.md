# PELT TESTING

Pelt is a library for testing your algorithms and generate 
various data type for these algorithm of differents ways.

## Usage

### Help

This function provides a summary of all the methods that Pelt has.

*Example:*

`
Pelt.help()
`

*Output:*


![Pelt Help](screenshots/help.PNG)


### Test

This function represent a unit test, it's a more basic functionality
in Pelt.

*Params: test( function, expected value, optional text)*

```
Pelt.test(10 + 5, 15)

output: UNIT TEST [🕙 66275899.9337248]
        Success Test
        Expected Value: 15
        Ouput: 15 🥇

Pelt.test(sum( 20,20 ), 40)

output: UNIT TEST [🕙 66275899.9337248]
        Success Test
        Expected Value: 40
        Ouput: 40 🥇

Pelt.test(sum( 25,10 ), 30)

output: UNIT TEST [🕙 66275899.9337248]
        Success Test
        Expected Value: 30
        Ouput: 35 💥 
```

Per default, test() add a example text for your unit test, but also you can 
add a own text.

```
Pelt.test(mult( 2,10 ), 20,"Multiplication")

output: MULTIPLICATION  [🕙 66275899.9337248]
        Success Test
        Expected Value: 20
        Ouput: 20 🥇
```