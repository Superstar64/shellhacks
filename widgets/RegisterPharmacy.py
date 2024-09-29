from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QVBoxLayout,
    QPushButton
)
from PySide6.QtCore import (
    Qt
)
class RegisterPharmacy(QWidget):
    def __init__(self, database):
        super().__init__()
        self.name = 'Register Pharamacy'
        self.database = database

        box = QVBoxLayout()
        box.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        company = QLineEdit()
        box.addWidget(company)

        address = QLineEdit()
        box.addWidget(address)

        confirm = QPushButton('Confirm')
        box.addWidget(confirm)

        def push():
            name = company.displayText()
            addr = address.displayText()
            database.execute('insert into pharmacies(name, address) values (?,?)', (name, addr))
        confirm.clicked.connect(push)

        self.setLayout(box)

    def update(self):
        pass