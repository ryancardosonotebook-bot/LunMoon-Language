class ASTNode:
    """A node in the abstract syntax tree."""
    def __init__(self, node_type, children=None):
        self.node_type = node_type
        self.children = children if children is not None else []

    def __repr__(self):
        return f"<ASTNode type='{self.node_type}' children={self.children}>"

class Parser:
    """Parses tokens into an abstract syntax tree (AST)."""
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        """Starts the parsing process and returns the root of the AST."""
        return self.program()

    def program(self):
        """Parses a program, which consists of multiple statements."""
        nodes = []
        while self.current_token_index < len(self.tokens):
            nodes.append(self.statement())
        return ASTNode('program', nodes)

    def statement(self):
        """Parses a single statement."""
        # Simple demonstration of statement parsing logic
        node = ASTNode('statement', [self.current_token()])
        self.next_token()  # Move to the next token
        return node

    def current_token(self):
        """Returns the current token."""
        return self.tokens[self.current_token_index]

    def next_token(self):
        """Advances to the next token."""
        self.current_token_index += 1

# Example usage:
# tokens = ['TOKEN1', 'TOKEN2', 'TOKEN3']
# parser = Parser(tokens)
# ast = parser.parse()
# print(ast)