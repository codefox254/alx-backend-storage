#!/usr/bin/env python3
""" 102-log_stats """

from pymongo import MongoClient

def top_ips(mongo_collection):
    """
    Returns the top 10 most frequent IPs sorted by their frequency.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        List of dictionaries, each containing an IP address and its frequency.
    """
    pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": -1
            }
        },
        {
            "$limit": 10
        }
    ]

    return list(mongo_collection.aggregate(pipeline))


def log_stats():
    """
    Print stats about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Count all documents
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count by HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count status check requests
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

    # Get top 10 IPs
    print("IPs:")
    ips = top_ips(nginx_collection)
    for ip in ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    log_stats()
