
class AppStore:
    def __init__(self):
        self.app = {}
    
    def add_application(self, app):
        """добавление нового приложения app в магазин"""
        self.app.get[id(app)] = app
    
    def remove_application(self, app):
        """удаление приложения app из магазина"""
        self.app.pop(id(app))
    
    def block_application(self, app):
        obj = self.app.get(id(app), False)
        if not obj:
            False
        obj.blocked = True
    
    def total_apps(self):
        """"возвращает общее число приложений в магазине."""
        return len(self.app)


class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False
    

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)