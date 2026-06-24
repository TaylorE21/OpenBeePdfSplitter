from pathlib import Path
from datetime import datetime
import csv


class CsvLogger:

    def __init__(self):

        self.directory = Path("logs")

        self.directory.mkdir(exist_ok=True)

        self.file = self.directory / "log.csv"

        if not self.file.exists():

            with open(
                self.file,
                "w",
                newline="",
                encoding="utf-8"
            ) as f:

                writer = csv.writer(f)

                writer.writerow(
                    [
                        "date",
                        "pdf",
                        "commande",
                        "pages"
                    ]
                )

    def write(
            self,
            pdf,
            commande,
            pages):

        with open(
                self.file,
                "a",
                newline="",
                encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow(
                [
                    datetime.now(),
                    pdf,
                    commande,
                    pages
                ]
            )
