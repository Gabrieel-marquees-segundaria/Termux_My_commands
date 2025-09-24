No Termux (Android), as variáveis de ambiente funcionam do mesmo jeito que em sistemas Linux normais, mas com alguns detalhes próprios.
Vou te explicar os jeitos principais:


---

🔹 1. Definir variável apenas na sessão atual

Isso só vale até você fechar o Termux.
```

export MINHA_VARIAVEL="teste"
```
Depois pode conferir com:
```
echo $MINHA_VARIAVEL
```
Se fechar o Termux ou abrir outro, ela desaparece.


---

🔹 2. Definir variável de ambiente de forma permanente

No Termux, você precisa colocar o export em arquivos que são carregados toda vez que abre o shell.

Os principais arquivos são:
```
~/.bashrc → se estiver usando bash (padrão em versões antigas).

~/.zshrc → se estiver usando zsh.

~/.profile ou ~/.bash_profile → funciona para login shell.

```
👉 Exemplo para tornar permanente:

echo 'export MINHA_VARIAVEL="teste"' >> ~/.bashrc

Depois, recarregue:
```
source ~/.bashrc
````
Ou simplesmente feche e abra o Termux.


---

🔹 3. Usar o arquivo ~/.termux/termux.properties

Esse arquivo serve para configurações do próprio Termux (atalhos, teclado, etc.), não para variáveis de ambiente do shell.
Então, para variáveis de ambiente, você não usa esse arquivo, só os .bashrc, .zshrc ou .profile.


---

🔹 4. Conferindo todas as variáveis
```
printenv
```
ou
```
env

```
---

👉 Resumindo:

Temporário: export VAR="valor"

Permanente: adicionar no ~/.bashrc, ~/.zshrc ou ~/.profile.



---

Quer que eu te mostre um exemplo prático no Termux definindo uma variável tipo JAVA_HOME ou PYTHONPATH?

