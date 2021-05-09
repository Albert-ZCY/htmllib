import os
import json

file = 'Tool.py'
path = __file__.strip(file)

def dictToArgs(dct):
    args = ''
    for key in dct:
        span = f' {key}="{dct[key]}"'
        args += span
    return args

def getPos(kw):
    web_lines = loadWebLines()
    for line in web_lines:
        if kw in line:
            return web_lines.index(line)

def loadWebLines():
    with open(path+'web-tmp/web_lines.json', 'r') as wl:
        return json.load(wl)

def writeWebLines(obj):
    with open(path+'web-tmp/web_lines.json', 'w') as wl:
        json.dump(obj, wl)

def loadInfo():
    with open(path+'info/info.json', 'r') as inf:
        return json.load(inf)

def writeInfo(content):
    with open(path+'info/info.json', 'w') as inf:
        json.dump(content, inf)