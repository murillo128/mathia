# PC-381 — Fixed finite-bandwidth refinement weights collapse to universal QMF

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE`. This extends PC-380 from the first anchored chord weight to every fixed scalar refinement weight whose squared modulus has finite Fourier bandwidth. Once the refinement degree exceeds that bandwidth, the power-map fiber average removes every nonconstant Fourier mode exactly, so the weighted composition operator is a scalar multiple of a proper isometry and its adjoint has the universal closed-disk spectrum. In particular, every fixed positive integer power of the common-anchor chord `|1-z|^r` eventually collapses in exactly this way for both prime and composite refinement degrees. Thus increasing a fixed positive chord power cannot by itself produce a prime-sensitive or RH-sensitive spectral mechanism.

This does **not** cover singular inverse-chord kernels with infinite Fourier tails, conductor-dependent weights whose bandwidth grows with the refinement degree, nonlinear/tensor weights, or genuinely cross-level nonseparable operators. Those remain outside this no-go.

## 1. Exact fiber-average identity

Work on the original unit-circle refinement geometry with normalized Haar measure. Let

\[
(V_m f)(z)=f(z^m),\qquad m\ge2,
\tag{1}
\]

and let `q` be a bounded scalar weight. Define

\[
S_{m,q}:=M_qV_m.
\tag{2}
\]

The adjoint of the power-map is the exact fiber average

\[
(V_m^*g)(z)=\frac1m\sum_{w^m=z}g(w).
\tag{3}
\]

It is convenient to denote this conditional expectation by

\[
(E_mg)(z):=\frac1m\sum_{w^m=z}g(w).
\tag{4}
\]

Then, without approximation,

\[
\boxed{
S_{m,q}^*S_{m,q}
=V_m^*M_{|q|^2}V_m
=M_{E_m(|q|^2)}.
}
\tag{5}
\]

Thus all scalar weighted-refinement norm information is controlled by which Fourier modes of `|q|^2` survive averaging over an `m`-point root fiber.

If

\[
g(z)=\sum_{k\in\mathbb Z}\widehat g(k)z^k,
\]

then roots-of-unity orthogonality gives

\[
\boxed{
E_mg(z)=\sum_{\ell\in\mathbb Z}\widehat g(m\ell)z^\ell.
}
\tag{6}
\]

The power-map fiber therefore acts as an exact Fourier aliasing selector: it keeps only frequencies divisible by `m` and rescales them by a factor `m` in frequency.

## 2. Finite-bandwidth weights become exactly universal

Assume that `|q|^2` has finite Fourier support,

\[
\widehat{|q|^2}(k)=0\qquad(|k|>D).
\tag{7}
\]

For every integer `m>D`, equation (6) leaves only the zero mode. Hence

\[
\boxed{
E_m(|q|^2)=\widehat{|q|^2}(0)=\|q\|_2^2,
}
\tag{8}
\]

and therefore

\[
\boxed{
S_{m,q}^*S_{m,q}=\|q\|_2^2 I
\qquad(m>D).
}
\tag{9}
\]

For nonzero `q`, the normalized operator

\[
W_{m,q}:=\|q\|_2^{-1}S_{m,q}
\tag{10}
\]

is an isometry for every refinement degree beyond the fixed bandwidth.

A particularly transparent sufficient condition is that `q` itself be a Laurent polynomial,

\[
q(z)=\sum_{j=A}^{B}c_jz^j.
\tag{11}
\]

Then `|q|^2` has Fourier bandwidth at most

\[
D=B-A,
\tag{12}
\]

so every `m>B-A` lies in the universal regime. No number-theoretic property of `m` enters the proof.

For the finitely many exceptional values `m<=D`, equation (6) is still exact:

\[
E_m(|q|^2)
=\sum_{|\ell|\le D/m}
\widehat{|q|^2}(m\ell)z^\ell.
\tag{13}
\]

Any residual dependence is therefore only the elementary divisibility condition that `m` divide a Fourier offset present in a fixed finite mask. Such a fixed mask cannot distinguish primes from composites at arbitrarily large conductor.

## 3. The normalized operator is a proper isometry

The isometry in (10) is not unitary when `m>=2`. This can be seen fiberwise without imposing any special Fourier support on vectors in the Hilbert space. For almost every base point `z`, the fiber `w^m=z` contains `m` points. The adjoint

\[
(S_{m,q}^*h)(z)
=\frac1m\sum_{w^m=z}\overline{q(w)}h(w)
\tag{14}
\]

is one scalar weighted linear functional on the `m` fiber values. Whenever the weight is nonzero on at least one branch, that functional has an `(m-1)`-dimensional orthogonal complement on the fiber; a measurable nonzero section of these complements gives a nonzero element of `ker S_{m,q}^*`.

Thus `W_{m,q}` has a nonzero unilateral-shift component in its Wold decomposition. Since an isometry has norm one and the adjoint of a nontrivial unilateral shift has the whole closed unit disk as spectrum,

\[
\boxed{
\sigma(W_{m,q}^*)=\overline{\mathbb D}
\qquad(m>D).
}
\tag{15}
\]

Equivalently,

\[
\boxed{
\sigma(S_{m,q}^*)
=\|q\|_2\,\overline{\mathbb D}
\qquad(m>D).
}
\tag{16}
\]

So after the weight's own RMS normalization, not merely the norm but the complete adjoint spectrum becomes independent of the refinement degree.

## 4. Every fixed positive integer anchored-chord power collapses

PC-380 treated the geometrically most immediate common-anchor weight `q_1(z)=1-z`, whose squared modulus has bandwidth one. The same mechanism can be evaluated exactly for every fixed positive integer power

\[
q_r(z):=(1-z)^r,
\qquad r\ge1.
\tag{17}
\]

On the unit circle,

\[
|q_r(z)|^2=|1-z|^{2r}
=(-1)^r z^{-r}(1-z)^{2r},
\tag{18}
\]

so

\[
\boxed{
|1-z|^{2r}
=\sum_{k=-r}^{r}
(-1)^k\binom{2r}{r+k}z^k.
}
\tag{19}
\]

Its Fourier bandwidth is exactly `r`, and the constant coefficient is

\[
\widehat{|1-z|^{2r}}(0)=\binom{2r}{r}.
\tag{20}
\]

Therefore for every refinement degree `m>r`,

\[
\boxed{
E_m(|1-w|^{2r})=\binom{2r}{r},
}
\tag{21}
\]

and

\[
\boxed{
S_{m,r}^*S_{m,r}=\binom{2r}{r}I,
\qquad
S_{m,r}:=M_{(1-z)^r}V_m.
}
\tag{22}
\]

After normalization by `sqrt(binomial(2r,r))`, `S_{m,r}` is a proper isometry and

\[
\boxed{
\sigma(S_{m,r}^*)
=\sqrt{\binom{2r}{r}}\,\overline{\mathbb D}
\qquad(m>r).
}
\tag{23}
\]

This gives the promised prime/composite control. For every fixed `r`, all sufficiently large primes and all sufficiently large composites have **exactly the same normalized spectral disk**. The collapse is not asymptotic and does not depend on the factorization of `m`.

The modulus-only weight `|1-z|^r` has the same squared modulus and therefore the same conclusion. Hence retaining or discarding the oriented chord phase does not rescue fixed positive chord powers.

## 5. What the exceptional low degrees can and cannot contain

When `2<=m<=r`, nonzero modes at frequencies `m,2m,...` can survive (6). For the anchored chord power they are explicitly the binomial coefficients in (19). This can make the finite list of low-degree operators differ from one another, but the dependence is completely exhausted by the Fourier aliases selected by divisibility of the fixed mode indices.

That finite exception set cannot support a refinement-scale prime discriminator: after `m>r` there is no remaining degree dependence at all after RMS normalization. Allowing a larger but still fixed finite-bandwidth trigonometric weight only replaces `r` by its bandwidth `D` and leads to the same conclusion.

This is materially stronger than checking a few powers individually. It rules out the entire class of fixed scalar finite-Fourier-bandwidth repairs to the canonical power-map transfer.

## 6. Prior-art and novelty audit

The abstract mechanism in (5)--(10) is classical weighted-composition/QMF theory. Fiber averaging under finite covering maps, Fourier/polyphase aliasing, and the isometry condition obtained from constant fiber energy are standard parts of wavelet/filter-bank and Cuntz-representation theory. PC-380 already anchors this literature through the Dutkay--Jorgensen QMF/transfer-operator sources, and PC-212 records the earlier Prime-Circle classicalization into the same filter-bank/Cuntz setting.

The present result therefore makes **no novelty claim for the operator-theoretic mechanism**. The project-specific contribution is the exact no-go obtained by applying that classical fiber/Fourier structure to the prime-circle refinement mandate: any fixed scalar weight with finite `|q|^2` bandwidth becomes a universal proper-isometry model once the conductor exceeds that bandwidth. Equation (21) specializes this to every fixed positive integer power of the actual common-anchor chord.

No additional literature dependency beyond the sources already anchored by PC-380 and PC-212 is required for this classification, so `SOURCES.md` need not change.

## 7. RH relevance

This branch does not produce an RH mechanism. In the universal regime there is no free spectral parameter `s`, no gamma factor, no `s <-> 1-s` involution, no critical line, and no distinction between prime and composite refinement degree. The spectral disk is fixed entirely by the scalar RMS norm of the weight and becomes the unit disk after normalization.

The negative result matters because PC-380 explicitly left higher chord powers open. For all **fixed positive integer powers**, that opening is now closed: increasing the polynomial chord power only increases a finite Fourier bandwidth and delays the universal collapse from `m>1` to `m>r`.

## 8. Surviving frontier

The argument uses finite Fourier bandwidth essentially. The structurally different cases still alive are therefore those that evade this finite-aliasing theorem rather than merely choose another finite mask. In particular:

- singular or inverse-chord weights have infinite Fourier tails and can retain nonzero aliases at arbitrarily large `m`;
- conductor-dependent cyclotomic weights may have bandwidth growing with `m`, so the threshold `m>D` never becomes uniform;
- nonlinear/tensor observables need not reduce to the scalar conditional expectation in (5);
- genuinely cross-level nonseparable operators can retain information before each level is separately averaged.

Those cases require separate analysis. The present finding only closes the fixed scalar finite-bandwidth branch and should not be extrapolated to them.

## Sources

- PC-380, `Common-anchor chord-weighted refinement is a universal QMF shift`, for the `r=1` geometric branch and the weighted-composition/QMF prior-art anchors.
- PC-212, for the earlier Prime-Circle filter-bank/Cuntz classicalization cited by PC-380.
- Classical roots-of-unity orthogonality and finite Fourier/polyphase aliasing are used only in the exact derivation (6)--(13); no new external theorem is needed beyond the QMF/weighted-composition framework already recorded for this line.
