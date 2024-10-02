from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from font import font

class login(QWidget):
    def __init__(self):
        super().__init__()
        # Set the background color of the main window to dark grey
        self.setStyleSheet("background-color:darkgrey;")

        #set up logo img
        self.logo = QLabel(self)
        self.pixmap = QPixmap("logo/FullLogo.png")
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(self.pixmap.width(), self.pixmap.height())
        self.scaled_pixmap = self.pixmap.scaled(700, 700, aspectRatioMode=1)  # width, height
        self.logo.setPixmap(self.scaled_pixmap)
        self.logo.setStyleSheet("border: none;")

        # Set up the font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)
        #self.font.setBold(True)

        # Set up the main layout
        self.login_layout = QVBoxLayout(self)
        self.login_layout.setContentsMargins(0, 0, 0, 0)
        self.login_layout.setSpacing(0)

        # Create the inner login window
        self.login_window = QWidget(self)
        self.login_window.setFixedWidth(800)
        self.login_window.setFixedHeight(1200)

        # Add a margin around the login window to make the dark grey background visible
        self.login_layout.setContentsMargins(20, 20, 20, 20)  # Adjust the margin size as needed

        # Create label and set font
        self.admin_label = QLabel("ADMIN", self)
        self.admin_label.setFont(self.font)
        self.admin_label.setStyleSheet("border: none;")

        # Password box
        self.pw_box = QLineEdit(self)
        self.pw_box.setPlaceholderText("Enter Password")
        self.pw_box.setFixedWidth(600)
        self.pw_box.setFixedHeight(80)
        self.pw_box.setEchoMode(QLineEdit.Password)
        self.pw_box.setStyleSheet(
            "background-color:white;"
            "border : 1px solid lightgrey;"
            "border-radius : 5px;"
        )

        # Login button
        self.login_button = QPushButton("Login", self)
        self.login_button.setFont(self.font)
        self.login_button.setFixedWidth(250)
        self.login_button.setFixedHeight(80)
        self.login_button.setStyleSheet(
            "background-color:white;"
            "border : 1px solid lightgrey;"
            "border-radius : 5px;"
        )

        # Style for the login window
        self.login_window.setStyleSheet(
            "background-color:white;"
            "border : 3px solid lightgrey;"
            "border-radius: 25px;"
        )

        # Layout for the inner login window
        self.login_window_layout = QVBoxLayout(self.login_window)
        self.login_window_layout.addStretch()
        self.login_window_layout.addWidget(self.logo, alignment=Qt.AlignCenter)
        self.login_window_layout.addStretch()
        self.login_window_layout.addWidget(self.admin_label, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.pw_box, alignment=Qt.AlignCenter)
        self.login_window_layout.addWidget(self.login_button, alignment=Qt.AlignCenter)
        self.login_window_layout.addStretch()

        # Add the login window to the main layout, centering it
        self.login_layout.addWidget(self.login_window, alignment=Qt.AlignCenter)

