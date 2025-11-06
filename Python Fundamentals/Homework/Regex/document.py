from collections import Counter

from PyPDF2 import PdfReader
from nltk import word_tokenize
import PyPDF2


def load_pdf(path: str):
    with open(path, "rb") as f:
        pdf: PdfReader = PyPDF2.PdfReader(f)
        text: str = " ".join(page.extract_text() for page in pdf.pages)
    return text


class TextDocument:
    def __init__(self, docid: int, text: str):
        """ This creates a TextDocument instance with a string, a dictionary and an identifier. """
        self.text: str = text
        self.docid: int = docid
        self.word_to_count: Counter = Counter(self.normalized_tokens(text))

    @classmethod
    def normalized_tokens(cls, text: str):
        """ This takes a string and returns lower-case tokens, using nltk for tokenization. """
        return [w.lower() for w in word_tokenize(text)]

    @classmethod
    def from_file(cls, filename: str):
        """ This creates a TextDocument instance by reading a file. """
        with open(filename) as f:
            text: str = f.read().strip()
        return cls(text, filename)


# TODO: Inherit from TextDocument
class PDFDocument(TextDocument):
    # TODO: implement constructor (use load_pdf() and call parent constructor)
    def __init__(self, docid: int, text: str, path: str):
        TextDocument.__init__(self, docid, text)
        self.pdf: str = load_pdf(path)


class Author:
    # TODO: Implement the constructor of Author class
    def __init__(self, first_name: str, last_name: str):
        self.first_name: str = first_name
        self.last_name: str = last_name

    # TODO: Add a method get_initials() that returns the initials of the author's first and last names in uppercase, e.g., "J.D."
    def get_initials(self):
        return self.first_name[0].upper() + self.last_name[0].upper()
