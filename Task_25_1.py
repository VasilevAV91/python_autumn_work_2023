# Простой вариант
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.res = 0
        self.setWindowTitle('My App')
        self.button = QPushButton(f"{self.res}")

        self.setCentralWidget(self.button)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        print('Clicked!')
        self.res += 1
        self.button.setText(f"{self.res}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()