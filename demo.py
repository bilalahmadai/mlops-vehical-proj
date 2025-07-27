# below code is to check the logging config
# from src.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

# --------------------------------------------------------------------------------

# # below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

# --------------------------------------------------------------------------------

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()


# Data Ingestion Artifact:  DataIngestionArtifact(trained_file_path='artifact\\07_26_2025_17_06_46\\data_ingestion\\ingested\\train.csv', test_file_path='artifact\\07_26_2025_17_06_46\\data_ingestion\\ingested\\test.csv')

# Data Validation Artifact:  DataValidationArtifact(validation_status=True, message='', validation_report_file_path='artifact\\07_26_2025_17_06_46\\data_validation\\report.yaml')

# Data Transformation Artifact:  DataTransformationArtifact(transformed_object_file_path='artifact\\07_26_2025_17_06_46\\data_transformation\\transformed_object\\preprocessing.pkl', transformed_train_file_path='artifact\\07_26_2025_17_06_46\\data_transformation\\transformed\\train.npy', transformed_test_file_path='artifact\\07_26_2025_17_06_46\\data_transformation\\transformed\\test.npy')
# Model Trainer Artifact:  ModelTrainerArtifact(trained_model_file_path='artifact\\07_26_2025_17_06_46\\model_trainer\\trained_model\\model.pkl', metric_artifact=ClassificationMetricArtifact(f1_score=0.9309005767803096, precision_score=0.8813137798202338, recall_score=0.9864000121023252))

# data_ingestion_artifact =  DataIngestionArtifact(
#         trained_file_path='artifact\\07_26_2025_17_06_46\\data_ingestion\\ingested\\train.csv',
#         test_file_path='artifact\\07_26_2025_17_06_46\\data_ingestion\\ingested\\test.csv'
#         )

#     data_validation_artifact =   DataValidationArtifact(
#         validation_status=True,
#         message='',
#         validation_report_file_path='artifact\\07_26_2025_17_06_46\\data_validation\\report.yaml'
#         )

#     data_transformation_artifact =  DataTransformationArtifact(
#         transformed_object_file_path='artifact\\07_26_2025_17_06_46\\data_transformation\\transformed_object\\preprocessing.pkl',
#         transformed_train_file_path='artifact\\07_26_2025_17_06_46\\data_transformation\\transformed\\train.npy',
#         transformed_test_file_path='artifact\\07_26_2025_17_06_46\\data_transformation\\transformed\\test.npy'
#         )
#     model_trainer_artifact =   ModelTrainerArtifact(
#         trained_model_file_path='artifact\\07_26_2025_17_06_46\\model_trainer\\trained_model\\model.pkl',
#         metric_artifact=ClassificationMetricArtifact(
#             f1_score=0.9309005767803096,
#             precision_score=0.8813137798202338,
#             recall_score=0.9864000121023252
#             )
#         )
# --------------------------------------------------------------------------------

# from src.configuration.aws_connection import S3Client, boto3
# s3_client = S3Client()

# # Check the details of S3 buckets
# buckets = s3_client.s3_client.list_buckets()
# print("S3 Buckets:")
# for bucket in buckets['Buckets']:
#     print(f"- {bucket['Name']}")

# # Check IAM user details
# iam_client = boto3.client('iam')
# user_info = iam_client.get_user()
# print("IAM User:")
# print(f"User ARN: {user_info['User']['Arn']}")
# print(f"User Name: {user_info['User']['UserName']}")

# # Check permissions for each S3 bucket
# for bucket in buckets['Buckets']:
#     bucket_name = bucket['Name']
#     try:
#         # Attempt to get the bucket's ACL to check permissions
#         acl = s3_client.s3_client.get_bucket_acl(Bucket=bucket_name)
#         print(f"Permissions for bucket '{bucket_name}':")
#         for grant in acl['Grants']:
#             print(f" - Grantee: {grant['Grantee'].get('DisplayName', 'Unknown')}, Permission: {grant['Permission']}")
#     except Exception as e:
#         print(f"Could not retrieve permissions for bucket '{bucket_name}': {e}")


# import boto3
# import os
# from dotenv import load_dotenv
# load_dotenv()
# # Upload new object
# session = boto3.Session(
#     aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
#     aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
#     region_name='us-east-1'  # your bucket's region
# )

# s3 = session.client('s3')
# bucket = 'my-model-mlopsproj-bilal'

# # Upload new object
# s3.put_object(Bucket=bucket, Key='test.txt', Body='Uploaded by IAM user')

# --------------------------------------------------------------------------------

# from src.cloud_storage.aws_storage import SimpleStorageService
# s3 = SimpleStorageService()

# Upload file
# s3.upload_file("artifact\\07_26_2025_13_31_33\\model_trainer\\trained_model", "models/my_model.pkl", "my-model-mlopsproj-bilal")
from_filename = "artifact\\07_26_2025_13_31_33\\model_trainer\\trained_model"
to_filename = "model.pkl"
bucket_name = "my-model-mlopsproj-bilal"
# s3.upload_file(from_filename, to_filename, bucket_name)
# status = s3.s3_key_path_available(bucket_name, to_filename)
# print(status)
# model = s3.load_model(to_filename, bucket_name)
# print(model)
# print(model.__dict__)
# print(model.__class__)

# with open(from_filename, 'rb') as f:
#     s3.s3_client.put_object(Bucket=bucket_name, Key=to_filename, Body=f)

# Delete file
# s3.delete_file("models/my_model.pkl", "my-model-mlopsproj-bilal")
