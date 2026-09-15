# FD-137 — fixed-ratio scale localization still hides a maximal central-rank ancestry wall

**Status:** `EXACT-DERIVED + SQUAREFREE-ERDOS-KAC-AUXILIARY + PRIME-NUMBER-THEOREM-AUXILIARY + APPROXIMATE-ANCESTRY + FIXED-RATIO-SCALE-LOCALIZATION + GROWING-PRIME-UNIFORMITY + COMMON-SOURCE + CENTRAL-RANK-WALL + EXACT-RANK-CONDITIONAL-SATURATION + NEGATIVE/BOUNDARY`.

`FD-136` shows that the multiplicatively balanced weight `1/n` still averages away the moving central-`omega(n)` interface of the common `FD-132`--`FD-136` source. That leaves an ambiguity in the current frontier: perhaps the failure is still caused by averaging over too wide a range of physical scales, and a genuinely local multiplicative window would expose the defect without having to condition on multiplicative rank.

It does not. The same common source defeats mean ancestry **inside every fixed-ratio physical-scale shell**, uniformly over a very broad growing prime family. On a shell `(T,2T]`, every bad edge is forced into an `o(sqrt(log log T))` central rank strip, so squarefree Erdős--Kac still makes its marginal mass vanish. Thus the dilution in `FD-136` is not primarily across physical scales.

At the same time, the source contains cofinal shells on which the hidden defect is an exact rank wall: after conditioning on one rank, **every** admissible edge in that cell is defective with the maximal magnitude `2`, while all other ranks in the same shell are exact. The old witness is therefore killed maximally by genuine joint scale-rank localization. This does not prove that rank-conditioned ancestry is coercive for arbitrary sources; it identifies precisely which marginalization makes the current obstruction work and forces the next negative construction, if one exists, to be structurally different.

For a prime `p`, real `T>=3`, and fixed `1<=r<infinity`, put
\[
\mathcal E_p(T)
:=
\{n:T<n\le2T,\ n\text{ squarefree},\ p\nmid n\},
\tag{1}
\]
and define the fixed-ratio shell defects
\[
\mathfrak S_{p,r}(T;a)
:=
\frac1{|\mathcal E_p(T)|}
\sum_{n\in\mathcal E_p(T)}|a_{pn}+a_n|^r,
\tag{2}
\]
with value `0` if the shell is empty, and
\[
\mathfrak S^{\log}_{p,r}(T;a)
:=
\frac{\displaystyle\sum_{n\in\mathcal E_p(T)}|a_{pn}+a_n|^r/n}
{\displaystyle\sum_{n\in\mathcal E_p(T)}1/n}.
\tag{3}
\]

Let `P=P(T)>=2` satisfy
\[
\boxed{
1+
\log\!\left(
1+\frac{\log P(T)}{\log T}
\right)
=o\!\left(\sqrt{\log\log T}\right).
}
\tag{4}
\]
Then for every fixed anchor depth `K>=0` the common squarefree-unit source `a^(K)` from `FD-132`--`FD-136` satisfies, for every fixed finite `r`,
\[
\boxed{
\sup_{\substack{p\le P(T)\\p\text{ prime}}}
\mathfrak S_{p,r}(T;a^{(K)})
\longrightarrow0,
}
\tag{5}
\]
and also
\[
\boxed{
\sup_{\substack{p\le P(T)\\p\text{ prime}}}
\mathfrak S^{\log}_{p,r}(T;a^{(K)})
\longrightarrow0.
}
\tag{6}
\]
Nevertheless the coefficient disagreement remains macroscopic:
\[
\frac1H\#\{n\le H:a_n^{(K)}\ne\mu(n)\}
\longrightarrow\frac1{2\zeta(2)},
\tag{7}
\]
and its logarithmic density has the same limit.

The prime breadth in (4) is substantial. If
\[
P(T)=T^{A(T)},
\tag{8}
\]
then the condition is simply
\[
\log(1+A(T))=o(\sqrt{\log\log T}).
\tag{9}
\]
Thus every fixed power `A` is allowed, and so is, for example,
\[
A(T)=\exp((\log\log T)^{1/3}).
\tag{10}
\]
Scale localization to a single factor-two shell therefore does not rescue mean ancestry even when the monitored prime breadth grows far beyond any fixed power of the parent scale.

## 1. The witness is unchanged

Put
\[
\ell(n):=\log\log(n+e^e)
\tag{11}
\]
and on squarefree integers define
\[
b_K(n):=
\begin{cases}
+1,&\omega(n)\le K\text{ or }\omega(n)\le\ell(n),\\
-1,&\omega(n)>K\text{ and }\omega(n)>\ell(n),
\end{cases}
\qquad
a_n^{(K)}:=\mu(n)b_K(n),
\tag{12}
\]
with `a_n^(K)=0` on nonsquarefree integers.

As in `FD-132`, this agrees exactly with Möbius through rank `K`. For every admissible squarefree edge `n -> pn`,
\[
a_{pn}^{(K)}+a_n^{(K)}
=
\mu(n)\bigl(b_K(n)-b_K(pn)\bigr),
\tag{13}
\]
so each edge defect is either `0` or has magnitude exactly `2`. Equation (7), and the corresponding logarithmic-density statement, are the same squarefree Erdős--Kac half-space calculation already established in `FD-132` and `FD-136`.

The only issue here is whether shrinking the physical-scale average from `[1,H/p]` to one multiplicative shell makes the moving interface visible.

## 2. Every bad edge in one shell lies in one shrinking normalized rank strip

Fix a large `T`, an active prime `p<=P(T)`, and `n in E_p(T)`. Write
\[
L_T:=\log\log T,
\qquad m:=\omega(n).
\tag{14}
\]
Uniformly for `T<n<=2T`,
\[
\ell(n)=L_T+O(1/\log T).
\tag{15}
\]
Also
\[
0\le\ell(pn)-\ell(n)
\le
\log\!\left(
\frac{\log(2TP(T)+e^e)}{\log(T+e^e)}
\right)
\le
C\left[
1+\log\!\left(1+\frac{\log P(T)}{\log T}\right)
\right]
\tag{16}
\]
for an absolute `C` and all sufficiently large `T`.

Because `ell(n)>K+1` uniformly on the shell once `T` is large, the finite-rank anchor no longer participates in a transition. The parent gauge is determined by whether
\[
m\le\ell(n),
\tag{17}
\]
while the child gauge is determined by whether
\[
m+1\le\ell(pn).
\tag{18}
\]
If these two truth values differ, then `m` lies between the two thresholds. In either orientation,
\[
|m-\ell(n)|
\le
1+\ell(pn)-\ell(n).
\tag{19}
\]
Combining (15)--(16), every bad parent therefore satisfies
\[
\boxed{
|\omega(n)-L_T|
\le W_T,
}
\tag{20}
\]
where
\[
W_T
:=
C'\left[
1+\log\!\left(1+\frac{\log P(T)}{\log T}\right)
\right]
\tag{21}
\]
for a suitable absolute `C'`. By (4),
\[
\frac{W_T}{\sqrt{L_T}}\longrightarrow0.
\tag{22}
\]

The important point is that (20) is already a **single-shell** statement. No small-scale prefix has been discarded and no averaging over different physical scales has occurred.

## 3. Squarefree Erdős--Kac kills the shell marginal uniformly in the active prime

The unconditioned squarefree Erdős--Kac law implies
\[
\#\{n\le2T:n\text{ squarefree},\ |
\omega(n)-\log\log(2T)|\le W_T+1\}
=o(T).
\tag{23}
\]
Indeed, for any fixed `eta>0`, condition (22) eventually embeds the event in a normalized Gaussian window `|Z|<=eta`; after taking `T` large, `eta` may be sent to zero. No local limit theorem and no prime-uniform Erdős--Kac theorem are used.

Equation (20) embeds **every** bad parent for **every** `p<=P(T)` into the set counted in (23), because `log log(2T)-L_T=o(1)`. Hence the number of bad edges in each active prime direction is `o(T)`, uniformly in that direction.

The denominator is uniformly macroscopic. From the elementary squarefree count
\[
Q(x)=\frac{x}{\zeta(2)}+O(\sqrt x),
\tag{24}
\]
we obtain
\[
|\mathcal E_p(T)|
\ge
Q(2T)-Q(T)-\frac Tp-O(1)
\ge
\left(\frac1{\zeta(2)}-\frac12\right)T+O(\sqrt T).
\tag{25}
\]
The leading coefficient is positive. Since each bad edge contributes exactly `2^r`, equations (23)--(25) prove (5).

On a factor-two shell the reciprocal weights differ by at most a factor `2`:
\[
\frac1{2T}<\frac1n<\frac1T.
\tag{26}
\]
Therefore
\[
\mathfrak S^{\log}_{p,r}(T;a^{(K)})
\le2\mathfrak S_{p,r}(T;a^{(K)}),
\tag{27}
\]
which proves (6). Thus even replacing global harmonic balancing by a worst active-prime mean on **each individual multiplicative shell** leaves the source noncoercive.

## 4. Tuned shells reveal an exact one-rank wall

The same calculation shows why rank localization changes the answer discontinuously for this witness. Fix the prime direction `p=2` and put
\[
T_m:=\exp(\exp(m+1/2)).
\tag{28}
\]
For every `n` with
\[
T_m<n\le2T_m,
\tag{29}
\]
we have, uniformly as `m->infinity`,
\[
\ell(n)=m+\frac12+o(1),
\qquad
\ell(2n)=m+\frac12+o(1).
\tag{30}
\]
Hence for all sufficiently large `m>K`, both quantities in (30) lie strictly between `m` and `m+1`.

Now let `j=omega(n)` and assume `n` is odd and squarefree. If `j<=m-1`, then both parent and child gauges are `+1`. If `j>=m+1`, both gauges are `-1`. But if
\[
j=m,
\tag{31}
\]
then the parent is on the `+1` side while the child, of rank `m+1`, is on the `-1` side. Therefore on the whole shell,
\[
\boxed{
b_K(2n)\ne b_K(n)\quad\Longleftrightarrow\quad\omega(n)=m,}
\tag{32}
\]
and every rank-`m` admissible edge has
\[
\boxed{|a^{(K)}_{2n}+a^{(K)}_n|=2.}
\tag{33}
\]
All defects in that tuned physical shell are concentrated on one exact multiplicative-rank layer, and that layer is fully defective.

## 5. The maximal rank cell is nonvacuous and grows

For completeness, the rank-`m` cell in (32) contains not merely an isolated arithmetic accident. Let
\[
R_m:=3\cdot5\cdot7\cdots q_{m-1}
\tag{34}
\]
be the product of the first `m-1` odd primes. The prime number theorem gives
\[
\log R_m=O(m\log m),
\tag{35}
\]
whereas
\[
\log T_m=e^{m+1/2}.
\tag{36}
\]
Thus
\[
x_m:=\frac{T_m}{R_m}\longrightarrow\infty.
\tag{37}
\]
Again by the prime number theorem,
\[
\pi(2x_m)-\pi(x_m)
\sim\frac{x_m}{\log x_m}
\longrightarrow\infty.
\tag{38}
\]
For every prime `q in (x_m,2x_m]` and all sufficiently large `m`,
\[
n=R_mq
\tag{39}
\]
is odd, squarefree, has `omega(n)=m`, and lies in `(T_m,2T_m]`. Hence the exact-rank cell has cardinality tending to infinity.

Define its conditional defects by
\[
\mathfrak S_{2,m,r}(T_m;a)
:=
\frac{
\displaystyle\sum_{\substack{n\in\mathcal E_2(T_m)\\\omega(n)=m}}
|a_{2n}+a_n|^r
}{
\displaystyle\#\{n\in\mathcal E_2(T_m):\omega(n)=m\}
},
\tag{40}
\]
and analogously with reciprocal weights. Equations (32)--(39) give, for all sufficiently large `m`,
\[
\boxed{
\mathfrak S_{2,m,r}(T_m;a^{(K)})
=
\mathfrak S^{\log}_{2,m,r}(T_m;a^{(K)})
=2^r.
}
\tag{41}
\]

This is the maximum possible value in the squarefree-unit class.

## 6. The small shell mean is exactly rank marginalization

Because (32) says that no other rank in the tuned shell is defective, the unconditioned shell defect factors exactly as
\[
\boxed{
\mathfrak S_{2,r}(T_m;a^{(K)})
=
2^r
\frac{
\#\{n\in\mathcal E_2(T_m):\omega(n)=m\}
}{|\mathcal E_2(T_m)|}.
}
\tag{42}
\]
The harmonic version is equally exact:
\[
\boxed{
\mathfrak S^{\log}_{2,r}(T_m;a^{(K)})
=
2^r
\frac{
\displaystyle\sum_{\substack{n\in\mathcal E_2(T_m)\\\omega(n)=m}}1/n
}{
\displaystyle\sum_{n\in\mathcal E_2(T_m)}1/n
}.
}
\tag{43}
\]
By (5)--(6), both left-hand sides tend to zero. By (41), the defect conditional on the hidden rank layer stays maximal. Thus the vanishing is caused entirely by the marginal rank mass tending to zero, not by weak ancestry failure inside that rank and not by averaging unrelated physical scales.

For a finite-horizon formulation, take
\[
H_m:=\lceil4T_m\rceil.
\tag{44}
\]
Then every edge in (29) with `p=2` lies below `H_m`. Hence the same maximal rank wall occurs cofinally inside the ordinary truncated ancestry graph.

## 7. What this changes in the frontier

`FD-136` left two conceptually different interpretations of the harmonic failure: physical scales might still be too broadly mixed, or multiplicative rank might be the genuinely missing coordinate. Equations (5)--(6) eliminate the first interpretation for this common witness. Even factor-two shell localization, with a growing prime supremum, still assigns vanishing marginal mass to the defect.

Equations (32)--(43) then show that exact rank conditioning is not a cosmetic refinement. On cofinal active scales it changes the same source from vanishing mean defect to **maximal** conditional defect. The current `FD-132`--`FD-136` matched control therefore cannot refute a genuinely joint `(log n,omega(n))` law.

This is only a diagnostic boundary, not a positive coercivity theorem. It does **not** show that exact-rank shell means recover Möbius for arbitrary squarefree-unit sources, does not classify how wide a rank window may be before dilution returns, and does not show that a joint scale-rank norm retains enough source freedom below the `FD-135` rough-core reconstruction threshold. A new negative result now needs a different common source whose boundary remains sparse even after joint scale-rank conditioning; a positive result needs to turn that conditioning into quantitative control without reconstructing the physical Möbius prefix coefficient by coefficient.

The destination-side Fourier-skeleton route also remains untouched. Nothing here proves a critical Franel estimate, a square-root Mertens envelope, or repeated-square skeleton coercivity.

## 8. Adversarial and prior-art audit

Several possible loopholes were checked. The shell theorem uses no averaging over earlier scales and no discarded small-parent prefix. Uniformity in the growing prime family is obtained by embedding every bad edge into one unconditioned squarefree central-rank event, so no Erdős--Kac theorem uniform in `p` is imported. The denominator lower bound (25) is uniform even at `p=2`. The harmonic statement is not a separate probabilistic theorem; it follows solely from the bounded variation of `1/n` on one factor-two shell.

The exact-rank saturation is also not a singleton artifact: (38)--(39) give a growing family of admissible parents. The prime number theorem is used only for that nonvacuity statement and is already anchored in `SOURCES.md`; the shell noncoercivity itself uses only the same squarefree Erdős--Kac input already anchored for `FD-132`--`FD-136` plus the elementary squarefree count.

A targeted literature search checked localized Erdős--Kac/local-limit work and Boolean-slice influence results. Those are natural neighbors: local-limit theorems quantify the small mass of exact central `omega` layers, while majority-type Boolean functions similarly have small marginal coordinate influence despite a sharp Hamming-layer boundary. No such result is used as a load-bearing step here, and no source was found that directly supplies the arithmetic statement (5)--(6) together with the exact tuned-shell factorization (32), (42), and (43). No novelty is claimed for Gaussian anti-concentration, prime abundance in fixed-ratio intervals, or the abstract majority analogy. The durable delta is the line-specific separation: **fixed-ratio physical-scale localization still loses the common ancestry witness, while conditioning on the hidden multiplicative rank exposes a full-amplitude wall on the same scales**.
