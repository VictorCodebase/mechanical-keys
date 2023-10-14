from tkinter import *
from themes import *
import settings as settings
import db.db as db
import construct as construct
from keyResponse import *
from PIL import ImageTk, Image
import sys
import os

current_theme = 2

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 #if MEIPASS2 doesnt work, switch to MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def settingsInit():
    db.connect()
    global current_theme
    current_theme = db.fetch_one('settings', 'key_theme')
    print(current_theme)
#settingsInit()
def home(window):
    
    def openSettings(arg):
        settings.settings()
    
    # stsImage = Image.open(resource_path("./images/light_mode_settings.png"))
    # settingsImg = ImageTk.PhotoImage(stsImage)
    img = PhotoImage(file=resource_path("./images/light_mode_settings.png"))

    #?Giant wpm and fwpm display
    construct.construct_lables(window, ["23", "96"], 29, 53, ["Inter", 80, 'bold'], theme.primaryColor(), theme.highContrast(), 'w', True, 0, 127)
    #?smaller wpm and fwpm display
    construct.construct_lables(window, ["Avg", "WPM"], 155, 90, ["Inter", 20, 'normal'], theme.primaryColor(), theme.highContrast(), 'w', False, 0, 37)
    construct.construct_lables(window, ["Fastest", "WPM"], 155, 217, ["Inter", 20, 'normal'], theme.primaryColor(), theme.highContrast(), 'w', False, 0, 37)

    #? Change keyboard sound menu

    Canvas(window, width=280, height=360 ,bg=theme.secondaryColor(), highlightthickness=0).place(x= 290, y= 0)



    settingsBtn = Label(
        window,
        bg=theme.secondaryColor(),
        text='Settings',
        width=21,
        height=1,
        cursor='hand2',
        fg=theme.highContrast(),
        background=theme.secondaryColor(),
        font=("Inter", 15),
        activebackground=theme.primaryColor(),
        activeforeground=theme.highContrast(),
        borderwidth=1,
        highlightthickness=1,
        highlightbackground=theme.highContrast()  # Specify the outline color here
    )
    settingsBtn.place(x=300, y=26)
    settingsBtn.bind("<Button-1>", openSettings)


    # button styling
    button_width = 21
    button_height = 2
    starting_x = 300
    starting_y = 106
    button_spacing = 70
    font_size = 15
    type_face = "Inter"
    border_width = 1
    highlight_thickness = 1
    
    # Sound_1 = Label(
    #     window,
    #     text="Thock",
    #     bg=theme.secondaryColor(),
    #     width=button_width,
    #     height=button_height,
    #     fg=theme.highContrast(),
    #     font=(type_face, font_size),
    #     activebackground=theme.primaryColor(),
    #     activeforeground=theme.highContrast(),
    #     borderwidth=border_width,
    #     highlightthickness=highlight_thickness,
    #     highlightbackground=theme.lowContrast()  
    # )
    
    # ###########Hello. I am here to remind you that you look pretty today✨. Have a nice day.###########

    # Sound_2 = Label(
    #     window,
    #     text="Raining glass marble",
    #     bg=theme.secondaryColor(),
    #     width=button_width,
    #     height=button_height,
    #     fg=theme.highContrast(),
    #     font=(type_face, font_size),
    #     activebackground=theme.primaryColor(),
    #     activeforeground=theme.highContrast(),
    #     borderwidth=border_width,
    #     highlightthickness=highlight_thickness,
    #     highlightbackground=theme.lowContrast()  
    # )
    # Sound_3 = Label(
    #     window,
    #     text="1980's typwriter",
    #     bg=theme.secondaryColor(),
    #     width=button_width,
    #     height=button_height,
    #     fg=theme.highContrast(),
    #     font=(type_face, font_size),
    #     activebackground=theme.primaryColor(),
    #     activeforeground=theme.highContrast(),
    #     borderwidth=border_width,
    #     highlightthickness=highlight_thickness,
    #     highlightbackground=theme.lowContrast()  
    # )
    

    #construct.construct_buttons retunrs a string of buttons
    buttons = construct.construct_buttons(
        window, 
        ["Thock", "Raining glass marble", "1980's typwriter"], 
        starting_x, 
        starting_y, 
        button_width, 
        button_height,
        ["Inter", font_size, 'normal'], 
        theme.secondaryColor(), 
        theme.highContrast(), 
        theme.lowContrast(),
        highlight_thickness,
        border_width,
        'w', 
        0, 
        button_spacing)
    
    def change_highlighted_btn(button_num):
        buttons[current_theme - 1].config(bg=theme.secondaryColor())
        buttons[current_theme - 1].config(highlightbackground=theme.lowContrast())
        buttons[button_num].config(bg=theme.primaryColor())
        buttons[button_num].config(highlightbackground=theme.highContrast())
    
    def highlight_button(button_num):
        buttons[button_num].config(bg=theme.primaryColor())
        buttons[button_num].config(highlightbackground=theme.highContrast())
    
    def bind_buttons():
        print (buttons)

        #? Remember to manually bind funtionality here
        # index = 0
        # methods = [thock_theme, raining_glass_theme, typwriter_theme]
        # while index is not len(buttons) - 1:
        #     buttons[index].bind("<Button-1>", methods)
        #     index += 1
        buttons[0].bind("<Button-1>", thock_theme)
        buttons[1].bind("<Button-1>", raining_glass_theme)
        buttons[2].bind("<Button-1>", typwriter_theme)
        #? Selected theme button changes colour here
        highlight_button(current_theme - 1)

    #TODO: allow users to play demo sounds
    def thock_theme(arg):
        global current_theme
        themeNum = 1
        button_num = 0
        change_highlighted_btn(button_num)
        db.change_val('key_theme', themeNum)
        restart(arg)

    def raining_glass_theme(arg):
        themeNum = 2
        button_num = 1
        change_highlighted_btn(button_num)
        db.change_val('key_theme', themeNum)
        restart(arg)

    def typwriter_theme(arg):
        themeNum = 3
        button_num = 2
        change_highlighted_btn(button_num)
        db.change_val('key_theme', themeNum)
        restart(arg)

    bind_buttons()


    def restart(arg):
        restart_warnign.config(text="* Restarting to apply changes")
        window.after(1000, perform_restart)
    
    def perform_restart():
        os.execl(sys.executable, sys.executable, *sys.argv)
        


    #? Restart warning
    #TODO: Let user choose to restart but give option to automatically restart next time
    restart_warnign = Label(
        window,
        text="",
        bg=theme.secondaryColor(),
        fg=theme.warn(),
        font=("Inter", 10),  
    )
    restart_warnign.place(x=300, y= 310)


