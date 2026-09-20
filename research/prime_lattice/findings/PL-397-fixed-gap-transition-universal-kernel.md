# PL-397 — Fixed-gap saddle-transition scaling is universal and factorization-blind at leading order

**Evidence/status:** `CLASSICAL-UNIFORM-ASYMPTOTICS+EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION`.

**Parent finding:** `PL-396`.

## Claim

`PL-396` reopened fixed additive-gap pairs `q=r+d` after replacing the hard Riemann–Siegel cutoff by the continuation-faithful incomplete-gamma smoothing. The surviving local layer is real, but its leading uniform scaling does **not** contain a prime-factorization observable.

Fix an integer `d>0`, put

\[
q=r+d,
\qquad
T_r=2\pi r(r+d)=2\pi qr,
\qquad
t=T_r+r u,
\]

with `u` in a fixed compact set as `r -> infinity`. Let

\[
Q_n(t)=Q\!\left(\frac{s}{2},\pi i n^2\right),
\qquad
s=\frac12+it,
\]

be the exact Paris–Cang continuation weight, and let

\[
\Phi_{q,r}(t)=2\vartheta(t)-t\log(qr)
\]

be the cross-channel phase isolated in `PL-394`--`PL-396`. Then, uniformly for bounded `u`,

\[
Q_q(T_r+r u)
=
\frac12\operatorname{erfc}\!\left[
\sqrt{\frac{\pi i}{2}}
\left(d-\frac{u}{2\pi}\right)
\right]
+O(r^{-1}),
\tag{1}
\]

\[
Q_r(T_r+r u)
=
\frac12\operatorname{erfc}\!\left[
-\sqrt{\frac{\pi i}{2}}
\left(d+\frac{u}{2\pi}\right)
\right]
+O(r^{-1}),
\tag{2}
\]

and

\[
e^{i\Phi_{q,r}(T_r+r u)}
=
e^{-i\pi/4}
\exp\!\left(\frac{i u^2}{4\pi}\right)
\{1+O(r^{-1})\}.
\tag{3}
\]

Thus the normalized local data

\[
\bigl(Q_q,Q_r,e^{i\Phi_{q,r}}\bigr)
\]

converge to a kernel depending only on the **additive gap** `d`, the scaled local coordinate `u`, and archimedean constants. At leading order it does not depend on the exponent vectors `v(r)` and `v(r+d)` separately, their support, or their prime-factorization relation.

Here “factorization-blind” is deliberately narrow: `r` and `q` of course determine their factorizations. The statement is that the local asymptotic mechanism uses only the scalar integer labels/energies already present in the one-dimensional zeta representation and introduces no operation on prime-exponent coordinates. It therefore fails the line's matched-control test for a genuinely prime-lattice mechanism.

## 1. The incomplete-gamma transition has a universal fixed-gap limit

The exact representation used in `PL-396` contains

\[
Q\!\left(a,z\right),
\qquad
a=\frac{s}{2},
\qquad
z=\pi i n^2,
\qquad
\lambda_n=\frac{z}{a}=\frac{2\pi i n^2}{s}.
\]

The standard uniform incomplete-gamma expansion is

\[
Q(a,z)
=
\frac12\operatorname{erfc}\!\left(\eta\sqrt{a/2}\right)
+O(|a|^{-1/2}),
\tag{4}
\]

through the transition, with

\[
\frac12\eta^2=\lambda-1-\log\lambda,
\qquad
\eta\sim\lambda-1
\quad(\lambda\to1).
\tag{5}
\]

For `t=T_r+r u`, elementary expansion gives

\[
\lambda_r
=
1-\frac{d+u/(2\pi)}{r}+O(r^{-2}),
\tag{6}
\]

and

\[
\lambda_q
=
1+\frac{d-u/(2\pi)}{r}+O(r^{-2}).
\tag{7}
\]

The small imaginary correction caused by the `1/2` in `s=1/2+it` is `O(r^{-2})`. Since `eta=lambda-1+O((lambda-1)^2)` and

\[
\sqrt{a/2}
=
\frac12\sqrt{s}
=
r\sqrt{\frac{\pi i}{2}}\{1+O(r^{-1})\},
\]

(6)--(7) inserted into (4) give (1)--(2). The correction is `O(r^{-1})` because `|a|^{1/2} asymp r` and the uniform coefficient in the incomplete-gamma expansion is regular at `eta=0`.

This extends the `u=0` calculation already stored in `PL-396`. The important extra fact is that the **entire order-one transition profile on the natural `O(r)` time scale** has a fixed limiting shape. Moving along the saddle/transition layer does not expose hidden prime-coordinate information at leading order.

## 2. The stationary phase simultaneously becomes a universal Fresnel factor

The classical Riemann–Siegel phase has

\[
2\vartheta(t)
=
t\log\frac{t}{2\pi}-t-\frac{\pi}{4}
+\frac{1}{24t}+O(t^{-3}).
\tag{8}
\]

At `T_r=2 pi qr`,

\[
\Phi_{q,r}(T_r)
=
-T_r-\frac{\pi}{4}+O(T_r^{-1}).
\]

Because `qr` is an integer,

\[
e^{-iT_r}=e^{-2\pi i qr}=1.
\tag{9}
\]

Moreover,

\[
\Phi'_{q,r}(T_r)=O(T_r^{-2}),
\qquad
\Phi''_{q,r}(T_r)=\frac1{T_r}+O(T_r^{-3}).
\]

Taylor expansion with `t-T_r=r u` therefore yields

\[
\Phi_{q,r}(T_r+r u)
=
-T_r-\frac{\pi}{4}
+\frac{u^2}{4\pi}
+O(r^{-1}),
\tag{10}
\]

uniformly for bounded `u`; the cubic term is `O(r^{-1})`. Equations (9)--(10) give (3).

The phase therefore loses even the scalar center `r` at leading normalized order. Its surviving structure is the standard quadratic/Fresnel stationary-phase kernel. The integrality in (9) is genuine arithmetic input, but it is input from the ordinary integer labels `q,r`; it does not use their decomposition into prime-coordinate vectors.

## 3. Matched-control interpretation

Combining (1)--(3), any continuous local observable built only from the two Paris–Cang transition weights and the cross-phase has, after removing elementary scalar prefactors such as `(qr)^(-1/2)`, a leading limit of the form

\[
\mathcal K_d(u)
=
F\!\left(
\operatorname{erfc}(c[d-u/(2\pi)]),
\operatorname{erfc}(-c[d+u/(2\pi)]),
 e^{-i\pi/4}e^{iu^2/(4\pi)}
\right),
\qquad
c=\sqrt{\frac{\pi i}{2}},
\tag{11}
\]

for the corresponding continuous function `F`. There is no appearance of `v(r)`, `v(r+d)`, gcd/lcm data, Möbius or von-Mangoldt weights, or a prime-coordinate operator.

In exponent coordinates the pair satisfies

\[
\left\langle v(r+d)-v(r),(\log p)_p\right\rangle
=
\log\left(1+\frac d r\right)
=\frac d r+O(r^{-2}),
\]

but (1)--(3) only use this **scalar projection**. Two fixed-gap pairs with radically different factorization patterns have the same limiting local kernel for the same `d`. This is exactly the sort of universal analytic behavior that the line's canonical README requires to be separated from an independent arithmetic input.

The surviving channel of `PL-396` is therefore best viewed as an **additive near-diagonal boundary layer**. To become relevant to the prime-exponent program it would need an additional signed correlation or operator that depends nontrivially on `v(r)` and `v(r+d)` and survives averaging against `K_d(u)`. The universal saddle/transition kernel itself cannot supply that distinction.

## 4. Continuation status

No Euler-product identity is transported into the critical strip here. Equations (1)--(2) start from the exact absolutely convergent Paris–Cang representation, whose normalized incomplete-gamma factor implements analytic continuation on the critical line. Equation (3) uses the completed Riemann–Siegel phase coming from the gamma factor. The derivation is therefore continuation-faithful in the same sense as `PL-396`.

The result is nevertheless only a **local asymptotic statement** for fixed `d` and bounded `u`. It does not classify the sum over all near-diagonal pairs, and it does not assert that subleading terms or an independently inserted arithmetic weight are irrelevant.

## 5. Prior-art and novelty audit

No theorem-level novelty in incomplete-gamma or Riemann–Siegel asymptotics is claimed. Paris–Cang's exact representation and Paris's 2022 revisit already supply the smooth complementary-error-function transition; DLMF §8.12 gives the uniform `Q(a,z)` expansion and its transition variable, while the Riemann–Siegel theta expansion is classical.

The fixed-gap scaling (1)--(3) is an elementary line-specific consequence of those formulas evaluated in the `q=r+d`, `t=2 pi qr+O(r)` regime isolated by `PL-394`--`PL-396`. Targeted searches for combinations of “fixed gap/fixed difference”, “near diagonal”, “Riemann–Siegel”, “incomplete gamma”, and “coalescing saddle/transition” did not identify a source that assigns a prime-factorization invariant to this local kernel. The stored conclusion is therefore a **route restriction**, not a novelty claim: the classical continuation kernel that rescues the fixed-gap pairs is universal at leading scale and by itself does not satisfy the prime-lattice mandate.

### Sources

1. R. B. Paris and S. Cang, “An asymptotic representation for `zeta(1/2+it)`,” *Methods and Applications of Analysis* **4**(4) (1997), 449--470. Full text: https://intlpress.com/site/pub/files/_fulltext/journals/maa/1997/0004/0004/MAA-1997-0004-0004-a006.pdf.
2. R. B. Paris, “An asymptotic approximation for the Riemann zeta function revisited,” arXiv:2203.07863v2 (2022). https://arxiv.org/abs/2203.07863.
3. NIST Digital Library of Mathematical Functions, §8.12, “Uniform Asymptotic Expansions for Large Parameter,” especially equations 8.12.1--8.12.4: https://dlmf.nist.gov/8.12.
4. NIST Digital Library of Mathematical Functions, §25.9 and §25.10, asymptotic and Riemann–Siegel formulas for the Riemann zeta function: https://dlmf.nist.gov/25.9 and https://dlmf.nist.gov/25.10.

## 6. Adversarial boundaries and falsification tests

1. **Do not read “factorization-blind” as non-injectivity of `log n`.** The map `n -> log n` is injective, so the scalar label determines `n` and hence its factorization. The point is structural: the local kernel contains no operation that distinguishes prime-coordinate geometry from the same scalar spectrum treated as unlabeled integer modes.

2. **The result is leading-order and local.** Corrections of order `1/r`, a wider gap regime, summation over `d`, or coupling to an arithmetic weight can change the conclusion. They must be derived rather than inferred from (1)--(3).

3. **A nonzero local kernel is not an RH mechanism.** Even if the completed pair contribution is nonzero, no sign, positivity, zero-location constraint, trace identity, or cancellation theorem follows from the universal profile.

4. **The pair kernel is representation-derived, not yet invariant.** `PL-396` already requires comparison among exact continuation-faithful representations. The present result says that within the Paris–Cang chart the natural local scaling is universal; it does not prove that every exact decomposition has the identical pairwise kernel.

5. **Decisive escape condition.** This route restriction would be overcome by deriving, from a declared arithmetic operation, a factor-sensitive coefficient `A(r,r+d)` or operator coupling for which the weighted near-diagonal sum

\[
\sum_{r,d} A(r,r+d)\,\mathcal K_d(u)
\]

has an independently controlled signed/positive structure tied to the zeta zero divisor or to an RH-equivalent criterion. Merely rewriting `r` and `r+d` as exponent vectors does not meet this condition.

## Research consequence

`PL-396` correctly shows that analytic smoothing prevents the hard cutoff from deleting fixed-gap off-diagonal pairs. `PL-397` shows what that rescue actually gives at the natural local scale: a universal error-function/Fresnel kernel indexed by the **additive gap** `d`.

For `prime_lattice`, this redirects the next step away from further analysis of the bare transition kernel. A viable continuation-aware mechanism must add an arithmetic coupling that sees more than `log n`—for example a Möbius/von-Mangoldt, gcd/lcm, divisor-incidence, or other exponent-coordinate observable—and must prove that its interaction with the universal boundary-layer kernel produces cancellation or rigidity not shared by a matched scalar-frequency model.