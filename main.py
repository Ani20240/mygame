# აპლიკაციისთვის საჭირო მოდულების შემოტანა
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def on_click():
    print("Math, History and sport")
def main():
    #აპლიკაციის შექმნა
    app = QApplication([])
    #ფანჯრის შექმნა
    window = QWidget()

    #ფანჯრის ლოკაცია და ზომები
    window.setGeometry(200, 200, 600, 200)
    #ფანჯრის სახელის შეცვლა
    window.setWindowTitle("First App")

    #ელემენტების განლაგების წესის შექმნა
    layout = QVBoxLayout()

    #პირველი ელემენტის ანუ ვიჯეტის შექმნა
    label = QLabel("Guess what is Antony's favorite subject(first answer and than click the button!)")
    #წარწერის ფონტის და ზომის ცვლილება
    label.setFont(QFont("Arial", 26))

    #ღილაკის შექმნა
    button = QPushButton("Show answer")
    #ღილაკის დაჭერის შემთხვევაში რა გააკეთოს
    button.clicked.connect(on_click)

    #ელემენტის განაწილების წესისთვის ელემენტის გადაცემა
    layout.addWidget(label)
    layout.addWidget(button)

    #ფანჯარას ვუკავშირებ ელემენტების განლაგების წესს
    window.setLayout(layout)
    #ფანჯრის გამოჩენა
    window.show()
    #აპლიკაციის გაშვება
    app.exec_()
main()
   