# Token types

INTEGER, PLUS, EOF = 'INTEGER','PLUS','EOF'

class Token(object):
    def __init__(self,type,value):
        # the type of token
        self.type = type
        # the value contained in token
        self.value = value

    def __str__(self):
        return 'Token({type},{value})'.format(
            type=self.type,
            value=repr(self.value)
            )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self,text):
        # client string input, e.g. "3 + 5"
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        
        text = self.text

        if self.pos > len(text) -1:
            return Token(EOF,None);
