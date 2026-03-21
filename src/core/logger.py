import logging
import os

def configurar_logger():
    """Configura o sistema de log básico."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("AutoOrganizer")

logger = configurar_logger()
