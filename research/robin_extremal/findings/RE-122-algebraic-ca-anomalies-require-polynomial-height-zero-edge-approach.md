# RE-122 — algebraic CA anomalies require polynomial-height zero-edge approach

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + HEIGHT-APPROACH-GATE + RIEMANN-VON-MANGOLDT-TAIL + ALGEBRAIC-VISIBILITY-INDEX + NECESSARY-ZERO-APPROACH + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch of `RE-121`:

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\]

with a fixed high-strip cutoff

\[
\frac12<\sigma_0<\Theta.
\]

Write every nontrivial zero as `rho=beta+i gamma` and retain the `RE-121` positive boundary weight

\[
w(\rho)
:=
\frac1{|\rho|\,|1-\rho|}
+
\frac1{|1-\rho|^2},
\]

and near-edge mass

\[
W(t)
:=
\sum_{\substack{\sigma_0\le\beta<\Theta\\
0<\Theta-\beta\le t}}
w(\rho).
\tag{1}
\]

Define the **first approach height** of the subedge spectrum by

\[
\boxed{
H(t)
:=
\inf\left\{
|\gamma|:
\zeta(\beta+i\gamma)=0,
\ \sigma_0\le\beta<\Theta,
\ 0<\Theta-\beta\le t
\right\},
}
\tag{2}
\]

with `H(t)=infinity` when the set is empty. For sufficiently small `t`, every finite `H(t)` is large, because zeta has only finitely many zeros in each bounded ordinate window and edge zeros `beta=Theta` are excluded from (2).

The ordinary Riemann--von Mangoldt count converts this geometric quantity directly into the positive envelope of `RE-121`:

\[
\boxed{
W(t)
\ll_{\Theta,\sigma_0}
\frac{\log(eH(t))}{H(t)}
}
\tag{3}
\]

whenever `H(t)<infinity`, with the right side interpreted as zero when `H(t)=infinity`.

Thus a subedge spectrum that approaches the attained edge only at superpolynomial ordinate height is automatically invisible to **every fixed algebraic CA-height correction**. Conversely, an algebraically visible failure of the edge-only hierarchy forces a subedge zero to enter the relevant shrinking horizontal layer at only polynomial height in the CA phase.

More precisely, in the nonisolated case define the height-approach exponent

\[
\boxed{
\kappa_H
:=
\liminf_{t\downarrow0}
\frac{\log H(t)}{\log(1/t)},
}
\tag{4}
\]

and set `kappa_H=infinity` when `H(t)=infinity` for all sufficiently small `t`. Let

\[
R_K(\nu)
:=
B_\Theta(C)-\mathcal E_K(\nu)
\tag{5}
\]

be the order-`K` residual from `RE-121`, for regular CA states with `nu=log log C`. Then for every fixed `K>=0`,

\[
\boxed{
R_K(\nu)=o(\nu^{-A})
\qquad
\text{for every }A<\min\{\kappa_H,K+1\}.
}
\tag{6}
\]

In particular, if

\[
\kappa_H>K+1,
\tag{7}
\]

then the complete edge-only expansion through order `K` survives with the intrinsic `RE-121` remainder:

\[
\boxed{
B_\Theta(C)
=
\mathcal E_K(\nu)+O(\nu^{-K-1}).
}
\tag{8}
\]

The all-orders consequence is especially simple:

\[
\boxed{
\kappa_H=\infty
\quad\Longrightarrow\quad
\text{every fixed algebraic CA-height correction is edge-determined.}
}
\tag{9}
\]

Equivalently, it is sufficient that for every fixed `epsilon>0`, all sufficiently high subedge zeros close enough to the edge obey

\[
\Theta-\beta\ge |\gamma|^{-\epsilon}.
\tag{10}
\]

This allows subedge zeros to accumulate at `Theta`; it requires only that their horizontal deficits decay more slowly than every fixed inverse power of their ordinate.

The converse direction is quantitative. Suppose for fixed `K` and `0<A<K+1` there is an unbounded regular-CA sequence on which

\[
|R_K(\nu)|\ge c_0\nu^{-A}.
\tag{11}
\]

Then `RE-121` forces positive boundary mass in

\[
t_\nu
:=
\frac{(A+1)\log\nu}{\nu},
\tag{12}
\]

and (3) forces

\[
\boxed{
H(t_\nu)
\ll_{A,c_0,K,\Theta,\sigma_0}
\nu^A\log\nu.
}
\tag{13}
\]

Hence there is a subedge zero `rho_nu=beta_nu+i gamma_nu` with

\[
0<\Theta-\beta_\nu
\le
\frac{(A+1)\log\nu}{\nu},
\qquad
|\gamma_\nu|
\ll
\nu^A\log\nu.
\tag{14}
\]

In particular,

\[
\boxed{
\text{an order }\nu^{-A}\text{ anomaly implies }\kappa_H\le A.
}
\tag{15}
\]

For `A=0`, even this possibility disappears: the finite positive measure in `RE-121` has `W(t)\to0` as `t\downarrow0`, so the subedge source cannot produce a nonvanishing constant-order residual.

## 1. Riemann--von Mangoldt turns first approach height into a mass bound

For `|gamma|` large and `sigma_0<=beta<=Theta<1`, the weight in (1) satisfies

\[
w(\rho)
\ll_{\Theta,\sigma_0}
\frac1{1+\gamma^2}.
\tag{16}
\]

If `H=H(t)<infinity`, every zero contributing to `W(t)` has `|gamma|>=H`. Therefore

\[
W(t)
\ll
\sum_{\substack{\zeta(\rho)=0\\|\gamma|\ge H}}
\frac1{1+\gamma^2}.
\tag{17}
\]

The classical Riemann--von Mangoldt formula gives, in particular,

\[
N(T)=O(T\log T).
\tag{18}
\]

Split the tail in dyadic ordinate shells. For `H>=2`,

\[
\begin{aligned}
\sum_{|\gamma|\ge H}\frac1{1+\gamma^2}
&\ll
\sum_{j\ge0}
\frac{N(2^{j+1}H)}{(2^jH)^2}\\
&\ll
\frac1H
\sum_{j\ge0}
2^{-j}\bigl(\log H+j+1\bigr)\\
&\ll
\frac{\log(eH)}H.
\end{aligned}
\tag{19}
\]

This proves (3). No zero-density theorem near `Theta` is used here: (3) follows from the total zero count and the reciprocal-square weight already present in the CA boundary measure.

The estimate is intentionally one-sided. Knowing only the first zero height cannot determine how many near-edge zeros occur above it, nor their phases. It can only cap their total possible weighted mass.

## 2. The height exponent is a lower gate for algebraic visibility

Fix `A<kappa_H`. Choose `B` with

\[
A<B<\kappa_H.
\tag{20}
\]

By the definition of the liminf, for all sufficiently small `t`,

\[
H(t)\ge t^{-B}.
\tag{21}
\]

Since `log x/x` is decreasing for large `x`, equations (3) and (21) give

\[
W(t)
\ll
 t^B\log(1/t)
=
o(t^A).
\tag{22}
\]

`RE-121` proves the corresponding positive Laplace--Stieltjes rate equivalence also with `o` in place of `O`, so its envelope satisfies

\[
L(u)=o(u^{-A}).
\tag{23}
\]

For every fixed `K`, the signed subedge term therefore obeys

\[
\mathcal S_K(u)=o(u^{-A}).
\tag{24}
\]

Combining this with the exact `RE-121` decomposition

\[
R_K(\nu)
=
\mathcal S_K(\nu)+O(\nu^{-K-1})
\tag{25}
\]

proves (6). If `kappa_H>K+1`, choose `B` strictly between `K+1` and `kappa_H`; then (22) is actually `O(t^{K+1})`, and `RE-121` gives (8).

The condition `kappa_H=infinity` has the useful zero-wise interpretation (10). Indeed, if `H(t)>=t^{-B}` for every fixed `B` eventually, then a zero of deficit `Delta=Theta-beta` and ordinate `T=|gamma|` satisfies

\[
T\ge H(\Delta)\ge\Delta^{-B},
\]

hence `Delta>=T^{-1/B}`. Conversely, (10) for every `epsilon=1/B` implies the same superpolynomial lower bound for `H(t)`.

Thus the absolute-envelope branch of the finite-edge problem has a concrete geometric threshold: **fixed algebraic CA corrections can only see subedge zeros that approach the right edge at polynomial ordinate height.**

## 3. An algebraic CA residual produces an explicit polynomial-height zero

Assume (11) with `0<A<K+1`. Equation (17) of `RE-121` gives

\[
W(t_\nu)\gg_{c_0,K}\nu^{-A}
\tag{26}
\]

for `t_nu` from (12). In particular `H(t_nu)<infinity`. Combining (3) and (26),

\[
\frac{\log(eH(t_\nu))}{H(t_\nu)}
\gg
\nu^{-A}.
\tag{27}
\]

For large `x`, `log(ex)/x` is decreasing. If

\[
H(t_\nu)\ge D\nu^A\log\nu,
\]

then

\[
\frac{\log(eH(t_\nu))}{H(t_\nu)}
\le
\frac{A+2+o(1)}{D}\nu^{-A}.
\tag{28}
\]

Choosing `D` larger than the reciprocal constant in (27) gives a contradiction. This proves (13). The minimizing zero exists because zeros are discrete and only finitely many lie below every fixed ordinate bound, yielding (14).

Finally,

\[
\log\frac1{t_\nu}
=
\log\nu+O(\log\log\nu),
\tag{29}
\]

while (13) gives

\[
\log H(t_\nu)
\le
A\log\nu+O(\log\log\nu).
\tag{30}
\]

Taking the ratio proves (15).

For `A=0`, `RE-121` would instead force `W((\log\nu)/\nu)\gg1`. But `W(t)\to0` because it is the distribution function at zero of a finite measure with no atom at deficit zero; edge zeros were separated into `mathcal E_K`. Hence a genuine subedge correction is always `o(1)`.

## 4. Stress tests: the height exponent is a gate, not a mass law

The stronger statement

\[
W(t)\asymp t^{\kappa_H}
\]

is false even at the abstract coefficient level. Two controls already separate first-approach geometry from mass density.

First reuse the sparse dyadic control from `RE-121`: take conjugate pairs with

\[
\Delta_n:=\Theta-\beta_n=2^{-n},
\qquad
|\gamma_n|=2^n.
\]

Then

\[
H(t)\asymp t^{-1},
\qquad
\kappa_H=1,
\]

but reciprocal-square weights give

\[
W(t)\asymp t^2
\]

on dyadic scales. Thus `kappa_H=1` does not force an order-one boundary correction; sparse mass can remain much smaller.

At the opposite counting-density extreme, consider an abstract spectrum with `O(log m)` conjugate pairs near each integer ordinate `m`, each having deficit comparable to `1/m` and coefficient weight comparable to `1/m^2`. This respects the ordinary `O(T log T)` zero-counting scale. Then again

\[
H(t)\asymp t^{-1},
\qquad
\kappa_H=1,
\]

while

\[
W(t)
\asymp
\sum_{m\ge1/t}\frac{\log m}{m^2}
\asymp
t\log(1/t).
\]

So (3) is essentially sharp from total zero counting alone, including its logarithmic loss. These are coefficient-level falsification controls, not claimed zeta zero sets.

A third control is the superpolynomially separated example of `RE-121`, with `Delta_n=1/n` and `|gamma_n|=2^n`. There

\[
H(t)\asymp2^{1/t},
\qquad
\kappa_H=\infty,
\]

and the boundary mass is smaller than every algebraic power. This matches (9) and shows that absence of a fixed horizontal gap is fully compatible with all-orders edge closure.

The stress tests therefore leave exactly the intended implication: `kappa_H` is a **necessary geometric access scale** for algebraic visibility, not a substitute for the weighted mass `W`, and still less for its signed oscillatory transform.

## 5. Representation audit, prior art, and the remaining frontier

The primitive data are still the actual subedge zeros `(Theta-beta,gamma,rho)` from `RE-121`. The map to `H(t)` discards multiplicity, all zeros above the first qualifying ordinate, every coefficient beyond its horizontal deficit, and all phase information. It therefore cannot create an independent arithmetic source. Its role is diagnostic: combine one source coordinate already present in `RE-121` with an absolute tail bound to determine which zero geometries are even capable of producing an algebraic CA residual.

The ingredients outside Mathia are classical. Riemann--von Mangoldt gives `N(T)=O(T log T)`, and the reciprocal-square tail (19) is an elementary dyadic consequence. The prior-art audit included standard zeta-zero distribution references and current zero-density/zero-forcing work. Those sources study zero counts, zero-free regions, or force zeros near specified heights; they do not provide a theorem linking approach to a hypothetical attained finite right edge with regular-CA height corrections. No novelty is claimed for the zero count or tail estimate themselves.

The line-specific content is the splice with `RE-121`: its positive boundary mass is weighted strongly enough that total zero counting converts an algebraic Robin/CA anomaly into the explicit polynomial-height witness (14). No new external theorem beyond the standard zero-counting input already used in the line is load-bearing, so `SOURCES.md` needs no new anchor.

This narrows the nonisolated finite-edge frontier again. Absolute boundary mass can affect order `nu^{-A}` only if the subedge spectrum reaches a `log nu/nu` horizontal layer by ordinate about `nu^A` up to a logarithm. If the approach height is superpolynomial, every fixed algebraic correction collapses back to the edge hierarchy of `RE-120`. If polynomial-height approach does occur, that still does **not** imply an anomaly: the sparse dyadic control shows that mass may be too small, and `RE-121` already shows that phases may cancel. The surviving source question is therefore two-stage: first the actual rate/density of polynomial-height approach to the finite edge, then the signed phase structure of whatever weighted mass survives that gate.