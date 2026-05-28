import runpod
import os
import subprocess
import sys

# 🔗 رابط مجلد الـ Google Drive الخاص بمشروع مسبار
DRIVE_FOLDER_URL = "https://drive.google.com/drive/folders/1ElaPuurHazoxtAwNqO7WRK3m5CMt67xS?usp=drive_link"

def download_project_from_drive():
    print("[INFO] Starting download of the full project from Google Drive...")
    # تثبيت أداة gdown سحابياً داخل الحاوية لسحب المجلد من الدرايف
    subprocess.run([sys.executable, "-m", "pip", "install", "gdown"])
    
    try:
        # معرف المجلد المستخرج من الرابط الفعلي الخاص بكِ
        folder_id = "1ElaPuurHazoxtAwNqO7WRK3m5CMt67xS"
        # تحميل المجلد وتسميته بـ project داخل مسار /app في السيرفر
        subprocess.run(["gdown", "--folder", folder_id, "-O", "/app/project"])
        print("[INFO] Project downloaded successfully from Google Drive!")
    except Exception as e:
        print(f"[ERROR] Failed to download from Google Drive: {e}")

# أول ما يقلع السيرفر، يتأكد لو المجلد غير موجود يتوجه فوراً لتحميله
if not os.path.exists("/app/project"):
    download_project_from_drive()

# إضافة المجلد المسحوب لمسار نظام البايثون لتشغيل كود الـ handler الأصلي حقكِ
sys.path.append("/app/project")
from project.handler import handler as padel_handler

# إطلاق خدمة السيرفرليس لـ RunPod لتبدأ باستقبال طلبات دجانغو ومعالجة الفيديوهات
if __name__ == "__main__":
    runpod.serverless.start({"handler": padel_handler})