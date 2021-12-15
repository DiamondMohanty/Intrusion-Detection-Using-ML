APP_CONFIG = {
    'DEV': {
        'PORT': 5000,
        'HOST': '127.0.0.1',
        'WAF': True,
        'DEBUG': True,
        'MODELS': [
            {
                'location': 'models/xss_model.sav',
                'id': 'xss'
            }, {
                'location': 'models/sql_inject_model.sav',
                'id': 'sql_injection'
            },{
                'location': 'models/command_injection_model.sav',
                'id': 'command_injection'
            }

        ],
        'WAF_ENABLED': True,
        'LOG_DIR': '../logs'
    },
    'ENV': 'DEV'
}
