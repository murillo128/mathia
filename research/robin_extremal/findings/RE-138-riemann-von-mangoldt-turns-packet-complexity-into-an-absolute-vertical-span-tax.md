# RE-138 — Riemann–von Mangoldt turns packet complexity into an absolute vertical-span tax

**Status:** `CLASSICAL+DERIVED + EXACT-SPLICE + ACTUAL-ZETA-ZEROS + FINITE-ZERO-EDGE + LEADING-PACKET + RIEMANN-VON-MANGOLDT + TURAN-NAZAROV + SOURCE-SPECIFIC-COMPLEXITY-BOUND + ABSOLUTE-VERTICAL-SPAN + POLYNOMIAL-VISIBILITY-FLOOR + SUPERALGEBRAIC-HIDING-BARRIER + FINITE-ORDER-BUDGET + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-137` removes vertical diameter from the Turán–Nazarov observability cost but leaves packet cardinality as a live escape resource. For a formal spectrum that cardinality can be prescribed independently. For the actual zeta zero set it cannot: Riemann–von Mangoldt bounds the number of zeros available in an absolute ordinate interval.

Splicing the two statements eliminates cardinality from the leading-packet bound. An algebraically strong Robin atom already lies at polynomial height, so a packet of actual zeta zeros with bounded **absolute** vertical span contains only `O(log U)` modes. If its scaled horizontal spread is also `O(log U)`, its leading Robin packet has a fixed polynomial visibility floor relative to the target atom. Hence superalgebraic hiding cannot be achieved inside a bounded absolute vertical band merely by packing more actual zeta zeros there.

More quantitatively, the suppression exponent is controlled by a sum of two geometric resources: scaled horizontal spread divided by `log U`, and absolute vertical span. Thus a superalgebraically hidden strong packet of actual zeta zeros must send one of those resources to infinity. This is stronger than the reciprocal-box escape language of `RE-135`--`RE-136`: the source law upgrades the vertical conclusion from escape beyond every fixed `1/U` box to escape beyond every fixed **ordinate-width** band.

This remains a packet theorem, not a full-residual theorem. Zeros outside the chosen packet may still cancel its visible contribution. Closing that exterior-cancellation step still requires source-specific tail/tightness information.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad
0<\kappa<1,
\qquad
A>0.
\tag{1}
\]

For `K=0`, let `C_U` be any finite multiset of actual positive-ordinate nontrivial zeros of `zeta`, counted with multiplicity, satisfying

\[
\sigma_0\le \Re\rho<\Theta,
\tag{2}
\]

and containing a distinguished zero

\[
\rho_0=\beta_0+i\gamma_0.
\tag{3}
\]

Write

\[
N_U:=\#C_U,
\qquad
H_U:=U\max_{\rho\in C_U}|\Re\rho-\beta_0|,
\qquad
W_U:=\max_{\rho\in C_U}|\Im\rho-\gamma_0|.
\tag{4}
\]

Assume the target atom is algebraically strong,

\[
M_U:=|a_{\rho_0,0}(U)|\ge cU^{-A}
\tag{5}
\]

for some fixed `c>0`. Then

\[
\boxed{
\gamma_0\ll_{A,c,\sigma_0,\Theta} U^{A/2}.
}
\tag{6}
\]

Moreover the actual-zeta source law gives

\[
\boxed{
N_U
\ll_{A,c,\sigma_0,\Theta}
(1+W_U)\bigl(\log U+\log(2+W_U)\bigr).
}
\tag{7}
\]

Combining (7) with `RE-137`, there is a constant `C=C(A,c,sigma_0,Theta,kappa)>0` such that

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,0}(u)|
\ge
M_U
\exp\!\left[
-H_U
-C(1+W_U)\bigl(\log U+\log(2+W_U)\bigr)
\right].
}
\tag{8}
\]

In particular, if

\[
W_U\le W_0,
\qquad
H_U\le h_0\log U
\tag{9}
\]

for fixed `W_0,h_0`, then there is a fixed `B>0` such that

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,0}(u)|
\ge U^{-B}M_U.
}
\tag{10}
\]

So a bounded absolute vertical band and logarithmic scaled horizontal spread rule out superalgebraic relative hiding.

A useful inverse formulation is obtained by defining the relative hiding depth

\[
D_U
:=
\frac1{\log U}
\log_+\!\left(
\frac{M_U}
{\sup_{(1-\kappa)U\le u\le U}|\mathcal S_{C_U,0}(u)|}
\right).
\tag{11}
\]

Then

\[
\boxed{
D_U
\le
\frac{H_U}{\log U}
+C(1+W_U)
\left(
1+\frac{\log(2+W_U)}{\log U}
\right)
+o(1).
}
\tag{12}
\]

Consequently,

\[
\boxed{
D_U\longrightarrow\infty
\quad\Longrightarrow\quad
\frac{H_U}{\log U}\longrightarrow\infty
\ \text{along a subsequence, or}\ 
W_U\longrightarrow\infty
\ \text{along a subsequence}.
}
\tag{13}
\]

The implication in (13) is the source-specific conclusion: once the target atom is algebraically strong, polynomial height is automatic, and Riemann–von Mangoldt converts the abstract complexity escape in `RE-137` into an actual geometric escape in horizontal depth or **absolute** vertical span.

## 1. Algebraic strength already forces polynomial ordinate height

For the leading coefficient,

\[
a_{\rho,0}(U)
=
\frac{e^{-(\Theta-\beta)U}}{\rho(1-\rho)}.
\tag{14}
\]

On the fixed strip in (2),

\[
\Re\bigl(\rho(1-\rho)\bigr)
=
\beta(1-\beta)+\gamma^2
\gg_{\sigma_0,\Theta}1+\gamma^2.
\tag{15}
\]

Hence

\[
|a_{\rho,0}(U)|
\ll_{\sigma_0,\Theta}
\frac1{1+\gamma^2}.
\tag{16}
\]

Applying (16) to `rho_0` and using (5) gives

\[
1+\gamma_0^2\ll U^A,
\tag{17}
\]

which is (6). No independent polynomial-height hypothesis is needed.

The same height implication holds for every fixed finite `K`. Indeed the universal coefficient envelope already used in `RE-133` gives

\[
|a_{\rho,K}(U)|\ll_K(1+\gamma^2)^{-1}
\tag{18}
\]

on the fixed strip. Thus an algebraically strong finite-order target also has `gamma_0 << U^(A/2)`.

## 2. Riemann–von Mangoldt converts absolute vertical span into cardinality

Let `N(T)` count the nontrivial zeros of `zeta` with `0<Im rho<=T`, with multiplicity. The classical Riemann–von Mangoldt law is

\[
N(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi e}
+O(\log(T+2)).
\tag{19}
\]

It implies the uniform local bound

\[
\boxed{
N(t+w)-N(\max\{0,t-w\})
\ll
(1+w)\log(t+w+2)
}
\tag{20}
\]

for `t,w>=0`.

For completeness, if `w<=t/2`, subtracting (19) at the two endpoints makes the main term

\[
O\!\left(w\log(t+2)\right)
\tag{21}
\]

and the two endpoint errors contribute `O(log(t+2))`. If `w>t/2`, then `t+w<3w` and the crude upper bound from (19) gives

\[
N(t+w)\ll w\log(w+2),
\tag{22}
\]

which is again covered by (20).

Every member of `C_U` lies in the ordinate interval

\[
[\gamma_0-W_U,\gamma_0+W_U].
\tag{23}
\]

Therefore (20) gives

\[
N_U
\ll
(1+W_U)\log(\gamma_0+W_U+2).
\tag{24}
\]

Using (6),

\[
\log(\gamma_0+W_U+2)
\ll_A
\log U+\log(2+W_U),
\tag{25}
\]

and (7) follows.

Several points are worth making explicit. The estimate counts multiplicity, so no simplicity assumption is being smuggled in. `C_U` may be only a selected right-half-strip subset of the zeros in (23); bounding it by the total zero count only strengthens (24). Functional-equation pairing is therefore not needed for the order of magnitude, although it could improve constants for a purely off-critical right-half packet.

## 3. Turán–Nazarov eliminates cardinality from the leading-packet bound

`RE-137` proves, with constants depending only on the fixed strip and on `kappa`, that every finite leading packet satisfies

\[
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,0}(u)|
\ge
c_{\Theta,\kappa}
\exp[-H_U-C_\kappa N_U]
M_U.
\tag{26}
\]

Insert (7). After enlarging constants and absorbing the fixed prefactor, this becomes exactly (8).

This is the useful source splice. In `RE-137`, cardinality was an independent formal resource. For actual zeta zeros it is bounded by the number of zeros that physically fit in the ordinate interval. At algebraically relevant Robin height, that number grows only logarithmically in `U` per unit of absolute vertical span.

If `W_U<=W_0` and `H_U<=h_0 log U`, then (8) gives

\[
\sup|\mathcal S_{C_U,0}|
\ge
M_U\exp[-O(\log U)]
\ge
U^{-B}M_U
\tag{27}
\]

for a fixed `B`, proving (10). Taking logarithms in (8) gives (12).

To verify (13), suppose instead that both `H_U/log U` and `W_U` remain bounded along a subsequence. Then the right-hand side of (12) remains bounded there, contradicting `D_U->infinity`. Thus superalgebraic relative hiding must escape one of the two source-controlled geometric resources.

## 4. Finite-order transfer has an explicit source budget

For fixed `K>=0`, let `rho_0` maximize `|a_(rho,K)(U)|` on `C_U` and suppose

\[
M_{K,U}:=|a_{\rho_0,K}(U)|\ge cU^{-A}.
\tag{28}
\]

Equation (18) again gives polynomial target height, so (7) remains valid with constants depending on `K` as well.

The finite-order stability theorem in `RE-137` says that, when `kappa A<1`, the leading Turán signal survives provided

\[
(1+\kappa)H_U
+C_1(\kappa)N_U
+\log(N_U+1)
\le
(1-\kappa A-\eta)\log U
\tag{29}
\]

for some fixed `eta>0`. Substituting (7), a source-only sufficient condition is

\[
\begin{aligned}
(1+\kappa)H_U
&+C_2(1+W_U)
\bigl(\log U+\log(2+W_U)\bigr)
\\
&+O\!\left(
\log\bigl((2+W_U)\log U\bigr)
\right)
\le
(1-\kappa A-\eta)\log U,
\end{aligned}
\tag{30}
\]

with `C_2=C_2(A,K,kappa,c,sigma_0,Theta)`. Whenever (30) holds,

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,K}(u)|
\ge
c_{K,\Theta,\kappa}
\exp[-H_U-C_\kappa N_U]M_{K,U},
}
\tag{31}
\]

and (7) may again be inserted on the right.

This finite-order statement is deliberately conditional on the stability budget. The classical zero count alone gives `N_U=O(log U)` in a bounded vertical band, but the hidden constant need not be small enough to satisfy (29) for an arbitrary algebraic strength exponent `A`. The unconditional clean conclusion of this finding is therefore the leading-packet theorem (8)--(13), not a claim that every finite-order packet in every bounded band is visible at a prescribed polynomial exponent.

## 5. What this closes, and what it does not

`RE-135` showed that growing cardinality cannot hide a packet inside a fixed reciprocal box. `RE-136` quantified the isotropic escape cost and found the sharp `exp(-O(R))` law. `RE-137` then showed that vertical diameter itself is absent from leading-order observability: hiding pays in horizontal spread or cardinality.

The present source splice resolves the next ambiguity for actual zeta zeros. Cardinality cannot grow freely inside a bounded absolute ordinate band. An algebraically strong packet in such a band has only `O(log U)` available zeros, so the Turán loss is only polynomial in `U`. Therefore a **superalgebraically** hidden leading packet cannot remain simultaneously bounded in absolute vertical span and logarithmic in scaled horizontal spread.

This does **not** rule out ordinary algebraic relative hiding. The Riemann–von Mangoldt error term permits `O(log U)` zeros in a bounded interval, and feeding that into Turán–Nazarov gives only a polynomial floor. Nothing here improves that to a fixed positive fraction of `M_U`. In particular, this finding does not prove the reciprocal-scale tightness required to close the full Robin mechanism.

It also does not control cancellation from zeros outside `C_U`. A local packet can be visible while the complete strict-subedge sum is small because an exterior packet cancels it. Any global use therefore still needs a decomposition for which the exterior contribution is controlled, or a source theorem that constrains the full relevant packet at once.

Finally, no simplicity, pair-correlation, minimum-spacing, or RH assumption is used. The only source-specific input added to `RE-137` is the classical zero-counting law (19), together with the elementary fact that algebraic Robin strength forces polynomial ordinate height.

## 6. Adversarial stress test

**Could a multiple zero defeat the count?** No. `N(T)` counts zeros with multiplicity, and Turán–Nazarov in `RE-137` was stated for finite multisets. Multiplicity consumes cardinality budget rather than evading it.

**Could the target sit at superpolynomial height?** Not if it is algebraically strong. Equations (14)--(17) force `gamma_0=O(U^(A/2))`. This is not an external height assumption.

**Could a packet with tiny reciprocal-scale width still contain many zeros?** It may contain as many as `O(log U)` under the unconditional pointwise source law. That is exactly why the conclusion is a polynomial visibility floor rather than a fixed-relative floor. The theorem does not silently assume typical zero spacing.

**Could large vertical diameter invalidate Turán–Nazarov?** No; `RE-137` is independent of vertical diameter. Large `W_U` enters only through the source-side zero count. This separation is the point of the splice.

**Does (13) say vertical span alone must diverge?** No. Superalgebraic hiding may instead pay with `H_U/log U->infinity`. The conclusion is a genuine alternative, not a vertical-spacing theorem.

**Does a visible local packet make the full Robin residual visible?** No. Exterior cancellation is untouched. Treating (8) as a theorem about the complete subedge residual would be an invalid scope enlargement.

**Can the finite-`K` correction always be absorbed?** No. Section 4 keeps the exact stability budget from `RE-137`; no stronger finite-order conclusion is claimed.

## 7. Representation and prior-art audit

The cardinality elimination is representation-invariant at the source level: `N_U` is bounded by the actual number of zeta zeros in an ordinate interval, counted with multiplicity. The geometric quantities `H_U` and `W_U` are attached directly to zero coordinates and are not artifacts of choosing a basis for the exponential polynomial. The Turán step itself remains the same leading-packet representation audited in `RE-137`.

The ingredients are classical individually. Riemann–von Mangoldt gives (19)--(20), and Turán–Nazarov gives the propagation-of-smallness input already anchored for `RE-137`. The closest short-interval zero literature studies sharper counts, gaps, or averaged/conditional statistics; none is needed here. A current explicit improvement of the `O(log T)` error would change constants in (7) but not the qualitative span tax or the polynomial-vs-superalgebraic boundary.

The derived content is the Robin-specific splice: algebraic coefficient strength first makes polynomial height automatic, the actual-zeta count then converts packet cardinality into absolute vertical span, and `RE-137` turns that source bound into the hiding-depth inequality (12). No new external theorem beyond source material already used in this line is load-bearing, so `SOURCES.md` is unchanged.

## 8. Next frontier

The remaining gap is now sharper. To exclude even ordinary `o(M_U)` hiding, one needs more than the pointwise Riemann–von Mangoldt budget because `O(log U)` local complexity still permits a Turán floor tending to zero as a power of `U`. A genuinely stronger source input would have to control the **relevant off-critical packet**, not merely the total zero count: for example an `o(log U)` or bounded effective-complexity statement in the target-bearing band, a coefficient-weighted local count, or an exterior-tail theorem that prevents a polynomially visible packet from being cancelled by mass outside the band.

Conversely, any future matched control for actual-source plausibility should now report three resources separately: relative suppression depth, scaled horizontal spread, and absolute vertical span. Treating vertical displacement only in reciprocal units is no longer sufficient once the zeta zero-count law is imposed.