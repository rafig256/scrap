import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = 'https://www.heyvagroup.com/shownews/9971/%D8%AA%D9%85%D8%AF%DB%8C%D8%AF-%D9%88-%D8%AA%D8%B9%D9%88%DB%8C%D8%B6-%DA%A9%D8%A7%D8%B1%D8%AA-%D9%85%D9%87%D8%A7%D8%B1%D8%AA-%D9%81%D9%86%DB%8C-%D8%AD%D8%B1%D9%81%D9%87-%D8%A7%DB%8C.html'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
ps = soup.find_all('p')

count = 0
data_p_tag = []
min_word_count = 15

for p in ps:
    text = p.text.strip()
    words = text.split()  # جدا کردن متن به کلمات
    if len(words) >= min_word_count:
        count += 1
        data_p_tag.append(text)
        print(str(count) + ": " + text)

print(f"تعداد پاراگراف‌های واجد شرایط: {count}")

# ایجاد پوشه result اگر وجود ندارد
output_directory = 'result'
os.makedirs(output_directory, exist_ok=True)
output_file = os.path.join(output_directory, 'data.xlsx')

# ذخیره داده‌ها در فایل Excel
df = pd.DataFrame({'متن پاراگراف': data_p_tag})
df.to_excel(output_file, index=False)  # حذف آرگومان encoding

print(f"محتوای پاراگراف‌های واجد شرایط در فایل '{output_file}' ذخیره شد.")