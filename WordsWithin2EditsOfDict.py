def twoEditWords(queries, dictionary): 
    final = []
    
    for q in queries:
        for d in dictionary:
            diffs = sum(1 for char_q, char_d in zip(q, d) if char_q != char_d)
            
            if diffs <= 2:
                final.append(q)
                break
                
    return final

print(twoEditWords(["word","note","ants","wood"],["wood","joke","moat"]))