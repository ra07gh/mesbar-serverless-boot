# 1. استخدام نسخة بايثون رسمية وخفيفة ومستقرة
FROM python:3.10-slim

# 2. تثبيت حزم النظام الأساسية لتشغيل مكتبات الرؤية الحاسوبية والفيديو (OpenCV)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    git \
    && rm -rf /var/lib/apt/lists/*

# 3. تحديد مجلد العمل السحابي داخل الحاوية
WORKDIR /app

# 4. تثبيت مكتبة رون بود الأساسية أولاً لتهيئة السيرفرليس
RUN pip install --no-cache-dir runpod

# 5. نسخ ملف البوت الخفيف إلى داخل السيرفر
COPY boot.py .

# 6. الأمر البرمجي الذي يفرضه رون بود لتشغيل ملف التوجيه فور استيقاظ السيرفر
CMD [ "python", "-u", "boot.py" ]