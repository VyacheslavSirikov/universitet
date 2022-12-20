tdb = []
ts = []

db_input_count = int(input())

for i in range(0, db_input_count):
    tdb.append(input().split())

search_input_count = int(input())

for j in range(0, search_input_count):
    ts.append(input())

for town in ts:
    for data in tdb:
        if town in data:
            print(data[0])
            break
