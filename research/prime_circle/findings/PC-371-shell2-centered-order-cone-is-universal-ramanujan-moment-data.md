# PC-371 — shell-2 centered order cone is universal Ramanujan moment data

- **Finding ID:** `PC-371`
- **Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-BOUNDARY`
- **Status detail:** closes the simplest order/positivity escape left explicitly open by PC-369/PC-370. The canonical shell-2 centered profiles do carry an intrinsic strict sign and monotonicity cone that the matched reciprocal sign control of PC-355 does not preserve. However that cone is universal for arbitrary conjugation-stable unit-circle root configurations, and its canonical positive moment/resolvent data are finite binomial transforms of Ramanujan sums. Thus order structure genuinely escapes the common-unitary parity obstruction, but order alone does not supply an arithmetic or RH selector.
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + MATCHED-CONTROL AUDIT + REPRESENTATION AUDIT`
- **Research line:** `prime_circle`
- **Result type:** exact geometric cone / finite moment classicalization
- **RH relevance:** high as a frontier correction. PC-355--PC-370 remain exact for constructions that forget order, but their reciprocal matched control is not admissible once the full source-native radial order cone is retained. The first canonical cone-sensitive spectralization nevertheless collapses to primitive-root angular moments and standard Ramanujan/Dirichlet data.

## Claim

For `n>2`, let

\[
W_n(r):=\log \Phi_n(r)-\varphi(n)\log(1+r),
\qquad r>0,
\tag{1}
\]

be the canonical shell-2 centered profile used in PC-350--PC-370. Pair the primitive `n`-th roots as

\[
e^{\pm i\theta_1},\ldots,e^{\pm i\theta_q},
\qquad
q=\frac{\varphi(n)}2,
\qquad 0<\theta_j<\pi.
\tag{2}
\]

Introduce the inversion-invariant radial coordinate

\[
\boxed{
y(r):=\frac{4r}{(1+r)^2}
=\operatorname{sech}^2\!\left(\frac{\log r}{2}\right)
\in(0,1],
}
\tag{3}
\]

and the angular parameters

\[
\boxed{
\lambda_j:=\cos^2\!\left(\frac{\theta_j}{2}\right)\in(0,1).
}
\tag{4}
\]

Then the centered potential has the exact factorization

\[
\boxed{
\exp W_n(r)
=\prod_{j=1}^{q}\bigl(1-\lambda_j y(r)\bigr),
}
\tag{5}
\]

or equivalently

\[
\boxed{
W_n(r)=\sum_{j=1}^{q}\log\bigl(1-\lambda_j y(r)\bigr).
}
\tag{6}
\]

This has three immediate consequences.

First, every non-calibration shell lies in one strict source-native order cone:

\[
\boxed{
W_n(r)<0
\qquad(n>2,\ r>0).
}
\tag{7}
\]

Moreover `W_n(r)=W_n(r^{-1})`, it decreases strictly on `(0,1)`, increases strictly on `(1,infinity)`, tends to `0` at both radial ends, and has its unique minimum at the common-vertex radius `r=1`.

Second, if

\[
F_n(y):=-W_n(r(y)),
\tag{8}
\]

then

\[
\boxed{
F_n(y)=\sum_{j=1}^{q}-\log(1-\lambda_j y)
=\sum_{m\ge1}\frac{M_m(n)}m y^m,
}
\tag{9}
\]

where

\[
M_m(n):=\sum_{j=1}^{q}\lambda_j^m.
\tag{10}
\]

Every derivative of `F_n` is strictly positive on `0<y<1`:

\[
\boxed{
F_n^{(m)}(y)
=(m-1)!\sum_{j=1}^{q}
\frac{\lambda_j^m}{(1-\lambda_j y)^m}>0.
}
\tag{11}
\]

Thus `F_n` is an absolutely monotone finite atomic Hausdorff-moment potential. Its complete Taylor data are the moments of the positive atomic measure

\[
\nu_n:=\sum_{j=1}^{q}\delta_{\lambda_j}.
\tag{12}
\]

Third, those moments are already classical Ramanujan/Fourier data. For every `m>=1`,

\[
\boxed{
M_m(n)
=\frac{1}{2\,4^m}
\left[
\binom{2m}{m}\varphi(n)
+2\sum_{h=1}^{m}
\binom{2m}{m-h}c_n(h)
\right].
}
\tag{13}
\]

Hence the most canonical positivity-sensitive moment or Jacobi/resolvent spectralization does not produce a new arithmetic carrier: it is a finite binomial transform of the ordinary Ramanujan sums of the primitive-root shell.

The boundary is therefore exact. The sign-flipped matched reciprocal control of PC-355,

\[
W_n\longmapsto -W_n,
\tag{14}
\]

does **not** preserve the source-native order cone (7), so common-unitary parity is not a no-go once order is retained. But the cone itself is reproduced by every finite conjugation-stable multiset of non-real points on the unit circle after the same shell-2 normalization. It therefore fails the README's matched non-prime/non-arithmetic-root control. Keeping the full moment measure recovers the angular root set, but that is lossless cyclotomic reconstruction rather than a new zeta-zero mechanism.

## 1. Root-pair geometry gives the cone exactly

For one conjugate primitive-root pair `e^{+-i theta}`,

\[
(r-e^{i\theta})(r-e^{-i\theta})
=r^2-2r\cos\theta+1.
\tag{15}
\]

Dividing by the corresponding two shell-2 calibration factors gives

\[
\frac{r^2-2r\cos\theta+1}{(1+r)^2}
=1-\frac{2r(1+\cos\theta)}{(1+r)^2}.
\tag{16}
\]

Using

\[
1+\cos\theta=2\cos^2(\theta/2)
\tag{17}
\]

and (3) turns (16) into

\[
\boxed{
\frac{r^2-2r\cos\theta+1}{(1+r)^2}
=1-\cos^2(\theta/2)y(r).
}
\tag{18}
\]

Multiplying (18) over all primitive conjugate pairs proves (5).

This is a direct metric statement. For positive `r`, every primitive root of an `n>2` shell lies strictly closer to `r` than the calibration point `-1` does, after conjugate pairing and degree matching. No arithmetic cancellation is involved. Since `0<lambda_j<1` and `0<y<=1`, every factor in (5) lies strictly between `0` and `1`, proving (7).

The monotonicity is equally forced. The coordinate `y(r)` increases strictly from `0` to `1` on `(0,1)` and decreases strictly from `1` to `0` on `(1,infinity)`, while each `log(1-lambda_j y)` decreases strictly in `y`. Hence `W_n` has the asserted unique minimum at `r=1`.

Equivalently, direct differentiation of one pair gives

\[
\frac{d}{dr}
\log\frac{r^2-2r\cos\theta+1}{(1+r)^2}
=
\frac{2(1+\cos\theta)(r-1)}
{(r^2-2r\cos\theta+1)(1+r)},
\tag{19}
\]

whose sign is exactly `sign(r-1)`.

## 2. The common-vertex von Mangoldt value is the cone endpoint

At the minimum `r=1`, equation (1) gives

\[
W_n(1)
=\log\Phi_n(1)-\varphi(n)\log2.
\tag{20}
\]

The exact common-vertex identity already foundational to Prime Circle is

\[
\log\Phi_n(1)=\Lambda(n)
\qquad(n>1),
\tag{21}
\]

so

\[
\boxed{
F_n(1)
=-W_n(1)
=\varphi(n)\log2-\Lambda(n).
}
\tag{22}
\]

Thus the distinguished arithmetic endpoint of the positive potential is not new: it is exactly the existing von Mangoldt evaluation after the universal totient calibration is removed. The order cone organizes that endpoint geometrically, but does not create a second arithmetic selector.

In logarithmic radius `r=e^{-s}`, the same statement clarifies a sign issue important for radial-flux constructions. The centered flux

\[
-\frac{d}{ds}W_n(e^{-s})
\tag{23}
\]

has one fixed sign for every `n>2` and `s>0`, whereas the uncentered cyclotomic flux can retain arithmetic sign variation. Therefore imposing shell-2 centering and then appealing only to positivity necessarily forgets the signed shell distinction that a separate signed-flux assembly would need to preserve. This does not resolve any cross-shell assembly clue; it only identifies the exact loss introduced by the centered cone.

## 3. The positive moment sequence is a finite Ramanujan transform

From (4), conjugate pairing gives

\[
M_m(n)
=\frac12
\sum_{\substack{1\le a\le n\\(a,n)=1}}
\cos^{2m}\!\left(\frac{\pi a}{n}\right).
\tag{24}
\]

The elementary cosine-power identity

\[
\cos^{2m}x
=\frac1{4^m}
\left[
\binom{2m}{m}
+2\sum_{h=1}^{m}
\binom{2m}{m-h}\cos(2hx)
\right]
\tag{25}
\]

and the definition

\[
c_n(h)
=\sum_{\substack{1\le a\le n\\(a,n)=1}}
 e^{2\pi iha/n}
=\sum_{(a,n)=1}\cos(2\pi ha/n)
\tag{26}
\]

immediately give (13).

This makes the classicalization exact at every fixed moment order. If one extends (24) algebraically to all `n>=1` by

\[
\widehat M_m(n)
:=\frac12
\sum_{(a,n)=1}
\cos^{2m}(\pi a/n),
\tag{27}
\]

then for `Re(s)>2` the standard Dirichlet identities for `varphi` and Ramanujan sums give

\[
\boxed{
\sum_{n\ge1}\frac{\widehat M_m(n)}{n^s}
=
\frac{1}{2\,4^m\zeta(s)}
\left[
\binom{2m}{m}\zeta(s-1)
+2\sum_{h=1}^{m}
\binom{2m}{m-h}\sigma_{1-s}(h)
\right].
}
\tag{28}
\]

For every `n>2`, `widehat M_m(n)=M_m(n)`. The exceptional `n=1,2` convention only affects the calibration boundary and not the Prime-Circle transverse shells.

Equation (28) is precisely the kind of collapse the mandate requires us to detect. Fixed-order positive moments do not create a new zeta carrier: their shell Dirichlet transforms are the already-classical reciprocal-zeta/Ramanujan package. Increasing `m` recovers more of the finite root-angle measure, but that is reconstruction rather than a new functional-equation or critical-line mechanism.

## 4. Canonical cone-sensitive operator is just the angular multiplication operator

Let

\[
T_n:=\operatorname{diag}(\lambda_1,\ldots,\lambda_q)
\tag{29}
\]

on `C^q`, and let `1` denote the all-ones vector. Then

\[
\boxed{
F_n'(y)
=\langle 1,
T_n(I-yT_n)^{-1}1\rangle.
}
\tag{30}
\]

Thus the most direct resolvent attached to the positive cone has spectrum

\[
\operatorname{Spec}(T_n)
=\{\cos^2(\theta_j/2):1\le j\le q\}.
\tag{31}
\]

The Taylor moments determine this finite multiset, and because `theta -> cos^2(theta/2)` is injective on `(0,pi)`, the complete measure `nu_n` determines the primitive-root shell up to the already-present conjugation pairing. Any finite Jacobi matrix reconstructed from the full terminating moment problem is therefore another representation of the same atomic angular measure.

This is a legitimate information-preserving spectral object, but it is not an RH mechanism. Its spectrum is a finite subset of `(0,1)` fixed directly by primitive root angles. No independent spectral parameter, archimedean gamma factor, `s <-> 1-s` relation, zero equation, or critical-line selector is generated. Passing to shell Dirichlet transforms of its fixed moments returns to (28).

## 5. Matched non-arithmetic root configurations reproduce the entire cone class

The strict order property is not cyclotomic. Let

\[
A=\{e^{\pm i\alpha_1},\ldots,e^{\pm i\alpha_q}\},
\qquad 0<\alpha_j<\pi,
\tag{32}
\]

be any finite conjugation-stable multiset of unit-circle points, with no arithmetic assumption on the angles. Define its shell-2 normalized radial product

\[
W_A(r)
:=\sum_{j=1}^{q}
\log\frac{r^2-2r\cos\alpha_j+1}{(1+r)^2}.
\tag{33}
\]

Exactly the same derivation gives

\[
\boxed{
W_A(r)
=\sum_{j=1}^{q}
\log\left(1-\cos^2(\alpha_j/2)y(r)\right)<0,
}
\tag{34}
\]

with the same inversion symmetry, unique minimum, absolute monotonicity of `-W_A` in `y`, positive atomic moment measure, and finite real resolvent spectrum.

Therefore any argument using only the cone axioms

\[
W<0,
\qquad
W(r)=W(r^{-1}),
\qquad
W'\text{ has sign }r-1,
\qquad
-F\text{ is generated by positive unit-interval atoms},
\tag{35}
\]

is reproduced by continuously many non-prime, non-root-of-unity configurations. This directly fails the line-specific matched-root falsification control in the README.

The full atomic measure can of course distinguish the cyclotomic angles from generic angles. But once enough moments are retained to recover the atoms, the construction has become a lossless decoder of the original root geometry. Arithmetic specificity then comes from testing that reconstructed finite set for being a primitive root-of-unity shell, not from a new spectral phenomenon.

## 6. Relation to PC-191 and PC-355--PC-370

PC-191 already pairs primitive roots and factors the uniquely inversion-even exponentially centered reciprocal amplitude into strip-Poisson factors `2(cosh x-cos theta)^{-1}`. The present factorization is not a competing centering. It is the exact shell-2 centering later forced by PC-350, and the identity

\[
\frac{\cosh x-\cos\theta}{\cosh x+1}
=1-\cos^2(\theta/2)\operatorname{sech}^2(x/2)
\tag{36}
\]

is the bridge between the two viewpoints. No novelty is claimed for the elementary root-pair algebra.

PC-355 proves that the full centered Chen/Fock object and the sign-flipped reciprocal control are unitarily equivalent under the common transverse parity. PC-369 then shows that universal Hopf/Lie structure remains equivariant and explicitly leaves order/positivity as one possible source-forced escape. PC-370 closes the linear refinement-incidence escape but again leaves the cone possibility open.

Equation (7) shows that this possibility is real: the reciprocal sign control is outside the source-native radial cone. Hence one must not promote the PC-355 parity control to a no-go for representations that remember pointwise order.

Equations (13), (28), and (34) give the equally important second half: **the first intrinsic order cone is too universal to be arithmetic, while its complete canonical moment spectrum is classical primitive-root/Ramanujan data**. The viable frontier therefore moves one step further: any useful positivity mechanism must combine this order structure with an additional source-forced cross-shell or nonlocal operation that generic unit-circle root configurations cannot reproduce and that does not merely reconstruct the input shell.

## 7. Prior-art and novelty audit

The ingredients are classical. The primitive-root product for `Phi_n`, conjugate pairing, cyclotomic reciprocity, and `Phi_n(1)=exp Lambda(n)` are standard cyclotomic facts already used throughout this research line. PC-191 already records the conjugate-pair hyperbolic factorization closely adjacent to (18).

Ramanujan's original trigonometric sums and the modern product/correlation literature already anchored in `research/prime_circle/SOURCES.md` identify `c_n(h)` as the power/trigonometric moments of the primitive roots. Equation (13) is only the elementary cosine-power/binomial conversion of those classical moments. The Dirichlet transform (28) then follows directly from the standard identities already anchored in `SOURCES.md`,

\[
\sum_{n\ge1}\frac{\varphi(n)}{n^s}
=\frac{\zeta(s-1)}{\zeta(s)},
\qquad
\sum_{n\ge1}\frac{c_n(h)}{n^s}
=\frac{\sigma_{1-s}(h)}{\zeta(s)}.
\tag{37}
\]

A targeted literature search over cyclotomic real-axis bounds, primitive-root trigonometric moments, Hausdorff moment representations, and orthogonal-polynomial/spectral realizations found the moment viewpoint squarely inside classical root-of-unity/Ramanujan theory, not a new zeta spectral construction. No historical novelty is claimed for (5), (13), or the finite atomic resolvent (30).

The durable line-local delta is architectural: **the shell-2 centered Prime-Circle source has a strict intrinsic order cone that invalidates the sign-flipped reciprocal object as a full-geometry matched control, but this escape immediately classicalizes to a universal unit-circle moment cone and Ramanujan data.** This sharply separates what PC-355's unitary parity does and does not rule out.

## 8. Adversarial / falsification audit

1. **Exceptional shell:** `n=2` is exactly the calibration direction and has `W_2=0`; it lies on the boundary of the cone rather than contradicting strict negativity for transverse shells `n>2`.
2. **Root at `-1`:** no primitive `n>2` shell contains `-1`, so every `lambda_j` in (4) is strictly positive. Allowing `-1` in a generic control merely adds a zero atom and weakens strictness; it does not create arithmetic specificity.
3. **Root at `1`:** no primitive `n>1` shell contains `1`. The map `theta -> cos^2(theta/2)` is injective on the chosen conjugate representative interval `(0,pi)`, so no angular information is silently lost beyond conjugation.
4. **Branch of logarithm:** for `r>0`, `Phi_n(r)>0` for `n>2` and every factor in (5) is positive, so all logarithms are real and no branch choice enters.
5. **Representation completeness:** the scalar cone inequalities alone are highly lossy and admit arbitrary-angle controls; the full moment measure is faithful to the conjugate root set. The finding distinguishes those two regimes rather than conflating positivity with reconstruction.
6. **Control admissibility:** the reciprocal sign control remains a valid control for Hilbert/Fock constructions that ignore order. The present theorem does not refute PC-355--PC-370; it proves exactly why a cone-sensitive construction lies outside their common-unitary hypothesis.
7. **No hidden spectral parameter:** `T_n` in (29) is not offered as a Hilbert--Polya operator. It is only the multiplication operator of the finite atomic measure already encoded by the roots, included to audit the most canonical spectral wrapper of the cone.
8. **Dirichlet classicalization:** every fixed moment order reduces by (13) to finitely many Ramanujan sums, and (28) uses standard absolutely convergent Dirichlet identities for `Re(s)>2`. Any continuation beyond that domain is inherited from those classical factors.
9. **Matched generic geometry:** replacing the primitive angles by irrational or otherwise non-arithmetic angles leaves (5)--(11) and all cone properties intact. Therefore positivity by itself fails the line's explicit non-arithmetic-root falsification test.

## Conclusion

The positivity/order route left open after PC-369 is neither empty nor sufficient. Shell-2 centering forces every transverse cyclotomic radial profile into a strict negative, inversion-even, single-well cone, so the global sign-flip control cannot be used once that order structure is retained. But the same cone is universal for arbitrary unit-circle point sets, and its canonical moment/resolvent invariants are exactly primitive-root angular moments whose arithmetic coefficients are finite Ramanujan transforms.

A further Prime-Circle continuation must therefore use positivity **together with** a genuinely arithmetic cross-shell/nonlocal structure that survives matched generic root configurations. Cone membership, finite moment/Hankel data, or the direct angular multiplication operator alone do not cross the research mandate's novelty/RH threshold.
