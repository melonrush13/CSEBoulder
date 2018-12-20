import azure.cosmos.cosmos_client as cosmos_client

def GetDatabaseLink(database_id):
    return "dbs" + "/" + database_id

def GetContainerLink(database_id, collection_id):
    return GetDatabaseLink(database_id) +  "/" + "colls" + "/" +  collection_id

config = {
    'ENDPOINT': 'https://csebouldercosmos.documents.azure.com:443/',
    'PRIMARYKEY': 'enterkeyhere',
    'DATABASE': 'ocr-output',
    'CONTAINER': 'items'
}

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={
                                  'masterKey': config['PRIMARYKEY']})

container = GetContainerLink('IyJbAA==', 'IyJbAIklTSw=/')

searchInput = "physics"
# query = {'query': "SELECT * FROM server s"}
query = {'query': f"SELECT * FROM server s WHERE contains(s.ocr_text, '{searchInput}')"}

options = {}
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

result_iterable = client.QueryItems(container, query, options)
print(container)

for item in iter(result_iterable):
    print(item)