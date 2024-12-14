Descrição
Você foi encarregado de criar um sistema simples que verifica a integridade de arquivos, comparando o hash 
fornecido pelo usuário com o hash real do arquivo. Na função verificar_hashes que irá receber uma lista de 
hashes e compará-los com os valores esperados para cada arquivo. Seu objetivo é verificar se o hash calculado 
é igual ao hash esperado.

Entrada
Uma lista de pares de hashes (hash calculado e hash esperado), separados por vírgulas, e cada par separado 
por ponto e vírgula.

Saída
Para cada par de hashes fornecido, o código imprime o resultado "Correto" ou "Inválido".

def verificar_hashes(lista_hashes):
    for hash_comparacao in lista_hashes:
        # Remove espaços extras ao redor dos hashes e divide em 'hash_calculado' e 'hash_esperado'
        hash_calculado, hash_esperado = hash_comparacao.split(",")
        
        # Remove espaços extras que podem existir após a vírgula
        hash_calculado = hash_calculado.strip()
        hash_esperado = hash_esperado.strip()
        
        # Compara os hashes e imprime o resultado
        if hash_calculado == hash_esperado:
            print("Correto")
        else:
            print("Inválido")
        
# Lê a entrada do usuário
hashes_usuario = input()

# Divide a entrada por ponto e vírgula para criar a lista de hashes
lista_hashes = hashes_usuario.split(";")

# Chama a função para verificar os hashes
verificar_hashes(lista_hashes)

