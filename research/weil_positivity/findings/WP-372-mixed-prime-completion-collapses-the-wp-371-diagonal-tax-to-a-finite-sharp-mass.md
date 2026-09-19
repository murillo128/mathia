---
id: WP-372
title: Mixed-prime completion collapses the WP-371 diagonal tax to a finite sharp mass
branch: weil_positivity
status: supported
kind: mixed-prime-critical-toeplitz-positive-completion-boundary
claim_strength: exact classification of scalar positive-definite completions of the WP-371 positive critical prime-power rays when arbitrary mixed-prime Fourier coefficients are allowed, plus a sharp sparse/common-line control
created: 2026-09-19
related: [WP-096, WP-097, WP-100, WP-371]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical Poisson kernel and Herglotz/Toeplitz positivity
  - Bochner duality for positive-definite functions on discrete abelian groups
  - classical product/Riesz-product measure constructions on compact abelian groups
  - Kakutani equivalence/singularity theory for infinite product measures
  - Kronecker/Pontryagin density for one-parameter flows on finite tori
---

# WP-372 — Mixed-prime completion collapses the WP-371 diagonal tax to a finite sharp mass

## Claim

`WP-371` proves an exact local obstruction for the positive critical prime-power Toeplitz carrier

\[
(\log p)C_{p^{-1/2}}
=\sum_{k\ge1}\frac{\log p}{p^{k/2}}(U^k+U^{-k}).
\tag{1}
\]

If every prime ray is completed independently by a scalar diagonal, the least local tax is

\[
c_p^+:=\frac{2\log p}{\sqrt p+1},
\tag{2}
\]

and `WP-371` observes that `\sum_p c_p^+=\infty`. It deliberately leaves cross-prime completion open.

That escape is real already in the scalar positive-definite category. Let

\[
G=\mathbb Q_+^\times\cong\bigoplus_p\mathbb Z,
\qquad
\widehat G\cong\prod_p\mathbb T.
\tag{3}
\]

Ask for a finite positive measure `mu` on the prime torus, of total mass

\[
C=\mu(\widehat G),
\tag{4}
\]

whose one-prime Fourier rays are exactly the **positive-sign** `WP-371` coefficients

\[
\widehat\mu(p^k)
=\frac{\log p}{p^{|k|/2}},
\qquad k\in\mathbb Z\setminus\{0\},
\tag{5}
\]

while mixed-prime Fourier coefficients are unconstrained. Then such a positive measure exists if and only if

\[
\boxed{
C\ge C_+^*:=\sup_p\frac{2\log p}{\sqrt p+1}<\infty.
}
\tag{6}
\]

The supremum is attained at `p=13`, so

\[
C_+^*=\frac{2\log13}{\sqrt{13}+1}\approx1.1138511783.
\tag{7}
\]

For every `C>=C_+^*`, an explicit positive completion is

\[
\boxed{
\mu_C
=C\bigotimes_p
\left[
1+\frac{\log p}{C}
\left(P_{p^{-1/2}}(\theta_p)-1\right)
\right]\frac{d\theta_p}{2\pi},
}
\tag{8}
\]

where

\[
P_r(\theta)
=\frac{1-r^2}{1-2r\cos\theta+r^2}
=1+2\sum_{k\ge1}r^k\cos(k\theta).
\tag{9}
\]

If a reduced rational uses the distinct primes in a finite set `F`,

\[
r=\prod_{p\in F}p^{k_p},
\qquad k_p\ne0,
\tag{10}
\]

then this completion has the exact mixed coefficient

\[
\boxed{
\widehat\mu_C(r)
=C^{1-|F|}
\prod_{p\in F}
(\log p)p^{-|k_p|/2}.
}
\tag{11}
\]

Thus the divergent `WP-371` tax is **not a positivity tax for arbitrary global scalar completions**. It is the price of keeping the positive critical rays sparse/separable across primes. Once mixed-prime Fourier interactions are allowed, the sharp all-prime diagonal requirement drops from the divergent sum `\sum_p c_p^+` to the finite maximum `\sup_p c_p^+`.

The opposite boundary is equally sharp. If all mixed-prime coefficients are required to vanish, then on every finite prime set `P` positivity forces

\[
\boxed{
C\ge D_+(P):=
\sum_{p\in P}\frac{2\log p}{\sqrt p+1},
}
\tag{12}
\]

and `D_+(P)\to\infty`. Moreover the same threshold holds when the sparse carrier is assembled first on the **single common Weil translation line** `theta_p=t log p` and positivity is tested only afterwards: multiplicative independence of the primes makes the prime-log flow dense in the full finite torus, so the negative troughs can be approached simultaneously.

This is a decisive boundary on `WP-371`, not a Weil-positivity construction. The product factors in (8) were engineered from the target moments, the mixed sector is universal for free generators, the critical product is singular to product Haar by the same square-sum/Kakutani mechanism as `WP-100`, and no Gamma, polar, archimedean, or independent orientation theorem is produced.

**Classification:** `EXACT-DERIVED + MIXED-PRIME-POSITIVE-COMPLETION + SHARP-FINITE-MASS-THRESHOLD + SPARSE-SUM-VS-MIXED-MAX-DICHOTOMY + PRIME-LOG-DENSE-LINE-CONTROL + CRITICAL-HAAR-SINGULAR + MATCHED-CONTROL + NO-ZERO-DATA + CLASSICAL-INGREDIENTS + POSITIVE-BOUNDARY/NOT-WEIL-POSITIVITY + NO-GRAND-NOVELTY-CLAIM`.

## 1. One-prime marginals give the exact necessary bound

Let `mu` be any finite positive measure satisfying (5), with arbitrary mixed-prime coefficients. Push it forward to the `p`-th circle. Its total mass is `C`, and its nonzero Fourier coefficients are absolutely summable. Fourier uniqueness therefore gives the continuous density

\[
\begin{aligned}
w_{p,C}(\theta)
&=C+2(\log p)\sum_{k\ge1}p^{-k/2}\cos(k\theta)\\
&=C+(\log p)\bigl(P_{p^{-1/2}}(\theta)-1\bigr).
\end{aligned}
\tag{13}
\]

For `0<r<1`, the Poisson kernel is minimized at `theta=pi`, where

\[
P_r(\pi)=\frac{1-r}{1+r}.
\tag{14}
\]

Consequently

\[
\min_\theta w_{p,C}(\theta)
=C-\frac{2\log p}{\sqrt p+1}
=C-c_p^+.
\tag{15}
\]

A positive marginal must have nonnegative density, hence

\[
C\ge c_p^+
\qquad\text{for every prime }p.
\tag{16}
\]

This proves the necessity of (6).

The threshold is finite because `c_p^+ -> 0`. For completeness, writing `y=sqrt x` gives

\[
\frac{2\log x}{\sqrt x+1}
=\frac{4\log y}{y+1},
\tag{17}
\]

whose derivative has the sign of

\[
1+\frac1y-\log y.
\tag{18}
\]

The latter decreases strictly through zero once, between `sqrt(11)` and `sqrt(13)`. Thus the continuous envelope increases through `11` and decreases from `13` onward; direct comparison of the only two prime candidates gives (7).

This necessity argument already shows why summing the local taxes is too strong once mixed-prime moments are available. Every coordinate marginal sees only its own requirement `C>=c_p^+`; one common positive measure can pay all of those marginal costs with a single total mass provided correlations/mixed Fourier modes carry the compatibility.

## 2. The sharp finite threshold is attained by an explicit product completion

Assume `C>=C_+^*` and define

\[
\rho_{p,C}(\theta)
:=1+\frac{\log p}{C}
\bigl(P_{p^{-1/2}}(\theta)-1\bigr).
\tag{19}
\]

Equation (15) gives

\[
\rho_{p,C}(\theta)
\ge1-\frac{c_p^+}{C}
\ge0,
\tag{20}
\]

while the zero Fourier coefficient of `P_r-1` is zero, so

\[
\int_{\mathbb T}\rho_{p,C}\,dm=1.
\tag{21}
\]

Each `rho_{p,C}dm` is therefore a probability measure. Their countable product exists, and multiplying by `C` gives (8).

For `k!=0`, (9) yields

\[
\widehat{\rho_{p,C}}(k)
=\frac{\log p}{C}p^{-|k|/2}.
\tag{22}
\]

Characters of the infinite prime torus involve only finitely many coordinates, so product integration gives

\[
\begin{aligned}
\widehat\mu_C\!\left(\prod_{p\in F}p^{k_p}\right)
&=C\prod_{p\in F}\widehat{\rho_{p,C}}(k_p)\\
&=C^{1-|F|}
\prod_{p\in F}(\log p)p^{-|k_p|/2},
\end{aligned}
\tag{23}
\]

proving both (5) and (11). Together with the marginal necessity, this proves the `if and only if` classification (6).

The comparison with `WP-097` is exact but sign-sensitive. `WP-097` solves the same moment problem for the **negative** Weil-ray sign and obtains local cost `2 log p/(sqrt p-1)`, maximized at `p=2`. The present positive-sign carrier is the one actually isolated in `WP-371`; its antipodal minimum replaces `sqrt p-1` by `sqrt p+1`, and the sharp generator moves to `p=13`. The underlying product-measure technology is the same classical mechanism.

## 3. For sparse support the diagonal costs add exactly

Now force every mixed-prime Fourier coefficient to vanish. On a finite prime set `P`, Fourier uniqueness gives the density

\[
w^{\rm sparse}_{P,C}(\theta)
=C+\sum_{p\in P}(\log p)
\bigl(P_{p^{-1/2}}(\theta_p)-1\bigr).
\tag{24}
\]

Because the coordinates are independent on `T^P`, all local minima occur simultaneously at

\[
\theta_p=\pi
\qquad(p\in P).
\tag{25}
\]

Therefore

\[
\boxed{
\min_{\theta\in\mathbb T^P}
w^{\rm sparse}_{P,C}(\theta)
=C-D_+(P),
}
\tag{26}
\]

with `D_+(P)` from (12). Hence (12) is not merely the cost of separately completing each prime and then adding the results. It is the **globally optimal scalar diagonal** for the entire sparse finite-prime carrier.

Since `D_+(P)` is exactly the partial sum from `WP-371`, it diverges along prime exhaustion. Thus the sparse and mixed completion problems have sharply different asymptotics:

\[
\boxed{
\begin{array}{rcl}
\text{sparse one-prime Fourier support}
&:& C_{\min}(P)=\sum_{p\in P}c_p^+\to\infty,\\[1mm]
\text{arbitrary mixed-prime Fourier support}
&:& C_{\min}=\sup_pc_p^+=C_+^*<\infty.
\end{array}
}
\tag{27}
\]

The mixed coefficients in (11) are therefore not decorative. They are exactly the sector that changes the positivity budget from an additive one to a shared one.

## 4. Deferring scalar positivity until after common-line assembly does not reduce the sparse tax

`WP-371` is naturally read on one common spectral variable rather than on independent prime circles. Let

\[
(U_pg)(t)=e^{it\log p}g(t)
\tag{28}
\]

on `L^2(R)`, and for a finite prime set `P` define the assembled sparse operator

\[
A_P:=\sum_{p\in P}(\log p)C_{p^{-1/2}}(U_p).
\tag{29}
\]

It is multiplication by the continuous almost-periodic symbol

\[
a_P(t)
=\sum_{p\in P}(\log p)
 c_{p^{-1/2}}(t\log p),
\tag{30}
\]

where `c_r=P_r-1` is the centered Poisson symbol of `WP-371`.

The one-parameter phase orbit

\[
t\longmapsto
(t\log p)_{p\in P}\pmod{2\pi}
\tag{31}
\]

is dense in `T^P`. Indeed, the closure is a compact subgroup. If it were proper, a nontrivial torus character would annihilate it, giving integers `m_p`, not all zero, with

\[
\sum_{p\in P}m_p\log p=0.
\tag{32}
\]

Exponentiating would give `prod_p p^{m_p}=1`, contradicting unique factorization. This is the standard Kronecker/Pontryagin density argument specialized to prime logarithms.

Because the torus symbol is continuous, density of (31) implies

\[
\inf_{t\in\mathbb R}a_P(t)
=\min_{\theta\in\mathbb T^P}
\sum_{p\in P}(\log p)c_{p^{-1/2}}(\theta_p)
=-D_+(P).
\tag{33}
\]

The near-minimum values occur on intervals of positive measure, so (33) is also the essential infimum and hence the lower spectral edge of `A_P`. Consequently

\[
\boxed{
A_P+CI\succeq0
\quad\Longleftrightarrow\quad
C\ge D_+(P).
}
\tag{34}
\]

Thus there is no hidden gain from saying “assemble all prime rays first and impose one scalar positivity theorem only at the end.” In the sparse scalar category, prime-log recurrence aligns the antipodal negative troughs arbitrarily well, and the exact global threshold is still the sum of the local thresholds.

This is a useful adversarial control on (27): the finite threshold in (6) is genuinely paid by **new mixed-prime Fourier data**, not by an accidental mismatch between independent-torus and common-line representations.

## 5. The explicit mixed completion is still not the missing geometry

The existence theorem above is a boundary result, not evidence for RH or for Weil positivity.

**The moments are prescribed rather than derived.** Equation (19) was chosen so that (22) equals the target `WP-371` half-density. Positivity proves compatibility of those moments; it does not explain why a Mathia-native construction selects them.

**The mixed sector is universal.** Replace rational primes by free generators `g_j`, positive amplitudes `a_j`, and radii `0<r_j<1`. The same construction works whenever

\[
\sup_j\frac{2a_jr_j}{1+r_j}<\infty.
\tag{35}
\]

Hence neither the product completion nor its sign theorem distinguishes the rational primes from a matched free-generator system.

**Deleting the mixed sector destroys the sign.** Projecting (8) to constant plus one-prime Fourier chaos gives (24), whose minimum tends to `-infinity` for every fixed finite `C`. The positive theorem therefore cannot be followed by a naive “keep only the Weil rays” selector.

**The critical product leaves the canonical Haar class.** Put

\[
u_{p,C}(\theta)
=\rho_{p,C}(\theta)-1.
\tag{36}
\]

Its nonzero Fourier coefficients differ from those in `WP-100` only by sign, so Parseval gives exactly

\[
\|u_{p,C}\|_2^2
=\frac{2(\log p)^2}{C^2(p-1)}.
\tag{37}
\]

The prime sum of (37) diverges. The Hellinger/Kakutani argument of `WP-100` therefore applies unchanged to the sign-reversed factors: for every finite admissible `C`, the all-prime product in (8) is singular to product Haar. Positivity survives, but not as a regular density perturbation of the canonical prime-torus Hilbert geometry.

**There is no archimedean or polar term.** Nothing in (8) produces the Gamma/digamma contribution, the pole terms, or a source-forced finite--archimedean coupling. Nor does the construction supply the orientation needed to turn the positive-sign carrier into the exact global Weil functional.

These controls kill the tempting inference

\[
\text{finite positive completion of all critical prime rays}
\Longrightarrow
\text{global Weil positivity}.
\tag{38}
\]

What survives is narrower: mixed-prime interaction can remove the scalar completion divergence, so a future obstruction may not assume that `WP-371`'s local tax remains additive once the global object has genuinely nonseparable finite-place structure.

## 6. Prior-art and novelty audit

All analytic machinery used here is classical or already present in this research line. The Poisson kernel and its Toeplitz/Herglotz positivity are the subject of `WP-371`. Bochner duality on `Q_+^x` and the prime-torus representation are classified in `WP-096`. Product positive measures with prescribed one-prime rays are the mechanism of `WP-097`. The critical infinite-product singularity is the Kakutani mechanism of `WP-100`. The dense prime-log orbit in Section 4 is the standard Kronecker/Pontryagin theorem, with rational independence following immediately from unique factorization.

In fact the construction (8) is deliberately the **positive-sign sibling** of `WP-097`; no theorem-level novelty is claimed for it. The reason it passes the substantive gate is project-specific and narrower: `WP-371` had just established a divergent diagonal tax for the current positive critical prime-power Toeplitz carrier while explicitly leaving cross-prime completion unclassified. Equations (6)--(11) settle that escape sharply: cross-prime scalar positivity can pay the entire all-prime debt with one finite mass, while (24)--(34) prove that the improvement disappears exactly when the mixed sector is removed.

So `WP-371` should be read as an exact theorem about **sparse/separable scalar completion**, not as a no-go for global positive scalar kernels with mixed-prime correlations. The line's live burden moves upstream: the missing ingredient is not merely “some cross-prime positive completion,” which now exists cheaply, but a **source-forced nonseparable finite--archimedean structure** whose mixed terms are geometrically canonical, whose final selector preserves the exact Weil arithmetic without deleting the positivity-paying sector, and whose sign theorem is independent of RH or zero data.

## Consequence for the research line

The immediate post-`WP-371` frontier has an exact dichotomy. If the prime-power rays remain sparse after global assembly, their negative troughs align and every scalar positive completion pays the divergent sum `D_+(P)`. If arbitrary mixed-prime Fourier interactions are admitted before positivity, a finite positive completion exists at the sharp mass `C_+^*`.

This removes a false obstruction but does not produce the desired mechanism. **Cross-prime coupling by itself is too cheap and too programmable.** The next serious candidate must explain why its mixed sector is forced by Mathia geometry, how that same sector couples to the archimedean/polar terms, and why the eventual Weil selector is compatible with the sign theorem rather than obtained by throwing away the correlations that made positivity possible.
