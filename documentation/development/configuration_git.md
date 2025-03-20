# Configuração do Git para o Projeto

Este guia fornece os passos recomendados para configurar o Git adequadamente no projeto, seguindo boas práticas de desenvolvimento pleno.

---

## 1. Configuração Inicial

Defina suas credenciais globais:

Isso garante que todos os commits realizados sejam corretamente atribuídos ao seu usuário.

### Melhorando a Visualização dos Logs

Para facilitar a análise do histórico de commits, configure um alias para exibir logs simplificados:

Agora, em vez de executar `git log`, você pode simplesmente usar:

### Evitando Commits Duplicados no Pull

Configure a opção de pull com rebase para evitar problemas ao sincronizar código:

Verifique todas as configurações aplicadas:

Isso listará todas as configurações globais do Git para seu usuário.

---

## 2. Configuração do Repositório

1. Clone o repositório do projeto:

2) Navegue até o diretório do projeto:

3. Configure o repositório remoto:

4) Defina a branch principal como `main`:

5. Envie a branch `main` para o repositório remoto:

6) Verifique se a conexão com o repositório remoto está funcionando corretamente:

7. Confirme o status do repositório local:

Isso ajuda a garantir que o diretório local está sincronizado com o repositório remoto.

---

## 3. Configurar Gitignore

Crie um arquivo `.gitignore` na raiz do projeto para evitar o versionamento de arquivos desnecessários:

~~~bash
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg
.eggs/

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Pycharm project files
.idea/

# PyTest cache
.pytest_cache/

# Coverage
.coverage
coverage.xml

# Tox
.tox/
.cache/
.python-version

# VirtualEnv
.venv/

# Developers
*.sw*
manage.py
.DS_Store

# example database
drf_example
~~~

Para verificar se um arquivo está sendo ignorado corretamente:

Se um arquivo que deveria ser ignorado ainda aparece no `git status`, pode ser necessário removê-lo manualmente do repositório:

---

## 4. Gerenciamento de Branches

### Criando uma Nova Branch

Para criar e mudar para uma nova branch:

Para listar todas as branches disponíveis:

### Publicando a Branch no Repositório Remoto

Isso cria a branch no repositório remoto e a configura para rastreamento automático.

### Atualizando a Branch com Alterações da `main`

Antes de enviar um Pull Request, é recomendado atualizar a branch com as últimas mudanças da `main`:

Isso evita conflitos futuros no código.

### Renomeando e Excluindo Branches

Para renomear uma branch localmente:

Para excluir uma branch localmente:

Para excluir uma branch remotamente:

---

## 5. Boas Práticas de Commits

- Escreva mensagens de commit curtas e descritivas.
- Utilize a convenção de commits semânticos:
  - `feat:` para novas funcionalidades.
  - `fix:` para correções de bugs.
  - `docs:` para alterações em documentação.
  - `style:` para ajustes de formatação sem impacto no código.
  - `refactor:` para refatoração de código sem mudança na lógica.
  - `test:` para inclusão ou ajuste de testes.

Exemplo de commit bem formatado:

### Corrigindo o Último Commit

Se precisar modificar a mensagem do último commit (e ele ainda não foi enviado para o repositório remoto):

Se já enviou o commit, evite usar `--amend` pois pode causar conflitos.

---

## Conclusão

Seguindo essas práticas, você manterá um histórico de commits limpo, colaborativo e fácil de gerenciar. Para dúvidas adicionais, consulte a [documentação oficial do Git](https://git-scm.com/doc).

