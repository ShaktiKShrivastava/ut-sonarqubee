import requests


class APICalls:
    def __init__(self):
        self.session = requests.Session()

    def do_get(self, url):
        out = self.session.get(url)
        return out


class Connect:
    def __init__(self, uname, pwd):
        self.username = uname
        self.password = pwd

    def login(self):
        pass

    def logout(self):
        pass

    def send_command(self, cmd):
        return 'some_output'


if __name__ == '__main__':
    obj = APICalls()
    out = obj.do_get('URL')
    print(out)