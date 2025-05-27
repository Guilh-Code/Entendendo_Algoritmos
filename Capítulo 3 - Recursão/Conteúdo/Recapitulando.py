'''
📘 Capítulo 3 – Recursão

🔁 O que é recursão?
Recursão é uma técnica onde uma função chama a si mesma para resolver um problema.

É especialmente útil para problemas que podem ser divididos em subproblemas menores e semelhantes.
Bookey


🧩 Componentes principais
Caso base: A condição que encerra a recursão.

Chamada recursiva: A parte onde a função se chama novamente com uma entrada modificada.


📌 Exemplo: Fatorial

def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)
Neste exemplo, fat(3) calcula 3 * fat(2), que é 3 * 2 * fat(1), resultando em 3 * 2 * 1 = 6.


🧠 Pilha de chamadas
Cada chamada de função é armazenada em uma pilha até atingir o caso base.

Após o caso base ser alcançado, as chamadas são resolvidas em ordem inversa (LIFO - Last In, First Out).


⚠️ Cuidados
Certifique-se de que o caso base seja alcançado para evitar recursões infinitas.

Recursões profundas podem levar a estouros de pilha; considere a profundidade máxima permitida pela linguagem.

'''