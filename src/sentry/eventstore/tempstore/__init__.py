from __future__ import absolute_import

from sentry.utils.imports import import_string
from django.conf import settings


event_tempstore = import_string(settings.SENTRY_EVENT_TEMPSTORE)(
    **settings.SENTRY_EVENT_TEMPSTORE_OPTIONS
)


__all__ = ["event_tempstore"]
