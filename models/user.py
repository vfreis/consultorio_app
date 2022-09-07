class Usuario:
    def __init__(self, nome, dt_nasc, email, celular, telefone, sexo, cpf, senha):
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.email = email
        self.celular = celular
        self.telefone = telefone
        self.sexo = sexo
        self.cpf = cpf
        self.senha = senha
    def __repr__(self):
        return f'<nome: {self.nome}>'