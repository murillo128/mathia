# FD-134 — almost-full prime-family mean ancestry decay still does not recover Möbius

**Status:** `EXACT-CONSTRUCTION + SQUAREFREE-ERDOS-KAC-AUXILIARY + APPROXIMATE-ANCESTRY + ALMOST-FULL-PRIME-UNIFORMITY + COMMON-SOURCE + FIXED-RANK-ANCHOR + POSITIVE-DENSITY-MOBIUS-DISAGREEMENT + NEGATIVE/OBSTRUCTION`.

`FD-133` shows that the central-rank source from `FD-132` defeats uniform primewise **mean** ancestry control simultaneously for every prime `p<=H^alpha`, for each fixed `alpha<1`. Its proof deliberately stops there because the width of the rank strip containing every bad edge grows like `log(1/(1-alpha))` when `alpha` approaches one.

That fixed-power boundary is not the true limit of the construction. The same one common infinite source still defeats active prime families whose exponent tends to one. The correct scale is set by comparing that growing rank-strip width with the natural Erdős--Kac fluctuation `sqrt(log log X)` at the smallest parent scale.

For a prime `p`, a horizon `H`, and fixed `1<=r<infinity`, retain
\[
\mathcal E_{p,H}
:=
\{n\le H/p:n\text{ squarefree},\ p\nmid n\},
\qquad
\mathfrak P_{p,r,H}(a)
:=
\frac1{|\mathcal E_{p,H}|}
\sum_{n\in\mathcal E_{p,H}}|a_{pn}+a_n|^r.
\tag{1}
\]

Let `P=P(H)` satisfy `2<=P(H)<H`, and define the smallest parent scale
\[
Y(H):=\frac{H}{P(H)}.
\tag{2}
\]
Assume
\[
Y(H)\longrightarrow\infty
\tag{3}
\]
and
\[
\boxed{
1+\log\!\left(\frac{\log H}{\log Y(H)}\right)
=o\!\left(\sqrt{\log\log Y(H)}\right).
}
\tag{4}
\]
Then for every fixed integer `K>=0` there is one squarefree-supported unit-sign source `a^(K)`, independent of `H`, `P`, and `r`, such that
\[
a^{(K)}_n=\mu(n)\qquad(\omega(n)\le K),
\tag{5}
\]
while for every fixed finite `r>=1`,
\[
\boxed{
\sup_{\substack{p\le P(H)\\p\text{ prime}}}
\mathfrak P_{p,r,H}(a^{(K)})
\longrightarrow0,
}
\tag{6}
\]
and nevertheless
\[
\boxed{
\frac1H\#\{n\le H:a^{(K)}_n\ne\mu(n)\}
\longrightarrow\frac1{2\zeta(2)}=\frac3{\pi^2}.
}
\tag{7}
\]

Thus polynomial active-prime breadth was not the relevant obstruction in `FD-133`. Primewise mean ancestry remains noncoercive even for families reaching `H^(1-o(1))`, provided the exponent deficit approaches zero more slowly than the square-root-`log log` drift scale made precise below.

## 1. The source is unchanged

Put
\[
\ell(n):=\log\log(n+e^e)
\tag{8}
\]
and on squarefree integers define
\[
b_K(n):=
\begin{cases}
+1,&\omega(n)\le K\text{ or }\omega(n)\le\ell(n),\\
-1,&\omega(n)>K\text{ and }\omega(n)>\ell(n),
\end{cases}
\qquad
a^{(K)}_n:=\mu(n)b_K(n),
\tag{9}
\]
with `a_n^(K)=0` on nonsquarefree integers.

This is exactly the common source used in `FD-132` and `FD-133`. It has the physical squarefree support and unit amplitudes, and (5) is immediate. For every admissible ancestry edge `n -> pn`,
\[
a^{(K)}_{pn}+a^{(K)}_n
=
\mu(n)\bigl(b_K(n)-b_K(pn)\bigr),
\tag{10}
\]
so every bad edge has magnitude exactly `2`.

The coefficient-disagreement calculation is also unchanged. Once `ell(n)>K`, disagreement with Möbius is equivalent to `n` being squarefree and `omega(n)>ell(n)`. The squarefree Erdős--Kac law therefore gives (7), exactly as in `FD-132`: asymptotically one half of the squarefree integers lie above this central threshold, and squarefree integers have density `1/zeta(2)`.

Only the uniformity of the ancestry defect over the growing prime family requires a new argument.

## 2. Every bad edge lies in a moving strip whose width is explicit

Fix `H` and an active prime `p<=P(H)`, and write
\[
X:=\frac Hp.
\tag{11}
\]
Then
\[
X\ge Y(H)\longrightarrow\infty
\tag{12}
\]
uniformly over all active primes.

Discard parents `n<=sqrt(X)`. They contribute only `O(sqrt(X))` possible bad edges. For `sqrt(X)<n<=X`, equation (12) implies uniformly that `ell(n)>K+1` for large `H`, so the fixed low-rank anchor no longer affects whether an edge is bad.

Write `m=omega(n)`. In this range the parent gauge is `+1` exactly when
\[
m\le\ell(n),
\tag{13}
\]
while the child gauge is `+1` exactly when
\[
m+1\le\ell(pn).
\tag{14}
\]
Therefore a sign change can occur only if the integer `m` lies between the two thresholds in (13)--(14). In particular,
\[
|m-\ell(n)|
\le
1+\ell(pn)-\ell(n).
\tag{15}
\]

Because `pn<=H` and `n>sqrt(X)>=sqrt(Y)`, monotonicity gives
\[
0\le\ell(pn)-\ell(n)
\le
\ell(H)-\ell(\sqrt Y).
\tag{16}
\]
Also, uniformly for `sqrt(X)<n<=X`,
\[
|\ell(n)-\log\log X|
\le
\log2+o(1),
\tag{17}
\]
where the `o(1)` is uniform because `X>=Y->infinity`.

Finally,
\[
\ell(H)-\ell(\sqrt Y)
=
\log\!\left(\frac{2\log H}{\log Y}\right)+o(1).
\tag{18}
\]
Combining (15)--(18), there is an absolute constant `C` such that every sufficiently large bad parent outside the discarded square-root prefix satisfies
\[
\boxed{
|\omega(n)-\log\log X|
\le
W_H,
}
\tag{19}
\]
with
\[
W_H
:=
C\left[1+\log\!\left(\frac{\log H}{\log Y(H)}\right)\right].
\tag{20}
\]

Condition (4) is exactly the statement
\[
\frac{W_H}{\sqrt{\log\log Y(H)}}\longrightarrow0.
\tag{21}
\]
Since `X>=Y`, the same is true with `sqrt(log log X)` in the denominator, uniformly over the active prime family.

## 3. Squarefree Erdős--Kac gives uniform anti-concentration for this growing strip

Let
\[
Z_X(n)
:=
\frac{\omega(n)-\log\log X}{\sqrt{\log\log X}}
\tag{22}
\]
on squarefree integers `n<=X`. The squarefree Erdős--Kac theorem says that for every fixed real `t`, the distribution function of `Z_X` converges to the standard Gaussian distribution function `Phi(t)`.

Only fixed-threshold convergence is needed. Given `epsilon>0`, choose a fixed `eta>0` so small that
\[
\Phi(\eta)-\Phi(-\eta)<\epsilon.
\tag{23}
\]
By (21), for all sufficiently large `H`,
\[
\frac{W_H}{\sqrt{\log\log X}}<\eta
\qquad\text{for every }X\ge Y(H).
\tag{24}
\]
Ordinary convergence in the squarefree Erdős--Kac theorem at the two fixed thresholds `-eta` and `eta` is eventually valid for **all** `X>=Y(H)`. Hence
\[
\sup_{X\ge Y(H)}
\frac1X
\#\left\{
 n\le X:
 n\text{ squarefree},
 |\omega(n)-\log\log X|\le W_H
\right\}
\longrightarrow0.
\tag{25}
\]
This step needs no local limit theorem and no Erdős--Kac theorem uniform in a moving prime parameter: the growing strip is first shown to be `o(sqrt(log log X))`, then enclosed inside an arbitrarily narrow **fixed normalized** Gaussian window.

The denominator in (1) remains uniformly macroscopic. With
\[
Q(X):=\#\{n\le X:n\text{ squarefree}\}
=
\frac{X}{\zeta(2)}+O(\sqrt X),
\tag{26}
\]
we have for every prime `p`
\[
|\mathcal E_{p,H}|
\ge
Q(X)-\frac Xp
\ge
\left(\frac1{\zeta(2)}-\frac12\right)X+O(\sqrt X).
\tag{27}
\]
The coefficient in parentheses is positive. Equations (19), (25), and the discarded `O(sqrt X)` prefix therefore give `o(X)` bad parents uniformly over all `p<=P(H)`. Since each bad edge contributes `2^r`, equation (27) proves (6).

## 4. The exponent may tend to one substantially faster than any fixed-power statement sees

Write
\[
P(H)=H^{1-\delta(H)},
\qquad
Y(H)=H^{\delta(H)}.
\tag{28}
\]
Then (3)--(4) become
\[
\delta(H)\log H\longrightarrow\infty
\tag{29}
\]
and
\[
\boxed{
\log\frac1{\delta(H)}
=o\!\left(
\sqrt{\log\bigl(\delta(H)\log H\bigr)}
\right).
}
\tag{30}
\]
For fixed `delta=1-alpha`, this recovers `FD-133`. More importantly, `delta(H)` may now tend to zero.

For example, let
\[
L:=\log\log H,
\qquad
\delta(H):=\exp(-L^{1/3}).
\tag{31}
\]
Then
\[
\log\frac1\delta=L^{1/3},
\qquad
\log(\delta\log H)=L-L^{1/3},
\tag{32}
\]
so (30) holds. Consequently the same source passes the simultaneous primewise mean-ancestry test for **every prime**
\[
p\le H^{1-\exp(- (\log\log H)^{1/3})},
\tag{33}
\]
while remaining wrong on asymptotic coefficient density `3/pi^2`.

More generally, taking
\[
\delta(H)=e^{-g(H)},
\qquad
g(H)\to\infty,
\qquad
g(H)=o(\sqrt{\log\log H}),
\tag{34}
\]
satisfies (29)--(30). Thus the exponent deficit can vanish as `e^{-o(sqrt(log log H))}`.

This also identifies the natural limit of the **present proof mechanism**. When
\[
\log(1/\delta(H))\asymp\sqrt{\log\log H},
\tag{35}
\]
the worst-case threshold displacement is comparable with one Erdős--Kac standard deviation, so the shrinking-window anti-concentration argument no longer applies. Nothing here proves coercivity at that boundary; it only shows that a new idea or a different witness is required there.

## 5. What this changes in the ancestry frontier

`FD-133` left the near-full-prime regime `alpha(H)->1` as an explicit surviving possibility. Equations (4) and (30) remove a large part of that regime. Merely making the monitored prime family `H^(1-o(1))` large does not cure mean normalization: the same moving central-rank gauge can still concentrate every full-size defect on a strip whose relative Gaussian width tends to zero.

The surviving multiplicative hypotheses must therefore do something qualitatively stronger than increase directional breadth at the rate covered here. Examples still not ruled out are simultaneous rank-and-prime localization, edgewise `L^infinity` ancestry, a weighting that assigns nonvanishing mass to an `o(sqrt(log log X))` central rank strip, a growing exact anchor, prime cutoffs beyond condition (4), or a direct Fourier-skeleton coercivity estimate that avoids coefficient recovery.

This remains a stability obstruction only. It does not construct a source with the physical Mertens partial-sum envelope, does not saturate the repeated-square Fourier skeleton, and gives no Franel improvement or RH implication.

## 6. Adversarial and prior-art audit

The quantifiers are load-bearing. `K` and `r` are fixed. The source is one infinite sequence independent of the horizon and of the active prime cutoff. The supremum in (6) is taken **after** the prime family grows with `H`. Condition (4) is not replaced by the weaker requirements `P(H)=H^(1-o(1))` or `Y(H)->infinity`; the proof genuinely needs the rank-strip width to be little-oh of the squarefree Erdős--Kac fluctuation scale.

The potentially dangerous uniformity step was checked without importing a theorem uniform in `p`: every bad edge is embedded into the unconditioned central event (19), and the smallest parent scale `Y(H)` controls all active directions. The square-root prefix is uniformly negligible because `X>=Y->infinity`. The crude denominator subtraction in (27) is also uniform in `p`, including `p=2`.

The only non-elementary input is the same squarefree Erdős--Kac law already anchored in `SOURCES.md` for `FD-132`--`FD-133`: Huixi Li, Biao Wang, Chunlin Wang and Shaoyun Yi, *Some ergodic theorems over squarefree numbers and squarefull numbers*, Acta Arithmetica **221** (2025), 117--140, DOI `10.4064/aa240909-18-6`, arXiv `2405.18157`. Only the unconditioned squarefree Gaussian limit is used here. The squarefree count (26) is elementary from `1_squarefree(n)=sum_(d^2|n) mu(d)`.

A targeted prior-art audit found quantitative and multivariate Erdős--Kac results around Möbius correlations, but no theorem that supplies the line-specific implication (6) or its Farey-discrepancy interpretation directly. No novelty is claimed for Gaussian anti-concentration itself. The durable delta is the exact moving-cutoff criterion (4), which pushes the existing common-source obstruction from every fixed polynomial prime family into an explicit almost-full-prime regime and locates the square-root-`log log` drift scale where this particular argument stops.