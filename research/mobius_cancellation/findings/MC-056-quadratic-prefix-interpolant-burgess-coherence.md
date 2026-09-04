# MC-056 — Distinct exact-prefix quadratic interpolants pay a near-quartic product-conductor cost

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Fix `X>=2`. Let `q_1 != q_2` be odd primes larger than `X`, and let

\[
\chi_i(n)=\left(\frac{n}{q_i}\right)
\qquad(i=1,2)
\]

be the primitive quadratic characters modulo `q_i`. Assume both characters are exact Möbius-prefix interpolants in the sense used in `MC-055`:

\[
\chi_i(p)=-1
\qquad\text{for every prime }p\le X.
\tag{1}
\]

Equivalently, the square-free-supported comparators

\[
f_i(n)=\mu(n)^2\chi_i(n)
\]

satisfy `f_i(n)=mu(n)` for every `n<=X`.

Put

\[
Q=q_1q_2,
\qquad
\psi=\chi_1\chi_2.
\tag{2}
\]

Because the conductors are distinct coprime primes, `psi` is a primitive nonprincipal quadratic character of square-free conductor `Q`. Moreover

\[
\boxed{\psi(n)=1\qquad(1\le n\le X).}
\tag{3}
\]

Consequently its initial character sum has no cancellation at all:

\[
\boxed{\sum_{n\le X}\psi(n)=X.}
\tag{4}
\]

Applying the classical Burgess character-sum estimate to `(4)` gives the following pairwise conductor obstruction. For every fixed `delta>0`,

\[
\boxed{q_1q_2\gg_{\delta}X^{4-\delta}.}
\tag{5}
\]

In particular, after relabelling the arbitrarily small exponent loss,

\[
\boxed{\max(q_1,q_2)\gg_{\delta}X^{2-\delta}.}
\tag{6}
\]

Thus two **distinct** quadratic characters that are both completely indistinguishable from Möbius on the full coefficient prefix through `X` cannot both remain low-conductor objects. The exact-prefix escape in `MC-055` is therefore not freely repeatable across distinct quadratic interpolants with uniformly mild arithmetic complexity: pairwise coherence forces a near-quartic product-conductor budget.

This does not improve the Mertens bound and does not rule out a single moving comparator family. It is a multiscale/complexity obstruction for the specific quadratic-character interpolation class isolated in `MC-055`.

## 1. The quotient character is exactly principal on the observed prefix

For every integer `n<=X`, no prime divisor of `n` equals `q_1` or `q_2`, because both conductors exceed `X`. Write

\[
n=\prod_p p^{v_p(n)}.
\]

Every prime appearing in the product satisfies `p<=X`. From `(1)` and complete multiplicativity,

\[
\chi_i(n)=\prod_{p\mid n}(-1)^{v_p(n)}=(-1)^{\Omega(n)}
\qquad(i=1,2).
\tag{7}
\]

Hence

\[
\psi(n)=\chi_1(n)\chi_2(n)=1
\]

for all `n<=X`, proving `(3)` and `(4)`.

The argument is stronger than agreement of the square-free-supported comparators alone. Each quadratic character itself agrees with the Liouville sign law on the complete prefix, so the product character loses every visible phase on that prefix.

The distinctness assumption is load-bearing. If `q_1=q_2`, then `chi_1 chi_2` is principal and no nonprincipal character-sum estimate applies. The present obstruction measures the arithmetic cost of **changing** exact-prefix interpolant, not the cost of reusing one fixed character.

## 2. The product character is a primitive cubefree Burgess input

Each `chi_i` is primitive modulo the prime `q_i`. Since the conductors are coprime, their product is primitive modulo

\[
Q=q_1q_2.
\]

It is nonprincipal because its local component at either conductor prime is nonprincipal. Equivalently, in the quadratic language `psi` is the primitive real character associated with the product of the two coprime prime discriminant components.

The modulus `Q` is square-free and therefore cubefree. This matters because the standard Burgess theorem permits arbitrary fixed positive integer `r` for primitive characters of cubefree modulus.

Treviño's modern statement of the classical Burgess inequality (`MC-S34`) gives, for every fixed integer `r>=1` and every `epsilon>0`,

\[
\left|\sum_{M<n\le M+N}\psi(n)\right|
\ll_{r,\varepsilon}
N^{1-1/r}
Q^{(r+1)/(4r^2)+\varepsilon}.
\tag{8}
\]

Take `M=0` and `N=X`. Equation `(4)` turns `(8)` into

\[
X^{1/r}
\ll_{r,\varepsilon}
Q^{(r+1)/(4r^2)+\varepsilon}.
\tag{9}
\]

For fixed `r`, by taking `epsilon` arbitrarily small, `(9)` implies that for every `eta>0`,

\[
Q\gg_{r,\eta}
X^{4r/(r+1)-\eta}.
\tag{10}
\]

Now choose `r` sufficiently large, still fixed independently of `X`, so that

\[
\frac{4r}{r+1}>4-\frac\delta2,
\]

and then choose the Burgess epsilon small enough that the remaining exponent loss is below `delta/2`. This yields `(5)`. Equation `(6)` follows from

\[
\max(q_1,q_2)\ge\sqrt{q_1q_2}.
\]

No zeta zero-free region, Mertens estimate, GRH input, or unproved character-sum hypothesis enters this deduction.

## 3. What this adds to the MC-055 uniformity obstruction

`MC-055` proves that for every finite scale `X` one may manufacture a quadratic character `chi_X` whose associated square-free comparator agrees exactly with Möbius through `X`, while the frozen comparator has an unconditional square-root **exponent** for its own summatory function. It then shows that the missing difficulty moves into uniform control of the scale-dependent comparator certificate.

One possible escape left there was to impose a multiscale relation constraining how the comparator may change as `X` grows. The present result supplies a first exact constraint of that type.

Suppose a construction wants to replace one exact-prefix quadratic interpolant by another while keeping both conductors polynomially small at the same observation scale. Equations `(5)`--`(6)` say that the replacement cannot be cheap in both coordinates. For example, two distinct interpolants cannot both satisfy

\[
q_i\le X^{2-c}
\]

for any fixed `c>0` once `X` is sufficiently large, because then their product is at most `X^{4-2c}`, contradicting `(5)` with a smaller exponent loss.

There is a useful asymmetric form. If one interpolant has conductor

\[
q_1\le X^{1+o(1)},
\]

then any **distinct** exact-prefix replacement must satisfy

\[
\boxed{q_2\ge X^{3-o(1)}.}
\tag{11}
\]

This does not say that an interpolant of conductor `X^{1+o(1)}` exists. It says that if a scale-coherent scheme ever has one, switching to another character while preserving exact prefix agreement incurs a nearly cubic conductor jump.

Thus a moving-family strategy cannot treat the interpolants as arbitrary disposable finite-prefix certificates while simultaneously demanding low-complexity conductor control. The classical short-character-sum barrier already couples distinct certificates globally.

## 4. Why this is not a disguised Mertens argument

The obstruction never estimates `M(X)`. Indeed the entire point of multiplying two exact-prefix characters is that the Möbius/Liouville phase disappears:

\[
\chi_1(n)\chi_2(n)=1
\qquad(n\le X).
\]

The lower bound arises because a nonprincipal Dirichlet character cannot imitate the principal character for an interval much longer than the Burgess `Q^{1/4+o(1)}` scale. The argument therefore constrains the **complexity of two competing finite-prefix explanations**, not Möbius cancellation itself.

This is structurally different from `MC-055`'s pointwise lower bound on a cancellation certificate,

\[
C_X(\varepsilon)
\ge |M(X)|X^{-1/2-\varepsilon},
\]

which directly inherits the unknown Mertens size. Here the conclusion `(5)` is unconditional and independent of the value of `M(X)`.

The result also differs from the terminal-slab controls in `MC-045`--`MC-046`. Those construct scale-dependent multiplicative perturbations that are nearly invisible to selected one-scale or nearby-scale observables. Here the two objects are **exactly identical on every coefficient through `X`** at the square-free Möbius level, and the cost of having two distinct such arithmetic completions is detected only by comparing their global characters and invoking a short-character-sum theorem.

## 5. Prior art and novelty boundary

The decisive theorem is classical Burgess character-sum theory. Treviño, *The Burgess inequality and the least k-th power non-residue*, International Journal of Number Theory 11 (2015), no. 5, 1653–1678, DOI `10.1142/S1793042115400163`, arXiv `1412.3062`, states the standard estimate `(8)` for primitive characters and arbitrary `r` when the modulus is cubefree.

The surrounding least-character-nonresidue literature is also directly adjacent: Burgess bounds are a classical way to show that a nonprincipal character cannot remain principal-like for too long. A targeted search around least character nonresidues, pairs of characters agreeing on an initial interval, and Burgess bounds found this established mechanism but did not justify treating the pairwise formulation `(5)` as a standalone new theorem.

Accordingly, no novelty is claimed for Burgess's inequality, product/quotient characters, primitive-character conductor arithmetic, or the general principle that long initial character agreement forces large conductor. The retained Mathia contribution is only the exact specialization to the `MC-055` moving quadratic-prefix comparator frontier and the resulting multiscale falsification rule.

## 6. Boundaries and falsification tests

The conclusion is deliberately narrow.

- It requires two **distinct** exact-prefix quadratic interpolants. Reusing one character produces no nonprincipal quotient and is not constrained by `(5)`.
- It gives a lower bound on the **product** of the two conductors, not an unconditional near-quadratic lower bound for every individual interpolant.
- It does not prevent choosing one enormous conductor and reusing it over a long range of observation scales.
- It applies to the quadratic-character interpolation family of `MC-055`, not to arbitrary scale-dependent multiplicative comparators.
- It does not imply any new bound for `M(X)`, any zero-free region for zeta, or RH.
- Stronger least-nonresidue theorems may sharpen the exponent for special modulus classes, but no such sharpening is used here; `(5)` follows directly from the audited cubefree Burgess statement.

The claim is falsified if the product character in `(2)` fails to be primitive/nonprincipal under the stated distinct-prime hypotheses, or if the cubefree Burgess estimate does not apply uniformly for fixed arbitrary `r`. Both points are standard parts of the classical character theory used above.

## Consequence for the active frontier

`MC-055` showed that perfect finite-prefix agreement plus a frozen comparator's critical exponent is insufficient unless the cancellation certificate is controlled uniformly in the moving arithmetic object. The present finding narrows the multiscale escape: **distinct** exact-prefix quadratic certificates themselves cannot form a uniformly low-conductor family at a common scale.

A surviving quadratic-interpolant bootstrap must therefore exploit more than repeated finite-prefix existence. It must either control one fixed character across a sufficiently long range of scales, tolerate rapid conductor growth while proving estimates uniform enough in that growth, or introduce a relation between successive interpolants stronger than exact agreement on the already-observed Möbius prefix. Merely replacing the character whenever the observation scale increases does not remove the uniformity burden; Burgess turns that replacement into a quantitative conductor-coherence cost.