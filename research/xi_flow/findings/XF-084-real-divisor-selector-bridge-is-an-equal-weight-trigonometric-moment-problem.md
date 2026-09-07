# XF-084 — real-divisor selector bridge is an equal-weight trigonometric moment problem

**Status:** `EXACT-DERIVED` + `INTERFACE-REDUCTION` + `CARATHEODORY/TOEPLITZ-GATE` + `EQUAL-WEIGHT-REALIZATION-OPEN`. XF-083 proves that, *inside the class of same-degree periodic carriers whose roots are all real modulo the period*, exponentially accurate agreement of the centered logarithmic derivative on one safe center half-line forces exponentially accurate agreement of the source-visible power sums. It deliberately leaves existence open: nothing there constructs such a real-divisor carrier from transported Xi data. XF-079 simultaneously shows that the guarded selector itself only depends on the finite collection of periodic power sums that meet its visible sidebands.

Those two facts identify a simpler exact existence object. A degree-`N` real-divisor carrier is the same thing, at the level seen by the selector, as an **equal-weight `N`-atomic probability measure on the unit circle**. Its centered logarithmic derivative is automatically a Carathéodory/Herglotz function, and every finite prefix of its normalized power sums has a positive-semidefinite Hermitian Toeplitz moment matrix. Consequently any proposed Xi-to-real-divisor bridge has a finite-dimensional spectral falsifier before one attempts root placement. Conversely, matching the required visible moments by an equal-weight `N`-point quadrature is already enough to match the XF-079 selector at those sidebands; exponentially accurate approximation of the whole center-local function is stronger than the selector needs.

The positive-semidefinite condition is only the **weighted-measure relaxation**. It does not solve the equal-weight `N`-node problem, and this distinction is load-bearing at the precision used by XF-083. The live source-to-state bridge can therefore be split cleanly into (i) a Carathéodory/Toeplitz feasibility gate for the transported moment data, (ii) an equal-weight trigonometric moment realization at exactly `N=2D` nodes, and (iii) the still-separate heat/destination compatibility and positive-transition-mass obligations.

## 1. Real-divisor carriers are normalized Carathéodory functions

Use the XF-083 carrier normalization

\[
G(\theta)
=C e^{-iN\theta/2}
\prod_{j=1}^{N}(e^{i\theta}-\nu_j),
\qquad |\nu_j|=1,
\tag{1}
\]

and write

\[
P_m(G):=\sum_{j=1}^{N}\nu_j^{-m}.
\tag{2}
\]

For `w=e^{i theta}` in the open unit disk, XF-083's centered logarithmic derivative is

\[
U_G(w)
:=\partial_\theta\log G+\frac{iN}{2}
=i w\sum_{j=1}^{N}\frac1{w-\nu_j}
=-i\sum_{m\ge1}P_m(G)w^m.
\tag{3}
\]

Define the normalized transform

\[
\boxed{
\Phi_G(w)
:=1+\frac{2i}{N}U_G(w).
}
\tag{4}
\]

Using `(3)` twice gives the two exact forms

\[
\boxed{
\Phi_G(w)
=1+\frac2N\sum_{m\ge1}P_m(G)w^m
=\frac1N\sum_{j=1}^{N}\frac{\nu_j+w}{\nu_j-w}.
}
\tag{5}
\]

Every summand on the right is a unit-circle Carathéodory kernel. Hence

\[
\boxed{
\Re \Phi_G(w)
=\frac1N\sum_{j=1}^{N}
\frac{1-|w|^2}{|\nu_j-w|^2}
>0,
\qquad |w|<1.
}
\tag{6}
\]

This is an exact pointwise necessary condition for the desired real-divisor slice. In particular, if a proposed transported target field `U_*` is to satisfy

\[
|U_G(w)-U_*(w)|\le\varepsilon
\tag{7}
\]

at some interior point, then necessarily

\[
\boxed{
\Re\left(1+\frac{2i}{N}U_*(w)\right)
\ge -\frac{2\varepsilon}{N}.
}
\tag{8}
\]

A target that violates `(8)` by a margin larger than the interface error cannot be repaired by changing roots elsewhere. This test uses neither root ordering nor simplicity, and repeated real roots are allowed.

## 2. Every finite power-sum prefix obeys a Toeplitz PSD constraint

Put

\[
\mu_0:=1,
\qquad
\mu_m:=\frac{P_m(G)}N,
\qquad
\mu_{-m}:=\overline{\mu_m}.
\tag{9}
\]

For an integer `K>=1`, form the Hermitian Toeplitz matrix

\[
T_K(G):=(\mu_{a-b})_{0\le a,b\le K}.
\tag{10}
\]

For every `c=(c_0,\ldots,c_K) in C^{K+1}`,

\[
\begin{aligned}
c^*T_K(G)c
&=\sum_{a,b=0}^{K}
\mu_{a-b}c_a\overline{c_b}\\
&=\frac1N\sum_{j=1}^{N}
\left|\sum_{a=0}^{K}c_a\nu_j^{-a}\right|^2
\ge0.
\end{aligned}
\tag{11}
\]

Therefore

\[
\boxed{T_K(G)\succeq0\quad\text{for every }K.}
\tag{12}
\]

The proof is just the Gram identity `(11)`; no moment theorem is needed. This is already stronger than the separate scalar bounds `|P_m|<=N`. For example, the formally admissible normalized data

\[
\mu_1=\frac45,
\qquad
\mu_2=0
\tag{13}
\]

obey `|mu_1|,|mu_2|<=1`, but

\[
T_2=
\begin{pmatrix}
1&4/5&0\\
4/5&1&4/5\\
0&4/5&1
\end{pmatrix}
\tag{14}
\]

has eigenvalue

\[
1-\frac{4\sqrt2}{5}<0.
\tag{15}
\]

Thus no multiset of real periodic roots of any degree `N` can have `P_1=(4/5)N` and `P_2=0` simultaneously. The matrix gate detects phase correlations that coefficientwise magnitude checks miss.

## 3. XF-083 turns the PSD gate into an exponentially sharp falsifier

Let target power sums `Q_1,...,Q_K` define

\[
\widetilde\mu_0=1,
\qquad
\widetilde\mu_m=Q_m/N,
\qquad
\widetilde\mu_{-m}=\overline{\widetilde\mu_m},
\tag{16}
\]

and let `\widetilde T_K` be the corresponding Toeplitz matrix. Suppose a degree-`N` real-divisor carrier satisfies

\[
|P_m(G)-Q_m|\le\delta_m,
\qquad 1\le m\le K.
\tag{17}
\]

Each row of `T_K(G)-\widetilde T_K` contains at most two entries of size `delta_m/N` for each distance `m`, so

\[
\|T_K(G)-\widetilde T_K\|_{\rm op}
\le
\frac2N\sum_{m=1}^{K}\delta_m.
\tag{18}
\]

Since `T_K(G)` is PSD, Weyl's inequality gives the necessary condition

\[
\boxed{
\lambda_{\min}(\widetilde T_K)
\ge
-\frac2N\sum_{m=1}^{K}\delta_m.
}
\tag{19}
\]

In the particular center-local regime of XF-083, logarithmic-derivative mismatch `epsilon` gives

\[
\delta_m
\le
\left(\frac2r\right)^m
\epsilon^{1/6}M^{5/6},
\tag{20}
\]

where `r=e^{-y}` and `M=2Nr/(1-r)`. At the Xi scaling used there,

\[
N=2D,
\qquad
y=\Theta(D^{-1/2}),
\qquad
M=O(D^{3/2}),
\qquad
K=O(D^{1/2}\log\log T)=o(D).
\tag{21}
\]

Hence, if the candidate interface reaches `epsilon<=e^{-cD}`, equations `(19)`--`(21)` imply

\[
\boxed{
\lambda_{\min}(\widetilde T_K)
\ge -e^{-c'D}
}
\tag{22}
\]

for some `c'>0` and all sufficiently large `T`. The continuation loss `exp(O(K))` is subexponential in `D`, while `epsilon^{1/6}` retains an exponential margin.

Therefore a negative eigenvalue of polynomial size, or even `e^{-o(D)}` size, is a decisive **no-go certificate** for the real-divisor carrier demanded by the current source bridge. This test is finite-dimensional and can be applied to any concrete candidate moment vector before solving for roots.

There is also a useful benign regime. Gershgorin gives

\[
\lambda_{\min}(\widetilde T_K)
\ge
1-\frac2N\sum_{m=1}^{K}|Q_m|.
\tag{23}
\]

Thus if the total normalized moment mass is bounded by

\[
2\sum_{m=1}^{K}|Q_m|\le(1-\kappa)N
\tag{24}
\]

for some fixed `kappa>0`, the Toeplitz obstruction is automatically absent with margin `kappa`. In that case the hard issue is not positivity but equal-weight realization.

## 4. The XF-070 infrared quotient becomes a partial moment-completion problem

The source-visible state should **not** prescribe every low power sum. XF-070 proves that the unresolved ultra-infrared block can be quotiented in the exact selector-induced `H^3` geometry, and XF-079 shows that each visible sideband reads only its own `P_k`.

Let `S subset {1,...,K}` denote the indices actually constrained by the source-visible selector, with target values `Q_k` for `k in S`. A real-divisor carrier compatible with that selector must admit values for the unobserved moments

\[
Q_m,
\qquad m\in\{1,\ldots,K\}\setminus S,
\tag{25}
\]

such that the completed Toeplitz matrix `\widetilde T_K` passes `(12)` to the relevant error scale. The unobserved infrared moments are variables, not hidden constraints.

Thus the first existence gate is naturally a **Hermitian Toeplitz PSD completion problem**. This is exactly the right relaxation for the quotient logic of XF-070: it tests whether the visible data are compatible with *some* positive unit-circle moment state without forcing the source-invisible coordinates to be small or zero. If no PSD completion exists, no real-divisor carrier exists. If one does exist, only the weighted-measure relaxation has survived; the equal-weight degree constraint remains.

This also shows why reconstructing a whole center-local function can be unnecessarily strong for the selector. If one can find `N` unit-circle points satisfying

\[
\frac1N\sum_{j=1}^{N}\nu_j^{-k}
=\frac{Q_k}{N},
\qquad k\in S,
\tag{26}
\]

then the associated periodic root multiset has exactly the same `P_k` on every constrained sideband. XF-079 then gives the same one-center selector values there, including their phases, without first proving exponential agreement of `U_G` on a continuum of center-local points.

## 5. PSD is not the degree-`N` carrier theorem

The probability measure attached to an actual carrier is

\[
\boxed{
\rho_G
=\frac1N\sum_{j=1}^{N}\delta_{\nu_j}.
}
\tag{27}
\]

Every atom therefore has weight exactly `1/N`, with repeated roots represented by repeated atoms. This equal-weight/integer-multiplicity condition is stronger than positivity of the truncated Toeplitz matrix.

Classical Carathéodory--Fejer/Vandermonde and truncated trigonometric moment theory studies the larger problem in which the representing positive measure may have arbitrary positive weights. That classical theory explains why `(12)` is the natural weighted-measure cone, but the present finding does **not** use its converse as evidence for a Mathia carrier.

The precision distinction is severe. Even if a weighted atomic representation of the first `K` moments uses at most `K+1` atoms, the naive operation of rounding its weights to integer multiples of `1/N` gives only

\[
\|\Delta\mu\|_{\ell^\infty}
=O(K/N),
\qquad
|\Delta P_m|=O(K),
\tag{28}
\]

in the worst case. That is nowhere near the `e^{-c'D}` power-sum precision supplied by the XF-083 route. Equation `(28)` is only a warning about naive weight quantization, not a lower bound: moving equal-weight nodes can do much better, and exact Chebyshev-type trigonometric quadratures are known under additional regularity hypotheses.

This isolates a concrete constructive alternative. Rather than approximate the whole Gaussian/Xi quotient by an arbitrary trigonometric polynomial and then try to repair its zeros, one may seek a **regular positive representing measure for the source-visible moment data and then an equal-weight trigonometric quadrature with exactly `N=2D` nodes**. If this can be done directly at the relevant degree, the selector prefix is realized exactly and XF-080's tiny-outer-coefficient instability is bypassed. Proving the required regularity and node budget for the Xi-derived partial moment data is a new obligation; it is not supplied here.

## 6. Stress tests and evidence boundary

The unit-circle condition is load-bearing. If roots are allowed off the circle, `(6)` and `(11)` need not hold, which is consistent with XF-081--XF-082: their exponentially invisible Vieta perturbations escape the real-divisor class. The present gate therefore does not contradict those nonidentifiability examples; it explains a finite positivity constraint they were free to violate.

Repeated roots cause no problem: `(6)`, `(11)`, and the equal-weight measure `(27)` count multiplicity automatically. Root simplicity is needed elsewhere for some zero-motion arguments, but not for this existence screen.

The PSD completion gate is necessary, not sufficient, for an `N`-root carrier. Conversely, an exact equal-weight moment realization at one time does not prove that the carrier follows the Xi heat evolution, remains in the admissible real-rooted slice for the needed interval, or carries the positive-`Lambda` transition mass required at the destination. Those remain separate obligations.

The current proposed clue `CLUE-relative-xi-source-to-guarded-selector-stability` is therefore **not promoted by this finding**. XF-073 already supplies the line-local source-specific relative periodization estimate, but the clue's transported real-divisor existence step is exactly what `(12)`--`(27)` now test rather than assume.

## 7. Prior-art and novelty boundary

The positive-real kernel `(nu+w)/(nu-w)`, Herglotz/Carathéodory representation, positive-semidefinite Toeplitz moment matrices, and Vandermonde decompositions are classical. A modern reference for the Toeplitz/Vandermonde and truncated trigonometric moment framework is Zai Yang and Lihua Xie, **Frequency-selective Vandermonde decomposition of Toeplitz matrices with applications**, *Signal Processing* 142 (2018), 157--167, DOI `10.1016/j.sigpro.2017.07.024`, arXiv:1605.02431. Equal-weight realization belongs to the classical Chebyshev-type quadrature problem; a modern quantitative reference is Shoni Gilboa and Ron Peled, **Chebyshev-Type Quadratures for Doubling Weights**, *Constructive Approximation* 45 (2017), 193--216, DOI `10.1007/s00365-016-9360-4`, arXiv:1507.01505.

A targeted novelty search also found recent work on Toeplitz minors of the **Taylor-coefficient sequence** of the Riemann xi function (W. Michalowski, *An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann xi coefficients*, arXiv:2607.16795, July 2026). That is a different Toeplitz object from `(10)`: here the entries are transported periodic **log-Vieta/root power sums**, normalized as moments of a candidate real-divisor carrier. No claim is made that Toeplitz positivity itself is new.

The line-specific contribution is the exact reduction of the live XF-083 existence gap to an equal-weight truncated trigonometric moment problem, together with the quantitative spectral falsifier `(19)`--`(22)` at the Xi scaling and the partial-completion formulation that respects XF-070's infrared quotient. No external theorem is load-bearing for those statements, so `SOURCES.md` is unchanged.

## 8. Consequence for `xi_flow`

The current bridge should no longer be phrased only as “construct a real-rooted trigonometric polynomial approximating the Gaussian/Xi quotient.” There is a more targeted decision tree. First extract the source-visible candidate moments. Then test Carathéodory positivity and the Toeplitz PSD completion problem with the unresolved infrared modes left free. A negative eigenvalue above the exponentially small XF-083 tolerance is a rigorous obstruction. If the moment data lie inside the positive cone, the remaining algebraic task is an **equal-weight `N=2D` realization**, for which trigonometric quadrature is the relevant neighboring theory.

This does not prove that the Xi bridge exists, but it replaces an unconstrained root-placement problem by a finite convex feasibility screen followed by a sharply identified equal-weight realization problem. It also opens a selector-first route that can, in principle, avoid XF-083's full continuum approximation requirement: matching exactly the moments actually seen by XF-079 is enough for the guarded source state. The heat-transport compatibility and nonvanishing positive-transition resource remain the decisive later gates, and no upper bound on `Lambda` or RH implication is claimed.