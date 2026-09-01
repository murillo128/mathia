# WP-087 — Positive cover-angle reference mixtures violate dyadic log-degree scaling

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + POSITIVE-ENSEMBLE + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-085` and `WP-086` isolate a genuinely positive but singular logarithmic response in the noncommuting pointed-cover geometry. For cover degrees `m,n`, let

\[
P_k=W_kW_k^*,
\qquad
\Delta_{m,n}:=P_m(I-P_n)P_m\big|_{\operatorname{Ran}P_m},
\]

on one `lcm(m,n)` cell, and let

\[
L_{m,n}:=(-\log)'\Delta_{m,n}\succeq0
\]

be the reduced pseudolog: it is `-log x` on the positive spectrum of `Delta` and zero on its exact kernel. Then

\[
F(m,n):=\operatorname{Tr}L_{m,n}
=-\log\det{}'\Delta_{m,n}\ge0.
\]

`WP-085` gives the exact formula

\[
\boxed{
F(m,n)
= -\log\left(
\frac{((a-1)!)^2}{a^{a-2}b^{a-1}}
\right),
}
\tag{1}
\]

where

\[
g=(m,n),\qquad
a=\min(m/g,n/g),\qquad b=\max(m/g,n/g).
\]

A natural attempt to remove the reference-cover dependence of a single `F(m,n)` is to combine many positive reference sectors with fixed nonnegative weights. That entire additive repair already fails on the first dyadic prime ray.

Let `w_m >= 0`, `m>=2`, be any fixed finite or countable family of weights for which the two responses below are finite, and define

\[
\boxed{
G_w(n):=\sum_{m\ge2}w_mF(m,n).
}
\tag{2}
\]

Equivalently, whenever the direct sum is trace class,

\[
\mathcal L_{w,n}:=\bigoplus_{m\ge2}w_mL_{m,n}\succeq0,
\qquad
\operatorname{Tr}\mathcal L_{w,n}=G_w(n).
\tag{3}
\]

Then

\[
\boxed{
G_w(2)>0
\quad\Longrightarrow\quad
G_w(4)>2G_w(2).
}
\tag{4}
\]

But exact logarithmic degree would require

\[
\log4=2\log2.
\]

Therefore **no fixed positive additive mixture of the cover-angle pseudolog responses can reproduce `log n` for all degrees**. By Möbius inversion, it cannot have exact primitive `Lambda(n)` either. This is stronger than the finite-reference common-multiple blind spot: it applies to arbitrary countable nonnegative reference ensembles, without a moment assumption, as soon as the responses at degrees `2` and `4` are finite.

The obstruction is completely local and exact. It does not use zeta zeros, analytic continuation, the functional equation, or an archimedean model. The failure occurs before the construction reaches the global Weil assembly.

## 1. The dyadic reference response has an exact parity split

For `n=2`, equation (1) gives an especially simple result.

If `m` is even, then `(m,2)=2`, so one reduced degree is `1`. The two block partitions are nested after gcd reduction and

\[
\boxed{F(m,2)=0\qquad(m\text{ even}).}
\tag{5}
\]

If `m` is odd, then the reduced pair is `(2,m)` and `WP-085` gives

\[
\boxed{F(m,2)=\log m\qquad(m\text{ odd}).}
\tag{6}
\]

Consequently

\[
G_w(2)=\sum_{m\text{ odd}}w_m\log m.
\tag{7}
\]

Thus any positive reference ensemble capable of producing the required nonzero degree-two mass must assign positive weight to at least one odd reference degree.

## 2. Every odd reference overproduces degree four relative to degree two

Now evaluate the same reference at `n=4`.

For odd `m>=3`, gcd reduction is trivial. If `m=3`, equation (1) with `(a,b)=(3,4)` gives

\[
F(3,4)=\log12.
\]

If `m>=5`, equation (1) with `(a,b)=(4,m)` gives

\[
F(m,4)
=-\log\left(\frac{(3!)^2}{4^2m^3}\right)
=\log\left(\frac{4m^3}{9}\right).
\]

The same closed form also holds at `m=3`, since `4\cdot3^3/9=12`. Hence for every odd `m>=3`,

\[
\boxed{
F(m,4)=3\log m+\log\frac49.
}
\tag{8}
\]

Combining (6) and (8),

\[
\boxed{
F(m,4)-2F(m,2)
=\log\frac{4m}{9}>0
\qquad(m\text{ odd},\ m>=3).
}
\tag{9}
\]

For even `m`, equation (5) gives `F(m,2)=0`, while positivity of `L_{m,4}` gives

\[
F(m,4)-2F(m,2)=F(m,4)\ge0.
\tag{10}
\]

Thus every reference sector obeys the non-strict inequality

\[
F(m,4)\ge2F(m,2),
\tag{11}
\]

and every sector that contributes at degree `2` obeys it strictly.

## 3. Positive mixing cannot cancel the strict excess

Multiply (11) by arbitrary fixed `w_m>=0` and sum. Monotone convergence gives

\[
G_w(4)-2G_w(2)
=\sum_{m\ge2}w_m\bigl(F(m,4)-2F(m,2)\bigr)
\ge0.
\tag{12}
\]

If `G_w(2)>0`, equation (7) implies that at least one odd `m` has `w_m>0`. Its summand in (12) is strictly positive by (9), so

\[
\boxed{G_w(4)-2G_w(2)>0.}
\tag{13}
\]

No normalization of the total positive mass changes this conclusion. Multiplying all weights by one positive constant scales both sides, while any degree-independent positive reweighting is already included in the arbitrary family `{w_m}`.

If the countable sum at degree `4` diverges, the construction already fails to produce the finite target `log4`; if it is finite, (13) is the exact obstruction. No summability hypothesis beyond finiteness of the two target responses is needed.

This closes the additive positive-ensemble repair

```text
many reference covers
+ positive principal-angle pseudolog in each reference sector
+ fixed nonnegative mixing
    -> reference-free log degree.
```

## 4. Exact Mangoldt primitivization fails already between `2` and `4`

The relevance to the finite Weil coefficient is immediate and does not require examining all integers.

For any arithmetic preprimitive `G` with `G(1)=0`, define its divisor-Möbius primitive

\[
M_G(n):=\sum_{d\mid n}\mu(d)G(n/d).
\tag{14}
\]

At the first two powers of `2`,

\[
M_G(2)=G(2),
\qquad
M_G(4)=G(4)-G(2).
\tag{15}
\]

Exact von Mangoldt support would require

\[
M_G(2)=M_G(4)=\log2.
\tag{16}
\]

Equations (15)--(16) force

\[
G(2)=\log2,
\qquad
G(4)=2\log2=\log4.
\tag{17}
\]

But any positive cover-angle mixture with `G_w(2)=log2` satisfies, by (13),

\[
G_w(4)>2\log2,
\]

and therefore

\[
\boxed{
M_{G_w}(4)>M_{G_w}(2).
}
\tag{18}
\]

So the positive multireference repair cannot even keep the required constant `log 2` weight along the first two points of one prime-power ray. The failure precedes the critical attenuation `n^{-1/2}` and hence cannot be repaired by multiplying both prime-ray masses by the same externally imposed Weil factor afterward.

Equivalently, the elementary identity

\[
\log n=\sum_{d\mid n}\Lambda(d)
\]

shows globally that exact Möbius primitive `Lambda` is equivalent to preprimitive `log n`; (13) already rules this out at the smallest nontrivial divisibility test.

## 5. Operator meaning: positivity itself prevents reference averaging from repairing the bias

Each `L_{m,n}` is positive because the spectrum of `Delta_{m,n}` lies in `[0,1]` and the reduced pseudolog is nonnegative on that spectrum. A nonnegative direct sum or scalar mixture therefore preserves a genuine Hilbert-space positivity theorem.

The obstruction is not that positivity disappears under mixing. It is the opposite: **because the reference sectors are combined positively, their dyadic excess cannot cancel**. Every odd reference needed to see degree `2` contributes too much at degree `4`, while even references can only add further nonnegative degree-four mass.

This makes the escape boundary sharper than in `WP-085`--`WP-086`:

- one fixed reference is blind on its nested divisibility classes;
- bounded continuous two-projection calculus has the wrong scale (`WP-086`);
- the singular pseudolog restores logarithmic response for individual nonnested pairs;
- but averaging any number of those singular positive responses with fixed nonnegative weights violates the required dyadic logarithmic scaling.

The issue is therefore not removable by choosing a larger positive reference dictionary and averaging its scalar or direct-sum responses.

## 6. Matched controls and scope boundary

The proof uses only the exact block-cover projections and integer divisibility. Primality plays no role in (5)--(13). The same obstruction occurs in a matched integer-degree cover system with no zeta function attached. It is therefore a geometric constraint of this reference-ensemble construction, not hidden evidence for RH.

Several escapes remain outside the claim and must not be conflated with it:

1. **Signed reference coefficients.** They can cancel the positive excess in (13), but then the direct-sum/reference combination is no longer positive by construction. Any surviving sign theorem would have to come from additional geometry rather than from positive mixing.
2. **Degree-dependent weights `w_m(n)`.** They can be tuned separately at `2` and `4`; that abandons a fixed intrinsic reference geometry and is exactly the kind of hand-picked arithmetic normalization the Weil-positivity mandate excludes unless another Mathia structure forces it canonically.
3. **Genuinely nonseparable multi-projection coupling.** An operator formed from several `P_m` simultaneously, with cross-reference terms before taking principal angles/pseudologs, is not a positive mixture of the pairwise `L_{m,n}` and is not ruled out here.
4. **Nonperiodic or global boundary coupling.** The argument is per finite lcm cell, inheriting the periodic block-cover setup of `WP-085`; a nonperiodic global response remains outside the theorem.
5. **A finite--archimedean object formed before scalarization.** Nothing here rules out a single global operator in which the archimedean sector changes the finite reference geometry before the sign theorem is applied. The result shows only that an archimedean correction cannot rescue this particular additive finite response after it has already failed exact Mangoldt scaling.

The third and fifth items are now the relevant forms of the multireference escape. Merely adding more independently positive pairwise reference sectors is not.

## 7. Prior-art and novelty audit

The underlying operator ingredients are classical and are already classicalized in `WP-086`: Halmos' two-subspaces decomposition and the standard `C*`-algebra/functional calculus of two projections explain the principal-angle blocks. Principal-angle determinant and Grassmannian/Binet--Cauchy type constructions are also standard geometry. No novelty is claimed for reduced determinants, principal angles, logarithmic spectral functions, positive direct sums, or Möbius inversion.

A directed audit of principal-angle log-determinant distances, Grassmannian determinant kernels, and two-projection functional calculus found no external theorem needed for (5)--(13). The durable content here is the **Mathia-specific arithmetic specialization** of the exact `WP-085` determinant formula and the resulting dyadic inequality that kills positive reference averaging. It should be regarded as a derived obstruction inside the Mathia cover model, not as a claim of a new general theorem about Grassmannians.

The result is also distinct from the failure of `F(m,n)` to be a PSD scalar kernel established in `WP-085`. That earlier failure concerns quadratic assembly over degree variables. The present theorem assumes only termwise nonnegative reference weights and shows that even this much weaker positive scalar/direct-sum averaging cannot reproduce the required additive logarithmic degree.

## 8. Exact falsification surface

The finding is falsified if any of the following fails under the `WP-085` normalization:

1. for every even `m`, `F(m,2)=0`;
2. for every odd `m>=3`, `F(m,2)=log m`;
3. for every odd `m>=3`, `F(m,4)=log(4m^3/9)`;
4. therefore `F(m,4)-2F(m,2)=log(4m/9)>0` on every reference sector that contributes at degree `2`;
5. a nonnegative fixed mixture with finite degree-two and degree-four responses can violate the implication `G_w(2)>0 => G_w(4)>2G_w(2)`;
6. exact Möbius primitive `Lambda` does not force `G(2)=log2` and `G(4)=log4`.

All six tests are finite or elementary consequences of the exact determinant formula (1). No numerical evidence is load-bearing.

## Research consequence

The singular cover-angle response of `WP-085`--`WP-086` cannot be made reference-independent by a positive dictionary average. The first prime ray already forces the incompatible inequality

\[
\boxed{
G_w(4)>2G_w(2)
\quad\text{whenever}\quad
G_w(2)>0,
}
\]

whereas the required preprimitive obeys exact equality.

A viable continuation must therefore introduce **cross-reference interaction before pairwise scalarization**, a nonperiodic/global quotient, or a genuinely nonseparable finite--archimedean construction with its own independent sign theorem. Positive averaging of independently constructed principal-angle pseudolog sectors is closed.