from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QPushButton
)
from PySide6.QtCore import (
    Qt
)

class AddInventory(QWidget):
    def __init__(self, database):
        super().__init__()
        self.name = 'Add Inventory'
        self.database = database
        self.base = QVBoxLayout()
        self.base.addWidget(QWidget())
        self.setLayout(self.base)

    def update(self):
        # Qt doesn't support replacing layouts, so wrap it in an object instead
        inner = QWidget()
        self.base.takeAt(0).widget().deleteLater()
        self.base.addWidget(inner)

        vBox = QVBoxLayout()
        inner.setLayout(vBox)
        vBox.setAlignment(Qt.AlignmentFlag.AlignTop)
        drugTypes = QComboBox()
        drugTypesIndex = []
        for (id, name) in self.database.execute('select id, name from drug_type'):
            drugTypesIndex.append(id)
            drugTypes.addItem(name)
        
        pharamacies = QComboBox()
        pharamaciesIndex = []
        for (id, name, address) in self.database.execute('select id, name, address from pharmacies'):
            pharamaciesIndex.append(id)
            pharamacies.addItem(name + ' @ ' + address)

        vBox.addWidget(drugTypes)
        vBox.addWidget(pharamacies)
        confirm = QPushButton('Confirm')
        def push():
            drugTypeId = drugTypesIndex[drugTypes.currentIndex()]
            pharamacyId = pharamaciesIndex[pharamacies.currentIndex()]
            self.database.execute('insert into inventory(drug_type_id, pharmacy_id) values(?, ?)', (drugTypeId, pharamacyId))
        confirm.clicked.connect(push)
        vBox.addWidget(confirm)
        inner.setLayout(vBox)