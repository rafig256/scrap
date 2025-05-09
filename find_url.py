import os
import xml.etree.ElementTree as ET
import pandas as pd

def filter_urls(urls):
    filter_key = ['استخدام','نتایج','کارنامه','پذیرش','مصاحبه','آزمون']
    filtered_urls = []
    normal_urls = []

    for url in urls:
        if any(keyword in url for keyword in filter_key):
            filtered_urls.append(url)
        else:
            normal_urls.append(url)

    return normal_urls, filtered_urls

def find_urls_from_sitemap(sitemap_path):
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        loc_elements = root.findall('.//ns:loc', namespace)
        urls = [elem.text for elem in loc_elements]
        return urls
    except FileNotFoundError:
        return "فایل یافت نشد."
    except ET.ParseError:
        return "خطا در تجزیه فایل XML."

# مسیر فایل ورودی sitemap
sitemap_file_path = 'sitemap.xml'

# مسیر خروجی فایل‌ها
output_dir = 'resource'
output_excel_path_normal = os.path.join(output_dir, 'sitemap_links.xlsx')
output_excel_path_filtered = os.path.join(output_dir, 'filtered_links.xlsx')

# اطمینان از وجود پوشه خروجی
os.makedirs(output_dir, exist_ok=True)

# استخراج لینک‌ها
urls = find_urls_from_sitemap(sitemap_file_path)

# اعمال فیلترهای دلخواه
if isinstance(urls, list):
    urls, filtered_urls = filter_urls(urls)

    # ذخیره لینک‌های معمولی
    df_normal = pd.DataFrame(urls, columns=["URL"])
    df_normal.to_excel(output_excel_path_normal, index=False)

    # ذخیره لینک‌های فیلترشده
    df_filtered = pd.DataFrame(filtered_urls, columns=["Filtered URL"])
    df_filtered.to_excel(output_excel_path_filtered, index=False)

    print(f"{len(urls)} لینک معمولی در '{output_excel_path_normal}' ذخیره شد.")
    print(f"{len(filtered_urls)} لینک فیلترشده در '{output_excel_path_filtered}' ذخیره شد.")
else:
    print(urls)  # چاپ پیام خطا
