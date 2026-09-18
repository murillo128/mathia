# NB-207 — Fejér window majorants remove the harmonic loss at the Ford frontier

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + POSITIVE-EULER + SOURCE-ACQUISITION + FEJER-MAJORANT + FORD-REFINEMENT + SECOND-ORDER-FRONTIER + METHOD-BOUNDARY`.

`NB-205` transfers Ford's explicit bound for logarithmic exponential sums to the positive Euler shell through Erdős--Turán. At angular resolution `1/X_a`, that transfer pays a harmonic factor `log X_a`; after the Euler atom cap is applied, the favorable source mass is bounded by a term of size

\[
X_a\log X_a\,U,
\]

where `U` is the normalized exponential-sum bound. `NB-206` then shows that improving the exponential-sum exponent is delicate in the coupled limit.

There is, however, a loss in the transfer itself that can be removed without changing the arithmetic input. A positive trigonometric majorant built from the Fejér kernel detects one short favorable arc using Fourier coefficients with bounded total `l^1` mass. Consequently the carrier occupancy bound is

\[
\boxed{
\frac{\#E_{a,t}(q)}{x_a}
\ll
\frac q{X_a}+U,
}
\tag{1}
\]

rather than the Erdős--Turán bound `q/X_a + (log X_a)U`. Combining (1) with the same normalized Euler atom cap gives

\[
\boxed{
\sum_{n\in E_{a,t}(q)}w_{n,a}
\ll
q+X_aU.
}
\tag{2}
\]

For Ford's estimate this removes the second-order `log log X_a` tariff created by the harmonic sum. More precisely, writing

\[
X:=X_a=\log x_a,\qquad Q:=\log|t|,
\]

there are constants `C_0,C_1,c>0`, depending only on the fixed shell parameters, such that for all sufficiently small `a`, if `|t|>=e^Delta x_a` and

\[
\boxed{
\frac{(X-C_0)^3}
{133.66\,[Q+\log(C_0X)]^2}
\ge
\log X+C_1,
}
\tag{3}
\]

then

\[
\boxed{
\mathcal A_a(t)\ge \frac cX.
}
\tag{4}
\]

Thus the Ford boundary from `NB-205` can be approached with a relative buffer of order `1/log X`, rather than only a fixed relative margin. The remaining `X` in (2) is not another avoidable discrepancy artifact: for any argument that knows only carrier cardinality and the pointwise atom cap `w_n\ll X/x`, that factor is sharp by an exact finite-dimensional extremal lemma. Beating the `log X` exponent threshold in (3) therefore requires source-specific information about the actual von-Mangoldt weights, not a sharper source-blind interval-count transfer.

## 1. Setup inherited from the positive Euler shell

Keep the notation of `NB-205`:

\[
x_a=e^{r_0/a},\qquad X_a=\log x_a=\frac{r_0}{a},\qquad y_a=e^\Delta x_a,
\]

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=
\frac{\Lambda(n)n^{-1-a}}{D_a}
\mathbf 1_{[x_a,y_a)}(n),
\]

and

\[
\mathcal A_a(t):=
\sum_n w_{n,a}|e^{-it\log n}-1|.
\tag{5}
\]

By the prime number theorem, `D_a\asymp_{r_0,\Delta}1`, and on the fixed multiplicative shell

\[
\boxed{
w_{n,a}\ll_{r_0,\Delta}\frac{X_a}{x_a}.
}
\tag{6}
\]

Fix a sufficiently small constant `q>0`, and let

\[
E_{a,t}(q):=
\left\{
n\in[x_a,y_a):
\operatorname{dist}(t\log n,2\pi\mathbb Z)
\le\frac q{X_a}
\right\}.
\tag{7}
\]

`NB-205` bounded this set with Erdős--Turán. The only change here is to majorize this one specific short arc directly.

## 2. A Fejér majorant has bounded Fourier `l^1` cost

Work on the torus `T=R/Z`. Let `I` be any interval of length `ell<1/4`, and choose an integer `H` with

\[
H\asymp \ell^{-1}.
\tag{8}
\]

Write the normalized Fejér kernel as

\[
F_H(u)
=
\frac1{H+1}
\left(
\frac{\sin \pi(H+1)u}{\sin \pi u}
\right)^2.
\tag{9}
\]

It is nonnegative, has integral one, and has Fourier support `|h|<=H`. Put

\[
r=\frac1{2(H+1)}
\]

and let `J` be the interval obtained by enlarging `I` by `r` at each endpoint. For every `theta in I`, the translate `J-theta` contains `[-r,r]`.

For `|u|<=r`, the elementary inequalities

\[
\sin(\pi(H+1)|u|)\ge 2(H+1)|u|,
\qquad
\sin(\pi|u|)\le\pi|u|
\]

give

\[
F_H(u)\ge\frac{4(H+1)}{\pi^2}.
\]

Hence

\[
\eta_H:=\int_{-r}^r F_H(u)\,du\ge\frac4{\pi^2}.
\tag{10}
\]

Define

\[
P_{I,H}(\theta)
:=
\eta_H^{-1}(\mathbf 1_J*F_H)(\theta).
\tag{11}
\]

Then `P_(I,H)>=1` on `I` and `P_(I,H)>=0` everywhere. Writing

\[
P_{I,H}(\theta)=\sum_{|h|\le H}c_he^{2\pi i h\theta},
\]

we have

\[
c_0=\eta_H^{-1}|J|
\ll \ell+H^{-1}
\ll\ell,
\tag{12}
\]

and, for every `1<=|h|<=H`,

\[
|c_h|
\le
\eta_H^{-1}|\widehat{\mathbf 1_J}(h)|
\le
\eta_H^{-1}|J|.
\]

Therefore

\[
\boxed{
\sum_{1\le|h|\le H}|c_h|
\ll H|J|
\ll1.
}
\tag{13}
\]

The last estimate is the whole gain. Erdős--Turán uses coefficients of size `1/h` and pays `sum_(h<=H)1/h\asymp log H`; a direct positive majorant for one prescribed interval has bounded total Fourier cost when its degree is matched to the inverse interval length.

This is classical Fejér-kernel technology. The proof above is included so that no new external harmonic-analysis theorem is load-bearing.

## 3. Carrier occupancy without the harmonic loss

Let

\[
\theta_n:=\frac{t\log n}{2\pi}\pmod1,
\qquad
S_h(t):=
\sum_{x_a\le n<y_a}e^{ih t\log n}.
\tag{14}
\]

The favorable condition (7) is an interval in `T` of length `ell\asymp q/X_a`. Choose `H\asymp X_a/q` as in (8). Since `1_E<=P_(I,H)`, summing (11) over the integer carrier gives

\[
\#E_{a,t}(q)
\le
c_0\#([x_a,y_a)\cap\mathbb Z)
+
\sum_{1\le|h|\le H}|c_h|\,|S_h(t)|.
\tag{15}
\]

If

\[
\sup_{1\le h\le H}\frac{|S_h(t)|}{x_a}\le U,
\tag{16}
\]

then (12)--(13) imply

\[
\boxed{
\frac{\#E_{a,t}(q)}{x_a}
\ll_{q,\Delta}
\frac q{X_a}+U.
}
\tag{17}
\]

The dependence on fixed `q` can be absorbed once `q` is chosen. There is no `log X_a` multiplying `U`.

Using the atom cap (6),

\[
\boxed{
\sum_{n\in E_{a,t}(q)}w_{n,a}
\ll
q+X_aU.
}
\tag{18}
\]

This should be compared directly with equation (16) of `NB-205`, where the second term is `X_a log X_a U`.

## 4. Ford now needs to beat only `log X`

For `|t|>=e^Delta x_a`, split the fixed multiplicative shell into `O_\Delta(1)` intervals of ratio at most two and apply Ford's Theorem 2 to `h|t|`, uniformly for

\[
1\le h\le H\asymp X_a.
\]

Exactly as in `NB-205`, after absorbing the fixed shell partition and Ford's numerical prefactor, there are fixed constants `C_0,C_2>0` such that

\[
U
\le
C_2
\exp\!\left\{
-
\frac{(X-C_0)^3}
{133.66\,[Q+\log(C_0X)]^2}
\right\}.
\tag{19}
\]

Set

\[
\Phi(X,Q):=
\frac{(X-C_0)^3}
{133.66\,[Q+\log(C_0X)]^2}.
\tag{20}
\]

If

\[
\Phi(X,Q)\ge\log X+C_1
\tag{21}
\]

with `C_1` chosen sufficiently large, then

\[
XU\le C_2e^{-C_1}.
\]

Choose first a fixed small `q`, and then a fixed large `C_1`. Equation (18) then shows that the favorable set carries at most, say, half of the normalized Euler mass. For every `n` outside `E_(a,t)(q)`,

\[
|e^{-it\log n}-1|
\ge
2\sin\frac q{2X}
\gg_q\frac1X.
\tag{22}
\]

Positivity of the weights now gives

\[
\mathcal A_a(t)\gg\frac1X,
\]

which proves (3)--(4).

The leading Ford frontier is unchanged: solving `Phi(X,Q)\asymp log X` gives

\[
Q_*(X)
=
\frac1{\sqrt{133.66}}
\frac{X^{3/2}}{\sqrt{\log X}}
(1+o(1)).
\tag{23}
\]

But the approach to that frontier is sharper. Since replacing `log X` by `log X+C_1` changes its inverse square root by relative `O(1/log X)`, condition (21) allows

\[
\boxed{
Q
\le
\frac1{\sqrt{133.66}}
\frac{X^{3/2}}{\sqrt{\log X}}
\left(1-O\!\left(\frac1{\log X}\right)\right),
}
\tag{24}
\]

with a sufficiently large fixed constant in the `O` term, after the harmless `O(log X)` shift inside `Q` is absorbed. The Erdős--Turán transfer instead has to overcome `X log X`, so at this second-order level it pays an additional `log log X` in the exponent threshold.

Thus `NB-205`'s fixed-`kappa` theorem remains correct, but its harmonic factor is a feature of that discrepancy transfer, not an intrinsic tariff of the positive Euler shell.

## 5. The remaining atom tariff is exactly sharp for source-blind transfer

The factor `X` in (18) comes from converting a carrier count into positive source mass using only a pointwise atom cap. Unlike the harmonic factor, this loss cannot be removed without additional information about the weights.

Let `Omega` be any finite carrier, `E subset Omega`, and consider all probability vectors `w=(w_omega)` satisfying

\[
0\le w_\omega\le b,
\qquad
\sum_{\omega\in\Omega}w_\omega=1.
\tag{25}
\]

Assuming this class is nonempty,

\[
\boxed{
\sup_w\sum_{\omega\in E}w_\omega
=
\min\{1,b|E|\}.
}
\tag{26}
\]

The upper bound is immediate. If `b|E|>=1`, distribute total mass one inside `E`, never exceeding `b`. If `b|E|<1`, put mass `b` on every point of `E` and distribute the remaining `1-b|E|` on `Omega\E`; this is possible because nonemptiness gives `b|Omega|>=1`, hence the complement capacity is at least `1-b|E|`.

For the Euler shell, `b\asymp X/x`. Therefore an argument that uses only a bound on `#E` and the cap `w_n\ll X/x` cannot force a fixed amount of mass outside `E` unless

\[
\frac{\#E}{x}\ll\frac1X.
\tag{27}
\]

Consequently a source-blind Fourier occupancy argument must still achieve

\[
U\ll\frac1X,
\tag{28}
\]

which is exactly the exponent requirement `Phi>=log X+O(1)` in (21).

The extremizing probability vectors in this lemma are not claimed to be Euler weights. Equation (26) is a **method boundary**, not an arithmetic counterexample: it says that cardinality plus an atom cap contains no information capable of beating the `X` tariff. Any further improvement has to use additional structure of the actual weights.

## 6. Representation audit and research frontier

The Fejér step is generic. It applies to any phase carrier for which one controls all Fourier sums up to frequency `H\asymp1/ell`; neither primes nor the Nyman--Beurling problem are needed. The exact atom-cap extremal statement is also generic finite-dimensional linear programming.

The arithmetic content enters in three places: the phase is `t log n`, Ford supplies a uniform bound for its integer exponential sums at the required growing harmonics, and the positive Euler shell has total mass `\asymp1` with atom cap `\asymp X/x` by PNT normalization. These ingredients produce the specific Ford frontier (23).

No new load-bearing literature theorem is introduced here. Fejér majorants and their sharper Selberg--Vaaler relatives are classical prior art; the required majorant is proved explicitly above. Ford's estimate and PNT are already anchored in `SOURCES.md`. The project-local contribution is the transfer diagnosis: **the `log X` harmonic loss in `NB-205` is removable, whereas the remaining `X` source-blind atom tariff is exact.**

This also sharpens the next useful question. Improving the unweighted carrier discrepancy further cannot change the exponent threshold below `log X` while the proof ends with only (6). The natural positive-source route is now to estimate a genuinely source-aware quantity, for example von-Mangoldt-weighted logarithmic Fourier coefficients or a weighted window majorant, so that favorable Euler mass is controlled directly rather than by `#E times max w_n`.

The larger limitations remain unchanged. Positivity is load-bearing: signed or complex synthesis can cancel between phase sectors. And this is still a source-acquisition theorem, not a direct lower bound for the optimal Nyman--Beurling distance; a destination-coupled argument must still show which Euler acquisition condition is forced by a successful approximant.

## Consequence

`NB-205` reached the Vinogradov--Korobov height with a fixed relative margin. `NB-206` showed that importing a formally stronger fixed-epsilon VMVT exponent does not safely close that margin. The present finding instead improves the deterministic transfer around Ford's existing theorem: a Fejér window majorant removes the harmonic `log X` loss and reaches to within relative `O(1/log X)` of the Ford boundary.

What remains is now cleanly separated. The harmonic discrepancy loss was methodological and removable. The `X` atom tariff is also methodological, but **provably unavoidable for every source-blind cardinality-plus-cap transfer**. Passing that barrier requires arithmetic information about where the Euler mass actually sits, rather than a more efficient way to count the underlying integers.
