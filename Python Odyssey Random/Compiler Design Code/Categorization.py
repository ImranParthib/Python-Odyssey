import re

s = input("Enter code: ")

# Define lists of operators, keywords, and symbols
operators = ["+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">=",
             "&&", "||", "!", "&", "|", "^", "~", "<<", ">>", "+=", "-=", "*=", "/="]
keywords = ['int', 'float', 'char', 'double', 'auto', 'break', 'case', 'const', 'continue', 'default', 'do', 'else', 'enum', 'extern', 'for', 'goto', 'if',
            'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']

symbols = [';', ',', '(', ')', '{', '}', '[', ']', ':']

# Split the input into words and remove extra whitespace
words = re.findall(r'\w+|\S', s)

# Initialize lists to store categorized items
categorized_operators = []
categorized_keywords = []
categorized_symbols = []
categorized_identifiers = []

# Categorize words
for word in words:
    if word in operators:
        categorized_operators.append(word)
    elif word in keywords:
        categorized_keywords.append(word)
    elif word in symbols:
        categorized_symbols.append(word)
    else:
        categorized_identifiers.append(word)

# Print the results
print("Operators:", ", ".join(categorized_operators))
print("Keywords:", ", ".join(categorized_keywords))
print("Symbols:", ", ".join(categorized_symbols))
print("Identifiers:", ", ".join(categorized_identifiers))
