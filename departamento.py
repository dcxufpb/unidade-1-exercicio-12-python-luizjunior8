
class Departamento:

    def __init__(self, nome, sigla, localizacao, coordenador):
        self.nome = nome
        self.sigla = sigla
        self.localizacao = localizacao
        self.coordenador = coordenador

    def validar_campos_obrigatorios(self):

        if not self.nome:
            raise Exception("O campo nome do departamento é obrigatório")

        if not self.localizacao:
            raise Exception("O campo localização do departamento é obrigatório")   

    def dados_departamento(self):

        self.validar_campos_obrigatorios()

        nomeDep = self.sigla and self.nome + ", " or self.nome

        siglaDep = self.sigla and self.sigla or ""

        localDep = "End.: " + self.localizacao

        return (f"""{nomeDep}{siglaDep}
{localDep}
{self.coordenador.dados_coordenador()}""")


class Coordenador:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def validar_campos_obrigatorios(self):

        if not self.nome:
            raise Exception("O nome do coordenador é obrigatório")

        if not self.cpf:
            raise Exception("O cpf do coordenador é obrigatório")

    def dados_coordenador(self):

        self.validar_campos_obrigatorios()

        idadeCord = self.idade and (f"\n{self.idade} anos") or ""

        cpfCord = "CPF: " + self.cpf

        return (f"""{self.nome}{idadeCord}
{cpfCord}""")