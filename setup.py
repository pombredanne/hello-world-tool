import scraperwiki
from datetime import datetime

scraperwiki.sqlite.save([], {'message': 'hello world!', 'datetime': datetime.now()})
