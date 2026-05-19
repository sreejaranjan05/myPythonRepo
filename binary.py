stack = []
string = "HELLO"

for ch in string:
    stack.append(ch)

rev = ""
while stack:
    rev += stack.pop()

print("Reversed string:", rev)
