# 🎮 Jogo de Adivinhação

Jogo desenvolvido em Python onde o jogador tenta adivinhar um número secreto entre 1 e 100, com três níveis de dificuldade e diferentes tipos de dicas para ajudar (ou confundir!) durante o jogo.

---

## 📋 Como funciona

O jogo gera um número aleatório entre 1 e 100 e o jogador precisa adivinhar qual é esse número. A cada tentativa errada, uma dica é fornecida dependendo da dificuldade escolhida. O jogador perde se esgotar todas as tentativas sem acertar.

---

## ⚙️ Dificuldades

### 😊 Fácil — 15 tentativas
- Dicas diretas informando se o número secreto é maior ou menor que o chute

### 😐 Normal — 10 tentativas
- A cada tentativa as dicas são sorteadas aleatoriamente entre dica normal e enigma
- Quanto mais próximo do número secreto, mais reveladora a dica

### 💀 Difícil — 5 tentativas
- Dicas apenas em forma de enigma
- Faixas de distância mais amplas, dificultando a dedução
- Quando muito longe do número secreto, o silêncio é sua única resposta

---

## 🎯 Regras

- Digite um número entre 1 e 100
- A cada tentativa errada você recebe uma dica
- Acerte antes de esgotar as tentativas para vencer
- Se esgotar as tentativas sem acertar, o número secreto é revelado

---

## 💡 Sistema de dicas

### Fácil
| Situação | Dica |
|----------|------|
| Número maior | "O número secreto é maior!" |
| Número menor | "O número secreto é menor!" |

### Normal
| Situação | Tipo |
|----------|------|
| Próximo | Enigma |
| Maior | Sorteado entre normal e enigma |
| Menor | Sorteado entre normal e enigma |

### Difícil
| Distância | Dica |
|-----------|------|
| <= 5 | Muito próximo |
| <= 20 | Próximo |
| <= 40 | Médio |
| <= 60 | Longe |
| > 60 | Silêncio |

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

---

## ▶️ Como rodar

```bash
python jogo-adivinhacao.py
```

---

## 👨‍💻 Autor

**Vitor Brunelli Vendramin**  
[![GitHub](https://img.shields.io/badge/GitHub-VitorBVendramin-181717?style=flat&logo=github)](https://github.com/VitorBVendramin)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-vitorvendramin-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/vitorvendramin/)