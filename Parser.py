from bs4 import BeautifulSoup
import requests

def parse():
    url = 'https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php'
    try:
        page = requests.get(url)
        print(page.status_code)
        soup = BeautifulSoup(page.text, 'html.parser')
    except:
        print('Error')
        return -1

    block = soup.findAll('div', id='pagecontent')
    description = ''
    for data in block:
        if data.find('a'):
            description = str(data.text).split('\n\n\n')#разделение строки по трём переносам
    f = open('text.txt', 'w')
    for data in description:
        f.write(data.strip() + '\n')#удаление лишних пробелов + перенос строки
    f.close()