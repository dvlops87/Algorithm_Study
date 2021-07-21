# 2504. 괄호의 값
# ‘()’ 인 괄호열의 값은 2이다.
# ‘[]’ 인 괄호열의 값은 3이다.
# ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
# ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
# 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.


question = input()
stack = []
total = 0 
for _ in range(len(question)):
    if "()" in question:
        question = question.replace("()", "2")
    elif "[]" in question:
        question = question.replace("[]", "3")
    elif "(" in question:
        question = question.replace("(", "2*")
        stack.append("(")
        print(stack)
    elif "[" in question:
        question = question.replace("[", "3*")
        stack.append("[")
    elif ")" in question:
        try:   
            stack.pop()
            question = question.replace(")",'')
        except: print(0)
    elif "]" in question:
        try: 
            stack.pop()
            question = question.replace("]", '')
        except : print(0)
print(question)
if len(stack) == 0 : print(1)
else: print(0)


# for x in question:
#     if x == "(" or x == "[":
#         stack.append(x)
#     elif x == ")":
#         stack.pop()
#         total += 2 
#         if len(stack) !=0 and stack[len(stack)-1] == "[":
#             total *= 3
#         elif len(stack)!=0 and stack[len(stack)-1] == "(":
#             total *=2
#         elif len(stack) == 0 :
#             total += 2 
#     elif x == "]":
#         stack.pop()
#         total +=3
#         if len(stack) !=0 and stack[len(stack)-1] == "[":
#             total *= 3
#         elif len(stack)!=0 and stack[len(stack)-1] == "(":
#             total *=2
#         elif len(stack) == 0 :
#             total += 2 
        
# if len(stack) == 0 : print(total)
# else : print(0)
        
    