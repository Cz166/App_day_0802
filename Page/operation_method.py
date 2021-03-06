import time
import allure
from appium.webdriver.common.touch_action import TouchAction
from Base.Base import Base
import Page

class method_001(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    """
    常用滑动屏幕
    """

    @allure.step(title='滑动屏幕向右')
    def right_downward_slide(self):
        TouchAction(self.driver).press(x=965, y=1666).move_to(x=77, y=1582).release().perform()
    @allure.step(title='滑动屏幕向上')
    def up_slide(self):
        TouchAction(self.driver).press(x=481, y=1672).move_to(x=504, y=691).release().perform()
    @allure.step(title='滑动屏幕向下')
    def below_slide(self):
        TouchAction(self.driver).press(x=504, y=691).move_to(x=481, y=1672).release().perform()

    """
    截图
    """
    @allure.step(title='屏幕截图操作')
    def screenshot(self):
        now = time.strftime('%Y_%m_%d-%H_%M_%S')
        return self.driver.get_screenshot_as_file \
            ('E:/PyCharm 2017.3.4/App_08_01/Screenshot/register_001_%s.png' % now)

    """
    初始页面
    """

    @allure.step(title='点击启动页面_教程_进入爱优品按钮')
    def click_access_love_youpin(self):
        self.click_element(Page.access_love_youpin)

    @allure.step(title='点击始终允许')
    def click_allow_button(self):
        self.click_element(Page.allow_button)

    """
    个人中心
    """
    @allure.step(title='点击_我的')
    def click_my_button(self):
        self.click_element(Page.my_button)

    @allure.step(title='点击登录、个人中心入口按钮')
    def click_register(self):
        self.click_element(Page.personal_center)

    @allure.step(title='点击退出登录按钮')
    def click_quit_register(self):
        self.click_element(Page.quit_register)

    @allure.step(title='点击退出登录_确定按钮')
    def click_quit_is_register(self):
        self.click_element(Page.quit_is_register)

    @allure.step(title='点击登录页面_确定按钮')
    def click_register_confirm(self):
        self.click_element(Page.register_confirm)


    """
    我的订单
    """

    @allure.step(title='点击我的订单按钮')
    def click_my_indent(self):
        self.click_element(Page.my_indent)
    @allure.step(title='我的订单_点击返回按钮')
    def click_return_button(self):
        self.click_element(Page.return_button)
    @allure.step(title='点击我发布的按钮')
    def click_I_issue(self):
        self.click_element(Page.I_issue)
    @allure.step(title='点击官方回收按钮')
    def click_official_recycle(self):
        self.click_element(Page.official_recycle)
    @allure.step(title='点击我的收藏')
    def click_my_collect(self):
        self.click_element(Page.my_collect)
    @allure.step(title='点击我的关注')
    def click_my_attention(self):
        self.click_element(Page.my_attention)
    @allure.step(title='点击粉丝')
    def click_fans(self):
        self.click_element(Page.fans)
    @allure.step(title='点击我的消息')
    def click_news(self):
        self.click_element(Page.my_news)
    @allure.step(title=' 点击我的评论')
    def click_my_comment(self):
        self.click_element(Page.my_comment)
    @allure.step(title='点击系统消息')
    def click_system_news(self):
        self.click_element(Page.system_news)
    @allure.step(title='点击我的红包')
    def click_my_red_packet(self):
        self.click_element(Page.my_red_packet)
    @allure.step(title='点击隐私设置')
    def click_privacy_set(self):
        self.click_element(Page.privacy_set)
    @allure.step(title='点击电话隐私')
    def click_phone_privacy(self):
        self.click_element(Page.phone_privacy)
    @allure.step(title='点击版本更新')
    def click_release_update(self):
        self.click_element(Page.release_update)
    # 常用方法_正确帐号登录（断言是否登录成功并截图）
    @allure.step(title='输入正确帐号、密码，成功登录')
    def succeed_register(self):
        # 向右滑动屏幕
        for i in range(3):
            self.right_downward_slide()
        # 点击进入爱优品按钮
        self.click_access_love_youpin()
        # 点击始终允许按钮
        self.click_allow_button()
        # 点击我的按钮
        self.click_my_button()
        # 获取登录状态
        if '马上登录' in self.gain_a_group_text(Page.my_list):
            # 点击登录、个人中心入口
            self.click_register()
            # 输入账户
            self.send_keys_text(Page.register_acctount, '13198690728')
            # 输入密码
            self.send_keys_text(Page.register_passwod, 'aaa123456')
            # 点击确定按钮
            self.click_register_confirm()
            try:
                if self.gain_a_group_text(Page.my_list):
                    assert '131986' in self.gain_a_group_text(Page.my_list)
                else:
                    assert False
            finally:
                self.screenshot()
