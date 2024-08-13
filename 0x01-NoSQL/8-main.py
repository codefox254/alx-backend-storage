#!/usr/bin/env python3
""" 8-main """


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    :param mongo_collection: The pymongo collection object.
    :return: A list of all documents in the collection. Returns an empty list if no documents are found.
    """
    return mongo_collection.find()
