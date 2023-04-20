import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 


#having user input text to translate
text = input("Enter the text you want to translate: ")
source_language_code = input("Provide the two letter source language code ")
target_language_code = input("Provide the two letter target language code ")



def main():
    translate_text(
        Text=text,
        SourceLanguageCode=source_language_code,
        TargetLanguageCode=target_language_code
        )

if __name__=="__main__":
    main()
