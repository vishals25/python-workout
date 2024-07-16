from ast import arg
import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit,QLineEdit,QPushButton,QApplication
from backend import Chatbot 
import threading

class ChatBoxWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot=Chatbot()

        self.setMinimumSize(700,500)

        self.chat_area=QTextEdit(self)
        self.chat_area.setGeometry(10,10,500,320)
        self.chat_area.setReadOnly(True)


        self.input_field=QLineEdit(self)
        self.input_field.setGeometry(10,340,500,40)
        self.input_field.returnPressed.connect(self.send_message)

        self.button=QPushButton("Send",self)
        self.button.setGeometry(520,340,100,40)

        self.button.clicked.connect(self.send_message)
        

        self.show()

    def send_message(self):
        message=self.input_field.text().strip()
        self.chat_area.append(f"ME :{message}")
        self.input_field.clear()

        thread=threading.Thread(target=self.get_bot_response,args=(message,))
        thread.start()

        response=self.chatbot.get_response(message)
        self.chat_area.append(f"BOT :{response}")


    def get_bot_response(self,message):
        response=self.chatbot.get_response(message)
        self.chat_area.append(f"BOT :{response}")


app=QApplication(sys.argv)
main_window=ChatBoxWindow()
sys.exit(app.exec())