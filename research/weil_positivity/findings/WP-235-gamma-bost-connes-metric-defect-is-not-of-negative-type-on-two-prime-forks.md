# WP-235 — Gamma–Bost–Connes metric defect is not of negative type on two-prime forks

**Status:** `EXACT-DERIVED + TWO-PRIME-FORK-CERTIFICATE + NOT-CND + NO-SCHOENBERG-HADAMARD-CORRECTION + MATCHED-DIVISIBILITY-CONTROL + FREE-MONOID-CONTROL + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-233` and `WP-234` isolate two independently positive critical kernels with the same one-prime restrictions: the Bost–Connes Gram uses the weighted divisor `ell^1` distance, while the one-dimensional Gamma/log Gram uses the absolute scalar logarithmic distance. `WP-234` already rules out interpreting their **additive** difference as a passive positive correction.

There is a second natural escape: perhaps the discrepancy is itself a positive multiplicative sector. If the metric defect between the two kernels were conditionally negative definite, Schoenberg's theorem would make its exponential a positive-definite kernel, so one could pass from one Gram to the other by a canonical positive Hadamard factor rather than by an additive correction.

That escape fails on the smallest genuinely mixed-prime configuration. The defect is pointwise nonnegative and vanishes on every divisibility chain, but on any fork `{a,ap,aq}` with distinct primes `p<q` it violates conditional negative definiteness. Equivalently, the corresponding normalized exponential kernel has a negative `3 x 3` determinant for every positive scale. Thus the independent-Cauchy Bost–Connes geometry and the common-Cauchy Gamma geometry cannot be related by a separate scalar Schoenberg/Markov-positive correction sector. A surviving global construction must change or derive the mixed-prime coupling before the final scalar positivity readout, or leave the scalar Hadamard/Schoenberg class entirely.

## 1. Exact defect between the two canonical distances

For positive integers `m,n`, write

\[
g=(m,n),\qquad m=ga,\qquad n=gb,\qquad (a,b)=1.
\tag{1}
\]

The divisor distance from `WP-233` is

\[
d_{\rm div}(m,n)
=\sum_p |v_p(m)-v_p(n)|\log p
=\log a+\log b,
\tag{2}
\]

whereas the scalar logarithmic distance is

\[
d_{\log}(m,n)
=|\log m-\log n|
=|\log a-\log b|.
\tag{3}
\]

Define their nonnegative defect

\[
\boxed{
D(m,n):=d_{\rm div}(m,n)-d_{\log}(m,n).
}
\tag{4}
\]

Using `x+y-|x-y|=2 min(x,y)` for `x,y>=0` gives the exact formula

\[
\boxed{
D(m,n)
=2\min(\log a,\log b)
=2\log\min\!\left(\frac{m}{g},\frac{n}{g}\right).
}
\tag{5}
\]

Hence `D>=0`. Moreover `D(m,n)=0` whenever `m|n` or `n|m`. The entire discrepancy is therefore invisible on every divisibility chain, exactly matching the fact from `WP-233`/`WP-234` that the two positive kernels agree on each prime ray and, more generally, on comparable states.

At a branching pair the defect is nonzero. For any integer `a>=1` and distinct primes `p<q`,

\[
D(a,ap)=D(a,aq)=0,
\tag{6}
\]

while

\[
\begin{aligned}
D(ap,aq)
&=(\log p+\log q)-|\log p-\log q|\\
&=\boxed{2\log p}>0.
\end{aligned}
\tag{7}
\]

Thus `D` is precisely a mixed-prime branching/cancellation defect: it measures what is lost when the signed valuation displacement is collapsed from the full divisor `ell^1` geometry to the one-dimensional sum `log m-log n`.

## 2. The two-prime fork violates conditional negative definiteness

A Hermitian kernel `D` with zero diagonal is conditionally negative definite when

\[
\sum_{i,j}\overline{c_i}c_jD(x_i,x_j)\le0
\quad\text{whenever}\quad
\sum_i c_i=0.
\tag{8}
\]

Take the three points

\[
x_0=a,\qquad x_1=ap,\qquad x_2=aq
\tag{9}
\]

and the real coefficients

\[
(c_0,c_1,c_2)=(-2,1,1).
\tag{10}
\]

They sum to zero. By (6)--(7), the only nonzero off-diagonal defect on this fork is

\[
D(x_1,x_2)=D(x_2,x_1)=2\log p.
\tag{11}
\]

Therefore

\[
\boxed{
\sum_{i,j}c_ic_jD(x_i,x_j)
=4\log p>0.
}
\tag{12}
\]

This has the wrong sign for (8). Consequently

\[
\boxed{D\text{ is not conditionally negative definite.}}
\tag{13}
\]

The obstruction does not depend on the basepoint `a`, on a limiting argument, or on infinitely many primes. It appears on one exact three-state configuration containing only a common ancestor and two distinct prime children.

## 3. Every nontrivial Schoenberg exponential fails on the same fork

The same obstruction can be read directly at the positive-kernel level. For `t>0`, define the would-be multiplicative correction

\[
R_t(m,n):=e^{-tD(m,n)}.
\tag{14}
\]

On the fork (9), put

\[
r=e^{-2t\log p}=p^{-2t},\qquad 0<r<1.
\tag{15}
\]

Then

\[
[R_t(x_i,x_j)]_{i,j=0}^2
=
\begin{pmatrix}
1&1&1\\
1&1&r\\
1&r&1
\end{pmatrix}.
\tag{16}
\]

Its determinant is

\[
\boxed{
\det R_t=-(1-r)^2<0.
}
\tag{17}
\]

Hence `R_t` is not positive semidefinite for **any** `t>0`. This finite determinant is also an explicit instance of the classical Schoenberg equivalence between negative-definite kernels and positivity of all exponentials `e^{-tD}`.

At the critical half-density scale `t=1/2`, equations (2)--(5) and the kernels of `WP-234` give

\[
\boxed{
\frac{G_{\rm BC}(m,n)}{K_\infty(m,n)}
=e^{-D(m,n)/2}
=\frac{(m,n)}{\min(m,n)}.
}
\tag{18}
\]

On `{a,ap,aq}` the nontrivial entry is `1/p`, so

\[
\det\left[\frac{G_{\rm BC}}{K_\infty}\right]
=-\left(1-\frac1p\right)^2<0.
\tag{19}
\]

Thus the exact critical ratio is not a positive-definite normalized correlation kernel.

The reverse ratio fails even more immediately. Since

\[
\frac{K_\infty(ap,aq)}{G_{\rm BC}(ap,aq)}=p>1
\tag{20}
\]

while its diagonal entries are one, its `2 x 2` principal minor on `{ap,aq}` is negative. Any normalized positive-semidefinite kernel must satisfy `|K(x,y)|<=1` by Cauchy--Schwarz. Therefore neither direction admits a normalized positive Hadamard factor:

\[
\boxed{
G_{\rm BC}\ne K_\infty\circ R\quad\text{and}\quad
K_\infty\ne G_{\rm BC}\circ S
}
\tag{21}
\]

for any scalar normalized positive-definite factor equal to the exact pointwise quotient.

## 4. Why this is stronger than the additive obstruction in WP-234

`WP-234` observes that `K_\infty-G_{\rm BC}` cannot be positive semidefinite: both kernels have diagonal one, so a positive difference with zero diagonal would have to vanish identically. That closes a passive **additive** correction.

The present certificate closes a different natural mechanism. Positive metric/Dirichlet sectors often combine multiplicatively after exponentiation: if an independently geometric correction supplied a negative-type defect `D`, then `e^{-tD}` would be a positive Gram/Markov factor, and Schur multiplication would preserve positivity. Equations (12) and (17) prove that the exact Bost–Connes-to-Gamma discrepancy has no such scalar realization.

The failure is geometrically informative. Both `d_div` and `d_log` are individually negative-type distances, but their nonnegative difference is not. Pointwise ordering of two negative-type metrics therefore does not make the residual a new positive energy. The scalar projection from the valuation vector to `log n` destroys exactly the mixed-prime branching geometry needed for such a residual decomposition.

This is not a sign convention issue: replacing `D` by `-D` makes the exponential exceed one on the mixed-prime pair while retaining unit diagonal, so the reverse normalized positive factor is impossible as well.

## 5. The obstruction survives the weighted free-monoid control

The calculation is not special to rational primes. Let a free commutative monoid have two generators `g_1,g_2` with positive weights `w_1<=w_2`. Compare the valuation `ell^1` distance

\[
d_1(\alpha,\beta)
=\sum_j |\alpha_j-\beta_j|w_j
\tag{22}
\]

with the scalarized distance

\[
d_s(\alpha,\beta)
=\left|\sum_j(\alpha_j-\beta_j)w_j\right|.
\tag{23}
\]

On any translated fork `{\gamma,\gamma+e_1,\gamma+e_2}`, the defect `D_w=d_1-d_s` vanishes from the ancestor to either child and equals

\[
D_w(\gamma+e_1,\gamma+e_2)=2w_1>0.
\tag{24}
\]

The coefficients `(-2,1,1)` again give conditional quadratic value `4w_1>0`, and the exponential kernel again has determinant

\[
-(1-e^{-2tw_1})^2<0.
\tag{25}
\]

Thus this is a universal branching obstruction for scalarizing a weighted free-monoid `ell^1` geometry. It does not by itself distinguish the rational primes, the Riemann Gamma factor, or the completed zeta function. Its value is as a matched falsifier for the proposed global-gluing mechanism.

## 6. Aggressive falsification and exact scope

**Does failure of `D` to be CND mean either canonical kernel is not positive?** No. `WP-234` gives independent Bochner proofs that both `G_BC` and `K_infty` are positive definite. The obstruction concerns only their **exact pointwise quotient** as an additional scalar positive sector.

**Could another scalar factor work if it does not equal the quotient?** Not while keeping both endpoint kernels fixed under Hadamard multiplication. Once `G_BC`, `K_infty`, and the multiplicative relation are specified, the factor is pointwise forced wherever the denominator is nonzero; both kernels are strictly positive, so (18) is unavoidable.

**Could an additive correction still work after changing the diagonal?** That is a different construction and must derive its diagonal/counterterm independently. `WP-233` shows that the canonical local jump diagonal needed to repair the finite Weil block diverges globally, and `WP-234` rules out the equal-diagonal passive difference between these two normalized Grams.

**Could a matrix-valued or operator-valued correction evade the determinant?** Yes. The present result is scalar and Hadamard/Schoenberg specific. A noncommutative correspondence, matrix-valued boundary sector, graded/indefinite intermediate object, non-passive reduction, or cohomological incidence could alter the mixed-prime architecture before the final positive form. Such a route must prove its sign independently rather than inherit it from the scalar defect considered here.

**Could one choose a different cross-prime Cauchy coupling?** Yes, and `WP-234` supplies a continuum of positive matched controls. This finding does not select a coupling. It shows that the discrepancy between the two distinguished endpoint couplings cannot itself be interpreted as a separate positive scalar energy.

**Does the result yield Weil positivity or RH?** No. It is a negative structural result. It removes a natural positive-gluing mechanism and sharpens what a surviving Mathia-native global geometry must do.

## 7. Prior art and novelty boundary

No historical novelty is claimed for conditionally negative-definite kernels, Schoenberg's theorem, Schur/Hadamard products of positive kernels, `ell^1` negative type, normalized-kernel Cauchy--Schwarz bounds, or classical positive-definiteness results for GCD matrices. A convenient modern source restating Schoenberg's classical 1938 theorem is V. P. Zastavnyi, *Analog of Schoenberg's Theorem for a-Conditionally Negative Definite Matrix-Valued Kernels*, Mathematical Notes 114 (2023), 66--76, DOI `10.1134/S0001434623070064` / MathNet `https://www.mathnet.ru/eng/mzm13758`. `WP-234` already records Guillot--Wu, *Total nonnegativity of GCD matrices and kernels*, arXiv:1901.01947, for the classical GCD-matrix background.

The bounded structural audit searched for the exact quotient `gcd(m,n)/min(m,n)`, for Schoenberg/negative-type treatments of that ratio, and for the defect `sum |x_j|-|sum x_j|`. It did not surface prior work asserting the Mathia-specific two-prime-fork consequence above. Absence from a bounded search is not a novelty proof.

The internal novelty boundary is precise. `WP-233` derives the divisor-`ell^1` versus scalar-log mismatch. `WP-234` classifies the endpoint kernels as independent-versus-common Cauchy couplings, shows that prime-ray data do not determine the coupling, and kills the additive equal-diagonal positive correction. The durable new delta here is the exact negative-type classification of the **metric residual itself**, with a three-state certificate valid at every positive Schoenberg scale.

## 8. Consequence for the live global-completion frontier

The two canonical critical positive geometries now fail to decompose into one another in both simplest scalar-positive senses:

\[
\boxed{
\text{no additive PSD correction (WP-234),}
\qquad
\text{no multiplicative Schoenberg/PD correction (WP-235).}
}
\tag{26}
\]

The reason is already visible before archimedean/polar assembly: the common-coordinate Gamma geometry identifies opposite prime-coordinate motions by scalar cancellation, whereas the Bost–Connes geometry keeps their full divisor `ell^1` separation. That lost branching information is pointwise nonnegative but is not itself a positive Dirichlet/Schoenberg geometry.

Therefore the accepted mixed-prime/global-completion program should not try to bolt a separate scalar positive correction onto one endpoint kernel to obtain the other. A surviving route must derive a genuinely joint finite--archimedean object — or another source-forced cross-prime dependence structure — **before** the final sign theorem. Only then is it meaningful to test whether the same intrinsic construction supplies the finite Mangoldt terms, Gamma/polar counterterms, and a global Weil quadratic form whose nonnegativity is independent of RH.

## Dependencies

- `research/weil_positivity/findings/WP-216-bost-connes-critical-conditioning-forces-poisson-gcd-gram-but-weil-ray-is-indefinite-defect.md`
- `research/weil_positivity/findings/WP-233-adjacent-gamma-jump-density-samples-bost-connes-weil-ray-but-positive-completion-is-divergent.md`
- `research/weil_positivity/findings/WP-234-gamma-and-bost-connes-critical-grams-are-common-versus-independent-cauchy-couplings.md`
- `research/weil_positivity/findings/WP-118-gamma-schoenberg-shared-coupling-has-coherent-prime-divergence-through-sigma-one.md`
- `research/weil_positivity/clues/CLUE-mixed-prime-positive-completion-selector-quotient.md`
- `research/weil_positivity/SOURCES.md`

## Bottom line

The nonnegative metric defect between the critical Bost–Connes divisor Gram and the one-dimensional Gamma/log Gram is **not** of negative type. On every two-prime fork `{a,ap,aq}`, it vanishes along the two ancestor edges but is positive between the children, giving both an immediate CND-sign violation and a negative determinant for `e^{-tD}` at every `t>0`. Consequently the exact Bost–Connes/Gamma mismatch cannot be packaged as an independently positive scalar Schoenberg/Markov Hadamard sector. The remaining route must alter or derive the mixed-prime coupling at a more intrinsic global level before positivity is read out.