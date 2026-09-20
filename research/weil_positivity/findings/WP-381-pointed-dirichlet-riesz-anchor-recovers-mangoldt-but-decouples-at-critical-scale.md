---
id: WP-381
title: Pointed Dirichlet Riesz anchor recovers Mangoldt but decouples at critical scale
branch: weil_positivity
status: supported
kind: pointed-dirichlet-finite-global-incidence-scaling-obstruction
claim_strength: exact RH-independent identification of the unique bounded pointed-Dirichlet Riesz anchor for the cyclotomic endpoint functional, yielding the critical Weil finite coefficient Lambda(n)/sqrt(n) as a canonical positive-Gram cross term; the coupling vanishes on every unbounded prime-power sequence, and any scalar amplification that keeps it nonzero forces the anchor energy to diverge
created: 2026-09-20
related: [WP-071, WP-072, WP-073, WP-161, WP-162, WP-168, WP-374, WP-375, WP-378, WP-379, WP-380]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical local Dirichlet spaces at a boundary point
  - classical Hardy H2 reproducing-kernel evaluation at zero
  - classical cyclotomic identity Phi_n(1)=p for prime powers and 1 otherwise
  - classical von Mangoldt finite-prime coefficient
---

# WP-381 — Pointed Dirichlet Riesz anchor recovers Mangoldt but decouples at critical scale

## Claim

The pointed local Dirichlet geometry used in `WP-072`, `WP-168`, `WP-379`, and `WP-380` contains a canonical bounded finite--global incidence that is stronger than the bulk-Gram information isolated there.

For

\[
D_1(F,G)
:=\left\langle
T_1F,T_1G
\right\rangle_{H^2},
\qquad
T_1F(z):=\frac{F(z)-F(1)}{z-1},
\tag{1}
\]

let

\[
e(z):=z-1.
\tag{2}
\]

Then `T_1e=1`, so `D_1(e)=1`. More importantly,

\[
\boxed{
D_1(F,e)=F(1)-F(0).
}
\tag{3}
\]

Thus `e` is the unit Riesz representer, in the pointed Dirichlet quotient by constants, of the endpoint-difference functional `F -> F(1)-F(0)`. It is not fitted to primes or to zeta data: it is forced by the distinguished boundary point `1` already present in the definition of `D_1` and by the Hardy constant vector.

For the primitive cyclotomic logarithmic shell

\[
F_n(z):=\log\Phi_n(z),\qquad n>1,
\tag{4}
\]

using the analytic branch with `F_n(0)=0`, the classical value of the cyclotomic polynomial at `1` gives

\[
F_n(1)=\log\Phi_n(1)=\Lambda(n).
\tag{5}
\]

Consequently, under the critical half-density normalization forced by `WP-073`,

\[
W_n:=n^{-1/2}F_n,
\tag{6}
\]

one has the exact identity

\[
\boxed{
D_1(W_n,e)=\frac{\Lambda(n)}{\sqrt n}.
}
\tag{7}
\]

This is precisely the arithmetic coefficient scale appearing in the finite-prime side of a Weil explicit formula at the critical line. Therefore the pointed geometry does **not** lose the Mangoldt selector at finite scale: it converts the formerly unbounded ambient `H^2` boundary trace of `WP-378` into a canonical bounded cross term.

The escape nevertheless fails at the next required gate. Along every unbounded prime-power sequence,

\[
\frac{\Lambda(n)}{\sqrt n}\longrightarrow0,
\tag{8}
\]

while `D_1(e)=1` and the critical shell bulk remains nontrivial. Hence the canonical finite--global incidence block-diagonalizes in the critical limit. If the anchor is rescaled to `a_ne` and one requires

\[
|D_1(W_n,a_ne)|\ge \delta>0
\tag{9}
\]

on an unbounded prime-power sequence, then necessarily

\[
|a_n|\ge
\delta\frac{\sqrt n}{\Lambda(n)},
\qquad
D_1(a_ne)=|a_n|^2
\ge
\delta^2\frac{n}{\Lambda(n)^2}
\longrightarrow\infty.
\tag{10}
\]

So the exact bounded Riesz anchor provides the right finite coefficient but cannot retain a nonvanishing critical coupling inside a fixed finite-energy global sector. Amplifying it enough to survive moves the divergence into the global energy rather than producing the missing archimedean counterterm.

## 1. The endpoint functional is already internal to the pointed metric

Equation (3) is elementary but structurally important. Evaluating (1) at zero gives

\[
(T_1F)(0)
=\frac{F(0)-F(1)}{-1}
=F(1)-F(0).
\tag{11}
\]

Since `T_1e=1`, the Hardy inner product with the constant function extracts exactly that constant coefficient:

\[
D_1(F,e)
=\langle T_1F,1\rangle_{H^2}
=(T_1F)(0).
\tag{12}
\]

Evaluation at zero is a bounded functional of norm one on `H^2`, with Riesz vector `1`. Because `T_1` identifies the pointed Dirichlet quotient by constants with its Hardy image, `e=z-1` is the corresponding canonical unit representer modulo the null constants of `D_1`.

This matters for the interpretation of the preceding no-go chain. In the unpointed `H^2` topology of `WP-378`, the arithmetic value `F_n(1)` is genuinely an unbounded boundary trace. After passing to the source-forced pointed metric, the same arithmetic value is no longer external or singular: for shells satisfying `F_n(0)=0`, it is an ordinary bounded coordinate of the positive Hilbert geometry.

That does not contradict `WP-379` or `WP-380`. Those findings show that after critical normalization the nondegenerate **bulk shell Gram** becomes degree-universal or asymptotically forgets primitive factorization. Equation (7) identifies an additional bounded coordinate whose exact support remains arithmetic at every finite `n`, but whose magnitude tends to zero on the same critical scale.

## 2. Cyclotomic shells give the exact Mangoldt coefficient

For every `n>1`, `Phi_n(0)=1`, hence the analytic logarithm in (4) satisfies

\[
F_n(0)=0.
\tag{13}
\]

The classical endpoint identity is

\[
\Phi_n(1)=
\begin{cases}
p,&n=p^k,\\
1,&n\text{ has at least two distinct prime factors},
\end{cases}
\tag{14}
\]

so

\[
\log\Phi_n(1)=\Lambda(n).
\tag{15}
\]

Combining (3), (13), and (15) proves

\[
D_1(F_n,e)=\Lambda(n),
\tag{16}
\]

and then (7) follows from (6).

The smallest matched control is exact. For a prime `p`,

\[
D_1(W_p,e)=\frac{\log p}{\sqrt p}>0,
\tag{17}
\]

whereas for `n=6`, or any non-prime-power shell,

\[
D_1(W_n,e)=0.
\tag{18}
\]

At the same time `W_6` has nonzero pointed bulk norm. The anchor therefore sees exactly the arithmetic support that the positive bulk energy itself fails to isolate. The effect is not a numerical prime/composite proxy and does not arise from a fitted kernel.

## 3. A positive completion contains the finite prime sum as a cross term

For any finite shell combination

\[
X=\sum_{n>1}c_nW_n,
\tag{19}
\]

linearity of (7) gives

\[
D_1(X,e)
=\sum_{n>1}c_n\frac{\Lambda(n)}{\sqrt n}.
\tag{20}
\]

Therefore the independently positive pointed energy

\[
D_1(X-te)
= D_1(X)
-2\operatorname{Re}\!\left(
\overline t\sum_{n>1}c_n\frac{\Lambda(n)}{\sqrt n}
\right)
+|t|^2
\ge0
\tag{21}
\]

contains the exact critical Mangoldt-weighted finite sum as its mixed term.

This is the strongest part of the route: the finite coefficient is generated by a canonical positive Gram completion, rather than inserted as a zero spectrum, a zeta determinant, an RH-equivalent positivity functional, or an arbitrary regularization. If the coefficients `c_n` are supplied by a test-function sampling map, (20) has the correct coefficient-level arithmetic normalization for the finite explicit-formula contribution.

But equation (21) is **not** a Weil positivity theorem. The geometry has not derived the required test-function map, `D_1(X)` is the pointed cyclotomic bulk Gram already shown by `WP-379`/`WP-380` to have the wrong matched-control behavior, and `|t|^2` is only a one-dimensional positive counterterm. No Gamma factor, polar term, real-place measure, or global cohomological/intersection theorem has appeared.

## 4. Critical scaling kills the bounded finite--global incidence

The exact support in (7) might suggest retaining the anchor as the real-place component. The critical normalization blocks the simplest version of that idea.

For `n=p^k`,

\[
0<\frac{\Lambda(n)}{\sqrt n}
=\frac{\log p}{p^{k/2}}
\le \frac{\log n}{\sqrt n}
\longrightarrow0
\tag{22}
\]

as `n->infinity`. Thus the augmented two-by-two Gram

\[
\begin{pmatrix}
D_1(W_n)&D_1(W_n,e)\\
D_1(e,W_n)&1
\end{pmatrix}
\tag{23}
\]

loses its arithmetic off-diagonal entry on every unbounded prime-power family. On non-prime-powers that entry is already exactly zero. The fixed unit anchor therefore preserves the selector only as a vanishing finite-scale coordinate.

The scalar-amplification obstruction (10) is exact and requires no prime-distribution input. If a rescaled copy `a_ne` is required to keep the prime-power cross term uniformly away from zero, its positive self-energy must diverge at least like `n/Lambda(n)^2`. Normalizing that anchor back to bounded energy returns the vanishing coupling.

This rules out a particularly natural interpretation of the pointed escape: the critical finite term cannot be maintained as an order-one incidence with a **fixed bounded-energy one-dimensional global anchor**. An `n`-dependent amplification can of course be written, but absent a separate source geometry producing both that divergence and its compensating archimedean term, it is exactly the kind of hand-chosen renormalization excluded by the research mandate.

## 5. Adversarial controls and scope

Several tempting stronger conclusions do not follow.

First, (7) does not contradict the critical shell-collapse theorem of `WP-380`: continuity only requires the difference of the anchor coordinates to tend to zero when the shell vectors approach one another, and `log p/sqrt(p)->0` does exactly that. The new point is finite-scale exactness and its canonical Riesz realization, not a surviving asymptotic separation.

Second, positivity of the anchor energy alone gives a square such as `|sum c_n Lambda(n)/sqrt(n)|^2`; it does not reproduce the linear finite term by itself. The linear term appears only by polarization/cross term in (21), together with the bulk and global self-energies. Those remaining terms must be identified from the same geometry before any Weil interpretation is justified.

Third, nothing here rules out an infinite-dimensional real-place sector, a source-forced varying family of global states, an indefinite intermediate coupling followed by a genuine global sign theorem, or a topology in which finite and archimedean components are assembled before the critical limit. The result only closes the fixed bounded Riesz-anchor completion and quantifies the cost of the obvious scalar rescue.

Fourth, the arithmetic content is already present in the cyclotomic shell through the classical identity (14). The result does not claim that local Dirichlet geometry discovers primes from featureless data. Its substantive content is representation-theoretic: the pointed transform converts that source arithmetic into a bounded canonical positive-Gram incidence with exactly the critical finite Weil scaling, and the same calculation proves why that incidence disappears in the critical bounded-energy limit.

## 6. Prior-art and novelty audit

All ingredients separately are classical. The value `Phi_n(1)` is the standard cyclotomic characterization of prime powers; `Lambda(n)` is the classical von Mangoldt coefficient; evaluation at zero is the elementary reproducing-kernel functional of `H^2`; and local Dirichlet spaces at a boundary point are established function-space constructions. A bounded literature search did not locate a source using the particular cyclotomic pointed-Dirichlet Riesz identity (7) as a finite--archimedean Weil-positivity mechanism.

No broad literature novelty is claimed. Relative to the Mathia line, however, the result changes the search boundary left by `WP-378`--`WP-380`. The exact Mangoldt selector need not remain a singular boundary operation once the canonical pointed topology is adopted: it is already a bounded unit-anchor cross term. The obstruction is more specific and more informative. The correct finite coefficient is present, but **critical scale separation** sends its coupling to zero; rescuing it by scalar amplification makes the positive global self-energy diverge.

This is distinct from classical Weil positivity, Hilbert--Polya, Connes/trace, Frobenius/cohomology, Sonin/localization, or an intersection-form proof. There is no zero data and no RH-equivalent sign functional. Conversely, there is also no Gamma/polar completion and no global sign theorem, so the finding must not be promoted into evidence for RH.

## Consequence for the research line

The pointed Prime-Circle route should no longer be described as forcing a choice between a positive bulk and an intrinsically singular Mangoldt boundary trace. Its own local Dirichlet geometry contains a canonical bounded bridge:

\[
W_n\ \longleftrightarrow\ e=z-1
\qquad\text{with incidence}\qquad
\frac{\Lambda(n)}{\sqrt n}.
\tag{24}
\]

That is a genuine narrowing improvement because it identifies the first source-forced noncharacter incidence in this analytic-disk route whose finite coefficient has exactly the critical Weil scale and exact prime-power support.

The bridge nevertheless fails the global gate in its minimal form. Its coupling vanishes precisely in the critical regime where the bulk geometry stays nondegenerate, and keeping the coupling order one forces divergent anchor energy. The next useful test is therefore **not another bounded scalar anchor**. It is whether the source geometry supplies a real-place family or global boundary response whose own norm/counterterm has the required divergent scale and whose renormalized finite--archimedean assembly produces the Gamma/polar terms before positivity is taken. Without that independent source mechanism, multiplying `e` by `sqrt(n)/Lambda(n)` or an equivalent compensator is merely inserting the desired normalization by hand.

## Conclusion

The canonical pointed Dirichlet metric does contain more arithmetic than its critical bulk Gram suggests. The unit vector `e=z-1` is the Riesz anchor for endpoint difference, and primitive cyclotomic shells satisfy the exact identity

\[
D_1(n^{-1/2}\log\Phi_n,e)
=\frac{\Lambda(n)}{\sqrt n}.
\]

This gives a genuine positive-Gram realization of the finite critical Mangoldt coefficient and exact matched-control support. But it is a finite-scale bridge, not yet a global Weil form: the coupling tends to zero along every unbounded prime-power sequence, while any scalar amplification that prevents that decay makes the anchor energy diverge. The surviving question is whether Mathia itself forces an archimedean/global sector whose geometry supplies exactly that missing scale and counterterm, rather than adding it by normalization choice.
