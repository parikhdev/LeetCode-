import re
text = ''' The Elon musk phone number is (921)-456-3321 , Where as the Mukesh Ambani phone number is 9998887776 '''
pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches = re.findall(pattern,text)
print(matches)