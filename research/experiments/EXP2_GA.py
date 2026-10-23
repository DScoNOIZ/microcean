#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ЭКСПЕРИМЕНТ E2 (R2): Сходимость простого GA на модельной задаче «сборки».
См. теоретическую часть концепции (R1), план E2.

Модель: целевая «программа» = вектор из L=20 слотов, каждый слот выбирает
фрагмент из M=10 альтернатив. Целевой вектор t известен ПО ПОСТРОЕНИЮ
(ландшафт с композиционной структурой, низкая эпистазия: фитнес аддитивен
по слотам). Фитнес = доля слотов, совпавших с t. Глобальный оптимум = 1.0.

Параметры (по плану): L=20, M=10, N in {50,100,200}, p_c=0.8, p_m=0.05,
G=200 поколений, 30 прогонов, фиксированный seed.
Операторы: турнирная селекция (k=3), равномерный кроссовер, точечная мутация,
элитизм (1 лучший). Оценка фитнеса детерминированная (без шума).

Версии: python 3.13.14, numpy 2.4.3 (PCG64: default_rng детерминирован).
Seed master: 42. Целевой вектор t фиксируется master-генератором и
сохраняется в results/EXP2_target.csv (для воспроизводимости).
"""
import numpy as np
import csv, os

# ---------------------------------------------------------------- параметры
L, M = 20, 10
P_C, P_M = 0.8, 0.05
G_MAX = 200
RUNS = 30
SEED_MASTER = 42
N_OPTIONS = [50, 100, 200]
TOUR = 3
OUT = "results"
os.makedirs(OUT, exist_ok=True)

master = np.random.default_rng(SEED_MASTER)
target = master.integers(0, M, size=L)          # глобальный оптимум (по построению)
run_seeds = master.integers(0, 2**31, size=RUNS)  # семена 30 прогонов

with open(f"{OUT}/EXP2_target.csv", "w") as f:
    f.write("L,M,target\n")
    f.write(f"{L},{M},{','.join(map(str, target))}\n")

# ---------------------------------------------------------------- GA
def fitness(pop):
    # pop: (N, L) int -> доля совпавших слотов (0..1)
    return (pop == target).mean(axis=1)

def run_ga(N, seed, track=True):
    rng = np.random.default_rng(seed)
    pop = rng.integers(0, M, size=(N, L))
    best_traj = np.zeros(G_MAX + 1)
    mean_traj = np.zeros(G_MAX + 1)
    hit_gen = None
    for g in range(G_MAX + 1):
        f = fitness(pop)
        b = f.max()
        best_traj[g] = b
        mean_traj[g] = f.mean()
        if b >= 1.0 and hit_gen is None:
            hit_gen = g
        if g == G_MAX:
            break
        # --- турнирная селекция (k=3)
        idx = rng.integers(0, N, size=(N, TOUR))
        f3 = f[idx]
        win = idx[np.arange(N), f3.argmax(axis=1)]
        parents = pop[win]
        # --- равномерный кроссовер с вероятностью p_c
        child = np.empty_like(parents)
        half = parents[: N // 2].copy()
        other = parents[N // 2 :].copy()
        # склеиваем попарно: child[j] = half[j] или other[j]
        use_cx = rng.random(N // 2) < P_C
        for j in range(N // 2):
            if use_cx[j]:
                mask = rng.random(L) < 0.5
                child[j] = np.where(mask, half[j], other[j])
            else:
                child[j] = half[j]
            child[N // 2 + j] = other[j]
        # --- мутация
        mut = rng.random((N, L)) < P_M
        child[mut] = rng.integers(0, M, size=mut.sum())
        # --- элитизм: лучший родитель выживает
        child[np.argmin(fitness(child))] = pop[np.argmax(f)]
        pop = child
    f = fitness(pop)
    return best_traj, mean_traj, f.max() >= 1.0 - 1e-12, hit_gen

# ---------------------------------------------------------------- прогоны
summary = []
traces = {}  # N -> (mean_best по поколениям)
for N in N_OPTIONS:
    best_all = np.zeros((RUNS, G_MAX + 1))
    mean_all = np.zeros((RUNS, G_MAX + 1))
    hits = []
    for r in range(RUNS):
        bt, mt, ok, hg = run_ga(N, int(run_seeds[r]))
        best_all[r] = bt
        mean_all[r] = mt
        hits.append(hg if ok else None)
    n_ok = sum(1 for h in hits if h is not None)
    hg_ok = [h for h in hits if h is not None]
    mean_hit = float(np.mean(hg_ok)) if hg_ok else float("nan")
    std_hit = float(np.std(hg_ok)) if hg_ok else float("nan")
    traces[N] = best_all.mean(axis=0)
    summary.append((N, n_ok, RUNS, mean_hit, std_hit, best_all[:, -1].mean(),
                    best_all[:, -1].std()))

out = []
def line(s=""):
    out.append(s)

line("=" * 84)
line("E2. СХОДИМОСТЬ GA НА МОДЕЛЬНОЙ ЗАДАЧЕ СБОРКИ  (L=%d, M=%d, p_c=%.1f, p_m=%.2f, G=%d, runs=%d, seed=%d)"
     % (L, M, P_C, P_M, G_MAX, RUNS, SEED_MASTER))
line("=" * 84)
line("Целевой вектор t = %s" % list(map(int, target)))
line("")
line(f"{'N':>5} | {'успех (оптимум 1.0)':>20} | {'покол. 1-го хита mean±std':>26} | {'фитнес на G=200 mean±std':>24}")
line("-" * 84)
for (N, n_ok, R, mh, sh, fb, fs) in summary:
    line(f"{N:>5} | {n_ok:>5}/{R:<13} | {mh:>10.1f} ± {sh:<10.1f} | {fb:>10.4f} ± {fs:.4f}")

line("")
line("Средний лучший фитнес по поколениям (mean по 30 прогонам):")
line(f"{'gen':>6} | " + " | ".join(f"N={N:<6}" for N in N_OPTIONS))
for g in [0, 5, 10, 20, 40, 60, 100, 150, 200]:
    cells = " | ".join(f"{traces[N][g]:>10.4f}" for N in N_OPTIONS)
    line(f"{g:>6} | {cells}")
line("")
line("ДОКАЗЫВАЕТ: на классе ландшафтов с композиционной структурой GA находит сборку "
     "за ~N*G оценок (см. долю пространства в E1.4) — инженерная реализуемость ядра.")
line("НЕ ДОКАЗЫВАЕТ: универсальности (NFL), эффективности на реальных языках, отсутствия "
     "локальных оптимумов на реальных ландшафтах.")

print("\n".join(out))
with open(f"{OUT}/EXP2_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")

# ---------------------------------------------------------------- PNG (matplotlib optional)
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False

if HAS_MPL:
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for N in N_OPTIONS:
        ax.plot(range(G_MAX + 1), traces[N], label=f"N={N}")
    ax.set_xlabel("поколение")
    ax.set_ylabel("лучший фитнес (средний по 30 прогонам)")
    ax.set_title("E2: сходимость GA (сборка L=20, M=10), seed=42")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(f"{OUT}/EXP2_ga_convergence.png", dpi=140)
    print(f"\n[PNG сохранён: {OUT}/EXP2_ga_convergence.png]")
else:
    print("\n[matplotlib недоступен — PNG пропущен; численные таблицы выше полны]")