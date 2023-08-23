from sly import Parser
from level1lexer import CLexer

class CParser(Parser):
    tokens = CLexer.tokens
    literals=CLexer.literals

    def __init__(self):
        self.valid = True
        super().__init__()

    @_('return_type identifier "(" ")" "{" statements "}"')
    def program(self, p):
        return p.return_type, p.identifier, p.statements
    
    @_('INT')
    def return_type(self, p):
        return p.INT
    
    @_('statement ";" statements', 'statement ";"')
    def statements(self, p):
        return [p.statement ]+ p.statements if len(p) == 3 else [p.statement]
    
    @_('declaration_stmt', 'assignment_stmt', 'print_stmt')
    def statement(self, p):
        return p[0]
    
    @_('type list_of_variables')
    def declaration_stmt(self, p):
        return ('declaration', p.type, p.list_of_variables)
    
    @_('identifier "=" identifier', 'identifier "=" constant')
    def assignment_stmt(self, p):
        print()
        return ('assignment', p.identifier, p[2])
    
    @_('PRINT identifier')
    def print_stmt(self, p):
        return ('print', p.identifier)
    
    @_('INT')
    def type(self, p):
        return 'int'
    
    @_('identifier "," list_of_variables', 'identifier')
    def list_of_variables(self, p):
        res=list()
        if len(p) == 3:
            res.append(p.identifier)
            return res + p.list_of_variables
        else:
            res.append(p.identifier)
            return res
    
    @_('ID')
    def identifier(self, p):
        return p.ID
    
    @_('NUMBER')
    def constant(self, p):
        return p[0]

    def error(self, p):
        self.valid = False
        if p is None:
            print("Syntax error at EOF")
        else:
            print(f"Syntax error at line {p.lineno}, position {p.index}, token=`{p.type}`")

if __name__ == '__main__':
    lexer = CLexer()
    parser = CParser()
    
    code = """
            int main(){

     int a;
     a=30;
     print a;

} 
"""
    tokens = lexer.tokenize(code)
    result = parser.parse(tokens)

    if parser.valid:
        print(result)
        print("The code is Valid") 
    else:
        print("Code is not Valid")

