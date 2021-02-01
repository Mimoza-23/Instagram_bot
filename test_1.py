from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time 
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import os
import re
import sys
from PyQt5 import QtCore,QtGui,QtWidgets 
from des import * 

class InstagramBot():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        options = Options()
        # options.add_argument("--headless")
        self.browser = webdriver.Firefox(options=options)

    def close_browser(self):

        self.browser.close()
        self.browser.quit()
    
    def login(self):
        browser = self.browser
        browser.get('https://www.instagram.com/')
        time.sleep(random.randrange(4 ,6))

        username_input = browser.find_element_by_name("username") 
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(5)
        password_input = browser.find_element_by_name("password") 
        password_input.clear()
        password_input.send_keys(password)

        password_input = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
        time.sleep(10)

class GUI(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QTabWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = self.ui.lineEdit.text()
        self.password = self.ui.lineEdit_2.text()
        self.ui.pushButton.clicked.connect(self.go_to)

    def go_to(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        # try:
        username = self.username
        password = self.password
        self.inst = InstagramBot(username,password)
        self.inst.login()
        # except:
        #     print("Слушай что-то пошло нет так(")
            
        
        

# class InstagramBot(GUI,QtCore.QThread):
#     about_auth = QtCore.pyqtSignal()
#     def __init__(self):
#         QtCore.QThread.__init__(self,username,password)
#         self.username = username
#         self.password = password
#         options = Options()
#         # options.add_argument("--headless")
#         self.browser = webdriver.Firefox(options=options)

    

    # def run(self):
    #     while True:
    #         try:
    #             browser = self.browser
    #             browser.get('https://www.instagram.com/')
    #             time.sleep(random.randrange(4 ,6))

    #             username_input = browser.find_element_by_name("username") 
    #             username_input.clear()
    #             username_input.send_keys(username)

    #             time.sleep(5)
    #             password_input = browser.find_element_by_name("password") 
    #             password_input.clear()
    #             password_input.send_keys(password)

    #             password_input = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
    #             time.sleep(10)
    #         except:
    #             print("Слушай что-то пошло нет так(")
    #             self.browser.close()
    #             self.browser.quit()
    #             mywin.close()

    # def close_browser(self):

    #     self.browser.close()
    #     self.browser.quit()

    # def login(self):
    #     browser = self.browser
    #     browser.get('https://www.instagram.com/')
    #     time.sleep(random.randrange(4 ,6))

    #     username_input = browser.find_element_by_name("username") 
    #     username_input.clear()
    #     username_input.send_keys(username)

    #     time.sleep(5)
    #     password_input = browser.find_element_by_name("password") 
    #     password_input.clear()
    #     password_input.send_keys(password)

    #     password_input = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
    #     time.sleep(10)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywin = GUI()
    mywin.show()
    sys.exit(app.exec_())