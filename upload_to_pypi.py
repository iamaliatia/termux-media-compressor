import os
import requests

# معلومات الدخول والملف
url = "https://upload.pypi.org/legacy/"
username = "__token__"
# ⚠️ حط الـ Token ديالك الجديد كامل بين المعقوفتين هنا:
password = "pypi-AgEIcHlwaS5vcmc..." 

# تحديد ملف الـ wheel اللي تجمع عندك ف مجلد dist
dist_dir = "dist"
files_in_dist = os.listdir(dist_dir)
wheel_file = [f for f in files_in_dist if f.endswith('.whl')][0]
file_path = os.path.join(dist_dir, wheel_file)

print(f"جاري رفع الملف: {wheel_file} ...")

# قراءة الملف وإرساله بـ التشفير الصحيح
with open(file_path, 'rb') as f:
    files = {'content': (wheel_file, f, 'application/octet-stream')}
    # هنا كنشفروا البيانات بـ UTF-8 باش نتفاداو خطأ latin-1 د الشاشة
    response = requests.post(url, auth=(username, password), files=files)

if response.status_code == 200 or response.status_code == 201:
    print("🎉 مبروك! ترفعات المكتبة بنجاح تّام فـ PyPI!")
else:
    print(f"❌ وقع مشكل ف الرفع. كود الخطأ: {response.status_code}")
    print(response.text)
