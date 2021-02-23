from random import randint

class Generator:

    @staticmethod
    def generate_int(items):
        
        if items <= 1:
            return randint( 0,150 )

        l = [ randint(0,150) for i in range(0,items) ]

        return l

    @staticmethod
    def generate_str(items):

        str_dict = {
            1:"Lorem", 2: "Ipsum", 3:"dolor", 4:"amet",
            5:"consectetur", 6:"fugiat", 7:"nulla", 
            8:"Excepteur", 9:"occaecat", 10:"proident"
        }
        
        if items <= 1:
            return str_dict[randint( 1,10 )]


        l = [ str_dict[ randint(1,10) ] for i in range(0,items) ]


        return l

    @classmethod
    def generate_mix(cls,items):

        if items <= 1:
            mix = randint(0,1)

            if mix:
                return cls.generate_int(1)

            else:
                return cls.generate_str(1)

        else:

            l = []

            for i in range(0,items):
                mix = randint(0,1)

                if mix:
                    l.append( cls.generate_int(1) )

                else:
                    l.append( cls.generate_str(1) )

            return l


    @classmethod
    def generate_dict(cls,items):

        d = { cls.generate_mix(1):cls.generate_mix(1) for i in range(0,items) }

        return d

    @classmethod
    def generate_set(cls,items):

        s = set( cls.generate_mix(1) for i in range(0,items) )

        return s
