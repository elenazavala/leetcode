class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "/" or tokens[i] == "*":
                op = tokens[i]
                
                firstValue = stack.pop()
                secondValue = stack.pop()
                if op == "+":
                    operation = firstValue + secondValue 
                elif op == '-':
                    operation = secondValue - firstValue
                elif op == '/':
                    operation = int(secondValue / firstValue)
                else:
                    operation = firstValue * secondValue
                    
                stack.append(operation)                
                continue
            
            stack.append(int(tokens[i]))
                
        
        return stack.pop()
