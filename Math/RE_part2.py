import re
text = ''' Benefits of Yoga           
Note 1 - Overview
Yoga calms mind, yoga calms body
Note 2 - Doing it the right way
Doing it in the right way is the most important way'''

#We have to extract the Note values using RE
pattern = 'Note \d - ([^\n]*)'
matches = re.findall(pattern, text)
print(matches)