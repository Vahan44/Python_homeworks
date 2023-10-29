import time

def fileName():
    
    try:
        filename = input("Enter the name of a text file you want to open:  ")
        with open(filename,"r") as f:
            print(f.read())
            time.sleep(3)
            answer=input("\nDo you want to write in this file or create new file?\nType yes if you want to write in this file, else type create\n")
            if answer.lower()=="yes":
                with open(filename,"a") as f:
                    f.write(input("Enter text to add at the end: "))
                    f.close()
                    print("Successfully closed the file")
            else:
                new_file=input("Input the name of file you want to create.\n")
                if new_file.isnumeric():
                    try:
                        raise ValueError('Invalid Filename: Name is numeric.')
                    except ValueError as error:
                            print(error)
                else:
                    if new_file.lower().endswith(".txt"):
                        try:
                            raise SyntaxWarning("No need to write the extension")
                        except SyntaxWarning as warning:
                            print(warning)
                    try:
                        with open(new_file,"x") as f:
                            f.write(input("\nEnter text to add at the end of the document: "))
                    except FileExistsError:
                        print("File already exists.")
                    else:
                        print("\nThe writing is successful")
                    finally:
                        f.close()
    except FileNotFoundError:
        print("File not found. \nIf you're sure that the file exists, please provide it's path.\nFor example C:/User/user/Desktop/Lec_7/test.txt")
        fileName()

fileName()