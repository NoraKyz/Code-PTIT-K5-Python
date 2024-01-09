import typing
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from employee import Employee
from manager import Manager


class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Register")

        self.setWindowTitle("Add NV")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.setWindowTitle("Insert NV Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.QBtn.clicked.connect(self.add_NV)

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Họ và Tên")
        layout.addWidget(self.name_input)

        self.salary_input = QLineEdit()
        self.salary_input.setPlaceholderText("Lương")
        layout.addWidget(self.salary_input)

        self.department_input = QLineEdit()
        self.department_input.setPlaceholderText("Phòng Ban")
        layout.addWidget(self.department_input)

        self.department_id_input = QLineEdit()
        self.department_id_input.setPlaceholderText("ID Phòng Ban")
        layout.addWidget(self.department_id_input)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

        self.manager = Manager()

    def add_NV(self):
        name = self.name_input.text()
        salary = self.salary_input.text()
        department = self.department_input.text()
        department_id = self.department_id_input.text()
        if name == "" or salary == "" or department == "" or department_id == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Please fill in all the fields.')
            return
        elif not self.salary_input.text().isnumeric():
            QMessageBox.warning(QMessageBox(), 'Error', 'Invalid Salary Input.')
            return
        else:
            employee = Employee(name, salary, department_id, department)
            self.manager.add_NV(employee)
            QMessageBox.information(QMessageBox(), 'Successful', 'NV is added successfully.')
            self.close()


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search NV")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.QBtn.clicked.connect(self.search_NV)

        layout = QVBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("ID NV")
        layout.addWidget(self.search_input)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

        self.manager = Manager()

    def search_NV(self):
        input_id = self.search_input.text()
        if input_id == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not search NV.')
        else:
            employee = self.manager.find_NV(input_id)
            if employee != None:
                QMessageBox.information(QMessageBox(), 'Successful', str(employee))
                self.close()
            else:
                QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find NV.')


class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete NV")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.QBtn.clicked.connect(self.delete_NV)

        layout = QVBoxLayout()

        self.delete_input = QLineEdit()
        self.delete_input.setPlaceholderText("ID NV")
        layout.addWidget(self.delete_input)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

        self.manager = Manager()

    def delete_NV(self):
        input_id = self.delete_input.text()
        if input_id == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Please fill in the ID NV.')
        elif self.manager.find_NV(input_id) == None:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find NV.')
        else:
            self.manager.delete_NV(input_id)

            QMessageBox.information(QMessageBox(), 'Successful', "NV is deleted successfully.")
            self.close()


class SalaryIncreaseDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SalaryIncreaseDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Increase")

        self.setWindowTitle("Increase Salary")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.QBtn.clicked.connect(self.increase_salary)

        layout = QVBoxLayout()

        self.id_nv_input = QLineEdit()
        self.id_nv_input.setPlaceholderText("ID NV")

        self.new_salary_input = QLineEdit()
        self.new_salary_input.setPlaceholderText("Increase Amount")

        layout.addWidget(self.id_nv_input)
        layout.addWidget(self.new_salary_input)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

        self.manager = Manager()


    def increase_salary(self):
        id_nv = self.id_nv_input.text()
        if id_nv == "" or self.new_salary_input.text() == "":
            QMessageBox.warning(QMessageBox(), 'Error', 'Please fill in the ID NV and increase amount.')
            return
        elif not self.new_salary_input.text().isnumeric():
            QMessageBox.warning(QMessageBox(), 'Error', 'Invalid Salary Input.')
            return
        elif self.manager.find_NV(id_nv) == None:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find NV.')
            return
        else:
            new_salary = self.new_salary_input.text()
            if not new_salary.isnumeric():
                QMessageBox.warning(QMessageBox(), 'Error', 'Invalid salary.')
                return
            else:
                self.manager.update_salary_NV(id_nv, new_salary)

                QMessageBox.information(QMessageBox(), 'Successful', "Salary is increased successfully.")
                self.close()


class Ui_MainWindow(object):
    def __init__(self):
        self.manager = Manager()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("QLNV")
        MainWindow.resize(1080, 640)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 41, 1071, 541))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 0, 1061, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reload_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reload_btn.setFont(font)
        self.reload_btn.setObjectName("reload_btn")
        self.horizontalLayout.addWidget(self.reload_btn)
        self.insert_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.insert_btn.setFont(font)
        self.insert_btn.setObjectName("insert_btn")
        self.horizontalLayout.addWidget(self.insert_btn)
        self.salary_increase_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.salary_increase_btn.setFont(font)
        self.salary_increase_btn.setObjectName("salary_increase_btn")
        self.horizontalLayout.addWidget(self.salary_increase_btn)
        self.search_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.delete_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReload = QtGui.QAction(parent=MainWindow)
        self.actionReload.setObjectName("actionReload")
        self.actionInsert = QtGui.QAction(parent=MainWindow)
        self.actionInsert.setObjectName("actionInsert")
        self.actionSearch = QtGui.QAction(parent=MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.actionDelete = QtGui.QAction(parent=MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSalary_Increase = QtGui.QAction(parent=MainWindow)
        self.actionSalary_Increase.setObjectName("actionSalary_Increase")
        self.actionUI_create_by_Toanr = QtGui.QAction(parent=MainWindow)
        self.actionUI_create_by_Toanr.setEnabled(False)
        self.actionUI_create_by_Toanr.setObjectName("actionUI_create_by_Toanr")
        self.menuFile.addAction(self.actionReload)
        self.menuFile.addAction(self.actionInsert)
        self.menuFile.addAction(self.actionSalary_Increase)
        self.menuFile.addAction(self.actionSearch)
        self.menuFile.addAction(self.actionDelete)
        self.menuAbout.addAction(self.actionUI_create_by_Toanr)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Salary"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Department"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DepartmentID"))

        
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Custom)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Custom)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Custom)

        self.reload_btn.setText(_translate("MainWindow", "Reload"))
        self.insert_btn.setText(_translate("MainWindow", "Insert"))
        self.salary_increase_btn.setText(_translate("MainWindow", "Salary Increase"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.delete_btn.setText(_translate("MainWindow", "Delete"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionReload.setText(_translate("MainWindow", "Reload"))
        self.actionInsert.setText(_translate("MainWindow", "Insert"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionSalary_Increase.setText(_translate("MainWindow", "Salary Increase"))
        self.actionUI_create_by_Toanr.setText(_translate("MainWindow", "UI created by Toanr"))

        self.reload_btn.clicked.connect(self.reload)
        self.insert_btn.clicked.connect(self.insert)
        self.salary_increase_btn.clicked.connect(self.salary_increase)
        self.search_btn.clicked.connect(self.search)
        self.delete_btn.clicked.connect(self.delete)

        self.actionReload.triggered.connect(self.reload)
        self.actionInsert.triggered.connect(self.insert)
        self.actionSalary_Increase.triggered.connect(self.salary_increase)
        self.actionSearch.triggered.connect(self.search)
        self.actionDelete.triggered.connect(self.delete)


    def reload(self):
        data = self.manager.load_NV()
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(data[i].id))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(data[i].name))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(data[i].salary)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(data[i].department_name))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(data[i].department_id))


    def insert(self):
        dlg = InsertDialog()
        dlg.exec()
        self.reload()

    def salary_increase(self):
        dlg = SalaryIncreaseDialog()
        dlg.exec()
        self.reload()

    def search(self):
        dlg = SearchDialog()
        dlg.exec()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec()
        self.reload()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.reload()
    MainWindow.show()
    sys.exit(app.exec())
