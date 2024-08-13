#!/usr/bin/env python3
"""
List all documents in a collection using pymongo
"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    :param mongo_collection: The pymongo collection object.
    :return: A list of all documents in the collection. Returns an empty list if no documents are found.
    """
    return list(mongo_collection.find())
