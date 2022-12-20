import customtkinter
import subprocess
from customtkinter import filedialog
import requests as reqs
import json
import os

app = customtkinter.CTk()
app.geometry("500x250")
app.title("By Clumsy#2304")
app.resizable(False,False)


global filename, msg, ram
filename = ''
msg = "Select a file path"
ram = 6


def audio_fix():
    req = reqs.get(url='https://lopsidedheavyvirus.steamtest083.repl.co/risetexture.zip')
    print("Susccess")
    with open("LauncherFiles\\resourcepacks\\risetexture.zip", 'wb') as f:
        f.write(req.content)


os.makedirs("LauncherFiles", exist_ok=True)

if os.path.isfile('LauncherFiles\cum.json'):
    with open('LauncherFiles\cum.json', 'r') as cum:
        cum = json.load(cum)
        filename = cum['file_path']
        ram = cum['ram']
else:
    with open('LauncherFiles\cum.json', 'w') as cum:
        json.dump({"ram": "6", "file_path": ""}, cum)

def browseFiles():
    global filename
    filename = filedialog.askdirectory()
    with open('LauncherFiles\cum.json', 'w') as cum:
        json.dump({"ram": ram, "file_path": filename}, cum)

def launch_Rise():
    global filename, msg
    ram = str(int(slider.get()))
    with open('LauncherFiles\cum.json', 'w') as cum:
        json.dump({"ram": ram, "file_path": filename}, cum)
    if not filename:
        msg = "Select a file path"
        create_toplevel()
    elif not os.path.isfile(f'{filename}\\files\\azul-1.8.9_345\\bin\\java.exe'):
        msg = "JDK was not found in the supplied file path"
        create_toplevel()
    else:
        command = fr'{filename}\files\azul-1.8.9_345\bin\java.exe -noverify -Xms512m -Xmx{ram}g -Djava.library.path={filename}\files\1.8.9-natives-win -cp "{filename}\files\RiseCompressed.jar;lwjgl.jar;lwjgl_util.jar" net.minecraft.client.main.Main -uuid fc5bc365-aedf-30a8-8b89-04e462e29bde -accessToken yes -version 1'
        subprocess.Popen(command, shell=True, cwd="LauncherFiles", stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#Popup Shit

def create_toplevel(app=app):
    global msg
    window = customtkinter.CTkToplevel(app)
    window.geometry("425x150")
    window.title("By Clumsy#2304")
    window.resizable(False,False)

    label = customtkinter.CTkLabel(master=window, text=msg)
    label.pack(side="top", fill="both", expand=True, padx=40, pady=40)


#Launch Shit
button = customtkinter.CTkButton(master=app, text="Launch",font=("product_sans", 20), command=launch_Rise)
button.place(relx=0.2, rely=0.8, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="File Path",font=("product_sans", 20), command=browseFiles)
button.place(relx=0.8, rely=0.8, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Audio Fix",font=("product_sans", 20), command=audio_fix)
button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

label = customtkinter.CTkLabel(master=app, text="Rise 6 launcher", font=("product_sans", 20))
label.place(relx=0.5, rely=0.10,  anchor=customtkinter.CENTER)

#Ram Shit
label = customtkinter.CTkLabel(master=app, text="Ram Allocation", font=("product_sans", 16))
label.place(relx=0.5, rely=0.4,  anchor=customtkinter.CENTER)

label = customtkinter.CTkLabel(master=app, text="2gb", font=("product_sans", 16))
label.place(relx=0.27, rely=0.5,  anchor=customtkinter.CENTER)

label = customtkinter.CTkLabel(master=app, text="6g", font=("product_sans", 16))
label.place(relx=0.50, rely=0.6,  anchor=customtkinter.CENTER)

label = customtkinter.CTkLabel(master=app, text="10gb", font=("product_sans", 16))
label.place(relx=0.74, rely=0.5,  anchor=customtkinter.CENTER)

slider = customtkinter.CTkSlider(master=app, from_=2, to=10, number_of_steps=4,)
slider.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
slider.set(int(ram))

app.mainloop()