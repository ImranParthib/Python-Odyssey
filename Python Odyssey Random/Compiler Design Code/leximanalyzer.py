s = input()
op = ["+", "-", "*", "/", "="]
kwords = ['int', 'float', 'char',
          'double', "auto", "break", "case", "const", "continue", "default", "do", "else", "enum", "extern", "for", "goto", "if", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]
sy = [';', ","]
l = list(s.split(" "))
print(l)
operators = []
keywords = []
symb = []
idnt = []
for element in l:
    if element in op:
        if element not in operators:
            operators.append(element)
    elif element in kwords:
        if element not in keywords:
            keywords.append(element)
    elif element in sy:
        if element not in symb:
            symb.append(element)
    else:
        idnt.append(element)
print("Operators: ", ", ".join(operators))
print("Data types: ", ", ".join(keywords))
print("Symbol: ", " ".join(symb))
print("Identifier: ", ", ".join(idnt))
