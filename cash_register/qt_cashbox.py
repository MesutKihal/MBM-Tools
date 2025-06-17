from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1050, 768)
        self.setWindowTitle('Cashbox Desktop')
        self.widgets()
        self.showMaximized()
        
    def widgets(self):
        # Body Section
        self.main = QFrame()
        self.body = QGridLayout(self.main)
        self.setCentralWidget(self.main)

###################################### Cash Register Page #############################################################
        
        self.__cash_register_div = QFrame()
        self.__cash_register_layout = QGridLayout(self.__cash_register_div)

        # Search Bar (CRT)
        self.__search_bar = QLineEdit()
        self.__search_bar.setPlaceholderText("Type the title of the product you want to add")
        self.__cash_register_layout.addWidget(self.__search_bar, 1, 0, 1, 2)

        # Search or Scan button (CRT)
        self.__search_btn = QPushButton("Scan Barcode")
        self.__search_btn.setIcon(QIcon("assets\\img\\webcam.png"))
        self.__search_btn.setIconSize(QSize(30, 20))
        self.__cash_register_layout.addWidget(self.__search_btn, 1, 2, 1, 1)
        
        # Products Table (CRT)
        self.__products_table = QTableWidget()
        self.__products_table.setColumnCount(5)
        self.__products_table.setRowCount(12)
        self.__products_table.setAlternatingRowColors(True)
        self.__products_table.setHorizontalHeaderLabels(["Title", "Category", "Price", "In Stock", "Expiration"])
        self.__products_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        for row in range(3):
            for col in range(3):
                item = QTableWidgetItem(f"Row {row+1}, Col {col+1}")
                self.__products_table.setItem(row, col, item)
        self.__cash_register_layout.addWidget(self.__products_table, 2, 0, 7, 3)

        # Customer Select (CRT)
        self.__customer_select = QComboBox()
        self.__customer_select.addItems(['One', 'Two',  'Three', 'Four', 'Five'])
        self.__customer_select.setStyleSheet("font-size: 18px;")
        self.__cash_register_layout.addWidget(self.__customer_select, 1, 3, 1, 3)

        # Bill Label (CRT)
        self.__total_label = QLabel("BILL")
        self.__total_label.setAlignment(Qt.AlignCenter)
        self.__total_label.setStyleSheet("font-size: 20px;")
        self.__cash_register_layout.addWidget(self.__total_label, 2, 3, 1, 3)

        # Bill List (CRT)
        self.__bill_list = QListWidget()
        self.__bill_list.setStyleSheet("font-size: 18px;padding: 5px;border: 1px solid #ddd;")
        self.__bill_list.addItem(QListWidgetItem("PRICE \t| PRODUCT TITLE"))
        self.__cash_register_layout.addWidget(self.__bill_list, 3, 3, 1, 3)

        # Total Label (CRT)
        self.__total_label = QLabel("TOTAL")
        self.__total_label.setAlignment(Qt.AlignCenter)
        self.__total_label.setStyleSheet("font-size: 18px;color: white;background: black;border: 1px solid #ddd;")
        self.__cash_register_layout.addWidget(self.__total_label, 6, 3, 1, 1)
        
        # Total (CRT)
        self.__total_ = QLabel("دج 0.00")
        self.__total_.setAlignment(Qt.AlignCenter)
        self.__total_.setStyleSheet("font-size: 20px;color: red;")
        self.__cash_register_layout.addWidget(self.__total_, 7, 3, 1, 1)
        
        # Bill Buttons (CRT)
        self.__print_btn = QPushButton("Print")
        self.__print_btn.setIcon(QIcon("assets\\img\\printing.png"))
        self.__print_btn.setIconSize(QSize(30, 40))
        self.__cash_register_layout.addWidget(self.__print_btn, 6, 4, 1, 1)
        
        self.__undo_btn = QPushButton("Undo")
        self.__undo_btn.setIcon(QIcon("assets\\img\\undo.png"))
        self.__undo_btn.setIconSize(QSize(30, 40))
        self.__cash_register_layout.addWidget(self.__undo_btn, 6, 5, 1, 1)
        
        self.__clear_btn = QPushButton("Clear")
        self.__clear_btn.setIcon(QIcon("assets\\img\\bin.png"))
        self.__clear_btn.setIconSize(QSize(30, 40))
        self.__cash_register_layout.addWidget(self.__clear_btn, 7, 4, 1, 1)
        
        self.__mail_btn = QPushButton("Mail")
        self.__mail_btn.setIcon(QIcon("assets\\img\\email.png"))
        self.__mail_btn.setIconSize(QSize(30, 40))
        self.__cash_register_layout.addWidget(self.__mail_btn, 7, 5, 1, 1)
######################################################################################################################
########################################### Inventory Page ###########################################################
        
        self.__inventory_div = QFrame()
        self.__inventory_layout = QGridLayout(self.__inventory_div)
        
        # Search Bar (INV)
        self.__inv_search_bar = QLineEdit()
        self.__inv_search_bar.setPlaceholderText("Type the title of the product you want to add")
        self.__inventory_layout.addWidget(self.__inv_search_bar, 1, 0, 1, 6)
        
        # Search Button (INV)
        self.__inv_search_btn = QPushButton("Search")
        self.__inv_search_btn.setIcon(QIcon("assets\\img\\search.png"))
        self.__inv_search_btn.setIconSize(QSize(30, 40))
        self.__inventory_layout.addWidget(self.__inv_search_btn, 1, 6)
        
        # Products Table (INV)
        self.__inventory_table = QTableWidget()
        self.__inventory_table.setColumnCount(5)
        self.__inventory_table.setRowCount(14)
        self.__inventory_table.setHorizontalHeaderLabels(["Title", "Category", "Price", "In Stock", "Expiration"])
        self.__inventory_table.setAlternatingRowColors(True)
        self.__inventory_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.__inventory_layout.addWidget(self.__inventory_table, 2, 0, 3, 7)

        # Add Product (INV)
        self.__add_product_button = QPushButton("Add new product")
        self.__add_product_button.setIcon(QIcon("assets\\img\\add.png"))
        self.__add_product_button.setIconSize(QSize(30, 40))
        self.__add_product_button.setStyleSheet("background: #90EE90;")
        self.__inventory_layout.addWidget(self.__add_product_button, 5, 3)
 
        # Product Card (INV)
        self.__product_card = QFrame()
        self.__card_layout = QVBoxLayout(self.__product_card)
        self.__inventory_layout.addWidget(self.__product_card, 1, 8, 5, 1)
        
        
        # Product Image (INV)
        self.__product_image = QPixmap("assets\\img\\noimage.jpg")
        self.__product_image = self.__product_image.scaled(300, 300, Qt.KeepAspectRatio)
        self.__img_container = QLabel()
        self.__img_container.setPixmap(self.__product_image)
        self.__card_layout.addWidget(self.__img_container)
        
        # Product ID (INV)
        self.__product_id = QLabel("Product ID (Barcode, QRCode, REF)")
        self.__product_id.setFont(QFont("consolas", 14))
        self.__product_id.setStyleSheet("background: #fff;border-radius: none;")
        self.__card_layout.addWidget(self.__product_id)
        
        # Product Title (INV)
        self.__product_title = QLabel("Product Title")
        self.__product_title.setFont(QFont("consolas", 14))
        self.__product_title.setStyleSheet("background: #D5EDC8;border-radius: none;")
        self.__card_layout.addWidget(self.__product_title)
        
        # Product Category (INV)
        self.__product_category = QLabel("Product Category")
        self.__product_category.setFont(QFont("consolas", 14))
        self.__product_category.setStyleSheet("background: #fff;border-radius: none;")
        self.__card_layout.addWidget(self.__product_category)
        
        # Product Price (INV)
        self.__product_price = QLabel("Product Price")
        self.__product_price.setFont(QFont("consolas", 14))
        self.__product_price.setStyleSheet("background: #D5EDC8;border-radius: none;")
        self.__card_layout.addWidget(self.__product_price)
        
        # Product Quantity (INV)
        self.__product_quantity = QLabel("Product Quantity")
        self.__product_quantity.setFont(QFont("consolas", 14))
        self.__product_quantity.setStyleSheet("background: #fff;border-radius: none;")
        self.__card_layout.addWidget(self.__product_quantity)
        
        # Product Experation (INV)
        self.__product_exp_date = QLabel("Product Experation Date")
        self.__product_exp_date.setFont(QFont("consolas", 14))
        self.__product_exp_date.setStyleSheet("background: #D5EDC8;border-radius: none;")
        self.__card_layout.addWidget(self.__product_exp_date)
        
        # Edit Product (INV)
        self.__edit_product_button = QPushButton("Edit Product")
        self.__edit_product_button.setIcon(QIcon("assets\\img\\edit.png"))
        self.__edit_product_button.setIconSize(QSize(30, 40))
        self.__card_layout.addWidget(self.__edit_product_button)
        
######################################################################################################################
########################################### Add Product Page #########################################################
  
        self.__add_product_div = QFrame()
        self.__add_product_div.setFixedSize(1100, 550)
        self.__add_product_layout = QGridLayout(self.__add_product_div)
        
        # Product Image (INV)
        self.__add_product_image = QPixmap("assets\\img\\noimage.jpg")
        self.__add_product_image = self.__product_image.scaled(400, 400, Qt.KeepAspectRatio)
        self.__add_product_img_container = QLabel()
        self.__add_product_img_container.setPixmap(self.__add_product_image)
        self.__add_product_img_btn = QPushButton("Insert Image")
        self.__add_product_layout.addWidget(self.__add_product_img_container, 0, 0, 11, 1)
        self.__add_product_layout.addWidget(self.__add_product_img_btn, 12, 0)
        
        
        # Product ID (INV_ADD)
        self.__add_product_id_label = QLabel("PRODUCT ID, BARCODE or QRCODE")
        self.__add_product_id = QLineEdit()
        self.__add_product_id.setFont(QFont("consolas", 14))
        self.__add_product_layout.addWidget(self.__add_product_id_label, 0, 1)
        self.__add_product_layout.addWidget(self.__add_product_id, 1, 1)
        
        # Product Title (INV_ADD)
        self.__add_product_title_label = QLabel("PRODUCT TITLE")
        self.__add_product_title = QLineEdit()
        self.__add_product_title.setFont(QFont("consolas", 14))
        self.__add_product_layout.addWidget(self.__add_product_title_label, 2, 1)
        self.__add_product_layout.addWidget(self.__add_product_title, 3, 1)
        
        # Product Category (INV_ADD)
        self.__add_product_category_label = QLabel("PRODUCT CATEGORY")
        self.__add_product_category = QLineEdit()
        self.__add_product_category.setFont(QFont("consolas", 14))
        self.__add_product_layout.addWidget(self.__add_product_category_label, 4, 1)
        self.__add_product_layout.addWidget(self.__add_product_category, 5, 1)
        
        # Product Price (INV_ADD)
        self.__add_product_price_label = QLabel("PRODUCT PRICE")
        self.__add_product_price = QDoubleSpinBox()
        self.__add_product_price.setFont(QFont("consolas", 14))
        self.__add_product_layout.addWidget(self.__add_product_price_label, 6, 1)
        self.__add_product_layout.addWidget(self.__add_product_price, 7, 1)
        
        # Product Quantity (INV_ADD)
        self.__add_product_quantity_label = QLabel("PRODUCT QUANTITY")
        self.__add_product_quantity = QSpinBox()
        self.__add_product_quantity.setFont(QFont("consolas", 14))
        self.__add_product_layout.addWidget(self.__add_product_quantity_label, 8, 1)
        self.__add_product_layout.addWidget(self.__add_product_quantity, 9, 1)
        
        # Product Experation (INV_ADD)
        self.__add_product_exp_date_label = QLabel("PRODUCT EXPERATION DATE")
        self.__add_product_exp_date = QDateEdit()
        self.__add_product_exp_date.setDate(QDate.currentDate())
        self.__add_product_exp_date.setFont(QFont("consolas", 14))
        self.__add_product_layout.addWidget(self.__add_product_exp_date_label, 10, 1)
        self.__add_product_layout.addWidget(self.__add_product_exp_date, 11, 1)
        
        # Save Button (INV_ADD)
        def saveAddedProduct():
            """ Save Product """
            self.__add_product_div.hide()
        self.__add_product_save_btn = QPushButton("Save")
        self.__add_product_save_btn.clicked.connect(lambda: saveAddedProduct())
        self.__add_product_layout.addWidget(self.__add_product_save_btn, 12, 1)
        
######################################################################################################################
########################################### Statistics Page ##########################################################
        
        self.__statistics_div = QFrame()
        self.__statistics_layout = QGridLayout(self.__statistics_div)

######################################################################################################################
########################################### Suppliers Page ###########################################################
        
        self.__suppliers_div = QFrame()
        self.__suppliers_layout = QGridLayout(self.__suppliers_div)
######################################################################################################################
########################################### Customers Page ###########################################################
        
        self.__customers_div = QFrame()
        self.__customers_layout = QGridLayout(self.__customers_div)
######################################################################################################################
########################################### Settings Page ############################################################
        
        self.__settings_div = QFrame()
        self.__settings_layout = QGridLayout(self.__settings_div)
         
        
        # Updating the widgets
        def updateView(page):
            pages = {
                "CRT": self.__cash_register_div,
                "INV": self.__inventory_div,
                "STC": self.__statistics_div,
                "SUP": self.__suppliers_div,
                "CUS": self.__customers_div,
                "SET": self.__settings_div,
            }
            for key in pages.keys():
                if key == page:
                    pages[key].show()
                else:
                    pages[key].hide()

        # Cash Register Button (CRT)
        self.__cash_register_btn = QPushButton("Cash Register", self)
        self.__cash_register_btn.setIcon(QIcon("assets\\img\\cash-register.png"))
        self.__cash_register_btn.setStyleSheet("font-size: 14px;")
        self.__cash_register_btn.setIconSize(QSize(30, 40))
        self.__cash_register_btn.clicked.connect(lambda : updateView('CRT'))

        # Inventory Button (INV)
        self.__inventory_btn = QPushButton("Inventory", self)
        self.__inventory_btn.setIcon(QIcon("assets\\img\\products.png"))
        self.__inventory_btn.setStyleSheet("font-size: 14px;")
        self.__inventory_btn.setIconSize(QSize(30, 40))
        self.__inventory_btn.clicked.connect(lambda : updateView('INV'))

        # Statistics Button (STC)
        self.__statistics_btn = QPushButton("Statistics", self)
        self.__statistics_btn.setIcon(QIcon("assets\\img\\sales.png"))
        self.__statistics_btn.setStyleSheet("font-size: 14px;")
        self.__statistics_btn.setIconSize(QSize(30, 40))
        self.__statistics_btn.clicked.connect(lambda : updateView('STC'))

        # Suppliers Button (SUP)
        self.__suppliers_btn = QPushButton("Suppliers", self)
        self.__suppliers_btn.setIcon(QIcon("assets\\img\\supplier.png"))
        self.__suppliers_btn.setStyleSheet("font-size: 14px;")
        self.__suppliers_btn.setIconSize(QSize(30, 40))
        self.__suppliers_btn.clicked.connect(lambda : updateView('SUP'))

        # Customers Button (CUS)
        self.__customers_btn = QPushButton("Customers", self)
        self.__customers_btn.setIcon(QIcon("assets\\img\\customer.png"))
        self.__customers_btn.setStyleSheet("font-size: 14px;")
        self.__customers_btn.setIconSize(QSize(30, 40))
        self.__customers_btn.clicked.connect(lambda : updateView('CUS'))

        # Settings Button (SET)
        self.__settings_btn = QPushButton("Settings", self)
        self.__settings_btn.setIcon(QIcon("assets\\img\\cogwheel.png"))
        self.__settings_btn.setStyleSheet("font-size: 14px;")
        self.__settings_btn.setIconSize(QSize(30, 40))
        self.__settings_btn.clicked.connect(lambda : updateView('SET'))
        
        # Add Product Button (INV_ADD)
        self.__add_product_button.clicked.connect(lambda: self.__add_product_div.show())

        self.body.addWidget(self.__cash_register_btn, 0, 0)
        self.body.addWidget(self.__inventory_btn, 0, 1)
        self.body.addWidget(self.__statistics_btn, 0, 2)
        self.body.addWidget(self.__suppliers_btn, 0, 3)
        self.body.addWidget(self.__customers_btn, 0, 4)
        self.body.addWidget(self.__settings_btn, 0, 5)
        self.body.addWidget(self.__cash_register_div, 1, 0, 7, 6)
        self.body.addWidget(self.__inventory_div, 1, 0, 7, 6)
        self.body.addWidget(self.__statistics_div, 1, 0, 7, 6)
        self.body.addWidget(self.__suppliers_div, 1, 0, 7, 6)
        self.body.addWidget(self.__customers_div, 1, 0, 7, 6)
        self.body.addWidget(self.__settings_div, 1, 0, 7, 6)
        updateView("CRT")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("assets\\themes\\modern.qss", "r") as f:
        app.setStyleSheet(f.read())
    cashbox = App()
    cashbox.show()
    app.exec()
