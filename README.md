# Entregável 1 - Harpia UFRJ

> Miguel Rangel de Magalhães

Programa simplificado que verifique se um robô tem bateria suficiente para realizar uma missão.



Para **instalar** o programa nas distros `Arch` ou `Fedora` siga o procedimento abaixo:

```bash
git clone https://github.com/miguelhahaa/entregavel1-miguelmagalhaes.git && pip install rich
cd entregavel1-miguelmagalhaes/src/missao.py
```

O programa deve ser chamado usando as flags seguidas de um número, a função de cada flag está descrita abaixo:

| comando | descrição          |
| ------- | ------------------ |
| -b      | bateria atual      |
| -d      | duração do voo     |
| -c      | consumo por minuto |

Abaixo está um exemplo de execução:

```bash
python missao.py -b 100 -d 20 -c 2
> === Missão Possível ===
> **barra de bateria restante**
```
