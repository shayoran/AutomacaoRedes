notepad README.md

Markdown
# 🚀 NetDevOps Automation Suite: Cisco IOS & Netmiko

Repositório de engenharia de automação de redes desenvolvido para gerir, auditar e aplicar configurações em infraestruturas Cisco de forma escalável, utilizando **Python** e a biblioteca **Netmiko**.

---

## 🛠️ Arquitetura e Funcionalidades

Este projeto afasta-se dos métodos tradicionais e manuais de administração de redes, implementando as melhores práticas do setor:
- **Gestão de Inventário Dinâmico:** Separação estrita entre a lógica de execução do código e os dados de acesso aos equipamentos (`inventario_redes`).
- **Resiliência e Tratamento de Erros:** Arquitetura multi-dispositivo baseada em ciclos (*loops*) com tratamento cirúrgico de exceções por equipamento (isolamento de falhas de `Timeout` ou `Authentication`, garantindo que o script nunca quebra a meio de uma execução massiva).
- **Parsing Avançado de Dados:** Integração com TextFSM (`use_textfsm=True`) para converter outputs brutos de CLI em estruturas de dados limpas e exportação automática para formato **JSON**.
- **Gestão de Mudança e Auditoria:** Capacidade de efetuar *deployments* de blocos de configuração em massa (`send_config_set`), seguidos de gravação persistente (`write memory`) e auditoria automática do estado pós-alteração (`show running-config`).

---

## 📂 Estrutura do Projeto

```text
AutomacaoRedes/
│
├── venv/                      # Ambiente virtual isolado em Python
├── teste_rede.py              # Script principal de automação e NetDevOps
├── interfaces_estruturadas.json # Exemplo de dados parseados em JSON
└── README.md                  # Documentação oficial do projeto
⚙️ Pré-requisitos e Instalação
Certifica-te de que tens o Python instalado no teu sistema. Recomenda-se a utilização de um ambiente virtual (venv).

Abrir o projeto e ativar o ambiente virtual (Windows PowerShell):

PowerShell
cd C:\Users\Francisco Gomes\AutomacaoRedes
.\venv\Scripts\Activate
Instalar as dependências necessárias:

PowerShell
pip install netmiko ntc-templates
💻 Exemplo de Utilização (teste_rede.py)
O script principal está configurado de forma modular para suportar inventários multi-dispositivo, executar recolhas de diagnóstico estruturadas e aplicar políticas de segurança em massa.

Para executar o script de automação:

PowerShell
python teste_rede.py

👨‍💻 Autor
Desenvolvido por Francisco Gomes no âmbito de projetos avançados de automação de infraestruturas de redes e NetDevOps.
