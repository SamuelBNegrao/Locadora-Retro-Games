# Executar testes
#pytest test_biblioteca.py -v

import pytest
from biblioteca import Item, Usuario, LimiteEmprestimosExcedidoError, ItemIndisponivelError

def test_item_alugar_e_devolver():
    item = Item("FIFA 25", "Jogo", "001")
    usuario = Usuario("Samuel", 1)

    usuario.alugar_item(item)
    assert not item.disponivel

    usuario.devolver_item(item)
    assert item.disponivel

def test_limite_excedido():
    usuario = Usuario("Teste", 2)
    itens = [Item(f"Item{i}", "Categoria", str(i)) for i in range(4)]

    for i in range(3):
        usuario.alugar_item(itens[i])

    with pytest.raises(LimiteEmprestimosExcedidoError):
        usuario.alugar_item(itens[3])
