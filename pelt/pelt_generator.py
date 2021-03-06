from random import randint

class Generator:

    @staticmethod
    def gt_int( items=1 ):

        """
        () => Return a random number
        (5) => Return a list of length specified with random numbers
        """

        #If items is less two, return one random number
        
        if items <= 1:
            return randint( 0,300 )


        # List comprehensions, when index reach the value of items, return a number list random 
        return [ randint(0,300) for i in range(0,items) ]

    @staticmethod
    def gt_str( items =1 ):

        """
        () => Return a random string
        (5) => Return a list of length specified with random strings
        """ 

        # Dictionary with strings of example
        str_dict = {
            1:"Lorem", 2: "Ipsum", 3:"dolor", 4:"amet", 5:"consectetur", 
            6:"fugiat", 7:"nulla", 8:"Excepteur", 9:"occaecat", 10:"proident",
            11:"generator", 12:"combined", 13:"looks", 14:"reasonable", 15:"therefore",
            16:"injected", 17:"words", 18:"standard",19:"since", 20:"Finibus",
            21:"Latin", 22:"Hals", 23:"qwertyuytr", 24:"jurlisrr", 25:"ghorlayck",
            26:"Ors", 27:"Cors-c", 28:"PowerUp", 29:"p", 30:"Ha",
            31:"GO", 32:"Golang", 33:"PY", 34:"Python", 35:"Java",
            36:"JS", 37:"Javascript", 38:"Rust", 39:"RS", 40:"Clojure",
            41:"Perl", 42:"HTML", 43:"CSS", 44:"TS", 45:"Typescript",
            46:"C++", 47:"C", 48:"C#", 49:"Pascal", 50:"Arduino"
        }
        
        if items <= 1:
            return str_dict[randint( 1,len(str_dict) )]

        # List comprehensions, when index reach the value of items, return a string list random 
        return [ str_dict[ randint(1, len(str_dict)) ] for i in range(0,items) ]

    @classmethod
    def gt_mix( cls,items=1 ):

        """
        () => Return a number or string random
        (5) => Return a list of length specified with numbers and strings random
        """

        if items <= 1:
            mix = randint(0,1)

            #When mix if 1, return a number
            if mix:
                return cls.gt_int(1)

            else:
                return cls.gt_str(1)

        else:

            # We Define a list
            list = []

            for i in range(0,items):
                mix = randint(0,1)

                # If in this turn mix is 1, generate a random number and add it the list
                if mix:
                    list.append( cls.gt_int(1) )

                else:
                    list.append( cls.gt_str(1) )

            return list


    @classmethod
    def gt_dict( cls,items=1 ):

        """
        () => Return a random dictionary with length 1
        (5) => Return a random dictionary with length specified
        """

        # Generate a random dictionary with mix key and values
        return { cls.gt_mix(1):cls.gt_mix(1) for i in range(0,items) }

    @classmethod
    def gt_set( cls,items =1):

        """
        () => Return a random set with length 1
        (5) => Return a random set with length specified
        """

        # Generate a random set with mix values
        return set( cls.gt_mix(items) )
