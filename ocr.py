import re
import fitz
import pytesseract

from PIL import Image


class OCRProcessor:

    def __init__(self, pattern):

        self.pattern = re.compile(
            pattern,
            re.IGNORECASE
        )

    def find_command(self, page):

        # 1 - Texte natif

        text = page.get_text()

        result = self.pattern.search(text)

        if result:

            return result.group(1)

        # 2 - OCR

        pix = page.get_pixmap(dpi=300)

        image = Image.frombytes(
            "RGB",
            [pix.width, pix.height],
            pix.samples
        )

        text = pytesseract.image_to_string(
            image,
            lang="fra"
        )

        result = self.pattern.search(text)

        if result:

            return result.group(1)

        return None
