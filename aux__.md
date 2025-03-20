# Configuração do Git para o Projeto

Este guia fornece os passos recomendados para configurar o Git adequadamente no projeto, seguindo boas práticas de desenvolvimento pleno.

---

## 1. Configuração Inicial

Defina suas credenciais globais:
```bash
git config --global user.name "Eugenio"
git config --global user.email "eugeniojosemouraneto092@gmail.com"
```

Configure o editor de texto preferido para mensagens de commit:
```bash
git config --global core.editor "code --wait" # Para VSCode
```

Habilite a exibição de logs de forma simplificada:
```bash
git config --global alias.lg "log --oneline --graph --all --decorate"
```

Configure a opção de pull com rebase para evitar commits duplicados:
```bash
git config --global pull.rebase true
```

Verifique a configuração:
```bash
git config --list
```

---

## 2. Vinculando o Git ao Repositório Remoto

Siga estes passos para vincular seu projeto Git a um repositório remoto:

1. **Inicializar o Repositório (Caso Não Exista)**
Se você ainda não inicializou um repositório Git no seu projeto, use o comando:
```bash
git init
```

2. **Adicionar os Arquivos ao Controle de Versão**
Adicione todos os arquivos do projeto ao controle de versão:
```bash
git add .
```

3. **Fazer o Primeiro Commit**
Crie um commit com uma mensagem descritiva:
```bash
git commit -m "chore: inicialização do projeto"
```

4. **Adicionar o Repositório Remoto**
Vincule o repositório local ao remoto:
```bash
git remote add origin <URL_DO_REPOSITORIO>
```
Para verificar se o repositório remoto foi adicionado corretamente:
```bash
git remote -v
```

5. **Definir a Branch Principal**
Caso a branch principal não esteja definida como `main`, você pode renomeá-la:
```bash
git branch -M main
```

6. **Enviar para o Repositório Remoto**
Envie a branch `main` para o repositório remoto e configure o rastreamento:
```bash
git push -u origin main
```

7. **Verificar o Status**
Certifique-se de que o commit foi enviado corretamente:
```bash
git status
git log
```

---

## 3. Configurar Gitignore

Adicione um arquivo `.gitignore` com as seguintes exclusões comuns:
```
# Logs
logs
*.log

# Node
node_modules/

# Python
__pycache__/
*.py[cod]

# Configs Locais
.env
```

Certifique-se de que o `.gitignore` está funcionando:
```bash
git check-ignore -v nome-do-arquivo
```

---

## Conclusão

Seguindo esses passos, você terá seu projeto vinculado ao repositório remoto e pronto para colaboração. Para dúvidas adicionais, consulte a [documentação oficial do Git](https://git-scm.com/doc).

