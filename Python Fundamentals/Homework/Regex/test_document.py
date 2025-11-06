import inspect
import os

from unittest import TestCase
from document import PDFDocument, TextDocument


class DocumentTest(TestCase):

    @staticmethod
    def _get_constructor_args(cls):
        return dict(inspect.signature(cls.__init__).parameters)

    def test_inheritance(self):  # [1 points]
        self.assertTrue(issubclass(PDFDocument, TextDocument))

    def test_constructor(self):  # [1 points]
        constructor_args = DocumentTest._get_constructor_args(PDFDocument)
        for arg in ["docid", "filepath", "author"]:
            self.assertIn(arg, constructor_args)
        filepath_dummy_pdf = os.path.join(os.path.dirname(__file__), "dummy.pdf")
        pdf = PDFDocument(docid=1, filepath=filepath_dummy_pdf, author=None)
        self.assertTrue(hasattr(pdf, "text"))
        self.assertTrue(
            pdf.text.startswith("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur imperdiet libero")
        )

    @staticmethod
    def _get_constructor_args(cls):
        """Helper method to get constructor arguments of a class."""
        return cls.__init__.__code__.co_varnames[1:cls.__init__.__code__.co_argcount]

    def test_author(self):  # [1 points]
        from homework.hw03_regex.document import Author
        author_constructor_args = DocumentTest._get_constructor_args(Author)
        for arg in ["firstname", "lastname", "age"]:
            self.assertIn(arg, author_constructor_args)

        pdf_doc_constructor_args = DocumentTest._get_constructor_args(PDFDocument)
        self.assertIn("author", pdf_doc_constructor_args)

    def test_author_initials(self):  # [1 points]
        from homework.hw03_regex.document import Author
        author = Author("John", "Doe", 30)
        self.assertEqual(author.get_initials(), "J.D.")
