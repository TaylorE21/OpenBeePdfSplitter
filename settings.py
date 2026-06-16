from configparser import ConfigParser
from pathlib import Path


class Settings:

    def __init__(self):

        self.config = ConfigParser()

        self.file = Path("config.ini")

        if self.file.exists():
            self.config.read(self.file, encoding="utf-8")

    @property
    def ocr_pattern(self):

        return self.config.get(
            "OCR",
            "pattern",
            fallback="Num\\s+Commande\\s+Open\\s+Bee"
        )

    @property
    def language(self):

        return self.config.get(
            "GENERAL",
            "language",
            fallback="fra"
        )
