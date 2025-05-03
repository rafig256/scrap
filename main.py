import requests
from bs4 import BeautifulSoup

url = 'https://www.heyvagroup.com/shownews/7790/%DA%A9%D9%86%DA%A9%D9%88%D8%B1.html'

r = requests.get(url)

soup = BeautifulSoup(r.content , 'html.parser')

ps = soup.find_all('p')

count = 0  # تعریف یک متغیر شمارنده با مقدار اولیه صفر

for p in ps:
    text = p.text.strip()  # حذف space ها، newline ها و tab ها از ابتدا و انتهای متن
    if text:  # اگر متن بعد از حذف فضاهای خالی، چیزی داشت چاپ کن
        count +=1
        print(str(count) + ": " + text)  # تبدیل عدد به رشته با str()
