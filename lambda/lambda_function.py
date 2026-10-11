"""Week 1 skeleton: health check only. TF-IDF and S3/DynamoDB in week 2."""
import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json; charset=utf-8"},
        "body": json.dumps({"status": "ok", "project": "course-faq-chatbot", "phase": "week-1"}, ensure_ascii=False)
    }
