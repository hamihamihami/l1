from sly import Lexer
class CLexer(Lexer):
    tokens={ID,NUMBER,INT,PRINT}
    literals={'+','*','-','/','=','(',')',';','{','}',','}
    ignore=' \t\n'
    ID=r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['print']=PRINT
    ID['int']=INT
    NUMBER=r'[0-9]+'
    def error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        self.index += 1
