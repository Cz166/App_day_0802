from selenium.webdriver.common.by import By

"""
初始页面
"""

# 启动页面_教程_进入爱优品
access_love_youpin = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/ip_ll_enter')
# 始终允许按钮
allow_button = (By.ID,'com.android.packageinstaller:id/permission_allow_button')


"""
个人中心功能
"""
# 我的_按钮
my_button = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/lfi_tv_my')
# 我的_列表（一组）
my_list = (By.CLASS_NAME,'android.widget.TextView')
# 登录、个人中心入口按钮
personal_center = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_rl_login')
# 退出登录按钮
quit_register = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_ll_out_login')
# 退出登录_确定按钮
quit_is_register= (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/dc_right')
# 登录页面_账户
register_acctount = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_et_user')
# 登录页面_密码
register_passwod = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_et_pwd')
# 登录页面_确定页面
register_confirm = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/al_ll_login')

"""
我的订单
"""
# 我的订单
my_indent = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_rl_my_order')
# 我的订单_返回按钮
return_button = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/lt_rl_left')

"""
我发布的
"""
# 我发布的
I_issue = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_rl_my_release')
# 我的发布_官方回收
official_recycle = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/amr_tv_official')

"""
我的收藏
"""
# 我的收藏
my_collect = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_rl_collect')

"""
我的关注
"""
# 我的关注
my_attention = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_rl_myfollow')
# 粉丝
fans = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/amr_tv_fans')

"""
我的消息
"""
# 我的消息
my_news = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_rl_my_message')
# 我的消息_我的评论
my_comment = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/amm_rl_comment')
# 我的消息_系统消息
system_news = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/amm_rl_message')

"""
我的红包
"""
# 我的红包
my_red_packet = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_rl_my_red_packet')

"""
隐私设置
"""
# 隐私设置
privacy_set = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_rl_my_password')
# 电话隐私
phone_privacy = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/btn')

"""
版本更新
"""

# 版本更新
release_update = (By.ID,'com.huashidai.cl.lovegoods.lovegoods:id/fm_rl_update')