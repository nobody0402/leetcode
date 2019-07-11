class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = ["+","-","*","/"]
        stack = []
        for s in tokens:
            if s in ops:
                a = stack.pop()
                b = stack.pop()
                
                if s == "+":
                    stack.append(b+a)
                elif s == "-":
                    stack.append(b-a)
                elif s == "*":
                    stack.append(b*a)
                else: 
                    if a * b < 0 and b%a !=0:
                        stack.append(b/a+1)
                    else:
                        stack.append(b/a)
            else:
                stack.append(int(s))
                
        return stack[0]
        