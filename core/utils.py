import socket


def normalize_host(target):
    target = target.replace("https://", "").replace("http://", "")
    target = target.strip("/")
    return target


def resolve_host(target):
    host = normalize_host(target)
    return socket.gethostbyname(host)
