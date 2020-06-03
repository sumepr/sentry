from __future__ import absolute_import

import logging

from .base import BaseEventTmpStore
from sentry.cache.redis import RedisClusterCache

logger = logging.getLogger(__name__)


class RedisClusterEventTempStore(BaseEventTmpStore):
    def __init__(self, **options):
        super(BaseEventTmpStore, self).__init__(inner=RedisClusterCache(**options))
