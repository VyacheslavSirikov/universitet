import re

pattern = r"^Рейс (\d+) (?:прибыл|отправился) (из|в) (\w+) в (\d{2}:\d{2}:\d{2})"

with open("bbb.txt", "r", encoding="utf-8") as bbb:
    with open("ttt.txt", "w", encoding="utf-8") as ttt:
        for line in bbb:
            res = re.search(pattern, line)
            if res:
                ttt.write(f"[{res.groups()[3]}] Поезд № {res.groups()[0]} {res.groups()[1]} {res.groups()[2]}\n")