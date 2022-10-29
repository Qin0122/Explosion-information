from tkinter import filedialog, Tk, Label
import ttkbootstrap as tk
from ttkbootstrap.constants import *
from pynput.keyboard import Key, Controller as key
from pynput.mouse import Button as Bu, Controller as mouse_el
import time
from ctypes import *
import os
from PIL import Image
import win32con, win32clipboard
import pyautogui


"""
============= 窗口设计 ===========
"""
class Explosion_window(tk.Frame):
    # master等待接收根窗口对象，app等待接收自定义的模块
    def __init__(self, master=None, app=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack()
        # 调用在根窗口创建组件的函数
        self.createWidget()

    def createWidget(self):
        tk.Label(self, text='IT工藤新一 爆炸信息窗口', font=('华文行楷', 25)).grid(row=0, column=0, pady=10)
        tk.Button(self, text='第一式：我只说一句', command=self.first_formula, bootstyle=SUCCESS).grid(row=1, column=0, pady=10)
        tk.Button(self, text='第二式：唐僧念经', command=self.second_formula, bootstyle=SUCCESS).grid(row=2, column=0, pady=10)
        tk.Button(self, text='第三式：不说了，扔图', command=self.three_formula, bootstyle=SUCCESS).grid(row=3, column=0, pady=10)

    # 第一式
    def first_formula(self):
        root_1 = tk.Toplevel() # 实例化一个顶级类窗口
        root_1.title('第一式')
        root_1.geometry('500x300')
        tk.Label(root_1, text='第一式：我只说一句', font=('华文行楷', 22)).grid(row=0, column=1, pady=10)
        tk.Label(root_1, text='招数内容：', font=('华文行楷', 15)).grid(row=1,column=0)
        tk.Label(root_1, text='放招次数：', font=('华文行楷', 15)).grid(row=2, column=0)
        tk.Label(root_1, text='放招间隔(s)：', font=('华文行楷', 15)).grid(row=3, column=0)

        words = tk.StringVar() # 接收用户输入的文字
        times = tk.IntVar() # 结束放招次数
        time_interval = tk.IntVar() # 接收放招间隔

        tk.Entry(root_1, textvariable=words, font=('黑体', 15)).grid(row=1, column=1, pady=10)
        tk.Entry(root_1, textvariable=times, font=('黑体', 15)).grid(row=2, column=1, pady=10)
        tk.Entry(root_1, textvariable=time_interval, font=('黑体', 15)).grid(row=3, column=1, pady=10)
        tk.Button(root_1, text='确定放招', command=lambda: app.first_move(words.get(), times.get(), time_interval.get(), root_1), bootstyle=(SUCCESS, OUTLINE)).grid(row=4, column=1)
        root_1.mainloop()

    def second_formula(self):
        formula = 2
        self.second_three_formula(formula) # 调用放招函数

    def three_formula(self):
        formula = 3
        self.second_three_formula(formula)  # 调用放招函数

    def second_three_formula(self, formula): # 第二、第三式的窗口一样，为了提高代码的重用性，用选择判断语句进行操作
        root_2 = tk.Toplevel()

        if formula == 2:
            title1 = '第二式：唐僧念经'
            text1 = '选择txt文件'
            tk.Button(root_2, text='确定放招', command=lambda: app.second_move(filepath.get(), time_interval.get(), root_2),
                      bootstyle=(SUCCESS, OUTLINE)).grid(row=3, column=1, pady=10)

        elif formula == 3:
            title1 = '第三式：不说了，扔图'
            text1 = '选择表情包文件夹'
            tk.Button(root_2, text='确定放招', command=lambda: app.three_move(filepath.get(), time_interval.get(), root_2),
                      bootstyle=(SUCCESS, OUTLINE)).grid(row=3, column=1, pady=10)

        root_2.title(title1)
        root_2.geometry('700x190')
        filepath = tk.StringVar()  # 接收路径
        time_interval = tk.IntVar()  # 接收放招间隔
        tk.Label(root_2, text=title1, font=('华文行楷', 22)).grid(row=0, column=1)
        tk.Label(root_2, text='文件路径：', font=('华文行楷', 15)).grid(row=1, column=0)
        tk.Label(root_2, text='放招间隔(s)：', font=('华文行楷', 15)).grid(row=2, column=0)

        def select_file(filepath):  # 选择
            # 选择文件夹
            if formula == 2:
                select_file_path = filedialog.askopenfilename()  # 使用askopenfilename函数选择单个文件
            elif formula == 3:
                select_file_path = filedialog.askdirectory() # askdirectory选择文件夹
            filepath.set(select_file_path)

        tk.Entry(root_2, textvariable=filepath, font=('黑体', 15)).grid(row=1, column=1)
        tk.Entry(root_2, textvariable=time_interval, font=('黑体', 15)).grid(row=2, column=1)
        tk.Button(root_2, text=text1, command=lambda: select_file(filepath)).grid(row=1, column=2, pady=10)

    # 倒计时
    def count_down(self, info=None):
        pass


"""
=============== 功能实现 ================
"""
class Send_information(object):
    def __init__(self):
        pass

    # 放招函数，用于第一、二式
    def Release_moves(self, words=None, times=0, time_interval=0, txt_li=None): # times接收发送的次数，time_interval接收发送的时间间隔
        keyboard = key()  # 获取键盘权限
        mouse = mouse_el()  # 获取鼠标权限
        mouse.press(Bu.left)  # 鼠标左键点击
        mouse.release(Bu.left)  # 鼠标左键松开
        n = 5
        print('请在五秒内将鼠标放到聊天框内并点击！！！')
        for k in range(5):
            print(f'倒计时{n - k}秒')
            time.sleep(1)  # 程序运行等待五秒你是猪

        if times == 0:
            for i in txt_li:
                keyboard.type(f"{i}")  # 输入框的内容
                keyboard.press(Key.enter)  # 回车键按下
                keyboard.release(Key.enter)  # 回车键松开
                time.sleep(time_interval)
        else:
            for i in range(times):
                keyboard.type(f"{words}")  # 输入框的内容
                keyboard.press(Key.enter)  # 回车键按下
                keyboard.release(Key.enter)  # 回车键松开
                time.sleep(time_interval)


    # 接收用户输入的数据
    def first_move(self, words, times, time_interval, root_1):
        root_1.destroy()
        self.Release_moves(words=words, times=times, time_interval=time_interval) # 调用放招函数


    # 接收用户选择的文件路径
    def second_move(self, txt_path, time_interval, root_2):
        root_2.destroy()
        txt_li = [] # 保存txt中的语句
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f: # 循环遍历输出txt文件内容
                if line in ['\n', '\r\n']: # 判空处理
                    pass
                elif line.strip() == "": # 空行直接跳过
                    pass
                else:
                    txt_li.append(line.strip()) # 将内容保存到txt中
        self.Release_moves(txt_li=txt_li, time_interval=time_interval) # 调用放招哈数


    # 接收用户选择的图片
    def three_move(self, photo_path, time_interval, root_3):
        root_3.destroy()
        filepath = [photo_path + '/' + file for file in os.listdir(photo_path)] # 拼接路径
        i = 0
        n = 5
        print('请在五秒内将鼠标放到聊天框内并点击！！！')
        for k in range(5):
            print(f'倒计时{n - k}秒')
            time.sleep(1)  # 程序运行等待五秒你是猪

        # 复制图片
        for path in filepath:
            try:
                im = Image.open(path)
                im.save('11.bmp')
                aString = windll.user32.LoadImageW(0, r"11.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)
            except:
                continue

            if aString != 0:  ## 由于图片编码问题  图片载入失败的话  aString 就等于0
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.SetClipboardData(win32con.CF_BITMAP, aString)
                win32clipboard.CloseClipboard()

                keyboard = key()  # 获取键盘权限
                if i == 0:
                    i += 0
                pyautogui.hotkey('ctrl', 'v')
                keyboard.press(Key.enter)  # 回车键按下
                keyboard.release(Key.enter)  # 回车键松开
                time.sleep(time_interval)

if __name__ == '__main__':
    root = tk.Window()   # 建立一个根窗口
    root.title('爆炸信息') # 窗口名称
    root.geometry('500x300') # 窗口大小  宽x高
    app = Send_information() # 实例化Send_information对象
    Explosion_window(root, app) # 实例化Explosion_window对象
    root.mainloop()





