# writefile.py
# Aurthor: Akshay Pastagiya
# This program is to write data in to the file
import os.path

def write(filename,data): 
    if not os.path.isfile(filename):
        print(f"File ({filename}) doesnot exist")
        Y = input(f"Do you want to create file ({filename}) Y/N: ")
        if Y == "Y":
            with open(filename, "x") as f:     
                f.write(data) 
                print(f"Write in to the file ({filename}) completed") 
        elif Y == "N":
            print("File not created run programm again with correct file name")
        else:
            print(f"Enter correct input")
    else:
        with open(filename, "w") as f:     
            f.write(data)
            print(f"Write in to the file ({filename}) completed") 