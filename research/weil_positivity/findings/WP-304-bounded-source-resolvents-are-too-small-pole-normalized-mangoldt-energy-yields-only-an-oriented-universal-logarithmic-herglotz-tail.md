---
id: WP-304
title: Bounded source resolvents are too small; pole-normalized Mangoldt energy yields only an oriented universal logarithmic Herglotz tail
branch: weil_positivity
status: supported
kind: source-resolvent-compression-finite-mass-obstruction-and-renormalized-nevanlinna-asymptotic
claim_strength: exact finite-mass decay obstruction for bounded resolvent compressions, exact logarithmic asymptotic for the positive-energy pole-normalized Mangoldt measure, exact cancellation of that real logarithm under the canonical evenization, and a matched-control proof that the surviving logarithm is density-universal rather than arithmetic-specific
created: 2026-09-14
related: [WP-015, WP-117, WP-256, WP-273, WP-275, WP-277, WP-303]
prior_art:
  - Fritz Gesztesy and Eduard Tsekanovskii, On Matrix-Valued Herglotz Functions, Mathematische Nachrichten 218 (2000), 61-138, DOI 10.1002/1522-2616(200010)218:1<61::AID-MANA61>3.0.CO;2-D, for the classical Nevanlinna-Riesz-Herglotz representation and operator-valued realizations
  - Jussi Behrndt, Fritz Gesztesy, and Shu Nakamura, Spectral shift functions and Dirichlet-to-Neumann maps, Mathematische Annalen 371 (2018), 1255-1300, DOI 10.1007/s00208-017-1593-4, for Weyl/DtN Nevanlinna positivity
  - Tom M. Apostol, Introduction to Analytic Number Theory, Springer, 1976, for the classical Mertens/von-Mangoldt weighted estimates used below
  - NIST Digital Library of Mathematical Functions, Chapter 5, especially sections 5.9 and 5.11, for integral and asymptotic formulas for the digamma function
---

# WP-304 — Bounded source resolvents are too small; pole-normalized Mangoldt energy yields only an oriented universal logarithmic Herglotz tail

## Claim

`WP-303` leaves open an independently forced **nonlocal resolvent/Stieltjes/boundary transform** of Mathia's source spectral measure. The first resolvent version can now be classified sharply.

For any self-adjoint source operator `H` and any bounded incidence/compression map `V`,

\[
M_V(z):=V^*(H-z)^{-1}V,
\qquad \operatorname{Im}z>0,
\tag{1}
\]

is operator-valued Herglotz and satisfies

\[
\boxed{
\|M_V(iy)\|\le \frac{\|V\|^2}{y}
\qquad(y>0).
}
\tag{2}
\]

Equivalently, its compressed spectral measure

\[
\Sigma_V(\Delta)=V^*E_H(\Delta)V
\tag{3}
\]

has finite total mass `V^*V`. Hence a bounded source resolvent compression always decays at imaginary infinity and **cannot itself generate the logarithmically growing Gamma/digamma scale** already identified intrinsically in `WP-117`.

There is a narrow source-side escape, but it does not solve the Weil problem. Take the positive-energy half of `WP-273`/`WP-275`'s pole-normalized Mangoldt measure,

\[
\mu_+
:=
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}\,\delta_{\log n}.
\tag{4}
\]

Its cumulative mass obeys

\[
\boxed{
\mu_+([0,R])=R+O(1).
}
\tag{5}
\]

Thus `mu_+` has infinite total mass, but it satisfies the Nevanlinna integrability condition

\[
\int_0^\infty \frac{d\mu_+(E)}{1+E^2}<\infty.
\tag{6}
\]

The canonical regularized Herglotz transform

\[
m_+(z)
:=
\int_0^\infty
\left(
\frac1{E-z}-\frac{E}{1+E^2}
\right)d\mu_+(E)
\tag{7}
\]

therefore exists, and along the imaginary axis

\[
\boxed{
\operatorname{Re}m_+(iy)=-\log y+O(1),
\qquad
\operatorname{Im}m_+(iy)=\frac\pi2+O(y^{-1})
}
\tag{8}
\]

for `y -> +infinity`.

The logarithm is real, exact at leading order, and source-forced once the positive-energy half is chosen. But it is **not arithmetic-specific**: every positive measure on `[0,infinity)` with cumulative mass `R+O(1)` has the same asymptotic (8). Lebesgue measure itself gives the reference response exactly. Moreover the canonical explicit-formula carrier in `WP-275` is the even measure

\[
\mu_{\rm sym}=\mu_+ + \check\mu_+,
\tag{9}
\]

and its paired resolvent response on `iy` is purely imaginary; the real logarithm cancels identically. Therefore the logarithmic tail survives only after an **orientation/positive-energy split** and an **infinite-mass renormalization**. Neither operation supplies the exact Gamma profile, the pole terms, the finite-prime/archimedean orientation of the Weil form, or an independent global sign theorem.

So the direct route left by `WP-303` narrows to:

\[
\boxed{
\text{bounded source resolvent compression}
\;\text{is too small};
\quad
\text{log growth requires an unbounded/generalized boundary channel or renormalized infinite-mass measure.}
}
\tag{10}
\]

Even then, the first surviving logarithm is a universal density effect and disappears under the canonical evenization. A successful resolvent/boundary mechanism must therefore derive, before target comparison, both the required orientation and a nontrivial subleading structure that distinguishes the Riemann Gamma sector from arbitrary unit-density Herglotz measures.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + BOUNDED-RESOLVENT-FINITE-MASS-DECAY + SOURCE-NATIVE-RENORMALIZED-HERGLOTZ-ESCAPE + MANGOLDT-MERTENS-LINEAR-ENERGY-DENSITY + UNIVERSAL-LOG-ASYMPTOTIC + EVENIZATION-CANCELLATION + MATCHED-CONTROL + CLASSICAL-HERGLOTZ-PRIOR-ART + NOT-WEIL-POSITIVITY`.

## 1. Bounded resolvent compressions have finite spectral mass

Let `H=H^*` on a Hilbert space `mathcal H` and let

\[
V:\mathcal K\to\mathcal H
\tag{11}
\]

be bounded. The spectral theorem gives

\[
M_V(z)
=V^*(H-z)^{-1}V
=\int_{\mathbb R}\frac{d\Sigma_V(E)}{E-z},
\tag{12}
\]

where

\[
\Sigma_V(\Delta)=V^*E_H(\Delta)V\succeq0.
\tag{13}
\]

The total operator mass is

\[
\boxed{
\Sigma_V(\mathbb R)=V^*V.
}
\tag{14}
\]

In particular this is a finite positive operator-valued measure in norm on every scalar matrix element.

The standard resolvent identity gives

\[
\operatorname{Im}M_V(z)
=(\operatorname{Im}z)
V^*(H-\bar z)^{-1}(H-z)^{-1}V
\succeq0,
\tag{15}
\]

so `M_V` is a Herglotz/Nevanlinna function. But positivity does not remove the high-energy constraint. For `z=iy`,

\[
\|(H-iy)^{-1}\|\le \frac1y,
\tag{16}
\]

therefore

\[
\boxed{
\|M_V(iy)\|
\le
\frac{\|V\|^2}{y}.
}
\tag{17}
\]

This conclusion is independent of whether `H` has pure point, singular continuous, or absolutely continuous spectrum. It uses only self-adjointness and **bounded** source incidence.

`WP-117` records the canonical critical Gamma variation

\[
H_\infty(t)
=
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
-\psi\!\left(\frac14\right),
\tag{18}
\]

with

\[
H_\infty(t)=\log|t|+O(1).
\tag{19}
\]

Thus no scalar matrix element, finite-dimensional compression, or bounded operator compression of the raw resolvent (12) can equal this archimedean response at large imaginary energy. The mismatch is not a coefficient error: one class decays as `1/y`, while the other grows logarithmically.

This closes the most literal nonlocal-resolvent escape in `WP-303`.

## 2. The pole-normalized Mangoldt half-measure has linear energy mass

The obstruction above suggests the only way a Stieltjes/Herglotz response can acquire logarithmic growth: the representing spectral measure must have infinite total mass and the transform must be renormalized.

Mathia already contains a natural candidate. `WP-273` and `WP-275` isolate the pole-normalized arithmetic measure with atoms at `+/- log n` and weight `Lambda(n)/(n+1)`. Before evenization, its positive-energy half is (4).

Set

\[
A(x)
:=
\sum_{n\le x}\frac{\Lambda(n)}{n+1}.
\tag{20}
\]

The classical Mertens estimate for von Mangoldt weights is

\[
\sum_{n\le x}\frac{\Lambda(n)}n
=\log x+O(1).
\tag{21}
\]

The change from `1/n` to `1/(n+1)` is absolutely summable because

\[
0\le
\sum_{n\ge2}\Lambda(n)
\left(\frac1n-\frac1{n+1}\right)
=
\sum_{n\ge2}\frac{\Lambda(n)}{n(n+1)}
\le
\sum_{n\ge2}\frac{\log n}{n^2}
<\infty.
\tag{22}
\]

Hence

\[
\boxed{A(x)=\log x+O(1).}
\tag{23}
\]

Passing to the logarithmic energy coordinate `x=e^R` gives exactly

\[
\boxed{
M(R):=\mu_+([0,R])=R+O(1).
}
\tag{24}
\]

No RH input, zero data, or analytic continuation is used here. In fact the `O(1)` form is already a classical Mertens-level statement.

Equation (24) immediately shows that `mu_+` cannot be the scalar spectral measure of a bounded vector/compression as in (14): its total mass is infinite.

## 3. Infinite mass is still Nevanlinna-admissible

Infinite mass does not prevent a Herglotz representation. What is required for the regularized Nevanlinna integral is

\[
\int_0^\infty\frac{d\mu_+(E)}{1+E^2}<\infty.
\tag{25}
\]

Equation (24) gives this directly. Stieltjes integration by parts yields, for `R` large,

\[
\int_{[1,R]}\frac{d\mu_+(E)}{1+E^2}
=
\frac{M(R)}{1+R^2}
-
\frac{M(1)}2
+
\int_1^R
\frac{2E\,M(E)}{(1+E^2)^2}\,dE.
\tag{26}
\]

Since `M(E)=O(E)`, the last integrand is `O(E^{-2})`. Letting `R -> infinity` proves (25).

Therefore the regularized transform (7) is a legitimate scalar Herglotz function. This is precisely the boundary between the bounded-resolvent class and a generalized/unbounded boundary realization: the positivity theorem survives, but the finite-mass realization does not.

The distinction matters. The general Herglotz representation may also contain an affine term `az+b` with `a>=0`; such a term is absent from the bounded resolvent compression (12). Allowing the full Nevanlinna class is already a genuine enlargement of mechanism, not a hidden way to evade (17).

## 4. Unit energy density forces a universal logarithm

The asymptotic of (7) can be obtained without any zero information.

Let `lambda` denote Lebesgue measure on `[0,infinity)` and define the reference regularized transform

\[
m_0(z)
:=
\int_0^\infty
\left(
\frac1{E-z}-\frac{E}{1+E^2}
\right)dE.
\tag{27}
\]

At `z=iy`, `y>0`, its real part is

\[
\begin{aligned}
\operatorname{Re}m_0(iy)
&=
\int_0^\infty
\left(
\frac{E}{E^2+y^2}
-\frac{E}{1+E^2}
\right)dE\\
&=
\boxed{-\log y},
\end{aligned}
\tag{28}
\]

while

\[
\operatorname{Im}m_0(iy)
=
\int_0^\infty\frac{y}{E^2+y^2}\,dE
=
\boxed{\frac\pi2}.
\tag{29}
\]

Now write the signed measure

\[
d\nu=d\mu_+-dE,
\qquad
N(R):=\nu([0,R]).
\tag{30}
\]

Equation (24) says

\[
\boxed{N(R)=O(1).}
\tag{31}
\]

For the real kernel

\[
r_y(E)
:=
\frac{E}{E^2+y^2}-\frac{E}{1+E^2},
\tag{32}
\]

both endpoint boundary terms vanish and Stieltjes integration by parts gives

\[
\int_0^\infty r_y(E)\,d\nu(E)
=-\int_0^\infty N(E)r_y'(E)\,dE.
\tag{33}
\]

The function `E/(E^2+a^2)` increases once and decreases once, with total variation `1/a`. Therefore, for `y>=1`,

\[
\int_0^\infty |r_y'(E)|\,dE
\le 1+\frac1y
\le2.
\tag{34}
\]

Using (31) in (33),

\[
\int_0^\infty r_y(E)\,d\nu(E)=O(1).
\tag{35}
\]

Combining with (28) proves

\[
\boxed{
\operatorname{Re}m_+(iy)=-\log y+O(1).
}
\tag{36}
\]

For the imaginary kernel

\[
q_y(E)=\frac{y}{E^2+y^2},
\tag{37}
\]

the total variation on `[0,infinity)` is `1/y`. The same integration-by-parts argument gives

\[
\int_0^\infty q_y(E)\,d\nu(E)=O(y^{-1}),
\tag{38}
\]

and (29) yields

\[
\boxed{
\operatorname{Im}m_+(iy)=\frac\pi2+O(y^{-1}).
}
\tag{39}
\]

This is an exact asymptotic consequence of the source measure.

## 5. The logarithm fails the arithmetic-specificity control

Equation (36) looks superficially promising because the Gamma/digamma sector also has logarithmic high-energy growth. It does not pass the branch's matched-control gate.

The proof of (36) uses no prime-power spacing after (24). More generally, if `mu` is **any** positive measure on `[0,infinity)` satisfying

\[
\mu([0,R])=R+O(1),
\tag{40}
\]

then the same argument gives

\[
\operatorname{Re}m_\mu(iy)=-\log y+O(1),
\qquad
\operatorname{Im}m_\mu(iy)=\frac\pi2+O(y^{-1}).
\tag{41}
\]

Lebesgue measure is the sharpest control: it has no primes at all and gives the leading response exactly.

A discrete control works as well. Replace the prime-power atoms by an approximately unit-density lattice in energy and choose bounded positive masses so that the cumulative discrepancy from `R` stays bounded. Its regularized Herglotz transform has the same logarithmic leading term.

Therefore

\[
\boxed{
\text{the first logarithm records asymptotic energy density, not Riemann arithmetic.}
}
\tag{42}
\]

The arithmetic information can only live in the bounded/subleading remainder, the exact pole structure, or an additional coupling law. Matching just the `log y` scale is not evidence that the source has generated the Riemann archimedean factor.

This also prevents a novelty overclaim. Herglotz representations, Mertens estimates, and logarithmic Cauchy-transform asymptotics are classical. The branch-local contribution is the exact application to `WP-275`'s source-selected pole-normalized measure and the resulting localization of what a surviving resolvent completion would still have to explain.

## 6. Canonical evenization cancels the real logarithm

There is a stronger falsification. The pole-normalized measure entering the explicit-formula carrier in `WP-275` is not `mu_+` but the symmetric measure

\[
\mu_{\rm sym}
=
\mu_+ + \check\mu_+,
\qquad
\check\mu_+(A)=\mu_+(-A).
\tag{43}
\]

For one positive energy `E`, the paired resolvent kernel is

\[
\frac1{E-z}+\frac1{-E-z}
=
\frac{2z}{E^2-z^2}.
\tag{44}
\]

The odd Nevanlinna subtraction terms `E/(1+E^2)` cancel between `+E` and `-E`. Along `z=iy`,

\[
\frac{2iy}{E^2+y^2}
\tag{45}
\]

is purely imaginary. Hence

\[
\boxed{
\operatorname{Re}m_{\rm sym}(iy)=0
}
\tag{46}
\]

for the canonical paired response, wherever it is defined by the corresponding regularization.

So the logarithm in (36) is **orientation-sensitive**. It appears only after choosing the positive-energy half supplied naturally by the source Fock Hamiltonian of `WP-256`/`WP-275`, not from the even explicit-formula carrier itself.

This does not make the positive-energy split illegitimate: the source Hamiltonian really does have energies `k log p >=0`. But it means the split is an additional structural datum that a global construction must transport and orient correctly. If one restores the canonical `+/- log n` symmetry too early, the real logarithmic candidate disappears.

## 7. Relation to the exact Gamma channel of WP-117

`WP-117` is stronger on the archimedean side than the present asymptotic: Prime Circle independently selects the Riemann `q=2` channel and yields the exact normalized digamma variation, with its own unconditional Lévy--Dirichlet positivity theorem.

The present result therefore should **not** be read as a new derivation of Gamma from primes. It answers a different live question created by `WP-303`: can the source arithmetic spectral measure itself, through a canonical nonlocal resolvent compression, supply the missing smooth archimedean response?

The answer splits cleanly:

1. **Bounded compression: no.** Equation (17) forces decay and cannot reach the Gamma logarithm.
2. **Renormalized infinite-mass source response: only partially.** The pole-normalized positive-energy measure reaches a logarithmic Herglotz class, but the leading logarithm is universal and its sign/convention does not by itself identify the Weil archimedean orientation.
3. **Canonical evenization: no real logarithm.** Equation (46) removes the apparent bridge.

Thus the exact Prime-Circle Gamma channel and the exact arithmetic source measure still need a genuinely coupled geometric law if they are to become parts of one positive global object.

## 8. Prior-art and novelty audit

The underlying ingredients are classical.

The identity (15) is the standard Herglotz/Weyl positivity formula and is already the boundary-response control used in `WP-015`. The general Nevanlinna representation allows positive measures satisfying (25), including infinite-mass measures after the standard subtraction; Gesztesy--Tsekanovskii and the Weyl/DtN literature cover this realization framework. Therefore neither Herglotz positivity nor the use of a regularized Cauchy transform is new.

Equation (21) is a classical Mertens estimate. Equations (18)--(19) are the standard digamma asymptotic already used in `WP-117` and recorded in DLMF. The calculation (36) is a direct Abel/Stieltjes consequence of these classical facts.

The Mathia-specific content is narrower: `WP-273`/`WP-275` independently produced exactly the weight `Lambda(n)/(n+1)` on logarithmic prime-power energies; `WP-303` independently left nonlocal resolvent/boundary response as one of the few surviving source laws. Combining those two facts yields the exact finite-mass no-go, the required transition to an infinite-mass Nevanlinna class, the unit-density universality control, and the evenization cancellation.

This is also distinct from Hilbert--Pólya or zero-defined Weyl functions: no zeta zero enters the construction. It is distinct from Connes/trace-formula positivity because no trace formula or adelic quotient is asserted. It is not a new boundary-triple theorem, and it does not promote generic Herglotz positivity to Weil positivity.

## 9. Aggressive falsification and scope boundary

Several tempting stronger claims fail.

**First, logarithmic growth is not enough.** Equation (41) gives the same leading logarithm for nonarithmetic controls. Exact Gamma requires its full meromorphic/subleading structure, not only `log y`.

**Second, the sign of the real logarithm is convention-sensitive.** The Herglotz convention `(E-z)^{-1}` gives `-log y` in (36), while changing transform conventions changes signs. No Weil orientation is inferred from this asymptotic alone.

**Third, the canonical symmetric carrier cancels the real part.** The one-sided result cannot be silently substituted for the even explicit-formula measure.

**Fourth, a general Weyl function can evade the bounded-compression estimate.** Unbounded boundary maps, boundary relations, renormalized traces, scattering matrices, determinants, and domain-changing couplings can produce growth not allowed by (17). They are not ruled out. They are precisely the surviving category.

**Fifth, an affine Herglotz term does not rescue bounded compression.** A general Nevanlinna function may contain `az+b`; the raw bounded resolvent (12) does not. Adding such a term by hand would change the source law, and in any case a linear term does not explain the exact Gamma logarithm.

**Sixth, determinants/log-determinants are outside the theorem.** An infinite-dimensional regularized determinant can accumulate many decaying resolvent contributions into a logarithm. That is a different nonlinear/nonlocal observable and requires its own source-forcing and subtraction audit.

These exclusions are mechanism boundaries, not loopholes in the proved statements.

## 10. Consequence for the research frontier

After `WP-303`, the live spectral branch allowed a source-forced nonlocal resolvent/scattering/boundary transform. `WP-304` removes its simplest bounded form and identifies what must change for the branch to remain viable.

A surviving construction must now derive **before Gamma matching** at least one of the following from Mathia's intrinsic geometry:

- an unbounded or generalized boundary incidence whose spectral measure has the required infinite-mass Nevanlinna asymptotics;
- a source-forced renormalization/subtraction law, rather than the standard subtraction chosen merely because it makes the target finite;
- a nontrivial orientation mechanism explaining why the positive-energy half, rather than the canonical even carrier, is the relevant boundary response;
- or a genuinely finite--archimedean coupled operator/nonlinear spectral observable whose subleading response distinguishes the Riemann Gamma profile from every unit-density control.

The decisive next test is therefore **not** whether another transform can produce a logarithm. That is cheap. It is whether a Mathia-native source law fixes the orientation, renormalization, and subleading spectral structure while retaining an independent positivity theorem and reproducing the pole/global terms in the same object.

## Conclusion

The nonlocal resolvent escape has a sharp boundary. Bounded positive source incidence gives a finite spectral measure and a resolvent response that dies as `1/y`, so it cannot generate the Gamma scale. The pole-normalized Mangoldt source can cross that boundary only because its positive-energy spectral mass is infinite but Nevanlinna-admissible; after regularization it produces a logarithm.

That logarithm is nevertheless **universal unit-density behavior**, not a Riemann-specific archimedean structure, and the canonical `+/-` evenization removes its real part altogether. The surviving route therefore has to explain substantially more than logarithmic growth: it must source the orientation, renormalization, exact Gamma remainder, pole terms, and global sign from one coupled geometry rather than from a generic Herglotz realization.