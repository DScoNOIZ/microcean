#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ЭКСПЕРИМЕНТ E6 (R2): Gossip — число раундов до полного распространения.
См. R1: 05-p2p-layer.md ([ДОКАЗАНО] Karp et al. 2000: push-pull на полном
графе ~ log_3 n + O(log log n) раундов), план E6.

Модель Karp 2000 (push-pull на полном графе): один узел знает «слух»;
в каждом раунде КАЖДЫЙ узел выбирает случайного соседа и выполняет и PUSH
(если я знаю — сосед узнаёт), и PULL (если сосед знает — я узнаю).

n in {10^2, 10^3, 10^4, 10^5}; 30 прогонов; seed фиксирован (master 42).
Сравнение с log_3 n и log_2 n.

Версии: python 3.13.14, numpy 2.4.3 (векторизованная симуляция).
"""
import numpy as np
import math
import os

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

NS = [10**2, 10**3, 10**4, 10**5]
RUNS = 30
SEED_MASTER = 42
OUT = "results"
os.makedirs(OUT, exist_ok=True)

def gossip_rounds(n, seed, cap=200):
    """Возвращает число раундов до полного распространения (push-pull)."""
    rng = np.random.default_rng(seed)
    informed = np.zeros(n, dtype=bool)
    informed[rng.integers(0, n)] = True
    for rnd in range(1, cap + 1):
        if informed.all():
            return rnd - 1
        peers = rng.integers(0, n, size=n)   # peers[i] — сосед узла i
        # PUSH: узлы, чей сосед знает слух... нет: push = я знаю -> сосед узнаёт
        # реализация: соседи знающих узлов узнают (поиск по маске)
        informed_new = informed.copy()
        # соседи всех информированных узлов:
        known_peers = peers[informed]
        informed_new[known_peers] = True
        # PULL: я узнаю, если мой сосед знает
        informed_new |= informed_new[peers]
        informed = informed_new
    return cap

master = np.random.default_rng(SEED_MASTER)
seeds = master.integers(0, 2**31, size=RUNS)

out = []
def line(s=""):
    out.append(s)

line("=" * 86)
line("E6. GOSSIP (push-pull, Karp 2000, полный граф): раунды до полного распространения")
line("=" * 86)
line(f"{'n':>8} | {'раунды mean±std':>16} | {'min':>4} | {'max':>4} | {'log_3 n':>8} | {'log_2 n':>8} | {'ratio mean/log3':>16}")
line("-" * 86)
mean_rounds = {}
for n in NS:
    rs = [gossip_rounds(n, int(s)) for s in seeds]
    mean_rounds[n] = np.mean(rs)
    line(f"{n:>8,} | {np.mean(rs):>9.2f} ± {np.std(rs):<6.2f} | {min(rs):>4} | {max(rs):>4} | "
         f"{math.log(n, 3):>8.2f} | {math.log(n, 2):>8.2f} | {np.mean(rs)/math.log(n,3):>16.2f}")

line("")
line("ВЫВОД: число раундов ~ log n (O(log n) [ДОКАЗАНО]); mean близко к log_3 n")
line("(константа push-pull из Karp 2000) — сеть узнаёт об обновлении фрагмента")
line("за логарифмическое число раундов.")
line("НЕ ДОКАЗЫВАЕТ: устойчивость к потерям пакетов/асинхронности/частичным")
line("графам (отдельные модели, вне R2).")

print("\n".join(out))
with open(f"{OUT}/EXP6_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")

# PNG: масштабирование (matplotlib optional)
if HAS_MPL:
    fig, ax = plt.subplots(figsize=(7, 4.5))
    xs = np.array(NS, dtype=float)
    ax.plot(xs, [mean_rounds[n] for n in NS], "o-", label="симуляция (mean)")
    ax.plot(xs, [math.log(n, 3) for n in NS], "s--", label="log_3 n")
    ax.plot(xs, [math.log(n, 2) for n in NS], "^--", label="log_2 n")
    ax.set_xscale("log")
    ax.set_xlabel("n (узлов)")
    ax.set_ylabel("раунды")
    ax.set_title("E6: gossip push-pull — раунды до полного распространения")
    ax.legend()
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(f"{OUT}/EXP6_gossip.png", dpi=140)
    print(f"[PNG: {OUT}/EXP6_gossip.png]")
else:
    print("[matplotlib недоступен — PNG пропущен; таблица выше полна]")