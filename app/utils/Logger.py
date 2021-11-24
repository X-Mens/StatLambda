LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            "datefmt": '%Y-%m-%d %H:%M:%S %p',
            'format': '%(levelname)s | %(module)s | %(message)s'
        },
    },
    'handlers': {
        'default': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        },
        'app': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        }
    }
}
