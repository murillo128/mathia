# AF-268 — Finite zero surgery breaks exact Bohr source recurrence

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SOURCE`, `ALMOST-PERIODICITY`, `ZERO-SURGERY`, `CATEGORY-OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-267 shows that count-preserving off-critical zero replacements can approach the Riemann logarithmic-derivative channel arbitrarily closely in the full vertical supremum norm on every fixed line `Re(s)=sigma>1`. Metric proximity therefore does not supply a positive robustness gap. There is nevertheless an exact global source property that every nontrivial **finite** zero surgery loses: Bohr uniform almost periodicity in the vertical translation variable.

Fix

\[
\sigma>1,
\tag{1}
\]

and use the same Riemann completion normalization as AF-266--AF-267,

\[
\mathcal R_f(s)
:=\frac{f'}{f}(s)-A(s),
\qquad
A(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi\!\left(\frac s2\right).
\tag{2}
\]

Let `AP(R)` denote the Banach space of Bohr uniformly almost-periodic functions on the real line with the supremum norm, and let `C_0(R)` be the continuous functions tending to zero as `|t|->infinity`.

For the genuine completed zeta function,

\[
\mathcal R_\xi(\sigma+it)
=-\sum_{m\ge2}\Lambda(m)m^{-\sigma}e^{-it\log m},
\tag{3}
\]

and the series converges absolutely and uniformly in `t`. Therefore

\[
\boxed{
 t\longmapsto\mathcal R_\xi(\sigma+it)
 \in AP(\mathbb R).
}
\tag{4}
\]

Now perform any finite signed divisor surgery on `xi`. Write its nonconstant rational multiplier after cancellation as

\[
H(s)
=C\,
\frac{\prod_{j=1}^{J}(s-\alpha_j)^{u_j}}
     {\prod_{k=1}^{K}(s-\beta_k)^{v_k}},
\qquad
u_j,v_k\in\mathbb N,
\tag{5}
\]

with all denominator factors chosen so that the resulting control

\[
F(s)=H(s)\xi(s)
\tag{6}
\]

is legitimate in the declared class. Assume the signed divisor difference is nontrivial, equivalently `H` is not constant after cancellation. Since `sigma>1` lies to the right of the nontrivial zeta zero strip and of the AF-267 surgery, the vertical trace is regular and

\[
D_{F,\sigma}(t)
:=\mathcal R_F(\sigma+it)-\mathcal R_\xi(\sigma+it)
=\frac{H'}H(\sigma+it).
\tag{7}
\]

This defect is a finite signed sum of Cauchy kernels,

\[
D_{F,\sigma}(t)
=
\sum_j\frac{u_j}{\sigma+it-\alpha_j}
-
\sum_k\frac{v_k}{\sigma+it-\beta_k},
\tag{8}
\]

so

\[
\boxed{
D_{F,\sigma}\in C_0(\mathbb R)\setminus\{0\}.
}
\tag{9}
\]

But

\[
\boxed{
AP(\mathbb R)\cap C_0(\mathbb R)=\{0\}.
}
\tag{10}
\]

Consequently

\[
\boxed{
\mathcal R_F(\sigma+i\,\cdot)\notin AP(\mathbb R)
}
\tag{11}
\]

for every nontrivial finite zero surgery. In particular, `F` cannot retain on that vertical line an exact source law given by an absolutely convergent ordinary Dirichlet series, or more generally by any absolutely convergent discrete general-Dirichlet series, because every such vertical trace is a uniform limit of finite exponential sums and hence belongs to `AP(R)`.

There is also a quantitative category-defect bound. For every `h in C_0(R)`,

\[
\boxed{
\frac12\|h\|_\infty
\le
\operatorname{dist}_\infty(h,AP(\mathbb R))
\le
\|h\|_\infty.
}
\tag{12}
\]

Since translation by the genuine almost-periodic channel preserves the subspace `AP(R)`, equations `(7)` and `(12)` give

\[
\boxed{
\frac12\|D_{F,\sigma}\|_\infty
\le
\operatorname{dist}_\infty\!\left(
\mathcal R_F(\sigma+i\,\cdot),AP(\mathbb R)
\right)
\le
\|D_{F,\sigma}\|_\infty.
}
\tag{13}
\]

Thus exact source-category membership is rigid against every finite nontrivial divisor surgery, while the category defect itself can still have zero uniform separation radius. Applied to the AF-267 controls `F_n`,

\[
0<
\operatorname{dist}_\infty\!\left(
\mathcal R_{F_n}(\sigma+i\,\cdot),AP(\mathbb R)
\right)
\le
\|\mathcal R_{F_n}-\mathcal R_\xi\|_{\sigma,\infty}
\longrightarrow0.
\tag{14}
\]

So AF-267 does not contradict exact Dirichlet-source rigidity: its controls approach the source category arbitrarily closely without ever entering it.

## Exact derivation

### 1. The Riemann source trace is uniformly almost periodic

For `Re(s)=sigma>1`, the Euler-product logarithmic derivative gives the absolutely convergent Dirichlet series

\[
\mathcal R_\xi(s)
=-\sum_{m\ge2}\Lambda(m)m^{-s}.
\tag{15}
\]

Because

\[
\sum_{m\ge2}\Lambda(m)m^{-\sigma}<\infty,
\tag{16}
\]

the Weierstrass `M`-test makes the partial sums

\[
P_X(t)
=-\sum_{2\le m\le X}\Lambda(m)m^{-\sigma}e^{-it\log m}
\tag{17}
\]

converge uniformly on the entire real line to `(3)`. Each `P_X` is a finite trigonometric polynomial with real frequencies `log m`, hence Bohr almost periodic. The uniform closure characterization of Bohr almost-periodic functions proves `(4)`.

Nothing prime-specific is needed for this closure step. More generally, if

\[
G(s)=\sum_{n\ge1}a_ne^{-\lambda_ns}
\tag{18}
\]

satisfies

\[
\sum_n|a_n|e^{-\lambda_n\sigma}<\infty,
\tag{19}
\]

then `t -> G(sigma+it)` is a uniform limit of the finite exponential sums `sum_{n<=N} a_n e^{-lambda_n sigma}e^{-it lambda_n}` and therefore lies in `AP(R)`.

### 2. Every finite divisor surgery contributes a transient `C_0` defect

The fixed completion term `A(s)` cancels in the difference, so logarithmic differentiation of `(5)` gives `(8)`. Each summand obeys

\[
\frac1{\sigma+it-z}=O(|t|^{-1})
\qquad(|t|\to\infty),
\tag{20}
\]

and is continuous on the observation line. Hence the finite sum belongs to `C_0(R)`.

If `(8)` vanished identically in `t`, analytic continuation would give `H'/H=0` on its domain and therefore `H` constant. Equivalently the inserted and removed finite divisors cancel exactly. Under the nontrivial-surgery hypothesis this is excluded, proving `(9)`.

### 3. A nonzero Bohr almost-periodic function cannot vanish at infinity

Let `g in AP(R) cap C_0(R)`, fix `t_0`, and choose `epsilon>0`. By Bohr almost periodicity, the set of `epsilon`-almost periods is relatively dense. In particular there are arbitrarily large positive `tau` such that

\[
\sup_t|g(t+\tau)-g(t)|<\epsilon.
\tag{21}
\]

Choose such a `tau` large enough that

\[
|g(t_0+\tau)|<\epsilon,
\tag{22}
\]

which is possible because `g in C_0(R)`. Then

\[
|g(t_0)|
\le
|g(t_0)-g(t_0+\tau)|+|g(t_0+\tau)|
<2\epsilon.
\tag{23}
\]

Since `epsilon` is arbitrary, `g(t_0)=0`; since `t_0` was arbitrary, `(10)` follows. Equations `(4)`, `(9)`, and linearity of `AP(R)` then prove `(11)`.

### 4. Distance from a transient defect to the recurrent source category

Let `h in C_0(R)`, let `g in AP(R)`, and put

\[
\delta=\|h-g\|_\infty.
\tag{24}
\]

Fix `t_0`. For a sequence `epsilon_r downarrow0`, choose arbitrarily large `epsilon_r`-almost periods `tau_r` of `g` such that also `h(t_0+tau_r)->0`. Then

\[
\begin{aligned}
|g(t_0)|
&\le
|g(t_0)-g(t_0+\tau_r)|
+|g(t_0+\tau_r)-h(t_0+\tau_r)|
+|h(t_0+\tau_r)|\\
&\le
\epsilon_r+\delta+|h(t_0+\tau_r)|.
\end{aligned}
\tag{25}
\]

Letting `r->infinity` gives `|g(t_0)|<=delta`. Hence

\[
\|g\|_\infty\le\delta.
\tag{26}
\]

Therefore

\[
\|h\|_\infty
\le
\|h-g\|_\infty+\|g\|_\infty
\le2\delta,
\tag{27}
\]

which gives the lower bound in `(12)` after taking the infimum over `g in AP(R)`. The upper bound follows by taking `g=0`.

Finally, because `\mathcal R_\xi(sigma+i·) in AP(R)`, addition by this fixed function maps `AP(R)` bijectively to itself. Thus

\[
\operatorname{dist}_\infty(
\mathcal R_F(\sigma+i\,\cdot),AP)
=
\operatorname{dist}_\infty(D_{F,\sigma},AP),
\tag{28}
\]

and `(13)` follows from `(12)`.

## What this changes in the Arithmetic Fidelity audit

AF-265--AF-267 separated three notions that had previously been easy to conflate: compact-open visibility, full-height metric visibility, and uniform robustness against signed matched controls. The present result adds a fourth: **membership in the exact source category**.

The AF-267 controls are engineered so their signed Cauchy-transform defects become uniformly tiny. Yet every fixed nontrivial surgery leaves a localized transient in the vertical variable: after the observer passes the finitely modified zero heights, the defect dies away. An exact discrete Dirichlet source behaves in the opposite structural way. Its vertical trace is recurrent under translations; information carried at one height recurs arbitrarily far away through the Bohr almost-periodic orbit.

This gives a precise nonlocal resource that a finite zero replacement cannot fake:

\[
\text{finite divisor surgery}
\quad\Longrightarrow\quad
\text{transient }C_0\text{ defect},
\qquad
\text{exact discrete source law}
\quad\Longrightarrow\quad
\text{Bohr recurrence}.
\tag{29}
\]

The discriminator is not another pointwise statistic or a larger vertical window. It is a global translation-closure property of the retained representation. In Arithmetic Fidelity language, the right-half-plane Euler/Dirichlet representation carries relational provenance across arbitrarily separated heights that is destroyed by locally editing only finitely many zeros.

At the same time `(14)` is an important warning. The exact source category has **zero robustness radius** against the AF-267 sequence: nonmembers can approach it uniformly. Therefore “the control has no Euler/Dirichlet source” is an exact admissibility obstruction, not by itself a quantitative stability theorem. Any RH-facing use still needs a reason that approximate or limiting controls cannot exploit this nonclosed-looking boundary at the scale relevant to the final theorem.

## Prior art and novelty assessment

The almost-periodic ingredients are classical. Ingo Schoolmann, **“On Bohr's theorem for general Dirichlet series,”** *Mathematische Nachrichten* 293(8), 1591--1612 (2020), DOI `10.1002/mana.201800542`, recalls Bohr uniform almost periodicity as uniform approximation by trigonometric polynomials and proves corresponding vertical-line almost-periodicity statements for broad classes of general Dirichlet series; see in particular Proposition 3.4 and Corollary 3.9. The implication from absolute convergence in `(19)` is even more elementary, following directly from uniform convergence of the finite exponential sums.

The intersection statement `AP(R) cap C_0(R)={0}` and the distance estimate `(12)` are derived here directly from the defining relative density of almost periods. No broad novelty claim is made for either fact; they belong naturally to classical almost-periodic function theory.

The Arithmetic Fidelity contribution is the **specific category audit of the AF-265--AF-267 zero-surgery fiber**: every nontrivial finite signed divisor modification produces a transient Cauchy defect and therefore exits the exact vertically recurrent Dirichlet-source category, even though balanced replacements can approach that category arbitrarily closely in the same supremum norm.

## Boundaries and failure modes

- This is an exact **finite-surgery** obstruction. It does not classify infinite signed rearrangements of the zero divisor, where an infinite Cauchy-transform defect need not lie in `C_0(R)` and may itself carry recurrent structure.
- The result does not distinguish rational primes from arbitrary discrete generalized-prime/frequency systems. Absolute convergence of any discrete general Dirichlet series already gives Bohr almost periodicity. The retained property is discrete-source recurrence, not rational-prime specificity.
- The result does not prove RH. The genuine `xi` channel `(3)` is almost periodic in `Re(s)>1` whether or not zeta has off-critical zeros; any genuine off-critical zeros would be globally coupled to the full source rather than obtainable as an isolated finite perturbation of the same `xi`.
- Equation `(13)` is not a positive uniform margin over the AF-267 family. Their defect norms tend to zero, so their distances to `AP(R)` tend to zero as well. Exact membership and robust recoverability remain different questions.
- The theorem uses **Bohr uniform** almost periodicity. Weaker Besicovitch, Stepanov, distributional, or mean almost-periodic notions have different closure and vanishing-at-infinity behavior and are not covered by `(10)`--`(13)`.
- The observation line is fixed at `sigma>1`, where the genuine von-Mangoldt series converges absolutely. No claim is made that the same direct uniform-almost-periodic representation persists after analytic continuation into the critical strip.
- A nontrivial finite rational multiplier can alter normalization at finitely many points without affecting the argument. Scalars disappear under logarithmic differentiation; the obstruction lives in the signed divisor defect.

## Evidence classification

`EXACT-DERIVED` for the finite-surgery `C_0` defect, the intersection theorem `(10)`, and the quantitative distance bound `(12)`--`(14)`. `LITERATURE+DERIVED` for the placement of uniformly convergent/general Dirichlet vertical traces in classical Bohr almost-periodic theory, with the actual Riemann trace `(3)` following directly from absolute convergence. The result is an Arithmetic Fidelity source-category obstruction with **no broad novelty claim** for its classical almost-periodic ingredients.