from time import sleep
from Base.init_driver import get_driver
from Page.operation_method import method_001
import Page,pytest

class Test_Case:
    # 初始化App
    def setup_class(self):
        self.Dv = method_001(get_driver())
    # 关闭App
    def teardown_class(self):
        self.Dv.driver.quit()
    """无前置条件_初始化App正确帐号登录，退出"""
    @pytest.mark.run(order=1)
    def test_register_quit(self):
        self.Dv.succeed_register()
        # 向上滑动屏幕
        self.Dv.up_slide()
        # 点击退出登录
        self.Dv.click_quit_register()
        # 点击退出登录_确定按钮
        self.Dv.click_quit_is_register()
        try:
            self.Dv.up_slide()
            if self.Dv.gain_a_group_text(Page.my_list):
                assert '马上登录' in self.Dv.gain_a_group_text(Page.my_list)
            else:
                assert False
        finally:
            self.Dv.screenshot()
    # """前置条件(已初始化App并在我的页面)_正确帐号登录"""
    # @pytest.mark.run(order=2)
    # def test_register(self):
    #     self.Dv.below_slide()
    #     if '马上登录' in self.Dv.gain_a_group_text(Page.my_list):
    #         # 点击登录、个人中心入口
    #         self.Dv.click_register()
    #         # 输入账户
    #         self.Dv.send_keys_text(Page.register_acctount, '13198690728')
    #         # 输入密码
    #         self.Dv.send_keys_text(Page.register_passwod, 'aaa123456')
    #         # 点击确定按钮
    #         self.Dv.click_register_confirm()
    #         try:
    #             if self.Dv.gain_a_group_text(Page.my_list):
    #                 assert '131986' in self.Dv.gain_a_group_text(Page.my_list)
    #             else:
    #                 assert False
    #         finally:
    #             self.Dv.screenshot()
    # """前置条件(已初始化App并在我的页面)_我的订单正确性验证"""
    # @pytest.mark.run(order=3)
    # def test_my_indent(self):
    #     # 点击我的订单按钮
    #     self.Dv.click_my_indent()
    #     # 点击返回按钮
    #     self.Dv.click_return_button()
    # """前置条件(已初始化App并在我的页面)_我发布的正确性验证"""
    # @pytest.mark.run(order=4)
    # def test_I_issue(self):
    #     # 点击我发布的按钮
    #     self.Dv.click_I_issue()
    #     # 点击官方发布
    #     self.Dv.click_official_recycle()
    #     # 点击返回按钮
    #     self.Dv.click_return_button()
    # """前置条件(已初始化App并在我的页面)_我的收藏正确性验证"""
    # @pytest.mark.run(order=5)
    # def test_my_collect(self):
    #     # 点击我的收藏
    #     self.Dv.click_my_collect()
    #     # 点击返回按钮
    #     self.Dv.click_return_button()
    # """前置条件(已初始化App并在我的页面)_我的关注正确性验证"""
    # @pytest.mark.run(order=6)
    # def test_my_attention(self):
    #     # 点击我的关注按钮
    #     self.Dv.click_my_attention()
    #     # 点击粉丝
    #     self.Dv.click_fans()
    #     # 点击返回按钮
    #     self.Dv.click_return_button()
    # """前置条件(已初始化App并在我的页面)_我的消息正确性验证"""
    # @pytest.mark.run(order=7)
    # def test_my_news(self):
    #     # 点击我的消息按钮
    #     self.Dv.click_news()
    #     # 点击我的评论
    #     self.Dv.click_my_comment()
    #     # 点击返回按钮
    #     self.Dv.click_return_button()
    #     # 点击系统消息
    #     self.Dv.click_system_news()
    #     for i in range(2):
    #         # 点击返回按钮
    #         self.Dv.click_return_button()
    # """前置条件(已初始化App并在我的页面)_我的红包正确性验证"""
    # @pytest.mark.run(order=8)
    # def test_my_red_packet(self):
    #     # 点击我的红包按钮
    #     self.Dv.click_my_red_packet()
    #     # 点击返回按钮
    #     self.Dv.click_return_button()
    # """前置条件(已初始化App并在我的页面)_隐私设置正确性验证"""
    # @pytest.mark.run(order=9)
    # def test_privacy_set(self):
    #     # 点击隐私设置
    #     self.Dv.click_privacy_set()
    #     # 点击电话隐私
    #     self.Dv.click_phone_privacy()
    #     # 点击返回按钮
    #     self.Dv.click_return_button()
    # """前置条件(已初始化App并在我的页面)_上滑屏幕_版本更新正确性验证"""
    # @pytest.mark.run(order=10)
    # def test_release_update(self):
    #     # 向上滑动屏幕
    #     self.Dv.up_slide()
    #     # 点击版本更新
    #     self.Dv.click_release_update()



if __name__ == '__main__':
    pytest.main('test_use_case_register.py')

