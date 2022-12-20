dictionary = {}

input_count = int(input())

for i in range(0, input_count):
    name, voice_count = input().split()

    if name in dictionary:
        dictionary[name] = str(int(voice_count) + int(dictionary[name]))
    else:
        dictionary[name] = voice_count

for name, voice_count in sorted(dictionary.items()):
    print(name + ' ' + voice_count)
