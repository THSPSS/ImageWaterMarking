import tkinter as tk
from tkinter import Label
from tkinter import filedialog , messagebox
from PIL import Image, ImageTk , ImageDraw
from PIL.ImageFont import ImageFont
from pyexpat.errors import messages


def imageUploader():
    global img
    global shown_img
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)

    # if file is selected
    if len(path):
        app.geometry("1000x1000")
        img = Image.open(path)
        # img.grid(row=2, columnspan=3)
        shown_img = ImageTk.PhotoImage(file=path)
        # picLable= Label(app, image=pic)
        buttonImage = tk.Button(app, image=shown_img)
        buttonImage.grid(row=2, columnspan=3)

    else:
        print("No file is chosen. Please select a file.")

def addWatermark():
    global img
    global nameTag
    #create a label with text over the image
    draw = ImageDraw.Draw(img)
    position = (10, 10)  # (x, y) coordinates
    draw.text(position, nameTag.get(), fill=(255, 255, 255))  # White color
    saveEditedIamge.config(state=tk.NORMAL)

def saveEditedImage():
    # global copied_img
    # copied_img.save("watermarked_image.png")
    if img :
        img.save("watermarked_image.png")
        messagebox.showinfo("success", f"Image saved successfully")
    else:
        messagebox.showwarning("Warning", "No image is currently loaded or edited.")

def checkInput(*args):
    if nameTag.get().strip():
        addWatermarkButton.config(state=tk.NORMAL)
    else:
        addWatermarkButton(state=tk.DISABLED)


if __name__ == "__main__":

    app = tk.Tk()
    scrollbar = tk.Scrollbar(app , orient=tk.VERTICAL)

    #set title of program and size
    app.title("Add Watermark")
    app.geometry("296x200")

    #declaring string variable
    #watermark string check
    nameTag = tk.StringVar()
    nameTag.trace_add("write", checkInput)

    #creating a label for
    #nameTapg using widget Label
    nameTagLabel = tk.Label(app , text= "Name Tag", font=('calibre',10,'bold'))

    # creating a entry for input
    # name using widget Entry
    nameTagEntry = tk.Entry(app , textvariable=nameTag , font=('calibre', 10 , 'normal' ))

    # after nametag for watermark than showing upload image button
    uploadButton = tk.Button(app , text = "upload image", command=imageUploader)

    # showing image placeholder
    img = Image.open('placeholder.png')
    img = img.resize((300,100))
    tkImg = ImageTk.PhotoImage(img)
    imgLabel = Label(app, image=tkImg)

    # creating button to add name tag text on top of image
    addWatermarkButton = tk.Button(app , text= "add watermark", command=addWatermark , state=tk.DISABLED)

    #creating button to save edited,which name tag is added,
    saveEditedIamge = tk.Button(app , text = " save edited image" , command =saveEditedImage , state=tk.DISABLED)

    # placing label and entry in the required position using grid method
    uploadButton.grid(row=0, columnspan=4)
    nameTagLabel.grid(row=1, column=1)
    nameTagEntry.grid(row=1, column=2)
    imgLabel.grid(row=2,columnspan=4)
    addWatermarkButton.grid(row=3, column=1)
    saveEditedIamge.grid(row=3 , column=2)




    app.mainloop()

