from PySide6.QtWidgets import QWidget

class ViewDrug(QWidget):
    def __init__(self, database):
        super().__init__()
        self.name = 'List of Drugs'

    def update(self):
        pass