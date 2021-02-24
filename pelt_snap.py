from os import listdir, getcwd, path, mkdir, rmdir, remove

class Snap:

    @staticmethod
    def handler_file():
        # filter all directories of the current dir
        created = list( filter( lambda x: x == "Tests", listdir( getcwd() )))

        # If dir exist, return True
        if len(created):
            return True
        
        return False
    
    @classmethod
    def snap_take_memo(cls,name):

        # If dir exist, not create it and open file with it's name
        if cls.handler_file():
            open("{0}/Tests/{1}.txt".format( getcwd(),name ), "w")
            return 

        # Create dir 'Tests' in current dir
        new_path = path.join(getcwd(), "Tests")  
        mkdir(new_path)

        # Create file with the name assigned
        open("{0}/Tests/{1}.txt".format( getcwd(),name ), "w")
        return

    @classmethod
    def snap_remove_memo(cls,name):

        # If dir exist, not create it and open file with it's name

        try:
            if cls.handler_file():

                # Find file in Tests dir and remove it
                rm_path = path.join( getcwd() , "Tests\{0}.txt".format( name ))  
                remove(rm_path)
                return "Test Removed Succesfully ✔"

        # If the file not exist, return this
        except:
            return "Test Already Not Exist 💢"


    @classmethod
    def snap_remove_all_memo(cls):

        # If dir exist, not create it and open file with it's name
        if cls.handler_file():
            files = listdir( getcwd() + "\Tests" )

            # If dir has files, removes it
            if len( files ):
                for file in files:
                    remove(path.join(getcwd(), "Tests\{0}".format(file)))
            
            # Get path and remove dir
            rm_path = path.join( getcwd() , "Tests")  
            rmdir(rm_path)
            return "All Tests Removed Succesfully ✅"

        return "Tests Already Not Exist 💢"
