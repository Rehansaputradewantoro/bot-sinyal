init.py

import logging from .config import config

Konfigurasi logging bawaan untuk modul ini

logging.basicConfig(level=logging.INFO) logger = logging.getLogger(name)

logger.info("Package bot trading berhasil diinisialisasi.")

all = ["config"]

