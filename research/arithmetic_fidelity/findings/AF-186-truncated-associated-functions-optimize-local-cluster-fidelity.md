# AF-186 — Truncated associated functions optimize local cluster fidelity under general derivative weights

**Status:** `EXACT-DERIVED`, `GENERAL-THEORY`, `QUANTITATIVE-RECOVERY`, `NEGATIVE/OBSTRUCTION`, `LITERATURE-CONTEXT`, `CANDIDATE-NEW-STRUCTURE`

## Claim

AF-182--AF-185 show that parity-split positive clusters can retain exact first-order source separation while smooth observation kernels suppress their discrepancy to arbitrarily high order. AF-185 packages this for Gevrey derivative budgets. The mechanism admits a sharper formulation for an arbitrary positive derivative-weight sequence, and the relevant object is a **local/truncated associated function** in which admissible cancellation order is capped by source locality.

Let

\[
M=(M_m)_{m\ge1},\qquad M_m>0,
\tag{1}
\]

be any fixed positive sequence. Fix a base point `x`, a neighborhood radius `r>0`, and for each sufficiently small `0<\delta<1` let `\Lambda_\delta` index real- or complex-valued smooth observation kernels

\[
K_{\delta,\lambda}(u),\qquad \lambda\in\Lambda_\delta,
\tag{2}
\]

on `[x,x+r]`. Assume constants `C>0`, `a_0>0`, and scales `A_\delta\ge a_0` such that for every integer `m>=1`, every `\lambda`, and every `u\in[x,x+r]`,

\[
\boxed{
|\partial_u^m K_{\delta,\lambda}(u)|
\le C A_\delta^m M_m.
}
\tag{3}
\]

Choose any integer locality cap `n_\delta>=1` satisfying

\[
\boxed{n_\delta\delta\longrightarrow0.}
\tag{4}
\]

Put

\[
t_\delta=\frac{2}{A_\delta\delta},
\tag{5}
\]

and define the positive-order truncated associated function

\[
\boxed{
\Omega_{M,n}(t)
=
\max_{1\le m\le n}
\left(m\log t-\log M_m\right)
=
\log\max_{1\le m\le n}\frac{t^m}{M_m}.
}
\tag{6}
\]

Equivalently, with

\[
h_{M,n}(s)=\min_{1\le m\le n}M_m s^m,
\tag{7}
\]

one has

\[
\exp[-\Omega_{M,n}(t)]=h_{M,n}(1/t).
\tag{8}
\]

For each `\delta`, choose an order `m_\delta\in\{1,\ldots,n_\delta\}` attaining the maximum in `(6)`, and form the normalized parity-split probability measures

\[
\mu_{+,\delta}-\mu_{-,\delta}
=
2^{1-m_\delta}
\sum_{j=0}^{m_\delta}
(-1)^{m_\delta-j}
\binom{m_\delta}{j}
\delta_{x+j\delta}.
\tag{9}
\]

Then, for all sufficiently small `\delta`:

1. the complete support lies in `[x,x+r]` and has diameter at most `n_\delta\delta=o(1)`;
2. `\mu_{+,\delta}` and `\mu_{-,\delta}` are distinct positive probability measures agreeing on every polynomial moment of degree below `m_\delta`;
3. their source separation is exactly
   \[
   \boxed{W_1(\mu_{+,\delta},\mu_{-,\delta})=\delta;}
   \tag{10}
   \]
4. their observation discrepancy
   \[
   D_\delta
   =
   \sup_{\lambda\in\Lambda_\delta}
   \left|
   \int K_{\delta,\lambda}(u)
   \,d(\mu_{+,\delta}-\mu_{-,\delta})(u)
   \right|
   \tag{11}
   \]
   obeys the optimized envelope
   \[
   \boxed{
   D_\delta
   \le
   2C\exp\!\left[-\Omega_{M,n_\delta}(t_\delta)\right].
   }
   \tag{12}
   \]

Consequently, if

\[
L_\delta=\log(1/\delta)
\tag{13}
\]

and

\[
\boxed{
\frac{\Omega_{M,n_\delta}(2/(A_\delta\delta))}
{\log(1/\delta)}
\longrightarrow\infty,
}
\tag{14}
\]

then for every fixed `N>0`,

\[
\boxed{D_\delta=o(\delta^N),}
\tag{15}
\]

while the source distance remains exactly `\delta`. Hence no uniform inverse Hölder estimate

\[
W_1(\mu,\nu)\le C_0D(\mu,\nu)^\alpha
\tag{16}
\]

with fixed `\alpha>0` can hold on a source class containing these local adaptive controls.

The condition `(14)` is also exact for the **best upper bound obtainable from this parity-split finite-difference construction plus the declared derivative envelope `(3)`**: among all allowed orders `1<=m<=n_\delta`, the smallest such envelope is precisely the right-hand side of `(12)`. This is a mechanism-level optimization statement, not a converse theorem for the actual inverse problem.

## Derivation

### 1. The derivative envelope gives one cost for each cancellation order

For every integer `m>=1`, the exact forward-difference identity gives

\[
\Delta_\delta^mK(x)
=
\int_{[0,\delta]^m}
K^{(m)}(x+u_1+\cdots+u_m)
\,du_1\cdots du_m.
\tag{17}
\]

Whenever `m\delta<=r`, `(3)` therefore implies

\[
|\Delta_\delta^mK_{\delta,\lambda}(x)|
\le
C(A_\delta\delta)^mM_m.
\tag{18}
\]

The normalization of the parity split contributes `2^{1-m}`, so the order-`m` controls satisfy

\[
D_{\delta,m}
\le
2C\left(\frac{A_\delta\delta}{2}\right)^mM_m.
\tag{19}
\]

Using `t_\delta=2/(A_\delta\delta)`, this is

\[
D_{\delta,m}
\le
2C\exp\!\left[-\left(m\log t_\delta-\log M_m\right)\right].
\tag{20}
\]

Minimizing `(20)` over the geometrically admissible orders `1<=m<=n_\delta` is therefore exactly the same as maximizing `(6)`. This proves `(12)`.

No log-convexity, moderate-growth condition, or quasianalyticity assumption on `M` is needed for this finite optimization. Such hypotheses become relevant only when one wants to interpret `M` as a standard Denjoy--Carleman/ultradifferentiable weight sequence or derive regular asymptotics for its full associated function.

### 2. The locality truncation is mathematically necessary

The classical associated function of a weight sequence optimizes over all derivative orders. That unrestricted optimization can choose an order so large that the corresponding parity cluster occupies a macroscopic interval, which would invalidate a local inverse-fidelity conclusion.

The cap `m<=n_\delta` prevents that escape. Since `(4)` holds,

\[
m_\delta\delta
\le n_\delta\delta\to0,
\tag{21}
\]

so the controls collapse to the same base point even though their cancellation order may diverge. Thus `\Omega_{M,n_\delta}` is not merely a finite approximation to the standard associated function: in this fidelity problem the truncation records a genuine geometric resource constraint.

### 3. Superalgebraic observation flatness is exactly the growth of the local associated function beyond the source logarithm

From `(12)`, for fixed `N>0`,

\[
\log\frac{D_\delta}{\delta^N}
\le
\log(2C)
-
\Omega_{M,n_\delta}(t_\delta)
+
N L_\delta.
\tag{22}
\]

Condition `(14)` drives the right side to `-\infty`, giving `(15)`.

Conversely, consider only the family of derivative-envelope bounds in `(19)`. If there exists a sequence of admissible orders `m_\delta<=n_\delta` for which those bounds are `o(\delta^N)` for every fixed `N`, then

\[
\frac{m_\delta\log t_\delta-\log M_{m_\delta}}
{L_\delta}
\to\infty.
\tag{23}
\]

Since `\Omega_{M,n_\delta}` is the maximum over all admissible orders, `(14)` follows. Hence `(14)` exactly characterizes when **this declared derivative envelope, optimized over local parity-split cancellation order, certifies superalgebraic invisibility**.

Actual kernels may have additional algebraic structure or cancellations that make their true discrepancies smaller than `(19)`. Therefore `(14)` is not necessary for instability of the underlying compression.

### 4. Positivity and exact source distance are independent of the weight sequence

The binomial signs in `(9)` split one row into two positive halves of equal unnormalized mass `2^{m_\delta-1}`. The elementary finite-difference identity annihilates every polynomial of degree below `m_\delta`, so all corresponding moments agree.

AF-182 proves for this same normalized parity split that the one-dimensional cumulative-distribution formula gives exactly

\[
W_1(\mu_{+,\delta},\mu_{-,\delta})=\delta.
\tag{24}
\]

Thus the observation can become superalgebraically small without the source pair itself becoming superalgebraically close in the declared metric. If `(16)` held with some `\alpha>0`, choose `N>1/\alpha`; then `(15)` would give `D_\delta^\alpha=o(\delta)`, contradicting `(24)`.

## Gevrey specialization and recovery of AF-185

Take

\[
M_m=(m!)^q,
\qquad q\ge1.
\tag{25}
\]

The corresponding unrestricted associated function is classical and satisfies, up to constants,

\[
\Omega_M(t)
=
\sup_{m\ge1}\left(m\log t-q\log(m!)\right)
\asymp t^{1/q}
\qquad(t\to\infty).
\tag{26}
\]

However, the unrestricted maximizing order is not automatically local. AF-185 supplies exactly the missing geometric choice. With

\[
\varepsilon_\delta=A_\delta\delta,
\qquad
\rho_\delta=\varepsilon_\delta L_\delta^q,
\tag{27}
\]

its condition

\[
\rho_\delta\to0
\tag{28}
\]

and order

\[
m_\delta
=
\left\lfloor
L_\delta\rho_\delta^{-1/(2q)}
\right\rfloor
\tag{29}
\]

satisfy `m_\delta\delta->0`, `m_\delta/L_\delta->infinity`, and `\varepsilon_\delta m_\delta^q->0`. Taking any locality cap `n_\delta>=m_\delta` with `n_\delta\delta->0`, the term of `(6)` at this order already gives

\[
\frac{\Omega_{M,n_\delta}(2/\varepsilon_\delta)}{L_\delta}
\to\infty.
\tag{30}
\]

Thus AF-185 is recovered as the Gevrey instance of `(14)`.

There is also a useful converse at the level of existence of local optimizing caps. Since every truncated associated function is bounded by the full one in `(26)`, if `\varepsilon_\delta L_\delta^q` stays bounded below along a subsequence, then `t_\delta^{1/q}=O(L_\delta)` there and `\Omega_{M,n_\delta}(t_\delta)=O(L_\delta)` for every cap. Therefore no local cap can satisfy `(14)` on that subsequence. In this Gevrey family, the AF-185 gate is exactly the threshold for the existence of a local parity-cluster sequence whose derivative-envelope bound is superalgebraically small.

## A genuinely non-Gevrey example

The associated-function formulation is not only a reparameterization of Gevrey order. Consider

\[
M_m=\exp(m^\beta),
\qquad \beta>1,
\tag{31}
\]

and for simplicity a scale-independent `A_\delta=A>0`. Writing `u=\log t`, continuous optimization of

\[
mu-m^\beta
\tag{32}
\]

has maximizer

\[
m_*=(u/\beta)^{1/(\beta-1)}
\tag{33}
\]

and maximum

\[
\left(\beta-1\right)
\beta^{-\beta/(\beta-1)}
\,u^{\beta/(\beta-1)}.
\tag{34}
\]

Integer optimization has the same leading asymptotic. Since `t_\delta=2/(A\delta)` gives `u=L_\delta+O(1)`, the optimal order grows only polylogarithmically and hence remains local:

\[
m_*\delta\to0.
\tag{35}
\]

Choosing a cap containing the nearest optimizing integer gives

\[
\Omega_{M,n_\delta}(t_\delta)
\asymp
L_\delta^{\beta/(\beta-1)},
\tag{36}
\]

so `(14)` holds and the same positive controls are invisible to every algebraic output scale. This derivative budget grows much faster than `(m!)^q` for every fixed Gevrey order `q`, yet its associated-function growth still identifies an admissible local cancellation order that defeats every inverse power law.

This example is the main reason to keep `(6)` rather than only a factorial exponent: the fidelity threshold depends on the Legendre-type competition between **resolution gain `m\log t`** and **regularity cost `\log M_m`**, not on Gevrey terminology.

## Prior art and novelty assessment

The unrestricted weight-sequence machinery is classical.

- Hikosaburo Komatsu, **“Ultradistributions, I. Structure theorems and a characterization,”** *Journal of the Faculty of Science, University of Tokyo, Section IA Mathematics* 20 (1973), 25--105, is foundational prior art for ultradifferentiable weight sequences and their associated growth functions.
- Armin Rainer and Gerhard Schindl, **“Composition in ultradifferentiable classes,”** *Studia Mathematica* 224(2) (2014), 97--131, DOI `10.4064/sm224-2-1`, is modern weight-sequence/weight-function prior art and explicitly treats associated weight functions.
- Vincent Thilliez, **“On Quasianalytic Local Rings,”** *Expositiones Mathematicae* 26(1) (2008), 1--23, DOI `10.1016/j.exmath.2007.04.001`, is standard Denjoy--Carleman context for weight sequences, quasianalyticity, and related growth conditions.
- Stevan Pilipović, Nenad Teofanov, and Filip Tomić, **“A Paley-Wiener theorem in extended Gevrey regularity,”** arXiv:`1901.00698` (2019), derive sharp associated-function asymptotics for a nonstandard extended-Gevrey weight sequence, confirming that associated functions are established tools well beyond fixed Gevrey order.

The associated function itself, its Legendre-transform character, Gevrey asymptotics, and finite-difference derivative estimates are therefore not new. A targeted audit did not identify an authoritative source that combines **positive parity-split moment-matched clusters, a shrinking-support order cap, and the truncated associated function as the exact optimization criterion for inverse-fidelity failure**. That absence is not a priority claim. The candidate-new structure here is the synthesis and especially the locality truncation: source geometry turns the classical unrestricted associated function into the exact budget function for this matched-control mechanism.

## Boundaries and failure modes

1. **No global converse.** If `(14)` fails, the compression may still be unstable for a different reason, or the kernels may have cancellations much stronger than the envelope `(3)` records. The converse proved here concerns only the optimized bound generated by `(3)` and parity-split finite differences.

2. **The locality cap is part of the theorem.** Using the unrestricted associated function without checking the maximizing cluster diameter can manufacture a false local obstruction. Any application must expose an admissible `n_\delta` with `n_\delta\delta->0`.

3. **The source class must allow growing complexity.** The number of support nodes is `m_\delta+1`; multiplicities in the generalized-prime realization grow binomially. Fixed support size, bounded multiplicity, minimum separation, entropy budgets, or other complexity restrictions can block the construction.

4. **The derivative weights must be uniform across the observation family.** `M` is fixed, `C` is uniform, and all resolution-dependent exponential scaling is exposed in `A_\delta`. Allowing hidden `\delta`- or `\lambda`-dependent order weights would change `\Omega` and invalidate the audit.

5. **No standard weight-sequence axioms are assumed in the abstract theorem.** Classical Denjoy--Carleman interpretations require their own log-convexity, normalization, moderate-growth, or quasianalyticity hypotheses as appropriate. The finite fidelity optimization itself uses only positivity of `M_m`.

6. **The source metric is normalized one-dimensional `W_1`.** Different source metrics or unnormalized counting measures change the comparison scale. The exact `W_1=\delta` statement is inherited from AF-182's normalized parity split.

7. **No exact observation collision is asserted.** Equation `(12)` is quantitative. For finite `\delta`, the full observation family may remain injective.

8. **No RH consequence is asserted.** A concrete arithmetic application must still verify that its actual observation kernels satisfy `(3)`, that the relevant source controls are admissible, and that the downstream argument needs a recovery modulus strong enough for `(14)` to obstruct it.

## Consequences for Arithmetic Fidelity

AF-185 identified a Gevrey-order logarithmic gate. AF-186 replaces the factorial exponent by a more intrinsic quantity: the local associated function of the derivative budget. The resulting audit is portable across regularity classes.

For a compression observed at source scale `\delta`, derive its uniform derivative weights `A_\delta^mM_m`, choose the largest cancellation orders allowed by the source geometry, and compute

\[
\Omega_{M,n_\delta}\!\left(\frac{2}{A_\delta\delta}\right).
\tag{37}
\]

The ratio of `(37)` to `\log(1/\delta)` is the exact superalgebraic-flatness diagnostic supplied by this mechanism. It simultaneously records observation resolution, derivative regularity, and admissible source complexity. In particular, it makes precise a broader principle suggested by the recent Arithmetic Fidelity frontier: **stable compression cannot be assessed from observation smoothness or source separation alone; the decisive quantity is the optimization of surviving resolution against the complexity cost of the source distinctions one permits.**