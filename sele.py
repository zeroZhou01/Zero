from time import sleep
import selenium
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
class TestWemork:
    def test_wework_cookie(self):
        print("开始测试")
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
    driver.get("http://dmstest.gdyph.com")
    sleep(3)
    #通过id查找元素赋值
    driver.find_element(By.ID,"company").send_keys("广州一品红制药有限公司")
    print("公司名称赋值成功....")
    sleep(1)
    driver.find_element(By.ID, "act").send_keys("20500280")
    print("账号赋值成功.....")
    sleep(1)
    driver.find_element(By.ID, "pwd").send_keys("edoc2")
    print("密码赋值成功....")
    sleep(1)
    driver.find_element(By.ID,"submit").click()
    print("登录成功！......")
    sleep(1)
    driver.find_element(By.LINK_TEXT, "文档").click()
    print("跳转到文档模块")
    input("按任意键结束")
#   driver.find_element_by_id("username").send_keys("ksdhak") 过期
#   driver.find_element(By.XPATH,"//div[@class='member_edit_item_right']/input[@name='acctid']").send_keys("hshsg233")
#   driver.find_element(By.XPATH,"//input[@class='ww_checkbox'and@name='sendInvite']").click()
#   driver.find_element(By.XPATH,"//form/div[@class='member_colRight_operationBar ww_operationBar']/a[@class='qui_btn ww_btn js_btn_save']").click()
#    driver.find_element(By.LINK_TEXT,"添加成员").click()
if __name__ == '__main__':
    test_cookie()