import re
text = ''' The Elon musk phone number is (921)-456-3321 , Where as the Mukesh Ambani phone number is 9998887776 '''
pattern = r'\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches = re.findall(pattern,text)
print(matches)

"""
=============================================================================
PYTHON REGULAR EXPRESSIONS (re) 
=============================================================================
Regular Expressions (Regex/RE) are a mini-language for finding, matching,
and manipulating text patterns. 

HEURISTIC APPROACH IN NLP:
Regex is a "heuristic" (rule-based/practical) approach in NLP. You hardcode 
exact rules (e.g., "Find all words ending in 'ing'") instead of letting 
a machine learning model guess based on training data. It is primarily 
used for text cleaning, data extraction, and preprocessing.

GOLDEN RULE: 
Always use Raw Strings by prefixing with 'r' (e.g., r"\n"). This stops 
Python from interpreting backslashes as escape characters so the regex 
engine can read them properly.

-----------------------------------------------------------------------------
1. CORE FUNCTIONS (The Actions)
-----------------------------------------------------------------------------
import re

re.search(pattern, text)  -> Scans ENTIRE text, returns Match object for FIRST match.
re.match(pattern, text)   -> Checks for a match ONLY at the VERY BEGINNING.
re.findall(pattern, text) -> Finds ALL matches, returns them as a standard Python List.
re.sub(pat, repl, text)   -> Finds ALL matches and REPLACES them with a new string.

-----------------------------------------------------------------------------
2. CHARACTER CLASSES (The "Who")
Note: Uppercase is always the exact opposite of lowercase!
-----------------------------------------------------------------------------
\d : Any digit (0-9)
\D : Any NON-digit (letters, symbols, spaces)

\w : Any word character (a-z, A-Z, 0-9, and underscores)
\W : Any NON-word character (spaces, punctuation)

\s : Any whitespace (space, tab, newline)
\S : Any NON-whitespace character

 . : Any character EXCEPT a newline (\n)

-----------------------------------------------------------------------------
3. ANCHORS & BOUNDARIES (The "Where")
These match positions in the text, not actual characters.
-----------------------------------------------------------------------------
^  : Starts with     -> r"^Hello"  (Matches "Hello world", NOT "Say Hello")
$  : Ends with       -> r"world$"  (Matches "Hello world", NOT "world peace")
\b : Word boundary   -> r"\bcat\b" (Matches "the cat", NOT "the catalog")

-----------------------------------------------------------------------------
4. QUANTIFIERS (The "How Many")
Place these immediately AFTER a character or group.
-----------------------------------------------------------------------------
*      : 0 or more times     -> r"ca*t"   (Matches ct, cat, caat, caaaat)
+      : 1 or more times     -> r"ca+t"   (Matches cat, caat... but NOT ct)
?      : 0 or 1 time         -> r"colou?r"(Matches color, colour)
{n}    : Exactly n times     -> r"\d{3}"  (Matches 123, 999)
{n,m}  : Between n & m times -> r"\d{2,4}"(Matches 12, 123, 1234)

-----------------------------------------------------------------------------
5. SETS AND GROUPS
-----------------------------------------------------------------------------
[ ]    : Character Set -> Matches ANY ONE character inside. 
                          r"[aeiou]" matches any single vowel.
                          r"[A-Z]" matches any single capital letter.

[^ ]   : Negated Set   -> Matches any character NOT inside. 
                          r"[^0-9]" matches anything that isn't a number.

( )    : Grouping      -> Groups multiple characters together. 
                          r"(abc)+" matches "abc", "abcabc", etc.

 |     : OR Operator   -> Matches pattern before OR after. 
                          r"cat|dog" matches "cat" or "dog".
=============================================================================
"""

# ===========================================================================
# PRACTICAL TEMPLATE: Testing Regex in Python
# ===========================================================================
import re

# Example text containing various data
sample_text = """
Contact us at support@example.com or sales-info@company.net.
Call me at 555-123-4567 or at 999-888-7777 tomorrow.
Order IDs: #A123, #B456, #C789.
"""

# --- EXAMPLE 1: FIND ALL PHONE NUMBERS ---
# Pattern: 3 digits, hyphen, 3 digits, hyphen, 4 digits
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phones = re.findall(phone_pattern, sample_text)
print(f"Phones found: {phones}") 
# Output: ['555-123-4567', '999-888-7777']


# --- EXAMPLE 2: EXTRACT EMAIL ADDRESSES ---
# Pattern: 
# 1. [\w.-]+   -> 1 or more word chars, dots, or hyphens (username)
# 2. @         -> exact '@' symbol
# 3. [\w.-]+   -> 1 or more word chars, dots, or hyphens (domain)
# 4. \.        -> exact '.' symbol (escaped with backslash)
# 5. [a-zA-Z]+ -> 1 or more letters (com, net, org)
email_pattern = r"[\w.-]+@[\w.-]+\.[a-zA-Z]+"
emails = re.findall(email_pattern, sample_text)
print(f"Emails found: {emails}")
# Output: ['support@example.com', 'sales-info@company.net']


# --- EXAMPLE 3: DATA CENSORSHIP (re.sub) ---
# Replace all 3-digit order numbers with '***'
# Pattern: '#' followed by 1 uppercase letter, then exactly 3 digits
order_pattern = r"#[A-Z]\d{3}"
censored_text = re.sub(order_pattern, "[REDACTED]", sample_text)
print(f"\nCensored Text: {censored_text}")