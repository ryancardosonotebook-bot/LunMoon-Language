import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def compile_and_execute(filename):
    with open(filename, 'r') as file:
        code = file.read()
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        interpreter.execute()