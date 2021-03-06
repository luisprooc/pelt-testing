# PELT TESTING

Pelt is a library for testing your algorithms and generate 
various data type for these algorithm of differents ways.

INSTALLATION AND IMPORTATION:

```console
pip install pelt-testing

from pelt import Pelt
```

**Contents:**

- [Basics](#Basics)
- [Generators](#Generators)
- [Snap](#Snap)

---

## Basics

One of functionalities of Pelt, is evaluate your algorithm with differents types of tests. 
Among they are evaluate the type of data, the expected value, if two tests are same type, among others.

### Help

This function provides a summary of all the methods that Pelt has.

*Example:*

```python
Pelt.help()
```

*Output:*


![Pelt Help](screenshots/help.PNG)


### Test

This function represent a unit test, it's the more basic functionality
in Pelt.

*Params: test( function, expected value, optional text)*

```python
Pelt.test(10 + 5, 15)

Output: UNIT TEST [🕙 66275899.9337248]
        Success Test
        Expected Value: 15
        Ouput: 15 🥇

Pelt.test(sum( 20,20 ), 40)

Output: UNIT TEST [🕙 66275899.9337248]
        Success Test
        Expected Value: 40
        Ouput: 40 🥇

Pelt.test(sum( 25,10 ), 30)

Output: UNIT TEST [🕙 66275899.9337248]
        Success Test
        Expected Value: 30
        Ouput: 35 💥 
```

Per default, test() add a example text for your unit test, but also you can 
add a own text.

```python
Pelt.test(mult( 2,10 ), 20,"Multiplication")

Output: MULTIPLICATION  [🕙 66275899.9337248]
        Success Test
        Expected Value: 20
        Ouput: 20 🥇
```


### Describe

This function represent a group of unit tests, it prints a detailed feedback of this tests group
Per default it add a example test, but also you can add a own text.

*Params: describe( matrix, optional text)*

```python
Pelt.describe((
    ( sum(10,20),30 ),
    ( sum(20,20),40, "SUM OF NUMBERS" ),
    ( sum(25,25),55, "INCORRECT SUM OF NUMBERS" ),
),"SUMS")

Ouput: 🔍 SUMS 🔎

        UNIT TEST [🕙 61346599.9386544]

        Success Test 
        Expected Value: 30
        Ouput: 30 🥇
        ➖➖➖➖➖➖➖➖

        SUM OF NUMBERS [🕙 62347999.937653]

        Success Test
        Expected Value: 40
        Ouput: 40 🥇
        ➖➖➖➖➖➖➖➖

        INCORRECT SUM OF NUMBERS [🕙 63402799.936598]

        Failed Test
        Expected value: 55
        Ouput: 50 💥
        ➖➖➖➖➖➖➖➖
```

Without own text and with matrix:

```python
Pelt.describe([
    [ sum(5,5),10 ],
    [ sum(13,12),25, "SUM OF NUMBERS" ]
])

Ouput: 🔍 TESTS GROUP 🔎

        UNIT TEST [🕙 81670499.918331]

        Success Test
        Expected Value: 10
        Ouput: 10 🥇
        ➖➖➖➖➖➖➖➖

        SUM OF NUMBERS [🕙 83254399.9167468]

        Success Test
        Expected Value: 25
        Ouput: 25 🥇
        ➖➖➖➖➖➖➖➖
```


### Is_equal

It compare the type and the value of the two tests introduced, something examples below.

*Params: is_equal( test1, test2 )*

```python
Pelt.is_equal(10, 10)

Output: ❕ ---TEST COMPARISON--- ❕

        10 AND 10 ARE EQUAL 🥇
        10 :: <class 'int'>
        10 :: <class 'int'>

Pelt.is_equal("Javascript","Java")

Ouput:  ❕ ---TEST COMPARISON--- ❕

        Javascript AND Java NOT ARE EQUAL 💥
        Javascript :: <class 'str'>
        Java :: <class 'str'>

Pelt.is_equal(10,"10")

Output: ❕ ---TEST COMPARISON--- ❕

        10 AND 10 NOT ARE EQUAL 💥
        10 :: <class 'int'>
        10 :: <class 'str'>

Pelt.is_equal( [10,20,30],[10,20,"30"] )

Output: ❕ ---TEST COMPARISON--- ❕

        [10, 20, 30] AND [10, 20, '30'] NOT ARE EQUAL 💥
        [10, 20, 30] :: <class 'list'>
        [10, 20, '30'] :: <class 'list'>
```


### Not_is_equal

Contrary to is equal, this function evaluates if the two tests are not of the same type and value.

*Params: not_is_equal( test1, test2 )*

```python
Pelt.not_is_equal([10,20,30],[10,20,"30"])

Ouput:  ❗ ---TEST COMPARISON--- ❗

        [10, 20, 30] AND [10, 20, '30'] NOT ARE EQUAL 🥇
        [10, 20, 30] :: <class 'list'>
        [10, 20, '30'] :: <class 'list'>

Pelt.not_is_equal(10,10)

Ouput:  ❗ ---TEST COMPARISON--- ❗

        10 AND 10 ARE EQUAL 💥
        10 :: <class 'int'>
        10 :: <class 'int'>
```


### Is_equal_type

It compare only the data type between the two tests introduced, In this case the value of data not is important,
something examples below.

*Params: is_equal_type( test1, test2 )*

```python
Pelt.is_equal_type(10,5)

Output: ❕ ---TEST TYPE COMPARISON--- ❕

        10 AND 5 ARE THE SAME TYPE 🥇
        10 :: <class 'int'>
        5 :: <class 'int'>

Pelt.is_equal_type("10",10)

Output: ❕ ---TEST TYPE COMPARISON--- ❕

        10 AND 10 NOT ARE THE SAME TYPE 💥
        10 :: <class 'str'>
        10 :: <class 'int'>

Pelt.is_equal_type("JS","Javascript")

Output: ❕ ---TEST TYPE COMPARISON--- ❕

        JS AND Javascript ARE THE SAME TYPE 🥇
        JS :: <class 'str'>
        Javascript :: <class 'str'>
```


### Not_is_equal_type

Contrary to is equal type, this function evaluates if the two tests are not of the same type, 
the data value not is important.

*Params: not_is_equal_type( test1, test2 )*

```python
Pelt.not_is_equal_type(10, 10)

Output: ❗ ---TEST TYPE COMPARISON--- ❗

        10 AND 10 ARE THE SAME TYPE 💥
        10 :: <class 'int'>
        10 :: <class 'int'>

Pelt.not_is_equal_type((1,4,5), [10,"GO"])

Output: ❗ ---TEST TYPE COMPARISON--- ❗

        (1, 4, 5) AND [10, 'GO'] NOT ARE THE SAME TYPE 🥇
        (1, 4, 5) :: <class 'tuple'>
        [10, 'GO'] :: <class 'list'>
```


### Is_type

It evaluate the type of value of your data or your test.

*Params: is_type( value )*

```python
Pelt.is_type( (1,4,5) ) 

Output: ❕---VALUE TYPE--- ❕

        (1, 4, 5) ⇔ 'tuple'

Pelt.is_type( sum(10,20) )

Output: ❕---VALUE TYPE--- ❕

        30 ⇔ 'int'

Pelt.is_type( {"5",4,5} )

Output: ❕---VALUE TYPE--- ❕ 

        {'5', 4, 5} ⇔ 'set'
```


### Is_none

It evaluate if your test is none or not.

*Params: is_none( test )*

```python
Pelt.is_none( sum(10,20) )

Output: ❕---TEST NONE--- ❕

        NOT IS NONE 💥

Pelt.is_none( None )

Output: ❕---TEST NONE--- ❕

        IS NONE 🥇
```


## Generators 

Pelt also offers various types of test data generators for you to test your 
algorithms and evaluate the result with the data that can be found in Pelt. 
This will prevent you from generating data manually and repetitively. 


### Gt_int

This method generates a random number between 0 and 300, this method can take 
a number as a parameter. If you pass a number as a parameter, this method will 
return you an array of numbers with the length of the parameter you added. 

*Params: gt_int( number ), per default it is 1*

```python
> print( Pelt.gt_int() )

Output: 254

> print( Pelt.gt_int(5) )

Output: [162, 13, 16, 15, 106]

> number_list = Pelt.gt_int(10)

Output: [242, 275, 211, 105, 58, 40, 201, 281, 28, 38]
```

_Now we are going to use it in our software:_

```python
def sum(a,b):
    return a + b, ( a,b ) 

print( sum( Pelt.gt_int(),Pelt.gt_int() ))

Output: (78, (61, 17)) => result: 78, a: 61, b: 17

〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰

def div(a,b):
    return a / b, ( a,b ) 

print( div( Pelt.gt_int(),Pelt.gt_int() ))

Output: (2.456896551724138, (285, 116)) => result: 2.456896551724138, a: 285, b: 116

〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰

def duplicate_list(list):

    duplicate = []
    for i in list:
        duplicate.append( i * 2)

    return duplicate, list

print( duplicate_list( Pelt.gt_int(5) ))

Output: ([416, 226, 362, 296, 512], [208, 113, 181, 148, 256])

〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰

>> More Advance 

def duplicate_list(list):
    
    duplicate = [ i * 2 for i in list]

    return duplicate, list

print( duplicate_list( Pelt.gt_int(12) ))

Output: ([396, 154, 354, 530, 224, 480, 192, 196, 180, 452, 120, 24], [198, 77, 177, 265, 112, 240, 96, 98, 90, 226, 60, 12])

〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰

number_list = Pelt.gt_int(4)

print( list( map( lambda x: x * 2, number_list )), number_list )

Output: [330, 142, 180, 564] [165, 71, 90, 282]
```


### Gt_str

It has a similar behavior to gt_int, basically its difference
It is that this function generates a string randomly and gt_int an integer.

*Params: gt_str( number ), per default it is 1*

```python
> print( Pelt.gt_str() )

Output: injected

> print( Pelt.gt_str(4) )

Output: ['Lorem', 'qwertyuytr', 'p', 'occaecat']

〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰

def inject_py(string):

    return "{}py ".format( string ) 

print( inject_py(Pelt.gt_str()) )

Output: nullapy 

〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰

def duplicate_string(string):

    return list( map(lambda x: x * 2,string) ) 

print( duplicate_string(Pelt.gt_str(4)) )

Output: ['IpsumIpsum', 'consecteturconsectetur', 'fugiatfugiat', 'injectedinjected']
```


### Gt_mix

As its name implies, mix returns a number or a string randomly. If you pass a number as a parameter, 
it can return an list with numbers and strings.

*Params: gt_mix( number ), per default it is 1*

```python
> print( Pelt.gt_mix() )

Output: 248

> print( Pelt.gt_mix(5) )

Output: ['since', 'standard', 267, 285, 'Excepteur']
```

Remember, you can combine generators with tests:

```python
# As the tests have return a print built in, it is not necessary to put them in your function

def type_data(data):

    return Pelt.is_type(data)

type_data( Pelt.gt_mix() )

Output: ❕---VALUE TYPE--- ❕

        Latin ⇔ 'str'

〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰

def equal_values(value1,value2):

    return Pelt.is_equal_type(value1,value2)

equal_values( Pelt.gt_mix(),Pelt.gt_mix() )

Output: ❕---TEST TYPE COMPARISON--- ❕

        PowerUp AND 169 NOT ARE THE SAME TYPE 💥
        PowerUp :: <class 'str'>
        169 :: <class 'int'>
```


### Gt_dict

This generator return a random dictionary with random keys and values, 
per deafult not return nested dictionaries, but you can custom the dictionarys
combining the others generators.

*Params: gt_dict( number ), per default it is 1*

```python
> print( Pelt.gt_dict() )

Output: {'looks': 155}

# You can also create a custom dictionary, depending on your need.

multy_dict = {
    Pelt.gt_str(): Pelt.gt_mix(5)
}

> print(multy_dict)

Output: {'looks': ['words', 5, 115, 102, 'PowerUp']}

multy_dict = {
    Pelt.gt_int(): Pelt.gt_dict(4), 
    Pelt.gt_str(): Pelt.gt_str(5)
}

> print(multy_dict)

Output: {22: {296: 'dolor', 'qwertyuytr': 298, 75: 'standard', 'words': 'p'}, 
        'Ors': ['PowerUp', 'Finibus', 'injected', 'fugiat', 'therefore']}
```


### Gt_set

This generator return a random set, it has a similar behavior that the others,
some examples below:

*Params: gt_set( number ), per default it is 1*

```python
> print( Pelt.gt_set(5) )

Output: {136, 200, 'Cors-c', 277, 120}

def joiner(value):

    example = {"example",1,2}
    return value.union(example) 

print( joiner(Pelt.gt_set(4)) )

Output: {1, 2, 'ghorlayck', 'example', 201, 283, 'injected'}
```


## Snap

After learning the functionality of the generators, surely you would have liked that 
said test data could have it in a separate flow to test and to better predict the result of your algorithms.
Now we are going to unleash all the power that Pelt can offer, with the snap functions we can archive test data 
and test it later with a much more predictable result, allowing you to use the tests in a more efficient way.

**NOTE: SNAPS ONLY RECEIVE A GENERATORS**

### Snap_take

This function creates a file with the generated data that you passed to the function, you must pass it the 
name you want for your file, if you passed it the name of an existing file it will overwrite the data.

*Params: Pelt.snap_take( "file name", ( Generators, Generators, ... ) ) => Require a matrix*

```python
Pelt.snap_take("Data", (
    Pelt.gt_int(5), Pelt.gt_str(4)
))
```


![Pelt Snap_take](screenshots/snaps.PNG)


```python
def duplicate(numbers):
    return list(map( lambda x: x *2, numbers))


data = Pelt.gt_int(5)

Pelt.snap_take("Data",(
    duplicate(data), data
))
```


![Pelt Snap_take](screenshots/take.PNG)


### Snap_rm

This function creates a file with the generated data that you passed to the function, you must pass it the 
name you want for your file, if you passed it the name of an existing file it will overwrite the data.

*Params: Pelt.snap_rm( "file name" )*

```python
Pelt.snap_rm("Data")
```

It removes a file generate with these name.


### Snap_rm_all

This function remove all files generated with snap.

*Params: Pelt.snap_rm_all()*

```python
Pelt.snap_rm_all()
```

