class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        for c in tokens:
          if c == "+":
            stack.append(stack.pop() + stack.pop())
          elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a) 
          elif c == "*":
            stack.append(stack.pop() * stack.pop())
          elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
          else:
            stack.append(int(c))

        return stack.pop()



problem = Solution()
print(problem.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))