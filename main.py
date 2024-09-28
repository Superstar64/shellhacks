from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton
import sys

app = QApplication(sys.argv)

window = QTabWidget()

addDrug = QWidget()
window.addTab(addDrug, 'Add Drug')

window.show()

sys.exit(app.exec())