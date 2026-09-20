# PC-380 — Common-anchor chord-weighted refinement is a universal QMF shift

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the most canonical non-unimodular branch-amplitude repair left open by PC-375 and still compatible with the branch-resolved frontier of PC-379. If the source power-map transfer is weighted by the actual Euclidean chord from the common anchor, then the chord has exactly constant mean-square over every power-map fiber. After the forced normalization by `sqrt(2)`, the weighted composition operator is an isometry for every degree `m>=2`; its adjoint has the universal closed-disk spectrum. The same statement holds for the full complex chord vector `1-z`, not only its modulus, and it survives unchanged for composite degrees and arbitrary anchors. Thus the most immediate geometry-forced non-unimodular branch weight is a classical quadrature-mirror-filter/isometry mechanism, not a new Prime-Circle spectral carrier.

This does **not** classify singular inverse-chord weights, higher chord powers, conductor-dependent cyclotomic amplitudes, source-dependent domains, or genuinely matrix/nonlinear cross-level interactions. It closes the direct common-anchor chord amplitude itself on the canonical Haar/arcsine `L^2` refinement spaces.

## 1. The common-anchor chord has constant fiber energy

Work first on the original unit-circle geometry. Let

\[
\mathbb T=\{z:|z|=1\},
\qquad
(V_m f)(z)=f(z^m),
\qquad m\ge2,
\tag{1}
\]

on `L^2(T,dm_H)` with normalized Haar measure. Since the power map preserves Haar measure, `V_m` is an isometry and

\[
(V_m^*g)(z)
=\frac1m\sum_{w^m=z}g(w).
\tag{2}
\]

The geometry supplies a distinguished scalar amplitude without any external kernel: the Euclidean chord from the common anchored vertex `1`,

\[
\boxed{d(w):=|1-w|.}
\tag{3}
\]

For every `z in T`, the `m` roots of `w^m=z` satisfy

\[
\sum_{w^m=z}w=0,
\qquad
\sum_{w^m=z}\overline w=0.
\tag{4}
\]

Since

\[
d(w)^2=(1-w)(1-\overline w)=2-w-\overline w,
\]

(4) gives the exact fiber identity

\[
\boxed{
\frac1m\sum_{w^m=z}d(w)^2=2
}
\tag{5}
\]

for **every** degree `m>=2` and every base point `z`. This is stronger than an asymptotic or shell average: the root-mean-square anchored chord is exactly `sqrt(2)` on each individual refinement fiber.

The identity is also anchor-independent. For any fixed `alpha in T`,

\[
d_\alpha(w)=|\alpha-w|
\]

satisfies the same equation because

\[
d_\alpha(w)^2=2-\overline\alpha w-\alpha\overline w.
\tag{6}
\]

The common vertex therefore selects a concrete chord field, but not a special fiber-energy law unavailable to a matched regular-cover control.

## 2. The chord-weighted transfer is the adjoint of a proper isometry

Define the normalized inverse-branch transfer retaining the chord amplitude before averaging,

\[
\boxed{
(P_m^{\rm ch}f)(z)
:=\frac1m\sum_{w^m=z}d(w)f(w)
=V_m^*M_d f.
}
\tag{7}
\]

Its adjoint is

\[
(P_m^{\rm ch})^*=M_dV_m.
\tag{8}
\]

Equation (5) implies

\[
\begin{aligned}
(M_dV_m)^*(M_dV_m)
&=V_m^*M_{d^2}V_m\\
&=2I.
\end{aligned}
\tag{9}
\]

Hence

\[
\boxed{
W_m:=2^{-1/2}M_dV_m
\quad\text{is an isometry},
\qquad
2^{-1/2}P_m^{\rm ch}=W_m^*.
}
\tag{10}
\]

The isometry is proper. In the measurable branch parametrization

\[
w_j(z)=\exp\!\left(\frac{i(\arg z+2\pi j)}m\right),
\qquad 0\le j<m,
\tag{11}
\]

a function can be chosen on two branches so that, for arbitrary square-integrable `h(z)`,

\[
g(w_0(z))=d(w_1(z))h(z),
\qquad
g(w_1(z))=-d(w_0(z))h(z),
\tag{12}
\]

with `g=0` on the remaining branches. Then

\[
V_m^*M_dg=0.
\tag{13}
\]

Thus `ker W_m^*` is not merely nonzero but infinite dimensional. The Wold decomposition of an isometry therefore contains a nonzero unilateral-shift summand, and the spectrum of its adjoint is the complete closed unit disk. From (10),

\[
\boxed{
\sigma(P_m^{\rm ch})
=\sqrt2\,\overline{\mathbb D}
\qquad(m\ge2).
}
\tag{14}
\]

After the source-forced RMS normalization `1/sqrt(2)`, the complete spectrum is independent of the refinement degree.

## 3. Keeping the full complex chord vector changes nothing

Using the Euclidean magnitude in (3) discards the phase of the oriented chord. The stronger complex weight

\[
q(w):=1-w
\tag{15}
\]

retains that phase. Define

\[
Q_m:=V_m^*M_q.
\tag{16}
\]

Then

\[
Q_m^*=M_{\overline q}V_m
\]

and `|q|=d`, so the same calculation gives

\[
(Q_m^*)^*Q_m^*
=V_m^*M_{|q|^2}V_m
=2I.
\tag{17}
\]

Consequently `2^{-1/2}Q_m^*` is again a proper isometry and

\[
\boxed{
\sigma(Q_m)=\sqrt2\,\overline{\mathbb D}.
}
\tag{18}
\]

Thus the collapse is not caused by taking an absolute value. The complete complex anchored-chord vector, including its branch phase, lies in the same universal isometric class.

PC-375 proved a different statement: arbitrary **unimodular** branch phases cannot change the normalized Chebyshev-transfer disk. Equations (5)--(18) close the most immediate non-unimodular loophole: the actual geometry-forced chord magnitude is precisely normalized by its own constant fiber energy, so it also returns to a proper-isometry model.

## 4. The real-cyclotomic/Chebyshev quotient gives the same identity

The result descends exactly to the shell-2 coordinate used in PC-372--PC-379. Write

\[
\lambda=\frac{2+z+z^{-1}}4
=\frac{1+\cos\theta}{2},
\qquad
z=e^{i\theta}.
\tag{19}
\]

The anchored chord is then

\[
\boxed{
d(\lambda)=2\sqrt{1-\lambda}.}
\tag{20}
\]

Let

\[
C_m(\lambda)=\frac{1+T_m(2\lambda-1)}2
\tag{21}
\]

and let `lambda_0(x),...,lambda_{m-1}(x)` be its generic inverse images. If

\[
u_j=2\lambda_j-1,
\]

then the `u_j` are the roots of

\[
T_m(u)-(2x-1)=0.
\]

The coefficient of `u^{m-1}` in `T_m` is zero, hence

\[
\sum_{j=0}^{m-1}u_j=0,
\qquad
\boxed{
\sum_{j=0}^{m-1}\lambda_j=\frac m2.
}
\tag{22}
\]

Therefore

\[
\boxed{
\frac1m\sum_{C_m(\lambda)=x}d(\lambda)^2
=\frac4m\sum_j(1-\lambda_j)
=2.
}
\tag{23}
\]

On the invariant arcsine space of PC-374,

\[
d\mu(\lambda)=\frac{d\lambda}{\pi\sqrt{\lambda(1-\lambda)}},
\]

the Chebyshev Koopman operator is the quotient of the circle power-map operator, so (9)--(14) repeat verbatim. The non-unimodular anchored chord does not break the universal tent/Cuntz model isolated in PC-379; after RMS normalization it supplies another proper isometry.

## 5. Matched controls and why this is not a Prime-Circle discriminator

The obstruction is exact under every natural control required by the research mandate.

First, no step uses primality. Replacing a prime refinement degree `p` by any composite `m>=2` leaves (5), (10), and (14) unchanged. Second, moving the distinguished anchor from `1` to any `alpha in T` leaves the fiber energy equal to `2` by (6). Third, the same construction can be started directly from the generic circle endomorphism `z -> z^m` without primitive shells or cyclotomic polynomials at all.

Thus the architecture

\[
\text{power-map refinement}
+\text{common-anchor chord amplitude}
+\text{inverse-branch transfer}
\]

has an exact nonarithmetic model with the same normalized operator and spectral type. Highlighting only prime degrees changes which members of the family are selected, but not the mechanism carried by each weighted refinement.

This also explains why the result is stronger than observing that the first or second moment is elementary. The **complete bounded transfer operator** generated by the direct chord amplitude is already in a universal isometric class; there is no hidden discrete spectral divisor left in this canonical `L^2` realization.

## 6. Prior-art and novelty audit

The abstract mechanism is classical quadrature-mirror-filter/wavelet theory. A weight `m_0` for the covering `z -> z^m` defines an isometric weighted composition operator exactly when its squared modulus has constant normalized sum over the `m` preimages. Bratteli, Evans and Jorgensen, *Compactly supported wavelets and representations of the Cuntz relations*, **Applied and Computational Harmonic Analysis** 8 (2000), 166--196, DOI `10.1006/acha.2000.0283`, treats quadrature-mirror filters and the resulting Cuntz-isometry framework. This source is already part of the Prime-Circle prior-art boundary through PC-212.

For `m=2`, `(1-z)/sqrt(2)` is, up to the conventional phase/index normalization, the elementary Haar high-pass filter. For general `m`, the same two-tap chord polynomial is still a normalized isometric filter row because (5) is just the generalized fiber-energy/QMF condition. A complete `m`-channel filter bank would require additional orthogonal rows; PC-380 does not claim that this one chord weight by itself supplies the full bank.

The project-local contribution is therefore not a new wavelet theorem. It is the exact classification of the **specific source-forced common-anchor chord amplitude** at the current Prime-Circle frontier. PC-375 left non-unimodular amplitudes open, and PC-379 left chord amplitudes as a possible way to decorate the otherwise flat branch correspondence. Equations (5)--(18) show that the most direct such decoration lands exactly on the classical QMF/isometry surface and has a degree-independent normalized disk spectrum.

No absence-of-literature argument is needed for the negative conclusion: the explicit constant-fiber-energy identity reduces the candidate to established isometry machinery.

## 7. Boundary and research consequence

PC-380 rules out the route

\[
\boxed{
\text{common-anchor chord}
\longrightarrow
\text{linear inverse-branch amplitude}
\longrightarrow
\text{new prime-sensitive transfer spectrum}.
}
\]

The scope is intentionally sharp. It does not cover reciprocal or singular chord weights such as those classified in PC-035--PC-036; powers or nonlinear functions of the chord whose squared fiber average is not constant; amplitudes depending on the exact conductor or primitive-shell label rather than only on the geometric branch point; analytic/nuclear function spaces with a genuinely independently forced domain; or matrix-valued/nonlinear interactions between several refinement directions before scalar averaging.

The surviving branch-resolved frontier after PC-379 is therefore narrower. Merely attaching the most immediate Euclidean or complex chord from the common vertex does not provide the missing arithmetic carrier. A viable branch amplitude must retain **additional conductor/shell information or noncommuting relational structure** that cannot be reduced to the universal QMF normalization of a one-point chord observable.

## Audit / falsification tests

1. For arbitrary `z in T` and `m>=2`, enumerate the roots of `w^m=z` and verify (4)--(5).
2. Check directly that `W_m^*W_m=I` for `W_m=2^{-1/2}M_dV_m`.
3. Use the two-branch construction (12) with arbitrary `h` to verify that `ker W_m^*` is infinite dimensional.
4. Apply the Wold decomposition to recover the normalized closed-disk spectrum.
5. Repeat with the complex weight `1-z` and verify that only `|1-z|^2` enters the isometry condition.
6. In the Chebyshev quotient, verify `sum_j lambda_j=m/2` from the missing `u^{m-1}` coefficient of `T_m`, then recover (23).
7. Repeat every calculation for a composite degree and for a rotated anchor. Any prime-specific spectral distinction inside this construction would contradict the exact identities above.
