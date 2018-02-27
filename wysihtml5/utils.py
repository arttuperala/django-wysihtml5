#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.core.exceptions import ImproperlyConfigured
from django.utils.functional import keep_lazy
try:
    from importlib import import_module
except ImportError:
    from django.utils.importlib import import_module  # Django 1.6 / py2.6


def get_function(function_path):
    """
    import and return function from ``path.to.module.function`` argument
    """
    try:
        mod_name, func_name = function_path.rsplit('.', 1)
        mod = import_module(mod_name)
    except ImportError as e:
        raise ImproperlyConfigured(('Error importing module %s: "%s"' %
                                   (mod_name, e)))
    return getattr(mod, func_name)


def keeptags(value, tags):
    tags = [re.escape(tag) for tag in tags.split()]

    def _replacer(match):
        if match.group(1) in tags:
            return match.group(0)
        else:
            return ''

    return re.sub(r'</?([^> ]+).*?>', _replacer, value)

keeptags = keep_lazy(())(keeptags)