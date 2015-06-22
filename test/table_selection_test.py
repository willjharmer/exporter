from test import *
from wtforms_test import FormTestCase

class TestExportForm(FormTestCase):
    form_class = ExportForm

    def has_expected_field(self):
        self.assert_has("tables")

    def test_choices_come_from_database(self):
        self.assert_choices("tables", [("TableA","TableA"),("DataTableB","DataTableB"),("DataTableC","DataTableC")])
