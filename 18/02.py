#! /usr/bin/env python3
import re
import math

# ==== INPUT ====
data = ""
with open('18.txt', 'r') as file:
    data = file.read().strip()

rows = [row.strip().replace('(', '( ').replace(')', ' )').split(' ') for row in data.split('\n')]

# ==== SOLUTION ====

plus  = sum
times = math.prod

def evaluate(statement):
    accumulator = 0
    operator = plus
    while statement:
        element = statement.pop(0)
        if element == '(':
            accumulator = operator((accumulator, evaluate(statement)))
        elif element == ')':
            return accumulator
        elif element == '+':
            operator = plus
        elif element == '*':
            operator = times
        else:
            accumulator = operator((accumulator, int(element)))
    else:
        return accumulator


# def eval_rpn(stack):



# def rpn(statement):
#     output = []
#     operators = []

#     while statement:
#         element = statement.pop(0)
#         if element == '(':
#             operators.append(element)
#         elif element == ')':
#             while operators and operators[-1] != '(':
#                 output.append(operators.pop())
#             if operators[-1] == '(':
#                 operators.pop()
#         elif element in ['+','*']:
#             while operators and operators == '*' and operators[-1] == '+':
#                 output.append(operators.pop())
#             operators.append(operators)
#         else:
#             output.append(element)

#     while operators:
#         output.append(operators.pop())
#     return output



# total = 0
# for line in rows:
#     stack = rpn(line)
#     print(stack)
#     ev = evaluate(line)
#     print(ev)
#     total += ev

# print()
# print(total)



def to_postfix(statement):  # Shunting yard algorithm
    output = []
    stack = []
    while statement:
        token = statement.pop(0)
        if token not in ['+', '*', '(', ')']:
            output.append(token)
        elif token in ['+', '*']:
            while stack and token == '*' and stack[-1] == '+':
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack[-1] == '(':
                stack.pop()
    while stack:
        output.append(stack.pop())
    return output


def evaluate_postfix(statement):
    stack = []
    for token in statement:
        if token not in ['+', '*']:
            stack.append(token)
        elif token == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        else:
            stack.append(int(stack.pop()) * int(stack.pop()))
    return stack[0]


total = 0
for line in rows:
    total += evaluate_postfix(to_postfix(line))
print(total)  # Part 2
