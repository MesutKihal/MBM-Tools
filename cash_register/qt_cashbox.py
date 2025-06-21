from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import pandas as pd
import random

plt.style.use('bmh')

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)

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
        self.__search_bar.setPlaceholderText("Type the title of the product or scan barcode")
        self.__cash_register_layout.addWidget(self.__search_bar, 1, 0, 1, 2)

        # Search or Scan button (CRT)
        self.__search_btn = QPushButton("Search")
        self.__search_btn.setIcon(QIcon("assets\\img\\search.png"))
        self.__search_btn.setIconSize(QSize(30, 30))
        self.__cash_register_layout.addWidget(self.__search_btn, 1, 2, 1, 1)
        
        # Products Table (CRT)
        self.__products_table = QTableWidget()
        self.__products_table.setColumnCount(6)
        self.__products_table.setRowCount(20)
        self.__products_table.setAlternatingRowColors(True)
        self.__products_table.setHorizontalHeaderLabels(["ID", "Title", "Category", "Price", "In Stock", "Expiration"])
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
        self.__inv_search_btn.setIconSize(QSize(30, 30))
        self.__inventory_layout.addWidget(self.__inv_search_btn, 1, 6)
        
        # Products Table (INV)
        self.__inventory_table = QTableWidget()
        self.__inventory_table.setColumnCount(6)
        self.__inventory_table.setRowCount(20)
        self.__inventory_table.setHorizontalHeaderLabels(["ID", "Title", "Category", "Price", "In Stock", "Expiration"])
        self.__inventory_table.setAlternatingRowColors(True)
        self.__inventory_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.__inventory_layout.addWidget(self.__inventory_table, 2, 0, 3, 7)

        # Add Product (INV)
        self.__add_product_button = QPushButton("Add new product")
        self.__add_product_button.setIcon(QIcon("assets\\img\\add.png"))
        self.__add_product_button.setIconSize(QSize(30, 40))
        self.__inventory_layout.addWidget(self.__add_product_button, 5, 3)
 
        # Product Card (INV)
        self.__product_card = QFrame()
        self.__card_layout = QVBoxLayout(self.__product_card)
        self.__inventory_layout.addWidget(self.__product_card, 1, 8, 5, 1)
        
        
        # Product Image (INV)
        self.__product_image = QPixmap("assets\\img\\noimage.png")
        self.__product_image = self.__product_image.scaled(300, 300, Qt.KeepAspectRatio)
        self.__img_container = QLabel()
        self.__img_container.setPixmap(self.__product_image)
        self.__card_layout.addWidget(self.__img_container)
        
        # Product ID (INV)
        self.__product_id = QLabel("Product ID (Barcode, QRCode, REF)")
        self.__product_id.setFont(QFont("Helvetica", 14))
        self.__product_id.setStyleSheet("background: #fff;border-radius: none;")
        self.__card_layout.addWidget(self.__product_id)
        
        # Product Title (INV)
        self.__product_title = QLabel("Product Title")
        self.__product_title.setFont(QFont("Helvetica", 14))
        self.__product_title.setStyleSheet("background: #ddd;border-radius: none;")
        self.__card_layout.addWidget(self.__product_title)
        
        # Product Category (INV)
        self.__product_category = QLabel("Product Category")
        self.__product_category.setFont(QFont("Helvetica", 14))
        self.__product_category.setStyleSheet("background: #fff;border-radius: none;")
        self.__card_layout.addWidget(self.__product_category)
        
        # Product Price (INV)
        self.__product_price = QLabel("Product Price")
        self.__product_price.setFont(QFont("Helvetica", 14))
        self.__product_price.setStyleSheet("background: #ddd;border-radius: none;")
        self.__card_layout.addWidget(self.__product_price)
        
        # Product Quantity (INV)
        self.__product_quantity = QLabel("Product Quantity")
        self.__product_quantity.setFont(QFont("Helvetica", 14))
        self.__product_quantity.setStyleSheet("background: #fff;border-radius: none;")
        self.__card_layout.addWidget(self.__product_quantity)
        
        # Product Experation (INV)
        self.__product_exp_date = QLabel("Product Experation Date")
        self.__product_exp_date.setFont(QFont("Helvetica", 14))
        self.__product_exp_date.setStyleSheet("background: #ddd;border-radius: none;")
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
        self.__add_product_image = QPixmap("assets\\img\\noimage.png")
        self.__add_product_image = self.__product_image.scaled(400, 400, Qt.KeepAspectRatio)
        self.__add_product_img_container = QLabel()
        self.__add_product_img_container.setPixmap(self.__add_product_image)
        self.__add_product_img_btn = QPushButton("Insert Image")
        self.__add_product_layout.addWidget(self.__add_product_img_container, 0, 0, 11, 1)
        self.__add_product_layout.addWidget(self.__add_product_img_btn, 12, 0)
        
        
        # Product ID (INV_ADD)
        self.__add_product_id_label = QLabel("PRODUCT ID, BARCODE or QRCODE")
        self.__add_product_id = QLineEdit()
        self.__add_product_id.setFont(QFont("Helvetica", 14))
        self.__add_product_layout.addWidget(self.__add_product_id_label, 0, 1)
        self.__add_product_layout.addWidget(self.__add_product_id, 1, 1)
        
        # Product Title (INV_ADD)
        self.__add_product_title_label = QLabel("PRODUCT TITLE")
        self.__add_product_title = QLineEdit()
        self.__add_product_title.setFont(QFont("Helvetica", 14))
        self.__add_product_layout.addWidget(self.__add_product_title_label, 2, 1)
        self.__add_product_layout.addWidget(self.__add_product_title, 3, 1)
        
        # Product Category (INV_ADD)
        self.__add_product_category_label = QLabel("PRODUCT CATEGORY")
        self.__add_product_category = QLineEdit()
        self.__add_product_category.setFont(QFont("Helvetica", 14))
        self.__add_product_layout.addWidget(self.__add_product_category_label, 4, 1)
        self.__add_product_layout.addWidget(self.__add_product_category, 5, 1)
        
        # Product Price (INV_ADD)
        self.__add_product_price_label = QLabel("PRODUCT PRICE")
        self.__add_product_price = QDoubleSpinBox()
        self.__add_product_price.setFont(QFont("Helvetica", 14))
        self.__add_product_layout.addWidget(self.__add_product_price_label, 6, 1)
        self.__add_product_layout.addWidget(self.__add_product_price, 7, 1)
        
        # Product Quantity (INV_ADD)
        self.__add_product_quantity_label = QLabel("PRODUCT QUANTITY")
        self.__add_product_quantity = QSpinBox()
        self.__add_product_quantity.setFont(QFont("Helvetica", 14))
        self.__add_product_layout.addWidget(self.__add_product_quantity_label, 8, 1)
        self.__add_product_layout.addWidget(self.__add_product_quantity, 9, 1)
        
        # Product Experation (INV_ADD)
        self.__add_product_exp_date_label = QLabel("PRODUCT EXPERATION DATE")
        self.__add_product_exp_date = QDateEdit()
        self.__add_product_exp_date.setDate(QDate.currentDate())
        self.__add_product_exp_date.setFont(QFont("Helvetica", 14))
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
########################################### Edit Product Page #########################################################
  
        self.__edit_product_div = QFrame()
        self.__edit_product_div.setFixedSize(1100, 550)
        self.__edit_product_layout = QGridLayout(self.__edit_product_div)
        
        # Product Image (INV_EDIT)
        self.__edit_product_image = QPixmap("assets\\img\\noimage.png")
        self.__edit_product_image = self.__product_image.scaled(400, 400, Qt.KeepAspectRatio)
        self.__edit_product_img_container = QLabel()
        self.__edit_product_img_container.setPixmap(self.__edit_product_image)
        self.__edit_product_img_btn = QPushButton("Insert Image")
        self.__edit_product_layout.addWidget(self.__edit_product_img_container, 0, 0, 11, 1)
        self.__edit_product_layout.addWidget(self.__edit_product_img_btn, 12, 0)
        
        
        # Product ID (INV_EDIT)
        self.__edit_product_id_label = QLabel("PRODUCT ID, BARCODE or QRCODE")
        self.__edit_product_id = QLineEdit()
        self.__edit_product_id.setFont(QFont("Helvetica", 14))
        self.__edit_product_layout.addWidget(self.__edit_product_id_label, 0, 1)
        self.__edit_product_layout.addWidget(self.__edit_product_id, 1, 1)
        
        # Product Title (INV_EDIT)
        self.__edit_product_title_label = QLabel("PRODUCT TITLE")
        self.__edit_product_title = QLineEdit()
        self.__edit_product_title.setFont(QFont("Helvetica", 14))
        self.__edit_product_layout.addWidget(self.__edit_product_title_label, 2, 1)
        self.__edit_product_layout.addWidget(self.__edit_product_title, 3, 1)
        
        # Product Category (INV_EDIT)
        self.__edit_product_category_label = QLabel("PRODUCT CATEGORY")
        self.__edit_product_category = QLineEdit()
        self.__edit_product_category.setFont(QFont("Helvetica", 14))
        self.__edit_product_layout.addWidget(self.__edit_product_category_label, 4, 1)
        self.__edit_product_layout.addWidget(self.__edit_product_category, 5, 1)
        
        # Product Price (INV_EDIT)
        self.__edit_product_price_label = QLabel("PRODUCT PRICE")
        self.__edit_product_price = QDoubleSpinBox()
        self.__edit_product_price.setFont(QFont("Helvetica", 14))
        self.__edit_product_layout.addWidget(self.__edit_product_price_label, 6, 1)
        self.__edit_product_layout.addWidget(self.__edit_product_price, 7, 1)
        
        # Product Quantity (INV_EDIT)
        self.__edit_product_quantity_label = QLabel("PRODUCT QUANTITY")
        self.__edit_product_quantity = QSpinBox()
        self.__edit_product_quantity.setFont(QFont("Helvetica", 14))
        self.__edit_product_layout.addWidget(self.__edit_product_quantity_label, 8, 1)
        self.__edit_product_layout.addWidget(self.__edit_product_quantity, 9, 1)
        
        # Product Experation (INV_EDIT)
        self.__edit_product_exp_date_label = QLabel("PRODUCT EXPERATION DATE")
        self.__edit_product_exp_date = QDateEdit()
        self.__edit_product_exp_date.setDate(QDate.currentDate())
        self.__edit_product_exp_date.setFont(QFont("Helvetica", 14))
        self.__edit_product_layout.addWidget(self.__edit_product_exp_date_label, 10, 1)
        self.__edit_product_layout.addWidget(self.__edit_product_exp_date, 11, 1)
        
        # Save Button (INV_EDIT)
        def saveAddedProduct():
            """ Save Product """
            self.__edit_product_div.hide()
        self.__edit_product_save_btn = QPushButton("Save")
        self.__edit_product_save_btn.clicked.connect(lambda: saveAddedProduct())
        self.__edit_product_layout.addWidget(self.__edit_product_save_btn, 12, 1)

######################################################################################################################
########################################### Statistics Page ##########################################################
        
        self.__statistics_div = QFrame()
        self.__statistics_layout = QGridLayout(self.__statistics_div)
        
        # Product Count
        self.__product_count_label = QLabel("Products Count")
        self.__product_count = QLabel("48")
        self.__product_count.setStyleSheet("font-size: 28px;color: red;")
        self.__statistics_layout.addWidget(self.__product_count_label, 0, 0)
        self.__statistics_layout.addWidget(self.__product_count, 1, 0)
        
        # Product in Stock
        self.__product_in_stock_label = QLabel("Products In Stock")
        self.__product_in_stock = QLabel("357")
        self.__product_in_stock.setStyleSheet("font-size: 28px;color: red;")
        self.__statistics_layout.addWidget(self.__product_in_stock_label, 0, 1)
        self.__statistics_layout.addWidget(self.__product_in_stock, 1, 1)
        
        # Category Count
        self.__category_count_label = QLabel("Category Count")
        self.__category_count = QLabel("12")
        self.__category_count.setStyleSheet("font-size: 28px;color: red;")
        self.__statistics_layout.addWidget(self.__category_count_label, 0, 2)
        self.__statistics_layout.addWidget(self.__category_count, 1, 2)
        
        # Loyal Customers Count
        self.__customers_count_label = QLabel("Loyal Customers Count")
        self.__customers_count = QLabel("57")
        self.__customers_count.setStyleSheet("font-size: 28px;color: red;")
        self.__statistics_layout.addWidget(self.__customers_count_label, 0, 3)
        self.__statistics_layout.addWidget(self.__customers_count, 1, 3)
        
        # Monthly Revenue
        self.__customers_count_label = QLabel("Monthly Revenue")
        self.__customers_count = QLabel("52039.18")
        self.__customers_count.setStyleSheet("font-size: 28px;color: green;")
        self.__statistics_layout.addWidget(self.__customers_count_label, 0, 4)
        self.__statistics_layout.addWidget(self.__customers_count, 1, 4)
        
        # Annual Revenue
        self.__customers_count_label = QLabel("Annual Revenue")
        self.__customers_count = QLabel("654821.23")
        self.__customers_count.setStyleSheet("font-size: 28px;color: green;")
        self.__statistics_layout.addWidget(self.__customers_count_label, 0, 5)
        self.__statistics_layout.addWidget(self.__customers_count, 1, 5)
        
        # Sales Plot
        self.__plot_canvas = MplCanvas(self)
        self.__plot_toolbar = NavigationToolbar(self.__plot_canvas, self)
        x = ["SAT", "SUN", "MON", "TUE", "WED", "THU", "FRI"]
        y = [random.randint(15, 37) for _ in range(7)]
        df = pd.DataFrame({'DAYS': x, 'NUMBER OF SALES': y})
        self.__plot_canvas.ax.clear()
        sns.barplot(data=df, x='DAYS', y='NUMBER OF SALES', ax=self.__plot_canvas.ax)
        self.__plot_canvas.draw()
        self.__statistics_layout.addWidget(self.__plot_canvas, 3, 0, 3, 3)
        self.__statistics_layout.addWidget(self.__plot_toolbar, 2, 0, 1, 3)
        
        # Daily Plot Button
        self.__plot_day_btn = QPushButton("Per Day")
        self.__statistics_layout.addWidget(self.__plot_day_btn, 6, 0)
        
        # Weekly Plot Button
        self.__plot_week_btn = QPushButton("Per Week")
        self.__statistics_layout.addWidget(self.__plot_week_btn, 6, 1)
        
        # Monthly Plot Button
        self.__plot_month_btn = QPushButton("Per Month")
        self.__statistics_layout.addWidget(self.__plot_month_btn, 6, 2)
        
        
        # Low Stock Items
        self.__low_stock_label = QLabel("Low Stock Items")
        self.__low_stock_table = QTableWidget()
        self.__low_stock_table.setColumnCount(3)
        self.__low_stock_table.setRowCount(5)
        self.__low_stock_table.setHorizontalHeaderLabels(["ID", "Title", "Quantity"])
        self.__low_stock_table.setAlternatingRowColors(True)
        self.__low_stock_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.__statistics_layout.addWidget(self.__low_stock_label, 2, 3, 1, 3)
        self.__statistics_layout.addWidget(self.__low_stock_table, 3, 3, 1, 3)
        
        # Impending Exparation
        self.__close_exp_label = QLabel("Impending Expiration")
        self.__close_exp_table = QTableWidget()
        self.__close_exp_table.setColumnCount(3)
        self.__close_exp_table.setRowCount(5)
        self.__close_exp_table.setHorizontalHeaderLabels(["ID", "Title", "Expiration Date"])
        self.__close_exp_table.setAlternatingRowColors(True)
        self.__close_exp_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.__statistics_layout.addWidget(self.__close_exp_label, 4, 3, 1, 3)
        self.__statistics_layout.addWidget(self.__close_exp_table, 5, 3, 1, 3)
        
        # Most Profitable
        self.__most_profit_label = QLabel("Most Profitable")
        self.__most_profit_arr = []
        for i in range(3):
            frame = QFrame()
            layout = QVBoxLayout(frame)
            img = QPixmap("assets\\img\\noimage.png")
            img = img.scaled(100, 100, Qt.KeepAspectRatio)
            container = QLabel()
            container.setPixmap(img)
            layout.addWidget(container)
            
            id = QLabel(f"Title: Product {i+1}")
            id.setFont(QFont("Helvetica", 12))
            id.setStyleSheet("background: #fff;border-radius: none;font-size: 14px;")
            layout.addWidget(id)
            
            rev = QLabel(f"Avg Revenue:  {random.randint(6752, 9823)}")
            rev.setFont(QFont("Helvetica", 12))
            rev.setStyleSheet("background: #fff;border-radius: none;font-size: 14px;")
            layout.addWidget(rev)
            self.__most_profit_arr.append(frame)
            self.__statistics_layout.addWidget(frame, 3, 3+i)
            frame.hide()
            
        self.__statistics_layout.addWidget(self.__most_profit_label, 2, 3, 1, 3)

        
        # Least Popular
        self.__less_popular_label = QLabel("Least Popular")
        self.__less_popular_arr = []
        for i in range(3):
            frame = QFrame()
            layout = QVBoxLayout(frame)
            img = QPixmap("assets\\img\\noimage.png")
            img = img.scaled(100, 100, Qt.KeepAspectRatio)
            container = QLabel()
            container.setPixmap(img)
            layout.addWidget(container)
            
            id = QLabel(f"Title: Product {i+1}")
            id.setStyleSheet("background: #fff;border-radius: none;font-size: 14px;")
            layout.addWidget(id)
            
            rev = QLabel(f"Sold(U):  {random.randint(0, 20)}")
            rev.setStyleSheet("background: #fff;border-radius: none;font-size: 14px;")
            layout.addWidget(rev)
            self.__less_popular_arr.append(frame)
            self.__statistics_layout.addWidget(frame, 5, 3+i)
            frame.hide()
            
            
        self.__statistics_layout.addWidget(self.__less_popular_label, 4, 3, 1, 3)
        
        # Category Chart
        self.__pie_canvas = MplCanvas(self)
        self.__pie_label = QLabel("Category Distribution")
        labels = ["CAT 01", "CAT 02", "CAT 03"]
        perc = [25, 36, 39]
        self.__pie_canvas.ax.pie(perc, labels=labels, autopct='%1.1f%%')
        self.__pie_canvas.ax.set_aspect("equal")
        self.__pie_canvas.ax.legend(title = "Categories:")
        self.__pie_canvas.fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        self.__statistics_layout.addWidget(self.__pie_canvas, 3, 3, 2, 3)
        self.__statistics_layout.addWidget(self.__pie_label, 2, 3, 1, 3)
        switchDict = {
            "tables": [
                self.__low_stock_label,
                self.__low_stock_table,
                self.__close_exp_label,
                self.__close_exp_table
            ],
            "products": [
                self.__most_profit_arr,
                self.__most_profit_label,
                self.__less_popular_label,
                self.__less_popular_arr
            ],
            "chart": [
                self.__pie_canvas,
                self.__pie_label
            ]
        }
        def switchStat(stat):
            # Show
            for value in switchDict[stat]:
                if type(value) is list:
                    for widget in value:
                        widget.show()
                else:
                    value.show()
                    
            # Hide
            for key in switchDict.keys():
                if key != stat:
                    for value in switchDict[key]:
                        if type(value) is list:
                            for widget in value:
                                widget.hide()
                        else:
                            value.hide()
            
        
        # Tables Button
        self.__tables_btn = QPushButton("Tables")
        self.__tables_btn.clicked.connect(lambda: switchStat("tables"))
        self.__statistics_layout.addWidget(self.__tables_btn, 6, 3)
        
        # Products Button
        self.__products_btn = QPushButton("Products")
        self.__products_btn.clicked.connect(lambda: switchStat("products"))
        self.__statistics_layout.addWidget(self.__products_btn, 6, 4)
        
        # Categories Button
        self.__categories_btn = QPushButton("Categories")
        self.__categories_btn.clicked.connect(lambda: switchStat("chart"))
        self.__statistics_layout.addWidget(self.__categories_btn, 6, 5)
        switchStat('tables')
        
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
        
        # Edit Product Button (INV_EDIT)
        self.__edit_product_button.clicked.connect(lambda: self.__edit_product_div.show())

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
