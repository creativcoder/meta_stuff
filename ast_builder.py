import unittest

# class Expr():
#     def __init__(self):
#         self.lhs = None
#         self.op = None
#         self.rhs = None

class Node():
    def __init__(self):
        self.frag = ""
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None


OPS = ['-','+','*','/','%']



class Ast():
    def __init__(self,expr):
        self.root = None
        self.expr = expr
        self.pos = len(expr)-1
    def eat(self):
        if self.pos == -1:
            return 'EOF'
        # print self.expr[self.pos]
        return self.expr[self.pos]
        self.pos -= 1
    def createAst(self):
        lexeme = self.eat()
        print(lexeme)
        while lexeme is not 'EOF':
            lexeme = self.eat()
            print(lexeme)
            if lexeme in OPS:
                if self.root == None:
                    self.root = Node()
                    print self.expr[self.pos+1:]
                else:
                    pass


def main():
    s = "2+3*2-4"
    a = Ast(s)
    a.createAst()

main()
