# WI-284 — complete screening forces a prime-deleted critical support

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** the **one-signed, completely screened** first-crossing branch of `WI-267`, `WI-281`--`WI-283`. This finding restores the full first-crossing quadratic-form constraint after `WI-283` showed that support topology alone is relaxation-sharp.
- **Result:** if a nonnegative Suzuki first-crossing null mode screens every active prime-power autocorrelation, then its positive support is not merely prime-log-distance avoiding. On the entire form-domain subspace supported there, every von Mangoldt term vanishes identically, so the full first-crossing Weil form equals the prime-deleted gamma-plus-pole form of `WI-240`. Consequently that restricted prime-deleted form is positive semidefinite and has bottom exactly zero, attained by the same null mode.
- **What it does not claim:** this does not rule out such a support, does not give a quantitative spectral gap, does not handle incomplete screening or sign-changing null modes, and does not turn the full-space negative index of `WI-240` into a contradiction by itself.
- **Novelty boundary:** minimization of Weil's quadratic functional on support-restricted spaces is classical Bombieri/Yoshida territory, and Suzuki gives the modern localized closed-form/operator realization. The new line-local deduction is that **complete one-signed prime screening makes the actual hypothetical first-crossing support a zero-ground-state domain for the prime-deleted form**, because every prime shift vanishes on the whole supported subspace rather than only on the null vector. No historical priority claim is made.

## Claim

Let `a>0` be a first crossing for Suzuki's localized Weil form, so that

\[
q_a\ge 0
\tag{1}
\]

on its form domain `\mathfrak D(q_a)`, and suppose there is a normalized real null mode

\[
0\ne v\ge0,
\qquad
A_av=0,
\qquad
q_a(v)=0.
\tag{2}
\]

Extend functions by zero outside `(-a,a)`. For `d>0`, write

\[
C_f(d):=\int_{\mathbb R} f(x+d)f(x)\,dx,
\tag{3}
\]

and let

\[
\mathcal P_a:=\{\log n:\Lambda(n)>0,\ \log n<2a\}
\tag{4}
\]

be the active prime-power lags. The endpoint `\log n=2a`, when it occurs in a Fourier truncation convention, contributes zero for functions supported in the open aperture and can be included without changing the argument.

Assume **complete screening**:

\[
C_v(d)=0
\qquad(d\in\mathcal P_a).
\tag{5}
\]

Let

\[
E:=\{x\in(-a,a):v(x)>0\}
\tag{6}
\]

modulo null sets, and define the supported form-domain subspace

\[
\mathfrak D_E
:=\{u\in\mathfrak D(q_a):u=0\ \text{a.e. on }E^c\}.
\tag{7}
\]

Let `q_{\rm arch}^a` be the exact prime-deleted gamma-plus-pole form of `WI-240`, so on the common form domain

\[
q_a=q_{\rm arch}^a-q_{\rm prime}^a,
\tag{8}
\]

where `q_{\rm prime}^a` is the finite von Mangoldt translation form.

Then:

\[
\boxed{
q_{\rm prime}^a(u,w)=0
\quad\text{for every }u,w\in\mathfrak D_E.
}
\tag{9}
\]

Hence

\[
\boxed{
q_{\rm arch}^a(u)=q_a(u)\ge0
\quad(u\in\mathfrak D_E),
}
\tag{10}
\]

while

\[
\boxed{
q_{\rm arch}^a(v)=0,
\qquad
q_{\rm arch}^a(v,u)=0
\quad(u\in\mathfrak D_E).
}
\tag{11}
\]

Therefore the prime-deleted form restricted to the closed support subspace selected by `E` has spectral bottom exactly zero, and `v` is a zero ground-state vector of that restricted form. In variational language,

\[
\boxed{
\inf_{0\ne u\in\mathfrak D_E}
\frac{q_{\rm arch}^a(u)}{\|u\|_2^2}=0.
}
\tag{12}
\]

Thus a completely screened one-signed first-crossing counterexample must solve a much stronger support-selection problem than the packing relaxation of `WI-281`--`WI-283`: it must choose a prime-log-distance-avoiding support on which the **entire prime-deleted Weil form becomes critical at zero**.

## 1. Complete one-signed screening deletes every prime term on the support subspace

For each `d\in\mathcal P_a`, (5) and `v\ge0` give

\[
0=C_v(d)=\int v(x+d)v(x)\,dx,
\tag{13}
\]

with nonnegative integrand. Hence

\[
v(x+d)v(x)=0
\quad\text{for a.e. }x,
\tag{14}
\]

or equivalently

\[
|E\cap(E-d)|=0.
\tag{15}
\]

This is the support-packing implication used in `WI-281`. The extra point here is that (15) is inherited by **every** pair of functions supported in `E`. If `u,w\in\mathfrak D_E`, then almost everywhere

\[
u(x+d)\overline{w(x)}=0,
\qquad
u(x)\overline{w(x+d)}=0.
\tag{16}
\]

Therefore every sesquilinear prime-translation contribution at lag `d` vanishes. Summing over the finite active set proves (9).

No sign argument is used for `u` or `w`; one-signedness is needed only once, to pass from the scalar equalities (5) for the original null mode to the geometric disjointness (15). After that step the deletion is an operator-level statement on the whole supported subspace.

## 2. Firstness turns support deletion into prime-deleted spectral criticality

`WI-240` records Suzuki's exact decomposition on compactly supported smooth vectors as

\[
\begin{aligned}
q_a(u)
={}&\frac1{2\pi}\int
\left(\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi\right)
|\widehat u(z)|^2\,dz\\
&-\frac1{2\pi}\int |\widehat u(z)|^2
\sum_{n\le e^{2a}}\frac{2\Lambda(n)}{\sqrt n}\cos(z\log n)\,dz\\
&-\frac1{2\pi}\int\widehat{r_{0,a}''}(z)|\widehat u(z)|^2\,dz.
\end{aligned}
\tag{17}
\]

Deleting only the middle von Mangoldt term gives `q_{\rm arch}^a`. By density/form closure the same decomposition holds at the quadratic-form level used here; equivalently, the prime contribution is a finite bounded sum of translation pairings on `L^2(-a,a)`.

Equation (9) therefore gives

\[
q_{\rm arch}^a(u,w)=q_a(u,w)
\qquad(u,w\in\mathfrak D_E).
\tag{18}
\]

At a first crossing the full form is nonnegative, so (10) follows immediately. Since `v\in\mathfrak D_E` and its prime autocorrelations vanish,

\[
q_{\rm arch}^a(v)=q_a(v)=0.
\tag{19}
\]

Moreover `A_av=0` implies the weak null equation

\[
q_a(v,u)=0
\qquad(u\in\mathfrak D(q_a)),
\tag{20}
\]

and (18) gives the polarized statement in (11). Thus zero is both a lower bound and an attained Rayleigh quotient on `\mathfrak D_E`, proving (12).

Because the prime perturbation is bounded at fixed aperture, `q_{\rm arch}^a` has the same form domain as `q_a`. Intersecting that domain with the closed `L^2(E)` support subspace gives the natural closed restricted-form problem. No standalone global positivity or self-adjointness claim for the artificially prime-deleted form is needed.

## 3. This survives the `WI-283` support-relaxation barrier

`WI-283` proves that the geometric data

- complete prime-log distance avoidance,
- full essential span, and
- the `WI-267` prime-translation support domination

still allow profiles with `B_+` arbitrarily close to the packing ceiling `K_{\rm pack}`. That construction works because arbitrarily small-amplitude satellites can radically alter the closed support while barely changing a scalar quadratic objective.

The constraint (10)--(12) is different. Once an actual completely screened first-crossing null mode selects `E`, **every admissible perturbation supported in `E` must have nonnegative prime-deleted energy**. A tiny satellite added solely to satisfy support topology is harmless only if the enlarged support also preserves this infinite family of variational inequalities. Thus the exact null equation/firstness pair leaves an operator-domain shadow that is absent from the support-only relaxation.

A concrete contradiction target is now:

\[
\boxed{
\text{for every first-crossing-compatible, prime-log-distance-avoiding }E,
\ \exists u\in\mathfrak D_E:\ q_{\rm arch}^a(u)<0.
}
\tag{21}
\]

Any theorem of the form (21) rules out complete one-signed screening outright. A quantitative version,

\[
\inf_{0\ne u\in\mathfrak D_E}
\frac{q_{\rm arch}^a(u)}{\|u\|_2^2}\le-c(a)<0,
\tag{22}
\]

would provide a robust defect that could potentially be coupled to incomplete screening rather than merely exclude the exact zero-overlap endpoint.

## 4. Relation to the full-space negative index

`WI-240` proves that the prime-deleted form has unbounded odd negative index as the aperture grows. That fact is now directly relevant but is **not** by itself enough to contradict (10). A quadratic form can have many negative directions on the full space and still be nonnegative after restriction to a sparse support subspace.

What `WI-240` supplies is a family of explicit slowly varying negative subspaces that any screened support must avoid in the variational sense. If `F\subset\mathfrak D(q_{\rm arch}^a)` is a negative subspace, then (10) forces

\[
F\cap\mathfrak D_E=\{0\}.
\tag{23}
\]

So the next source-specific problem can be stated without another scalar packing surrogate: determine whether prime-log-distance avoidance is compatible with annihilating **all** negative directions of the exact gamma-plus-pole form while retaining a zero mode. The full-space index alone does not answer that support-sensitive question.

This also explains why generic PSD cut inequalities from `WI-269`--`WI-280` can hit scalar budget walls while (12) remains informative. Those arguments compress firstness into finitely many multiplier inequalities. Here complete screening lets us retain firstness on an entire infinite-dimensional supported form domain before any scalar compression.

## 5. Prior-art and novelty audit

The load-bearing exact zeta input is Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096, version of 19 Aug 2026, <https://arxiv.org/abs/2606.09096>. Suzuki gives the localized lower-bounded closed form, its self-adjoint operator `A_a`, the Rayleigh characterization of the bottom eigenvalue, and the exact gamma/von-Mangoldt/pole decomposition used in `WI-240`.

The support-restricted variational viewpoint is classical rather than new. Suzuki's historical discussion records that Enrico Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers. I** (2000), Problem 2, and **A variational approach to the explicit formula** (2003), Problem A, minimized the Weil Rayleigh quotient on `L^2(\mathcal E)` for a finite union of intervals `\mathcal E`, with existence of a minimizer proved in the corresponding theorem. Yoshida's earlier localization is also part of this lineage. Thus (12) should be read as a zeta-source-induced support restriction inside an established variational framework, not as invention of support-restricted Weil minimization.

The line-local novelty audit against `WI-240`, `WI-267`, `WI-269`, and `WI-281`--`WI-283` finds no earlier statement of (9)--(12). `WI-281` extracts only distance avoidance from screened autocorrelations; `WI-283` proves that adding support domination still does not lower the scalar packing supremum; `WI-269` keeps a PSD family of multiplier compressions; and `WI-240` studies the prime-deleted form on the whole aperture. The present deduction is the exact intersection of those ingredients: screening deletes the prime operator on the whole selected support subspace, while firstness forces the remaining prime-deleted form to be PSD and critical there. Targeted external searches located the Bombieri/Suzuki support-restricted variational framework but not this prime-screening implication. Search absence is not a priority claim.

## 6. Stress tests and boundaries

- **Why one-signedness is essential:** for sign-changing `v`, `C_v(d)=0` may result from cancellation and does not imply `E\cap(E-d)` is null. Then the prime operator need not vanish on the support subspace.
- **Why complete screening is essential:** if even one active prime-power lag has nonzero overlap, the corresponding translation form survives on `\mathfrak D_E`; (18) is then false.
- **Endpoint lag:** a possible lag exactly `2a` cannot overlap two functions supported in the open interval `(-a,a)` except on a null boundary, so it causes no extra term.
- **No illegitimate use of `WI-240`:** unbounded negative index on the full aperture does not imply negative index on `L^2(E)`. A support-sensitive theorem is still required.
- **No hidden RH assumption:** the first-crossing setup is conditional on RH being false, as in the established Suzuki branch. The deduction shows what a hypothetical first null mode would have to satisfy; it does not assume global Weil positivity.
- **Form-domain rather than arbitrary `L^2(E)`:** all claims are made on `\mathfrak D_E=\mathfrak D(q_a)\cap L^2(E)`. This avoids asserting that every square-integrable supported function has finite prime-deleted energy.

## 7. Research consequence

`WI-283` closed the route

\[
\text{screening}+\text{support domination}
\Longrightarrow
\text{strict scalar packing decrement}.
\]

The exact first-crossing problem now has a sharper replacement:

\[
\boxed{
\text{complete one-signed screening}
\Longrightarrow
\lambda_{\min}\!\left(q_{\rm arch}^a\big|_{E}\right)=0.
}
\tag{24}
\]

The next high-value target is therefore a **support-sensitive archimedean spectral obstruction**: combine the forbidden prime-log distances with the exact gamma-plus-pole kernel to prove that every admissible screened support either carries a negative prime-deleted direction or has a strictly positive bottom, either of which contradicts the required zero criticality. Unlike another support-cover inequality, such a result would use information that `WI-283`'s arbitrarily small-amplitude saturation cannot fake.