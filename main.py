# -*- coding:utf-8 -*-
# @project: 闲聊机器人
# @filename: main.py
# @author: ShuleHao
# @contact: 2571540718@qq.com
# @time: 2022/8/25 7:23
# @Blog:https://blog.csdn.net/hubuhgyf?type=blog
import sys
sys.path.append('..')
from gpt_bot import GPTBot
import psutil
from pywinauto.application import Application
import pyperclip
import io
import sys
import time
import pyautogui
from wxauto import WeChat
from love_api import romantic,good_night,good_morning,star,brain_teaser,love_talk
pyautogui.FAILSAFE = False  # 关闭自动保护机制
import datetime
# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
class Cj(object):
    def __init__(self,friend):
        self.friend=friend
        # 获取到程序进程 PID
        procId = self.get_pid("WeChat.exe")

        if (procId == -1):
            print("WeChat.exe  is not running")

        # 连接到对应的app
        app = Application(backend='uia').connect(process=procId)

        # 获取到微信实例
        self.main_Dialog = app.window_(title=u"微信", class_name="WeChatMainWndForPC")

        # 打开微信窗口
        pyautogui.hotkey('ctrl', 'alt', 'w')

        # 弹出窗口,防止快捷键打开失败
        self.main_Dialog.restore()

        # 打开指定的用户消息框
        self.main_Dialog.type_keys('^f')
        pyperclip.copy(friend)
        self.main_Dialog.type_keys('^v')
        # 打开指定用户的发消息页面
        self.main_Dialog.type_keys('{ENTER}')
        self.wx = WeChat()
        self.bot = GPTBot()

    # 根据进程名获取到对应的id ,用于连接
    def get_pid(self,processName):
        for proc in psutil.process_iter():
            try:
                if (proc.name() == processName):
                    return proc.pid
            except psutil.NoSuchProcess:
                pass
        return -1
    def ai_robot(self,frequency):
        print("开始使用ai_robot")
        '''
        :param frequency:对象不回消息的条数
        :return:
        '''
        temp = 0
        message_len_list = []
        while True:
            msgs = self.wx.GetAllMessage
            out_or_in=self.wx.GetLastMessage[0]
            friend_text = []
            for msg in msgs:
                if msg[0] == self.friend:
                    friend_text.append(msg[1])
            if out_or_in != self.friend:#不回消息
                    temp += 1
            if temp == frequency:  # 对方不回消息几次停止发送
                break
            # 最新的一条消息作为ai机器人的输入
            text = friend_text[-1]
            info = self.bot.answer(text)
            inputMsg = self.main_Dialog.child_window(title="输入", control_type="Edit")
            inputMsg.click_input()
            pyperclip.copy(info)
            inputMsg.type_keys('^v')
            self.main_Dialog.type_keys('{ENTER}')
            time.sleep(2)
    def Judgment_message(self):
        message=self.wx.GetLastMessage
        # print("女朋友说：",message)
        if message[0]==self.friend:
            return message[1]
        return None
    def send_message_normally(self,info):
        inputMsg = self.main_Dialog.child_window(title="输入", control_type="Edit")
        inputMsg.click_input()
        pyperclip.copy(info)
        inputMsg.type_keys('^v')
        self.main_Dialog.type_keys('{ENTER}')
    def love_talk_or_ai_bot(self,info):
        info=love_talk(info)
        print("恋爱宝典：",info)
        if info:
            inputMsg = self.main_Dialog.child_window(title="输入", control_type="Edit")
            inputMsg.click_input()
            pyperclip.copy(info)
            inputMsg.type_keys('^v')
            self.main_Dialog.type_keys('{ENTER}')
        else:
            self.ai_robot(5)


    def earthy_love_story(self,info):
        '''
        :param info:list
        :return:
        '''
        if len(info) > 1:
            inputMsg = self.main_Dialog.child_window(title="输入", control_type="Edit")
            inputMsg.click_input()
            pyperclip.copy(info[0])
            inputMsg.type_keys('^v')
            self.main_Dialog.type_keys('{ENTER}')
            time.sleep(0.5)
            temp_stwich = True
            while True:
                if (self.wx.GetLastMessage[0] == self.friend) and (temp_stwich):
                    inputMsg = self.main_Dialog.child_window(title="输入", control_type="Edit")
                    inputMsg.click_input()
                    pyperclip.copy(info[1])
                    inputMsg.type_keys('^v')
                    self.main_Dialog.type_keys('{ENTER}')
                    time.sleep(0.5)
                    temp_stwich = False
                else:
                    my_brain = love_talk(self.Judgment_message())
                    if my_brain:
                        self.send_message_normally(my_brain)
                    #ai机器人为备选
                    else:
                        self.ai_robot(5)
        else:
            inputMsg = self.main_Dialog.child_window(title="输入", control_type="Edit")
            inputMsg.click_input()
            pyperclip.copy(info[0])
            inputMsg.type_keys('^v')
            self.main_Dialog.type_keys('{ENTER}')
            time.sleep(0.5)
            while True:
                if self.Judgment_message():
                    my_brain=love_talk(self.Judgment_message())
                    if my_brain:
                        self.send_message_normally(my_brain)
                    else:
                        self.ai_robot(5)

girl_friend=Cj("xxx")#输入发送人的微信备注
print("初始化已完成")
temp=True#指针防止多次重复发送
while True:
    cur = datetime.datetime.now()
    # 早安
    if (cur.hour == 5) and (cur.minute == 20)and(temp):
        print("早安")
        temp=False
        girl_friend.send_message_normally(good_morning())
    # 星座
    elif (cur.hour == 7) and (cur.minute == 31)and(temp):
        print("星座")
        temp = False
        girl_friend.send_message_normally(star())
    # 脑筋急转弯
    elif (cur.hour == 13) and (cur.minute == 14)and(temp):
        print("脑筋急转弯")
        temp = False
        girl_friend.send_message_normally(brain_teaser())
    # 土味情话
    elif (cur.hour == 17) and (cur.minute == 20)and(temp):
        print("土味情话")
        temp = False
        girl_friend.earthy_love_story(romantic())
    # 晚安
    elif (cur.hour == 21) and (cur.minute == 19)and(temp):
        print("晚安")
        temp = False
        girl_friend.send_message_normally(good_night())
    elif not (temp) and (cur.hour != 5)and(cur.hour != 7) and(cur.hour != 13) and(cur.hour != 17) and(cur.hour != 21):
        temp=True#恢复指针状态
    elif girl_friend.Judgment_message():
        print("回复消息")
        girl_friend.love_talk_or_ai_bot(girl_friend.Judgment_message())
    else:continue