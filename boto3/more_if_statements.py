import boto3
############ 3 separate if statements included
import json

# This uses a json string as an input 
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"fr",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""

json_input = json.loads(json_string) # We use loads as we are loading from a string.

# Defines two variables to store the language code from the input.
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# The if statement checks to see if the language code is the same as the source code
if SourceLanguageCode == TargetLanguageCode:
    print("The SourceLanguageCode is the same as the TargetLanguageCode - stopping")
else:
    print("The Source Language and Target Language codes are different - proceeding")
    
    
    
    
###################################################

# A defined list of languages supported by Amazon Translate
languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF","nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it","ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es","sw","sv","tl","ta","th","tr","uk","ur","vi"]

# This uses a json string as an input
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""

json_input = json.loads(json_string)

# Extracts the SourceLanguageCode and TargetLanguageCode from the JSON
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# Uses an if-else statement to check that the SourceLanguageCode is in the languages list.
if SourceLanguageCode in languages:
    print("The SourceLanguageCode is valid - proceeding")
else:
    print("The SourceLanguageCode is not valid - stopping")
    
    
#############################################

# A defined list of languages supported by Amazon Translate
languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF","nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it","ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es","sw","sv","tl","ta","th","tr","uk","ur","vi"]

# This uses a json string as an input
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""

json_input = json.loads(json_string)

SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# Uses an if-elif-else statements to check that the SourceLanguageCode is in the languages list.
if SourceLanguageCode == TargetLanguageCode:
    print("The SourceLanguageCode is the same as the TargetLanguageCode - nothing to do")
elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
    print("Neither the SourceLanguageCode and TargetLanguageCode are valid - stopping")
elif SourceLanguageCode not in languages:
    print("The SourceLanguageCode is not valid - stopping")
elif TargetLanguageCode not in languages:
    print("The TargetLanguageCode is not valid - stopping")
elif SourceLanguageCode in languages and TargetLanguageCode in languages:
    print("The SourceLanaguageCode and TargetLanguageCode are valid - proceeding")
else:
    print("There is an issue")
    
    ######################################
    
    ###########input function examples
    
# Open the input file to get the json.
def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        return contents['Input']

# Boto3 function to use Amazon Translate to translate the text and only return the Translated Text
def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText'])

# Add a Loop to iterate over the json file.
def translate_loop():
    input_text = open_input()
    for item in input_text:
        if input_validation(item) == True:
            translate_text(**item)
        else:
            raise SystemError    
