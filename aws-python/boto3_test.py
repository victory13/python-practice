import boto3

#s3_client = boto3.client('s3')
#
# buckets=[]
# for bucket in s3_resource.buckets.all():
#     buckets.append(bucket.name)
# print(buckets)

s3_resource = boto3.resource('s3')
""""
buckets = s3_resource.buckets.all()

for i in buckets:
    print(i.name)
"""
#accessing buckets
readbucket = s3_resource.Bucket('pythonniki')

bucketlist = readbucket.objects.all()

for i in bucketlist:
    print(i.key)