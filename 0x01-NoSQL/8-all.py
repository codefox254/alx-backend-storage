#!/usr/bin/env python3
"""
Module for listing all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of formatted dictionaries where each dictionary contains
        the ObjectId and the 'name' field of a document. Returns an empty
        list if no documents are found.
    """
    documents = mongo_collection.find()
    result = []
    for doc in documents:
        result.append({
            "_id": doc["_id"],
            "name": doc.get("name", "")
        })
    return result
