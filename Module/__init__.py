from .buttons import get_main_menu from .gban import gban, ungban from .absen import absen, cek_absen from .broadcast import broadcast_message

def initialize(): print("All modules successfully loaded!")

import logging from .config import config

Konfigurasi logging bawaan untuk modul ini

logging.basicConfig(level=logging.INFO) logger = logging.getLogger(name)

logger.info("Package bot trading berhasil diinisialisasi.")

all = ["config"]

