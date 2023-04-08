import os, datetime
import pandas

class MyLOgger11:
    def __init__(self, path) -> None:
        self.log_file = path
        self.wipe()
        
    def wipe(self):
        open(self.log_file, "r").close()

    def write(self, message: str, ekran: bool) -> None:
        message = datetime.datetime.now().strftime("%y:%m:%d %H:%M:S") + f" {message}"
        if ekran:
            print(message)
        with open(self.log_file, "a") as f:
            f.write(message + "\n")


