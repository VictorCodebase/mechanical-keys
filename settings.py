from tkinter import *
from themes import *
import db.db as db
import construct as construct

ready = True
app_theme = 'device'

def settingsInit():
    db.connect()
    global app_theme
    app_theme = db.fetch_one('settings', 'theme')
    print(app_theme)


def settings():
    global ready
    if not ready:
        settingsNotReady()
        return
    print ('running settings')
    #TODO: minimize to tray, change volume, theme, disengage dynamic and emersive features, vary emersive features intensity
    window = Tk()
    window.title("Mechanical Keys Simulator - Settings")
    window.geometry("566x339")
    window.configure(bg=theme.primaryColor())

    Label(
        window, 
        text="Settings", 
        bg= theme.primaryColor(), 
        fg=theme.highContrast(), 
        font=("Inter", 20, 'bold')
        ).place(x =35, y = 30)
    
    #? Used construct module to create settings labels
    settings_ = ["Key Volume", "Theme", "Dynamic volume intensity", "Emersive features intensity"]
    construct.construct_lables(window, settings_, 35, 100, ["Inter", 10, 'normal'], theme.primaryColor(), theme.highContrast(), 'w', False, 0, 50)

    #? Keyboard volume slider
    Scale(
        window,
        from_=0,
        to=100,
        orient=HORIZONTAL,
        bg=theme.primaryColor(),
        fg=theme.highContrast(),
        highlightthickness=0,
        length=200,
        ).place(x= 130, y= 90)
    
    #? Themes radio buttons
    themes_ = ["Light", "Dark", "Device"]
    construct.construct_radio_buttons(window, themes_, 130, 140, ["Inter", 10, 'normal'], theme.primaryColor(), theme.highContrast(), 'w', 60, 0)


    # #? Change keyboard sound volume
    # Label(
    #     window, 
    #     text="Volume:", 
    #     bg= theme.primaryColor(), 
    #     fg=theme.highContrast(), 
    #     font=("Inter", 10)
    #     ).place(x =35, y = 100)

    
    # #? change app theme
    # Label(
    #     window, 
    #     text="Theme:", 
    #     bg= theme.primaryColor(), 
    #     fg=theme.highContrast(), 
    #     font=("Inter", 10)
    #     ).place(x =35, y = 150)
    # Radiobutton(
    #     window,
    #     text="Light",
    #     bg=theme.primaryColor(),
    #     fg=theme.highContrast(),
    #     highlightthickness=0,
    #     ).place(x= 130, y= 150)
    

    window.mainloop()
        
#settings()


def settingsNotReady():
    window = Tk()
    window.title("Mechanical Keys Simulator - Settings")
    window.geometry("566x339")
    window.configure(bg=theme.primaryColor())
    Label(
        window, 
        text="Coming soon in early September update alongside other mind blowing features✨", 
        bg= theme.primaryColor(), 
        fg=theme.highContrast(), 
        font=("Inter", 10)
        ).place(x =15, y = 100)
    Label(
        window, 
        text="See you then!!", 
        bg= theme.primaryColor(), 
        fg=theme.highContrast(), 
        font=("Inter", 10)
        ).place(x =15, y = 120)
    #? Change keyboard sound menu
    #Canvas(width=260, height=275 ,bg=theme.secondaryColor(), highlightthickness=0).place(x= 290, y= 36)
    window.mainloop()    