Sistema RH Center 🖥️

 ![exemplo](https://github.com/user-attachments/assets/ee21af5c-ae13-4559-959b-ea2627ab509f)

O RH Center é uma aplicação de linha de comando desenvolvida em Python para facilitar o gerenciamento de funcionários em pequenas empresas.
O sistema permite o cadastro de novos colaboradores, a persistência de dados em arquivos CSV e a geração de relatórios estatísticos.

🚀 Funcionalidades
- Cadastro de Funcionários: Registro de nome, idade e salário bruto com validação de dados em tempo real.
- Armazenamento Persistente: Utiliza arquivos CSV para garantir que os dados não sejam perdidos ao fechar o programa.
- Relatórios Estatísticos:
- Cálculo de média salarial da empresa.
- Identificação do funcionário com o maior salário.
- Contagem total de colaboradores cadastrados.
- Interface Amigável: Menu interativo com sistema de limpeza de tela automático para Windows e Linux.

🛠️ Tecnologias Utilizadas
Python 3.12+

- Módulo os: Para manipulação de sistema e caminhos de arquivos.
- Módulo csv: Para leitura e escrita de dados estruturados.
- Módulo time: Para controle de fluxo e UX (pausas em mensagens de erro).

📋 Como Executar o Projeto
Pré-requisitos: Certifique-se de ter o Python instalado em sua máquina.

Clonar o repositório:

Bash
git clone https://github.com/seu-usuario/RH-Center.git
Acessar a pasta:

Bash
cd rh-center
Executar o sistema:

Bash
python rh_center.py

🏗️ Estrutura do Código

O projeto foi construído seguindo boas práticas de modularização, dividindo as responsabilidades em funções específicas:

- ler_funcionarios_csv(): Responsável por carregar os dados do arquivo de disco para a memória.
- cad_funcionarios(): Gerencia o fluxo de entrada de dados e tratamento de exceções (try/except).
- relatorios(): Realiza o processamento lógico e cálculos matemáticos sobre a base de dados.
- main(): Ponto de entrada que gerencia o loop principal e a navegação do usuário.

- 👨‍💻 Autor
Tiago Freitas Formado em Análise e Desenvolvimento de Sistema, Desenvolvedor PYTHON, apaixonado pela lógica, organização de dados e novas tecnologias.

👨‍💻 Sobre o Autor
Tiago - Desenvolvedor em transição de carreira, com sólida experiência prévia de 8 anos como Instrutor de Informática. Atualmente focado em dominar o ecossistema Python, especificamente no desenvolvimento de APIs com FastAPI.
