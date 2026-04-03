import re
text = ''' Benefits of Yoga           
Note 1 - Overview
Yoga calms mind, yoga calms body
Note 2 - Doing it the right way
Doing it in the right way is the most important way'''

#We have to extract the Note values using RE
pattern = r"Note \d - ([^\n]*)"
#r"Note \d+ - ([^\n]*)"       
# Now it will perfectly match Note 1 -, Note 15 -, or even Note 999 -!
matches = re.findall(pattern, text)
print(matches)
'''Rule for re.findall():
-> If there are NO parentheses () in your pattern: It returns the entire matched string.
-> If there ARE parentheses () in your pattern: It completely changes its behavior. It will use the whole pattern to find the right location in the text, but it will only return the specific text that was captured inside the parentheses.'''
#Remember we have to use \ with words to make them powerful while use \ with symbols to remove their power

'''
( : Starts a Capture Group. This tells re.findall that we only want to keep the stuff inside these parentheses in our final list.

[^\n] : This is a Negated Set. \n means "newline". The ^ inside the brackets means "NOT". So this means "match any character that is NOT a newline".

* : Means "zero or more times". Combined with the above, it matches the entire rest of the line until the text drops to a new line.

) : Ends the Capture Group.

Because of those parentheses, re.findall ignores the "Note 1 - " part in the final output and only hands you the extracted titles: ['Overview', 'Doing it the right way'].

What is the meaning of the backward slash \?

In Regular Expressions, the backslash(\) is the Escape Character. It has two opposite jobs depending on what you put it next to:

(It gives normal characters SUPERPOWERS.)

d is just the letter "d".
\d becomes a superpower that matches ANY digit (0-9).

w is just the letter "w".
\w becomes a superpower that matches ANY word character.

(It takes superpowers AWAY from special symbols.)

. is a superpower that matches any character.
\. removes the superpower and just matches a literal, normal period/dot.

* is a superpower that means "zero or more".
\* removes the superpower and matches a literal asterisk.'''