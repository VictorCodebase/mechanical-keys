from tkinter import *
from themes import *
import settings as settings
import db.db as db
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
settingsInit()
def home(window):
    
    def openSettings(arg):
        settings.settings()
    
    # stsImage = Image.open(resource_path("./images/light_mode_settings.png"))
    # settingsImg = ImageTk.PhotoImage(stsImage)
    img = PhotoImage(file=resource_path("./images/light_mode_settings.png"))

    #?word per minute display
    Label(
        window, 
        text="23", 
        bg= theme.primaryColor(), 
        fg=theme.textColor(), 
        font=("Inter", 80, 'bold')
        ).place(x =29, y = 53)
    Label(
        window, 
        text="Avg", 
        bg= theme.primaryColor(), 
        fg=theme.textColor(), 
        font=("Inter", 20)
        ).place(x =155, y = 90)
    Label(
        window, 
        text="WPM", 
        bg= theme.primaryColor(), 
        fg=theme.textColor(), 
        font=("Inter", 20)
        ).place(x =155, y = 127)

    #?fastest word per minute display   
    Label(
        window, 
        text="96", 
        bg= theme.primaryColor(), 
        fg=theme.textColor(), 
        font=("Inter", 80, 'bold')
        ).place(x =29, y = 180)
    Label(
        window, 
        text="Fastest", 
        bg= theme.primaryColor(), 
        fg=theme.textColor(), 
        font=("Inter", 20)
        ).place(x =155, y = 217)
    Label(
        window, 
        text="WPM", 
        bg= theme.primaryColor(), 
        fg=theme.textColor(), 
        font=("Inter", 20)
        ).place(x =155, y = 254)

    #? Change keyboard sound menu

    Canvas(window, width=280, height=360 ,bg=theme.secondaryColor(), highlightthickness=0).place(x= 290, y= 0)



    settingsBtn = Label(
        window,
        bg=theme.secondaryColor(),
        text='Settings',
        width=21,
        height=1,
        cursor='hand2',
        fg=theme.textColor(),
        background=theme.primaryColor(),
        font=("Inter", 15),
        activebackground=theme.primaryColor(),
        activeforeground=theme.textColor(),
        borderwidth=1,
        highlightthickness=1,
        highlightbackground=theme.textColor()  # Specify the outline color here
    )
    settingsBtn.place(x=300, y=26)
    settingsBtn.bind("<Button-1>", openSettings)
    
    # settingsIcon = Canvas(
    #     window,
    #     width=stsImage.width,
    #     height=stsImage.height,
    # )
    # settingsIcon.place(x= 500, y= 50)
    # settingsIcon.create_image(0,0,anchor=tk.NW, image=settingsImg)
    #Im really sorry. I really tried to get a transparent icon here, but its too much work. Feel free to do that. Ill make custom icons instead

    # Label(
    #     window,
    #     image=img
    # ).place(x= 500, y= 50)




    # button styling
    button_width = 21
    button_height = 2
    button_spacing = 70
    font_size = 15
    type_face = "Inter"
    border_width = 1
    highlight_thickness = 1
    
    Sound_1 = Label(
        window,
        text="Thock",
        bg=theme.secondaryColor(),
        width=button_width,
        height=button_height,
        fg=theme.textColor(),
        font=(type_face, font_size),
        activebackground=theme.primaryColor(),
        activeforeground=theme.textColor(),
        borderwidth=border_width,
        highlightthickness=highlight_thickness,
        highlightbackground=theme.textColor()  
    )
    
    ###########Hello. I am here to remind you that you look pretty today✨. Have a nice day.###########

    Sound_2 = Label(
        window,
        text="Raining glass marble",
        bg=theme.secondaryColor(),
        width=button_width,
        height=button_height,
        fg=theme.textColor(),
        font=(type_face, font_size),
        activebackground=theme.primaryColor(),
        activeforeground=theme.textColor(),
        borderwidth=border_width,
        highlightthickness=highlight_thickness,
        highlightbackground=theme.textColor()  
    )
    Sound_3 = Label(
        window,
        text="1980's typwriter",
        bg=theme.secondaryColor(),
        width=button_width,
        height=button_height,
        fg=theme.textColor(),
        font=(type_face, font_size),
        activebackground=theme.primaryColor(),
        activeforeground=theme.textColor(),
        borderwidth=border_width,
        highlightthickness=highlight_thickness,
        highlightbackground=theme.textColor()  
    )
    


    buttons = [Sound_1, Sound_2, Sound_3]
    def place_buttons(spacing, starting_x=300, starting_y=106):
        for i in range(len(buttons)):
            buttons[i].place(x=starting_x, y=starting_y + spacing * i)

        #? Remember to manually bind funtionality here
        buttons[0].bind("<Button-1>", thock_theme)
        buttons[1].bind("<Button-1>", raining_glass_theme)
        buttons[2].bind("<Button-1>", typwriter_theme)
        #? Selected theme button changes colour here
        buttons[current_theme - 1].config(bg=theme.primaryColor())


    def thock_theme(arg):
        global current_theme
        themeNum = 1
        button_num = 0
        buttons[current_theme - 1].config(bg=theme.secondaryColor())
        buttons[button_num].config(bg=theme.primaryColor())
        db.change_val('key_theme', themeNum)

            #TODO: allow users to play demo sounds
            # currentSound = pygame.mixer.Sound(resource_path(f'{currentTheme}key-1.wav'))
            # currentSound.set_volume(dynamicVolume.get_dynamic_volume())
            # #currentSound.set_volume(1)
            # currentSound.play()
        restart(arg)


    def raining_glass_theme(arg):
        themeNum = 2
        button_num = 1
        buttons[current_theme - 1].config(bg=theme.secondaryColor())
        buttons[button_num].config(bg=theme.primaryColor())
        db.change_val('key_theme', themeNum)
        restart(arg)

    def typwriter_theme(arg):
        themeNum = 3
        button_num = 2
        buttons[current_theme - 1].config(bg=theme.secondaryColor())
        buttons[button_num].config(bg=theme.primaryColor())
        db.change_val('key_theme', themeNum)
        restart(arg)

    place_buttons(button_spacing)

    def restart(arg):
        restart_warnign.config(text="* Restarting to apply changes")
        window.after(1000, perform_restart)
    
    def perform_restart():
        os.execl(sys.executable, sys.executable, *sys.argv)
        
#ajndksndaondisbdj jsdnjnkansansdck o naskdmklamdkaklmmksmdak

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


