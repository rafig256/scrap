# Scrapy Project for Heyva Educational Consulting Data

This project utilizes the Scrapy framework in Python to scrape educational consulting information from the Heyva website (https://www.heyvagroup.com/). The collected data will be used for preparing a dataset to train an artificial intelligence model.

## Table of Contents
- [Persian](#پروژه-اسکرپ-داده‌های-مشاوره-تحصیلی-هیوا)
- [English](#scrapy-project-for-heyva-educational-consulting-data)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## پروژه اسکرپ داده‌های مشاوره تحصیلی هیوا

این پروژه از فریمورک Scrapy در پایتون برای جمع‌آوری اطلاعات مشاوره تحصیلی از وب‌سایت هیوا (https://www.heyvagroup.com/) استفاده می‌کند. داده‌های جمع‌آوری شده برای آماده‌سازی یک مجموعه داده جهت آموزش یک مدل هوش مصنوعی به کار خواهند رفت.

### فهرست مطالب
- [پروژه اسکرپ داده‌های مشاوره تحصیلی هیوا](#پروژه-اسکرپ-داده‌های-مشاوره-تحصیلی-هیوا)
- [Scrapy Project for Heyva Educational Consulting Data](#scrapy-project-for-heyva-educational-consulting-data)
- [نصب](#نصب)
- [نحوه استفاده](#نحوه-استفاده)
- [ساختار پروژه](#ساختار-پروژه)
- [مشارکت](#مشارکت)
- [مجوز](#مجوز)

---

## Installation

To run this Scrapy project, you need to have Python and pip installed on your system. Follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd [YOUR_REPOSITORY_NAME]
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS and Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You might need to create a `requirements.txt` file listing your project dependencies, including `scrapy`)*

## نصب

برای اجرای این پروژه Scrapy، باید پایتون و pip روی سیستم شما نصب باشند. مراحل زیر را دنبال کنید:

1.  **کلون کردن ریپازیتوری:**
    ```bash
    git clone [آدرس_ریپازیتوری_شما]
    cd [نام_ریپازیتوری_شما]
    ```

2.  **ایجاد یک محیط مجازی (توصیه می‌شود):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # در macOS و Linux
    venv\Scripts\activate  # در Windows
    ```

3.  **نصب وابستگی‌های مورد نیاز:**
    ```bash
    pip install -r requirements.txt
    ```
    *(توجه: ممکن است لازم باشد یک فایل `requirements.txt` ایجاد کنید که شامل وابستگی‌های پروژه شما از جمله `scrapy` باشد)*

---

## Usage

To run the spider and scrape the data, navigate to the project's root directory in your terminal and execute the following command:

```bash
scrapy crawl heyva_spider -o output.json