from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QPushButton, QFormLayout
from PySide6.QtCore import Qt


class RegisterPharmacy(QWidget):
    def __init__(self, database):
        super().__init__()
        self.name = "Register Pharamacy"
        self.database = database

        box = QFormLayout()
        box.setAlignment(Qt.AlignmentFlag.AlignTop)

        company = QLineEdit()
        box.addRow("Company", company)

        address = QLineEdit()
        box.addRow("Address", address)

        confirm = QPushButton("Confirm")
        box.addWidget(confirm)

        def push():
            name = company.displayText()
            addr = address.displayText()
            database.execute(
                "insert into pharmacies(name, address) values (?,?)", (name, addr)
            )

        confirm.clicked.connect(push)

        self.setLayout(box)

    def update(self):
        pass
