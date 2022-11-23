#!/usr/bin/env python
# coding: utf-8

# In[2]:


# pip install selenium


# In[6]:


# pip install webdriver-manager


# In[15]:


#크롬 드라이버 자동 설치

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)


# In[24]:


#이미지 크롤링

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

elem = driver.find_element(By.CSS_SELECTOR, ".RNNXgb > div > div.a4bIc > input")
elem.send_keys("바다")
elem.send_keys(Keys.RETURN)


# In[32]:


import time
from selenium.webdriver.common.by import By

elem = driver.find_element(By.TAG_NAME, "body")
for i in range(70):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    
try:
    driver.find_element(By.CSS_SELECTOR, " div.qvfT1 > div.YstHxe > input").click()
    
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass


# In[39]:


links = []
images = driver.find_elements(By.CSS_SELECTOR, "#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img")

for image  in images:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))

print(' 찾은 이미지 개수: ', len(links))


# In[48]:


#크롤링한 이미지 다운로드 받기

import urllib.request

for k, i in enumerate(links):
    url = i
    urllib.request.urlretrieve(url, "C:\\파이썬과 40개의 작품들\\mycode\\19. 구글 이미지 크롤링\\사진다운로드\\"+str(k) + ".jpg")
    
print("다운로드 완료하였습니다.")

