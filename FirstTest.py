from selenium.webdriver.support.ui import Select
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Лёша\\Desktop\\HomeWork\\chromedriver.exe")

#1. Перейти по ссылке на главную страницу сайта Netpeak. (https://netpeak.ua/)
driver.get("https://netpeak.ua/")
driver.maximize_window()
#2. Перейдите на страницу "Работа в Netpeak", нажав на кнопку "Карьера"
driver.find_element_by_link_text("Карьера").click()
#3. Перейти на страницу заполнения анкеты, нажав кнопку - "Я хочу работать в Netpeak"
driver.find_element_by_link_text("Я хочу работать в Netpeak").click()
#4. Загрузить файл с недопустимым форматом в блоке "Резюме", например png, и проверить что на странице появилось сообщение, о том что формат изображения неверный.
driver.find_element_by_name('up_file').send_keys('C:\\Users\\Лёша\\Desktop\\HomeWork\\1.png')
alertMessage = driver.find_element_by_id("up_file_name")
assert alertMessage.text == "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)."
#5. Заполнить случайными данными блок "3. Личные данные"
daySelect = Select(driver.find_element_by_name('bd'))
daySelect.select_by_value('26')
daySelect = Select(driver.find_element_by_name('bm'))
daySelect.select_by_value('03')
daySelect = Select(driver.find_element_by_name('by'))
daySelect.select_by_value('1988')
driver.find_element_by_id('inputName').send_keys('Oleksii')
driver.find_element_by_id('inputLastname').send_keys('Klein')
driver.find_element_by_id('inputEmail').send_keys('gglodessa@gamil.com')
driver.find_element_by_id('inputPhone').send_keys('0639714230')
#6. Нажать на кнопку отправить резюме
driver.find_element_by_id('submit').click()
#7. Проверить что сообщение на текущей странице - "Все поля являются обязательными для заполнения" - подсветилось красным цветом
color = driver.find_element_by_xpath("/html/body/div[2]/div/p").value_of_css_property("color")
assert color == "rgba(255, 0, 0, 1)"
#8. Нажать на логотип для перехода на главную страницу и убедиться что открылась нужная страница.
driver.find_element_by_class_name('logo-block').click()
assert "Раскрутка сайта, продвижение сайтов: Netpeak Украина — performance-маркетинг для бизнеса" in driver.title
driver.quit()
