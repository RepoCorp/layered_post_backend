import json
import pymongo

from bson.objectid import ObjectId
from bson import json_util

pem_locator ='global-bundle.pem'

def lambda_handler(event, context):
    client = pymongo.MongoClient('mongodb://catalinadelacuesta:39$(123.A23Jufer@docdb-2023-07-31-13-17-47.cluster-cnb5lwju2hhj.us-east-1.docdb.amazonaws.com', tls=True, tlsCAFile=pem_locator, replicaSet='rs0', connect=True)
    db = client.blog
    collection = db.posts

    blog_posts = list(collection.find({}))

    client.close()

    return {
        'statusCode': 200,
        'body': {'blog_post': parse_json(blog_posts)}
    }


def parse_json(data):
    return json.loads(json_util.dumps(data))