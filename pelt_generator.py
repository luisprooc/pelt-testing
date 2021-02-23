from random import randint

class Generator:

    @staticmethod
    def generate_int(items):
        
        if items <= 1:
            return randint( 0,150 )

        return [ randint(0,150) for i in range(0,items) ]

    @staticmethod
    def generate_str(items):

        str_dict = {
            1:"Lorem", 2: "Ipsum", 3:"dolor", 4:"amet",
            5:"consectetur", 6:"fugiat", 7:"nulla", 
            8:"Excepteur", 9:"occaecat", 10:"proident"
        }
        
        if items <= 1:
            return str_dict[randint( 1,10 )]


        return [ str_dict[ randint(1,10) ] for i in range(0,items) ]

    @classmethod
    def generate_mix(cls,items):

        if items <= 1:
            mix = randint(0,1)

            if mix:
                return cls.generate_int(1)

            else:
                return cls.generate_str(1)

        else:

            list = []

            for i in range(0,items):
                mix = randint(0,1)

                if mix:
                    list.append( cls.generate_int(1) )

                else:
                    list.append( cls.generate_str(1) )

            return list


    @classmethod
    def generate_dict(cls,items):

        return { cls.generate_mix(1):cls.generate_mix(1) for i in range(0,items) }

    @classmethod
    def generate_set(cls,items):

        return set( cls.generate_mix(items) )
