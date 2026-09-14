# FD-125 — square-root common sources saturate the Fourier skeleton on repeated-square horizons

**Status:** `EXACT-DERIVED + FLOOR-QUOTIENT-FOURIER-SKELETON + COMMON-SOURCE-COUNTERMODEL + SQUARE-ROOT-ENVELOPE + SUPEREXPONENTIAL-SHARPNESS + POINTWISE-SPARSE-SATURATION + NEGATIVE/ROUTE-RESTRICTION`.

`FD-124` proves that a polynomial-growth common source can Cesàro-saturate the minimal floor-quotient Fourier skeleton only on a schedule whose average logarithmic horizon growth tends to infinity. That theorem deliberately leaves genuinely superexponential schedules open. The escape is real already at the square-root source envelope: one can build a **single horizon-independent source** that pointwise saturates the skeleton along an explicit repeated-square chain.

Let

\[
H_0=4,
\qquad
H_{j+1}=H_j^2,
\qquad
H_j=4^{2^j},
\tag{1}
\]

and retain

\[
\mathcal Q_H
:=
\left\{\left\lfloor\frac Hm\right\rfloor:1\le m\le H\right\},
\qquad
\tau_H(k):=\left\lfloor\frac Hk\right\rfloor,
\tag{2}
\]

\[
A_H(k)
:=
\sum_{d\mid k}d\,Y\!\left(\tau_H(d)\right),
\qquad
\mathcal E_H^{\mathcal Q}(Y)
:=
\sum_{k\in\mathcal Q_H}\frac{|A_H(k)|^2}{k^2},
\tag{3}
\]

and

\[
S_H(Y)
:=
\frac{|Y(H)|^2}{\mathcal E_H^{\mathcal Q}(Y)}
\quad\text{when }\mathcal E_H^{\mathcal Q}(Y)>0.
\tag{4}
\]

There exists one real sequence `Y` on the positive integers such that

\[
\boxed{|Y(n)|\le 2\sqrt n\qquad(n\ge1),}
\tag{5}
\]

while at every retained horizon

\[
\boxed{Y(H_j)=\sqrt{H_j}}
\tag{6}
\]

and

\[
\boxed{
\mathcal E_{H_j}^{\mathcal Q}(Y)
=
H_j
+O\!\left(H_{j-1}(\log H_{j-1})^3\right).
}
\tag{7}
\]

Consequently

\[
\boxed{
S_{H_j}(Y)
=
1-O\!\left(\frac{(\log H_{j-1})^3}{H_{j-1}}\right)
\longrightarrow1.
}
\tag{8}
\]

Thus common-source coherence plus a polynomial envelope—even the critical square-root envelope—does not force a pointwise relative energy gap on sufficiently sparse horizons. `FD-124`'s superexponential escape is qualitatively sharp for the abstract common-source Fourier-skeleton problem. Any theorem assigning a positive relative cost to a prescribed physical horizon must use an additional arithmetic law that this construction does not satisfy.

## 1. Recursive construction of one common source

`FD-118` proves two facts used here: `\tau_H` is an involution of `\mathcal Q_H`, and

\[
\{1,\ldots,\lfloor\sqrt H\rfloor\}
\subseteq\mathcal Q_H.
\tag{9}
\]

For each stage put

\[
t_j:=\sqrt{H_j}=H_{j-1}\qquad(j\ge1),
\tag{10}
\]

with `t_0=2`. Let `P_{-1}=\varnothing`. Assume `Y` has already been assigned on

\[
P_{j-1}:=\bigcup_{i<j}\mathcal Q_{H_i}.
\tag{11}
\]

Every old index lies below or at `H_(j-1)=sqrt(H_j)`, so by (9)

\[
P_{j-1}\subseteq\mathcal Q_{H_j}.
\tag{12}
\]

Keep those old values unchanged. For every new index

\[
r\in\mathcal Q_{H_j}\setminus P_{j-1},
\]

define

\[
\boxed{
Y(r)
:=
t_j\,
\frac{\mu(\tau_{H_j}(r))}{\tau_{H_j}(r)}.
}
\tag{13}
\]

This is exactly the `FD-119` equality ray written in the physical source coordinate `r`: if `k=\tau_(H_j)(r)`, involutivity gives `r=\tau_(H_j)(k)`, so (13) is

\[
Y(\tau_{H_j}(k))=t_j\frac{\mu(k)}k.
\tag{14}
\]

The endpoint `H_j` is new at stage `j`, and `\tau_(H_j)(H_j)=1`. Hence (13) gives (6).

The recursion defines a single infinite source rather than one source per horizon. Indeed `\mathcal Q_(H_j)` contains every integer at most `H_(j-1)`, and `H_(j-1)\to\infty`; every positive integer therefore enters some `P_j` and receives one permanent value.

## 2. The permanent source obeys a square-root envelope

Suppose `r` is first assigned at horizon `H` and write

\[
k=\tau_H(r).
\]

By involutivity, `r=floor(H/k)`. Equation (13) and `|\mu(k)|\le1` give

\[
|Y(r)|
\le
\frac{\sqrt H}{k}.
\tag{15}
\]

Since

\[
\frac Hk<r+1,
\tag{16}
\]

we obtain

\[
|Y(r)|
<
\frac{r+1}{\sqrt H}
\le
\frac{r+1}{\sqrt r}
\le
2\sqrt r.
\tag{17}
\]

The value never changes later, so (5) holds globally. In particular this countermodel satisfies the polynomial-growth hypothesis of `FD-124` with exponent `alpha=1/2`, not merely the trivial linear envelope available for the physical Mertens source.

## 3. Only the inherited old coordinates perturb the equality ray

Fix a retained horizon `H_j` and abbreviate

\[
H:=H_j,
\qquad
H_-:=H_{j-1}=\sqrt H,
\qquad
t:=\sqrt H.
\tag{18}
\]

In the reindexed coordinates of `FD-119`, set

\[
x_k:=Y(\tau_H(k)),
\qquad
x_k^{(0)}:=t\frac{\mu(k)}k,
\qquad
\delta_k:=x_k-x_k^{(0)}.
\tag{19}
\]

If `r=\tau_H(k)` was first assigned at the current stage, (13) makes `\delta_k=0`. Hence the support of `\delta` is contained in the coordinates corresponding to old indices `r\in P_(j-1)`. Both the permanent value and the current equality-ray value obey the estimate (17), so

\[
|\delta_k|\le4\sqrt r,
\qquad r=\tau_H(k)\in P_{j-1}.
\tag{20}
\]

Because `\tau_H` is a bijection on `\mathcal Q_H`, this yields

\[
\sum_{k\in\mathcal Q_H}|\delta_k|^2
\ll
\sum_{r\in P_{j-1}}r.
\tag{21}
\]

The floor-quotient hyperbola decomposition gives, with `s=floor(sqrt N)`,

\[
\mathcal Q_N
=
\{1,\ldots,s\}
\cup
\left\{\left\lfloor\frac Nm\right\rfloor:1\le m\le s\right\}.
\tag{22}
\]

Therefore

\[
\sum_{r\in\mathcal Q_N}r
\le
\frac{s(s+1)}2
+
N\sum_{m\le s}\frac1m
\ll N\log(2N).
\tag{23}
\]

Since the horizons are obtained by repeated squaring, the last previous stage dominates the earlier ones:

\[
\sum_{r\in P_{j-1}}r
\le
\sum_{i<j}\sum_{r\in\mathcal Q_{H_i}}r
\ll
H_-\log(2H_-).
\tag{24}
\]

Combining (21)--(24),

\[
\boxed{
\sum_{k\in\mathcal Q_H}|\delta_k|^2
\ll
H_-\log(2H_-).
}
\tag{25}
\]

Now use the elementary divisor-transform stability estimate proved in `FD-120`. If

\[
B(k):=\sum_{d\mid k}d\,\delta_d,
\tag{26}
\]

then

\[
\sum_{k\in\mathcal Q_H}\frac{|B(k)|^2}{k^2}
\ll
(1+\log H)^2
\sum_{k\in\mathcal Q_H}|\delta_k|^2.
\tag{27}
\]

Equations (25)--(27), together with `log H=2 log H_-`, give

\[
\sum_{k\in\mathcal Q_H}\frac{|B(k)|^2}{k^2}
\ll
H_-(\log H_-)^3.
\tag{28}
\]

The equality-ray Fourier vector has only its first mode nonzero. Moreover `\delta_1=0`, because `\tau_H(1)=H` and the current endpoint is newly assigned with `Y(H)=t`. Thus `B(1)=0`, so the cross term with the equality ray vanishes exactly. Hence

\[
\mathcal E_H^{\mathcal Q}(Y)
=
t^2+
\sum_{k\in\mathcal Q_H}\frac{|B(k)|^2}{k^2},
\tag{29}
\]

which proves (7). Dividing by `t^2=H=H_-^2` proves (8).

## 4. Why this does not contradict the multihorizon gaps

The construction does not evade `FD-121`--`FD-124`; it realizes their surviving sparse regime. At the transition

\[
H_j=H_{j-1}^2,
\qquad
q_j=\frac{H_j}{H_{j-1}}=H_{j-1},
\tag{30}
\]

the ratio itself diverges as the previous horizon. The chain has

\[
\frac1n\log\frac{H_n}{H_0}
=\frac{2^n-1}{n}\log4
\longrightarrow\infty,
\tag{31}
\]

exactly as `FD-124` requires of any Cesàro-saturating polynomial common source.

There is also no conflict with the fixed-dilation gaps of `FD-122`. Those estimates keep the squarefree dilation `q` fixed while the base horizon grows. Here the dilation changes at every stage and tends rapidly to infinity. An inherited endpoint such as `Y(H_(j-1))` may create a substantial absolute perturbation at horizon `H_j`, but its energy cost is only on the `H_(j-1)=sqrt(H_j)` scale and is therefore negligible relative to the critical energy `H_j`.

This identifies the exact limitation of common-source coherence by itself. Reusing one permanent source destroys independent one-horizon optimization at finite horizon entropy, but sufficiently sparse scales leave enough new quotient coordinates to reinstall the equality ray while the old coordinates occupy only a lower-order part of the native Fourier norm.

## 5. Boundary, falsification test, and prior-art audit

The sequence constructed here is **not** asserted to be a Mertens trajectory. Its increments need not lie in `{-1,0,+1}`, its zero set need not be the nonsquarefree integers, it need not obey the Möbius sign/multiplicative law, and no growing family of exact divisor identities is imposed. `FD-120` already shows that a full squarefree/unit-amplitude law can be cheap when witnesses are allowed to depend on the horizon; this result addresses the complementary issue of horizon-independent coherence while deliberately dropping that physical increment law.

Therefore the theorem does not obstruct a pointwise Farey/RH argument that combines common-source coherence with genuinely arithmetic cross-scale information. It does rule out a stronger conclusion from only the hypotheses used by `FD-124`: polynomial source growth plus exact reuse of one source across horizons cannot force the designated endpoint to pay a positive relative Fourier-skeleton cost on all sufficiently large scales.

The decisive falsification test is the current-horizon perturbation estimate. A counterexample must show that some permanent old assignment contributes more than

\[
O\!\left(H_{j-1}(\log H_{j-1})^3\right)
\]

to the `H_j` skeleton energy despite (20)--(27), or that the recursive source is not simultaneously well-defined on the nested floor-quotient carriers. Both points reduce to the exact involution/divisor transform already proved in `FD-118` and the self-contained perturbation bound of `FD-120`.

A targeted prior-art audit covered Franel--Landau/Farey harmonic formulations, Mertens floor-quotient compression, and the floor-quotient partial-order literature. Lagarias--Richman and Cardinal provide established floor-quotient/Mertens compression context, but no matching theorem was located for this common-source sparse-horizon extremizer. Search absence is not a novelty proof. No external theorem is load-bearing: (22)--(24) are elementary and the only nontrivial internal analytic input is the already-canonical `FD-120` transform bound, so `SOURCES.md` requires no new dependency.

The durable consequence is a sharp route restriction. After `FD-124`, the remaining superexponential loophole cannot be closed by a better bookkeeping argument using only polynomial growth and source coherence. A continuation that targets the physical Mertens/Farey source must spend an additional law—bounded/squarefree increments, multiplicative sign correlation, growing divisor compatibility, or another exact arithmetic constraint—at the sparse horizons themselves.