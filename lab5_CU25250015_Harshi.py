# # Ques 1 Infix to POstfix
# class Stack:
#     def __init__(self):
#         self.items = []
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         return None
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         return None
#     def is_empty(self):
#         return len(self.items) == 0

# def precedence(operator):
#     if operator == '+' or operator == '-':
#         return 1
#     elif operator == '*' or operator == '/':
#         return 2
#     elif operator == '^':
#         return 3
#     return 0

# def infix_to_postfix(expression):
#     stack = Stack()
#     postfix = ""
#     for char in expression:
#         if char == ' ':
#             continue
#         if char.isalnum():
#             postfix += char
#         elif char == '(':
#             stack.push(char)
#         elif char == ')':
#             while not stack.is_empty() and stack.peek() != '(':
#                 postfix += stack.pop()

#             stack.pop() 
#         else:
#             while (not stack.is_empty() and
#                    stack.peek() != '(' and
#                    precedence(stack.peek()) >= precedence(char)):
#                 postfix += stack.pop()

#             stack.push(char)
#     while not stack.is_empty():
#         postfix += stack.pop()

#     return postfix

# expression = input("Enter an infix expression: ")

# postfix = infix_to_postfix(expression)

# print("Infix Expression :", expression)
# print("Postfix expression :", postfix)

# ques 2 Postfix Expression Evaluation
class IntegerStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

def evaluate_postfix(expression):
    stack = IntegerStack()

    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2

            elif char == '-':
                result = operand1 - operand2

            elif char == '*':
                result = operand1 * operand2

            elif char == '/':
                result = operand1 / operand2

            elif char == '^':
                result = operand1 ** operand2

            stack.push(result)

    return stack.pop()
expression = input("Enter a postfix expression: ")

result = evaluate_postfix(expression)

print("Postfix Expression:", expression)
print("Final Result:", result)
