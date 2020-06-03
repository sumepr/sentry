from __future__ import absolute_import

from sentry.cache import default_cache

from .base import BaseEventTempStore


class DefaultEventTempStore(BaseEventTempStore):
    def __init__(self, **options):
        super(DefaultEventTempStore, self).__init__(inner=default_cache, **options)
