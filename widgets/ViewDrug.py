from PySide6.QtWidgets import (
    QWidget,
    QTableWidget,
    QVBoxLayout,
    QTableWidgetItem
)

class ViewDrug(QWidget):
    def __init__(self, database):
        super().__init__()
        self.name = 'List of Drugs'
        self.database = database
        self.base = QVBoxLayout()
        self.base.addWidget(QWidget())
        self.setLayout(self.base)

    def update(self):
        # Qt doesn't support replacing layouts, so wrap it in an object instead
        inner = QWidget()
        self.base.itemAt(0).widget().deleteLater()
        self.base.addWidget(inner)

        data = []
        for item in self.database.execute('select drug_id, drug_type.name, pharmacies.name, pharmacies.address from inventory, drug_type, pharmacies where drug_type.id = drug_type_id and pharmacies.id = pharmacy_id'):
            data.append(item)
        
        table = QTableWidget(len(data), 4)
        table.setColumnWidth(3, 300)
        table.setHorizontalHeaderLabels(['Drug Id', 'Drug', 'Pharmacy', 'Address'])
        index = 0
        for (id, drug, pharamacy, address) in data:
            table.setItem(index, 0, QTableWidgetItem(str(id)))
            table.setItem(index, 1, QTableWidgetItem(str(drug)))
            table.setItem(index, 2, QTableWidgetItem(str(pharamacy)))
            table.setItem(index, 3, QTableWidgetItem(str(address)))
            index += 1

        box = QVBoxLayout()
        box.addWidget(table)

        inner.setLayout(box)