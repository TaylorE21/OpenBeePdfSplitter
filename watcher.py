import time
from pathlib import Path

from splitter import PdfSplitter
from settings import Settings
from logger import logger


class FolderWatcher:

    def __init__(self):

        self.settings = Settings()

        self.running = True

    def stop(self):

        self.running = False

    def run(self):

        input_dir = Path(self.settings.input_directory)

        output_dir = Path(self.settings.output_directory)

        splitter = PdfSplitter(
            self.settings.ocr_pattern,
            output_dir
        )

        logger.info("Surveillance démarrée")

        while self.running:

            pdfs = list(input_dir.glob("*.pdf"))

            for pdf in pdfs:

                try:

                    logger.info(f"Traitement : {pdf.name}")

                    splitter.split(str(pdf))

                    if self.settings.delete_source:

                        pdf.unlink()

                        logger.info(
                            f"Suppression : {pdf.name}"
                        )

                except Exception as e:

                    logger.exception(e)

            time.sleep(self.settings.watch_interval)
