# MC-341 — Finite-dimensional analog transcripts pay exponential spread for source capacity

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-340` closes the finite-state loophole for source-natural dephasing, but leaves an explicit gap: one real coordinate can encode an arbitrary finite source alphabet if arbitrarily tiny separations or arbitrarily large dynamic range are allowed. Once the transcript is required to have a source-natural Euclidean metric, that loophole has an exact geometric price.

Keep the reciprocal endpoint notation of `MC-338`--`MC-340`:

\[
G=\mathbf F_2^R,
\qquad
\Xi=G\setminus\{0\},
\qquad
m=2^R-1,
\]

with source vector

\[
X=(X_1,\ldots,X_R),
\qquad
X_i=x_i(A),
\qquad
A\sim\operatorname{Unif}(\Xi).
\]

Let the complete coefficient observations `Y=(Y_1,\ldots,Y_R)` be downstream of a deterministic real transcript

\[
T=\Phi(X)\in\mathbf R^d,
\qquad
X\longrightarrow T\longrightarrow Y.
\tag{1}
\]

Write

\[
S_T:=\operatorname{supp}(T),
\qquad
K_T:=|S_T|,
\]

and, when `K_T>=2`, define its Euclidean **spread**

\[
\operatorname{spr}(T)
:=
\frac{D_T}{\Delta_T},
\qquad
D_T:=\max_{u,v\in S_T}\|u-v\|_2,
\qquad
\Delta_T:=\min_{u\ne v}\|u-v\|_2.
\tag{2}
\]

This is scale invariant: rescaling the transcript changes `D_T` and `Delta_T` by the same factor.

Suppose a coefficient family has normalized energy

\[
\mathcal E(W)\le C
\]

and achieves nontrivial all-mode dephasing

\[
\delta(W)\le1-\eta
\qquad(0<\eta\le1).
\]

Define

\[
L_R(\eta,C)
:=
\left[
\frac R2
\left(
\frac{\eta^2}{C}-\frac1{m^2}
\right)
-
\operatorname{TC}(X)
\right]_+.
\tag{3}
\]

Then

\[
\boxed{
K_T\ge e^{L_R(\eta,C)}
}
\tag{4}
\]

and every `d`-dimensional Euclidean realization of the transcript obeys

\[
\boxed{
\operatorname{spr}(T)
\ge
\frac12
\left(
\exp\!\left(\frac{L_R(\eta,C)}d\right)-1
\right).
}
\tag{5}
\]

Thus the `MC-340` linear information requirement cannot be hidden for free inside a small number of analog coordinates. For fixed `eta>0` and `C<infinity`, the punctured source law has `TC(X)=O(1)`, so

\[
L_R(\eta,C)=\frac{\eta^2}{2C}R+O(1).
\tag{6}
\]

Consequently:

- if `d=O(1)`, every such transcript has exponentially growing spread;
- if `d=o(R/log R)`, every such transcript has superpolynomial spread;
- if `spr(T)<=R^B` for fixed `B`, then necessarily

\[
\boxed{
d=\Omega(R/\log R).}
\tag{7}
\]

There is a sharper matched-filter statement. If

\[
\mathcal E(W)\le1,
\qquad
\delta(W)=0,
\]

then `MC-340` forces the transcript to determine the entire source vector. The support of `X` has

\[
K_X=
\begin{cases}
2^R-1, & R\text{ even},\\
2^{R-1}, & R\text{ odd},
\end{cases}
\tag{8}
\]

so `T` must be injective on at least `2^(R-1)` source states and

\[
\boxed{
\operatorname{spr}(T)
\ge
\frac12
\left(2^{(R-1)/d}-1\right).
}
\tag{9}
\]

For a scalar transcript (`d=1`), ordering the distinct real values sharpens the elementary packing constant to

\[
\boxed{
\operatorname{spr}(T)
\ge K_X-1
\ge2^{R-1}-1.
}
\tag{10}
\]

Near the matched-filter floor, `MC-340` gives another direct form. If

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon,
\]

put

\[
q_\varepsilon
:=
\varepsilon-\frac{\varepsilon^2}{2}
\]

and

\[
L_R^{\mathrm{near}}(\varepsilon)
:=
\left[
H(X)-R h(q_\varepsilon)
\right]_+.
\tag{11}
\]

Then

\[
\boxed{
\operatorname{spr}(T)
\ge
\frac12
\left(
\exp\!\left(\frac{L_R^{\mathrm{near}}(\varepsilon)}d\right)-1
\right).
}
\tag{12}
\]

Whenever `h(q_epsilon)<log 2`, the exponent in `(12)` is linear in `R/d`. Hence a fixed-dimensional, well-conditioned analog transcript cannot even approach exact dephasing at unit coefficient energy.

No estimate for `M(x)` follows. The result is a finite endpoint conditioning theorem. Its value is to replace the statement "one real number can encode all source bits" by a quantitative dichotomy: **either expose many metric degrees of freedom, or hide the source information in exponentially fine analog separation.**

## 1. MC-340 forces exponentially many distinguishable transcript states

Because `T` is deterministic from `X`,

\[
I(X;T)=H(T).
\tag{13}
\]

The Markov condition `(1)` and data processing give

\[
I(X;Y)\le I(X;T)=H(T)\le\log K_T.
\tag{14}
\]

`MC-340` proves that `delta(W)<=1-eta` and `E(W)<=C` imply

\[
I(X;Y)
\ge
\frac R2
\left(
\frac{\eta^2}{C}-\frac1{m^2}
\right)
-
\operatorname{TC}(X).
\tag{15}
\]

Combining `(14)` and `(15)` proves `(4)`. Since `MC-340` also computes

\[
\operatorname{TC}(X)\to0
\quad(R\to\infty,\ R\text{ even}),
\qquad
\operatorname{TC}(X)\to\log2
\quad(R\to\infty,\ R\text{ odd}),
\]

formula `(6)` follows.

This step is representation independent: it uses only source information. Geometry enters only after one chooses an actual metric transcript in which robustness or conditioning is meaningful.

## 2. Euclidean packing converts state capacity into a spread lower bound

Let `K=K_T` and suppose `K>=2`. Around every point of `S_T` place an open Euclidean ball of radius `Delta_T/2`. The balls are disjoint by definition of minimum separation.

Fix any support point `t_0`. Every center lies within distance `D_T` of `t_0`, so all `K` disjoint balls lie inside the ball centered at `t_0` with radius

\[
D_T+\frac{\Delta_T}{2}.
\]

Comparing `d`-dimensional Euclidean volumes gives

\[
K\left(\frac{\Delta_T}{2}\right)^d
\le
\left(D_T+\frac{\Delta_T}{2}\right)^d.
\tag{16}
\]

Taking `d`-th roots and rearranging yields the classical packing inequality

\[
\frac{D_T}{\Delta_T}
\ge
\frac{K^{1/d}-1}{2}.
\tag{17}
\]

Substitution of `(4)` proves `(5)`.

If the transcript is complex-valued, `T in C^d`, the same argument applies after identifying `C^d` with `R^(2d)`; the denominator `d` in `(5)`, `(9)` and `(12)` is then replaced by `2d`.

For `d=1`, sort the distinct transcript values. `K-1` adjacent gaps are each at least `Delta_T`, so

\[
D_T\ge(K-1)\Delta_T,
\]

which proves the sharper scalar inequality `(10)`.

## 3. Exact and near-exact dephasing give stronger capacity than constant-factor dephasing

At `E(W)<=1` and `delta(W)=0`, equation (10) of `MC-340` gives

\[
I(X;Y)=H(X),
\]

so `H(X|Y)=0`: `Y` determines `X`. Since `Y` is downstream of `T`, `T` must also determine `X` and is therefore injective on the support of `X`.

For even `R`, the source-character map is a bijection on the full cube and puncturing removes exactly one state, giving `K_X=2^R-1`. For odd `R`, there is one parity relation and the image contains `2^(R-1)` states. This proves `(8)`--`(10)`.

For `delta(W)<=epsilon` at unit energy, equation (9) of `MC-340` gives

\[
I(X;Y)
\ge
H(X)-R h(q_\varepsilon).
\tag{18}
\]

Applying `(14)` and then `(17)` proves `(12)`.

The difference between `(5)` and `(12)` is useful. Constant-factor dephasing needs only a fixed positive information rate, while near-exact matched-filter dephasing approaches the full `log 2` nats per source. Both force exponential state packing in fixed metric dimension, but with different exponents.

## 4. Prior art and novelty boundary

The geometric ingredient is classical metric entropy / Euclidean packing, not a new theorem. Roman Vershynin, *High-Dimensional Probability: An Introduction with Applications in Data Science*, 2nd ed., Cambridge University Press (2026), develops packing and covering numbers together with their standard volume bounds; the author's official open version is available at `https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-2.pdf`. In computational geometry the scale-free ratio of largest to smallest pairwise distance is standardly called the **spread** of a point set; for example Jeff Erickson, *Dense point sets have sparse Delaunay triangulations*, Discrete & Computational Geometry 33 (2005), 83--115, arXiv `cs.CG/0110030`, uses exactly that terminology.

A targeted literature audit on 17 September 2026 found no reason to claim novelty for the packing inequality, spread, metric entropy, or low-dimensional embedding language. `MC-340` already establishes the source-information lower bound. The durable Mathia delta here is only their exact specialization and composition: the reciprocal endpoint's linear source-information requirement implies `(5)`, `(9)` and `(12)`, so low syntactic dimension can evade the information gate only by paying a quantitatively large metric spread.

## Boundaries and falsification tests

- **The Euclidean metric must be source-natural.** Mutual information in `MC-340` is invariant under arbitrary invertible re-encoding; spread is not. A candidate cannot be rejected merely because one arbitrary coordinate chart makes its spread large. The theorem becomes meaningful only after the analytic construction supplies a canonical norm, metric, finite-precision scale, or stability notion.
- **Large spread is not itself a contradiction.** A noiseless exact real statistic may encode exponentially many states with exponentially small separations. The result prices that escape; it does not forbid it.
- **Transcript spread and coefficient energy are distinct currencies.** `E(W)` enters through `MC-340`; `spr(T)` measures conditioning of the source transcript. No inequality identifying the two is assumed here.
- **The Markov factorization is load-bearing.** All coefficient observations being charged must be downstream of `T`. Hidden side information outside the transcript invalidates `(14)` and must be included in the charged transcript.
- **The finite source model remains the scope.** Nothing here proves a metric-capacity bound for a natural analytic Möbius transcript, improves `M(x)`, or supplies a zero-free region.
- **The volume constant is intentionally crude.** Sharper sphere-packing or coding bounds can improve constants but cannot change the exponential `R/d` dependence relevant to this obstruction.
- **No arithmetic randomness assumption is used.** The theorem depends only on the exact source law and the already proved `MC-340` information requirement.

## Consequence for the research line

The continuous-coordinate loophole after `MC-340` is now sharply localized. Counting real or complex coordinates is indeed meaningless by itself, because a single analog value can encode the complete finite source state. But if the actual arithmetic transcript comes with a natural metric and is required to remain polynomially conditioned, bounded-energy dephasing forces at least `Omega(R/log R)` real metric dimensions; fixed-dimensional transcripts require exponential spread.

The next arithmetic question is therefore concrete: for a genuine Möbius-derived coefficient architecture, identify the canonical transcript metric and prove either that its spread/conditioning is controlled at the relevant scale or that achieving the needed source information necessarily drives that conditioning cost superpolynomially. Without such a source-natural metric theorem, analog re-encoding remains a real escape rather than an eliminated loophole.