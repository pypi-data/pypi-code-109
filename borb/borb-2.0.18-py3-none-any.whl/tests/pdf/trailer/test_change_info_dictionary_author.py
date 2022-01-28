import unittest
from datetime import datetime
from pathlib import Path

from borb.io.read.types import Decimal, Dictionary, Name, String
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.table.fixed_column_width_table import (
    FixedColumnWidthTable as Table,
)
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF

unittest.TestLoader.sortTestMethodsUsing = None


class TestChangeInfoDictionaryAuthor(unittest.TestCase):
    """
    This test attempts to read the DocumentInfo for each PDF in the corpus
    """

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        # find output dir
        p: Path = Path(__file__).parent
        while "output" not in [x.stem for x in p.iterdir() if x.is_dir()]:
            p = p.parent
        p = p / "output"
        self.output_dir = Path(p, Path(__file__).stem.replace(".py", ""))
        if not self.output_dir.exists():
            self.output_dir.mkdir()

    def test_write_document(self):

        # create document
        pdf = Document()

        # add page
        page = Page()
        pdf.append_page(page)

        # add test information
        layout = SingleColumnLayout(page)
        layout.add(
            Table(number_of_columns=2, number_of_rows=3)
            .add(Paragraph("Date", font="Helvetica-Bold"))
            .add(Paragraph(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))
            .add(Paragraph("Test", font="Helvetica-Bold"))
            .add(Paragraph(Path(__file__).stem))
            .add(Paragraph("Description", font="Helvetica-Bold"))
            .add(
                Paragraph(
                    "This test creates a PDF with an empty Page, and a Paragraph of text. "
                    "A subsequent test will change the info dictionary of this PDF."
                )
            )
            .set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        )

        layout.add(
            Paragraph(
                """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            """,
                font_size=Decimal(10),
                vertical_alignment=Alignment.TOP,
                horizontal_alignment=Alignment.LEFT,
                padding_top=Decimal(5),
                padding_right=Decimal(5),
                padding_bottom=Decimal(5),
                padding_left=Decimal(5),
            )
        )

        pdf["XRef"]["Trailer"][Name("Info")] = Dictionary()
        pdf["XRef"]["Trailer"]["Info"][Name("Author")] = String("Joris Schellekens")

        # attempt to store PDF
        with open(self.output_dir / "output_001.pdf", "wb") as out_file_handle:
            PDF.dumps(out_file_handle, pdf)

    def test_read_document_info_dictionary_raw(self):

        doc = None
        with open(self.output_dir / "output_001.pdf", "rb") as pdf_file_handle:
            doc = PDF.loads(pdf_file_handle)

        assert doc is not None
        assert "XRef" in doc
        assert "Trailer" in doc["XRef"]
        assert "Info" in doc["XRef"]["Trailer"]
        assert "Author" in doc["XRef"]["Trailer"]["Info"]
        assert doc["XRef"]["Trailer"]["Info"]["Author"] == "Joris Schellekens"

    def test_read_document_info_dictionary_convenience(self):

        doc = None
        with open(self.output_dir / "output_001.pdf", "rb") as pdf_file_handle:
            doc = PDF.loads(pdf_file_handle)

        assert doc.get_document_info().get_author() == "Joris Schellekens"

    def test_change_document_info_dictionary(self):
        doc = None
        with open(self.output_dir / "output_001.pdf", "rb") as pdf_file_handle:
            doc = PDF.loads(pdf_file_handle)

        assert doc is not None
        assert "XRef" in doc
        assert "Trailer" in doc["XRef"]
        assert "Info" in doc["XRef"]["Trailer"]
        assert "Author" in doc["XRef"]["Trailer"]["Info"]
        doc["XRef"]["Trailer"]["Info"][Name("Author")] = String("Boris Schellekens")

        # attempt to store PDF
        with open(self.output_dir / "output_002.pdf", "wb") as out_file_handle:
            PDF.dumps(out_file_handle, doc)

    def test_read_document_info_dictionary_convenience_002(self):

        doc = None
        with open(self.output_dir / "output_002.pdf", "rb") as pdf_file_handle:
            doc = PDF.loads(pdf_file_handle)

        assert doc.get_document_info().get_author() == "Boris Schellekens"


if __name__ == "__main__":
    unittest.main()
