# აპლიკაციისთვის საჭირო მოდულების შემოტანა
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
data = [["what is Antony's favorite color?", "green"], ["How many planets are in our solar system?", "eight"],
        ["Who is Donald Trump?", "President"]]
i = 0
value = False
label = ""


def main():
    global i, value, label
    app = QApplication([])
    window = QWidget()

    window.setGeometry(100, 100, 500, 500)
    window.setWindowTitle("Quizz")

    layout = QVBoxLayout()

    label = QLabel(data[i][0])
    label.setFont(QFont("Arial", 16))

    # ტექსტის შემყვანი ელემენტის შექმნა
    textbox = QTextEdit()
    textbox.setFont(QFont("Arial", 16))

    button = QPushButton("Answer")
    button.clicked.connect(lambda: on_click(textbox.toPlainText()))

    # ღილაკის სიმაღლის რეგულირება
    button.setMinimumHeight(50)

    # ღილაკის წარწერის ზომა
    button.setFont(QFont("Arial", 16))

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    app.exec_()


def on_click(msg):
    global i, value
    # მესიჯის ყუთის შექმნა
    message = QMessageBox()

    # მესიჯის ყუთში ინფოს გამოტანა
    value = msg.lower() == data[i][1].lower()
    message.setText(str(value))

    # მესიჯის ყუთის გაშვება
    message.exec_()

    if value and i < len(data) - 1:
        i += 1
        value = False
    else:
        label.setText("Victory!")

    label.setText(data[i][0])


main()