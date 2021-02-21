from time import perf_counter_ns, perf_counter
from colorama import Fore,init

class Pelt:
    
    init(autoreset=True)

    @staticmethod
    def help():
        print(":::::::::  :::::::::: :::    ::::::::::: \n \
:+:    :+: :+:        :+:        :+:     \n \
+:+    +:+ +:+        +:+        +:+     \n \
+#++:++#+  +#++:++#   +#+        +#+     \n \
+#+        +#+        +#+        +#+     \n \
#+#        #+#        #+#        #+#     \n \
###        ########## ########## ###     \n")

        print("test(func, result, 'Optional Text')")
        
        return 

    @staticmethod
    def test(func,result,text="UNIT TEST"):
        """
        ( sum( 10,20 ) , 30 , "Optional Text" ) => Print a Feedback Of This Unit Test
        """
        start = perf_counter()
        test = func

        print("\n{0} [Finished in: {1}]\n".format( text.upper(), perf_counter_ns() - start ))

        if test == result:
            print(Fore.GREEN + "Success Test \nExpected Value: {0} \nOuput: {1}".format(result,func))
            return

        else:
            print(Fore.RED + "Failed Test \nExpected value: {0} \nOuput: {1}".format(result,func))
            return 

    def describe(self,*tests,text="TESTS GROUP"):

        """
        (
            [ func, result, "Optional Text" ],
            [ func, result, "Optional Text" ],
            text= "Optional Text"
        ) => Print a Test Group  
        """

        print("\n====== {0} ======".format( text.upper()) )

        for i in range(0,len(tests)):

            if len(tests[i]) > 2:
                self.test( tests[i][0],tests[i][1], tests[i][2] )
            
            else:
                self.test( tests[i][0],tests[i][1] )

            print(Fore.LIGHTCYAN_EX + "+--------------------+")


        return
