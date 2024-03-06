from aluno import Aluno

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def cadastrarAluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def editarAluno(self, aluno: Aluno):
        for alu in self.alunos:
            if str(alu.matricula) == str(aluno.matricula):
                alu.nome = aluno.nome
                alu.idade = aluno.idade
                alu.curso = aluno.curso
                alu.nota = aluno.nota
                return True
        return False

    def removerAluno(self, matricula: str):
        for aluno in self.alunos:
            if str(aluno.matricula) == matricula:
                self.alunos.remove(aluno)
                return True
        return False

    def listarAluno(self):
        return self.alunos
