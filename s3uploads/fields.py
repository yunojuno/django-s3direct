from django.db.models import Field
from django.conf import settings
from s3upload.widgets import S3UploadWidget


class S3UploadField(Field):
    def __init__(self, *args, **kwargs):
        dest = kwargs.pop('dest', None)
        self.widget = S3UploadWidget(dest=dest)
        super(S3UploadField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'TextField'

    def formfield(self, *args, **kwargs):
        kwargs['widget'] = self.widget
        return super(S3UploadField, self).formfield(*args, **kwargs)


if 'south' in settings.INSTALLED_APPS:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^s3upload\.fields\.S3UploadField"])
