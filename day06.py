from collections import Counter

from helpers import get_file

packets = get_file("06")

for packet in packets:
    start = 0
    end = 14
    while True:
        check = packet[start:end]
        if len(Counter(check)) == 14:
            print(end)
            break
        start += 1
        end += 1
