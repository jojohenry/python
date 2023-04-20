#function that shows hello world

def hello_world():
    print("Hello World")
    
#this line will call the function
hello_world()

#assign hello_world to a function

greeting = hello_world()
print(greeting)



#using Boto3

import boto3

client = boto3.client('translate')

def translate_text(): #declare the function using def, name, braces for parameters and a coloon
    response = client.translate_text(
        Text='I am learning some code in AWS today', #assigning the variable 'text'
        SourceLanguageCode='en', # 2 letter code from aws documentation for english
        TargetLanguageCode='fr'# 2 letter code from aws documentation for french
    )
    print(response) #print needs to be within the indent of the function
    
 #main function   
def main():
    translate_text() #calling the function. returned as a dictionary


#main function determines which code to run first
if __name__=="__main__":
    main()
        
