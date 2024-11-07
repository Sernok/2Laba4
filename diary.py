from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget, QLabel, QHBoxLayout
import sys


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Записная книжка")
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        # Contact name input
        self.contactName = QLineEdit()
        self.contactName.setPlaceholderText("Имя")

        # Contact number input
        self.contactNumber = QLineEdit()
        self.contactNumber.setPlaceholderText("Телефон")
        # Layout for name and number inputs
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Имя"))
        input_layout.addWidget(self.contactName)
        input_layout.addWidget(QLabel("Телефон"))
        input_layout.addWidget(self.contactNumber)

        # Add the input layout to the main layout
        main_layout.addLayout(input_layout)
        # Add contact button
        self.addContactBtn = QPushButton("Добавить")
        self.addContactBtn.clicked.connect(self.add_contact)
        main_layout.addWidget(self.addContactBtn)
        # Contact list
        self.contactList = QListWidget()
        main_layout.addWidget(self.contactList)

    def add_contact(self):
        # Get the input text from name and number fields
        name = self.contactName.text().strip()
        number = self.contactNumber.text().strip()
        # Only add contact if both fields are filled
        if name and number:
            contact = f"{name} {number}"
            self.contactList.addItem(contact)
            # Clear the input fields after adding
            self.contactName.clear()
            self.contactNumber.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyNotes()
    window.show()
    sys.exit(app.exec_())