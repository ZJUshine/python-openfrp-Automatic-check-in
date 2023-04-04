import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

# 设置网站URL和登录信息
url = 'https://console.openfrp.net/'
username = 'zjushine'
password = 'LUxuancun3641'

# 创建Chrome浏览器驱动器实例
driver = webdriver.Chrome(options=chrome_options)

# 打开网站
driver.get(url)

# 等待页面加载完成
time.sleep(5)

# 输入用户名和密码
driver.find_element("xpath",'/html/body/div[1]/div/div[1]/form/div[1]/div/div/div/input').send_keys(username)
driver.find_element("xpath",'/html/body/div[1]/div/div[1]/form/div[2]/div/div/div/input').send_keys(password)

# 点击登录按钮
driver.find_element("xpath",'//*[@id="of-app"]/div/div[1]/form/div[3]/button').click()

# 等待页面加载完成
time.sleep(5)

# 进入个人中心
driver.find_element("xpath",'//*[@id="of-app"]/div/div[1]/div[1]/ul/div/div[8]/li').click()

# 等待页面加载完成
time.sleep(5)

# 执行签到操作
driver.find_element("xpath",'//*[@id="of-app"]/div/div[2]/div/div/div/div[1]/div/div[2]/form/div[1]/div/div[1]/div[2]/button/span').click()

# 关闭浏览器
driver.quit()