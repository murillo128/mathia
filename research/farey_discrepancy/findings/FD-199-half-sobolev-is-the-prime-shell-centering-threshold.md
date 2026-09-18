# FD-199 — Half-Sobolev is the prime-shell centering threshold for positive weighted Fourier energy

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** weighted prime shell / rank-one centering / Sobolev phase transition
- **Depends on:** FD-117, FD-196, FD-198
- **Classification:** `EXACT-DERIVED + WEIGHTED-PRIME-SHELL + RANK-ONE-CENTERING + PHASE-TRANSITION`

## Claim

`FD-196` studies the weighted positive Fourier energies

\[
\mathcal E_{H,\sigma}(K)
:=
\sum_{k\le K}
\frac{|\mathcal B_H(k)|^2}{k^{2\sigma}},
\qquad
0\le \sigma\le1,
\qquad
K=\lfloor\sqrt H\rfloor,
\]

where

\[
\mathcal B_H(k)
=
\sum_{d\mid k}
d\,M\!\left(\left\lfloor\frac Hd\right\rfloor\right).
\]

`FD-198` showed at the single weight `sigma=1/2` that the prime shell already makes the RH-facing positive-energy target much more coercive than one-row recovery suggests. The same shell can be analyzed for every weight, and it has a sharp transition exactly at the half-Sobolev index.

Let

\[
\mathcal P_K
=
\{p\text{ prime}:K/2<p\le K\},
\]

and define

\[
S_\sigma(K)
:=
\sum_{p\in\mathcal P_K}p^{-2\sigma}.
\tag{1}
\]

For prime `p`, the two-divisor identity from `FD-198` is

\[
\mathcal B_H(p)-\mathcal B_H(1)
=
p\,M\!\left(\left\lfloor\frac Hp\right\rfloor\right).
\tag{2}
\]

Hence the centered weighted prime-shell energy is exactly

\[
\boxed{
\mathcal C_{H,\sigma}
:=
\sum_{p\in\mathcal P_K}
\frac{|\mathcal B_H(p)-\mathcal B_H(1)|^2}{p^{2\sigma}}
=
\sum_{p\in\mathcal P_K}
p^{2-2\sigma}
\left|M\!\left(\left\lfloor\frac Hp\right\rfloor\right)\right|^2.
}
\tag{3}
\]

The direct transfer from the full positive energy to this centered shell satisfies

\[
\boxed{
\mathcal C_{H,\sigma}
\le
\bigl(1+S_\sigma(K)\bigr)
\mathcal E_{H,\sigma}(K).
}
\tag{4}
\]

Moreover `1+S_sigma(K)` is the exact squared operator norm of the centering map on the restricted measurement-coordinate Hilbert space consisting of the coordinates `B_H(1)` and `B_H(p)`, `p in P_K`. This sharpness statement is about the measurement-coordinate operator itself; it is **not** a claim that an arithmetic Farey/Möbius source attains the extremizing coordinate vector.

The prime number theorem gives, for fixed `sigma`,

\[
S_\sigma(K)
\sim
\frac{K^{1-2\sigma}}{\log K}
\int_{1/2}^{1}u^{-2\sigma}\,du.
\tag{5}
\]

Thus

\[
S_\sigma(K)
\to0
\quad\Longleftrightarrow\quad
\sigma\ge\frac12,
\tag{6}
\]

where at the endpoint

\[
S_{1/2}(K)
\sim
\frac{\log2}{\log K}.
\tag{7}
\]

Below the endpoint,

\[
S_\sigma(K)
\asymp_\sigma
\frac{K^{1-2\sigma}}{\log K}
\to\infty,
\qquad 0\le\sigma<\frac12.
\tag{8}
\]

Combining (3)--(5), the prime-shell RMS obeys

\[
\boxed{
\left(
\frac1{|\mathcal P_K|}
\sum_{p\in\mathcal P_K}
\left|M\!\left(\left\lfloor\frac Hp\right\rfloor\right)\right|^2
\right)^{1/2}
\ll
\mathcal E_{H,\sigma}(K)^{1/2}
K^{\sigma-3/2}
(\log K)^{1/2}
\bigl(1+S_\sigma(K)\bigr)^{1/2}.
}
\tag{9}
\]

As in `FD-198`, these are `Theta(K/log K)` distinct samples of `M(n)` with `n=Theta(K)`. If

\[
\mathcal E_{H,\sigma}(K)
=
H^{\gamma+o(1)},
\tag{10}
\]

then (9) becomes the piecewise phase diagram

\[
\boxed{
\operatorname{RMS}_{p\in\mathcal P_K}
M\!\left(\left\lfloor\frac Hp\right\rfloor\right)
\ll
\begin{cases}
K^{\gamma+\sigma-3/2+o(1)},
& \sigma\ge\tfrac12,\\[4pt]
K^{\gamma-1+o(1)},
& 0\le\sigma<\tfrac12.
\end{cases}
}
\tag{11}
\]

This gives a concrete interpretation of the `FD-196` RH-facing line

\[
\gamma+\sigma=\frac32.
\tag{12}
\]

For **every** `sigma>=1/2`, a positive weighted energy on that line forces

\[
\operatorname{RMS}_{p\in\mathcal P_K}
M\!\left(\left\lfloor\frac Hp\right\rfloor\right)
=
K^{o(1)}.
\tag{13}
\]

For `sigma<1/2`, the same direct comparison only gives

\[
\operatorname{RMS}
\ll
K^{1/2-\sigma+o(1)}.
\tag{14}
\]

Therefore `sigma=1/2` is not merely one convenient weighted norm. It is the exact threshold at which the common base row `B_H(1)=M(H)` can be subtracted from an entire square-root prime shell at asymptotically bounded cost in the positive diagonal energy. Above that threshold the whole `FD-196` critical line is shell-overcoercive in the same sense found by `FD-198`; below it, the raw positive norm pays an increasing rank-one centering tariff.

## 1. Exact norm of the prime-shell centering map

Restrict the weighted input norm to the coordinates used by the shell:

\[
\|x\|_{\sigma}^2
=
|x_0|^2
+
\sum_{p\in\mathcal P_K}
\frac{|x_p|^2}{p^{2\sigma}}.
\tag{15}
\]

Set

\[
u_0=x_0,
\qquad
u_p=p^{-\sigma}x_p,
\qquad
v_p=p^{-\sigma}.
\tag{16}
\]

Then the centered output has norm

\[
\sum_{p\in\mathcal P_K}
\frac{|x_p-x_0|^2}{p^{2\sigma}}
=
\sum_{p\in\mathcal P_K}|u_p-v_pu_0|^2.
\tag{17}
\]

In Euclidean coordinates the centering operator is

\[
T(u_0,u)=u-vu_0.
\tag{18}
\]

Its output Gram matrix is

\[
TT^*=I+vv^*,
\tag{19}
\]

so

\[
\|T\|^2
=
1+\|v\|_2^2
=
1+S_\sigma(K).
\tag{20}
\]

Taking `x_0=B_H(1)` and `x_p=B_H(p)`, the restricted input norm is at most the full energy `E_(H,sigma)(K)`, which proves (4).

Equation (20) is useful for interpreting the threshold but must be read at the correct representation level. It proves the best constant for arbitrary vectors in these **measurement coordinates**. It does not prove that the extremizing vector belongs to the image of the Möbius source under the Farey transform. The source-level consequence used here is only the valid upper bound (4), which applies to every actual Farey observation.

## 2. Why the threshold is exactly one half

On the dyadic prime shell, partial summation together with PNT gives

\[
\sum_{K/2<p\le K}p^{-2\sigma}
\sim
\frac1{\log K}
\int_{K/2}^{K}t^{-2\sigma}\,dt.
\tag{21}
\]

After `t=Ku`, this is (5). The integral over `u in [1/2,1]` is a positive finite constant for every fixed `sigma`; at `sigma=1/2` it equals `log 2`. Therefore the centering vector `v=(p^{-sigma})_p` changes from vanishing `l_2` mass to diverging `l_2` mass exactly at `sigma=1/2`.

This is the structural reason that `FD-198` worked so cleanly at the half-Sobolev weight. The prime shell contains about `K/log K` modes. Weighting each common base contribution by `p^{-2sigma}` costs roughly

\[
\frac{K}{\log K}K^{-2\sigma},
\tag{22}
\]

which vanishes precisely from the half-Sobolev exponent upward.

## 3. RMS consequence and the two spectral lines

For `0<=sigma<=1`, the exponent `2-2sigma` in (3) is nonnegative and every shell prime satisfies `p>K/2`. Hence

\[
\sum_{p\in\mathcal P_K}
\left|M\!\left(\left\lfloor\frac Hp\right\rfloor\right)\right|^2
\ll_\sigma
K^{2\sigma-2}
\mathcal C_{H,\sigma}.
\tag{23}
\]

PNT also gives

\[
|\mathcal P_K|
\sim
\frac{K}{2\log K}.
\tag{24}
\]

Dividing (23) by (24), applying (4), and taking square roots gives (9). Because `H=K^2+O(K)`, substitution of (10) yields (11).

Two lines from `FD-196`/`FD-197` now acquire a direct shell meaning.

On the RH-facing recovery line `gamma+sigma=3/2`, every weight `sigma>=1/2` forces subpower RMS on the reciprocal-prime shell. Thus the overcoercion seen by `FD-198` is not special to the single half-Sobolev norm: it fills the entire upper half of the weighted critical line.

On the generic/classical and random-multiplicative line

\[
\gamma+\sigma=2,
\tag{25}
\]

all `sigma>=1/2` give

\[
\operatorname{RMS}
\ll
K^{1/2+o(1)},
\tag{26}
\]

which is exactly the natural square-root scale highlighted by `FD-197`. For `sigma<1/2`, the direct transfer instead gives only `K^(1-sigma+o(1))`; the loss is the common base coordinate, not a change in the prime-shell identity itself.

This distinction suggests a more specific next object than simply trying another positive diagonal weight. A signed or projected statistic can remove the rank-one base mode `B_H(1)` explicitly before paying a norm budget. Such centering alone does not solve RH—the centered positive shell would still be overcoercive if required to be subcritical—but it identifies exactly which part of the low-`sigma` loss is an avoidable observation-space artifact and which part is the genuine simultaneous-amplitude demand.

## 4. Representation and hostile checks

The source-to-observation representation is unchanged from `FD-117/FD-196`. Equations (2) and (3) use only retained Fourier/divisor-transform coordinates and exact subtraction of one observed coordinate. There is no hidden source access, interpolation or approximate inverse.

The sharp constant in (20) is deliberately classified at the measurement-space level. Promoting it to a source-level lower bound would require proving that near-extremizing coordinate vectors are realizable by the arithmetic source class; no such claim is made. This keeps the representation audit clean while preserving the source-valid upper consequences (9)--(14).

The quotient samples remain distinct by the argument of `FD-198`: for distinct odd primes `p<q` in `(K/2,K]`, the prime gap is at least two and

\[
\frac Hp-\frac Hq
=
\frac{H(q-p)}{pq}
\ge
\frac{2H}{K^2}
\ge2.
\tag{27}
\]

Thus the shell RMS is genuinely simultaneous rather than repeated sampling of one quotient coordinate.

The transition is also specific to the transfer from an **uncentered positive diagonal energy** to the centered prime shell. It is not an information-theoretic impossibility below `sigma=1/2`: a signed statistic, an explicitly centered norm or a source-specific identity could remove the common row without paying the factor `S_sigma(K)`. The theorem identifies the exact tariff of the current positive-energy route, not a universal lower bound for all Farey observables.

## 5. Prior-art and formalization gates

The ingredients used in the proof are the exact Farey divisor transform already established in this line, elementary Hilbert-space operator algebra, and the prime number theorem. PNT is already anchored in `SOURCES.md`. Targeted searches around weighted Mertens samples `M(floor(H/p))`, prime-shell mean squares and Sobolev-weighted Farey energies did not locate a direct analogue of the weighted centering transition (4)--(14). No new external theorem is load-bearing, so `SOURCES.md` is unchanged.

No formalization issue is opened. The finite exact core, `||T||^2=1+||v||^2`, is elementary linear algebra; the substantive content is the asymptotic interaction of that rank-one centering operator with the PNT-sized prime shell and the `FD-196` phase diagram rather than a new reusable formal combinatorial lemma.