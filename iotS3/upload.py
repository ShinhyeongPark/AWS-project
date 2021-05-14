import boto3 

s3_resource = boto3.resource( 
				's3', 
                aws_access_key_id = "AKIA5VZTIAOJSOLVW463",         # 액세스 ID
                aws_secret_access_key = "2WChAcMTCEfuHL2wSSLtCt5H6loktGmAWTihc6f+",    # 비밀 엑세스 키 
                region_name = "eu-north-1"
)

# get image file
data = open('/Users/etlaou/Downloads/FinalProject/iotS3/images/(image)2.png', 'rb') 

# save image to S3 bucket as public 
s3_resource.Bucket('yangjae-team10-bucket').put_object(Body=data, Key='(image)2.png', ACL='public-read') 

# get public image url 
url = "https://s3-%s.amazonaws.com/%s/%s" % ('eu-north-1', 'yangjae-team10-bucket', '(image)2.png')