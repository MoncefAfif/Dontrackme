import tkinter as tk
from tkinter import filedialog
from PIL import Image


def create_gui():
    root = tk.Tk()
    root.title("Select file")
    root.geometry("200x100")
    video_button = tk.Button(root, text="Select video", command=select_video)
    video_button.pack()
    image_button = tk.Button(root, text="Select image", command=select_image)
    image_button.pack()
    root.mainloop()


def select_video():
    file_paths = filedialog.askopenfilenames(filetypes=[("Video files", "*.mp4;*.avi;*.mkv;*.wmv")])
    if file_paths:
        for file_path in file_paths:
            remove_metadata_video(file_path)
    else:
        print("No files selected.")


def select_image():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.ico")])
    if file_paths:
        for file_path in file_paths:
            remove_metadata_image(file_path)
    else:
        print("No files selected.")


def remove_metadata_video(file_path):
    try:
        if file_path.endswith('.mp4'):
            from mutagen.mp4 import MP4
            video = MP4(file_path)
            video.delete()
            video.save()
        else:
            from mutagen.easyid3 import EasyID3
            video = EasyID3(file_path)
            video.delete()
            video.save()
        print('Metadata removed successfully')
    except Exception as e:
        print(f'An error occurred: {e}')


def remove_metadata_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.save(file_path, "jpeg", icc_profile=None)
        print('Metadata removed successfully')
    except Exception as e:
        print(f'An error occurred: {e}')


create_gui()
