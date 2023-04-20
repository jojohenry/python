import boto3

def translate_text(**kwargs):#key word arguments 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    translate_text(Text='I am learning to code in AWS',SourceLanguageCode='en',TargetLanguageCode='fr')

if __name__=="__main__":
    main()
    
###################################################

#Complete the same way
#Using kwargs as dictionary for the function results
    
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### kwargs used to input the arguments

kwargs={
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()    
    
    
#Same Results for both functions
{'TranslatedText': "J'apprends à coder dans AWS", 'SourceLanguageCode': 'en', 'TargetLanguageCode': 'fr', 'ResponseMetadata': {'RequestId': 'd30e7f20-3bf6-462f-b0f6-02110170495d', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'd30e7f20-3bf6-462f-b0f6-02110170495d', 'cache-control': 'no-cache', 'content-type': 'application/x-amz-json-1.1', 'content-length': '101', 'date': 'Tue, 10 Jan 2023 20:26:56 GMT'}, 'RetryAttempts': 0}}
{'TranslatedText': "J'apprends à coder dans AWS", 'SourceLanguageCode': 'en', 'TargetLanguageCode': 'fr', 'ResponseMetadata': {'RequestId': 'cfac5f35-6e75-41d9-a082-a2559228b1fe', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'cfac5f35-6e75-41d9-a082-a2559228b1fe', 'cache-control': 'no-cache', 'content-type': 'application/x-amz-json-1.1', 'content-length': '101', 'date': 'Tue, 10 Jan 2023 20:26:56 GMT'}, 'RetryAttempts': 0}}
