s = input()
stack = []
for i in s:
    if i in ['(','[']:
        stack.append(i)
    else: 
        if stack and i==')':
            if len(stack)>1 and str(stack[-1]).isdigit():
                n = stack.pop()*2
                stack.pop()
                stack.append(n)
            elif stack[-1]=='(':
                stack.pop()
                stack.append(2)
            else:
                stack.append('-')
                break
                
        elif stack and i==']':
            if len(stack)>1 and str(stack[-1]).isdigit():
                n = stack.pop()*3
                stack.pop()
                stack.append(n)
            elif stack[-1]=='[':
                stack.pop()
                stack.append(3)
            else:
                stack.append('-')
                break
                
        else:
            stack.append('-')
            break
    if len(stack)>1 and str(stack[-1]).isdigit() and str(stack[-2]).isdigit():
        stack.append(stack.pop()+stack.pop())
 
if len(stack)==1 and str(stack[-1]).isdigit():
    print(stack.pop())
else:
    print(0)
