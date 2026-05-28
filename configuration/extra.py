####
## This file contains extra configuration options that can't be configured
## directly through environment variables.
####

## Specify one or more name and email address tuples representing NetBox administrators. These people will be notified of
## application errors (assuming correct email settings are provided).
# ADMINS = [
#     # ['John Doe', 'jdoe@example.com'],
# ]
ADMINS = [
    ['Mark Bevill', 'mark.bevill@sunshine811.com'],
]

## URL schemes that are allowed within links in NetBox
ALLOWED_URL_SCHEMES = (
    'file', 'ftp', 'ftps', 'http', 'https', 'irc', 'mailto', 'sftp', 'ssh', 'tel', 'telnet', 'tftp', 'vnc', 'xmpp',
)

## Enable installed plugins. Add the name of each plugin to the list.
# from netbox.configuration.configuration import PLUGINS
# PLUGINS.append('my_plugin')

## Plugins configuration settings. These settings are used by various plugins that the user may have installed.
## Each key in the dictionary is the name of an installed plugin and its value is a dictionary of settings.
# from netbox.configuration.configuration import PLUGINS_CONFIG
# PLUGINS_CONFIG['my_plugin'] = {
#   'foo': 'bar',
#   'buzz': 'bazz'
# }


## Remote authentication support
# REMOTE_AUTH_DEFAULT_PERMISSIONS = {}
REMOTE_AUTH_ENABLED=True
REMOTE_AUTH_AUTO_CREATE_USER=True
REMOTE_AUTH_BACKEND='social_core.backends.azuread.AzureADOAuth2'
SOCIAL_AUTH_AZUREAD_OAUTH2_KEY='9f62ea56-72e6-4a8a-8b9c-7896c5cc132c'
SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET='rIy8Q~~CDk1hd1km4s11fDUJHdL6p1QxpOXYnak7'
SOCIAL_AUTH_REDIRECT_IS_HTTPS=True

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

SOCIAL_AUTH_AZUREAD_OAUTH2_RESOURCE = 'https://graph.microsoft.com/'
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'netbox.authentication.user_default_groups_handler',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details'
)


# Define special user types using groups. Exercise great caution when assigning superuser status.
SOCIAL_AUTH_PIPELINE_CONFIG = {
    'AZUREAD_USER_FLAGS_BY_GROUP': {
        "is_staff": ['technical-operations-manager','technical-operations-staff'],
        "is_superuser": ['technical-operations-manager','technical-operations-staff']
    },

    'AZUREAD_GROUP_MAP': {
        'technical-operations-manager': 'netbox-admin',
        'technical-operations-staff': 'netbox-admin',
    }

}

## By default uploaded media is stored on the local filesystem. Using Django-storages is also supported. Provide the
## class path of the storage driver in STORAGE_BACKEND and any configuration options in STORAGE_CONFIG. For example:
# STORAGE_BACKEND = 'storages.backends.s3boto3.S3Boto3Storage'
# STORAGE_CONFIG = {
#     'AWS_ACCESS_KEY_ID': 'Key ID',
#     'AWS_SECRET_ACCESS_KEY': 'Secret',
#     'AWS_STORAGE_BUCKET_NAME': 'netbox',
#     'AWS_S3_REGION_NAME': 'eu-west-1',
# }


## This file can contain arbitrary Python code, e.g.:
# from datetime import datetime
# now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
# BANNER_TOP = f'<marquee width="200px">This instance started on {now}.</marquee>'