class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        operators = ['+','-','*','/']
        
        numbers = []
        
        for token in tokens:
            if token not in operators:
                numbers.append(token)
            else:
                number1 = int(numbers.pop())
                number2 = int(numbers.pop())
                if token == '+':
                    result = number2 + number1
                elif token == '-':
                    result = number2 - number1
                elif token == '*':
                    result = number2 * number1
                elif token =='/':
                    result = number2 / number1
                else:
                    pass
                
                numbers.append(str(result))
                print numbers
                
        return int(numbers[0])


lista = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
d = Solution()
print d.evalRPN(lista)