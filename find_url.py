import xml.etree.ElementTree as ET
import pandas as pd 

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

# مسیر خروجی فایل Excel
output_excel_path = 'result/sitemap_links.xlsx'

# استخراج لینک‌ها
urls = find_urls_from_sitemap(sitemap_file_path)

# اگر لیستی از لینک‌ها بود، ذخیره در Excel
if isinstance(urls, list):
    df = pd.DataFrame(urls, columns=["URL"])
    df.to_excel(output_excel_path, index=False)
    print(f"{len(urls)} لینک در فایل '{output_excel_path}' ذخیره شد.")
else:
    print(urls)  # چاپ پیام خطا در صورت نیاز
