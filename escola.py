from aluno import Aluno

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def cadastrarAluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def editarAluno(self, aluno: Aluno):
        for alu in self.alunos:
            if alu.matricula == aluno.matricula:
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

if __name__ == "__main__":
    escola = Escola("Infinity School")
    a1 = Aluno("Jonas", 19, "Python", 10)
    a2 = Aluno("Isaac", 22, "JavaScript", 10)
    escola.cadastrarAluno(a1)
    escola.cadastrarAluno(a2)
    print(escola.listarAluno())
    a1.nome = "Jonas Lopes"
    escola.editarAluno(a1)
    print(escola.listarAluno())
    escola.removerAluno(a1.matricula)
    print(escola.listarAluno())
