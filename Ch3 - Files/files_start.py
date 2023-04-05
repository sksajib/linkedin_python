#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    myfile=open("textfile.txt","w+")
    for i in range(10):
        myfile.write("This is some text\n")
    myfile=open("textfile.txt","a+")
    for i in range(10):
        myfile.write("This is some text\n")
    myfile.close()
    
    # Open the file for appending text to the end
    myfile=open("textfile.txt","r")
    if myfile.mode=="r":
        #content=myfile.read()
        fl=myfile.readlines()
        for x in fl:
            print(x)
    myfile=open("textfile.txt","r")
    if myfile.mode=="r":
        content=myfile.read()   
    print(content)

    # write some lines of data to the file

    
    # close the file when done

    
    # Open the file back up and read the contents

    
if __name__ == "__main__":
    main()
