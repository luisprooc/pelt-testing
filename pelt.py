from time import perf_counter_ns, perf_counter
from colorama import Fore,init
from pelt_generator import Generator

class Pelt:
    
    init(autoreset=True)

    @staticmethod
    def test(func,result,text="UNIT TEST"):
        """
        ( sum( 10,20 ) , 30 , "Optional Text" ) => Print a feedback of this unit test
        """
        start = perf_counter()
        test = func

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

        for i in range(0,len(tests)):

            if len(tests[i]) > 2:
                cls.test( tests[i][0],tests[i][1], tests[i][2] )
            
            else:
                cls.test( tests[i][0],tests[i][1] )

            print(Fore.LIGHTCYAN_EX + "+--------------------+")

        return

    @staticmethod
    def is_equal(test1,test2):

        """
        ( 10, 30 ) => Eval if the two values are equal  
        """
        print("\n❕---TEST COMPARISON---❕ \n")

        if test1 == test2:
            print(Fore.GREEN + "{0} AND {1} ARE EQUAL 🥇".format( test1, test2 ))

        else: 
            print(Fore.RED + "{0} AND {1} NOT ARE EQUAL 💥".format( test1, test2 ))

        return


    @staticmethod
    def is_equal_type(test1,test2):

        """
        ( 10, '30' ) => Eval if the two values are equal  
        """
        print("\n❕---TEST TYPE COMPARISON---❕ \n")

        if type(test1) == type(test2):
            print(Fore.GREEN + "{0} AND {1} ARE THE SAME TYPE 🥇".format( test1, test2 ))

        else: 
            print(Fore.RED + "{0} AND {1} NOT ARE THE SAME TYPE 💥".format( test1, test2 ))

        return


    @staticmethod
    def is_type(value):

        """
        ( '20' ) => Eval the type of value  
        """
        print("\n❕---VALUE TYPE---❕ \n")

        test = str( type(value) )
        print(Fore.LIGHTBLUE_EX + "{0} ⇔ {1}".format( value, test[7:-1] ))
        
        return

    @staticmethod
    def gt_int(items=1):
        return Generator.generate_int(items)

    
    @staticmethod
    def gt_str(items=1):
        return Generator.generate_str(items)

    
    @staticmethod
    def gt_mix(items=1):
        return Generator.generate_mix(items)

    @staticmethod
    def gt_dict(items=1):
        return Generator.generate_dict(items)

    @staticmethod
    def gt_set(items=1):
        return Generator.generate_set(items)
    
    @staticmethod
    def is_none(test):

        print(Fore.LIGHTBLUE_EX + "\n❕---TEST NONE---❕\n")
        
        if test == None:
            print(Fore.GREEN + " IS TRUE 🥇")
            return 

        print(Fore.RED + " IS FALSE 💥")
        return


    @staticmethod
    def help():

        print(Fore.LIGHTGREEN_EX + " :::::::::  :::::::::: :::    ::::::::::: \n \
:+:    :+: :+:        :+:        :+:     \n \
+:+    +:+ +:+        +:+        +:+     \n \
+#++:++#+  +#++:++#   +#+        +#+     \n \
+#+        +#+        +#+        +#+     \n \
#+#        #+#        #+#        #+#     \n \
###        ########## ########## ###     \n")

        print(" test     => Print a feedback of this unit test \n \
describe => Print a feedbacks of the group tests \n \
is_equal =>  Eval if the two values are equal \n \
is_equal_type => Eval if the two values are equal \n \
is_type  => Eval the type of value ")
        
        return 
