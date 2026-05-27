# Termux Media Compressor 🚀

A lightweight, powerful, and completely offline Python CLI tool designed specifically for Termux on Android. It allows you to batch-compress images and videos locally on your phone to free up storage space without sacrificing privacy or relying on slow internet uploads.

## ✨ Features
- **Local & Offline:** No internet required. Your media files never leave your device.
- **Smart Image Compression:** Uses `Pillow` to optimize and compress JPEG/PNG images efficiently.
- **Advanced Video Compression:** Uses `FFmpeg` with the H.264 (`libx264`) codec to dramatically reduce video file sizes while keeping acceptable quality.
- **Space Saving Statistics:** Dynamically calculates total folder size before and after compression to show exactly how many Megabytes (MB) you saved.
- **Safe Execution:** Saves all compressed files into a separated `compressed_media` folder without touching or risking your original files.

---

## 🛠️ Prerequisites & Pre-installation

Before installing the library, you need to set up the required packages inside your Termux terminal.

### 1. Update Termux Packages
```bash
pkg update && pkg upgrade -y
