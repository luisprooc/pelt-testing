# Imports
from time import perf_counter_ns, perf_counter
from colorama import Fore,init
from pelt_generator import Generator
from pelt_snap import Snap

# Multi inheritance
class Pelt( Generator,Snap ):
    
    # Run and clear colors of the console
    init(autoreset=True)

    @staticmethod
    def test(func,result,text="UNIT TEST"):
        """
        ( sum( 10,20 ) , 30 , "Optional Text" ) => Print a feedback of this unit test
        """
        # take the time before run the test
        start = perf_counter()
        test = func

        # Print duration of test
        print("\n{0} [🕙 {1}]\n".format( text.upper(), perf_counter_ns() - start ))

        if test == result:
            print(Fore.GREEN + "Success Test \nExpected Value: {0} \nOuput: {1} 🥇".format(result,func))
            return

        else:
            print(Fore.RED + "Failed Test \nExpected value: {0} \nOuput: {1} 💥".format(result,func))
            return 


    @classmethod
    def describe(cls,tests,text="TESTS GROUP"):

        """
        ([
            [ func, result, "Optional Text" ],
            [ func, result, "Optional Text" ],
        ],"Optional Text" ) => Require a matrix  
        """
        print("\n🔍 {0} 🔎".format( text.upper()) )

        # Walk through test matrix
        for i in range(0,len(tests)):

            # If array inside of matrix have more two elements, display with description
            if len(tests[i]) > 2:
                cls.test( tests[i][0],tests[i][1], tests[i][2] )
            
            else:
                cls.test( tests[i][0],tests[i][1] )

            print(Fore.LIGHTCYAN_EX + "➖➖➖➖➖➖➖➖")

        return

    @staticmethod
    def is_equal(test1,test2):

        """
        ( 10, 30 ) => Evaluate if the two values are equal  
        """
        print("\n❕---TEST COMPARISON--- ❕ \n")

        #If test1 and test2 are same, display this
        if test1 == test2:
            print(Fore.GREEN + "{0} AND {1} ARE EQUAL 🥇\n".format( test1, test2 ))

        else: 
            print(Fore.RED + "{0} AND {1} NOT ARE EQUAL 💥\n".format( test1, test2 ))

        return

    @staticmethod
    def not_is_equal(test1,test2):

        """
        ( 10, 30 ) => Evaluate if the two values not are equal  
        """
        print("\n❕---TEST COMPARISON--- ❕ \n")

        #If test1 and test2 not are same, display this
        if test1 != test2:
            print(Fore.GREEN + "{0} AND {1} NOT ARE EQUAL 🥇\n".format( test1, test2 ))

        else: 
            print(Fore.RED + "{0} AND {1} ARE EQUAL 💥\n".format( test1, test2 ))

        return


    @staticmethod
    def is_equal_type(test1,test2):

        """
        ( 10, '30' ) => Evaluate if the two values are equal  
        """
        print("\n❕---TEST TYPE COMPARISON--- ❕ \n")

        #If test1 and test2 are same type, display this
        if type(test1) == type(test2):
            print(Fore.GREEN + "{0} AND {1} ARE THE SAME TYPE 🥇\n".format( test1, test2 ))

        else: 
            print(Fore.RED + "{0} AND {1} NOT ARE THE SAME TYPE 💥\n".format( test1, test2 ))

        return


    @staticmethod
    def not_is_equal_type(test1,test2):

        """
        ( 10, '30' ) => Evaluate if the two values not are equal  
        """
        print("\n❕---TEST TYPE COMPARISON--- ❕ \n")

        #If test1 and test2 are same type, display this
        if type(test1) != type(test2):
            print(Fore.GREEN + "{0} AND {1} NOT ARE THE SAME TYPE 🥇".format( test1, test2 ))

        else: 
            print(Fore.RED + "{0} AND {1} ARE THE SAME TYPE 💥".format( test1, test2 ))

        return


    @staticmethod
    def is_type(value):

        """
        ( '20' ) => Evaluate the type of value  
        """
        print("\n❕---VALUE TYPE--- ❕ \n")
        
        # Convert value for slicing
        test = str( type(value) )

        #Print only the type of test
        print(Fore.LIGHTBLUE_EX + "{0} ⇔ {1}".format( value, test[7:-1] ))
        
        return

    @staticmethod
    def is_none(test):

        """
        (None) => Evaluate if your test return None
        """

        print(Fore.LIGHTBLUE_EX + "\n❕---TEST NONE--- ❕\n")

        #If the test in None, return True
        
        if test == None:
            print(Fore.GREEN + " IS NONE 🥇\n")
            return 

        print(Fore.RED + " NOT IS FALSE 💥\n")
        return

    @staticmethod
    def help():

        """
        Show all functions of Pelt
        """

        # ASCII
        print(Fore.LIGHTGREEN_EX + "             :::::::::  :::::::::: :::    ::::::::::: \n \
            :+:    :+: :+:        :+:        :+:     \n \
            +:+    +:+ +:+        +:+        +:+     \n \
            +#++:++#+  +#++:++#   +#+        +#+     \n \
            +#+        +#+        +#+        +#+     \n \
            #+#        #+#        #+#        #+#     \n \
            ###        ########## ########## ###     \n")

        print("             test     => Print a feedback of this unit test \n \
            describe => Print a feedbacks of the group tests \n \
            is_equal =>  Eval if the two values are equal \n \
            is_equal_type => Eval if the two values are equal \n \
            is_type  => Eval the type of value ")
        
        return 
