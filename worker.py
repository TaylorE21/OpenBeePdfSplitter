from PySide6.QtCore import QObject, Signal

from splitter import PdfSplitter
from settings import Settings


class SplitWorker(QObject):

    progress = Signal(int, int)
    log = Signal(str)
    finished = Signal()
    error = Signal(str)

    def __init__(self, pdf_file, output):

        super().__init__()

        self.pdf_file = pdf_file
        self.output = output

    def run(self):

        try:

            settings = Settings()

            splitter = PdfSplitter(
                settings.ocr_pattern,
                self.output
            )

            self.log.emit("Début du traitement...")

            splitter.split(
                self.pdf_file,
                callback=self.progress.emit
            )

            self.log.emit("Découpage terminé")

        except Exception as e:

            self.error.emit(str(e))

        finally:

            self.finished.emit()
