# Documentação do repositório

1. O código executa **três funções simultaneamente** usando *threads*:

   * Verifica se um número é **par ou ímpar**
   * Verifica se um número é **primo**
   * Valida um **CPF**

## Objetivo

Praticar o uso de **threads em Python**, permitindo que várias funções rodem ao mesmo tempo, sem precisar esperar uma terminar para começar outra.

## Passos realizados

1. Criei o arquivo `threads_funcoes.py`.
2. Implementei três funções principais:

   * `par_ou_impar()` → verifica se o número digitado é par ou ímpar.
   * `primo()` → verifica se o número digitado é primo ou não.
   * `validar_cpf()` → confere se o CPF informado é válido seguindo as regras dos dígitos verificadores.
3. Criei três *threads*:

   * `t1 = threading.Thread(target=par_ou_impar)`
   * `t2 = threading.Thread(target=primo)`
   * `t3 = threading.Thread(target=validar_cpf)`
4. Iniciei as *threads* com:

   * `t1.start()`, `t2.start()`, `t3.start()`
5. Aguardei todas terminarem com:

   * `t1.join()`, `t2.join()`, `t3.join()`

## Explicação técnica

* **Thread**: permite executar várias partes do código ao mesmo tempo.
* `threading.Thread(target=funcao)` → cria uma nova *thread* para rodar a função.
* `start()` → inicia a execução.
* `join()` → faz o programa principal esperar o fim de cada *thread*.

## Dificuldades

1. Entender o funcionamento de *threads* simultâneas e como cada função pode rodar ao mesmo tempo.
2. Tratar a entrada do usuário quando várias *threads* pedem dados simultaneamente (pode causar confusão no console).

---

Quer que eu adicione uma seção **"Resultado esperado"** (mostrando o que aparece no terminal quando o código roda)? Isso deixaria sua documentação mais completa.
