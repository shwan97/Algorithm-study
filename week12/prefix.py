"""
백준 1918, 후위표기식
https://www.acmicpc.net/problem/1918

연산자 우선순위를 고려하여 다시 풀어보기
"""

import sys

infix_expression = sys.stdin.readline()[:-1]
# print("len", len(infix_expression))
# print(infix_expression)
operators = []
operands = []
answer = ''
for char in infix_expression:
    # print("char: ", char)

    if char.isalpha():  # 피연산자(알파벳대문자)
        operands.append(char)
    elif char == '(':
        operators.append(char)
    elif char in ['*', '/']:
        while operators and operators[-1] in ['*', '/']:
            op2 = operands.pop()
            op1 = operands.pop()
            string = op1 + op2 + operators.pop()
            operands.append(string)
        operators.append(char)
    elif char in ['+', '-']:
        while operators and operators[-1] in ['*', '/', '+', '-']:
            op2 = operands.pop()
            op1 = operands.pop()
            string = op1 + op2 + operators.pop()
            operands.append(string)
        operators.append(char)

    else: # char == ')'
        while operators and operators[-1] != '(':
            op2 = operands.pop()
            op1 = operands.pop()
            string = op1 + op2 + operators.pop()
            # print(')', string)
            operands.append(string)
        if operators[-1] == '(':
            operators.pop()

while operators:
    op2 = operands.pop()
    op1 = operands.pop()
    string = op1 + op2 + operators.pop()
    # print('last', string)
    operands.append(string)

print(operands.pop())


