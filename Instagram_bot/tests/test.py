#!/urs/bin/python3
#-*- coding: utf-8 -*-










# import eel
# eel.init("web")
# eel.start("main.html")

# with open("test_users_list.txt", "r") as a:
#     users_names = a.read().split("\n")
#     print(users_names)


# with open("test_users_list.txt", "r") as a:
#     users_names1 = a.read()
#     users_names = []
#     users_names.append(users_names1)
#     if '\n '
# print(users_names)







# direc_users_list = open('test_users_list.txt','r')
# lines = direc_users_list.readlines()
# print(lines)


# if user in lines:
#     print(f'Мы уже подписаны на {user}, переходим к следующему пользователю!')
    






# followers_count = "177 подписчиков"
# if len(followers_count) == 16:
#     print("прикол какой-то2222")
# elif len(followers_count) == 15:
#     print("прикол какой-то")


# followers_count = '19,5тыс.'
# followers_count = (''.join(followers_count.split('тыс.')))
# followers_count = int(''.join(followers_count.split(',')))
# followers_count = followers_count * 100
# print(followers_count)




# followers_count = "26тыс. подписчиков"
# if followers_count.find('тыс.'):
#     followers_count = int(followers_count.split('тыс.')[0])
#     followers_count = followers_count * 1000
#     print("Количество подписчиков " + str(followers_count))
#     loops_count = int(followers_count / 12)
#     print("Число итераций:" + str(loops_count))



    #функция отправки сообщений

    # def send_direct_message(self,usernames='', message='', img_path=''):
    #     browser = self.browser
    #     time.sleep(random.randrange(2,4))

    #     direct_message_button = '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a'

    #     if not self.xpath_exists(direct_message_button):
    #         print("Кнопка отправки сообщений не найдена!")
    #         self.close_browser
    #     else:
    #         print("Отправляем сообщение...")
    #         direct_message = browser.find_element_by_xpath(direct_message_button).click()
    #         time.sleep(random.randrange(2, 4))
    #     # отключение всплывающего окна
    #     if self.xpath_exists("/html/body/div[5]/div/div"):
    #         browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    #     time.sleep(random.randrange(2, 4))

    #     send_message_button = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/button").click()
    #     time.sleep(random.randrange(2, 4))
        
    #     #отправка сообщения нескольким пользователям
    #     for user in usernames:

    #         # вводим получателя
    #         to_input = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input")
    #         to_input.send_keys(user)
    #         time.sleep(random.randrange(2, 4))

    #         users_list = browser.find_element_by_xpath(
    #             "/html/body/div[5]/div/div/div[2]/div[2]").find_element_by_tag_name("button").click()
    #         time.sleep(random.randrange(2, 4))


    #     next_button = browser.find_element_by_xpath(
    #         "/html/body/div[5]/div/div/div[1]/div/div[2]/div/button").click()
    #     time.sleep(random.randrange(2, 4))
    #     # отправка текстового сообщения
    #     if message:
    #         text_message_area = browser.find_element_by_css_selector(
    #                 "#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea")
    #         text_message_area.clear()
    #         text_message_area.send_keys(message)
    #         time.sleep(random.randrange(2, 4))
    #         text_message_area.send_keys(Keys.ENTER)
    #         print(f"Сообщение для {usernames} успешно отправлено!")
    #         time.sleep(random.randrange(2, 4))
        
    #     #отправка картинки
    #     if img_path:
    #         send_img_input = browser.find_element_by_xpath("/html/body/div[2]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input")
    #         send_img_input.send_keys(img_path)
    #         print(f"Изображение для {usernames} успешно отправлено!")
    #         time.sleep(random.randrange(2, 4))

    #     self.close_browser



    #     elif function == "3":
    # base_users = input('Вставьте базу получателей:')
    # with open(base_users, "r") as a:
    #     users_names = a.read().split("\n")
    # text_message = input("Введите сообщение которое надо отправить пользователям:")
    # my_bot = InstagramBot(username, password)
    # my_bot.login()
    # my_bot.send_direct_message(users_names,text_message,)

# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum + i
#     return theSum

# print("Количество лайков на странице:" + str(listsum(a)))

# a = [6, 9, 19, 29, 19, 23, 21, 38, 22, 22, 27, 45, 17, 17, 20, 15, 28, 20, 61, 12, 14, 64, 24, 30, 13, 13, 15, 10, 13, 15, 14, 14, 15, 10, 12, 11, 6, 26, 13, 17, 8, 11, 23, 21, 6, 11, 8, 10, 14, 12, 18, 12, 15, 11, 10, 12, 8, 7, 4, 18, 
# 5, 15, 10, 12, 6, 3, 7, 5, 6, 6]
# print(len(a))


# followers_count = "1,182 followers"
# if "k" in followers_count:
#     followers_count = (''.join(followers_count.split('k')))
#     followers_count = int(''.join(followers_count.split('.')))
#     followers_count = followers_count * 1000
# elif "," in followers_count:
#     followers_count = (''.join(followers_count.split(',')))
#     followers_count = int(followers_count.split(' ')[0])

# else:
#     followers_count = int(followers_count.split(' ')[0] + followers_count.split(' ')[1])

# print(followers_count)
            