
class Router:
    def __init__(self):
        self.buffer: list = []
        self.servers: dict = {}
    
    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру"""
        self.servers[server.ip] = server
        server.router = self
        
    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера"""
        s = self.servers.pop(server.ip,False)
        if s:
            s.router = None
          
    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера серверам"""
        for d in self.buffer:
            if d.ip in self.servers:
                self.servers[d.ip].buffer.append(d)
                print(self.buffer)
        self.buffer.clear() 


class Server:
    server_ip = 1
    
    def __init__(self):
        self.buffer: list = []
        self.ip: int = Server.server_ip
        Server.server_ip += 1
        self.router = None

    def send_data(self, data):
        """Для отправки информационного пакета data (объекта класса Data)
        с указанным IP-адресом получателя
        """
        if self.router: # отправляет в роутер пакет Data
            self.router.buffer.append(data)

    def get_data(self):
        """Возвращает список принятых пакетов"""
        b = self.buffer[:]
        self.buffer.clear()
        return b

    def get_ip(self):
        """Возвращает свой IP-адрес"""
        return self.ip


class Data:
    def __init__(self, msg: str, ip: int):
        """ Пакет информации

        Args:
            msg (str): передаваемые данные (строка
            ip (int): IP-адрес назначения.
        """
        self.data = msg
        self.ip = ip


router = Router()

sv_from = Server() # создаем сервер
sv_from2 = Server() # создаем сервер
sv_to = Server()

router.link(Server())
router.link(Server())

router.link(sv_from)
router.link(sv_from2)
router.link(sv_to)

sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))

router.send_data()

msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
