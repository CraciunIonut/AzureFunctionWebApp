import logging

import azure.functions as func
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey

import user

import json

import config

def Find(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')    

    if req.method == "GET":
        filename = f'templates/finduser.html'
        with open(filename, 'rb') as f:
            return func.HttpResponse(
                body=f.read(),
                mimetype='text/html',
                status_code=200
            )
            
    elif req.method == "POST":
        HOST = config.settings['host']
        MASTER_KEY = config.settings['master_key']
        DATABASE_ID = config.settings['database_id']
        CONTAINER_ID = config.settings['container_id']

        client = cosmos_client.CosmosClient(HOST, {'masterKey' : MASTER_KEY})

        database = client.get_database_client(DATABASE_ID)

        body = req.get_body()

        body_json = body.decode('utf-8').replace("'", '"')
    
        before, sep, _id = body_json.partition('=')

        _id = int(_id)

        try:
            container = database.create_container(id=CONTAINER_ID, partition_key=PartitionKey(path='/userID'))

        except exceptions.CosmosResourceExistsError:
            container = database.get_container_client(CONTAINER_ID)

        items = list(container.query_items(
            query = "SELECT * from c where c.userID=@id",
            parameters=[{"name" : "@id", "value": _id}]
        ))

        userJson = json.dumps(items)

        return func.HttpResponse(userJson, mimetype='text/json')
        

        




