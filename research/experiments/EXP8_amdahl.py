#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ЭКСПЕРИМЕНТ E8 (R2): Закон Амдала — ускорение vs доля последовательной части.
См. теоретическую часть концепции (R1; [ДОКАЗАНО] Amdahl 1967: S(n) = 1/((1-p)+p/n),
предел 1/(1-p)), план E8.

Сетка: p (параллельная доля) in {0.5, 0.9, 0.95, 0.99},
       n (число процессоров) in {1, 2, 4, 8, 16, 64, 256, 1024, inf}.
Таблица + PNG (логарифмическая шкала по n).

Версии: python 3.13.14; детерминированная формула, seed не нужен.
"""
import os

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

PS = [0.5, 0.9, 0.95, 0.99]
NS = [1, 2, 4, 8, 16, 64, 256, 1024, float("inf")]
OUT = "results"
os.makedirs(OUT, exist_ok=True)

def speedup(p, n):
    if n == float("inf"):
        return 1.0 / (1.0 - p)
    return 1.0 / ((1.0 - p) + p / n)

out = []
def line(s=""):
    out.append(s)

line("=" * 92)
line("E8. ЗАКОН АМДАЛА: S(n) = 1 / ((1-p) + p/n),  предел S(inf) = 1/(1-p)")
line("=" * 92)
hdr = f"{'p \\ n':>8} | " + " | ".join(f"{'inf' if n == float('inf') else str(n):>6}" for n in NS)
line(hdr)
line("-" * 92)
for p in PS:
    cells = " | ".join(f"{speedup(p, n):>8.2f}" for n in NS)
    line(f"{p:>8.2f} | {cells}")

line("")
line("Пределы:  p=0.50 -> 2.00;  p=0.90 -> 10.0;  p=0.95 -> 20.0;  p=0.99 -> 100.0")
line("Даже при p=0.99 потолок 100x; при p=0.95 — 20x. Последовательные 5% съедают")
line("95% потенциального выигрыша при n=1024 (S=19.6 vs идеальные 1024).")
line("")
line("ВЫВОД: количественная граница выигрыша от параллелизации сборки; честный")
line("предел [ДОКАЗАНО] (согласуется с файлом 08 R1).")
line("НЕ ДОКАЗЫВАЕТ: реальную параллельную долю конкретной сборки (измеряется в")
line("прототипе, вне R2).")

print("\n".join(out))
with open(f"{OUT}/EXP8_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")

# PNG (matplotlib optional)
if HAS_MPL:
    fig, ax = plt.subplots(figsize=(7.5, 5))
    xs = np_log = [1, 2, 4, 8, 16, 64, 256, 1024]
    for p in PS:
        ys = [speedup(p, n) for n in xs]
        ax.plot(xs, ys, "o-", label=f"p={p}")
    ax.plot(xs, xs, "k--", label="идеал (S=n)")
    ax.set_xscale("log", base=2)
    ax.set_xticks(xs)
    ax.set_xticklabels([str(x) for x in xs])
    ax.set_xlabel("число процессоров n")
    ax.set_ylabel("ускорение S(n)")
    ax.set_title("E8: закон Амдала")
    ax.legend()
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(f"{OUT}/EXP8_amdahl.png", dpi=140)
    print(f"[PNG: {OUT}/EXP8_amdahl.png]")
else:
    print("[matplotlib недоступен — PNG пропущен; таблица выше полна]")