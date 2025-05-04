import xml.etree.ElementTree as ET

def count_urls_from_sitemap(sitemap_path):
    """
    شمارش تعداد URLها در یک فایل sitemap.xml.

    Args:
        sitemap_path (str): مسیر فایل sitemap.xml.

    Returns:
        int: تعداد URLهای موجود در فایل sitemap.
    """
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        # namespace را برای فایل های سایت مپ در نظر بگیرید
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = root.findall('.//ns:loc', namespace)
        return len(urls)
    except FileNotFoundError:
        return "فایل یافت نشد."
    except ET.ParseError:
        return "خطا در تجزیه فایل XML."

# مسیر فایل sitemap.xml خود را جایگزین کنید
sitemap_file_path = 'sitemap.xml'  # یا مسیر کامل فایل را وارد کنید

url_count = count_urls_from_sitemap(sitemap_file_path)

if isinstance(url_count, int):
    print(f"تعداد URLهای موجود در فایل sitemap: {url_count}")
else:
    print(url_count)