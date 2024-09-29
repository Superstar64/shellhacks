from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QPushButton, QFormLayout
from PySide6.QtCore import Qt


class RegisterDrug(QWidget):
    def __init__(self, database):
        super().__init__()
        self.name = "Register Drug"
        self.database = database

        box = QFormLayout()
        box.setAlignment(Qt.AlignmentFlag.AlignTop)

        drug = QLineEdit()
        box.addRow("Drug", drug)

        confirm = QPushButton("Confirm")
        box.addWidget(confirm)

        def push():
            name = drug.displayText()
            database.execute("insert into drug_type(name) values (?)", (name,))

        confirm.clicked.connect(push)

        self.setLayout(box)

    def update(self):
        pass
