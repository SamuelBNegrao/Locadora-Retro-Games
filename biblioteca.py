# locadora.py
from datetime import datetime

# EXCEÇÕES
class LocadoraError(Exception):
    pass

class LimiteEmprestimosExcedidoError(LocadoraError):
    pass

class CartuchoIndisponivelError(LocadoraError):
    pass


# CLASSE CARTUCHO
class Cartucho:
    def __init__(self, titulo: str, plataforma: str, fabricante: str, codigo: str):
        self.titulo = titulo
        self.plataforma = plataforma
        self.fabricante = fabricante
        self.codigo = codigo
        self.disponivel = True
        self.data_emprestimo = None

    def alugar(self):
        if not self.disponivel:
            raise CartuchoIndisponivelError(f"O cartucho '{self.titulo}' já está alugado.")
        self.disponivel = False
        self.data_emprestimo = datetime.now()

    def devolver(self):
        if self.disponivel:
            raise LocadoraError(f"O cartucho '{self.titulo}' já foi devolvido.")
        self.disponivel = True
        return self.calcular_multa()

    def calcular_multa(self):
        if self.data_emprestimo:
            dias = (datetime.now() - self.data_emprestimo).days
            if dias > 5:
                return (dias - 5) * 1.0
        return 0.0

    def __str__(self):
        status = "Disponível" if self.disponivel else "Alugado"
        return f"{self.titulo} ({self.plataforma}) - {self.fabricante} - {status}"


# CLASSE USUARIO
class Usuario:
    def __init__(self, nome: str, id_usuario: int):
        self.nome = nome
        self.id_usuario = id_usuario
        self.cartuchos_alugados = []

    def alugar_cartucho(self, cartucho: Cartucho):
        if len(self.cartuchos_alugados) >= 3:
            raise LimiteEmprestimosExcedidoError(f"{self.nome} atingiu o limite de 3 cartuchos alugados.")
        cartucho.alugar()
        self.cartuchos_alugados.append(cartucho)
        return f"{self.nome} alugou '{cartucho.titulo}' com sucesso!"

    def devolver_cartucho(self, cartucho: Cartucho):
        if cartucho not in self.cartuchos_alugados:
            raise LocadoraError(f"O cartucho '{cartucho.titulo}' não foi alugado por {self.nome}.")
        multa = cartucho.devolver()
        self.cartuchos_alugados.remove(cartucho)
        if multa > 0:
            return f"Cartucho devolvido com multa de R$ {multa:.2f}"
        return "Cartucho devolvido dentro do prazo."

    def __str__(self):
        return f"Usuário: {self.nome} | Cartuchos alugados: {len(self.cartuchos_alugados)}"
