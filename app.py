import time
from colorama import Fore,init

class Pelt:
    
    init(autoreset=True)

    @staticmethod
    def message(m):
        print(m)
        return 

    @staticmethod
    def test(func,result,text="UNIT TEST"):
        """
        (func, expect)
        """
        print("\n{0} \n".format(text))

        if func == result:
            print(Fore.GREEN + "Success Test \nExpected Value: {0} \nOuput: {1}".format(result,func))
            return

        else:
            print(Fore.RED + "Failed Test \nExpected value: {0} \nOuput: {1}".format(result,func))
            return 