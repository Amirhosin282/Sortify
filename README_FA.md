# Sortify 📂

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Sortify یک ابزار سبک و ساده بر پایه پایتون است که فایل‌های یک پوشه را بر اساس نوع آن‌ها به‌صورت خودکار مرتب می‌کند.

این برنامه پوشه موردنظر را بررسی کرده و فایل‌های اسناد، تصاویر، صوتی، ویدئویی و سایر فایل‌ها را در پوشه‌های جداگانه قرار می‌دهد تا نظم بیشتری به فایل‌های شما بدهد.

> ساده، سریع و مناسب برای استفاده روزمره.

---

## 🚀 ویژگی‌ها

* مرتب‌سازی خودکار فایل‌ها بر اساس پسوند
* ساخت خودکار پوشه‌های موردنیاز
* پشتیبانی از فایل‌های متنی، تصویری، صوتی و ویدئویی
* پشتیبانی از پسوندهای بزرگ و کوچک (مانند JPG و jpg)
* قابل اجرا در ویندوز، لینوکس و مک
* سبک و بدون وابستگی‌های اضافی

---

## 📦 دسته‌بندی فایل‌ها

| پوشه      | پسوندهای پشتیبانی‌شده                               |
| --------- | --------------------------------------------------- |
| Documents | pdf, doc, docx, txt, odt, rtf, ppt, pptx, xls, xlsx |
| Audio     | mp3, wav, flac, ogg, m4a                            |
| Videos    | mp4, mkv, avi, mov, wmv, webm, flv                  |
| Pictures  | jpg, jpeg, png, gif, bmp, webp, svg, tiff           |
| Other     | سایر فایل‌ها                                        |

---

## 📁 نمونه عملکرد

قبل از اجرا:

```text
Downloads/
├── Report.pdf
├── Song.mp3
├── Photo.JPG
├── Movie.mkv
└── Unknown.xyz
```

بعد از اجرا:

```text
Downloads/
├── Documents/
│   └── Report.pdf
├── Audio/
│   └── Song.mp3
├── Pictures/
│   └── Photo.JPG
├── Videos/
│   └── Movie.mkv
└── Other/
    └── Unknown.xyz
```

---

## 🛠 نحوه استفاده

ابتدا مخزن را دریافت کنید:

```bash
git clone https://github.com/amirhosin282/sortify.git
```

سپس برنامه را اجرا کنید:

```bash
python main.py
```

در ادامه مسیر پوشه موردنظر را وارد کنید تا Sortify فایل‌ها را به‌صورت خودکار مرتب کند.

---

## ⚠️ نکات

* اگر پوشه‌های مقصد از قبل وجود داشته باشند، مجدداً ساخته نخواهند شد.
* فایل‌ها جابه‌جا می‌شوند و کپی نمی‌شوند.
* برای اجرای صحیح برنامه باید دسترسی لازم به پوشه هدف را داشته باشید.
* فایل‌هایی که نوع آن‌ها شناسایی نشود به پوشه `Other` منتقل خواهند شد.


![Footer](https://capsule-render.vercel.app/api?type=waving\&color=gradient\&height=80\&section=footer)
