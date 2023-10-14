from winreg import ConnectRegistry, OpenKey, QueryValueEx, HKEY_CURRENT_USER
import db.db as db
import sys


themes = {
    "light": "#FFFFFF",
    "lightSecondary": "#F0F0F0",
    "lightLowContrast": "#909090",
    "lightHighContrast": "#1E1E1E",
    
    "dark": "#1E1E1E",
    "darkSecondary": "#545454",
    "darkLowContrast": "#909090",
    "darkHighContrast": "#F0F0F0"
}

app_theme = 'device'
def settingsInit():
    db.connect()
    global app_theme
    app_theme = db.fetch_one('settings', 'theme')
    print(app_theme)
    
class theme:

    def get_sys_theme():
        default = True
        try:
            aReg = OpenKey(ConnectRegistry(None,HKEY_CURRENT_USER), r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _=QueryValueEx(aReg, "AppsUseLightTheme")
            return value == 1
            #return defualt
        except:
            print(f"Error: {sys.exc_info()[0]}")
            return default
    
    def primaryColor():
        global themes, app_theme
        if app_theme == 'device':
            if theme.get_sys_theme():
                return themes["light"]
            else:
                return themes["dark"]
        elif app_theme == 'light':
            return themes["light"]
        elif app_theme == 'dark':
            return themes["dark"]
        else:
            return themes["light"]
    
        
    def secondaryColor():
        global themes, app_theme
        if app_theme == 'device':
            if theme.get_sys_theme():
                return themes["lightSecondary"]
            else:
                return themes["darkSecondary"]
        elif app_theme == 'light':
            return themes["lightSecondary"]
        elif app_theme == 'dark':
            return themes["darkSecondary"]
        else:
            return themes["lightSecondary"]
    
    def lowContrast():
        global themes, app_theme
        if app_theme == 'device':
            if theme.get_sys_theme():
                return themes["lightLowContrast"]
            else:
                return themes["darkLowContrast"]
        elif app_theme == 'light':
            return themes["lightLowContrast"]
        elif app_theme == 'dark':
            return themes["darkLowContrast"]
        else:
            return themes["lightLowContrast"]
    
    def highContrast():
        global themes, app_theme
        if app_theme == 'device':
            if theme.get_sys_theme():
                return themes["lightHighContrast"]
            else:
                return themes["darkHighContrast"]
        elif app_theme == 'light':
            return themes["lightHighContrast"]
        elif app_theme == 'dark':
            return themes["darkHighContrast"]
        else:
            return themes["lightHighContrast"]
    def warn():
        return "#FF0000"
