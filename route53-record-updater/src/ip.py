from requests import get

def getCurrentIpV4():
    ip = get('https://api.ipify.org').content.decode('utf8')

    return ip