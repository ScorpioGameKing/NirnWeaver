from textual.app import ComposeResult
from textual.widgets import DataTable

class OrderPanel:
    _HEADERS = []
    _ROWS = []

    table:DataTable

    def __init__(self, headers, initial_rows):
        self._HEADERS = headers
        self._ROWS = initial_rows
        self.table = DataTable()
        self.table.id = "load_order"
        
    def show_table(self) -> DataTable:
        return self.table

    def build_table(self):
        self.table.zebra_stripes = True
        self.table.add_columns(*self._HEADERS[0])
        self.table.add_rows(self._ROWS[0:])

    def add_row(self, row):
        self._ROWS.append(row)
        self.table.add_row(*row)

    def add_rows(self, rows):
        self.table.add_rows(rows[0:])
