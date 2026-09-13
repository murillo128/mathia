# FD-083 — annular atom cap forces full-counting constant occupation

**Status:** `EXACT-DERIVED + ANNULAR-ANTI-CONCENTRATION + CONSTANT-POINTWISE-OCCUPATION + FULL-COUNTING-EXPONENT + FIXED-POWER-WINDOW-ABUNDANCE + SCHUR-TRANSVERSE-ABUNDANCE`.

`FD-081` proves that constant-strength pointwise nonsquarefree Jordan occupation is power-syndetic, while `FD-082` identifies the exact limitation of that statement: first passage alone is compatible with only `(log log X)^2` good horizons below `X`. The missing information is whether one physical horizon can carry essentially all the energy of many good annuli.

The physical Schur energy has a simple atom cap that rules out that concentration. `FD-046` gives, for every fixed `sigma>Theta`, the source envelope `|mathcal H(n)|<<_sigma n^sigma`; because `2sigma>1`, it implies

\[
E_{H,D}\ll_{D,\sigma}H^{2\sigma}
\]

and hence, for the logarithmic annular atom

\[
a_H:=\lambda_HE_{H,D},
\qquad
\lambda_H=\log\frac{H+1}{H},
\]

one has

\[
\boxed{a_H\ll_{D,\sigma}H^{2\sigma-1}.}
\tag{1}
\]

On the other hand `FD-078` proves that every fixed power annulus has total physical energy

\[
A_\alpha(Y):=
\sum_{Y^{1-\alpha}<H\le Y}a_H
=Y^{2\Theta+o(1)}.
\tag{2}
\]

Thus no individual horizon can carry more than a `Y^{-1+o(1)}` fraction of the annular energy at the zero-frontier exponent. When `FD-080` supplies an annulus with constant energy-weighted nonsquarefree occupation, a fixed positive fraction of its total energy must therefore be spread over `Y^{1-o(1)}` distinct pointwise horizons. This converts annular recurrence into full-counting-exponent constant pointwise occupation.

Fix a Schur head `D>=1`, a nonsquarefree integer `q>1`, and

\[
w(q):=\frac{J_2(q)}{q^2},
\qquad
c_q:=w(q)q^{-2\Theta},
\qquad
0<\eta<c_q.
\tag{3}
\]

Retain

\[
\nu_{H,D}:=\frac{U_{H,D}}{E_{H,D}},
\qquad 0\le\nu_{H,D}\le1,
\tag{4}
\]

with the harmless convention `nu_(H,D)=0` when `E_(H,D)=0`. Then for every fixed `epsilon>0`,

\[
\boxed{
\lim_{X\to\infty}
\frac{
\log\!\left(
1+\#\{H\in\mathbb Z:X<H\le X^{1+\epsilon},\ \nu_{H,D}>\eta\}
\right)
}{\log X}
=1+\epsilon.
}
\tag{5}
\]

In particular, with

\[
N_\eta(X):=\#\{H\le X:\nu_{H,D}>\eta\},
\]

one has

\[
\boxed{
\lim_{X\to\infty}
\frac{\log(1+N_\eta(X))}{\log X}=1.
}
\tag{6}
\]

For `q=4`, `w(4)=3/4` and `Theta<=1`, so `c_4>=3/64`. Hence (5)--(6) hold unconditionally for every fixed

\[
0<\eta<\frac3{64}.
\tag{7}
\]

Under RH, the admissible four-adic threshold extends to every `eta<3/16`.

## 1. Every annular energy atom is below the total scale by one full counting power

`FD-046` proves that for every fixed `sigma>Theta`,

\[
|\mathcal H(n)|\le C_\sigma n^\sigma.
\tag{8}
\]

Since

\[
E_{H,D}
=
\sum_{D<r\le H}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2
\]

and

\[
0<\frac{J_2(r)}{r^2}\le1,
\]

we obtain

\[
E_{H,D}
\le
C_\sigma^2H^{2\sigma}
\sum_{r>D}r^{-2\sigma}
\ll_{D,\sigma}H^{2\sigma}.
\tag{9}
\]

The convergence is valid because Hardy's theorem gives `Theta>=1/2`, hence `sigma>1/2`. Also

\[
\lambda_H=\log(1+H^{-1})\le H^{-1},
\]

so (9) gives (1). In particular, for every `H<=Y`,

\[
\boxed{
a_H\ll_{D,\sigma}Y^{2\sigma-1}.}
\tag{10}
\]

Meanwhile `FD-078` gives the full limit

\[
\frac{\log(1+A_\alpha(Y))}{\log Y}\longrightarrow2\Theta
\tag{11}
\]

for every fixed `0<alpha<1`. Since `2Theta>0`, the annular energy tends to infinity on the logarithmic scale, and for every fixed `delta>0`, eventually

\[
A_\alpha(Y)\ge Y^{2\Theta-\delta}.
\tag{12}
\]

Combining (10)--(12), any subset of the annulus that carries a fixed positive fraction of `A_alpha(Y)` must contain at least

\[
Y^{1-2(\sigma-\Theta)-\delta+o(1)}
\]

distinct horizons. Since `sigma>Theta` and `delta>0` can be arbitrarily small, a fixed energy fraction requires `Y^{1-o(1)}` physical atoms.

## 2. A constant annular occupation forces `Y^(1-o(1))` constant pointwise witnesses

Fix constants

\[
0<\eta<\eta_0<c_q
\tag{13}
\]

and a fixed annulus parameter `0<alpha<1`. Write

\[
A=A_\alpha(Y)
=\sum a_H,
\qquad
B=B_\alpha(Y)
=\sum a_H\nu_{H,D},
\qquad
\Omega(Y)=\frac BA,
\tag{14}
\]

where all sums in this section are over `Y^(1-alpha)<H<=Y`.

Suppose

\[
\Omega(Y)>\eta_0.
\tag{15}
\]

Let

\[
\mathcal G_\eta(Y)
:=
\{H:Y^{1-\alpha}<H\le Y,\ \nu_{H,D}>\eta\}
\]

and let

\[
A_\eta(Y):=\sum_{H\in\mathcal G_\eta(Y)}a_H.
\]

Using only `0<=nu<=eta` off `G_eta` and `nu<=1` on it,

\[
B
\le
\eta(A-A_\eta)+A_\eta
=
\eta A+(1-\eta)A_\eta.
\tag{16}
\]

Together with (15), this forces

\[
\boxed{
A_\eta(Y)
>
\frac{\eta_0-\eta}{1-\eta}\,A_\alpha(Y).
}
\tag{17}
\]

Thus a **fixed positive fraction of the entire physical annular energy** lies on horizons whose pointwise occupation already exceeds the fixed threshold `eta`.

Apply the atom cap (10). For every `sigma>Theta`,

\[
\#\mathcal G_\eta(Y)
\gg_{D,\sigma,\eta,\eta_0}
\frac{A_\alpha(Y)}{Y^{2\sigma-1}}.
\tag{18}
\]

Using (12), for every `delta>0`,

\[
\#\mathcal G_\eta(Y)
\gg
Y^{1-2(\sigma-\Theta)-\delta}
\tag{19}
\]

along every sufficiently large endpoint satisfying (15). Letting `sigma` decrease to `Theta` and then `delta` decrease to zero yields the exact counting exponent

\[
\boxed{
\lim_{\substack{Y\to\infty\\\Omega(Y)>\eta_0}}
\frac{\log(1+\#\mathcal G_\eta(Y))}{\log Y}=1.
}
\tag{20}
\]

The upper bound in (20) is trivial because the annulus contains at most `Y` integers. The lower bound is the new anti-concentration step: positivity alone, used in `FD-081`, extracts only one witness; the physical atom cap forces almost a full counting power of distinct witnesses.

## 3. Annular first passage puts a full-counting family inside every fixed-power future window

It remains to place the good annulus from (20) inside an arbitrary prescribed physical window. Fix `epsilon>0`. Choose any real number

\[
1<t<1+\epsilon
\tag{21}
\]

and set

\[
\alpha:=1-\frac1t.
\tag{22}
\]

Then `0<alpha<1` and `1/(1-alpha)=t`. Choose a fixed `beta>0` small enough that

\[
t(1+\beta)<1+\epsilon.
\tag{23}
\]

For a large starting horizon `X`, define

\[
Z:=\left\lceil X^t\right\rceil.
\tag{24}
\]

Apply `FD-080` with the fixed annulus parameter (22), the same fixed dilation `q`, and the threshold `eta_0<c_q`. For all sufficiently large `X`, there is an annular endpoint `Y` such that

\[
Z<Y\le Z^{1+\beta},
\qquad
\Omega_{D,\alpha}(Y)>\eta_0.
\tag{25}
\]

The lower edge of this annulus lies beyond `X`:

\[
Y^{1-\alpha}
>Z^{1/t}
\ge X.
\tag{26}
\]

The upper edge stays inside the target window, because (23)--(25) give

\[
Y
\le
X^{t(1+\beta)+o(1)}
<X^{1+\epsilon}
\tag{27}
\]

for large `X`. Hence every pointwise witness counted by (20) lies inside

\[
(X,X^{1+\epsilon}].
\]

Moreover `Y>Z=X^{t+o(1)}`, so (20) gives

\[
\#\{H:X<H\le X^{1+\epsilon},\ \nu_{H,D}>\eta\}
\ge
X^{t-o(1)}.
\tag{28}
\]

The parameter `t` was arbitrary below `1+epsilon`. Therefore, for every fixed `kappa>0`, choose `t>1+epsilon-kappa`; equation (28) gives

\[
\liminf_{X\to\infty}
\frac{\log(1+\#\{X<H\le X^{1+\epsilon}:\nu_{H,D}>\eta\})}{\log X}
\ge1+\epsilon-\kappa.
\]

Letting `kappa` decrease to zero and using the trivial upper bound by the interval length proves (5).

To deduce (6), apply (5) with any fixed `epsilon>0` at the starting point

\[
X_0:=X^{1/(1+\epsilon)}.
\]

The resulting good horizons all lie below `X`, and their number is `X^{1-o(1)}`. Since `N_eta(X)<=X`, the cumulative counting exponent is exactly one.

## 4. Consequence for the `FD-082` sparsity obstruction

`FD-082` remains correct as an information-sufficiency result about `FD-081`: subpower first passage **by itself** permits an integer-ratio control with only `(log log X)^2` good horizons. The new theorem imports information that was absent from that control, namely the physical per-horizon energy envelope (1) together with the full annular energy exponent (2).

With those inputs, the sparse-control geometry is impossible for the actual occupation set. For every fixed admissible `eta`, the physical set

\[
\mathcal G_\eta=\{H:\nu_{H,D}>\eta\}
\]

has full polynomial counting exponent and, more strongly, has full ambient counting exponent inside every fixed-power future window in the sense of (5).

This resolves the **anti-concentration branch** explicitly left open by `FD-082`: one good annulus cannot be serviced by one horizon, nor by a superpolynomially sparse cluster. Its constant weighted occupation requires `Y^{1-o(1)}` distinct constant-strength pointwise witnesses.

It does **not** by itself complete the RH-facing accumulation step. The GCD/Schur arguments of `FD-022`--`FD-023` impose coherence conditions on the horizons they compare; a large set of occupied integers is not automatically a compatible integer-ratio chain, and a fixed projective gain at many unrelated horizons cannot be multiplied without a valid transport inequality. What is removed is the previous **cardinality obstruction**: scarcity of constant-strength occupied horizons can no longer explain failure of accumulation.

## 5. Stress tests and boundary of the claim

The argument is insensitive to signs of `mathcal H` because the physical energy is quadratic. It uses no independence, probabilistic anti-concentration, regularity of `nu`, or lower bound on every individual `E_(H,D)`. Horizons with zero energy simply contribute zero atoms. The only pointwise analytic input is the already-established zero-frontier envelope (8); the lower input is the annular total-energy exponent (11).

The exponent-one conclusion is deliberately weaker than positive density. A set of size `X^(1-o(1))` may have natural density tending to zero, and (5) gives no fixed positive fraction of all integers in the power window. It also does not prove eventual pointwise occupation, a bounded additive gap between good horizons, positive logarithmic density, or the original accepted clue `U_(H,D)>=c_D E_(H,D)` for every sufficiently large `H`.

The threshold loss `eta<eta_0<c_q` is essential to (17). There is no conclusion at the endpoint `eta=c_q` from the current annular recurrence theorem. Likewise the atom cap cannot be replaced merely by the limsup statement `E_(H,D)=H^(2Theta+o_power(1))` at selected horizons; the uniform upper envelope for every `sigma>Theta` is what makes (18) valid over the complete annulus.

A decisive audit is therefore straightforward. To invalidate (5), one would need either a failure of the uniform bound `E_(H,D)<<_(D,sigma) H^(2sigma)` for some `sigma>Theta`, a failure of the full annular exponent in `FD-078`, or a sequence of endpoints with `Omega>eta_0` whose `eta`-good atoms carry a fixed energy fraction while numbering only `Y^(1-delta)` for some fixed `delta>0`. Equations (10), (12), and (17) rule out the third alternative directly.

## 6. Prior-art and novelty assessment

The analytic inputs are already anchored in the line: the Littlewood--Titchmarsh zero-frontier envelope is used through `FD-046`, and Pintz's 2026 average-order theorem enters only through the persisted annular-energy result `FD-078`. A fresh search of Farey-discrepancy/Mertens literature located the classical and recent local-discrepancy work already represented in `SOURCES.md`, including Dress's absolute-discrepancy theorem and García's Mertens-based local-discrepancy formulas, and confirmed Pintz's August 2026 average-order paper. No located source states the present Schur/Jordan conclusion that a constant occupied annulus, combined with the physical atom cap, forces `Y^(1-o(1))` distinct constant-occupation horizons or the fixed-power-window counting law (5).

No priority claim is made for the elementary weighted counting step (16)--(19); it is a direct deterministic consequence of a maximum-atom bound. The candidate-new structure is its specialization to the current Farey/Mertens Schur energy and its combination with `FD-080` to close the physical sparsity escape of `FD-082`. No new external theorem is load-bearing, so `SOURCES.md` requires no change.