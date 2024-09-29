from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

class AddDrug(QWidget):
    def __init__(self, cursor):
        super().__init__()
        self.name = 'AddDrug'

    def update(self):
        vBox = QVBoxLayout()
        intro = QLabel("This is a Program for logging newly created drugs")
        vBox.addWidget(intro)
        self.setLayout(vBox)