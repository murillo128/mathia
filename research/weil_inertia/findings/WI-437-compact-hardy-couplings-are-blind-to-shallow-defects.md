# WI-437 — compact Hardy couplings are asymptotically blind to shallow defects

Status: `EXACT-DERIVED + CLASSICAL-OPERATOR-THEORY + DECISIVE-BARRIER + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`

Parent: `WI-436`

## Claim

The mixed-frequency escape left open by `WI-436` has a sharp compactness barrier. For a single right-half Kunik defect at

\[
\rho=\frac12+d+i\gamma,
\qquad d>0,
\]

with multiplicity `m`, probe on the interior line

\[
\Re s=\frac12+a,
\qquad a=\theta d,
\qquad 0<\theta<1.
\]

Let `G_+` and `G_-` be the positive- and negative-frequency Hardy pieces of the one-zero logarithmic-derivative block from `WI-436`. If

\[
K:\mathcal H_+\longrightarrow\mathcal H_-
\]

is any fixed compact operator between the two Hardy channels, then

\[
\boxed{
\sup_{\gamma\in\mathbb R}
\frac{|\langle K G_+,G_-\rangle|}
{\|G_+\|_2\,\|G_-\|_2}
\longrightarrow0
\qquad(d\downarrow0).
}
\tag{1}
\]

The same statement holds for a compact conjugate-linear cross-channel map, and therefore for the nonconjugated bilinear convention of `WI-436` after the fixed Hardy reflection/conjugation that identifies the negative channel with the conjugate positive channel.

By contrast, the canonical `WI-436` bilinear pairing remains a fixed nonzero fraction of the channel norms:

\[
\boxed{
\frac{\displaystyle\int_{\mathbb R}G_+(t)G_-(t)\,dt}
{\|G_+\|_2\,\|G_-\|_2}
=\sqrt{1-\theta^2}.
}
\tag{2}
\]

Equivalently,

\[
\int_{\mathbb R}G_+(t)G_-(t)\,dt
=\frac{\pi m^2}{d},
\tag{3}
\]

whereas every fixed compact mixed correction is

\[
\boxed{
\langle K G_+,G_-\rangle=o_\theta\!\left(\frac{m^2}{d}\right)
}
\tag{4}
\]

uniformly in the ordinate `gamma`.

Thus a compact perturbation cannot change the leading shallow-defect saturation exposed by `WI-436`. Any Hankel/mixed-frequency route that is supposed to supply a **uniform per-defect coercive quantum down to arbitrarily small horizontal depth** must contain an essentially noncompact component. Compactness is not the whole obstruction, but noncompactness is a necessary gate.

For a classical Hankel operator

\[
H_\varphi=P_-M_\varphi|_{\mathcal H_+},
\]

Hartman's theorem therefore gives a concrete symbol-class boundary. On the disk, `H_phi` is compact exactly when its symbol class lies in

\[
H^\infty+C(\mathbb T).
\tag{5}
\]

After the Cayley transform to the half-plane, symbols in the corresponding `H^infty + C(dot R)` class are compact. In particular, a fixed smooth compactly supported or decaying boundary symbol is in the blind class. A viable Hankel escape from `WI-436` must leave this compact symbol class, or use a parameter family whose compactness degenerates at the same shallow-defect scale.

This does **not** say that every noncompact Hankel operator works. It says that a fixed compact one cannot be the missing source-side coercive mechanism.

## 1. Exact one-defect Hardy channels

For the finite Kunik block used in `WI-436`, the one-zero logarithmic derivative on `Re(s)=1/2+a` is

\[
G_{d,a,\gamma}(t)
=m\left(
\frac1{a-d+i(t-\gamma)}
-
\frac1{a+d+i(t-\gamma)}
\right).
\tag{6}
\]

Under the Fourier convention of `WI-429`--`WI-436`, for `xi>0` its two Hardy pieces satisfy

\[
\widehat G_+(\xi)
=-2\pi m\,e^{-(d-a)\xi}e^{-i\gamma\xi},
\tag{7}
\]

and

\[
\widehat G_-(-\xi)
=-2\pi m\,e^{-(d+a)\xi}e^{+i\gamma\xi}.
\tag{8}
\]

Write

\[
r_-=d-a=(1-\theta)d,
\qquad
r_+=d+a=(1+\theta)d.
\tag{9}
\]

Plancherel gives the exact norms

\[
\boxed{
\|G_+\|_2^2=\frac{\pi m^2}{r_-},
\qquad
\|G_-\|_2^2=\frac{\pi m^2}{r_+}.
}
\tag{10}
\]

Nonconjugated Parseval gives

\[
\begin{aligned}
\int_{\mathbb R}G_+(t)G_-(t)\,dt
&=\frac1{2\pi}
\int_0^\infty
\widehat G_+(\xi)\widehat G_-(-\xi)\,d\xi\\
&=2\pi m^2\int_0^\infty e^{-2d\xi}\,d\xi\\
&=\frac{\pi m^2}{d}.
\end{aligned}
\tag{11}
\]

Combining (10) and (11) proves (2):

\[
\frac{\pi m^2/d}
{\pi m^2/\sqrt{r_-r_+}}
=\frac{\sqrt{d^2-a^2}}d
=\sqrt{1-\theta^2}.
\tag{12}
\]

So at any fixed relative probe depth, for example `theta=1/2`, the canonical mixed pairing remains macroscopically correlated all the way to `d=0`; for `theta=1/2` the normalized correlation is exactly `sqrt(3)/2`.

## 2. The normalized shallow channels are uniformly weakly null

Strip off the harmless Fourier/Plancherel constants and multiplicity. The normalized positive-frequency profile is unitarily equivalent to

\[
u_{r,\gamma}(\xi)
=\sqrt{2r}\,e^{-r\xi}e^{-i\gamma\xi},
\qquad \xi>0,
\tag{13}
\]

with

\[
\|u_{r,\gamma}\|_{L^2(0,\infty)}=1.
\tag{14}
\]

As `r downarrow 0`, these vectors are weakly null **uniformly in `gamma`**. Indeed, first take `f` supported in `[0,R]`. Then

\[
\begin{aligned}
|\langle u_{r,\gamma},f\rangle|
&\le \sqrt{2r}\int_0^R|f(\xi)|\,d\xi\\
&\le \sqrt{2rR}\,\|f\|_2,
\end{aligned}
\tag{15}
\]

and the right side is independent of `gamma`. Compactly supported `L^2` functions are dense in `L^2(0,infty)`, while all `u_{r,gamma}` have norm one. Therefore

\[
\boxed{
\sup_{\gamma\in\mathbb R}
|\langle u_{r,\gamma},f\rangle|
\longrightarrow0
\quad(r\downarrow0)
}
\tag{16}
\]

for every `f in L^2(0,infty)`.

The normalized negative-frequency channel, after the fixed reflection identifying `H_-` with another copy of `L^2(0,infty)`, has the same form with `r=r_+` and the opposite phase. Since both `r_-` and `r_+` tend to zero with `d`, both one-defect channels are boundary-kernel/Paley--Wiener wave packets escaping weakly to infinity in frequency.

## 3. Compact operators kill the normalized shallow channel

Let `K` be compact from the positive channel to the negative channel. Equation (16) implies

\[
\boxed{
\sup_{\gamma\in\mathbb R}
\|K u_{r,\gamma}\|_2
\longrightarrow0
\qquad(r\downarrow0).
}
\tag{17}
\]

The uniformity is worth making explicit. If (17) failed, there would be `epsilon>0`, a sequence `r_n downarrow0`, and ordinates `gamma_n` with

\[
\|K u_{r_n,\gamma_n}\|_2\ge\varepsilon.
\]

But (16) says `u_{r_n,gamma_n} weakly ->0`, and every compact operator maps bounded weakly convergent sequences to norm-convergent sequences. Hence `K u_{r_n,gamma_n}->0` in norm, a contradiction.

Apply this to `r=r_-=(1-theta)d` and pair against the normalized negative channel. Cauchy--Schwarz gives

\[
\sup_\gamma
\frac{|\langle K G_+,G_-\rangle|}
{\|G_+\|_2\|G_-\|_2}
\le
\sup_\gamma\|K u_{r_-,\gamma}\|_2
\longrightarrow0,
\tag{18}
\]

which proves (1). Since

\[
\|G_+\|_2\|G_-\|_2
=\frac{\pi m^2}{d\sqrt{1-\theta^2}},
\tag{19}
\]

equation (4) follows as well.

The same proof works for compact conjugate-linear maps: compactness is a statement about the image of bounded sets, and weak convergence is preserved under the fixed conjugations/reflections relating the Hardy conventions. Thus the conclusion does not depend on whether a proposed mixed functional is written as a Hilbert-space sesquilinear matrix coefficient or in the nonconjugated bilinear convention used by the exact square in `WI-436`.

A slightly stronger useful version is immediate. If a family of compact cross-channel operators is **relatively compact in operator norm**, then (17)--(18) hold uniformly over that family as well, by a finite epsilon-net argument. Therefore merely allowing a bounded smooth parameter does not evade the obstruction unless the operator family itself loses norm precompactness as the defect approaches the boundary.

## 4. Hartman turns the abstract compactness barrier into a symbol gate

Hartman's classical theorem characterizes compact scalar Hankel operators on `H^2(T)`: for the standard convention

\[
H_\varphi=P_-M_\varphi|_{H^2},
\]

compactness is equivalent to the existence of a symbol representative in

\[
H^\infty+C(\mathbb T).
\tag{20}
\]

Bonsall--Power give a model-free proof and explicitly restate Hartman's characterization. A Cayley transform transfers the result to the half-plane Hardy model used here. Hence a fixed source multiplier whose boundary symbol is continuous on the one-point compactification of the real line, modulo an analytic `H^infty` term, produces a compact Hankel cross-channel map and is subject to (1).

This includes, in particular, fixed `C_c^infty(R)` multipliers and fixed continuous multipliers decaying to zero at both ends. Such symbols may create nontranslation-invariant frequency mixing, but that mixing is compact and therefore disappears on the normalized shallow Kunik channels.

Conversely, escaping the theorem requires an **essentially noncompact** Hankel class. In disk language the symbol must lie outside `H^infty+C(T)` modulo the usual symbol equivalence. In half-plane language it must retain noncompact boundary structure after Cayley transfer. Persistent oscillation, a nonremovable discontinuity/singularity, or a scale-dependent family escaping norm precompactness are examples of mechanisms that can evade this particular barrier; none is sufficient by itself.

## 5. Consequence for the post-WI-436 frontier

`WI-436` closed the translation-invariant mixed pairing as an independent bootstrap because the finite Kunik inner factor saturates it exactly, and left a nontranslation-invariant/Hankel-type arithmetic coupling as one possible escape. The present result splits that escape into two qualitatively different classes.

A fixed compact mixed operator is lower order on an arbitrarily shallow defect. It cannot alter the leading `pi m^2/d` matched-control signal and therefore cannot provide a depth-uniform source-side contradiction against the finite Blaschke model. In particular, taking the exact `WI-436` pairing and adding a compact correction gives, on a one-zero shallow block,

\[
B_{\rm canonical}+B_K
=\frac{\pi m^2}{d}\bigl(1+o_\theta(1)\bigr).
\tag{21}
\]

So a successful mixed-frequency route needs more than “nontranslation invariant”: it must expose an **essential** cross-frequency component whose normalized matrix elements remain order one on the boundary-kernel family (13), and that component must be fixed or controlled from arithmetic/source data independently of the off-line divisor.

This is a sharper falsification gate for future proposals. Before a source-derived Hankel observable is pursued, test its Calkin class. If the operator is compact, or if the relevant family remains norm precompact at the shallow scale, it cannot be the uniform first-defect detector. If it is noncompact, the next test is whether its essential response on the exact packets (13) is nonzero and source-controlled; noncompactness alone does not imply coercivity.

## 6. Relation to earlier local barriers

The result is not a duplicate of the earlier compactness findings in this line.

`WI-305` proves that a particular **tail-dropped localized explicit-formula comparison** has an essential negative numerical-range band as soon as the first prime channel activates, so no fixed compact self-adjoint correction can restore positivity. Its weakly-null sequence is a high-frequency arithmetic modulation and its obstruction comes from a prime atom that exceeds the fixed reserve.

Here the direction is different: the finite Kunik defect itself generates a canonical shallow-depth weakly-null Hardy-kernel family, and compact cross-channel operators vanish on that family. The conclusion classifies a specific escape proposed after `WI-436`, independently of Liu's tail-dropped comparison or any prime activation threshold.

`WI-273` is also neighboring rather than duplicative. There the positive Suzuki gap kernel is compact for every positive gap but tends to the noncompact Carleman wall as the gap closes. That is a useful analogue of the present compact/noncompact transition, but it concerns a different source kernel and a one-signed gap-screening problem. The exact Hardy-channel asymptotic (1)--(4) is not contained in that result.

## 7. Prior art and novelty audit

No novelty or priority claim is made for the functional-analysis ingredients.

- Philip Hartman, **On completely continuous Hankel matrices**, *Proceedings of the American Mathematical Society* **9** (1958), 862--866, DOI `10.1090/S0002-9939-1958-0108684-8`, is the classical source for the compact-Hankel characterization.
- F. F. Bonsall and S. C. Power, **A proof of Hartman's theorem on compact Hankel operators**, *Mathematical Proceedings of the Cambridge Philosophical Society* **78** (1975), 447--450, DOI `10.1017/S0305004100051914`, explicitly states the scalar `H^infty+C(T)` characterization and proves a more general shift-model version.
- Weak convergence of normalized Hardy reproducing kernels to zero at the boundary, and the fact that compact operators send bounded weakly-null sequences to norm-null sequences, are classical Hilbert-space facts. The proof above is included directly in (15)--(17), so no specialized reproducing-kernel theorem is load-bearing.
- Modern reproducing-kernel tests for Hankel/Schatten classes provide neighboring operator-theoretic context, but no such theorem is needed for the barrier.

A targeted literature search around compact Hankel operators, Hartman's theorem, normalized Hardy kernels, reproducing-kernel testing and essential norms found the classical operator mechanism above, but no zeta-specific theorem asserting the present finite-Kunik shallow-defect consequence. Repository-local duplication checks against `WI-273` and `WI-305` likewise found related compactness mechanisms in different objects, not this Hardy-channel gate. Absence from those searches is not evidence of priority.

## 8. Boundary conditions and falsification tests

1. **Fixed relative probe depth.** The comparison keeps `theta in (0,1)` fixed while `d downarrow0`. If `theta->1` simultaneously, the canonical normalized correlation `sqrt(1-theta^2)` itself vanishes, so (21) is no longer the relevant normalization. Choosing one fixed value such as `theta=1/2` is enough for the barrier.

2. **Uniform ordinate, not uniform depth-free operator families.** Equations (16)--(18) are uniform in `gamma`. They do not cover a family `K_d` whose Calkin/essential behavior changes with `d` and which is not norm precompact. Such a family is a genuine escape only if its scale dependence is independently justified by the zeta source rather than tuned from the unknown defect.

3. **Compactified continuity is the Hartman corollary, not arbitrary continuity on `R`.** A bounded continuous half-plane symbol that fails to extend continuously through the Cayley point at infinity need not lie in the compact Hankel class. The precise criterion is the Cayley pullback of `H^infty+C(T)`.

4. **Noncompact is necessary, not sufficient.** A noncompact operator may still have vanishing matrix elements on the particular boundary-kernel family (13). A viable source must prove a nonzero essential response on those packets and an independent arithmetic upper or sign constraint.

5. **Matched-control scope.** The one-zero block is the exact Kunik inner-factor control required by the line mandate. The argument does not assert that the full zeta logarithmic derivative is a finite Blaschke product. It proves that any proposed proof using only a fixed compact cross-channel correction has no term that can distinguish the full object from an arbitrarily shallow matched defect at leading order.

6. **Multiplicity.** The factor `m^2` cancels from the normalized statement, so repeated right-half zeros do not evade the barrier.

A direct falsification would be a fixed compact cross-channel operator `K` and a sequence `d_n downarrow0`, `gamma_n in R` for which the normalized coefficient in (1) stays bounded away from zero. Equation (16) plus compactness rules this out exactly.

## Consequence for the research line

The broad instruction “try a Hankel/nontranslation-invariant coupling” is now too weak. The first gate is the operator's **essential** class. Fixed smooth localized/decaying symbols generate compact Hankel couplings and are asymptotically invisible relative to the `WI-436` first-defect energy. The surviving corridor is narrower: an independently source-justified noncompact mixed-frequency observable, or a scale family whose loss of compactness is itself forced by arithmetic, with an order-one normalized response on the exact shallow Kunik packets.

This is a barrier, not a defect-to-zero theorem. It removes a large natural subclass of the post-`WI-436` search space while preserving a precise noncompact corridor for further work.