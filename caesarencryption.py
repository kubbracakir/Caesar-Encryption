import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Caesar_encryption:
    def __init__(self, text: str, key: int):
        self.text = text
        self.key = key

    def encode(self):
        encoded = ""
        for i in self.text:
            if i.isalpha():
                shift = 65 if i.isupper() else 97
                encoded += chr((ord(i) - shift + self.key) % 26 + shift)
            else:
                encoded += i
        return encoded

    def decode(self, decrypted):
        decoded = ""
        for j in decrypted:
            if j.isalpha():
                shift = 65 if j.isupper() else 97
                decoded += chr((ord(j) - shift - self.key) % 26 + shift)
            else:
                decoded += j
        return decoded

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.text_label = QLabel('Enter text:')
        layout.addWidget(self.text_label)

        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        self.key_label = QLabel('Enter key value:')
        layout.addWidget(self.key_label)

        self.key_input = QLineEdit()
        layout.addWidget(self.key_input)

        self.encode_button = QPushButton('Encode')
        self.encode_button.clicked.connect(self.encode)
        layout.addWidget(self.encode_button)

        self.decode_button = QPushButton('Decode')
        self.decode_button.clicked.connect(self.decode)
        layout.addWidget(self.decode_button)

        self.result_label = QLabel('Result:')
        layout.addWidget(self.result_label)

        self.result_text = QLineEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def encode(self):
        text = self.text_input.text()
        key = int(self.key_input.text())
        caesar = Caesar_encryption(text=text, key=key)
        self.result_text.setText(caesar.encode())

    def decode(self):
        decrypted = self.text_input.text()
        key = int(self.key_input.text())
        caesar = Caesar_encryption(text=decrypted, key=key)
        self.result_text.setText(caesar.decode(decrypted))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())