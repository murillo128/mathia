# PC-374 — Natural endpoint completion makes the critical line a universal half-density gauge

**Status:** `EXACT-DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for the natural endpoint/completion loophole left open by PC-373. On the source-forced Chebyshev refinement, the singular arcsine gauge does become globally relevant when one passes from finite interior shells to `L^2` spaces. However, on the line `Re(s)=1/2` it does exactly the universal half-density job required to convert Lebesgue measure into the invariant arcsine measure. The resulting weighted transfer operator is unitarily equivalent, after the scalar degree factor, to the ordinary Chebyshev Koopman adjoint. Its normalized spectrum is the closed unit disk for every degree. Thus the appearance of `1/2` in this natural completion is generic change-of-measure geometry, not a Prime-Circle arithmetic mechanism or an RH spectral signature.

This closes only the canonical Lebesgue/arcsine completion of the endpoint singularity. It does not exclude a different boundary extension carrying independently source-forced singular arithmetic data, nor a genuinely non-Chebyshev cross-shell operator.

## 1. The endpoint gauge is exactly the square root of the measure change

PC-373 identifies the source refinement

\[
C_p(\lambda)=\frac{1+T_p(2\lambda-1)}2
\]

and its intrinsic endpoint gauge

\[
h(\lambda)=2\sqrt{\lambda(1-\lambda)}.
\]

The invariant probability measure of the Chebyshev map on `[0,1]` is the arcsine measure

\[
d\mu(\lambda)
=\frac{d\lambda}{\pi\sqrt{\lambda(1-\lambda)}}
=\frac{2}{\pi h(\lambda)}\,d\lambda.
\tag{1}
\]

Hence

\[
d\lambda=\frac\pi2 h\,d\mu.
\tag{2}
\]

For `s=1/2+it`, multiplication by `h^s` therefore has exactly the modulus needed to pass between the two Hilbert spaces. Define

\[
J_s:=\sqrt{\frac\pi2}\,M_{h^s}:
L^2([0,1],d\lambda)\longrightarrow L^2([0,1],d\mu).
\tag{3}
\]

Then

\[
\|J_s f\|_{L^2(\mu)}^2
=\frac\pi2\int h^{2\operatorname{Re}s}|f|^2\,d\mu
=\int |f|^2\,d\lambda
\]

if and only if

\[
\boxed{\operatorname{Re}s=\frac12.}
\tag{4}
\]

Thus the distinguished vertical line arises before any arithmetic input: it is exactly the half-density exponent associated with the Radon–Nikodym factor between Lebesgue and arcsine/Haar-pushforward measure.

## 2. On that line the weighted transfer operator is a standard backward shift

Let

\[
(V_p f)(\lambda):=f(C_p(\lambda))
\]

on `H_mu=L^2([0,1],mu)`. Since `C_p` preserves the arcsine measure, `V_p` is an isometry. For almost every interior `x`, its adjoint is the equal inverse-branch average

\[
(V_p^*g)(x)=\frac1p\sum_{C_p(y)=x}g(y).
\tag{5}
\]

Consequently the unweighted preimage sum in PC-373 satisfies

\[
\mathcal L_{p,0}=pV_p^*.
\tag{6}
\]

PC-373 proved the exact gauge identity

\[
\mathcal L_{p,s}
=p^{-s}M_{h^{-s}}\mathcal L_{p,0}M_{h^s}.
\]

Combining it with (3) and (6) gives, for `Re(s)=1/2`,

\[
\boxed{
\mathcal L_{p,s}
=p^{1-s}J_s^{-1}V_p^*J_s.
}
\tag{7}
\]

The singular factors at `0` and `1` therefore do not create an additional spectrum in the natural `L^2(dlambda)` completion. The pointwise transfer formula, initially interpreted away from the critical preimages/endpoints, has the bounded almost-everywhere extension supplied by the unitary conjugacy (7).

The same calculation also shows why `1/2` is not evidence for the Riemann critical line here. It is forced solely by asking for the endpoint multiplier to implement a unitary change between the two canonical measures.

## 3. The spectrum contains no hidden zeta data

Use the orthonormal Chebyshev/cosine basis of `H_mu`,

\[
e_0=1,
\qquad
e_k(\lambda)=\sqrt2\,T_k(2\lambda-1),\quad k\ge1.
\tag{8}
\]

The composition law for Chebyshev polynomials gives

\[
V_p e_k=e_{pk}.
\tag{9}
\]

Therefore

\[
H_\mu
=\operatorname{span}\{e_0\}
\oplus
\bigoplus_{\substack{r\ge1\\p\nmid r}}
\overline{\operatorname{span}}\{e_{rp^j}:j\ge0\}.
\tag{10}
\]

On each nonconstant chain `V_p` is the unilateral shift, so `V_p^*` is the backward shift; the constant mode is fixed. Hence

\[
\boxed{\sigma(V_p^*)=\overline{\mathbb D}.}
\tag{11}
\]

Equation (7) now yields

\[
\boxed{
\sigma(\mathcal L_{p,s})
=p^{1-s}\overline{\mathbb D},
\qquad \operatorname{Re}s=\frac12.
}
\tag{12}
\]

As a set this is simply the closed disk of radius `sqrt(p)`. After the canonical scalar normalization `p^{s-1}`, the spectrum is the same closed unit disk for every prime. There are no zeta ordinates, no distinguished arithmetic eigenvalues, no gamma factor, and no functional-equation mechanism in this completion.

## 4. The matched non-prime control removes the arithmetic interpretation of `1/2`

Nothing in the preceding argument uses primality. For every integer `m>=2`,

\[
C_m(\lambda)=\frac{1+T_m(2\lambda-1)}2
\]

preserves the same arcsine measure and satisfies

\[
V_m e_k=e_{mk}.
\]

The same decomposition into shift chains gives

\[
\sigma(V_m^*)=\overline{\mathbb D},
\]

and on `Re(s)=1/2` the corresponding derivative-weighted transfer operator is again a scalar multiple of this universal backward-shift model under the same half-density unitary.

This is the decisive control. The vertical line `Re(s)=1/2` survives unchanged when prime arithmetic is removed entirely and the refinement degree is any integer. Its origin is therefore the measure-theoretic half-density relation, not the prime/new-vertex structure.

## 5. Classical boundary and novelty audit

The ingredients needed here are classical rather than a new spectral construction: Chebyshev maps preserve the arcsine measure, their composition operators act by index multiplication on the Chebyshev basis, and transfer/Koopman adjunction is the standard inverse-branch averaging relation. PC-373 already anchored the relevant literature through Boyarsky–Góra on invariant measures for Chebyshev maps, Bi–Antoniou on their Frobenius–Perron spectral decomposition, and Ruelle on transfer operators for expanding maps.

The project-local content is the exact closure of the endpoint loophole created by the singular conjugating gauge in PC-373. The calculation above shows that the most natural global completion does not turn that singularity into arithmetic spectral data: on its apparently suggestive line `Re(s)=1/2`, the gauge is precisely a unitary half-density conversion and exposes the universal shift model underneath.

This also separates the result from arbitrary spectral wrappers. No operator or critical line has been inserted to imitate zeta: both the Chebyshev refinement and its Jacobian weight are the source-forced objects already derived in PC-372/PC-373, and the negative conclusion follows by an exact unitary identification.

## 6. Falsification controls and surviving frontier

The load-bearing checks are direct:

1. verify the density identity (1) by `lambda=(1+cos theta)/2`;
2. verify `C_p` preserves `mu` and that generic fibers have `p` equal conditional weights, giving (5);
3. check `T_k(T_p(x))=T_{kp}(x)`, hence (9);
4. verify that `J_s` is unitary exactly at `Re(s)=1/2`;
5. decompose positive indices uniquely as `r p^j` with `p` not dividing `r`, giving the unilateral-shift chains in (10);
6. repeat with a composite degree `m` to confirm that the same half-density line and disk spectrum persist without prime arithmetic.

A viable endpoint-based Prime-Circle mechanism must therefore contain more than the natural Lebesgue/arcsine completion of the PC-373 gauge. What remains open is a boundary/domain structure independently forced by the original roots-of-unity geometry and carrying extra arithmetic data, or a genuinely non-Chebyshev, cross-shell/nonlocal interaction that is not reduced to this common measure change.

## Research consequence

PC-373 left open the possibility that its endpoint-singular conjugacy could acquire new spectrum after global completion. For the canonical `L^2` completion that possibility is now classified exactly:

\[
\boxed{
\operatorname{Re}s=\tfrac12
\quad\Longleftrightarrow\quad
h^s\text{ is the Lebesgue-to-arcsine half-density},
}
\]

and the normalized transfer operator is just the adjoint Chebyshev shift. The natural endpoint repair therefore does **not** provide a new bridge from Prime-Circle refinement to RH. Future work should not treat the occurrence of `1/2` in this branch as arithmetic evidence unless an additional source-forced structure breaks the universal half-density model.