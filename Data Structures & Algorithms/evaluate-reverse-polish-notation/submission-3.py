import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_dict = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        stack = []

        for token in tokens:
            if token in op_dict:
                b = stack.pop()
                a = stack.pop()

                if token == '/':
                    val = int(a / b)
                else:
                    val = op_dict[token](a, b)

                stack.append(val)
            else:
                stack.append(int(token))

        return stack[0]