from datetime import datetime, timedelta
from biblioteca import Usuario, Cartucho, CartuchoIndisponivelError, LimiteEmprestimosExcedidoError, LocadoraError

def main():
    print("🎮 Bem-vindo à Locadora Retrô Games 🎮\n")

    # ======================
    # CATALOGO DE CARTUCHOS
    # ======================
    catalogo = [
        Cartucho("Super Mario World", "Super Nintendo", "Nintendo", "SNES-001"),
        Cartucho("The Legend of Zelda: A Link to the Past", "Super Nintendo", "Nintendo", "SNES-002"),
        Cartucho("Street Fighter II", "Super Nintendo", "Capcom", "SNES-003"),
        Cartucho("Donkey Kong Country", "Super Nintendo", "Rare/Nintendo", "SNES-004"),
        Cartucho("F-Zero", "Super Nintendo", "Nintendo", "SNES-005"),

        Cartucho("Sonic the Hedgehog", "Mega Drive", "Sega", "MD-001"),
        Cartucho("Streets of Rage 2", "Mega Drive", "Sega", "MD-002"),
        Cartucho("Golden Axe", "Mega Drive", "Sega", "MD-003"),
        Cartucho("Mortal Kombat II", "Mega Drive", "Midway", "MD-004"),
        Cartucho("Altered Beast", "Mega Drive", "Sega", "MD-005"),

        Cartucho("Super Mario Bros 3", "NES", "Nintendo", "NES-001"),
        Cartucho("Metroid", "NES", "Nintendo", "NES-002"),
        Cartucho("Castlevania", "NES", "Konami", "NES-003"),
        Cartucho("Excitebike", "NES", "Nintendo", "NES-004"),
        Cartucho("Mega Man 2", "NES", "Capcom", "NES-005"),

        Cartucho("Pac-Man", "Atari 2600", "Namco", "AT-001"),
        Cartucho("Pitfall!", "Atari 2600", "Activision", "AT-002"),
        Cartucho("Space Invaders", "Atari 2600", "Taito", "AT-003"),
        Cartucho("Asteroids", "Atari 2600", "Atari", "AT-004"),
        Cartucho("Centipede", "Atari 2600", "Atari", "AT-005"),
    ]

    # ======================
    # USUÁRIOS
    # ======================
    usuario = Usuario("Samuel", 101)

    print("\n🎮 --- TESTE DE LOCAÇÃO ---")
    try:
        print(usuario.alugar_cartucho(catalogo[0]))
        print(usuario.alugar_cartucho(catalogo[5]))
        print(usuario.alugar_cartucho(catalogo[10]))
        print(usuario.alugar_cartucho(catalogo[15]))  # deve dar erro (limite)
    except (CartuchoIndisponivelError, LimiteEmprestimosExcedidoError, LocadoraError) as e:
        print(f"⚠️ Erro: {e}")

    try:
        print(usuario.devolver_cartucho(catalogo[0]))
    except LocadoraError as e:
        print(f"⚠️ Erro: {e}")

    print("\n--- STATUS FINAL ---")
    for cartucho in catalogo:
        status = "✅" if cartucho.disponivel else "❌"
        print(f"{status} {cartucho}")

    print(f"\nUsuário: {usuario.nome} | Cartuchos alugados: {len(usuario.cartuchos_alugados)}")

    # -------------------------------------------------------------------
    # 🧪 TESTE DE MULTA USANDO DATETIME
    # -------------------------------------------------------------------

    print("\n💰 --- TESTE DE MULTA COM ATRASO ---")

    # Pegar um novo cartucho para simular multa
    cartucho_teste = Cartucho("Donkey Kong Country", "Super Nintendo", "Rare/Nintendo", "SNES-004")
    usuario_teste = Usuario("TesteMulta", 202)

    # Aluga o cartucho
    usuario_teste.alugar_cartucho(cartucho_teste)
    print(f"{usuario_teste.nome} alugou {cartucho_teste.titulo} em {cartucho_teste.data_emprestimo.strftime('%d/%m/%Y %H:%M:%S')}")

    # Simula que o cartucho foi alugado há 8 dias (3 dias de atraso)
    cartucho_teste.data_emprestimo = datetime.now() - timedelta(days=8)

    # Devolve e calcula multa
    multa = cartucho_teste.devolver()
    print(f"Multa calculada: R$ {multa:.2f}")

    # -------------------------------------------------------------------
    # 🧩 TESTE EXTRA 1 – Tentar alugar jogo indisponível
    # -------------------------------------------------------------------
    print("\n🚫 --- TESTE: ALUGAR JOGO INDISPONÍVEL ---")
    usuario_a = Usuario("Carlos", 303)
    usuario_b = Usuario("Lucas", 404)

    usuario_a.alugar_cartucho(catalogo[2])
    try:
        usuario_b.alugar_cartucho(catalogo[2])  # já alugado
    except CartuchoIndisponivelError as e:
        print(f"⚠️ Erro capturado corretamente: {e}")

    # -------------------------------------------------------------------
    # 🧩 TESTE EXTRA 2 – Tentar devolver jogo não emprestado
    # -------------------------------------------------------------------
    print("\n🚫 --- TESTE: DEVOLVER JOGO NÃO EMPRESTADO ---")
    usuario_c = Usuario("Rafa", 505)
    try:
        usuario_c.devolver_cartucho(catalogo[3])  # nunca foi alugado
    except LocadoraError as e:
        print(f"⚠️ Erro capturado corretamente: {e}")

    print("\n✅ Todos os testes foram executados com sucesso!")

if __name__ == "__main__":
    main()
