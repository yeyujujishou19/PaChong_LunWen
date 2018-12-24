#!/usr/bin/env Python
# coding=utf-8
import  os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import json

#浏览器初始化
def browser_init(isWait):
    options = webdriver.ChromeOptions() #初始化变量
    #设置参数
    prefs = {'profile.default_content_settings.popups': 0,
             'download.default_directory': 'E:/sxl_Programs/Python/PDF/'}
    options.add_experimental_option('prefs', prefs)

    browser = webdriver.Chrome(executable_path='chromedriver.exe',
                               chrome_options=options)
    browser.set_window_size(500, 500)
    if isWait:
        browser.implicitly_wait(50)
    return browser

#登录网页
def login(username, password):
    browser.get('http://login.cnki.net/login')
    browser.find_element_by_id('TextBoxUserName').send_keys(username)
    browser.find_element_by_id('TextBoxPwd').send_keys(password)
    browser.find_element_by_id('Button1').click()


linkPath="E:/sxl_Programs/Python/paper_links_dict1.json"
bGlobalflag=True
while bGlobalflag:
    try:
        fileObject = open('DownLoadedLink.txt', "a")  # 保存已经下载的链接
        fileRead = open('DownLoadedLink.txt', "r")  # 读取已经下载的链接
        txtLines = fileRead.readlines()  # 读取txt内容
        browser = browser_init(True)  # 初始化浏览器
        login('ttod', 'ttod')  # 登录
        with open(linkPath, "r", encoding='UTF-8') as f:
            s = json.load(f)
            print(type(s))
            print(len(s))
            for key in s.keys():
                print(key)
                for subkey in s[key].keys():
                    print(subkey)
                    for i,url in enumerate(s[key][subkey]):
                        bflag=0
                        for c in txtLines:
                            a=c.find(url)
                            if(a==0):
                                # print("%s 已下载！" % (url))
                                bflag = 1
                        if(bflag==1):
                            continue    #如已经下载，则跳过
                        print(i,url)
                        browser.get(url)
                        paper_title = browser.title
                        print ('paper title:'+paper_title)
                        if '中国专利全文数据库' in paper_title:
                            continue
                        print('try download:'+paper_title)
                        try:
                            browser.find_element_by_xpath("//a[contains(text(),'PDF下载')]").click()
                            print('download pdf')
                            fileObject.write(url)   #将下载好的连接保存在txt中
                            fileObject.write('\n')
                        except NoSuchElementException as e:
                            try:
                                browser.find_element_by_xpath("//a[contains(text(),'整本下载')]").click()
                                print('download caj')
                                fileObject.write(url)  # 将下载好的连接保存在txt中
                                fileObject.write('\n')
                            except NoSuchElementException as e:
                                fileObject.write(url)  # 将下载好的连接保存在txt中
                                fileObject.write('\n')
                                print('download fail!')
                        if(subkey=="博硕士"):
                            sleep(15)
                        else:
                            sleep(15)
            bGlobalflag = False
    except:
        print ('process exception')      #不执行
        fileObject.close()  # 关闭文件
        print('重新启动')  #


print ('结束！')       #
fileObject.close()  # 关闭文件