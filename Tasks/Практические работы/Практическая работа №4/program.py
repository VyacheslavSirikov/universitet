def read_file(file):
    text = open(file, 'r', encoding="utf-8").read().lower()
    words = text.split()
    words = [word.strip('.,!;()[]-+=—') for word in words]
    uniq = []
    for word in words:
        if word not in uniq:
            uniq.append(word)
    return uniq


def save_file(uniq):
    text = open("count.txt", 'w')
    vs = len(uniq)
    text.write(f"{str(vs)} \n {uniq}")
    uniq.sort()
    s = "\n".join(uniq)
    return f"""Всего уникальных слов: {vs}\n========================\n{s} """
