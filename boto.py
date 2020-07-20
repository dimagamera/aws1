from boto3.session import Session
import boto3


def download():
    ACCESS_KEY = ''
    SECRET_KEY = ''
    session = Session(aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    s3_resource = boto3.resource('s3')
    your_bucket = "bucks-mybucketsss"
    file_name = "config.txt"
    s3 = boto3.client('s3')
    s3.download_file(your_bucket, file_name, file_name)


def config():
    instance = []
    f = open("config.txt")
    for item in f:
        instance.append(item)
    imageid = str(instance[0].replace("ImageId=", "").replace("\n", ""))
    mincount = instance[1].replace(
        "MinCount=", "").replace("\n", "")
    maxcount = instance[2].replace(
        "MaxCount=", "").replace("\n", "")
    keyname = str(instance[3].replace(
        "KeyName=", "").replace("\n", ""))
    instancetype = str(instance[4].replace(
        "InstanceType=", "").replace("\n", ""))
    groupid = str(instance[5].replace(
        "group_id=", "").replace("\n", ""))
    subnet = str(instance[6].replace("SubnetId=", "").replace("\n", ""))
    create_ins(imageid, mincount, maxcount,
               keyname, instancetype, groupid, subnet)


def create_ins(imageid, mincount, maxcount, keyname, instancetype, groupid, subnet):
    print(imageid)
    ec2 = boto3.resource('ec2', region_name="eu-north-1")
    instance = ec2.create_instances(ImageId=imageid, MinCount=int(mincount), MaxCount=int(maxcount),
                                    KeyName=keyname, InstanceType=instancetype, SecurityGroupIds=[groupid], SubnetId=subnet)
