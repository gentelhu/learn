from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 初始化浏览器驱动，这里以Chrome为例
driver = webdriver.Chrome()

# 打开网页
url = "https://meskc.ck.kenda.com.tw:8810/#/login?redirect=%2FproductionPlan"
driver.get(url)
time.sleep(3)  # 等待页面加载，可根据实际情况调整时间

# 输入账号
account_input = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
account_input.send_keys("562389")

# 输入密码
password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password_input.send_keys("562389")

# 点击登入按钮
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# 这里可以添加后续的操作，例如等待页面跳转后进行其他操作
time.sleep(5)

# 关闭浏览器
driver.quit()