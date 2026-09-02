# WP-103 — Gibbs exponentiation sparsifies the Weil score, but critical relative entropy diverges

**Status:** `EXACT-DERIVED + DECISIVE-BOUNDARY + MATCHED-CONTROL + CLASSICAL-INFO-GEOMETRY` for the nonlinear prime-torus selector route left open by `WP-098`/`WP-099`. This is not a global Weil-positivity mechanism.

## Claim

`WP-022` found a Mathia-native signed object unusually close to the finite explicit formula: the nonconstant part of the radial logarithmic score of the Prime-Lattice Poisson geometry has exactly the prime-power Weil coefficients. `WP-098` and `WP-099` later showed that positive linear quotients and passive positive Schur elimination cannot erase the mixed-prime modes required by a positive prime-torus completion while preserving the exact one-prime rays.

There is, however, a canonical **nonlinear** escape from that selector obstruction. For `sigma>0`, put

\[
r_p=p^{-\sigma},\qquad
P_{r_p}(\theta)=\frac{1-r_p^2}{1-2r_p\cos\theta+r_p^2},
\]

and define the Haar-centered nonconstant `WP-022` score potential

\[
\boxed{
V_{p,\sigma}(\theta)
=(\log p)\bigl(1-P_{r_p}(\theta)\bigr)
=-2(\log p)\sum_{k\ge1}p^{-k\sigma}\cos(k\theta).
}
\tag{1}
\]

Exponentiate it to a normalized positive circle density

\[
\boxed{
g_{p,\sigma}
=\frac{e^{V_{p,\sigma}}}{Z_{p,\sigma}},
\qquad
Z_{p,\sigma}=\int_{\mathbb T}e^{V_{p,\sigma}}\,dm.}
\tag{2}
\]

For every finite prime set `F`, the product Gibbs law

\[
\eta_{\sigma,F}
=G_{\sigma,F}m_F,
\qquad
G_{\sigma,F}=\prod_{p\in F}g_{p,\sigma}
\tag{3}
\]

is strictly positive and satisfies

\[
\boxed{
\log G_{\sigma,F}
=\sum_{p\in F}V_{p,\sigma}
-\sum_{p\in F}\log Z_{p,\sigma}.}
\tag{4}
\]

Consequently every nonconstant mixed-prime Fourier coefficient of `log G_{sigma,F}` is **exactly zero**, while

\[
\boxed{
\widehat{\log G_{\sigma,F}}(\pm k e_p)
=-(\log p)p^{-k\sigma}
\qquad(k\ge1).}
\tag{5}
\]

At `sigma=1/2`, (5) is exactly the finite-prime Weil ray. Thus the nonlinear logarithm really can do what the positive linear selectors of `WP-098`/`WP-099` cannot: a positive carrier can have a logarithm with exact sparse prime-power support and no mixed-prime modes.

This does **not** supply Weil positivity, for two independent reasons.

First, positivity of (2) is tautological: `e^V/Z` is a positive density for **every** bounded real potential `V`, with arbitrary signs and Fourier coefficients. Therefore the theorem `g>=0` imposes no sign condition on the arithmetic observable `V=log g+constant`; it cannot be the missing independent Weil sign theorem.

Second, the all-prime Gibbs geometry becomes non-regular at exactly the critical exponent. If

\[
d_{p,\sigma}
:=D_{\rm KL}(g_{p,\sigma}m\,\|\,m),
\]

then, up to harmless finitely many primes,

\[
\boxed{
d_{p,\sigma}\asymp
\|V_{p,\sigma}\|_{L^2(m)}^2
=rac{2(\log p)^2}{p^{2\sigma}-1}.}
\tag{6}
\]

Hence

\[
\boxed{
\sum_p d_{p,\sigma}<\infty
\iff \sigma>\frac12,}
\qquad
\boxed{
\sum_p d_{p,1/2}=\infty.}
\tag{7}
\]

Equivalently, the finite-cylinder relative entropies

\[
D_{\rm KL}(\eta_{\sigma,F}\|m_F)
=\sum_{p\in F}d_{p,\sigma}
\tag{8}
\]

are unbounded as `F` exhausts the primes at the Weil boundary. The normal Gibbs information/free-energy geometry therefore has infinite global cost precisely where (5) reaches the critical coefficients.

Moreover this particular nonlinear escape is not rescued by replacing the full coordinate Fisher geometry of `WP-102` with the one-dimensional multiplicative/Kronecker flow. For

\[
X=\sum_p(\log p)\partial_{\theta_p},
\]

the finite-cylinder log-density energy is

\[
\boxed{
\|X\log G_{\sigma,F}\|_{L^2(m_F)}^2
=2\sum_{p\in F}(\log p)^4
\frac{q_p(1+q_p)}{(1-q_p)^3},
\qquad q_p=p^{-2\sigma}.}
\tag{9}
\]

At `sigma=1/2`, its `k=1` contribution already dominates

\[
2\sum_{p\in F}\frac{(\log p)^4}{p},
\]

so the energy diverges as `F` grows. This does not close the arbitrary measure-level Kronecker-flow escape left open by `WP-102`; it closes it for the exact Gibbs/log-density selector constructed here.

Thus the nonlinear route

```text
WP-022 exact finite Weil score
    -> exponentiate to a positive Gibbs carrier
    -> take log to erase every mixed-prime mode exactly
    -> use Gibbs / entropy / multiplicative-flow positivity
    -> global Weil positivity
```

fails. The **selector step succeeds algebraically**, which is an important boundary on `WP-098`/`WP-099`, but positivity is too universal to constrain the selected signed potential and the natural global positive energies diverge at the critical exponent. A surviving nonlinear selector must therefore obtain its sign from genuinely new geometry rather than from mere exponentiation, and must also supply the archimedean and polar sectors without a hand-chosen critical renormalization.

## 1. The potential is the nonconstant `WP-022` score, not a new fitted kernel

`WP-022` gives the exact single-prime radial score

\[
\partial_\sigma\log P_{p^{-\sigma}}(\theta)
=
2(\log p)\frac{p^{-2\sigma}}{1-p^{-2\sigma}}
-2(\log p)\sum_{k\ge1}p^{-k\sigma}\cos(k\theta).
\tag{10}
\]

The second term is exactly (1). Since the Poisson kernel has Haar mean one,

\[
\int_{\mathbb T}V_{p,\sigma}\,dm
=(\log p)\left(1-\int P_{r_p}\,dm\right)=0.
\tag{11}
\]

Thus `V_{p,sigma}` is the Haar-centered nonconstant score already forced by the Prime-Lattice Poisson geometry. At the critical exponent its Fourier expansion is

\[
V_{p,1/2}(\theta)
=-2\sum_{k\ge1}\frac{\log p}{p^{k/2}}\cos(k\theta),
\tag{12}
\]

with no zero data or analytic continuation.

The construction (2) is therefore a serious test of the most obvious nonlinear escape: instead of squaring the signed score as Fisher geometry does, use it as a Gibbs potential so that positivity lives at the level of the carrier while the signed arithmetic remains in its logarithm.

## 2. Logarithm removes mixed-prime modes exactly

Every `g_{p,sigma}` depends on one coordinate only. For finite `F`, taking the logarithm of the product in (3) gives (4) identically. The normalizing constants contribute only to frequency zero. Since (1) has complex Fourier coefficients

\[
\widehat V_{p,\sigma}(\pm k)
=-(\log p)p^{-k\sigma},
\tag{13}
\]

we obtain (5), while every Fourier character involving two or more prime coordinates has coefficient zero in `log G_{sigma,F}`.

This is a genuine nonlinear distinction from `WP-097`--`WP-099`. A positive **density** generally requires mixed-prime Fourier coefficients, but its logarithm need not: factorization turns multiplication into addition before the readout is taken. Therefore the earlier positive-linear and passive-elimination no-go results must not be generalized to arbitrary nonlinear readouts.

The price is equally exact. The map

\[
V\longmapsto \frac{e^V}{\int e^Vdm}
\tag{14}
\]

works for every bounded real `V`. It would convert a randomized generalized-prime potential, a sign-flipped potential, or a completely artificial Fourier polynomial into an equally positive carrier. Consequently carrier positivity is logically upstream of, and insensitive to, the arithmetic sign pattern in `V`. No implication of the form

\[
G\ge0\quad\Longrightarrow\quad
\text{Weil quadratic form of the coefficients of }\log G\ge0
\]

follows from exponentiation.

This is the decisive sign failure even at finite `F`.

## 3. Exact local size of the Gibbs potential

The Poisson expansion gives

\[
V_{p,\sigma}
=-2(\log p)\sum_{k\ge1}r_p^k\cos(k\theta).
\]

Orthogonality of the cosine modes therefore yields

\[
\begin{aligned}
\|V_{p,\sigma}\|_2^2
&=4(\log p)^2\sum_{k\ge1}r_p^{2k}\frac12\\
&=2(\log p)^2\frac{r_p^2}{1-r_p^2}\\
&=\boxed{
\frac{2(\log p)^2}{p^{2\sigma}-1}.}
\end{aligned}
\tag{15}
\]

The sup norm is also explicit. Since

\[
\max P_r=\frac{1+r}{1-r},
\qquad
\min P_r=\frac{1-r}{1+r},
\]

we have

\[
\boxed{
M_{p,\sigma}:=\|V_{p,\sigma}\|_\infty
=\frac{2(\log p)p^{-\sigma}}{1-p^{-\sigma}}.}
\tag{16}
\]

For every fixed `sigma>0`, `M_{p,sigma}->0` as `p->infinity`. This makes the local Gibbs entropy uniformly quadratic in the potential on the prime tail.

## 4. Relative entropy is comparable to the squared score potential

For one prime abbreviate `V=V_{p,sigma}`, let

\[
\psi(t)=\log\int e^{tV}\,dm,
\qquad 0\le t\le1.
\tag{17}
\]

Because `int V dm=0`,

\[
\psi(0)=\psi'(0)=0.
\]

The tilted law with density `e^{tV}/int e^{tV}dm` has

\[
\psi''(t)=\operatorname{Var}_t(V).
\tag{18}
\]

The local relative entropy is

\[
\begin{aligned}
d_{p,\sigma}
&=\int g_{p,\sigma}\log g_{p,\sigma}\,dm\\
&=\psi'(1)-\psi(1)\\
&=\boxed{\int_0^1 t\,\psi''(t)\,dt.}
\end{aligned}
\tag{19}
\]

This identity gives a direct elementary comparison, with no asymptotic theorem required. Put `M=||V||_infty` and `s^2=||V||_2^2`. For every `t in [0,1]`, the tilted density lies between `e^{-2M}` and `e^{2M}`, so

\[
\mathbb E_t[V^2]\ge e^{-2M}s^2.
\tag{20}
\]

Using `int V dm=0` and `|e^{tV}-1|<=t e^M|V|`,

\[
|\mathbb E_t[V]|
\le t e^{2M}s^2.
\tag{21}
\]

Since `s^2<=M^2`, equations (20)--(21) imply

\[
\operatorname{Var}_t(V)
\ge\bigl(e^{-2M}-e^{4M}M^2\bigr)s^2.
\tag{22}
\]

For `M<=1/4` the coefficient on the right exceeds `2/5`. The upper bound

\[
\operatorname{Var}_t(V)
\le\mathbb E_t[V^2]
\le e^{2M}s^2
<2s^2
\tag{23}
\]

holds on the same tail. Integrating (19) therefore gives, for all sufficiently large primes,

\[
\boxed{
\frac15\|V_{p,\sigma}\|_2^2
\le d_{p,\sigma}
\le \|V_{p,\sigma}\|_2^2.}
\tag{24}
\]

Combining (15) and (24) proves (6).

For the ordinary primes,

\[
\sum_p\frac{(\log p)^2}{p^{2\sigma}-1}
\]

converges when `sigma>1/2` by comparison with `sum_{n>=2}(log n)^2n^{-2sigma}`. At `sigma=1/2` it becomes

\[
\sum_p\frac{(\log p)^2}{p-1}=\infty,
\tag{25}
\]

already by Euler's divergence of `sum_p 1/p`; below `1/2` the terms are larger. This proves the threshold (7).

For finite products, KL additivity gives (8). In the infinite product, relative entropy with respect to product Haar is the supremum of finite-cylinder relative entropies, so (7) says that the critical Gibbs carrier has infinite global relative entropy. The product probability itself still exists abstractly; what fails is precisely the finite regular information geometry that might have converted its positivity into a global sign mechanism.

## 5. The multiplicative/Kronecker-flow energy also diverges for this selector

`WP-102` proves a correlation-robust divergence for the full cylindrical Fisher geometry but deliberately leaves a one-dimensional Kronecker-flow geometry open. The present Gibbs selector can be tested against that escape directly because its logarithm is explicit.

Let

\[
X=\sum_{p\in F}(\log p)\partial_{\theta_p}
\tag{26}
\]

on a finite prime cylinder. Constants disappear under `X`, and (1) gives

\[
XV_{p,\sigma}
=2(\log p)^2\sum_{k\ge1}k p^{-k\sigma}\sin(k\theta_p).
\tag{27}
\]

Different prime coordinates and sine modes are orthogonal under Haar. Hence

\[
\begin{aligned}
\|X\log G_{\sigma,F}\|_2^2
&=2\sum_{p\in F}(\log p)^4
\sum_{k\ge1}k^2p^{-2k\sigma}\\
&=2\sum_{p\in F}(\log p)^4
\frac{q_p(1+q_p)}{(1-q_p)^3},
\end{aligned}
\tag{28}
\]

which is (9). At `sigma=1/2` the `k=1` terms alone give

\[
\|X\log G_{1/2,F}\|_2^2
\ge2\sum_{p\in F}\frac{(\log p)^4}{p}
\longrightarrow\infty.
\tag{29}
\]

Thus the obvious multiplicative-flow Dirichlet norm of the exact sparse log potential is no better behaved than the entropy norm. This is narrower than `WP-102`: a singular correlated measure could in principle possess some other finite flow-level geometry. Equation (29) only rules out the canonical Gibbs/log-density realization tested here.

## 6. Matched free-generator control

Nothing in the construction distinguishes rational primes. For a free commutative monoid with generator energies `E_j>0`, put

\[
r_j=e^{-\sigma E_j},
\qquad
V_{j,\sigma}=E_j(1-P_{r_j}).
\tag{30}
\]

Then

\[
\widehat V_{j,\sigma}(\pm k)
=-E_j e^{-k\sigma E_j},
\tag{31}
\]

and the same Gibbs exponentiation produces a positive product carrier whose logarithm has only generator-power Fourier rays. Its local quadratic size is

\[
\boxed{
\|V_{j,\sigma}\|_2^2
=\frac{2E_j^2}{e^{2\sigma E_j}-1}.}
\tag{32}
\]

Whenever `E_j e^{-sigma E_j}->0`, the same bounded-potential argument makes local entropy comparable to (32) on the tail. Therefore the entropy boundary is governed solely by summability of

\[
\sum_j\frac{E_j^2}{e^{2\sigma E_j}-1},
\tag{33}
\]

not by any specifically Riemannian functional equation or zero geometry. Setting `E_p=log p` merely places that generic free-generator threshold at `sigma=1/2`.

This matched control reinforces the sign objection: exponentiation can positively package any such generator system, including generalized-prime controls that do not satisfy the Riemann Weil criterion.

## 7. Prior-art and novelty audit

No novelty is claimed for Gibbs/exponential families, Kullback--Leibler divergence, convex log-partition functions, or additivity of relative entropy. These are classical information geometry. `WP-023` already records Amari--Cichocki as the durable repository anchor for divergence-induced information geometry, and `SOURCES.md` already records Kakutani for infinite product measure-class questions.

This finding is not a rephrasing of `WP-023`. There the positive divergences are taken **between members of the original product-Poisson family**, whose critical score has infinite Fisher length. Here the `WP-022` nonconstant score itself is exponentiated into a new Gibbs family specifically to test the nonlinear selector that `WP-098`/`WP-099` do not cover. The new exact fact is (4)--(5): logarithm completely removes mixed-prime Fourier support while retaining the prime-power coefficients. The new negative boundary is that this successful nonlinear sparsification has tautological carrier positivity and infinite critical entropy/multiplicative-flow energy.

Likewise this differs from `WP-100`--`WP-102`. Those findings constrain positive completions whose **measure moments** carry the exact one-prime rays. Here the exact arithmetic is carried by the **log density** instead. That distinction is why mixed modes can disappear algebraically, and also why the positivity theorem becomes vacuous with respect to the sign of the selected potential.

A bounded literature search for `Weil positivity`/Riemann-zeta constructions combining prime-torus Gibbs exponentiation, logarithmic Fourier sparsification, and relative entropy did not identify a prior result asserting this Mathia-specific combination. The underlying analytic ingredients are nevertheless classical, so the project-level contribution should be read only as the exact specialization and obstruction above, not as a new theorem of information geometry.

## 8. Consequence for the research frontier

The live mixed-prime selector question is narrowed in a useful way:

```text
positive linear quotient / conditional expectation
    -> impossible by WP-098

passive positive Schur elimination
    -> impossible by WP-099

nonlinear logarithm of a Gibbs carrier
    -> exact sparsification is possible
    -> positivity is tautological for arbitrary signed potentials
    -> critical relative entropy is infinite
    -> exact log-potential Kronecker energy is infinite
```

Therefore **mixed-prime sparsification itself is not the decisive missing theorem**. A nonlinear map can perform it exactly. What remains missing is a construction in which the selected finite-prime observable is tied to a nontrivial independent positive form whose sign survives the selection, while the same global object intrinsically generates the archimedean and polar terms.

The surviving routes are correspondingly more constrained: genuinely coupled finite--archimedean geometry before positivity, singular/nonlocal boundary structures with an independent sign theorem, higher/cohomological quotients that are not mere positive expectations, or a measure-level Kronecker mechanism not representable by the exact Gibbs log potential above. Simply exponentiating the known Weil comb, even when that comb came intrinsically from the Prime-Lattice Poisson score, does not qualify.