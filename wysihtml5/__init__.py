"""
django-wysihtml5 - Simple Django app that allows using the rich text editor Wysihtml5 in text fields.
"""
VERSION = (2, 0, 0)

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    return version
