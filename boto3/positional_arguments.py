import boto3

def translate_text(text, source_language_code, target_language_code): #defining the positional arguments 
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, #allows function to be reusable without hardcoding it
        SourceLanguageCode=source_language_code, #use positional arguments 
        TargetLanguageCode=target_language_code 
    )
    print(response) 

def main():
    translate_text("I am learning some code in AWS today", 'en', 'fr')
#above provides the arguments when the function is called in that order



if __name__=="__main__":
    main()
    
  #Response as a dictionary  
#{'TranslatedText': "J'apprends du code dans AWS aujourd'hui", 'SourceLanguageCode': 'en', 'TargetLanguageCode': 'fr', 'ResponseMetadata':
#{'RequestId': 'da68a76f-2cf9-43e6-85bd-18c529fb03cc', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'da68a76f-2cf9-43e6-85bd-18c529fb03cc', 'cache-control': 'no-cache', 'content-type': 'application/x-amz-json-1.1', 'content-length': '112', 'date': 'Tue, 10 Jan 2023 20:11:55 GMT'}, 'RetryAttempts': 0}}
