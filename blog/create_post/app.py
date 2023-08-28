import json
import os

import boto3 as boto3
import pymongo


secret_key = os.environ['SECRET_KEY']
# pem_locator ='/opt/python/rds-combined-ca-bundle.pem'
pem_locator = 'global-bundle.pem'
from bson.objectid import ObjectId

def lambda_handler(event, context):

    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    get_secret_value_response = client.get_secret_value(
        SecretId=secret_key
    )

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']


    client = pymongo.MongoClient(
        f'mongodb://catalinadelacuesta:${secret}@docdb-2023-07-31-13-17-47.cluster-cnb5lwju2hhj.us-east-1.docdb.amazonaws.com',
        tls=True, tlsCAFile=pem_locator, replicaSet='rs0', connect=True)

    db = client.blog
    collection = db.posts
    _id = collection.insert_one(event['blog_post'])

    print(f'id: {_id.inserted_id}')

    print(collection.find_one({'_id': ObjectId(_id.inserted_id)}))

    cursor = collection.find({})
    for document in cursor:
          print(document)

    client.close()

    return {
        'statusCode': 200,
        'body': json.dumps({'ID': str(_id.inserted_id)})
    }