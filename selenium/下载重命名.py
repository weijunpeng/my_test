import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import re

url = 'https://appgsoghlmo7596.pc.xiaoe-tech.com/p/t_pc/course_pc_detail/video/v_620df160e4b02b82584b9abf?product_id=term_6209ca3cafb84_bh99T4&type=6'
# headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"}

# resp = requests.get(url, headers=headers)
# soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

# #aa = soup.select('#xe-video > xe-fullscreendialog:nth-child(21) > div > div > div') #select('.article p')
# # bb=soup.find_all('div')
# # print(bb)

# #print(soup.prettify()) #prettify()用于格式化输出html/xml文档




option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
#以下三个设置作用：加载插件，但只能用打开一个浏览器，会调用cookie
# option.add_argument(r'user-data-dir=C:\Users\v_weijpeng.TENCENT\AppData\Local\Google\Chrome\User Data')  # C:\Users\v_weijpeng.TENCENT\AppData\Local\Google\Chrome\User Data\Default
# option.add_argument("--no-sandbox") 
# option.add_argument('--disable-dev-shm-usage')
# option.add_argument("--remote-debugging-port=9292")
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(20)  # 隐式等待 程序表现：每当driver执行动作时，暂停程序直到满足driver执行条件；若暂停时间超出设置的时间n秒，则触发异常

# 登录
driver.get(url='https://appgsoghlmo7596.pc.xiaoe-tech.com/login')
driver.find_element(By.CSS_SELECTOR,"#__layout > div > div > div > div > div > div.login-xiaoe-tabs > div.login-phone.gary > p").click()
driver.find_element(By.CSS_SELECTOR,"#__layout > div > div > div > div > div > div.login-xiaoe-phoneList > div.login-xiaoe-imgCode.input-margin > div > input").send_keys('18022311110092')
driver.find_element(By.CSS_SELECTOR,"#__layout > div > div > div > div > div > div.login-xiaoe-phoneList > div.login-xiaoe-enterCode.input-margin > div > input").send_keys('123456')
driver.find_element(By.XPATH,'//span[@class="ss-checkbox__input"]').click() 
driver.find_element(By.XPATH,'//button[text()="登录"]').click()

time.sleep(2)
driver.execute_script("window.scrollTo(0,1000)")
driver.find_element(By.XPATH,'//img[@src="https://wechatapppro-1252524126.cdn.xiaoeknow.com/appgsoghlmo7596/image/b_u_6209c60d2d1f8_p0FH2xZ0/l061xcsn00j5.jpg?imageMogr2/quality/80|imageMogr2/ignore-error/1"]').click() #成为一名合格律师


time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
print('当前页面：'+driver.title)

# 展开
elements_list = driver.find_elements(By.XPATH,'//i[@class="el-collapse-item__arrow el-icon-arrow-right"]')
print("找到需要展开元素数："+str(len(elements_list)))
i=0
for elements in elements_list :
    # if elements == elements_list[0] :
    #     continue
    # else :
        elements.click()
        i=i+1
        print('点击展开第{}次'.format(i))
        time.sleep(0.2)

#下载
time.sleep(5)
elements_list = driver.find_elements(By.CSS_SELECTOR,'div[data-v-56251fc4][data-v-1fbe4446]')
time.sleep(1)
print('找到需要下载元素数：'+str(len(elements_list)))
j=1
for elements in elements_list :
    elements.click()
    #切换到视频播放页
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[2])
    url_head='https://blog.luckly-mjw.cn/tool-show/m3u8-downloader/index.html?source='
    url_last = driver.find_element(By.XPATH,'//li[contains(@url,"m3u8")]').get_attribute('url')
    url=url_head+url_last

    title_name= driver.find_element(By.CSS_SELECTOR,'div[class="video-title"]>div>div').text

    #进入下载页
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH,'//div[text()="转码为MP4下载"]').click()

    try:
        element = WebDriverWait(driver, 60).until( EC.presence_of_element_located((By.XPATH, '//div[text()="下载完成"]')) )
        if element.text == '下载完成' :
            print('下载完成第{}个文件'.format(j))
            driver.close()
    except:
        # 如果找不到元素，则退出页面
        driver.close()
        print('下载失败-------------')
    time.sleep(10)
    path = r"C:\Users\v_weijpeng.TENCENT\Downloads\成为一名合格律师"
    if not os.path.exists(path):
        os.mkdir(path)

    ls_file=os.listdir(r'C:\Users\v_weijpeng.TENCENT\Downloads')
    listdir = [file for file in ls_file if re.match('\d{4}_\d{2}_\d{2} \d{2}_\d{2}.*',file)]
    listdir.sort()
    os.rename((r'C:\Users\v_weijpeng.TENCENT\Downloads'+'\\'+listdir[-1]), path+'\\'+listdir[-1]) #移动
    os.rename((path+'\\'+listdir[-1]), path+'\\'+title_name+'.mp4') #重命名

    driver.switch_to.window(driver.window_handles[1])
    j=j+1
    time.sleep(1)

