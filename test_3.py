from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time 
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import os
import re
import sys
from PyQt5 import QtCore, QtGui, QtWidgets 
from auth import *   
from switch import * 
from followers import *                                               


class InstagramBot():
    def __init__(self, username, password):
    
       self.username = username
       self.password = password
       options = Options()
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
        username_input.send_keys(self.username)                          

        time.sleep(5)
        password_input = browser.find_element_by_name("password") 
        password_input.clear()
        password_input.send_keys(self.password)                          
        password_input = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
        time.sleep(10)

    def get_all_followers(self,userpage):


        # browser = self.browser
        browser.get(userpage)
        time.sleep(4)
        file_name = userpage.split('/')[-2]

        if os.path.exists(f"{file_name}"):
            print(f"Папка {file_name} уже существует!")
        else:
            print(f"Создаём папку пользователя {file_name}")
            os.mkdir(file_name)

        wrong_userpage = "/html/body/div[1]/section/main/div/h2"
        if self.xpath_exists(wrong_userpage):
            print(f"Пользователя {file_name} не существует, проверьте URL")
            self.close_browser()
        else:
            print(f"Пользователь {file_name} успешно найден, начинаем скачивать ссылки на подписичиков!")
            time.sleep(2)

            followers_button = browser.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span") 
            followers_count = followers_button.text
            if "k" in followers_count:
                followers_count = (''.join(followers_count.split('k')))
                followers_count = int(''.join(followers_count.split('.')))
                followers_count = followers_count * 100
            elif "," in followers_count:
                followers_count = (''.join(followers_count.split(',')))
                followers_count = int(followers_count.split(' ')[0])
            else:
                followers_count = int(followers_count.split(' ')[0])
            
            print("Количество подписчиков " + str(followers_count))

            time.sleep(2)

            loops_count = int(followers_count / 12)
            if loops_count > 300:
                loops_count = 100
            print(f"Число итераций: {loops_count}")
            time.sleep(4)

            followers_button.click()
            time.sleep(4)

            followers_ul = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
            print(followers_ul)

            try:
                followers_urls = []
                for i in range(1, loops_count + 1):
                    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_ul)
                    time.sleep(random.randrange(2, 4))
                    print(f"Итерация #{i}")
                    
                all_urls_div = followers_ul.find_elements_by_tag_name("li")

                for url in all_urls_div:
                    url = url.find_element_by_tag_name("a").get_attribute("href")
                    followers_urls.append(url)
                
                #сохраняем подписчиков в файл
                with open(f"{file_name}/{file_name}.txt", "a") as text_file:
                    for link in followers_urls:
                        text_file.write(link + "\n")

                with open(f"{file_name}/{file_name}.txt") as text_file:
                    users_urls = text_file.readlines()

                    for user in users_urls[0:100000]:
                        try:
                            try:
                                with open(f'{file_name}/{file_name}_subscribe_list.txt','r') as subscribe_list_file:
                                    lines = subscribe_list_file.readlines()
                                    if user in lines:
                                        print(f'Мы уже подписаны на {user}, переходим к следующему пользователю!')
                                        continue

                            except Exception as ex:
                                print('Файл со ссылками ещё не создан!')
                                # print(ex)

                            browser = self.browser
                            browser.get(user)
                            page_owner = user.split("/")[-2]

                            if self.xpath_exists("/html/body/div[1]/section/main/div/header/section/div[1]/div/a"):

                                print("Это наш профиль, уже подписан, пропускаем итерацию!")
                            elif self.xpath_exists(
                                    "/html/body/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button"):
                                print(f"Уже подписаны, на {page_owner} пропускаем итерацию!")
                            else:
                                time.sleep(random.randrange(4, 8))

                                if self.xpath_exists(
                                        "/html/body/div[1]/section/main/div/div/article/div[1]/div/h2"):
                                    try:
                                        follow_button = browser.find_element_by_css_selector(
                                            "#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div > button").click()
                                        print(f'Запросили подписку на пользователя {page_owner}. Закрытый аккаунт!')
                                    except Exception as ex:
                                        print(ex)
                                else:
                                    try:
                                        if self.xpath_exists("/html/body/div[2]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button"):
                                            follow_button = browser.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div > div > span > span.vBF20._1OSdk > button").click()
                                            print(f'Подписались на пользователя {page_owner}. Открытый аккаунт!')
                                        else:
                                            follow_button = browser.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm > div > div > div > span > span.vBF20._1OSdk > button").click()
                                            print(f'Подписались на пользователя {page_owner}. Открытый аккаунт!')
                                    except Exception as ex:
                                        print(ex)
                                    # записываем данные в файл для ссылок всех подписок, если файла нет, создаём, если есть - дополняем
                                    with open(f'{file_name}/{file_name}_subscribe_list.txt','a') as subscribe_list_file:
                                        subscribe_list_file.write(user)

                                    time.sleep(random.randrange(8, 12))

                        except Exception as ex:
                            print(ex)
                            self.close_browser()

            except Exception as ex:
                print(ex)
                self.close_browser()

        self.close_browser()


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()                                              
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.go_to)
        
    def go_to(self):
        username = self.ui.lineEdit.text()                              
        password = self.ui.lineEdit_2.text()                            
        self.ui.lineEdit.clear()                                        
        self.ui.lineEdit_2.clear()                                      
        authwin.close()
        switchwin.show()
        self.inst = InstagramBot(username, password)
        self.inst.login()

class Followers(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()                                              
        self.ui = Ui_Form1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_follow)
    
    def start_follow(self):
        userpage = self.ui.lineEdit.text()
        self.inst = InstagramBot(username,password)
        self.inst.login()
        self.inst.get_all_followers(userpage)



class Switch(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()                                              
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.follow)
    
    def follow(self):
        followwin.show()





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    switchwin = Switch()
    followwin = Followers()
    authwin = GUI()
    authwin.show()
    sys.exit(app.exec_())


# Короче смотри свитч страница с набором функций фолловерс это именно подписки , тебе надо в них передать значени юзернейм и пороль

#Короче смотри скорее всего чтоб не мучаться тебе придется подключать sql другого выхода с передачей пороля я не вижу , либо же тебе надо переписать код и поменять дизайн без первоначального входа , просто свич окно в котором будут кнопки с функциями и уже в окне каждой функции отдельно выводить форму входа 