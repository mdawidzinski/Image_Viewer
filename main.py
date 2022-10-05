from tkinter import *
import tkinter.filedialog as tk_file
from PIL import Image, ImageTk  # pip install Pillow
from tkinter import messagebox  # to create messagebox
import os


root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
WIDTH = 650
HEIGHT = 550
x = screen_width/2 - WIDTH/2  # centered horizontally
y = screen_height - HEIGHT/0.8  # placed a bit bellow top of the screen
root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))
root.title('Image Viewer')
root.config(bg='#2192FF')
root.iconbitmap('image_photo_icon.ico')

images_list = []
images_was = []


def show_img():
    img = images_list[0]
    image_label = Label(image_frame, image=img)
    image_label.grid(row=0, column=0)


def open_folder():
    browse_txt.set('Loading...')
    images_list[:] = []  # clearing images list every time we open new directory
    folder = tk_file.askdirectory(title='Choose a folder')

    try:
        images_files = os.listdir(folder)
    except FileNotFoundError:
        browse_txt.set('BROWSE')
    else:
        for i in range(len(images_files)):
            if images_files[i].lower().endswith('.png') or images_files[i].lower().endswith('.jpg') \
                    or images_files[i].lower().endswith('.jpeg'):
                images_list.append([ImageTk.PhotoImage(Image.open(folder + '/' + images_files[i]).resize((551, 451)))])
        if images_list:
            show_img()
        else:
            messagebox.showinfo('Wrong Folder', 'Invalid (*.jpg, *.png, *.jpeg) files in folder.')

        browse_txt.set('BROWSE')


def next_img():
    if len(images_list) > 1:
        images_was.append(images_list[0])
        images_list.pop(0)

        show_img()


def prev_img():
    if len(images_was) > 0:
        images_list.insert(0, (images_was[-1]))
        images_was.pop()

        show_img()


image_frame = Frame(root, width=555, height=455, bg='#c8c8c8')
image_frame.grid(row=0, column=1)

back_btn = Button(root, text='Prev', bg='#9CFF2E', command=prev_img)
back_btn.grid(row=0, column=0, ipadx=5, ipady=5, padx=1)

next_btn = Button(root, text='Next', bg='#9CFF2E', command=next_img)
next_btn.grid(row=0, column=2, ipadx=5, ipady=5, padx=1)

browse_txt = StringVar()
browse_txt.set('BROWSE')
browse_btn = Button(root, textvariable=browse_txt, bg='#31E1F7', command=open_folder)
browse_btn.grid(row=1, column=1, ipadx=30, ipady=20)

exit_btn = Button(root, text='EXIT', command=root.quit, fg='red', activeforeground='red')
exit_btn.grid(row=2, column=1)


root.mainloop()
