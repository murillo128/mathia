---
id: WP-358
title: Nonconstant Hecke cusp-boundary positivity is a divisibility projection and still squares the critical half-density
branch: weil_positivity
status: supported
kind: nonconstant-hecke-boundary-divisibility-projection-no-go
claim_strength: exact full-cusp prime-Hecke representation and sharp boundary square; exact single-Fourier-mode T_n decomposition; matched Fourier-density obstruction to the critical half-density
created: 2026-09-18
related: [WP-216, WP-226, WP-255, WP-356, WP-357]
clues: [CLUE-maass-selberg-remainder-sign-interface, CLUE-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - classical self-adjoint normalized Hecke algebra on the modular surface
  - Henryk Iwaniec, Spectral Methods of Automorphic Forms, 2nd ed., AMS, 2002
  - classical Fourier-mode action of Hecke operators on automorphic forms
  - classical Maaß-Selberg relations and sharp/Arthur cusp truncation
  - Bost-Connes projection/range relations and KMS weights
---

# WP-358 — Nonconstant Hecke cusp-boundary positivity is a divisibility projection and still squares the critical half-density

## Claim

`WP-357` classified the cusp **constant mode** and left nonconstant Fourier modes as a genuine escape: there the Hecke operator retains arithmetic information that disappears after reduction to pure log-height translations. That escape can be classified exactly for a prime Hecke correspondence, and on each single Fourier mode for general `T_n`.

In the full cusp Hilbert space, the Petersson-normalized prime Hecke operator is unitarily equivalent to

\[
\boxed{
\mathcal U T_p\mathcal U^{-1}
=V_pS_{\log p}+V_p^*S_{-\log p},
}
\tag{1}
\]

where `S_a` translates log-height by `a`, while `V_p h(u)=h(pu)` is the angular isometry on `L^2(\mathbb T)`. Thus the nonconstant sector does retain genuine arithmetic structure: the range projection

\[
Q_p=V_pV_p^*
\tag{2}
\]

is exactly the projection onto Fourier indices divisible by `p`.

However, for the sharp cusp-height projection `P_\tau`, the inherited positive square is

\[
\boxed{
D_{p,\tau}^*D_{p,\tau}
=
I\otimes \mathbf 1_{(\tau,\tau+L]}
+
Q_p\otimes \mathbf 1_{(\tau-L,\tau]},
\qquad L=\log p,
}
\tag{3}
\]

with `D_{p,\tau}=[P_\tau,\mathcal U T_p\mathcal U^{-1}]`. The Hecke normalization again leaves **unit amplitudes**. The only finite-prime scalar weight available from the angular arithmetic in this positive quadratic form is the mass of `Q_p`.

Under the intrinsic Fourier Følner average,

\[
\frac{\operatorname{Tr}(F_NQ_pF_N)}{\operatorname{Tr}F_N}
\longrightarrow \frac1p.
\tag{4}
\]

Hence, after subtracting the universal forward branch, a flat-height boundary density produces `(\log p)/p`, not the critical Weil weight `(\log p)/\sqrt p`. Recovering `p^{-1/2}` requires taking a square root of the scalarized projection mass, or equivalently moving to an amplitude/overlap before the positive square. That is not supplied by the inherited boundary energy and is the same structural half-density obstruction isolated abstractly in `WP-226` and in the Bost-Connes route of `WP-216`.

So the nonconstant cusp sector **does add real arithmetic specificity**, unlike the Brownian constant-mode geometry of `WP-357`, but its canonical sharp-boundary positivity still squares the critical half-density. This closes the most direct nonconstant-Fourier escape for the sharp Hecke cusp-boundary commutator, without excluding smooth/Arthur truncation, scattering coupling before scalar reduction, infinite all-prime completions, or genuinely global/adelic constructions.

## 1. Exact full-cusp representation of `T_p`

Write the cusp coordinate as

\[
z=u+iy,
\qquad u\in\mathbb T=\mathbb R/\mathbb Z,
\qquad y=e^x.
\tag{5}
\]

Hyperbolic measure is `du\,dy/y^2`. The unitary log-height map is

\[
(\mathcal UF)(u,x)=e^{-x/2}F(u+i e^x),
\tag{6}
\]

from cusp `L^2(du\,dy/y^2)` to `L^2(\mathbb T_u\times\mathbb R_x,du\,dx)`.

For prime `p`, use the standard self-adjoint weight-zero normalization

\[
(T_pF)(z)
=
p^{-1/2}
\left(
F(pz)+\sum_{b=0}^{p-1}F\!\left(\frac{z+b}{p}\right)
\right).
\tag{7}
\]

Define the angular isometry

\[
(V_ph)(u)=h(pu).
\tag{8}
\]

Its adjoint is the transfer operator

\[
(V_p^*h)(u)
=
\frac1p\sum_{b=0}^{p-1}h\!\left(\frac{u+b}{p}\right).
\tag{9}
\]

On the Fourier basis `e_r(u)=e^{2\pi iru}`,

\[
V_pe_r=e_{pr},
\qquad
V_p^*e_r=
\begin{cases}
e_{r/p},&p\mid r,\\
0,&p\nmid r.
\end{cases}
\tag{10}
\]

Thus `V_p^*V_p=I`, while

\[
Q_p:=V_pV_p^*
\tag{11}
\]

is the orthogonal projection onto the closed span of Fourier modes with index divisible by `p`.

Let `(S_af)(x)=f(x+a)`. Under (6), the `F(pz)` branch receives the factor `p^{1/2}` from the height unitary, canceling the Hecke coefficient `p^{-1/2}`. On the averaged inverse branch, the factor `p^{-1/2}` from the height unitary combines with the `p` angular translates to give `V_p^*` with unit coefficient. Therefore

\[
\boxed{
\mathcal U T_p\mathcal U^{-1}
=V_pS_L+V_p^*S_{-L},
\qquad L=\log p.
}
\tag{12}
\]

The normalized Hecke operator has therefore split the prime datum into two different geometric pieces: logarithmic displacement `L=\log p` and a divisibility isometry `V_p`. There is no remaining scalar coefficient `p^{-1/2}` on either branch.

## 2. Exact sharp-boundary square

Let

\[
P_\tau=I\otimes\mathbf 1_{(\tau,\infty)}
\tag{13}
\]

and set

\[
D_{p,\tau}
=[P_\tau,\mathcal U T_p\mathcal U^{-1}].
\tag{14}
\]

Since `P_\tau` acts only in height,

\[
D_{p,\tau}
=V_pA+V_p^*B,
\qquad
A=[P_\tau,S_L],
\qquad
B=[P_\tau,S_{-L}].
\tag{15}
\]

For `L>0`, direct calculation gives

\[
Af(x)
=-\mathbf 1_{(\tau-L,\tau]}(x)f(x+L),
\qquad
A^*A=\mathbf 1_{(\tau,\tau+L]},
\tag{16}
\]

and

\[
Bf(x)
=\mathbf 1_{(\tau,\tau+L]}(x)f(x-L),
\qquad
B^*B=\mathbf 1_{(\tau-L,\tau]}.
\tag{17}
\]

The output supports of `A` and `B` are disjoint, so the cross terms in `D_{p,\tau}^*D_{p,\tau}` vanish. Using `V_p^*V_p=I` and `V_pV_p^*=Q_p` gives exactly (3):

\[
D_{p,\tau}^*D_{p,\tau}
=
I\otimes\mathbf 1_{(\tau,\tau+L]}
+
Q_p\otimes\mathbf 1_{(\tau-L,\tau]}.
\tag{18}
\]

On a pure Fourier mode `e_r\otimes f`,

\[
\boxed{
\|D_{p,\tau}(e_r\otimes f)\|^2
=
\int_\tau^{\tau+L}|f(x)|^2dx
+
\mathbf 1_{p\mid r}
\int_{\tau-L}^{\tau}|f(x)|^2dx.
}
\tag{19}
\]

For `r=0`, where every prime divides the Fourier index, this reduces to the two-sided annulus energy of `WP-356`. For `r\ne0`, the second branch is no longer universal: it is switched on exactly by the arithmetic condition `p\mid r`.

This is the first important distinction from `WP-357`. The nonconstant mode does **not** collapse to arithmetic-blind Brownian overlap geometry. The projection `Q_p` is a genuine prime-specific operator. What fails is more specific: its positive quadratic readout supplies the projection **mass**, rather than the critical square root of that mass.

## 3. General `T_n` on one Fourier mode

The same cancellation can be classified for every normalized Hecke operator

\[
(T_nF)(z)
=
\frac1{\sqrt n}
\sum_{\substack{ad=n\\d>0}}
\sum_{b\!\!\!\pmod d}
F\!\left(\frac{az+b}{d}\right).
\tag{20}
\]

Fix an angular Fourier mode `e_r`. The sum over `b mod d` vanishes unless `d\mid r`; when `d\mid r`, it contributes exactly `d`. The height dilation is `n/d^2`, and under (6) contributes the factor `\sqrt n/d`. Thus

\[
\frac1{\sqrt n}\cdot d\cdot\frac{\sqrt n}{d}=1.
\tag{21}
\]

Consequently,

\[
\boxed{
\mathcal U T_n\mathcal U^{-1}(e_r\otimes f)
=
\sum_{d\mid\gcd(n,r)}
 e_{rn/d^2}\otimes
 S_{\log(n/d^2)}f.
}
\tag{22}
\]

For `r\ne0`, distinct positive divisors `d` give distinct output Fourier indices `rn/d^2`. Therefore the corresponding sharp-boundary commutator branches are orthogonal, and

\[
\boxed{
\|[P_\tau,\mathcal U T_n\mathcal U^{-1}](e_r\otimes f)\|^2
=
\sum_{d\mid\gcd(n,r)}
\int_{I(a_d,\tau)}|f(x)|^2dx,
}
\tag{23}
\]

where `a_d=\log(n/d^2)`, terms with `a_d=0` vanish, and

\[
I(a,\tau)=
\begin{cases}
(\tau,\tau+a],&a>0,\\
(\tau+a,\tau],&a<0.
\end{cases}
\tag{24}
\]

Equation (23) is again a positive sum of **unit-amplitude** boundary energies. Arithmetic enters through which divisors survive and through the logarithmic translation lengths, not through a residual norm factor.

The restriction `r\ne0` matters. For `r=0`, all output frequencies collide, so the branches interfere and one returns to the constant-mode Brownian-overlap geometry classified in `WP-357`. Likewise, (23) is a single-input-Fourier-mode statement; arbitrary superpositions can create output-frequency collisions between different input modes and are not classified here.

## 4. Fourier density exposes the missing half-density

The projection `Q_p` has a canonical density with respect to the symmetric Fourier Følner sequence. Let `F_N` be the projection onto

\[
\operatorname{span}\{e_r:|r|\le N\}.
\tag{25}
\]

Then

\[
\frac{\operatorname{Tr}(F_NQ_pF_N)}{\operatorname{Tr}F_N}
=
\frac{\#\{r\in[-N,N]:p\mid r\}}{2N+1}
\longrightarrow\frac1p.
\tag{26}
\]

This statement needs no chosen automorphic eigenfunction and no inserted zero data. It is the intrinsic natural density of the range of the angular Hecke isometry.

Suppose the two boundary intervals in (18) are tested with equal height mass `m_L`; a flat local height density gives `m_L=L`. The normalized angular average of the positive square is then

\[
m_L\left(1+\frac1p\right).
\tag{27}
\]

The first term is the universal forward branch. Removing it leaves the arithmetic defect

\[
\boxed{
\frac{m_L}{p}.
}
\tag{28}
\]

For flat height density,

\[
\frac{m_L}{p}
=
\frac{\log p}{p}.
\tag{29}
\]

The finite-prime side of the critical Weil explicit formula instead requires the half-density scale

\[
\frac{\log p}{\sqrt p}
\tag{30}
\]

before the test-function translate is paired with its inverse/dual contribution. Equation (29) therefore does not miss the target by a normalization constant: the positive square has converted the available prime projection density `1/p` into a **quadratic mass**, while the Weil coefficient needs its square root.

One can of course write

\[
p^{-1/2}=\sqrt{\lim_{N\to\infty}
\frac{\operatorname{Tr}(F_NQ_pF_N)}{\operatorname{Tr}F_N}},
\tag{31}
\]

but (31) is a nonlinear scalar post-processing step. It is not the value of the inherited quadratic boundary form (18), and the sharp cusp geometry provides no independent theorem that promotes this square root to the coefficient of a global positive pairing. This is precisely the distinction emphasized by `WP-226`: a positive self-pairing naturally sees squared amplitudes; the critical arithmetic coefficient is a half-density and must arise **before** squaring if it is to be geometric rather than inserted.

## 5. Matched controls and falsification

The result survives the most important representation-control tests.

First, unlike `WP-357`, the nonconstant construction genuinely distinguishes primes through `Q_p`; replacing `p` only by a generic translation label would lose the divisibility projection. Thus this is not another proof that the entire construction is representation-universal.

Second, however, the sign theorem itself does not force the required coupling between the two prime data. For a fixed prime-isometry `V_p`, replace `L=\log p` in (12) by an arbitrary positive displacement `L'`. The calculation of (18) remains valid verbatim:

\[
D^*D
=I\otimes\mathbf 1_{(\tau,\tau+L']}
+Q_p\otimes\mathbf 1_{(\tau-L',\tau]}\succeq0.
\tag{32}
\]

So positivity knows separately that there is a positive boundary width and a divisibility projection, but it does not force the Weil-specific relation between logarithmic length and critical half-density.

Third, the arithmetic density itself is robust: (26) is exactly the density of the subgroup `p\mathbb Z` inside `\mathbb Z`. The obstruction therefore is not that the nonconstant cusp sector lacks finite arithmetic information. It is that the canonical quadratic energy reads the density at exponent `1`, not the required exponent `1/2`.

This also provides a precise comparison with the Bost-Connes route of `WP-216`. There, the canonical range projection has critical KMS mass `1/p`; here the Hecke angular range projection has Fourier Følner density `1/p`. These are **not being identified as the same state or the same representation**. What matches is the structural law: a natural prime isometry produces a projection of mass/density `1/p`, while a positive self-pairing sees that projection mass and therefore loses the desired half-density amplitude.

## 6. Prior-art and novelty audit

The ingredients of (12) are classical: normalized Hecke operators, their action on Fourier modes, and cusp truncation are standard automorphic-form technology. The projection onto `p`-divisible Fourier indices is also immediate from the classical transfer/isometry pair. No novelty is claimed for those components.

The line-specific result is the exact combination relevant to the `weil_positivity` mandate: after the cusp unitary, the Hecke normalization cancels all scalar branch amplitudes; the sharp boundary square can then be written exactly as (18), exposing `Q_p` as the only nonconstant-mode prime operator; and its canonical Fourier density is `1/p`, so the positive quadratic defect yields `(\log p)/p` rather than `(\log p)/\sqrt p`.

A bounded prior-art audit against standard Hecke/cusp-truncation, Maaß-Selberg/Arthur, Bost-Connes, Hilbert-Polya/trace, and Weil-positivity surfaces found the classical ingredients but no independent known theorem turning this exact nonconstant sharp-boundary commutator into a global Weil positivity mechanism. The result is therefore recorded as a **negative classification/redirect**, not as a new positivity criterion.

## 7. Scope and surviving escape routes

This finding closes only the direct sharp-boundary route represented by (14), together with the single-Fourier-mode decomposition (22)-(23). It does **not** prove that all nonconstant automorphic data are irrelevant. In particular, it leaves open:

- arbitrary finite Hecke polynomials acting on superpositions of nonconstant modes, where distinct inputs can collide in one output frequency;
- smooth or Arthur truncation in which boundary terms are coupled through a more structured remainder;
- Eisenstein/scattering data retained before reduction to a scalar phase or scalar boundary norm;
- infinite all-prime completions in which an operator-domain or renormalized global structure appears before positivity is taken;
- genuinely adelic, higher-rank, cohomological, or intersection-theoretic forms that couple finite and archimedean places at the source;
- an archimedean sector that is generated by the same global theorem rather than appended after the finite-prime calculation.

The most relevant surviving version of `CLUE-maass-selberg-remainder-sign-interface` is therefore narrower: any useful remainder must introduce a **linear/overlap-level coupling before the quadratic square**, or a global theorem whose positive form is not simply the norm square of the prime-isometry boundary defect.

## Consequence for the main question

Prime-Hecke cusp geometry does contain more arithmetic than the constant-mode picture suggested: its nonconstant boundary response remembers exact prime divisibility through a canonical projection. But the natural positivity theorem is still too weak in precisely the critical way. It outputs projection **mass** `1/p`, whereas Weil requires a prime half-density `p^{-1/2}` coupled to the logarithmic length.

Accordingly, this route does not yet provide a Mathia-native geometric form whose own positivity yields global Weil positivity. It instead sharpens the design constraint: a successful construction must make the half-density an intrinsic **amplitude before positivity is squared**, or must supply a genuinely global coupling in which the critical exponent is forced by the source theorem rather than recovered by taking a square root after scalarization.
