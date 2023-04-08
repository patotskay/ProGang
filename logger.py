import datetime


class MyLOgger11:

    def __init__(self, path) -> None:
        self.log_file = path
        self.__wipe()
        
    def __wipe(self):
        open(self.log_file, "r").close()

    def write(self, message: str, console: bool) -> None:
        message = datetime.datetime.now().strftime("%y:%m:%d %H:%M:S")\
              + f" {message}"
        if console:
            print(message)
        with open(self.log_file, "a") as f:
            f.write(message + "\n")
