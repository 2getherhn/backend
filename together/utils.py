import logging


def user_is_authenticated(user):
    if not hasattr(user.is_authenticated, '__call__'):
        return user.is_authenticated
    else:
        return user.is_authenticated()


def get_logger(name=__name__):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
