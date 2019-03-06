from bs4 import BeautifulSoup
import requests
import re
import os 


path_root = 'mzitu'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.\
36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
def get_data():
    global path_root
    url = 'https://www.mzitu.com'
    html = requests.get(url, headers=header).content
    soup = BeautifulSoup(html, "html.parser")
    pages = soup.select('.widgets_top')[0]
    if not os.path.isdir(path_root):
        path_root = os.makedirs(path_root)
        
    for page in pages.children:
        if page != '\n' and page.name == 'a':
            dir_name = page.next_element['alt'].split()[0]
            
            pre_dir = os.path.join(path_root, dir_name)
            if not os.path.isdir(pre_dir):
                pre_dir = os.makedirs(pre_dir)    
            page_url = page['href']
            page_nums = get_pages(page_url)
            
            for page in range(int(page_nums)):
                page = page_url+'/'+str(page+1)
                img_url = get_img(page)
                img_name = img_url.split('/')[-1]
                image = os.path.join(pre_dir,img_name)
                
                req = requests.get(img_url)
                
                if req.status_code == 403:
                    
                    raise Exception('网站反爬虫策略生效！')
                
            
                with open(image,'wb') as f:
                    f.write(req.content)
                        
                

def get_pages(url):
    html = requests.get(url, headers=header).content
    soup = BeautifulSoup(html, "html.parser")
    pages = soup.select('.pagenavi')[0]
    
    return pages.contents[-3].string
    
def get_img(url):
    html = requests.get(url, headers=header).content
    soup = BeautifulSoup(html, "html.parser")
    img = soup.select('.main-image')[0]
    
    return img.a.next_element['src']

    
    
if __name__ == '__main__':
    get_data()
