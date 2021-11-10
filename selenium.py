from time import sleep
import selenium
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
class TestWemork:
    def test_wework_cookie(self):
        # 使用命令行chrome --remote-debugging-port=9222打开调试浏览器
        # 在调试浏览器上进行要复用的操作然后执行下面的脚本（节省这些复用的操作时间）
        # 使用chrome复用（只有谷歌能复用）
        option = webdriver.ChromeOptions()
        # 设置debug地址给option
        option.debugger_address = "127.0.0.1:9222"
        # 设置驱动为调试的驱动
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        # 复用之后接下来的操作
        self.driver.find_element_by_link_text("通讯录").click()
        # self.driver.find_element_by_id("username").send_keys("5264")
        cookie=self.driver.get_cookies()
        # print(cookie)
        yaml.dump(cookie,open("cookies.yaml","w",encoding="UTF_8"))


def test_cookie():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
    cookies=yaml.safe_load(open("cookies.yaml",encoding="UTF_8"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    sleep(3)
    driver.find_element(By.LINK_TEXT,"添加成员").click()
    # driver.find_element(By.LINK_TEXT,"添加成员").click()
    sleep(3)
    driver.find_element_by_id("username").send_keys("ksdhak")
    driver.find_element(By.XPATH,"//div[@class='member_edit_item_right']/input[@name='acctid']").send_keys("hshsg233")
    driver.find_element(By.ID,"memberAdd_phone").send_keys("13265456545")
    driver.find_element(By.XPATH,"//input[@class='ww_checkbox'and@name='sendInvite']").click()
    driver.find_element(By.XPATH,"//form/div[@class='member_colRight_operationBar ww_operationBar']/a[@class='qui_btn ww_btn js_btn_save']").click()
#    我没遇到 添加成员按钮 点击失败的问题，直接跑通了
