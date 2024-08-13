#!/usr/bin/env python3
"""
Module for updating the topics of a school document in MongoDB.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document in the MongoDB collection based on the school name.

    Args:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school document to update.
        topics (list of str): The list of topics to update in the document.

    Returns:
        The result of the update operation.
    """
    result = mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result
