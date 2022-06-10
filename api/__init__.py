import os
import apps

if os.environ.('HEROKU') is not None:
    import logging
    stream_handler = logging.StreamHandler()
    apps.logger.addHandler(stream_handler)
    apps.logger.setLevel(logging.info)
    apps.logger.info('bot startup')
