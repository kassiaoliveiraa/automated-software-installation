
# Gerador de Senhas e Instalador de Software

Este repositório contém scripts para duas funcionalidades principais: **geração de senhas aleatórias** e **instalação automatizada de software**. Dependendo do sistema operacional que você estiver utilizando, escolha o script adequado.

## Scripts Disponíveis

### 1. **Gerador de Senhas**

1. **generate_password.bat** (Windows):
   - Script em Batch que gera uma senha aleatória de 14 caracteres e salva no arquivo `password.txt`.
   - Compatível com o Windows.
   - Executa um comando PowerShell internamente para gerar a senha.
   
2. **generate_password.sh** (Linux/macOS):
   - Script em Shell que gera uma senha aleatória de 14 caracteres e salva no arquivo `password.txt`.
   - Compatível com Linux e macOS.
   - Utiliza Bash para gerar a senha de acordo com um conjunto de caracteres pré-definido.

### 2. **Instalador de Software**

1. **install_software.bat** (Windows):
   - Script em Batch que automatiza a instalação de várias linguagens de programação, frameworks, IDEs, máquinas virtuais, ferramentas, editores e utilitários utilizando o `winget`.
   - O script instala os seguintes softwares:
     - **Linguagens e Frameworks**: Java (JDK 19), Python 3.9, Groovy 4
     - **Máquinas Virtuais**: VirtualBox
     - **IDEs**: IntelliJ IDEA Community Edition, PyCharm Community Edition
     - **Ferramentas e Editores**: Windows Terminal, Git, Notepad++, Visual Studio Code, DBeaver, Postman, Utilso
     - **Utilitários**: Discord, Steam, Epic Games Launcher, Spotify, iCloud, Google Chrome, WhatsApp, MoveMouse, WinZip
   
2. **install_software.sh** (Linux/macOS):
   - Similar ao script do Windows, mas adaptado para sistemas baseados em Unix. Utiliza o gerenciador de pacotes apropriado para instalar os softwares equivalentes em Linux/macOS (necessário configurar as ferramentas adequadas para cada ambiente).

## Como Usar

### Gerador de Senhas

#### No Windows

1. Certifique-se de que você possui o **PowerShell** instalado (padrão no Windows 7 e superior).
2. Execute o script `generate_password.bat`:

   ```bash
   generate_password.bat
   ```

3. Após a execução, a senha será gerada e salva no arquivo `password.txt` na mesma pasta.

#### No Linux/macOS

1. Garanta que você tem permissão para executar scripts de shell.
2. Dê permissão de execução ao script:

   ```bash
   chmod +x generate_password.sh
   ```

3. Execute o script:

   ```bash
   ./generate_password.sh
   ```

4. A senha será gerada e salva no arquivo `password.txt` na mesma pasta.

### Instalador de Software

#### No Windows

1. Garanta que o `winget` está instalado no seu sistema (disponível a partir do Windows 10).
2. Execute o script `install_software.bat`:

   ```bash
   install_software.bat
   ```

3. O script instalará automaticamente os softwares listados acima.

#### No Linux/macOS

1. Dê permissão de execução ao script:

   ```bash
   chmod +x install_software.sh
   ```

2. Execute o script:

   ```bash
   ./install_software.sh
   ```

3. O script instalará os softwares correspondentes (necessário configurar os pacotes e ferramentas adequados para o seu sistema).

## Observações

- Ambos os scripts de geração de senha geram senhas de 14 caracteres utilizando letras maiúsculas, minúsculas, números e símbolos.
- O arquivo `password.txt` será sobrescrito toda vez que o script de geração de senha for executado.
- Os scripts de instalação no Linux/macOS podem precisar de ajustes adicionais para gerenciar pacotes específicos de acordo com a distribuição ou preferências do usuário.
