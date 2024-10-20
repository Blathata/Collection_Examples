TYPE_OS = 2 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"

class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    def __new__(cls, *args, **kwargs):

        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
        else:
            obj = super().__new__(DialogLinux)
        
        obj.name = args[0]
        return obj
    
pt = Dialog('gt')
print(pt)

