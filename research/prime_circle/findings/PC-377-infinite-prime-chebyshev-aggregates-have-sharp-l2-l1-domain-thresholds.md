# PC-377 — Infinite prime Chebyshev aggregates have sharp ℓ²/ℓ¹ domain thresholds

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for the direct infinite linear-aggregation loophole left open by PC-376. The finite Chebyshev refinement family can be assembled over all prime degrees on the positive-mode algebraic core, but the resulting operator is closable exactly when its prime coefficients lie in `ell^2` and bounded exactly when they lie in `ell^1`. For the degree factor inherited from the raw Jacobian transfer, `a_p(s)=p^{1-s}`, the exact thresholds are `Re(s)>3/2` for closability and `Re(s)>2` for boundedness. Hence on the half-density line `Re(s)=1/2`, where PC-374 identifies the raw transfer with the Chebyshev backward shift by a unitary gauge, the literal all-prime sum is not merely unbounded: it is nonclosable. No closed spectral operator is obtained from that canonical linear assembly without adding extra damping, a different domain/topology, or cross-prime structure.

The functional-analytic mechanism is classical Hardy/infinite-polydisk multiplier theory plus an elementary graph-closure test. The line-local content is the exact domain classification for the Chebyshev transfer family derived in PC-372--PC-376 and the resulting closure of its most direct infinite-prime linear extension.

## 1. Exact all-prime operator on the positive Chebyshev sector

Let

\[
\mathcal H_+
=\overline{\operatorname{span}}\{e_n:n\ge1\}
\cong \ell^2(\mathbb N),
\]

where PC-374 uses the Chebyshev modes and, for every integer `m>=2`,

\[
V_m e_n=e_{mn},
\qquad
P_m:=V_m^*,
\qquad
P_m e_n=
\begin{cases}
e_{n/m},&m\mid n,\\
0,&m\nmid n.
\end{cases}
\tag{1}
\]

PC-376 identifies the finite coprime family `P_p` with the coordinate backward shifts in the Bohr/infinite-polydisk model. To test the infinite-global loophole, let `a=(a_p)` be arbitrary complex coefficients indexed by primes and define on

\[
\mathcal D_0=\operatorname{span}_{\mathrm{fin}}\{e_n:n\ge1\}
\]

the algebraic operator

\[
A_a:=\sum_p a_p P_p.
\tag{2}
\]

This is genuinely well-defined on `D_0`: for each basis vector only the finitely many prime divisors of `n` contribute,

\[
\boxed{
A_a e_n=\sum_{p\mid n}a_p e_{n/p}.
}
\tag{3}
\]

Thus no convergence prescription has been inserted at the definition stage. The question is whether this exact finite-shell action has a closed Hilbert-space realization when infinitely many prime refinement channels are present.

## 2. Closability is exactly the prime-coefficient ℓ² condition

The answer is sharp:

\[
\boxed{
A_a\text{ is closable on }\mathcal H_+
\iff
(a_p)_p\in\ell^2(\mathcal P).
}
\tag{4}
\]

First suppose `a notin ell^2(P)`. Choose increasing finite prime sets `F_N` with

\[
S_N:=\sum_{p\in F_N}|a_p|^2\longrightarrow\infty
\]

and put

\[
x_N:=\frac1{S_N}\sum_{p\in F_N}\overline{a_p}\,e_p.
\tag{5}
\]

For a prime `p`, (3) gives `A_a e_p=a_p e_1`; hence

\[
\|x_N\|^2=\frac1{S_N}\longrightarrow0,
\qquad
A_a x_N=e_1.
\tag{6}
\]

The graph closure therefore contains `(0,e_1)`, so it is not the graph of an operator. This proves nonclosability whenever `a notin ell^2`.

Conversely, if `a in ell^2`, then every basis vector belongs to the adjoint domain. Directly from (3),

\[
A_a^* e_m=\sum_p\overline{a_p}\,e_{pm},
\qquad
\|A_a^*e_m\|^2=\sum_p|a_p|^2<\infty.
\tag{7}
\]

For a finite linear combination `y=sum_{m in F}c_m e_m`, possible collisions among indices `pm` do not matter: the triangle inequality gives

\[
\|A_a^*y\|
\le
\sum_{m\in F}|c_m|\,\|a\|_{\ell^2}<\infty.
\tag{8}
\]

Thus `D_0 subset D(A_a^*)`. Since `D_0` is dense, the adjoint is densely defined and `A_a` is closable. This proves (4) without any multiplier theorem.

The obstruction is therefore stronger and cleaner than ordinary norm divergence. If the coefficient vector fails square summability, no choice of taking the closure of the canonical finite-mode graph can produce an operator at all.

## 3. Boundedness is exactly ℓ¹, with exact norm

The boundedness threshold is also sharp:

\[
\boxed{
A_a\text{ extends boundedly}
\iff
a\in\ell^1(\mathcal P),
\qquad
\|A_a\|=\sum_p|a_p|.
}
\tag{9}
\]

For `a in ell^1`, the operator series in (2) converges absolutely in operator norm because every `P_p` is a contraction, so

\[
\|A_a\|\le\sum_p|a_p|.
\tag{10}
\]

For the converse and exact norm, use the Bohr lift already identified in PC-376:

\[
e_n\longleftrightarrow\prod_p z_p^{\nu_p(n)},
\qquad
V_p\longleftrightarrow M_{z_p},
\qquad
P_p\longleftrightarrow M_{z_p}^*.
\tag{11}
\]

If `A_a` is bounded, its adjoint agrees on polynomials with multiplication by the linear symbol

\[
f_a(z)=\sum_p\overline{a_p}z_p.
\tag{12}
\]

The Hardy-space multiplier theorem of Hedenmalm--Lindqvist--Seip identifies bounded multipliers with bounded analytic Dirichlet/infinite-polydisk symbols. For each finite prime set `F`, conditional expectation to those coordinates is contractive in `L^infty`, while

\[
\sup_{|z_p|\le1,\,p\in F}
\left|\sum_{p\in F}\overline{a_p}z_p\right|
=
\sum_{p\in F}|a_p|.
\tag{13}
\]

Therefore boundedness forces uniformly bounded finite `ell^1` sums, hence `a in ell^1`. The same phase alignment in (13), followed by finite-section approximation, makes (10) an equality and proves (9).

This separates the natural infinite family into three exact regimes:

\[
\begin{array}{c|c}
\text{coefficient class}&\text{operator status}\\ \hline
 a\notin\ell^2&\text{nonclosable}\\
 a\in\ell^2\setminus\ell^1&\text{closable but unbounded}\\
 a\in\ell^1&\text{bounded, }\|A_a\|=\|a\|_1.
\end{array}
\tag{14}
\]

## 4. The source-derived Jacobian degree factor misses the closability region by one full unit

PC-373 derives the Jacobian-weighted Chebyshev transfer and PC-374 shows that on the half-density line `Re(s)=1/2` there is a common unitary `J_s` such that

\[
\mathcal L_{p,s}
=p^{1-s}J_s^{-1}P_pJ_s.
\tag{15}
\]

The corresponding degree-weighted Chebyshev-side family is therefore

\[
A_s:=\sum_p p^{1-s}P_p,
\tag{16}
\]

with

\[
|a_p(s)|=p^{1-\sigma},
\qquad \sigma=\operatorname{Re}s.
\]

Euler's divergence of the reciprocal-prime sum and the elementary comparison for prime powers give

\[
\sum_p|a_p(s)|^2
=
\sum_p p^{-(2\sigma-2)}
<\infty
\iff
\sigma>\frac32,
\tag{17}
\]

and

\[
\sum_p|a_p(s)|
=
\sum_p p^{-(\sigma-1)}
<\infty
\iff
\sigma>2.
\tag{18}
\]

Combining (4) and (9),

\[
\boxed{
\begin{aligned}
\operatorname{Re}s\le\frac32&:\quad A_s\text{ is nonclosable},\\
\frac32<\operatorname{Re}s\le2&:\quad A_s\text{ is closable but unbounded},\\
\operatorname{Re}s>2&:\quad A_s\text{ is bounded}.
\end{aligned}}
\tag{19}
\]

In the bounded region its norm is exactly

\[
\boxed{
\|A_s\|=\sum_p p^{1-\sigma}=P(\sigma-1),
}
\tag{20}
\]

where `P` is the classical prime-zeta function. The imaginary part of `s` changes only the coordinate phases `p^{-it}`; it does not affect closability, boundedness, or the norm.

Most importantly, at `s=1/2+it`, equation (15) is a unitary conjugacy and (19) gives

\[
\boxed{
\sum_p\mathcal L_{p,1/2+it}
\text{ on the transported finite-mode core is nonclosable.}
}
\tag{21}
\]

Thus the canonical half-density completion from PC-374 does not acquire a hidden global operator by simply summing all prime refinement transfers. The direct infinite sum fails before any spectral determinant or zero-set question can even be posed.

The normalized equal-channel aggregate is still more immediate: `sum_p P_p` corresponds to `a_p=1`, which is not in `ell^2`, hence is nonclosable by (4).

## 5. Matched prime-power controls show that the thresholds are degree-growth geometry

The numbers `3/2` and `2` in (19) should not themselves be given arithmetic significance. Replace the prime degrees `p` by the pairwise-coprime composite degrees `p^r`, `r>=2`, and consider

\[
A_s^{(r)}=\sum_p p^{r(1-s)}P_{p^r}.
\tag{22}
\]

Exactly the same proof applies because

\[
P_{p^r}e_{p^r}=e_1,
\qquad
(P_{p^r})^*e_m=e_{p^r m},
\]

and under the Bohr lift `(P_{p^r})^*` is multiplication by `z_p^r`. Hence

\[
A_s^{(r)}\text{ is closable}
\iff
\sum_p p^{2r(1-\sigma)}<\infty
\iff
\boxed{\sigma>1+\frac1{2r}},
\tag{23}
\]

while boundedness holds exactly for

\[
\boxed{\sigma>1+\frac1r}.
\tag{24}
\]

So these vertical thresholds move continuously with the chosen refinement-degree growth. They are Hardy/sequence-space summability boundaries, not an invariant critical line selected by prime-circle arithmetic. The actual RH-looking line `Re(s)=1/2` remains far inside the nonclosable region for every such control.

## 6. Prior-art and novelty audit

The ambient functional analysis is classical. Håkan Hedenmalm, Peter Lindqvist and Kristian Seip, *A Hilbert space of Dirichlet series and systems of dilated functions in L^2(0,1)*, Duke Math. J. 86 (1997), 1--37, DOI `10.1215/S0012-7094-97-08601-4`, establishes the square-summable Dirichlet-series/infinite-polydisk model and its multiplier algebra. The modern multiplier theory recorded in `SOURCES.md` by Fernández Vidal--Galicer--Sevilla-Peris gives the same surrounding framework. The convergence boundary of `sum_p p^{-u}` at `Re(u)=1` is standard Euler-product/prime-zeta theory.

Targeted searches around Hardy spaces of Dirichlet series, infinite-polydisk multipliers, linear symbols, closable unbounded multipliers and weighted backward shifts found the operator-theoretic ingredients inside this established framework. No historical novelty is claimed for the abstract `ell^2` closability test, the `ell^1` multiplier criterion, or the prime-zeta thresholds.

The project-local delta is not the abstract theorem in isolation. PC-376 classified every finite coprime Chebyshev transfer family as a universal polydisk shift and explicitly left genuinely infinite global operations as a surviving possibility. Equations (4)--(21) classify the most direct such operation: the literal linear sum over all prime refinement degrees, including the non-unimodular factor already forced by the Jacobian transfer. It does not survive as a closed operator at the half-density line.

This is distinct from PC-178. There the nonclosability comes from a point-mass Toeplitz form along each single prime-valuation axis of the resultant kernel. Here each `P_p` is individually bounded; nonclosability appears only when infinitely many distinct prime refinement channels are aggregated, and its exact boundary is the global coefficient condition `a in ell^2`.

## 7. Boundary of the negative result and falsification checks

This finding closes only the **direct linear all-prime assembly on the canonical finite-mode core**. It rules out obtaining an RH-facing closed operator merely by summing the PC-374/PC-376 prime transfer channels with equal normalized weights or with the raw degree factor `p^{1-s}`. It also shows that inserting sufficient scalar damping to repair the operator necessarily moves the construction into ordinary `ell^2`/`ell^1` summability and Hardy-multiplier territory.

It does not rule out an independently geometry-forced coefficient sequence in `ell^2` carrying additional arithmetic structure, a nonstandard domain not obtained as the closure of the finite-mode graph, nonlinear or matrix-valued cross-prime couplings, interactions before the Chebyshev quotient, or a genuinely global topology in which the channels do not assemble as the scalar sum (2). Those possibilities require new source data, not merely a different interpretation of the same divergent linear series.

The load-bearing checks are exact and local:

1. verify (3) directly from `P_p e_n` and finite prime divisibility;
2. for `a notin ell^2`, verify the graph witness (5)--(6), which proves nonclosability without spectral assumptions;
3. for `a in ell^2`, verify that every basis vector lies in `D(A_a^*)`, making the adjoint densely defined;
4. under the Bohr lift, verify that `A_a^*` is multiplication by the linear symbol (12), and use finite-coordinate phase alignment to recover exactly `sum|a_p|`;
5. test the endpoint exponents using divergence of `sum_p1/p`;
6. repeat with the prime-power controls (22) to confirm that the vertical thresholds move with degree growth and are not RH invariants.

## Research consequence

PC-376's finite-family collapse could not by itself exclude a new phenomenon produced only after infinitely many refinement degrees were assembled. The canonical scalar assembly is now classified completely: its graph closes exactly at the `ell^2` coefficient boundary and becomes bounded only at `ell^1`. The half-density transfer coefficients lie far outside even the first boundary. Therefore an infinite Prime-Circle refinement mechanism that remains relevant to RH must contain **additional global structure before or during assembly**; the literal sum of the existing Chebyshev transfer channels cannot supply it.