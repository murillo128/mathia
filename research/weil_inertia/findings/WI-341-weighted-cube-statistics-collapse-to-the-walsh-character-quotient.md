# WI-341 — weighted cube statistics collapse to the Walsh-character quotient

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-IDENTITY`.

**Parent findings:** WI-338, WI-339, WI-340.

WI-340 shows that deleting any geometry-defined family of injective additive cubes cannot lower the matched-energy Rademacher chaos floor in the unresolved top strip unless the retained fraction is superpolynomially small. A natural remaining repair is softer: keep most or all cubes but taper or reweight them, hoping to suppress the random floor without throwing away the geometry.

For the whole class of deterministic scalar reweightings of the same additive-cube monomial, there is an exact obstruction. The statistic only sees the **net coefficient of each unordered cube vertex set**, i.e. its Walsh character. Positive weights, and more generally weights that are sign-coherent on every equal-character class, cannot lower the renormalized random-chaos scale at all. Signed orientation/parameterization weights can lower it only by cancelling copies of the *same monomial*; such cancellation is source-blind algebraic redundancy, because it cancels for every scalar source, not specifically for the Rademacher countermodel.

Precisely, let `\mathcal C` be any deterministic family of injective additive `s`-cubes in an interval `I`, and write

\[
D:=|\mathcal C|.
\]

For `c\in\mathcal C`, let `A(c)` be its unordered set of `2^s` vertices and

\[
\chi_{A(c)}(\varepsilon)=\prod_{n\in A(c)}\varepsilon_n
\]

for independent Rademacher signs `\varepsilon_n`. Give the cubes arbitrary deterministic real weights `a_c`. For any nonzero normalization `Z`, put

\[
P_{a,Z}:=\frac1Z\sum_{c\in\mathcal C}a_c\chi_{A(c)}.
\tag{1}
\]

For each vertex set `A`, define its net coefficient

\[
T_A:=\sum_{c:\,A(c)=A}a_c.
\tag{2}
\]

Then Walsh orthogonality gives the exact quotient identity

\[
\boxed{
\|P_{a,Z}\|_2^2
=\frac1{Z^2}\sum_A T_A^2.
}
\tag{3}
\]

Thus every deterministic weighted cube statistic of the form (1) factors through the quotient

\[
c\longmapsto A(c).
\]

The oriented parameterization of a cube carries no additional information once the vertex product has been formed.

If the weights are sign-coherent inside each character class — in particular if `a_c\ge0` for every cube, or if the weight depends only on the unordered vertex set — let

\[
W:=\sum_c|a_c|,
\qquad
Q:=\sum_ca_c^2.
\]

If `m_A:=|\{c:A(c)=A\}|` and `m_A\le B`, then

\[
\boxed{
\frac{Q}{Z^2}
\le
\|P_{a,Z}\|_2^2
\le
\frac{BQ}{Z^2}.
}
\tag{4}
\]

For the natural own-mass normalization `Z=W`, define the effective cube count

\[
D_{\rm eff}:=\frac{W^2}{Q}.
\tag{5}
\]

Cauchy--Schwarz gives `D_{\rm eff}\le D`, and (4) becomes

\[
\boxed{
D_{\rm eff}^{-1/2}
\le
\|P_{a,W}\|_2
\le
\sqrt{B}\,D_{\rm eff}^{-1/2}.
}
\tag{6}
\]

In particular,

\[
\boxed{
\|P_{a,W}\|_2\ge D^{-1/2}.
}
\tag{7}
\]

So a positive taper cannot reduce the RMS chaos floor below the uniform unweighted scale. Concentrating the weight makes `D_eff` smaller and the floor larger. Deletion followed by renormalization by the retained mass is the extreme example: it cannot help even if almost all cubes are deleted.

There is an equally useful fixed-denominator formulation. If `Z=D` and

\[
\mu:=\frac1D\sum_c|a_c|,
\]

then Cauchy--Schwarz and (4) give

\[
\boxed{
\|P_{a,D}\|_2\ge\frac{\mu}{\sqrt D}.
}
\tag{8}
\]

In the WI-339/WI-340 top strip, where `s=O(\log\log N)`, `K=N^{\kappa+o(1)}`, `D=K^{s+1+o(1)}`, and

\[
R_s(K,N):=\frac{2^s\log\log N}{\log K}=s+1+O(1),
\tag{9}
\]

matching the source energy and taking the `2^{-s}` Gowers root gives a logarithmic RMS floor bounded below by

\[
\frac{\log\log N}{2}
\left(1-\frac{s+1}{R_s(K,N)}\right)
+
\frac{\log\mu}{2^s}
+o(1).
\tag{10}
\]

At (9), `2^s\asymp\log N` and the first term is `O(1)`. Consequently a positive/coherent fixed-denominator taper can force this floor to zero only if

\[
\boxed{
-\log\mu\gg2^s,
}
\tag{11}
\]

hence

\[
\boxed{
\mu=N^{-\omega(1)}.
}
\tag{12}
\]

Thus a fixed positive fraction, any polynomially small mean weight, or any smooth positive taper leaves a non-vanishing rooted random-chaos scale at the top transition. This is the weighted analogue of WI-340's deletion threshold, but (6)--(7) are stronger: if the statistic is renormalized by its own surviving mass, no amount of positive tapering lowers the floor at all.

## 1. Exact character quotient

Because every cube in `\mathcal C` is injective, its vertex product is a nonconstant Walsh character. Collecting equal characters in (1) gives

\[
ZP_{a,Z}
=
\sum_A T_A\chi_A.
\tag{13}
\]

Distinct Walsh characters are orthonormal under independent Rademacher signs, so Parseval yields (3) with no asymptotic error and no arithmetic input.

This identity is more informative than treating the individual parameterized cubes as separate terms. It says that the true degrees of freedom are the unordered vertex sets `A`, not the tuples `(x,h_1,\ldots,h_s)`. Any proposed geometry-only reweighting should therefore be audited only after the coefficients have been pushed forward to the character quotient (2).

For arbitrary signed weights one has the exact decomposition

\[
\sum_AT_A^2
=
Q
+2\sum_A\sum_{\substack{c<c'\\A(c)=A(c')}}a_ca_{c'}.
\tag{14}
\]

Hence lowering the `L^2` scale below `\sqrt Q/|Z|` requires a macroscopically negative cross term **inside equal-character classes**. In particular, achieving

\[
\sum_AT_A^2=o(Q)
\tag{15}
\]

forces

\[
\sum_A\sum_{\substack{c<c'\\A(c)=A(c')}}a_ca_{c'}
=-\frac12Q+o(Q).
\tag{16}
\]

This is the exact cancellation condition left by the weighted route.

## 2. Sign-coherent weights have the same effective-sample floor

Suppose all weights belonging to the same `A` have one sign. Then

\[
T_A^2
=\left(\sum_{c:A(c)=A}|a_c|\right)^2
\ge
\sum_{c:A(c)=A}a_c^2.
\tag{17}
\]

Summing (17) gives the lower half of (4). For the upper half, Cauchy--Schwarz inside a character class gives

\[
T_A^2
\le
m_A\sum_{c:A(c)=A}a_c^2
\le
B\sum_{c:A(c)=A}a_c^2,
\tag{18}
\]

and summing gives the upper half.

With `Z=W`, equation (6) follows immediately from `D_eff=W^2/Q`. Since

\[
W^2\le DQ,
\tag{19}
\]

one has `D_eff\le D` and therefore (7).

The multiplicity estimate from WI-338 applies unchanged to the present injective cubes:

\[
B\le
\bigl(2s(1+\log_2K)\bigr)^s
=K^{o(1)}
\tag{20}
\]

throughout the bow range. Thus the lower and upper `L^2` scales in (6) differ only by a subpower factor in the regime relevant to WI-339--WI-340. The weighted statistic has the same effective-sample-size law as an ordinary Rademacher average.

## 3. Signed orientation weights do not create source-specific cancellation

The sign-coherence hypothesis is essential. If two different parameterizations `c,c'` have the same vertex set, choosing `a_c=1` and `a_{c'}=-1` makes their contribution vanish identically. More generally, arbitrary signed weights can make `T_A` small or zero.

But this is not cancellation special to random signs. For **every** scalar source `f`, not just a Rademacher model,

\[
\prod_{n\in A(c)}f_n
=
\prod_{n\in A(c')}f_n
\qquad\text{whenever }A(c)=A(c').
\tag{21}
\]

Therefore the same pushforward coefficient `T_A` is the coefficient seen by every source. Orientation-dependent signs that cancel within one character class merely subtract duplicate copies of an identical monomial. If all `T_A` vanish, the statistic is identically zero for every source.

There is a canonical way to expose this degeneracy. After quotienting, define

\[
W_{\rm char}:=\sum_A|T_A|,
\qquad
Q_{\rm char}:=\sum_AT_A^2,
\qquad
M_{\rm eff}:=\frac{W_{\rm char}^2}{Q_{\rm char}}.
\tag{22}
\]

Whenever `W_char>0`, normalization by the actual post-cancellation mass gives exactly

\[
\boxed{
\left\|\frac1{W_{\rm char}}\sum_AT_A\chi_A\right\|_2
=M_{\rm eff}^{-1/2}
\ge |\{A:T_A\ne0\}|^{-1/2}
\ge D^{-1/2}.
}
\tag{23}
\]

Thus arbitrary signed scalar weights do not manufacture a lower-noise statistic after honest renormalization; they can only reduce the net character mass appearing in the denominator if one insists on keeping the original pre-cancellation normalization. Such a reduction is algebraic attenuation of the statistic itself, not evidence of the source-specific off-diagonal cancellation required by the bow clue.

This does not rule out a genuinely different observable. A statistic that couples adjacent derivative orders, inserts source/carrier information before the scalar vertex product is collapsed, or controls the actual signed two-point covariance may expose structure absent from (1). The finding only closes reweightings that remain linear combinations of the same scalar additive-cube monomials.

## 4. Consequence for the accepted bow clue

WI-340 left three broad possibilities in the bounded top strip: modify/cancel a positive-density family of generic cube monomials, couple orders, or retain source/carrier-specific signed covariance. Equations (3), (16), and (23) sharpen the first option.

A **soft positive taper is not a new escape**. Nor is a signed reweighting that depends only on the unordered vertex set. Orientation-dependent signed weights can cancel parameterization duplicates, but after the exact character quotient this either attenuates the same monomial for every source or disappears entirely. Therefore a useful continuation cannot obtain its gain merely from scalar geometry-only weights on the existing cube product.

The surviving generic route must change the observable after the character quotient: for example by coupling adjacent derivative orders or by keeping a source/carrier-specific signed correlation that is not represented by a single scalar coefficient `T_A` on each vertex product. This matches the original pointwise WI-195 requirement more closely than another Gowers-style reweighting.

## 5. Prior-art and novelty audit

The mathematical ingredients are classical. Walsh characters of independent Rademacher signs are orthonormal, so (3) is Parseval after collecting identical monomials. Equations (4), (6), (8), and (23) are Cauchy--Schwarz consequences. Bonami--Beckner hypercontractivity, used in WI-338--WI-340 to turn the corresponding `L^2` scales into simultaneous random-model concentration, is classical Rademacher-chaos technology. Modern work on moments of Rademacher chaoses and on weighted Gowers-type quantities confirms that weighted chaos/norm formulations are standard objects; none of that literature is needed for the exact identities above.

The external prior-art audit did not locate a source stating this particular bow-line conclusion: that deterministic scalar cube reweightings factor through the equal-vertex-set quotient and that positive/coherent reweighting cannot lower the renormalized top-strip chaos floor. No priority claim is made. The new content here is the line-specific deduction and the resulting no-go classification relative to WI-339--WI-340.

## 6. Evidence boundary and falsification

This is an exact random-model obstruction, not a theorem about the primes. It does not show that the arithmetic source behaves like independent Rademacher signs, nor does it rule out a statistic that uses information unavailable to the model. It also does not rule out a signed coefficient system under a deliberately fixed pre-cancellation denominator; it says precisely that any reduction then comes from shrinking the net character coefficients `T_A`, and that the same cancellation occurs for every scalar source.

A counterexample to the main no-go would require a deterministic scalar weighting of the same injective cube monomials, normalized by its actual post-cancellation mass, whose Rademacher `L^2` norm is `o(D^{-1/2})`. Equation (23) rules this out exactly. A genuine continuation must therefore leave this scalar character-quotient interface rather than refine its taper.

## Lineage

`WI-338 -> WI-339 -> WI-340 -> WI-341`.

- WI-338 identifies the Walsh expansion and subpower character multiplicity.
- WI-339 removes the zero-increment constant sector and moves the random transition to `R_s=s+1`.
- WI-340 shows that sparse deletion of generic injective cubes cannot lower the top-strip chaos floor without superpolynomial mass loss.
- WI-341 shows that soft positive/coherent weighting has the same obstruction, and that arbitrary signed scalar weighting acts only through the exact Walsh-character quotient; parameterization-level cancellation is source-blind.