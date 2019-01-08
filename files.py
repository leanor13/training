import json


with open("/Users/yulia_i/Documents/Course/config.json") as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res = {}

print(res)