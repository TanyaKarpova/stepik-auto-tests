import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

#Клик на первой вкладке; переход на вторую, расчет функции на второй
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

browser.find_element_by_class_name('btn-primary').click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_class_name('btn-primary').click()
