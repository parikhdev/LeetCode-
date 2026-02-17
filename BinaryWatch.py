def readBinaryWatch(turnedOn):
    List = []
    for h in range(12):
        for m in range(60):
            if (h.bit_count() + m.bit_count()) == turnedOn:
                List.append(f"{h}:{m:02d}")
    return List
print(readBinaryWatch(1))