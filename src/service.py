import schwabdev
import os

def Run():
    app_key = os.environ.get("APP_KEY")
    secret = os.environ.get("SECRET")
    client = schwabdev.Client(app_key, secret)

if __name__ == '__main__':
    Run()