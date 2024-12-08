import winreg

def get_windows_theme():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize')
        value, _ = winreg.QueryValueEx(key, 'AppsUseLightTheme')
        winreg.CloseKey(key)
        
        if value == 0:
            return "Темная тема"
        else:
            return "Светлая тема"
    except FileNotFoundError:
        return "Не удалось определить тему"

print(get_windows_theme())
