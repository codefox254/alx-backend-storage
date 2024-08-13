#!/usr/bin/env python3
"""
Module for retrieving schools by topic from MongoDB.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Retrieves a list of schools from a MongoDB collection that have a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List of documents (schools) that include the specified topic in their topics list.
    """
    return mongo_collection.find({"topics": topic})
