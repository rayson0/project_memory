import sqlite3 as sql
from PyQt6.QtWidgets import QTableWidgetItem


# класс для работы с базой данных
class DataBase:
    def __init__(self):
        with sql.connect('database/database.db', check_same_thread=False) as self.conn:
            self.conn.row_factory = sql.Row
            self.cur = self.conn.cursor()

    def get_rules(self):
        self.cur.execute('''SELECT text FROM rules''')
        return self.cur.fetchone()[0]

    def get_data_results(self):
        self.cur.execute('''SELECT * FROM results''')
        return list(self.cur.fetchall())

    def write_data_results(self, table_widget):
        results = self.get_data_results()
        table_widget.setRowCount(len(results))
        for index_row, row in enumerate(results):
            for index_col, item in enumerate(row):
                table_widget.setItem(index_row, index_col, QTableWidgetItem(str(item)))
        table_widget.resizeColumnsToContents()
