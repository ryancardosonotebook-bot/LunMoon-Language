class Interpreter:
    def __init__(self):
        self.variables = {}

    def execute_node(self, node):
        if isinstance(node, Assignment):
            self.execute_assignment(node)
        elif isinstance(node, IfStatement):
            self.execute_if(node)
        elif isinstance(node, WhileLoop):
            self.execute_while(node)
        elif isinstance(node, ForLoop):
            self.execute_for(node)
        elif isinstance(node, FunctionDef):
            self.execute_function_def(node)
        elif isinstance(node, FunctionCall):
            return self.execute_function_call(node)
        elif isinstance(node, PrintStatement):
            self.execute_print(node)
        elif isinstance(node, ReturnStatement):
            return self.execute_return(node)

    def execute_assignment(self, node):
        var_name = node.variable
        value = self.evaluate_expression(node.value)
        self.set_variable(var_name, value)

    def execute_if(self, node):
        if self.evaluate_expression(node.condition):
            for statement in node.true_statements:
                self.execute_node(statement)
        else:
            for statement in node.false_statements:
                self.execute_node(statement)

    def execute_while(self, node):
        while self.evaluate_expression(node.condition):
            for statement in node.body:
                self.execute_node(statement)

    def execute_for(self, node):
        iterable = self.evaluate_expression(node.iterable)
        for item in iterable:
            self.set_variable(node.loop_variable, item)
            for statement in node.body:
                self.execute_node(statement)

    def execute_function_def(self, node):
        self.set_variable(node.name, node)

    def execute_function_call(self, node):
        func = self.get_variable(node.function_name)
        args = [self.evaluate_expression(arg) for arg in node.arguments]
        return func.execute(args)

    def execute_print(self, node):
        value = self.evaluate_expression(node.value)
        print(value)

    def execute_return(self, node):
        return self.evaluate_expression(node.value)

    def evaluate_expression(self, expr):
        # Implementation for evaluating expressions based on the AST node
        pass

    def get_variable(self, name):
        return self.variables.get(name)

    def set_variable(self, name, value):
        self.variables[name] = value
