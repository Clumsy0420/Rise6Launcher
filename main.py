from customtkinter import filedialog
import requests as reqs
import customtkinter
import subprocess
import json
import os

app = customtkinter.CTk()
app.geometry("500x250")
app.title("By Clumsy#2304")
app.resizable(False, False)

filename = ""
ram = 6


os.makedirs("LauncherFiles", exist_ok=True)
if os.path.isfile("LauncherFiles\cum.json"):
    with open("LauncherFiles\cum.json", "r") as cum:
        cum = json.load(cum)
        filename = cum["file_path"]
        ram = cum["ram"]
else:
    with open("LauncherFiles\cum.json", "w") as cum:
        json.dump({"ram": "6", "file_path": ""}, cum)


def browseFiles():
    global filename
    filename = filedialog.askdirectory()
    with open("LauncherFiles\cum.json", "w") as cum:
        json.dump({"ram": ram, "file_path": filename}, cum)


def launchRise():
    global filename
    ram = str(int(ram_slider.get()))
    with open("LauncherFiles\cum.json", "w") as cum:
        json.dump({"ram": ram, "file_path": filename}, cum)
    if not filename:
        createTopLevel(app, "Select a file path")
    elif not os.path.isfile(f"{filename}\\files\\azul-1.8.9_345\\bin\\java.exe"):
        createTopLevel(app, "JDK was not found in the supplied file path")
    else:
        command = fr'{filename}\files\azul-1.8.9_345\bin\java.exe -noverify -Xms512m -Xmx{ram}g -Djava.library.path={filename}\files\1.8.9-natives-win -cp "{filename}\files\RiseCompressed.jar;lwjgl.jar;lwjgl_util.jar" net.minecraft.client.main.Main -uuid fc5bc365-aedf-30a8-8b89-04e462e29bde -accessToken yes -version 1'
        subprocess.Popen(command, shell=True, cwd="LauncherFiles", stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def audio_fix():
    try:
        file_path = "LauncherFiles\\resourcepacks\\risetexture.zip"
        url = "https://lopsidedheavyvirus.steamtest083.repl.co/risetexture.zip"
        command = f"curl -o {file_path} {url}"
        subprocess.run(command, shell=True)
    except:
        createTopLevel(app, "Resource Pack Folder Not Found Please Launch Rise")


def createTopLevel(app, msg):
    window = customtkinter.CTkToplevel(app)
    window.title(msg)
    window.geometry("425x150")
    window.resizable(False, False)

    label = customtkinter.CTkLabel(master=window, text=msg)
    label.pack(side="top", fill="both", expand=True, padx=40, pady=40)


bigFont = ("product_sans", 20)
smallFont = ("product_sans", 16)

# Launch Shit
launch_btn = customtkinter.CTkButton(master=app, text="Launch", font=bigFont, command=launchRise)
launch_btn.place(relx=0.2, rely=0.8, anchor=customtkinter.CENTER)

path_btn = customtkinter.CTkButton(master=app, text="File Path", font=bigFont, command=browseFiles)
path_btn.place(relx=0.8, rely=0.8, anchor=customtkinter.CENTER)

fix_btn = customtkinter.CTkButton(master=app, text="Audio Fix", font=bigFont, command=audio_fix)
fix_btn.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

title_lbl = customtkinter.CTkLabel(master=app, text="Rise 6 launcher", font=bigFont)
title_lbl.place(relx=0.5, rely=0.10, anchor=customtkinter.CENTER)

# Ram Shit
ram_lbl = customtkinter.CTkLabel(master=app, text="Ram Allocation", font=smallFont)
ram_lbl.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

ram_lbl_min = customtkinter.CTkLabel(master=app, text="2gb", font=smallFont)
ram_lbl_min.place(relx=0.27, rely=0.5, anchor=customtkinter.CENTER)

ram_lbl_mid = customtkinter.CTkLabel(master=app, text="6gb", font=smallFont)
ram_lbl_mid.place(relx=0.50, rely=0.6, anchor=customtkinter.CENTER)

ram_lbl_max = customtkinter.CTkLabel(master=app, text="10gb", font=smallFont)
ram_lbl_max.place(relx=0.74, rely=0.5, anchor=customtkinter.CENTER)

ram_slider = customtkinter.CTkSlider(master=app, from_=2, to=10, number_of_steps=4)
ram_slider.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
ram_slider.set(int(ram))

app.mainloop()