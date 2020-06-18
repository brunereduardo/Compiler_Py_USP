class PanicMode() :
    def __init__(self):
        self.errors = {}

    def panic_has_errors(self):
        return self.errors

    def add_error(self, analyzer, line, error):
        if self.errors.get(line, None) is None:
            self.errors[line] = []
            
        self.errors[line].append(f"Erro {analyzer} na linha {line}: {error}")