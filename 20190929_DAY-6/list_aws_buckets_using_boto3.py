import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
	print(bucket.name)


"""
# Importing a Module/Package in Python
import boto3

# Creating a Variable in Pyton and Calling a Module in a variable
list_s3_buckets = boto3.resource('s3')

# Print all the bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

"""