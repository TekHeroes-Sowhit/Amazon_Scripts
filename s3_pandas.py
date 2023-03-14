
import boto3
BUCKET_NAME="BOTO_SERIES"
s3=boto3.client("s3")
response=s3.list_objects(Bucket=BUCKET_NAME)
for obj in response["Contents"]:
    print(obj)
## upload a file to s3 bucket

with open("./file.jpg","rb") as file:
    s3.upload_fileobj(f,BUCKET_NAME,"burger_new_upload.jpg",ExtraArgs={"ACl":"public-read"})

## Download file with the binary_data
with open("downloaded_burger.jpeg","wb") as f:
    s3.download_fileobj(BUCKET_NAME,"burger.jpg",f)
    ## Code her to send image to frontend


## copy objects between different buckets

s3.copy_objects(ACL="public_read",Bucket="new-destination-bucket",
CopySource=f'/{Bucket_Name}/burger.jpg',key="CopiedImage.jpg",)

## Getting detailed about the objects
response=s3.get_object(Bucket=BUCKET_NAME,key="burger.jpg")
print(response)

##
bucket_location=s3.create_bucket(ACL="public-read",Bucket="new-destination-bucket-777")
print(bucket_location)
