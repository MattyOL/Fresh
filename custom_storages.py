from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage, ManifestFilesMixin, ClientError, FileNotFoundError


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION


# https://github.com/jschneier/django-storages/issues/841
class ManifestS3Boto3Storage(ManifestFilesMixin, S3Boto3Storage):
    def _open(self, name, mode='rb'):
        name = self._normalize_name(self._clean_name(name))
        try:
            f = S3Boto3StorageFile(name, mode, self)
        except ClientError as err:
            if err.response['ResponseMetadata']['HTTPStatusCode'] == 404:
                raise FileNotFoundError('File does not exist: %s' % name)
            raise  # Let it bubble up if it was some other error
        return f