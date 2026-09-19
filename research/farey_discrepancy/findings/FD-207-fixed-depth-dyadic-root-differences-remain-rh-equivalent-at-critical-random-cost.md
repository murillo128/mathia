# FD-207 — Fixed-depth dyadic root differences remain RH-equivalent at critical random cost

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** signed cross-scale root observable / finite-depth dyadic differencing / RH-equivalent route restriction / random-multiplicative benchmark
- **Depends on:** FD-197, FD-201, FD-204, FD-206
- **Classification:** `EXACT-DERIVED + SIGNED-CROSS-SCALE-ROOT-DIFFERENCE + RH-EQUIVALENCE + CRITICAL-RANDOM-BASELINE + DECISIVE-ROUTE-RESTRICTION`

## Claim

`FD-206` shows that the positive lowbit root anchor is already the RH-equivalent dyadic Mertens increment

\[
\Delta(n):=M(2n)-M(n)
\]

on the source-independent root-aligned Farey horizons

\[
H_n:=n p_n,
\]

where `p_n` is the largest prime at most `n`. A natural attempted escape is to subtract root anchors at neighboring dyadic scales **before** squaring, so that the difficult scalar coordinate can cancel.

Finite-depth dyadic differencing does remove the positive standalone anchor, but it does not lower the pointwise theorem surface.

Let `T` be the dilation operator

\[
(TF)(n):=F(2n),
\]

and for every fixed integer `q>=0` define

\[
\mathcal C_q(n)
:=(T-I)^q\Delta(n)
=
\sum_{j=0}^{q}(-1)^{q-j}\binom qj
\bigl(M(2^{j+1}n)-M(2^j n)\bigr).
\tag{1}
\]

Then for every fixed `q`,

\[
\boxed{
\mathrm{RH}
\iff
\mathcal C_q(n)=O_\varepsilon(n^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
}
\tag{2}
\]

More quantitatively, if `L` is nondecreasing with `L(n)>=1` and

\[
|\mathcal C_q(n)|\ll n^{1/2}L(n),
\tag{3}
\]

then

\[
\boxed{
M(N)\ll_q N^{1/2}L(N)+O_q(\log N).
}
\tag{4}
\]

The same observable is exactly a signed combination of Farey root sensors. If

\[
R(n):=S_{2,H_n}(p_n),
\]

then `FD-206` gives `R(n)=Delta(n)`, so

\[
\boxed{
\mathcal C_q(n)
=
\sum_{j=0}^{q}(-1)^{q-j}\binom qj
S_{2,H_{2^j n}}(p_{2^j n}).
}
\tag{5}
\]

Thus `q=1` is the first genuine cross-scale signed root edge,

\[
\mathcal C_1(n)
=
M(4n)-2M(2n)+M(n).
\tag{6}
\]

For the squarefree Rademacher multiplicative comparator used in `FD-197` and `FD-204`, every fixed depth also remains on the critical random scale:

\[
\boxed{
\mathbb E|\mathcal C_q^f(n)|^2
=
\frac{6}{\pi^2}
\left(\sum_{j=0}^{q}\binom qj^2 2^j\right)n
+O_q(n^{1/2}).
}
\tag{7}
\]

Hence, with the root-aligned shell scale `K_n=floor(sqrt(H_n))=Theta(n)`,

\[
\mathbb E\left[K_n|\mathcal C_q^f(n)|^2\right]
=\Theta_q(H_n).
\tag{8}
\]

The conclusion is a route restriction. A finite number of signed cross-scale root subtractions can preserve the favorable `H` random benchmark and eliminate the **literal** positive `|Delta(n)|^2` anchor, but if the resulting root difference is then paid as its own nonnegative pointwise square, its critical estimate is still RH-equivalent. The simplest post-`FD-206` repair therefore only moves the destination-complete coordinate to a finite dyadic difference. Any genuine escape has to use more than fixed-depth pointwise differencing before positivity: for example growing-depth structure, an aggregate signed relation across many root edges, or a Farey-native inequality in which no individual RH-equivalent root coefficient is separately forced to the square-root scale.

## 1. Exact realization by root-aligned Farey sensors

For every sufficiently large `m`, `FD-206` defines

\[
H_m=m p_m,
\qquad
K_m=\lfloor\sqrt{H_m}\rfloor,
\]

and proves that `p_m` is exactly the terminal prime in the critical shell

\[
K_m/2<p\le K_m.
\]

At that root there are no floor errors:

\[
S_{2,H_m}(p_m)
=
M(2m)-M(m)
=
\Delta(m).
\tag{9}
\]

Apply (9) at the finitely many source-independent scales

\[
m=n,2n,\ldots,2^q n.
\]

Substitution into the binomial expansion of `(T-I)^q` gives (5) exactly. No interpolation, inverse transform or asymptotic replacement is used.

The first case beyond `FD-206` is

\[
\mathcal C_1(n)
=R(2n)-R(n).
\tag{10}
\]

This is precisely the signed cross-scale operation suggested by the boundary of `FD-206`: cancellation happens between two physical Farey root sensors before any square is taken. The rest of the finding tests whether that operation has actually lowered the analytic destination.

## 2. A bounded odd-step defect lets one invert every fixed dyadic difference

The key elementary estimate is that the dyadic Mertens increment has bounded additive variation at every fixed shift. For integers `x,h>=1`,

\[
\begin{aligned}
\Delta(x+h)-\Delta(x)
&=
\bigl(M(2x+2h)-M(2x)\bigr)
-
\bigl(M(x+h)-M(x)\bigr),
\end{aligned}
\]

so `|mu|<=1` gives

\[
\boxed{
|\Delta(x+h)-\Delta(x)|\le 3h.
}
\tag{11}
\]

Now fix `q>=1` and put

\[
G(n):=\mathcal C_{q-1}(n).
\]

By construction,

\[
\mathcal C_q(n)=G(2n)-G(n).
\tag{12}
\]

The obstruction to recovering `G` from (12) would be independent constants on different dyadic orbits. The physical Mobius source removes that freedom because an odd binary step changes each fixed-scale `Delta` term by only boundedly many coefficients. Expanding `G` and applying (11),

\[
\begin{aligned}
|G(2n+1)-G(2n)|
&\le
\sum_{j=0}^{q-1}\binom{q-1}{j}
\left|
\Delta\!\left(2^j(2n+1)\right)
-
\Delta\!\left(2^j(2n)\right)
\right|\\
&\le
3\sum_{j=0}^{q-1}\binom{q-1}{j}2^j\\
&=
3^q.
\end{aligned}
\tag{13}
\]

Consequently, for `b in {0,1}`,

\[
\boxed{
G(2n+b)
=
G(n)+\mathcal C_q(n)+O_q(1).
}
\tag{14}
\]

This is the exact mechanism that reconnects the dyadic orbits. It depends on the bounded physical Mobius increments; it would be false as a statement about an arbitrary unconstrained source.

Take the binary prefixes of an arbitrary `N`, beginning from the leading digit `1` and repeatedly appending one bit:

\[
n_{r+1}=2n_r+b_r,
\qquad b_r\in\{0,1\}.
\]

Iterating (14) gives

\[
G(N)
=
G(1)
+
\sum_r \mathcal C_q(n_r)
+O_q(\log N).
\tag{15}
\]

The prefix sizes grow geometrically. If `alpha>0` and

\[
|\mathcal C_q(n)|\ll n^\alpha L(n)
\]

with nondecreasing `L`, then

\[
\sum_r n_r^\alpha L(n_r)
\ll_\alpha N^\alpha L(N),
\tag{16}
\]

because each earlier prefix is at most a fixed dyadic fraction of the final one. Equations (15)--(16) therefore transfer the same power exponent from `mathcal C_q` to `mathcal C_(q-1)`.

Repeating this argument a fixed number `q` of times yields

\[
|\Delta(n)|\ll_q n^\alpha L(n)+O_q(\log n).
\tag{17}
\]

Finally, as in `FD-206`,

\[
M(2n+b)-M(n)
=
\Delta(n)+b\,\mu(2n+1),
\tag{18}
\]

so the same binary-prefix telescope gives (4) when `alpha=1/2`.

Taking `L(n)=n^epsilon` proves the reverse implication in (2). The forward implication is immediate from the classical Littlewood--Mertens criterion: under RH, each of the finitely many terms in (1) is `O_epsilon(n^(1/2+epsilon))` after absorbing the fixed factors `2^j` into the constant.

For `q=1`, the bounded odd-step correction can be seen without the general estimate. Since

\[
\Delta(2n+1)-\Delta(2n)
=
\mu(4n+1)+\mu(4n+2)-\mu(2n+1)
=
\mu(4n+1)-2\mu(2n+1),
\tag{19}
\]

its modulus is at most `3`. Thus the second dyadic difference (6) already propagates from one binary prefix to both children with only bounded error.

## 3. Fixed-depth signed differencing keeps the critical random benchmark

Let

\[
f(n)=\mu(n)^2\prod_{p\mid n}X_p
\]

be the squarefree Rademacher multiplicative source used in the recent Farey findings, and write

\[
A_f(x):=\sum_{m\le x}f(m),
\qquad
\Delta_f(n):=A_f(2n)-A_f(n).
\]

Then

\[
\Delta_f(2^j n)
=
\sum_{2^j n<m\le2^{j+1}n}f(m).
\tag{20}
\]

For distinct `j`, these dyadic annuli are disjoint. The exact second-moment orthogonality

\[
\mathbb E[f(a)f(b)]
=
\mu(b)^2\,\mathbf 1_{a=b}
\]

therefore gives

\[
\mathbb E|\mathcal C_q^f(n)|^2
=
\sum_{j=0}^{q}\binom qj^2
\sum_{2^j n<m\le2^{j+1}n}\mu(m)^2.
\tag{21}
\]

Using the standard squarefree count

\[
\sum_{m\le x}\mu(m)^2
=
\frac6{\pi^2}x+O(x^{1/2}),
\tag{22}
\]

with `q` fixed proves (7). In particular,

\[
\mathbb E|\mathcal C_q^f(n)|^2=\Theta_q(n).
\tag{23}
\]

At the root-aligned Farey horizon, `H_n=Theta(n^2)` and `K_n=Theta(n)`, hence (8). Thus every fixed number of signed root subtractions has the same favorable **power** benchmark as the critical lowbit construction: the random model sees no return to the old `H^(3/2)` diagonal tariff.

This comparison is deliberately only a comparator. It does not imply a deterministic estimate for the physical Mobius source, and it does not make (2) easier than RH.

## 4. Why a positive finite-depth root edge is still destination-complete

Suppose a redesigned positive Farey energy contains, on the root-aligned family, the nonnegative term

\[
K_n|\mathcal C_q(n)|^2
\tag{24}
\]

for one fixed `q`. Since `H_n=Theta(n^2)` and `K_n=Theta(n)`, a bound

\[
K_n|\mathcal C_q(n)|^2
=O_\varepsilon(H_n^{1+\varepsilon})
\tag{25}
\]

implies, after the harmless renaming of `epsilon`,

\[
\mathcal C_q(n)=O_\varepsilon(n^{1/2+\varepsilon}).
\]

By (2), this already implies RH. Likewise

\[
K_n|\mathcal C_q(n)|^2
\ll
H_n\log^A H_n
\tag{26}
\]

gives

\[
M(N)\ll_q N^{1/2}\log^{A/2}N
\]

up to an absorbed logarithmic term.

So `FD-206` cannot be escaped merely by replacing the root anchor with one root difference, or with any other **fixed** finite number of dyadic root differences, and then assigning that resulting coordinate its own positive square at the critical budget. The literal coordinate has changed and cancellation does occur before squaring, but the new coordinate remains destination-complete because the bounded physical increments invert the fixed difference along the binary tree.

This does not rule out signed cross-scale methods as a class. It rules out the simplest finite-depth pointwise version. Three openings remain outside the theorem:

1. a differencing depth `q=q(n)` growing with scale, where both the inversion constants and the random coefficient mass are no longer uniform;
2. an aggregate signed relation among many root edges that is controlled without first obtaining a critical pointwise bound for each `mathcal C_q(n)`;
3. a different Farey-native observable whose recovery of the Mertens destination uses additional geometry rather than bounded inversion of a fixed dilation polynomial.

Those are materially different from putting a fixed-depth cross-scale coefficient into a positive norm.

## 5. Prior art, representation audit and falsification boundary

The only external theorem needed for the RH equivalence is the classical Littlewood--Mertens criterion already anchored in `SOURCES.md` through Titchmarsh. The squarefree-density input in (22) is also already covered there by a stronger Walfisz estimate. No source-list change is needed.

A targeted literature search for `M(2x)-M(x)`, dyadic Mertens criteria, and finite differences of the Mertens function did not identify a separate theorem needed for (2). No novelty is claimed for the abstract fact that a fixed dilation difference can be inverted by a binary telescope when the odd-step defect is bounded. The Mathia-specific content is the combination of that elementary inversion with the exact root-aligned Farey sensors of `FD-206`, plus the resulting route classification: finite-depth signed root differencing has critical random cost but remains RH-equivalent pointwise.

The representation boundary is exact. The horizons `H_(2^j n)` and primes `p_(2^j n)` depend only on the target scale and prime locations, never on observed Mobius values. Every summand in (5) is a native fixed-mode cross-horizon Farey sensor from `FD-201`, evaluated at the exact terminal shell root identified by `FD-206`. The operation is genuinely cross-scale because the physical horizon and root prime both change with `j`; no claim is made that these coefficients live in one single-horizon spectrum.

The fixed-depth hypothesis is essential. The proof uses constants bounded in terms of `q`; for example (13) gives `3^q`, while the random coefficient mass in (7) also grows with `q`. Nothing here shows that a depth tending to infinity with `n` remains invertible at critical cost. Likewise, (2) is a **pointwise** criterion. It does not convert average, signed-aggregate or sparse exceptional-set bounds for `mathcal C_q` into RH.

No clue status changes. The accepted local clues concern distinct ordering and Jordan-occupation mechanisms, and this finding neither resolves nor falsifies them. No formalization issue is opened: the finite-difference inversion is elementary, while the durable content is the restriction it places on the live signed/cross-scale research route.

## Conclusion

Cross-scale subtraction does exactly what `FD-206` asked for at the representation level: the positive standalone root anchor can be removed before squaring, and the squarefree-random benchmark stays at the critical `H` power. But a fixed number of such dyadic subtractions does **not** lower the pointwise analytic destination. Every fixed-depth root coefficient `(T-I)^q Delta` still has a square-root bound equivalent to RH.

Therefore the next signed Farey mechanism cannot gain merely by taking finitely many root differences and then controlling each resulting square positively. Any genuine advantage must appear only after a more global cancellation, a scale-growing construction, or a new Farey relation that does not expose an RH-equivalent fixed-depth root coefficient as an independently controlled nonnegative term.