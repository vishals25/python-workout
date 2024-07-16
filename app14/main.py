from re import S
from tkinter import dialog
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QLabel,QGridLayout,QMainWindow,QDialog,QTableWidget,QTableWidgetItem,QMessageBox
from PyQt6.QtGui import QAction,QIcon
from PyQt6.QtWidgets import QWidget,QPushButton,QLabel,QLineEdit,QDialog,QVBoxLayout,QComboBox,QToolBar,QStatusBar
import sys
import mysql.connector as sql



class DataBaseConnection:
    def __init__(self,host="localhost",user="root",password="vishal",database="school"):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
    def connect(self):
        connection=sql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
        return connection

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student ManagementSystem")
        self.setMinimumSize(600,500)

        file_menu_item=self.menuBar().addMenu("&File") # type: ignore
        help_menu_item=self.menuBar().addMenu("&Help") # type: ignore
        edit_menu_item=self.menuBar().addMenu("&Edit") # type: ignore
        
        add_student_action=QAction(QIcon("icons/add.png"),"Add Student",self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action) # type: ignore

        about_action=QAction(QIcon("icons/about.png"),"About",self)
        help_menu_item.addAction(about_action) # type: ignore
        about_action.triggered.connect(self.about)

        help_action=QAction(QIcon("icons/help.png"),"Help",self)
        help_menu_item.addAction(help_action) # type: ignore
        help_action.triggered.connect(self.help)

        search_action=QAction(QIcon("icons/search.png"),"Search",self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action) # type: ignore

        self.table=QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID","NAME","COURSE","MOBILE"))
        self.table.verticalHeader().setVisible(False) # type: ignore
        self.setCentralWidget(self.table)

        toolbar=QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        self.statusbar=QStatusBar()
        self.setStatusBar(self.statusbar)

        self.table.cellClicked.connect(self.cell_clicked)

    def load_data(self):
        connection=DataBaseConnection().connect()
        cursor=connection.cursor()
        cursor.execute("select * from students")
        result=cursor.fetchall() # type: ignore
        result=list(result) # type: ignore
        self.table.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.table.insertRow(row_number)
            print(row_data)
            for col_number,data in enumerate(row_data): # type: ignore
                self.table.setItem(row_number,col_number,QTableWidgetItem(str(data)))
        
        connection.close()
        
    def insert(self):
        dialog=InsertDialog()
        dialog.exec()

    def search(self):
        dialog=SearchDialog()
        dialog.exec()

    def cell_clicked(self):
        edit_button=QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)
        delete_button=QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        childern=self.findChildren(QPushButton)
        if childern:
            for child in childern:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def edit(self):
        dialog=EditDialog()
        dialog.exec()

    def delete(self):
        dialog=DeleteDialog()
        dialog.exec()

    def about(self):
        dialog=AboutDialog()
        dialog.exec()

    def help(self):
        dialog=HelpDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout=QVBoxLayout()

        self.student_name=QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name=QComboBox()
        courses=["biology","Math","Astronomy","Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.mobile=QLineEdit()
        self.mobile.setPlaceholderText("Mobile number")
        layout.addWidget(self.mobile)

        button=QPushButton("Add Student")
        layout.addWidget(button)
        button.clicked.connect(self.addstudent)

        self.setLayout(layout)

    def addstudent(self):
        name=self.student_name.text()
        course=self.course_name.itemText(self.course_name.currentIndex())
        mobile=self.mobile.text()
        connection=DataBaseConnection().connect()
        cursor=connection.cursor()
        cursor.execute("insert into students (name,course,mobile) values (%s,%s,%s)",(name,course,mobile))
        connection.commit()
        cursor.close()
        connection.close()

        main_window.load_data()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout=QVBoxLayout()

        self.student_name=QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        button=QPushButton("Search")
        layout.addWidget(button)
        button.clicked.connect(self.searchstudent)

        self.setLayout(layout)

    def searchstudent(self):
        name=self.student_name.text()
        print(name)
        connection=DataBaseConnection().connect()
        cursor=connection.cursor()
        cursor.execute("select * from students where name=%s",(name,)) #tuple
        result=cursor.fetchall() # type: ignore
        rows=list(result)
        print(rows)
        items=main_window.table.findItems(name,Qt.MatchFlag.MatchFixedString)
        for item in items:
            main_window.table.item(item.row(),1).setSelected(True) # type: ignore
        cursor.close()
        connection.close()


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student REcord")
        self.setFixedSize(300,300)

        layout=QVBoxLayout()

        index=main_window.table.currentRow()
        student_name=main_window.table.item(index,1).text() # type: ignore
        course=main_window.table.item(index,2).text() # type: ignore
        mobile=main_window.table.item(index,3).text() # type: ignore
        self.id=main_window.table.item(index,0).text() # type: ignore

        self.student_name=QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name=QComboBox()
        courses=["biology","Math","Astronomy","Physics"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course)
        layout.addWidget(self.course_name)

        self.mobile=QLineEdit(mobile)
        self.mobile.setPlaceholderText("Mobile number")
        layout.addWidget(self.mobile)

        button=QPushButton("Update Student Record")
        layout.addWidget(button)
        button.clicked.connect(self.editstudent)

        self.setLayout(layout)

    def editstudent(self):
        name=self.student_name.text()
        course=self.course_name.itemText(self.course_name.currentIndex())
        mobile=self.mobile.text()
        connection=DataBaseConnection().connect()
        cursor=connection.cursor()
        cursor.execute("UPDATE students SET name=%s, course=%s, mobile=%s WHERE id=%s", (name, course, mobile, self.id))
        connection.commit()
        cursor.close()
        connection.close()

        main_window.load_data()


class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student")
        self.index=main_window.table.currentRow()
        student_name=main_window.table.item(self.index,1).text() # type: ignore
        layout=QGridLayout()
        confirmation=QLabel(f"Are you sure to delete the student record\n\n'{student_name}'\n")
        yes=QPushButton("Delete")
        no=QPushButton("Retain")

        layout.addWidget(confirmation,0,0,1,2)
        layout.addWidget(yes,1,0)
        layout.addWidget(no,1,1)
        
        yes.clicked.connect(self.delete)
        no.clicked.connect(self.retain)

        self.setLayout(layout)

    def retain(self):
        self.close()

    def delete(self):
        id=main_window.table.item(self.index,0).text() # type: ignore
        connection=DataBaseConnection().connect()
        cursor=connection.cursor()
        cursor.execute("delete from students where  id=%s",(id,))
        connection.commit()
        cursor.close()
        connection.close()

        main_window.load_data()

        self.close()

        confirmation_widget=QMessageBox()
        confirmation_widget.setWindowTitle("Success")
        confirmation_widget.setText("Student record deleted successfully")
        confirmation_widget.exec()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About")

        content="""
        This Student Record Management System is a software application designed to efficiently handle the data and records related to students in an educational institution. 
        This system streamlines the process of maintaining and retrieving student information, including personal details, academic performance, attendance, and other relevant data. 
        By digitizing student records, the system ensures data accuracy, reduces administrative workload, and enhances the accessibility of information.
        """
        self.setText(content)

class HelpDialog(QMessageBox):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help")

        content="""
        For Contacting Supports:
            Mail:12345@example.com
            """
        self.setText(content)


app=QApplication(sys.argv)
main_window=MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())