import webbrowser
import requests

def open_in_broswer(str):
    f = open("test.html",'w', encoding='utf-8')
    f.write(str)
    f.close()
    webbrowser.open("test.html")
