import tkinter as tk
from tkinter import Label
from tkinter import filedialog , messagebox
from PIL import Image, ImageTk
from pyexpat.errors import messages


def imageUploader():
    global img
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes=fileTypes)

    # if file is selected
    if len(path):
        app.geometry("1000x1000")
        # img = Image.open(path)
        img = ImageTk.PhotoImage(file=path)
        # picLable= Label(app, image=pic)
        buttonImage = tk.Button(app, image=img)
        buttonImage.grid(row=2, columnspan=3)

    else:
        print("No file is chosen. Please select a file.")

def addWatermark():
    global img
    global nameTag
    print("add watermark to img and name tag is " , nameTag.get())
    #create a label with text over the image
    centerLabel = tk.Label(app , text=nameTag.get() , image=img, compound='center',fg="grey",font=("Arial", 14 , "bold"))
    centerLabel.grid(row=4 ,columnspan=4)
    saveEditedIamge.config(state=tk.NORMAL)

def saveEditedImage():
    global img
    print("save edited watermarked image")
    if img :
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG file", ".png"), ("JPEG file" , "*jpg")],
            initialfile="edited_image.png"
        )
        if save_path:
            try:
                img.save(save_path)
                messagebox.showinfo("success" ,f"Image saved successfully to {save_path}" )
            except Exception as e:
                messagebox.showerror("error" ,  f"An error occurred while saving: {e}")
    else:
        messagebox.showwarning("Warning", "No image is currently loaded or edited.")



if __name__ == "__main__":

    app = tk.Tk()
    scrollbar = tk.Scrollbar(app , orient=tk.VERTICAL)

    #set title of program and size
    app.title("Add Watermark")
    app.geometry("296x200")

    #declaring string variable
    #watermark string check
    nameTag = tk.StringVar()

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
    addWatermarkButton = tk.Button(app , text= "add watermark", command=addWatermark)

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

