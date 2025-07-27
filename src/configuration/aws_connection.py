import boto3
import os
from src.constants import AWS_SECRET_ACCESS_KEY_ENV_KEY, AWS_ACCESS_KEY_ID_ENV_KEY, REGION_NAME


class OldS3Client:

    s3_client=None
    s3_resource = None
    def __init__(self, region_name=REGION_NAME):
        """ 
        This Class gets aws credentials from env_variable and creates an connection with s3 bucket 
        and raise exception when environment variable is not set
        """

        if S3Client.s3_resource==None or S3Client.s3_client==None:
            __access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY, )
            __secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY, )
            if __access_key_id is None:
                raise Exception(f"Environment variable: {AWS_ACCESS_KEY_ID_ENV_KEY} is not not set.")
            if __secret_access_key is None:
                raise Exception(f"Environment variable: {AWS_SECRET_ACCESS_KEY_ENV_KEY} is not set.")
            print(f"\033[92m Environment variable: {AWS_ACCESS_KEY_ID_ENV_KEY} is set. \033[0m")
            print(f"\033[92m Environment variable: {AWS_SECRET_ACCESS_KEY_ENV_KEY} is set. \033[0m")
            S3Client.s3_resource = boto3.resource('s3',
                                            aws_access_key_id=__access_key_id,
                                            aws_secret_access_key=__secret_access_key,
                                            region_name=region_name
                                            )
            S3Client.s3_client = boto3.client('s3',
                                        aws_access_key_id=__access_key_id,
                                        aws_secret_access_key=__secret_access_key,
                                        region_name=region_name
                                        )
        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client

class S3Client:
    """
    Creates an S3 client and resource using a boto3 session initialized
    with credentials from environment variables.
    """
    s3_client = None
    s3_resource = None

    def __init__(self, region_name=REGION_NAME):
        """
        Initializes the S3 client and resource if not already created.
        Uses environment variables for AWS credentials.
        """

        if not S3Client.s3_client or not S3Client.s3_resource:
            access_key = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY)
            secret_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY)

            if not access_key:
                raise Exception(f"Environment variable '{AWS_ACCESS_KEY_ID_ENV_KEY}' is not set.")
            if not secret_key:
                raise Exception(f"Environment variable '{AWS_SECRET_ACCESS_KEY_ENV_KEY}' is not set.")

            print(f"\033[92mEnvironment variable '{AWS_ACCESS_KEY_ID_ENV_KEY}' is set.\033[0m")
            print(f"\033[92mEnvironment variable '{AWS_SECRET_ACCESS_KEY_ENV_KEY}' is set.\033[0m")

            # Initialize boto3 session
            session = boto3.Session(
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                region_name=region_name
            )

            # Create client and resource from session
            S3Client.s3_client = session.client('s3')
            S3Client.s3_resource = session.resource('s3')

        # Assign to instance
        self.s3_client = S3Client.s3_client
        self.s3_resource = S3Client.s3_resource
