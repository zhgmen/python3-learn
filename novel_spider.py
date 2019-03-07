import urllib.request
from bs4 import BeautifulSoup
import os


url = 'https://www.kanunu8.com/book3/8196/'
path = '白鹿原/'

def parse_page(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    for i in soup.select('tbody > tr > td > a'):
        print(i)
        if 'files' in i['href']:
            continue
        if not os.path.exists(path):
            os.makedirs(path)
        data_file = os.path.join(path, i.string+'.txt')
        print(data_file)
      
        print(url + i['href'])
        text = parse_content(url + i['href'])
        save_file(data_file, text)
    
def parse_content(url):
    html = get_html(url)
    
    soup = BeautifulSoup(html, 'html.parser')
    return str(soup.select('td > p')[0])

    
def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    html = response.read().decode('gbk')
    
    return html

def save_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)
                    

if __name__ == '__main__':
    parse_page(url)    
