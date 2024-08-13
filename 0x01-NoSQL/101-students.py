def top_students(mongo_collection):
    """
    Returns all students sorted by average score in descending order.
    
    Args:
        mongo_collection: pymongo collection object.
        
    Returns:
        List of dictionaries, each containing the student's details and average score.
    """
    # Calculate the average score for each student
    pipeline = [
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    
    # Execute the aggregation pipeline
    students = list(mongo_collection.aggregate(pipeline))
    
    return students
