from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel
import sys

app = QApplication(sys.argv)

window = QTabWidget()

addDrug = QWidget()
vBox = QVBoxLayout()
intro = QLabel("This is a Program for logging newly created drugs")
vBox.addWidget(intro)


addDrug.setLayout(vBox)
window.addTab(addDrug, 'Add Drug')


registerPharmacy = QWidget()
window.addTab(registerPharmacy, "Register Pharmacy")

window.show()

sys.exit(app.exec())