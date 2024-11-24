from storages.backends.s3boto3 import S3Boto3Storage



from .awscred import AWS_CREDENTIAL
class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False




