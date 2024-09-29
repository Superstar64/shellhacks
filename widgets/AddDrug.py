from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QComboBox
)
from PySide6.QtCore import (
    Qt
)

class AddDrug(QWidget):
    def __init__(self, database):
        super().__init__()
        self.name = 'AddDrug'
        self.database = database

    def update(self):
        vBox = QVBoxLayout()
        vBox.setAlignment(Qt.AlignmentFlag.AlignTop)
        drugTypes = QComboBox()
        drugTypesIndex = []
        for (id, name) in self.database.execute('select id, name from drug_type'):
            drugTypesIndex.append((id, name))
            drugTypes.addItem(name)
        
        pharamacies = QComboBox()
        pharamaciesIndex = []
        for (id, name, address) in self.database.execute('select id, name, address from pharmacies'):
            pharamaciesIndex.append((id, name, address))
            pharamacies.addItem(name + ' @ ' + address)

        vBox.addWidget(drugTypes)
        vBox.addWidget(pharamacies)
        self.setLayout(vBox)