from lib.secret_loader import get_secret
import os
from lib.secret_loader import get_secret

# eth node rpc request
ETH_RPC_URL = os.environ.get('ETH_RPC_URL', 'https://arbitrum-rinkeby.infura.io/v3/a19213eecc2e4a35bde97885da9e8bd8')

# timeout for get transaction receipt(second)
TX_TIMEOUT = os.environ.get('TX_TIMEOUT', 300)
KEEPER_KEY = get_secret('dev/mai3-keeper/key_file')

# gas price
GAS_PRICE = os.environ.get('GAS_PRICE', 1)

# contract address
MAX_NUM = int(os.environ.get('MAX_NUM', 100))
IS_USE_WHITELIST = os.environ.get('IS_USE_WHITELIST', True)
PERPETUAL_LIST = os.environ.get('PERPETUAL_LIST', '["0xc32a2dfee97e2babc90a2b5e6aef41e789ef2e13-0"]')
# notice lowercase
POOL_BLACK_LIST = os.environ.get('POOL_BLACK_LIST', '[]')
READER_ADDRESS = os.environ.get('READER_ADDRESS', '0x49354B337395dB4d23F71a1f74E080A10a6AcF0C')
IS_TAKE_OVER = os.environ.get('IS_TAKE_OVER', False)

# mcdex perpetual graph
GRAPH_URL = os.environ.get('GRAPH_URL', 'https://api.thegraph.com/subgraphs/name/mcdexio/mcdex3-kovan1')

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {
            "format": "%(asctime)s %(levelname)-7s - %(message)s - [%(filename)s:%(lineno)d:%(funcName)s]",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "./log/keeper.log",
            "maxBytes": 104857600, # 100MB
            "backupCount": 7,
            "encoding": "utf8"
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    }
}
