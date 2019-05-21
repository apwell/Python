INTEGER, PLUS, EOF = "INTEGER", "PLUS", "EOF"

class Token(object):
    def __init__(self,type,value):
        # type = INTEGER, PLUS, or EOF
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return "Token({type},{value})".format(type = self.type,value = self.value)

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self,text):
        # client string input EX: 3+5
        self.text = text
        # index for self.text
        self.pos = 0
        # current token
        self.current_token = None

    def error(self):
        raise Exception("Error Parsing")

    def get_next_token(self):
        text = self.text
        if self.pos > len(self.text) - 1:
            return Token(EOF,None)
        # get current character
        current_char = text[self.pos]
        if current_char.isdigit():
            token = Token(INTEGER,int(current_char))
            self.pos +=1
            return token
        if current_char == '+':
            token = Token(PLUS,current_char)
            self.pos +=1
            return token
        self.error()

    def eat(self,token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.

        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()
        # expecting single digit operand
        left = self.current_token
        self.eat(INTEGER)
        # expecting PLUS
        op = self.current_token
        self.eat(PLUS)
        # expecting single digit operand
        right = self.current_token
        self.eat(INTEGER)
        #should be at E0F now
        result = left.value + right.value
        return result

def main():
    while True:
        try:
            text = raw_input("calc> ")
        except EOFError:
            break

        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
