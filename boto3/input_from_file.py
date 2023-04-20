import boto3

#created this file and default file named test.txt
#this .py file needs to be run within the CLI

#with open(filename, 'r' ) as variable_name:
#   <Do something with variable here>

def open_input(file):
    with open(file, 'r') as f:
        text = f.read() #We use read() to read the actual contents of the file
        print(text)

def main():
    open_input("test.txt")

if __name__=="__main__":
    main()
