# -*- coding: utf-8 -*-

import requests
import urllib
import tkinter
import json
from sys import exit


def auto_login(userId, password):

    try:
        response = requests.get("http://123.123.123.123")
    except:
        print('Error! You may already login!')
        exit(0)

    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Referer':response.text.strip().lstrip("<script>top.self.location.href='").rstrip("'</script>"),
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) TkinterleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }

    url = "http://202.118.253.94:8080/eportal/InterFace.do?method=login"
    prefix = "<script>top.self.location.href='http://202.118.253.94:8080/eportal/index.jsp?"
    suffix = "'</script>"
    paraments = urllib.parse.quote(response.text.strip().lstrip(prefix).rstrip(suffix))
    paraments = urllib.parse.quote(paraments)
    form_data = "userId=" + userId + "&password=" + password + "&service=&queryString=" + paraments + "&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false"
    response = requests.post(url, data=form_data, headers=headers)
    response.encoding = 'utf-8'

    if not response.ok:
        print("Error:", response.status_code)
        exit(0)

    if response.json()['result'] == "success":
        print("Login succeeded.")
    else:
        print("Login failed:", response.json()['message'])


def read_data():
    try:
        with open(r'data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        return 0

    return data


def save_data():
    global username_entry
    global password_entry
    
    username=username_entry.get()
    password=password_entry.get()
    
    with open(r'data.json', 'w') as f:
        json.dump('$'.join((username, password)), f)
    
    auto_login(username,password)



def draw_window():
    ''' 设置窗口 '''
    window = tkinter.Tk()
    window.title('HIT-WLAN Auto Login')
    window.geometry('400x500')
    
    ''' Logo '''
    Logo=tkinter.PhotoImage(file="HIT_LOGO.png")  
    logo_label = tkinter.Label(window,image=Logo)
    logo_label.pack()
    
    ''' 标题 '''
    title_label=tkinter.Label(window,
                              text='HIT-WLAN Auto Login',
                              font=('Consolas',18))
    title_label.pack()
    
    ''' 文本框标签 '''
    username_label = tkinter.Label(window, text="学号",font=('等线',12))
    password_label = tkinter.Label(window, text="密码",font=('等线',12))
    
    ''' 文本框 '''
    username = tkinter.StringVar()
    password = tkinter.StringVar()
    
    global username_entry
    global password_entry
    username_entry = tkinter.Entry(window, show=None, textvariable=username)
    password_entry = tkinter.Entry(window, show='*', textvariable=password)
    
    ''' 显示文本框及其标签 '''
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    
    ''' 按钮 '''
    button = tkinter.Button(window, text='Save', font=('Consolas',10),command=save_data)
    button.pack()
    
    tkinter.mainloop()


def main():
    if read_data() == 0:
        draw_window()
    else:
        username = read_data().split('$')[0]
        password = read_data().split('$')[1]
        auto_login(username, password)

        wait=input('press enter to exit')


if __name__ == '__main__':
    main()
