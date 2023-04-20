import boto3

#Create a list of input text

def new_input_text_list():
    input_text=open_input()
    new_list=[]
    for item in input_text:
        text=item['item']
        new_list.append(text)
    print(new_list)
    
