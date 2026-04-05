def judgeCircle(moves):
    data = {'L': 0, 'R': 0, 'U':0, 'D': 0}
    for ch in moves:
        data[ch] = data.get(ch) + 1
    return data['L'] == data['R'] and data['U'] == data['D']     
print(judgeCircle('UD'))