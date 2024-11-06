# 👁️ **ScreenLogger** - Meu Primeiro Projeto

Um **ScreenLogger simples** feito em **Python** que envia **Capturas de Tela** para o seu e-mail.

## 📚 Sobre

Este projeto foi criado para um trabalho escolar e baseado em outros projetos open-source encontrados no GitHub. Foi feito inteiramente para fins educacionais.

## 🔧 Funcionalidades

- **Envio de Capturas de Tela por E-mail**: Capture e envie capturas de tela do seu PC, junto com informações como **Hostname, Sistema, Usuário e IP**.
- **Configurações Personalizáveis**: Altere facilmente o número de capturas por e-mail e o tempo de intervalo entre as capturas.
- **Integração com o Início Automático**: Ao ser convertido em um **executável**, o programa será automaticamente copiado para a **pasta de Inicialização** do Windows.
  
## 🛠️ **Principais Funções**
<img src="https://github.com/user-attachments/assets/54deb6db-15dd-4f27-bb21-49e410000769" />

- ✅ **Captura de Capturas de Tela**
- ✅ **Recuperação de Hostname**
- ✅ **Informações do Usuário**
- ✅ **Endereço IP**
- ✅ **Integração com a Inicialização Automática**

## ⚙️ **Configurações Padrão**

- `count = 20`: Número de capturas por e-mail (padrão: 20 capturas).
- `time.sleep(1)`: Tempo de intervalo entre cada captura (padrão: 1 segundo).

## 🛡️ **Testes de Antivírus**

![Teste Antivirus 1](https://github.com/user-attachments/assets/9bddf949-9f72-4810-b819-be4c866aee9e)  
![Teste Antivirus 2](https://github.com/user-attachments/assets/e5bb72a7-e698-4806-9774-933af345e2e6)

## 💾 **Como Criar o Executável (EXE)**

Caso queira rodar o **ScreenLogger** como um arquivo executável, utilize a biblioteca [AutoPyToExe](https://pypi.org/project/auto-py-to-exe/).

Após obter o arquivo **.exe**, altere a variável `(originalfilename)` para o nome do seu arquivo executável. Isso, juntamente com outras modificações, como a variável `(copiedfilename)`, garantirá que o arquivo seja copiado para a **pasta de Inicialização** do Windows, fazendo com que ele seja executado na inicialização.

## 👨‍💻 **Créditos**

Este projeto é baseado em contribuições de outros projetos open-source. Se você for o criador original de algum código utilizado, entre em contato para o devido reconhecimento.
