str = input()
# str = "int function(int a)"
n = len(str)

m = 0
result = ""

for i in range(n):
    if str[n - 1] == ')':
        if str.startswith('int'):
            print("Function type: Valid")
            print("Return type: int")
            break
        elif str.startswith('void'):
            print("Function type: Valid")
            print("Return type: void")
            break
        else:
            print("Function type: Valid")
            print("Return type: void")
            break
    else:
        print("Error Found")
        break

for i in range(n):
    if str[i] == '(':
        m = i

for i in range(m + 1, n - 1):
    result += str[i]

if str[m] == '(' and str[n - 1] == ')' and str[m + 1] != ')':
    print("Parameters:", result)
