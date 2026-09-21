from netmiko import ConnectHandler

# Inventário centralizado de dispositivos
inventario_redes = [
    {
        'device_type': 'cisco_ios',
        'host': '192.168.1.1',
        'username': 'admin',
        'password': 'password123',
        'port': 22,
    },
]

# Bloco de comandos de configuração a aplicar em massa
comandos_configuracao = [
    "line vty 0 4",
    "transport input ssh",
    "exec-timeout 15 0"
]

def aplicar_configuracoes_massa():
    print("[*] A iniciar rotina de alteração e configuração em massa...")
    
    for dispositivo in inventario_redes:
        host = dispositivo['host']
        print(f"\n--------------------------------------------------")
        print(f"[*] A estabelecer ligação SSH com {host} para alteração...")
        
        try:
            with ConnectHandler(**dispositivo) as net_connect:
                print(f"[+] Ligação estabelecida com sucesso a {host}!")
                
                # Envia o bloco de comandos de configuração de forma segura
                print(f"[*] A aplicar políticas de configuração em {host}...")
                output_config = net_connect.send_config_set(comandos_configuracao)
                print(output_config)
                
                # Opcional: Executa um comando de gravação (write memory)
                output_save = net_connect.send_command("write memory")
                print("[+] Configuração gravada permanentemente na NVRAM do equipamento.")
                
                # Recolhe o running-config atualizado para fins de auditoria
                config_atualizada = net_connect.send_command("show running-config")
                nome_ficheiro = f"config_auditada_{host.replace('.', '_')}.txt"
                
                with open(nome_ficheiro, "w", encoding="utf-8") as f:
                    f.write(config_atualizada)
                    
                print(f"[+] Auditoria pós-alteração salva com sucesso em: {nome_ficheiro}")

        except Exception as erro:
            print(f"[!] Erro ao atualizar o dispositivo {host}: {erro}")
            
    print("\n--------------------------------------------------")
    print("[*] Rotina de alteração em massa concluída.")

if __name__ == "__main__":
    aplicar_configuracoes_massa()