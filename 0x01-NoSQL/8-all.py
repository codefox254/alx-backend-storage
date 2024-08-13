from pymongo import MongoClient

def list_all(mongo_collection):
    """
    List all documents in a collection.

    :param mongo_collection: The pymongo collection object.
    :return: A list of all documents in the collection. Returns an empty list if no documents are found.
    """
    # Retrieve all documents from the collection
    documents = list(mongo_collection.find())
    
    return documents
