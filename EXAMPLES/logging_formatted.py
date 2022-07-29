#!/usr/bin/env python
import sys
sys.path.append('..')  # DON'T DO THIS
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    format='Wombat %(name)s %(filename)s:%(lineno)d %(asctime)s %(levelname)s %(message)s', # <1>
    filename='../TEMP/formatted.log',
    level=logging.INFO,
)

from carddeck import CardDeck

logger.info("this is information")
logger.warning("this is a warning")
logger.info("this is information")
logger.critical("this is critical")

d1 = CardDeck("Bob")
d2 = CardDeck("Ebenezer")
d3 = CardDeck("Nelly")


