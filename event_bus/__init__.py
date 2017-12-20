import logging

from .abstract.rabbit import BaseRabbit
from .abstract.rabbit import BaseConsumerMixin
from .abstract.rabbit import BaseProducerMixin
from .bus.event_bus import EventBus


logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.INFO)
