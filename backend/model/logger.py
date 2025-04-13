
import logging

# Configuração básica para logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    handlers=[
        logging.FileHandler("petshop.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
