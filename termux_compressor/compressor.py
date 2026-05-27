import os
import subprocess
from PIL import Image

def get_dir_size(path):
    """حساب الحجم الإجمالي للمجلد بالـ Megabytes"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size / (1024 * 1024)

def compress_image(input_path, output_path, quality=60):
    try:
        with Image.open(input_path) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.save(output_path, "JPEG", quality=quality)
            print(f"✅ Compressed Image: {os.path.basename(input_path)}")
    except Exception as e:
        print(f"❌ Error compressing image {input_path}: {e}")

def compress_video(input_path, output_path):
    try:
        cmd = [
            'ffmpeg', '-y', '-i', input_path,
            '-vcodec', 'libx264', '-crf', '28',
            '-acodec', 'aac', '-b:a', '128k',
            output_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(f"✅ Compressed Video: {os.path.basename(input_path)}")
    except Exception as e:
        print(f"❌ Error compressing video {input_path}: {e}")

def main():
    print("\n==========================================")
    print(" 🚀 Welcome to Termux Media Compressor 🚀 ")
    print("==========================================\n")
    
    folder_path = input("Enter the folder path (e.g., /sdcard/Download): ").strip()
    
    if not os.path.exists(folder_path):
        print("❌ Error: Path does not exist!")
        return

    output_folder = os.path.join(folder_path, "compressed_media")
    os.makedirs(output_folder, exist_ok=True)

    initial_size = get_dir_size(folder_path)

    for filename in os.listdir(folder_path):
        input_path = os.path.join(folder_path, filename)
        output_path = os.path.join(output_folder, filename)
        
        if os.path.isfile(input_path):
            ext = filename.lower().split('.')[-1]
            
            if ext in ['jpg', 'jpeg', 'png']:
                out_jpg = os.path.splitext(output_path)[0] + ".jpg"
                compress_image(input_path, out_jpg)
                
            elif ext in ['mp4', 'mkv', 'mov']:
                compress_video(input_path, output_path)

    final_size = get_dir_size(output_folder)
    saved_space = max(0, initial_size - final_size)

    print("\n==========================================")
    print("🎉 Compression Process Finished Successfully!")
    print(f"📂 Output Location: {output_folder}")
    print(f"📊 Initial Size: {initial_size:.2f} MB")
    print(f"📊 Compressed Size: {final_size:.2f} MB")
    print(f"💡 You Saved: {saved_space:.2f} MB of space!")
    print("==========================================\n")

if __name__ == "__main__":
    main()
