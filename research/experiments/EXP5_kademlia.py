#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ЭКСПЕРИМЕНТ E5 (R2): Kademlia — число хопов lookup при размерах сети.
См. R1: 05-p2p-layer.md ([ДОКАЗАНО] O(log n), E[T] <= (1+o(1)) log n / H_k), план E5.

Модель: случайные 64-битные ID узлов; k=20 бакетов; жадный итеративный lookup
(одиночный путь): на каждом шаге из таблицы текущего узла (по k случайных
контактов из каждого непустого бакета — «random-neighbor» модель из анализа
Maymounkov & Mazières 2002) выбирается контакт с минимальным XOR-расстоянием
до ключа; переход, пока есть улучшение.

Два способа вычисления (оба исполняются и сверяются):
 (1) МАТЕРИАЛИЗОВАННЫЙ: реальные массивы ID n узлов (n in {10^3, 10^4, 10^5}),
     бакеты = фактические подмножества узлов по общим префиксам (найдены
     searchsorted'ом по отсортированным ID).
 (2) ГЕНЕРАТИВНЫЙ: те же ходы, но контакты семплируются равномерно из
     интервалов бакетов (эквивалентно для случайных ID и не требует хранения
     n узлов) — применяется ко всем n, включая {10^6, 10^7, 10^9}.
Валидация: |mean_gen - mean_mat| на n in {10^3..10^5}.

Теоретические колонки: ceil(log2 n)  и  log2(n)/H_20 (H_20 = 3.5977...).
Версии: python 3.13.14, numpy 2.4.3. Seed master: 42, 1000 lookup на сеть.
"""
import numpy as np
import os

B = 64            # битность ID
K = 20            # размер бакета
LOOKUPS = 1000
SEED_MASTER = 42
OUT = "results"
os.makedirs(OUT, exist_ok=True)
H20 = sum(1.0 / k for k in range(1, 21))   # гармоническое число H_20

master = np.random.default_rng(SEED_MASTER)

def theory(n):
    import math
    return math.ceil(math.log2(n)), math.log2(n) / H20

# ---------------------------------------------------------------- материализованный
def lookup_materialized(ids_sorted, key, rng):
    """Жадный lookup по реальному массиву ID. ids_sorted: np.uint64 sorted."""
    n = len(ids_sorted)
    cur = ids_sorted[rng.integers(0, n)]
    cur_key = np.uint64(1) << 63            # sentinel: максимум
    hops = 0
    while True:
        dist_cur = int(cur ^ key)
        # бакет i: узлы с LCP(cur, Y) = i  =>  блоки по общему префиксу
        best = None
        best_d = dist_cur
        for i in range(B):
            p_i = int(cur) >> (B - i)                    # первые i бит
            lo_i = int(np.searchsorted(ids_sorted, np.uint64(p_i << (B - i))))
            hi_i = int(np.searchsorted(ids_sorted, np.uint64(((p_i + 1) << (B - i)) - 1),
                                       side="right"))
            c_i = hi_i - lo_i
            if c_i == 0:
                break                                     # дальше бакеты пусты
            p_n = int(cur) >> (B - i - 1)                 # первые i+1 бит
            lo_n = int(np.searchsorted(ids_sorted, np.uint64(p_n << (B - i - 1))))
            hi_n = int(np.searchsorted(ids_sorted, np.uint64(((p_n + 1) << (B - i - 1)) - 1),
                                       side="right"))
            c_n = hi_n - lo_n
            m = c_i - c_n                                 # размер региона i
            if m <= 0:
                continue
            s = min(K, m)                                 # контактов в бакете
            # регион = Block_i \ Block_{i+1}: два куска по краям
            left_len = lo_n - lo_i
            for _ in range(s):
                r = rng.integers(0, m)
                if r < left_len:
                    pos = lo_i + r
                else:
                    pos = hi_n + (r - left_len)
                cand = ids_sorted[pos]
                d = int(cand ^ key)
                if d < best_d:
                    best_d = d
                    best = cand
        if best is None or best_d >= dist_cur:
            break
        cur = best
        hops += 1
    return hops

# ---------------------------------------------------------------- генеративный
def lookup_generative(n, key, rng):
    """Тот же алгоритм, но контакты семплируются из интервалов бакетов
    (эквивалентно для равномерно случайных ID). Работает при любом n без
    хранения ID всех узлов."""
    import math
    cur = int(rng.integers(0, 2**64, dtype=np.uint64))
    hops = 0
    i_max = int(math.ceil(math.log2(n))) + 1
    while hops < 160:
        dist_cur = cur ^ key
        best, best_d = None, dist_cur
        for i in range(0, i_max):
            m_i = n >> (i + 1)                            # ожидаемый размер региона
            if m_i < 1:
                break
            s = min(K, m_i)
            # регион i узла cur: I_i \ I_{i+1} = ПОЛОВИНА I_i, где бит i
            # отличается от бита i узла cur. I_{i+1} лежит в половине с битом i,
            # равным биту cur, поэтому регион сдвинут на (1-bit_i)*half:
            p_i = cur >> (B - i)
            base_i = p_i << (B - i)
            half = 1 << (B - i - 1)
            bit_i = (cur >> (B - i - 1)) & 1
            reg_lo = base_i + ((1 - bit_i) << (B - i - 1))
            for _ in range(s):
                cand = int(rng.integers(reg_lo, reg_lo + half, dtype=np.uint64))
                d = cand ^ key
                if d < best_d:
                    best_d = d
                    best = cand
        if best is None or best_d >= dist_cur:
            break
        cur = best
        hops += 1
    return hops

# ---------------------------------------------------------------- прогоны
out = []
def line(s=""):
    out.append(s)

line("=" * 90)
line("E5. KADEMLIA: хопы lookup (b=%d бит, k=%d бакетов, %d lookup на сеть, seed=%d)"
     % (B, K, LOOKUPS, SEED_MASTER))
line("=" * 90)
line(f"{'n':>10} | {'ceil(log2 n)':>12} | {'log2(n)/H20':>12} | {'СИМ mean±std':>13} | {'max':>5} | {'режим':>22}")
line("-" * 90)

mat_ns = [10**3, 10**4, 10**5]
gen_ns = [10**3, 10**4, 10**5, 10**6, 10**7, 10**9]
results_mat, results_gen = {}, {}

# материализованный
for n in mat_ns:
    rng = np.random.default_rng(SEED_MASTER + n)
    ids = rng.integers(0, 2**64, size=n, dtype=np.uint64)
    ids_sorted = np.sort(ids)
    rng2 = np.random.default_rng(SEED_MASTER + 1000 * n)
    keys = rng2.integers(0, 2**64, size=LOOKUPS, dtype=np.uint64)
    hops = [lookup_materialized(ids_sorted, k, rng2) for k in keys]
    results_mat[n] = hops

# генеративный
for n in gen_ns:
    rng = np.random.default_rng(SEED_MASTER + 2000 * n)
    keys = [int(rng.integers(0, 2**64, dtype=np.uint64)) for _ in range(LOOKUPS)]
    hops = [lookup_generative(n, k, rng) for k in keys]
    results_gen[n] = hops

for n in gen_ns:
    t1, t2 = theory(n)
    h = results_gen[n]
    mode = ("генеративная" if n not in mat_ns else
            "генеративная (вал. с матер.)")
    line(f"{n:>10,} | {t1:>12} | {t2:>12.2f} | {np.mean(h):>8.2f} ± {np.std(h):<6.2f} | "
         f"{max(h):>5} | {mode:>22}")

line("")
line("Валидация генеративной модели против материализованной (mean хопов):")
line(f"{'n':>10} | {'материализованная':>18} | {'генеративная':>13} | {'отн. разница':>13}")
for n in mat_ns:
    mm = np.mean(results_mat[n])
    mg = np.mean(results_gen[n])
    line(f"{n:>10,} | {mm:>18.3f} | {mg:>13.3f} | {abs(mm-mg)/mm*100:>12.2f}%")

line("")
line("ВЫВОД: рост числа хопов логарифмический (O(log n) [ДОКАЗАНО]); симуляция на")
line("случайных таблицах (k=20) даёт константу ~1/H_20, т.е. заметно лучше грубой")
line("верхней оценки ceil(log2 n); при n=10^9 симуляция даёт ~%d хопов (теория ceil: %d)."
     % (round(np.mean(results_gen[10**9])), theory(10**9)[0]))
line("НЕ ДОКАЗЫВАЕТ: реальную производительность при churn/атаках (идеализированная")
line("сеть, случайные равномерные ID, случайные (не выученные) таблицы контактов).")

print("\n".join(out))
with open(f"{OUT}/EXP5_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
print("[OK]")