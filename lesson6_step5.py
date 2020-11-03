from selenium import webdriver
import math

URL = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

try:
    browser.get(URL)

    text_link = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element_by_link_text(text_link)
    link.click()

    # поиск элементов
    input1 = browser.find_element_by_tag_name("input")
    input2 = browser.find_element_by_name("last_name")
    input3 = browser.find_element_by_class_name("city")
    input4 = browser.find_element_by_id("country")
    button = browser.find_element_by_css_selector("button.btn")

    # заполнение формы
    input1.send_keys("Ivan")
    input2.send_keys("Petrov")
    input3.send_keys("Smolensk")
    input4.send_keys("Russia")
    button.click()

    # проверка результата
    alert = browser.switch_to_alert()
    print (alert.text.split(': ')[-1])

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
