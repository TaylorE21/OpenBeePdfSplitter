from pathlib import Path

import fitz

from ocr import OCRProcessor


class PdfSplitter:

    def __init__(
            self,
            pattern,
            output):

        self.ocr = OCRProcessor(pattern)

        self.output = Path(output)

        self.output.mkdir(
            exist_ok=True
        )

    def split(
            self,
            filename,
            callback=None):

        pdf = fitz.open(filename)

        current = None

        start = 0

        for index in range(len(pdf)):

            page = pdf[index]

            command = self.ocr.find_command(page)

            if callback:

                callback(index + 1, len(pdf))

            if command:

                if current:

                    self.save(
                        pdf,
                        start,
                        index - 1,
                        current
                    )

                current = command

                start = index

        if current:

            self.save(
                pdf,
                start,
                len(pdf) - 1,
                current
            )

    def save(
            self,
            pdf,
            first,
            last,
            command):

        new = fitz.open()

        new.insert_pdf(
            pdf,
            from_page=first,
            to_page=last
        )

        new.save(
            self.output /
            f"{command}.pdf"
        )

        new.close()
