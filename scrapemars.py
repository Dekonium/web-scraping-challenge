from bs4 import BeautifulSoup as bs
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

def scrape():

    title = []
    article_text = []

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://redplanetscience.com/')
    html = driver.page_source
    soup = bs(html)

    for tag in soup.find('div',class_='content_title'):    
        title.append(tag)

    for x in soup.find('div',class_='article_teaser_body'):
        article_text.append(x)


    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://spaceimages-mars.com/')
    html2 = driver.page_source

    soup = bs(html2)

    featured_image_url = []
    for j in soup.find('a',class_='showimg fancybox-thumbs')['href']:
        
        featured_image_url.append(j)
    


    for x in range(len(featured_image_url)):
        featured_image_url_cleaned = ''.join([str(n) for n in featured_image_url])


    featured_image_url_final = f'https://spaceimages-mars.com/{featured_image_url_cleaned}'

    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    df = tables[1]
    df1 = df.transpose()
    qwe = df1.to_html('table.html')
    asd= df1.to_json()

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://marshemispheres.com/')
    html3 = driver.page_source

    soup = bs(html3)

    hemisphere_image_urls = []
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By

    driver.find_element(By.XPATH, '//*[@id="product-section"]/div[2]/div[1]/div/a').click()
    driver.find_element(By.XPATH, '//*[@id="wide-image-toggle"]').click()
    cerberus_url = driver.find_element(By.XPATH, '//*[@id="wide-image"]/img')
    cerberus_url= cerberus_url.get_attribute('src')

    Cerberus_image_dict={'title':"Cerberus Hemisphere",'img_url':cerberus_url}

    driver.back()
    driver.find_element(By.XPATH, '//*[@id="product-section"]/div[2]/div[2]/div/a').click()
    driver.find_element(By.XPATH, '//*[@id="wide-image-toggle"]').click()
    Schiaparelli_Hemisphere_url = driver.find_element(By.XPATH, '//*[@id="wide-image"]/img')
    Schiaparelli_Hemisphere_url= Schiaparelli_Hemisphere_url.get_attribute('src')

    Schiaparelli_image_dict={'title':"Schiaparelli Hemisphere",'img_url':Schiaparelli_Hemisphere_url}
    driver.back()
    driver.find_element(By.XPATH, '//*[@id="product-section"]/div[2]/div[3]/div/a').click()
    driver.find_element(By.XPATH, '//*[@id="wide-image-toggle"]').click()
    Syrtis_Major_Hemisphere_url = driver.find_element(By.XPATH, '//*[@id="wide-image"]/img')
    Syrtis_Major_Hemisphere_url= Syrtis_Major_Hemisphere_url.get_attribute('src')

    Syrtis_image_dict={'title':"Syrtis Major Hemisphere",'img_url':Syrtis_Major_Hemisphere_url}
    driver.back()
    driver.find_element(By.XPATH, '//*[@id="product-section"]/div[2]/div[4]/div/a').click()
    driver.find_element(By.XPATH, '//*[@id="wide-image-toggle"]').click()
    Valles_Marineris_Hemisphere_url = driver.find_element(By.XPATH, '//*[@id="wide-image"]/img')
    Valles_Marineris_Hemisphere_url= Valles_Marineris_Hemisphere_url.get_attribute('src')

    Valles_image_dict={'title':"Valles Marineris Hemisphere",'img_url':Valles_Marineris_Hemisphere_url}
    hemisphere_image_urls=[Cerberus_image_dict,Schiaparelli_image_dict,Syrtis_image_dict,Valles_image_dict]

    scraped = {'Latest_Mars_News':[title,article_text],'Featured_Mars_Image':featured_image_url_final,'Mars_Facts':asd,'Mars_Hemispheres':hemisphere_image_urls}
    return scraped
    #'Mars Facts':df1