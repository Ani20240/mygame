from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter

class Photoshop:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setGeometry(200, 200, 800, 800)
        self.window.setWindowTitle("Photoshop")
        self.window.show()

        self.layout = QVBoxLayout()

        #სურათის შემოტანა
        self.label_image = QLabel()
        self.image = QPixmap(300, 300)
        self.label_image.setPixmap(self.image)
        self.label_image.setAlignment(Qt.AlignCenter)

        #წარწერა
        self.label = QLabel("Enter Image Name Below:")
        self.label.setFont(QFont("Arial", 20))

        #ტექსტის შესაყვანი არეალის შექმნა
        self.textbox = QTextEdit()
        self.textbox.setMaximumHeight(100)
        self.textbox.setFont(QFont("Arial", 20))

        #ღილაკების შექმნა
        self.button_rotate = QPushButton("Rotated Image")
        self.button_rotate.setMinimumHeight(50)
        self.button_rotate.setFont(QFont("Arial", 20))

        self.button_load = QPushButton("Load Image")
        self.button_load.setMinimumHeight(50)
        self.button_load.setFont(QFont("Arial", 20))

        self.button_blur = QPushButton("Blured Image")
        self.button_blur.setMinimumHeight(50)
        self.button_blur.setFont(QFont("Arial", 20))

        self.button_bl_w = QPushButton("Black_White Image")
        self.button_bl_w.setMinimumHeight(50)
        self.button_bl_w.setFont(QFont("Arial", 20))

        #ღილაკების ფუნქციებთან დაკავშირება
        self.button_load.clicked.connect(lambda: self.on_load(self.textbox.toPlainText()))
        self.button_rotate.clicked.connect(lambda: self.on_rotate())
        self.button_blur.clicked.connect(lambda: self.on_blur())
        self.button_bl_w.clicked.connect(lambda: self.on_black_white())
        #ცალკეული კომპონენტების (ვიჯეტების) ლეიაუთში დამატება
        self.layout.addWidget(self.label_image)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button_load)
        self.layout.addWidget(self.button_rotate)
        self.layout.addWidget(self.button_blur)
        self.layout.addWidget(self.button_bl_w)

        #ლეიაუთის დაკავშირება ფანჯარასთან
        self.window.setLayout(self.layout)
        self.app.exec_()

    def on_load(self, msg):
        try:
            with Image.open(msg) as original:
                #make copy
                self.new_name = "copy_"+msg
                original.save(self.new_name)
            #კოპიოს ეკრანზე გამოტანა
            self.image = QPixmap(self.new_name)
            self.label_image.setPixmap(self.image)
            self.textbox.setText("")
        except:
            self.textbox.setText("No Image Found")

    #დატრიალების ფუნქცია
    def on_rotate(self):
        with Image.open(self.new_name) as copy:
            pic_rotate = copy.transpose(Image.ROTATE_90)
            pic_rotate.save(self.new_name)
            #ფანჯარაში რომ აისახოს ცვლილება
            self.image = QPixmap(self.new_name)
            self.label_image.setPixmap(self.image)

    #გაბუნდოვნების ფუნქცია
    def on_blur(self):
        with Image.open(self.new_name) as copy:
            pic_blur = copy.filter(ImageFilter.BLUR)
            pic_blur.save(self.new_name)
            # ფანჯარაში რომ აისახოს ცვლილება
            self.image = QPixmap(self.new_name)
            self.label_image.setPixmap(self.image)

    def on_black_white(self):
        with Image.open(self.new_name) as copy:
            pic_gray = copy.convert("L")
            pic_gray.save(self.new_name)
            # ფანჯარაში რომ აისახოს ცვლილება
            self.image = QPixmap(self.new_name)
            self.label_image.setPixmap(self.image)





photoshop1 = Photoshop()
