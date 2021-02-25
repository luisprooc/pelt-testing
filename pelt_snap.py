from os import listdir, getcwd, path, mkdir, rmdir, remove
from colorama import init,Fore
class Snap:

    init(autoreset=True)

    # Private method
    @staticmethod
    def __handler_file():
        # filter all directories of the current dir
        created = list( filter( lambda x: x == "Generated", listdir( getcwd() )))

        # If dir exist, return True
        if len(created):
            return True
        
        return False
    
    @classmethod
    def snap_take(cls,name,files):

        """
        ("data",(( Pelt.gt_int(5), Pelt.gt_str(10) ))) => This function create a file with
            the data generated, Only works with generators.
        """

        # If dir exist, not create it and open file with it's name
        if cls.__handler_file():
            file = open("{0}/Generated/{1}.txt".format( getcwd(),name ), "w")

            for i in files:
                writen = "{0}\n".format( str(i) )
                file.write(writen)

            file.close()
            print(Fore.GREEN + "File Generated Succesfully ✔")
            return 

        # Create dir 'Generated' in current dir
        new_path = path.join(getcwd(), "Generated")  
        mkdir(new_path)

        # Create file with the name assigned
        file = open("{0}/Generated/{1}.txt".format( getcwd(),name ), "w")
        for i in files:
            writen = "{0}\n".format( str(i) )
            file.write(writen)

        file.close()
        print(Fore.GREEN + "File Generated Succesfully ✔")
        return

    @classmethod
    def snap_rm(cls,name):

        """
        ("data") => This function delete a file generated, require a name file without 
            extension
        """

        # If dir exist, not create it and open file with it's name

        try:
            if cls.__handler_file():

                # Find file in Generated dir and remove it
                rm_path = path.join( getcwd() , "Generated\{0}.txt".format( name ))  
                remove(rm_path)

                print(Fore.GREEN + "File Removed Succesfully ✔")
                return 

        # If the file not exist, return this
        except:
            print(Fore.RED + "File Already Not Exist 💢")
            return 


    @classmethod
    def snap_rm_all(cls):
        """
        () => This function delete all files generated
        """

        # If dir exist, not create it and open file with it's name
        if cls.__handler_file():
            files = listdir( getcwd() + "\Generated" )

            # If dir has files, removes it
            if len( files ):
                for file in files:
                    remove(path.join(getcwd(), "Generated\{0}".format(file)))
            
            # Get path and remove dir
            rm_path = path.join( getcwd() , "Generated")  
            rmdir(rm_path)
            print(Fore.GREEN + "Generated Removed Succesfully ✔")
            return 

        print(Fore.RED + "Generated Already Not Exist 💢")
        return
