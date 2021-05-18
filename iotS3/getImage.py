import json
import urllib.parse
import boto3

s3 = boto3.client('s3')

s3_resource = boto3.resource( 
				's3', 
                aws_access_key_id = "",         # 액세스 ID
                aws_secret_access_key = "",    # 비밀 엑세스 키 
                region_name = "eu-north-1"
)

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    # print(event)
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        # print("CONTENT TYPE: " + response['ContentType'])
        #event['Records'][0]['s3']['bucket']['arn']+
        # print(event['Records'][0]['s3']['bucket']['arn']+'/'+event['Records'][0]['s3']['object']['key'])
        return event['Records'][0]['s3']['bucket']['arn']+'/'+event['Records'][0]['s3']['object']['key']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
