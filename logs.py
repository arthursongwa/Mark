import logging
import os
from datetime import datetime

# Création d’un dossier "logs" s’il n'existe pas
os.makedirs("logs", exist_ok=True)

# Nom de fichier basé sur la date
log_filename = datetime.now().strftime("logs/log_%Y-%m-%d_%H-%M-%S.log")

# Configuration du logging
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,  # DEBUG pour tout loguer (peut être INFO ou WARNING selon ton besoin)
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# Ajout d’un handler console pour afficher les logs en console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logging.getLogger().addHandler(console_handler)