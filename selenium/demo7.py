# 网页常常会因为网络原因，程序问题等等导致打开网页慢，一直在那里打圈圈。
# 出现这种情况时网页里的很多元素就没有加载完成，如果你刚好要定位的元素没有加载完，这时定位的话程序就会抛出异常。
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 引入等待条件
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

# 隐式等待是一个全局设置，设置后所有的元素定位都会等待给定的时间，直到元素出现为止，等待规定时间元素没出现就报错。
# driver.implicitly_wait(10)

# driver.find_element_by_id('123')

# 显示等待就是设置一个等待时间，直到这个元素出现就停止等待，如果没出现就抛出异常。
# 使用的WebDriverWait().until()方法，WebDriverWait()里填driver和要等待的时间，until里填等待的元素。
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "search-show"))
)