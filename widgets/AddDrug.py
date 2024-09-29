from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QComboBox
)

class AddDrug(QWidget):
    def __init__(self, database):
        super().__init__()
        self.name = 'AddDrug'
        self.database = database

    def update(self):
        vBox = QVBoxLayout()
        drugTypes = QComboBox()
        drugTypesIndex = []
        for (id, name) in self.database.execute('select id, name from drug_type'):
            drugTypesIndex.append((id, name))
            drugTypes.addItem(name)
            
        vBox.addWidget(drugTypes)
        self.setLayout(vBox)