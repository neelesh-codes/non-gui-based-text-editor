from support import read_the_file, write_in_file, append_in_file
import pandas as pd


def show_file_context(filename: str) -> str:
    filename = str(filename)
    read_the_file(filename)
    return filename


def write_file_context(filename: str, write_arg: str) -> str:
    write_arg = str(write_arg)
    write_in_file(filename, write_arg)
    return write_arg


def append_file_context(filename, append_arg):
    append_in_file(filename, append_arg)
    return None


def help():
    DataFrame = pd.read_excel("help.xlsx", engine="openpyxl")
    print("\n\n\n\n")
    print(DataFrame)
    print("For more information: ")
    print("https://github.com/neelesh-codes/non-gui-based-text-editor")
    print("\n\n\n\n")


print("For more commands type ./he$p")
print("OR")
print("See the readme.md file in the https://github.com/neelesh-codes/non-gui-based-text-editor")
print("Note: ")
print("Before writing anything in any file see the readme.md gile in the https://github.com/neelesh-codes/non-gui-based-text-editor")
print("OR")
print("type ./he$p")
while True:
    userfile = input("Enter the file path or ./he$p : ")
    print("\n\n if you entered ./he$p enter None in command prompt.\n\n")
    user = input("Enter your commanuserfiled: ")

    if (user == "./sh$ow"):
        show_file_context(userfile)
        print("\n\n\nshowing was successful!!")

    elif (user == "./wr$te"):
        userwrite = input("Enter what you want to write :\n")
        write_file_context(userfile, userwrite)
        print("Writing was successful!!")

    elif (user == "./app$nd"):
        userappend = input("Enter what you want to append in the file : \n")
        append_file_context(userfile, userappend)
        print("Appending was successful!!")
    elif (userfile == "./he$p" and user == "None"):
        help()
    else:
        print("No Command matched.")

