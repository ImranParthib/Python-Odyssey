x = input("Enter the string here: ")
li = ['+', '-', '*', '/', '=']

if "int" in x:
    print("int found")
if ";" in x:
    print("specifier found")
if (x in li):
    print("operator found")
inp = input()
kwords = ['int', 'float', 'char', 'double', "auto", "break", "case", "const", "continue", "default", "do", "else",
         "enum", "extern", "for", "goto", "if", "long", "register", "return", "short", "signed", "sizeof", "static",
         "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]
c=0
x = len(inp)
if x > 31:
   c=0
elif (inp[0]>='0'and inp[0]<='9'):
   c=0
elif x <= 31 and inp not in kwords:
   if (inp[0] == '_' or inp[0] >= 'A' or inp[0] <= 'Z' or inp[0] >= 'a' or inp[0] <= 'z'):
       c=1
   for i in range(x):
       if (inp[i]==',' or inp[i]==' '):
           c=0
if c == 0:
   print("Invalid")
elif c == 1:
   print("Identifier")
