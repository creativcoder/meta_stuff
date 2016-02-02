# Token types

INTEGER, PLUS, WHITESPACE, EOF = 'INTEGER','PLUS','WHITESPACE','EOF'

class Token:
    INTEGER = 'INTEGER'
    PLUS = '+'
    MINUS = '-'
    DIV = '/'
    MULT = '*'
    MOD = '%'
    WHITESPACE = ' '
    EOF = 'EOF'


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
        self.tok_seq = []
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        
        text = self.text

        if self.pos > len(text) -1:
            return Token(EOF,None)

        current_char = text[self.pos]
        if current_char.isdigit():
            token = Token(INTEGER,int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS,current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self,token_type):
        # compare the current token type with the passed token
        # type and if they match then eat the current token and
        # assign the next token to the self.current_token,
        # otherwise raise the exception
        if self.current_token.type == token_type:
            self.tok_seq.append(self.current_token)
            self.current_token = self.get_next_token()
        else:
            self.error()

    def build_and_eval(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        print(self.tok_seq)
        print("")

        result = left.value + right.value
        return result


def main():
    print("\nKISS (Keep it simple stupid Interpreter) v0.0.1\n\n")
    while True:
        try:

            text = raw_input('kiss::>')
        except EOFError:
            break
        if not text:
            continue
        format_inp = text.replace(" ","")

        interpreter = Interpreter(format_inp)

        result = interpreter.build_and_eval()

        print(result)

if __name__=='__main__':
    main()