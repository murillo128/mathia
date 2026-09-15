# FD-132 — pointwise primewise ancestry decay still does not recover Möbius

**Status:** `EXACT-CONSTRUCTION + SQUAREFREE-ERDOS-KAC-AUXILIARY + APPROXIMATE-ANCESTRY + PRIMEWISE-POINTWISE-DECAY + COMMON-SOURCE + FIXED-RANK-ANCHOR + POSITIVE-DENSITY-MOBIUS-DISAGREEMENT + NEGATIVE/OBSTRUCTION`.

`FD-131` shows that taking the supremum over multiplicative ranks does not repair mean prime-ancestry control: a fixed finite set of prime directions can carry all defects while its share inside each rank tends to zero. The natural next repair is therefore to keep the **prime direction itself** visible and require a separate ancestry defect for every prime.

Pointwise primewise control is still insufficient if the convergence is only required prime by prime. There is one common infinite squarefree-unit source which agrees exactly with Möbius through any prescribed fixed multiplicative rank, differs from Möbius on asymptotically half of all squarefree integers, and nevertheless has vanishing ancestry defect in **every fixed prime direction**.

For a prime `p`, a horizon `H`, and fixed `1<=r<infinity`, put
\[
\mathcal E_{p,H}
:=
\{n\le H/p:n\text{ squarefree},\ p\nmid n\}
\tag{1}
\]
and, whenever this set is nonempty,
\[
\mathfrak P_{p,r,H}(a)
:=
\frac1{|\mathcal E_{p,H}|}
\sum_{n\in\mathcal E_{p,H}}|a_{pn}+a_n|^r.
\tag{2}
\]

Then for every fixed integer `K>=0` there is one source `a^(K)` with
\[
a^{(K)}_1=1,
\qquad
a^{(K)}_n=0\quad(n\text{ nonsquarefree}),
\qquad
a^{(K)}_n\in\{-1,+1\}\quad(n\text{ squarefree}),
\tag{3}
\]
such that
\[
\boxed{a^{(K)}_n=\mu(n)\qquad(\omega(n)\le K),}
\tag{4}
\]
while for every fixed prime `p`,
\[
\boxed{\mathfrak P_{p,r,H}(a^{(K)})\longrightarrow0}
\qquad(H\to\infty),
\tag{5}
\]
and yet
\[
\boxed{
\frac1H\#\{n\le H:a^{(K)}_n\ne\mu(n)\}
\longrightarrow\frac{1}{2\zeta(2)}=\frac3{\pi^2}.
}
\tag{6}
\]

Consequently (5) holds uniformly over every **fixed finite** family of prime directions. More generally, if `(w_p)` is any fixed nonnegative summable family of prime weights, then
\[
\boxed{
\sum_p w_p\,\mathfrak P_{p,r,H}(a^{(K)})\longrightarrow0,
}
\tag{7}
\]
where inactive prime directions are assigned defect zero. Thus neither finitely many primewise means nor any scale-independent `ell^1` weighting of primewise means has a dimension-free coercivity principle toward the Möbius source.

The obstruction is a moving **central-rank majority boundary**. Unlike `FD-131`, no fixed exceptional prime set carries the defect. Each fixed prime crosses the boundary on an asymptotically negligible fraction of squarefree integers, while the boundary still separates two macroscopic coefficient populations.

## 1. A central-rank gauge with an exact finite anchor

Let
\[
\ell(n):=\log\log(n+e^e),
\tag{8}
\]
so that `ell(n)=log log n+o(1)` as `n->infinity` but no small-`n` convention is needed. On squarefree integers define
\[
b_K(n):=
\begin{cases}
+1,&\omega(n)\le K\text{ or }\omega(n)\le\ell(n),\\
-1,&\omega(n)>K\text{ and }\omega(n)>\ell(n),
\end{cases}
\tag{9}
\]
and set
\[
a^{(K)}_n:=\mu(n)b_K(n)
\tag{10}
\]
on squarefree integers, with `a_n^(K)=0` otherwise.

Equation (4) is immediate. The physical coefficient support and amplitudes are also exact: only the squarefree sign law has been changed.

For an admissible ancestry edge `n -> pn`, Möbius contributes the required sign flip, so
\[
a^{(K)}_{pn}+a^{(K)}_n
=
\mu(n)\bigl(b_K(n)-b_K(pn)\bigr).
\tag{11}
\]
Thus every bad edge has magnitude exactly `2`, and primewise ancestry reduces to the probability that multiplication by `p` crosses the gauge boundary.

## 2. A fixed prime can cross only inside a bounded central strip

Fix a prime `p`. Since
\[
\ell(pn)-\ell(n)\longrightarrow0,
\tag{12}
\]
there is `N_0=N_0(p,K)` such that for `n>=N_0`,
\[
0<\ell(pn)-\ell(n)<1
\qquad\text{and}\qquad
\ell(n)>K+1.
\tag{13}
\]
Put `m=omega(n)`. The finite-rank anchor cannot create a bad edge once (13) holds: if `m<=K`, then `m+1<=K+1<ell(pn)`, so both gauges equal `+1`.

Suppose now `m>K`. If `b_K(n)=-1`, then `m>ell(n)`. By (13),
\[
m+1>\ell(n)+1>\ell(pn),
\tag{14}
\]
so the child also has gauge `-1`. Therefore every sufficiently large bad edge must cross from `+1` to `-1`, which forces
\[
m\le\ell(n)
\qquad\text{and}\qquad
m+1>\ell(pn).
\tag{15}
\]
Equivalently,
\[
\boxed{
\ell(pn)-1<m\le\ell(n).
}
\tag{16}
\]

Hence a fixed prime direction is defective only when the number of prime factors lies in a bounded-width strip around its normal order.

Let `X=H/p`. The contribution of `n<=sqrt(X)` to (2) is `o(|E_{p,H}|)`. For `sqrt(X)<n<=X`,
\[
\ell(n)=\log\log X+O(1),
\tag{17}
\]
uniformly. Thus (16) places every remaining bad parent inside
\[
|\omega(n)-\log\log X|\le C
\tag{18}
\]
for an absolute fixed-width constant once `p` is fixed.

The squarefree Erdős--Kac theorem with exclusion of a fixed finite prime set now gives
\[
\#\{n\le X:n\text{ squarefree},\ p\nmid n,\ |\omega(n)-\log\log X|\le C\}
=o(X).
\tag{19}
\]
The same theorem gives
\[
|\mathcal E_{p,H}|
\sim
\frac{p}{p+1}\frac{X}{\zeta(2)}.
\tag{20}
\]
Since each bad edge contributes `2^r`, equations (18)--(20) prove (5).

The external input is the finite-prime-exclusion squarefree Erdős--Kac law in Huixi Li, Biao Wang, Chunlin Wang and Shaoyun Yi, *Some ergodic theorems over squarefree numbers and squarefull numbers*, Acta Arithmetica **221** (2025), 117--140, DOI `10.4064/aa240909-18-6`; the current arXiv version `2405.18157` gives the needed specialization in Theorem 1.2(1) by taking `k=0`, the prime set `T` to be all primes, and the dynamical factor to be constant. On squarefree integers `Omega=omega`. Only the Gaussian limit with `S=emptyset` and `S={p}` is used.

## 3. The same boundary changes a positive-density set of coefficients

For sufficiently large `n`, `ell(n)>K`, so disagreement with Möbius is exactly
\[
a^{(K)}_n\ne\mu(n)
\quad\Longleftrightarrow\quad
n\text{ squarefree and }\omega(n)>\ell(n).
\tag{21}
\]

Apply the same squarefree Erdős--Kac law with no excluded primes. After discarding `n<=sqrt(H)`, which has zero relative density, every remaining `n` satisfies
\[
\ell(n)=\log\log H+O(1).
\tag{22}
\]
The bounded shift in (22) is `o(sqrt(log log H))`, so the Gaussian limit places asymptotically one half of the squarefree integers above the threshold. Since squarefree integers have density `1/zeta(2)`,
\[
\#\{n\le H:a^{(K)}_n\ne\mu(n)\}
=
\frac{H}{2\zeta(2)}+o(H),
\tag{23}
\]
which proves (6).

In particular, for every fixed finite `r>=1`,
\[
\frac1H\sum_{n\le H}|a^{(K)}_n-\mu(n)|^r
\longrightarrow
\frac{2^{r-1}}{\zeta(2)}>0.
\tag{24}
\]
Thus pointwise decay of every fixed prime-coordinate defect does not imply coefficient recovery even in density.

For a fixed finite prime set `P`, (5) immediately gives
\[
\max_{p\in P}\mathfrak P_{p,r,H}(a^{(K)})\to0.
\tag{25}
\]
For fixed summable weights, `0<=mathfrak P_{p,r,H}<=2^r`, so (7) follows from dominated convergence. This rules out every scale-independent summable averaging of the pointwise prime defects as a coercive substitute.

## 4. What this removes from the current frontier

`FD-130` showed that a global ancestry mean can hide a rank interface. `FD-131` showed that taking the worst rank can still hide a finite set of prime-coordinate defects. The present witness removes the next obvious repair: **checking every prime separately but only pointwise in the prime index**.

The distinction is the order of quantifiers. For each fixed `p`, its defect tends to zero, but the source is not approaching Möbius. The defective mass migrates through an increasing multiplicative dimension near `omega(n)~log log n`. A condition capable of seeing this witness therefore needs genuine uniformity over an active prime family whose size grows with the scale, a nonsummable/scale-dependent directional norm, a local `L^infinity` condition, or a destination-side Fourier-skeleton estimate that bypasses coefficient recovery.

This is the prime-coordinate analogue of the classical Boolean-majority phenomenon: a balanced nonconstant function can have every fixed coordinate influence tend to zero as the ambient dimension grows. Boolean influence and sharp-threshold theory are therefore prior-art neighbors, not novelty claims. The line-specific content here is the arithmetic realization on one common infinite Möbius prime-ancestry graph, with squarefree support, exact low-rank Möbius anchoring, fixed-prime exclusion, and the positive-density coefficient conclusion (6).

## 5. Boundaries and adversarial checks

The result does **not** establish Fourier-skeleton saturation, a square-root partial-sum envelope, or any new Franel--Landau estimate. It is a stability obstruction only: a proof cannot infer Möbius-like coefficients from primewise defects that vanish merely pointwise in `p`.

The result also does not defeat a genuinely uniform primewise hypothesis such as
\[
\sup_{p\le P(H)}\mathfrak P_{p,r,H}(a)\to0
\tag{26}
\]
for a suitable growing `P(H)`. The squarefree Erdős--Kac input used above has `p` fixed, and no uniformity in a moving prime is claimed. Likewise the edgewise `L^infinity` defect of the witness does not vanish: bad edges retain magnitude `2`. These are materially stronger conditions and remain open.

The construction is one common infinite source, so no horizon-dependent patching is hidden. The low-rank anchor is exact. Every fixed prime is treated, not merely almost every prime under a prime average. The transition calculation (16) was checked directly against finite squarefree enumerations; the empirical primewise defect decreases only very slowly, as expected from an Erdős--Kac central layer, but the exact implication from (16) and the Gaussian anti-concentration is asymptotic and does not depend on numerics.

A targeted literature audit found no source asserting this Farey/Möbius stability obstruction directly. The Gaussian distribution input is classical in spirit and the small-coordinate-influence analogy is standard Boolean-analysis territory; no novelty is claimed for either. The durable claim is the exact synthesis with the `FD-129`--`FD-131` ancestry program and the resulting quantifier barrier: **prime direction must remain visible uniformly with the active scale, not merely one fixed prime at a time**.