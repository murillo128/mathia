# WI-306 — The compressed-translation autocorrelation bound is exact

**Status:** `EXACT-DERIVED + CLASSICAL-NUMERICAL-RADIUS + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

WI-305 used the Haagerup--de la Harpe nilpotent numerical-radius inequality to show that no normalized real localizer supported in `(-1,1)` can make the first-prime defect small enough to avoid the compact-repair obstruction. That upper bound is not merely convenient: for a compressed translation on an interval it is **exact at every shift**. The extremal finite Jordan chain is literally embedded in the interval by translated copies of one smooth bump.

Consequently the atomwise lower bound of WI-305 is the optimal one-lag bound obtainable from support and normalization alone. At `q=2`, the best possible normalized localizer still leaves

\[
\boxed{
\inf_\chi w_2
=
\frac{\log2}{\sqrt2}
\left(1-\frac1{\sqrt2}\right)
=0.1435554814543009\ldots
>
\frac1{16}.
}
\]

Thus **optimizing the shape of `chi` inside the same support cannot weaken the first-prime obstruction at all**. More generally, if one freezes the same high-frequency reserve `beta_0=1/16` and asks only how wide the localizer support would have to become before the `q=2` autocorrelation gate could possibly stop obstructing, there is an exact discrete threshold: support length must exceed

\[
\boxed{5\log2.}
\]

For support length at most `5 log 2`, even the exact optimal autocorrelation leaves `w_2>1/16`; once the support length is strictly larger than `5 log 2`, a smooth translated-chain localizer exists with `w_2<1/16`. This last statement is only an isolated one-lag design threshold: changing the localizer support in Liu's full localization also changes other pieces of the certificate, so it is not a new positivity theorem.

## 1. Exact numerical radius of compressed translation

Let `I` be any open interval of length `ell>0`, extend functions by zero outside `I`, and define the compressed translation

\[
(S_af)(x)=f(x+a),
\qquad a>0,
\]

viewed as an operator on `L^2(I)`. Put

\[
N=N(\ell,a):=\left\lceil\frac{\ell}{a}\right\rceil.
\]

Then `S_a^N=0`: after `N` shifts the displacement is at least the interval length. Haagerup--de la Harpe therefore gives

\[
w(S_a)\le \cos\frac{\pi}{N+1}.
\tag{1}
\]

For this particular operator equality is elementary. After translating `I`, take it to be `(0,ell)`. Since `(N-1)a<ell`, choose a nonzero real

\[
\eta\in C_c^\infty\bigl((0,\min\{a,\ell-(N-1)a\})\bigr).
\]

The `N` translates `eta(x-ja)`, `j=0,...,N-1`, have disjoint supports inside `I`. Set

\[
c_j=\sin\frac{j\pi}{N+1},
\qquad
\chi(x)=\sum_{j=1}^{N}c_j\eta(x-(j-1)a).
\]

Then

\[
\|\chi\|_2^2
=\|\eta\|_2^2\sum_{j=1}^N c_j^2,
\]

while the lag-`a` autocorrelation is

\[
\langle\chi,S_a\chi\rangle
=\|\eta\|_2^2\sum_{j=1}^{N-1}c_jc_{j+1}.
\]

The sine vector is the Perron eigenvector of the path adjacency matrix, hence

\[
2\sum_{j=1}^{N-1}c_jc_{j+1}
=2\cos\frac{\pi}{N+1}\sum_{j=1}^N c_j^2.
\]

After normalizing `chi`,

\[
\boxed{
\rho_\chi(a)=\langle\chi,S_a\chi\rangle
=\cos\frac{\pi}{N+1}.
}
\tag{2}
\]

Combining (1) and (2) proves the exact smooth-localizer extremal law

\[
\boxed{
\sup_{\substack{\chi\in C_c^\infty(I;\mathbb R)\\\|\chi\|_2=1}}
\rho_\chi(a)
=\cos\frac{\pi}{\lceil\ell/a\rceil+1}.
}
\tag{3}
\]

The proof also describes explicit extremizers: a single smooth seed copied along the longest translation chain with discrete sine weights. No limiting or nonsmooth localizer is required.

## 2. Exact atomwise support loss

For an individually isolated prime-power atom `q` in the WI-304 localization defect, write `a=log q`. Its coefficient is

\[
w_q
=\frac{\Lambda(q)}{\sqrt q}
\bigl(1-\rho_\chi(a)\bigr).
\]

Equation (3) gives the exact one-lag optimization over every normalized real smooth localizer supported in an interval of length `ell`:

\[
\boxed{
\inf_\chi w_q
=\frac{\Lambda(q)}{\sqrt q}
\left(
1-
\cos\frac{\pi}{\lceil\ell/\log q\rceil+1}
\right).
}
\tag{4}
\]

Thus equation (7) of WI-305 is sharp atom by atom. A joint optimization over several lags may be more restrictive because one localizer must satisfy all autocorrelations simultaneously, but it can never improve the individual lower envelope in the direction needed to rescue `q=2`.

For Liu's normalized class `ell=2` and `q=2`,

\[
\left\lceil\frac2{\log2}\right\rceil=3,
\]

so (4) is exactly

\[
\inf_\chi w_2
=\frac{\log2}{\sqrt2}
\left(1-\cos\frac\pi4\right)
=\frac{\log2}{\sqrt2}
\left(1-\frac1{\sqrt2}\right).
\tag{5}
\]

WI-305 already proved this quantity exceeds `1/16`; the new content is that no hidden slack remains in the support-autocorrelation step.

## 3. The first-prime gate requires six translation cells at fixed reserve

Keep only the isolated `q=2` gate and freeze the high-frequency reserve at

\[
\beta_0=\frac1{16}.
\]

Let

\[
N=\left\lceil\frac{\ell}{\log2}\right\rceil.
\]

The exact best residual is

\[
r_N:=
\frac{\log2}{\sqrt2}
\left(1-\cos\frac{\pi}{N+1}\right),
\]

which decreases strictly with `N`. The transition occurs between `N=5` and `N=6`.

For `N=5`,

\[
r_5=
\frac{\log2}{\sqrt2}
\left(1-\frac{\sqrt3}{2}\right)
>\frac1{16}.
\tag{6}
\]

One completely elementary verification is to use

\[
\log2>\frac23,
\qquad
\frac1{\sqrt2}>\frac7{10},
\qquad
\sqrt3<\frac{97}{56}.
\]

Then

\[
r_5>
\frac23\frac7{10}
\left(1-\frac{97}{112}\right)
=\frac1{16},
\]

with strictness inherited from the displayed elementary bounds.

For `N=6`, the opposite strict inequality already follows from `1-cos x<x^2/2`, together with `log2<7/10`, `1/sqrt2<5/7`, and `pi^2<10`:

\[
r_6
<\frac12\frac{\pi^2}{98}
<\frac5{98}
<\frac1{16}.
\tag{7}
\]

Therefore the isolated first-prime gate can satisfy `w_2<=beta_0` only if `N>=6`, and it can satisfy it for a smooth localizer once `N>=6`. Since

\[
\left\lceil\frac{\ell}{\log2}\right\rceil\ge6
\quad\Longleftrightarrow\quad
\ell>5\log2,
\]

we obtain the exact fixed-reserve support threshold

\[
\boxed{
ell>5\log2.}
\tag{8}
\]

For a symmetric support `(-R,R)`, this reads

\[
R>\frac52\log2
=1.732867951\ldots .
\]

Again, (8) is not a prescription for Liu's full certificate: widening the localizer changes the rest of the localization and may change the reserve itself. It is a sharp falsification boundary for the proposed escape route “optimize or modestly widen the localizer while keeping the same first-prime/reserve interface.”

## 4. Consequence for the current frontier

WI-305 left several abstract ways to evade the compact-repair obstruction: retain noncompact source-exact information, increase the high-frequency reserve, reduce `1-rho_chi(log q)` by a stronger localizer mechanism, or add another noncompact supplier. Equation (3) closes one of those possibilities inside the current support class. There is **no better shape optimization** of a normalized smooth localizer on `(-1,1)` that can reduce the `q=2` defect below the WI-305 value.

Even allowing the support length to vary while artificially holding the same reserve fixed has a large discrete cost: five translation cells are still insufficient; the sixth is the first one that can cross the `1/16` gate. Thus any realistic redesign should focus on the noncompact tail/reserve side or change the localization architecture, rather than search for a cleverer compactly supported `chi` of comparable width.

This is a barrier result, not progress toward full Weil positivity by itself. It is useful precisely because it kills a plausible but weak optimization route at the exact constant.

## 5. Prior-art and novelty audit

The load-bearing numerical-radius inequality is classical: Uffe Haagerup and Pierre de la Harpe, **The Numerical Radius of a Nilpotent Operator on a Hilbert Space**, *Proc. Amer. Math. Soc.* 115 (1992), 371--379. Their bound is sharp, with the finite nilpotent Jordan shift as the model extremizer. The formula

\[
w(J_N)=\cos\frac{\pi}{N+1}
\]

is also the standard numerical-radius formula for the finite shift and follows immediately by diagonalizing the real part of `J_N`.

A targeted literature search found the classical finite-shift numerical-radius formula and broader work on numerical radii of restricted/truncated shifts, but no zeta/Weil source applying the exact translated-bump embedding to optimize Liu's localizer defect. Liu's frozen manuscript uses support disjointness at `q=8`; WI-305 uses Haagerup--de la Harpe only as an upper bound at `q=2`. The Mathia deduction recorded here is the exactness of that bound for the compressed interval translation and the resulting sharp `5 log 2` support threshold in the fixed-reserve first-prime gate. No priority claim is made.

### Validation boundary

Equations (1)--(8) are exact operator algebra plus elementary trigonometric inequalities. The zeta-specific use of `w_q` and `beta_0` inherits the source-exact normalization audited in WI-302--WI-305. The result concerns Liu's **tail-dropped bounded comparison interface**, not the full Weil form. It neither validates the unreplayed `17/16` theorem claim nor supplies evidence against RH.