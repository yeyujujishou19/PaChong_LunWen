#!/usr/bin/env Python
# coding=utf-8
import  os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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

#按关键词查找
def searchKey(subject):
    browser.get("http://www.cnki.net")
    browser.find_element_by_id('txt_SearchText').send_keys(subject)
    browser.find_element_by_class_name('search-btn').click()

#获取下载链接
def getDownloadLinks(browser, page_num):
    paper_downloadLinks = []
    for i in range(page_num):
        if i != 0:
            browser.find_element_by_link_text('下一页').click()
        for j, link in enumerate(browser.find_elements_by_css_selector('a[href^=\/kns\/detail]')):
            url = link.get_attribute('href')
            url_part = url.split('&')[3:6]
            url_str = '&'.join(url_part)
            down_url = 'http://kns.cnki.net/KCMS/detail/detail.aspx?' + url_str
            # print('page:'+str(i),'line:'+str(j),'url='+down_url)
            paper_downloadLinks.append(down_url)
    print('采集了%d条数据' % len(paper_downloadLinks))
    return paper_downloadLinks


subject = '深度学习'
page_num = 2
browser = browser_init(True) #初始化浏览器
searchKey(subject)  #按关键词搜索
#切换frame
browser.switch_to.frame('iframeResult')
paper_downloadLinks= getDownloadLinks(browser,page_num) #获取下载链接


#browser = browser_init(True)
login('ttod','ttod') #登录
for i,url in enumerate(paper_downloadLinks):
    print(url)
    browser.get(url)
    paper_title = browser.title
    print ('paper title:'+paper_title)
    if '中国专利全文数据库' in paper_title:
        continue
    print('try download:'+paper_title)
    try:
        browser.find_element_by_xpath("//a[contains(text(),'PDF下载')]").click()
        print('download pdf')
    except NoSuchElementException as e:
        try:
            browser.find_element_by_xpath("//a[contains(text(),'整本下载')]").click()
            print('download caj')
        except NoSuchElementException as e:
            print('download fail!')
    sleep(10)