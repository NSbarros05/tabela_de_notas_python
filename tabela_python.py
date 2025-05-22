from tabulate import tabulate

listaNotas = []

print("Bem-vindo!")
print("\nVamos adicionar notas em uma lista para você")

while True:
    try:
        nota = float(input(f"\nDigite a nota {len(listaNotas) + 1}: "))
        if 0 <= nota <= 10:
            listaNotas.append(nota)
        else:
            print("Por favor, digite uma nota entre 0 e 10.")
            continue
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")
        continue

    respContinua = input("\nGostaria de continuar? (s/n): ").lower()
    while respContinua not in ['s', 'n']:
        print("Por favor, digite 's/S' para sim ou 'n/N' para não.")
        respContinua = input("\nGostaria de continuar? (s/n): ").lower()

    if respContinua == 'n':
        print("\nLista fechada!")
        break

if listaNotas:
    tabela = [[i + 1, nota] for i, nota in enumerate(listaNotas)]
    
    print("\n=== Lista de Notas ===")
    print(tabulate(tabela, headers=["Índice", "Nota"], tablefmt="grid", floatfmt=".1f"))
    
    totalNotas = sum(listaNotas)
    mediaNotas = totalNotas / len(listaNotas)
    
    print("\n=== Estatísticas ===")
    print(f"Quantidade de notas: {len(listaNotas)}")
    print(f"Soma das notas: {totalNotas:.1f}")
    print(f"Média das notas: {mediaNotas:.1f}")
    print(f"Maior nota: {max(listaNotas):.1f}")
    print(f"Menor nota: {min(listaNotas):.1f}")
    print("=====================")
else:
    print("\nNenhuma nota foi adicionada.")

input('\nPrecione Enter para fechar a janela...')