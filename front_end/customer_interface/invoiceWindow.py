import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ..config.font import font


# Index 0: Car ID
# Index 1: Mileage
# Index 2: MPG
# Index 3: Price
# Index 4: Car Year
# Index 5: Car Model
# Index 6: Car Make
# Index 7: Car Color
# Index 8: Car Type
class invoice_window(QWidget):
    """
    A class that makes a invoice window to show the information for the reservation that was made when make was pressed.
    """

    def __init__(self, customer_window, car, num_days, start_date, end_date, ins):
        """
        Initalizes the invoice class window.
        """
        super().__init__()
        # setup main layout
        self.customer_window = customer_window
        self.main_layout = QVBoxLayout(self)
        self.car = []
        self.car = car
        self.num_days = num_days
        self.start_date = start_date
        self.end_date = end_date
        self.ins = ins

        # setup font
        self.set_font = font()
        self.font = QFont(self.set_font.font_family, 16)

        self.setup_main()

    def setup_form(self):
        """
        function to set up parameters for the form, makes the widgets, and adds them to the form.
        """
        self.form = QWidget()
        self.form_layout = QFormLayout(self.form)
        self.start = QLabel("Pick Up Date: " + self.start_date.toString("yyyy-MM-dd"))
        self.end = QLabel("Return Date: " + self.end_date.toString("yyyy-MM-dd"))
        self.Mileage = QLabel("Mileage: " + str(self.car[1]))
        self.MPG = QLabel("MPG: " + str(self.car[2]))
        self.Price = QLabel("Price: " + str(self.car[3] * self.num_days))
        self.Car_Year = QLabel("Car Year: " + str(self.car[4]))
        self.Car_Model = QLabel("Car Model: " + str(self.car[5]))
        self.Car_Make = QLabel("Car Make: " + str(self.car[6]))
        self.Car_Color = QLabel("Car Color: " + str(self.car[7]))
        self.Car_Type = QLabel("Car Type: " + str(self.car[8]))
        self.check_insurance = QLabel()

        # sets the text for if insurance is included
        if self.ins == 1:
            self.check_insurance.setText("Insurance Included: Yes")
        else:
            self.check_insurance.setText("Insurance Included: No")

        self.home_button = QPushButton("Home")
        self.home_button.setFixedSize(100, 50)
        self.home_button.setFont(self.font)
        self.home_button.setStyleSheet(
            "color: white; background:#efbe25; border-radius: 5px; outline: none;"
        )
        self.form_layout.addRow(self.start)
        self.form_layout.addRow(self.end)
        self.form_layout.addRow(self.Mileage)
        self.form_layout.addRow(self.MPG)
        self.form_layout.addRow(self.Price)
        self.form_layout.addRow(self.Car_Year)
        self.form_layout.addRow(self.Car_Model)
        self.form_layout.addRow(self.Car_Make)
        self.form_layout.addRow(self.Car_Color)
        self.form_layout.addRow(self.Car_Type)
        self.form_layout.addRow(self.check_insurance)
        self.form_layout.addRow(self.home_button)
        self.home_button.clicked.connect(self.clicked_home)

    def clicked_home(self):
        """
        function for when home button is clicked to go back to the start window.
        """
        self.customer_window.bottom_layout.setCurrentIndex(0)

    def setup_main(self):
        """
        fucntion to set up the main layout.
        """
        self.setup_form()
        self.main_layout.addWidget(self.form, alignment=Qt.AlignCenter)


if __name__ == "__main__":
    import sys

    from ..config.screenConfig import screen_config

    screen_config = screen_config()
    app = QApplication(sys.argv)
    list = []
    window = invoice_window()
    window.show()
    sys.exit(app.exec_())
