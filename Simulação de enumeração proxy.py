Descrição
Desenvolva um sistema que simule a enumeração de serviços em um servidor, dado um conjunto de portas e 
serviços associados. Você deve receber uma lista de números de portas e, para cada porta, retornar o serviço
 associado. Se a porta não estiver no dicionário, retorna "Desconhecido".

Entrada
Uma lista de números de portas separados por vírgula.

Saída
Uma lista de serviços correspondentes a essas portas.

# Dicionário que mapeia números de portas aos serviços correspondentes
port_services = {
    21: "FTP",      # Serviço de transferência de arquivos
    22: "SSH",      # Secure Shell (acesso remoto seguro)
    23: "Telnet",   # Protocolo de acesso remoto inseguro
    25: "SMTP",     # Serviço de envio de emails
    53: "DNS",      # Serviço de tradução de nomes de domínio
    80: "HTTP",     # Protocolo de transferência de hipertexto (web)
    110: "POP3",    # Serviço de recebimento de emails
    143: "IMAP",    # Serviço de recebimento de emails com suporte a pastas
    443: "HTTPS",   # Protocolo seguro de transferência de hipertexto
    3306: "MySQL",  # Banco de dados MySQL
    3389: "RDP",    # Remote Desktop Protocol (Acesso remoto ao Windows)
    5432: "PostgreSQL", # Banco de dados PostgreSQL
    6379: "Redis"   # Banco de dados Redis
}

# Função que realiza a enumeração de serviços
def enumerate_services(ports):
    # Inicializamos uma lista para armazenar os serviços correspondentes
    services = []
    
    # Itera sobre cada porta fornecida
    for port in ports:
        # Verifica se a porta existe no dicionário de serviços
        if port in port_services:
            # Se existir, adiciona o serviço correspondente à lista
            services.append(port_services[port])
        else:
            # Se a porta não estiver mapeada, adiciona "Desconhecido"
            services.append("Desconhecido")
    
    return services

# Função principal que lida com a entrada do usuário e exibe o resultado:
def main():
    # Lê a entrada do usuário (uma string de números de portas separados por vírgula)
    ports_input = input()
    
    # Converte a string de entrada para uma lista de inteiros (números de portas)
    ports = [int(port.strip()) for port in ports_input.split(",")]
    
    # Chama a função de enumeração para obter a lista de serviços correspondentes
    services = enumerate_services(ports)
    
    # Exibe o resultado
    print(services)

# Executa o programa
if __name__ == "__main__":
    main()
