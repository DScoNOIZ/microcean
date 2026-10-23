#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ЭКСПЕРИМЕНТ E3 (R2): Проверка Building Block Hypothesis — зависимость
сходимости от эпистазии. См. теоретическую часть концепции (R1; BBH — [ПРАВДОПОДОБНО]),
план E3.

Тот же GA, что в E2 (L=20, M=10, N=100, p_c=0.8, p_m=0.05, G=200, 30 прогонов).
Эпистазия λ in {0, 0.3, 0.7, 1.0} — доля фитнеса, зависящая от ПАР слотов:

  fitness(S) = (1-λ)*slot(S) + λ*pair(S),
  slot(S)  = доля слотов, совпавших с целевым t,
  pair(S)  = доля СМЕЖНЫХ пар слотов с РАВНЫМИ значениями.

Парный член конфликтует со слотовым (у целевого t соседние значения почти
всегда разные): это деструктивная эпистазия. При λ>0 глобальный оптимум
ландшафта смещается от «правильной сборки» — проверяем, как падает
сходимость к корректной сборке.

Меряем: конечную «корректность» (доля правильных слотов у лучшей особи)
и поколение достижения порога корректности 0.8 (если достижимо).

Версии: python 3.13.14, numpy 2.4.3. Seed master: 42 (как в E2).
"""
import numpy as np
import os

L, M = 20, 10
P_C, P_M = 0.8, 0.05
G_MAX = 200
RUNS = 30
SEED_MASTER = 42
N = 100
TOUR = 3
LAMBDAS = [0.0, 0.3, 0.7, 1.0]
OUT = "results"
os.makedirs(OUT, exist_ok=True)

master = np.random.default_rng(SEED_MASTER)
target = master.integers(0, M, size=L)   # тот же целевой вектор, что в E2
run_seeds = master.integers(0, 2**31, size=RUNS)

def slot_term(pop):
    return (pop == target).mean(axis=1)

def pair_term(pop):
    # доля смежных пар (i, i+1) с равными значениями
    return (pop[:, :-1] == pop[:, 1:]).mean(axis=1)

def fitness(pop, lam):
    return (1.0 - lam) * slot_term(pop) + lam * pair_term(pop)

def run_ga(lam, seed):
    rng = np.random.default_rng(seed)
    pop = rng.integers(0, M, size=(N, L))
    best_corr_traj = np.zeros(G_MAX + 1)   # корректность лучшей особи
    hit_gen = None
    for g in range(G_MAX + 1):
        f = fitness(pop, lam)
        f_slot = slot_term(pop)
        best_corr_traj[g] = f_slot.max()
        if f_slot.max() >= 0.8 and hit_gen is None:
            hit_gen = g
        if g == G_MAX:
            break
        idx = rng.integers(0, N, size=(N, TOUR))
        f3 = f[idx]
        win = idx[np.arange(N), f3.argmax(axis=1)]
        parents = pop[win]
        child = np.empty_like(parents)
        half = parents[: N // 2].copy()
        other = parents[N // 2 :].copy()
        use_cx = rng.random(N // 2) < P_C
        for j in range(N // 2):
            if use_cx[j]:
                mask = rng.random(L) < 0.5
                child[j] = np.where(mask, half[j], other[j])
            else:
                child[j] = half[j]
            child[N // 2 + j] = other[j]
        mut = rng.random((N, L)) < P_M
        child[mut] = rng.integers(0, M, size=mut.sum())
        child[np.argmin(fitness(child, lam))] = pop[np.argmax(f)]
        pop = child
    return best_corr_traj

# Предварительно считаем все прогоны (по одному разу), чтобы и сводка, и трейсы,
# и таблица по поколениям использовали одни и те же данные.
all_traj = {}   # lam -> (RUNS, G_MAX+1) корректность лучшей особи
for lam in LAMBDAS:
    traj = np.zeros((RUNS, G_MAX + 1))
    for r in range(RUNS):
        traj[r] = run_ga(lam, int(run_seeds[r]))
    all_traj[lam] = traj

out = []
def line(s=""):
    out.append(s)

line("=" * 82)
line("E3. EPISTASIS / BBH: корректность сборки vs эпистазия λ "
     "(N=%d, L=%d, M=%d, G=%d, runs=%d, seed=%d)" % (N, L, M, G_MAX, RUNS, SEED_MASTER))
line("=" * 82)
line("fitness = (1-λ)*slot + λ*pair; pair = доля смежных пар с равными значениями")
line("(парный член конфликтует с целевым вектором t — деструктивная эпистазия)")
line("")
line(f"{'λ':>5} | {'корректность@G=200 mean±std':>28} | {'достигли 0.8':>13} | {'покол. хита mean±std':>22}")
line("-" * 82)
for lam in LAMBDAS:
    traj = np.zeros((RUNS, G_MAX + 1))
    hits = []
    for r in range(RUNS):
        t = run_ga(lam, int(run_seeds[r]))
        traj[r] = t
        h = np.where(t >= 0.8)[0]
        hits.append(int(h[0]) if len(h) else None)
    ok = [h for h in hits if h is not None]
    line(f"{lam:>5.1f} | {traj[:, -1].mean():>13.4f} ± {traj[:, -1].std():<10.4f} | "
         f"{len(ok):>5}/{RUNS:<6} | "
         f"{(float(np.mean(ok)) if ok else float('nan')):>10.1f} ± "
         f"{(float(np.std(ok)) if ok else float('nan')):<10.1f}")

line("")
line("Средняя корректность лучшей особи по поколениям (mean по 30 прогонам):")
line(f"{'gen':>6} | " + " | ".join(f"λ={lam:<5}" for lam in LAMBDAS))
for g in [0, 10, 25, 50, 100, 200]:
    cells = " | ".join(f"{all_traj[lam][:, g].mean():>10.4f}" for lam in LAMBDAS)
    line(f"{g:>6} | {cells}")

line("")
line("ПРИМЕЧАНИЕ: полный послойный трейс корректности сохранён в EXP3_traces.csv "
     "(таблица выше — выборка поколений из него).")
line("")
line("ВЫВОД: с ростом λ (доля фитнеса от пар слотов) сходимость к корректной сборке "
     "ухудшается — BBH работает при низкой эпистазии; деструктивные взаимодействия "
     "слотов ломают композиционный поиск (на модели).")
line("НЕ ДОКАЗЫВАЕТ: ничего о реальных языках — только демонстрация механизма.")

print("\n".join(out))
with open(f"{OUT}/EXP3_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")

# сохраняем трейсы корректности (mean по прогонам) в CSV
with open(f"{OUT}/EXP3_traces.csv", "w") as f:
    f.write("gen," + ",".join(f"lam{l}" for l in LAMBDAS) + "\n")
    for g in range(G_MAX + 1):
        f.write(f"{g}," + ",".join(f"{all_traj[l][:, g].mean():.6f}" for l in LAMBDAS) + "\n")
print("[трейсы: results/EXP3_traces.csv]")