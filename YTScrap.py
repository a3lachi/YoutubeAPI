
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import threading
import os 
from selenium.webdriver.common.by import By
import pandas as pd
import time 



global iki
iki = 0


def Bitina(driver) :
    time.sleep(2)
    try :
        for i in range(10) : 
            driver.find_element(By.XPATH,"/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button").click()
            time.sleep(0.4)
    except :
        pass


def Bitina2(driver) :
    time.sleep(2)
    try :
        for i in range(10) : 
            driver.find_element(By.XPATH,"/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button").click()
            time.sleep(0.4)
    except :
        pass


def GetTrendingVideos() :

    options = Options()
    options.add_argument('-headless')
    driver_trending = webdriver.Firefox(options=options)

    driver_trending.get('https://www.youtube.com/feed/trending')

    Bitina(driver_trending)

    videos = driver_trending.find_element(By.ID,"contents")

    vidz = videos.find_elements(By.XPATH,"//div[@id='contents']//div[@id='grid-container']//a[@id='video-title']")


    Data = []

    for video in vidz :
    	Data.append([video.get_attribute('title'),video.get_attribute('href'),''])



    df = pd.DataFrame(Data,columns=['Video','Link','Comments'])

    print('Successfully scraped trending videos links.')
    driver_trending.quit()

    return df

def Handle() :
    global Yt_data
    global iki 
    video = 'e'
    try :
        video = Yt_data.iloc[iki]['Link']
        if type(video)!=str :
            iki+=1
            Handle()
        iki+=1
    except :
        video = 'e'

    return video 


def ScrapComments() :
    global Yt_data
    global nmbScroll
    video = Handle()
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    print('HHHHHHH ',video)
    while (len(video)>2) :
        print('servii ',video)
        driver.get(video)

        Bitina(driver)
        Bitina2(driver)

        time.sleep(3)
        comz = []
        for j in range(nmbScroll) :
            driver.execute_script("window.scrollTo(0,1000000)")
            time.sleep(1)
        comments = driver.find_element(By.ID,"comments")
        coms = comments.find_elements(By.XPATH,"//div[@id='comment-content']//yt-formatted-string[@id='content-text']")
        for a in coms :
            comz.append(a.text)

        Yt_data.at[iki,'Comments']=comz
        print('Finished scrapping video : ',video)
        video = Handle()
        if (video!=video) :
            break 
    driver.quit()





def ThreadYoutube(NumbVidz,nbScroll) :
    threads = []
    global Yt_data 
    global nmbScroll
    nmbScroll=nbScroll
    try :
        Yt_data = GetTrendingVideos()
        Yt_data = Yt_data[:NumbVidz]
        for i in range(NumbVidz):
            t = threading.Thread(target=ScrapComments)
            threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        print('Comments scraped with success.')
    except Exception as e :
        print('An error occured launching th threads.')
        print('The error says : ',e)

    return Yt_data 



def ScrapUrl(url,nmbScroll) :
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    Bitina(driver)
    Bitina2(driver)

    time.sleep(3)
    comz = []
    for j in range(nmbScroll) :
        driver.execute_script("window.scrollTo(0,1000000)")
        time.sleep(1)
    comments = driver.find_element(By.ID,"comments")
    coms = comments.find_elements(By.XPATH,"//div[@id='comment-content']//yt-formatted-string[@id='content-text']")
    for a in coms :
        comz.append(a.text)

    Yt_data.at[iki,'Comments']=comz





Yt_data = ThreadYoutube(2,3)


print(Yt_data.head(5))












