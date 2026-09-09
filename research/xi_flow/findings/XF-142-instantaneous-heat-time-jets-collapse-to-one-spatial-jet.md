# XF-142 — instantaneous heat-time jets collapse to one spatial jet

**Status:** `EXACT-DERIVED` + `STRUCTURAL/JET-EQUIVALENCE` + `TARGET-GENERAL` + `INSTANTANEOUS-OBSERVABILITY` + `CROSS-SCALE` + `CORRECTION-OF-INFORMATION-COUNT`. XF-141 shows that the transition-sharp central packet can match exactly every mixed derivative with `2p+q<N-2` at one observation slice. The stronger structural fact is that, for the periodic coefficient heat flow itself, those time derivatives are never independent coordinates at a fixed slice. After an explicit universal gauge, the local trace satisfies the ordinary one-dimensional heat equation, so every mixed parabolic derivative is exactly a rescaled pure spatial derivative. The quadratic coordinate count in XF-141 is therefore correct as a list of entries but not as an information count.

## Result / observations

Let

\[
E(w,s)=\sum_{k=0}^N E_k(0)e^{-a k(N-k)s}w^k,
\qquad a>0,
\tag{1}
\]

be any degree-`N` polynomial evolving under the exact periodic coefficient heat flow, with no assumption on its roots. In the XF-130--XF-141 logarithmic radial coordinate define

\[
Q(\beta,s):=E(-e^{\beta/N},s).
\tag{2}
\]

Then `Q` satisfies the constant-coefficient PDE

\[
\boxed{
\partial_sQ
=aN^2(\partial_\beta^2-\partial_\beta)Q.
}
\tag{3}
\]

Equivalently, the universal gauge

\[
\boxed{
\widehat Q(\beta,s)
:=e^{aN^2s/4-\beta/2}Q(\beta,s)
}
\tag{4}
\]

satisfies the ordinary heat equation

\[
\boxed{
\partial_s\widehat Q
=aN^2\partial_\beta^2\widehat Q.
}
\tag{5}
\]

Hence, at every space-time point and for every `p,q>=0`,

\[
\boxed{
(aN^2)^{-p}
\partial_s^p\partial_\beta^q\widehat Q
=
\partial_\beta^{2p+q}\widehat Q.
}
\tag{6}
\]

This gives an exact finite-jet equivalence. For an integer `K>=0`, let

\[
J_K^{\rm par}(Q)
:=
\left\{
\partial_s^p\partial_\beta^qQ:
2p+q\le K
\right\},
\qquad
J_K^{\rm sp}(Q)
:=
\left\{
\partial_\beta^mQ:
0\le m\le K
\right\}.
\tag{7}
\]

At a fixed observation point `(beta_0,s_0)`, the two data sets carry exactly the same information:

\[
\boxed{
J_K^{\rm par}(Q_1)=J_K^{\rm par}(Q_2)
\iff
J_K^{\rm sp}(Q_1)=J_K^{\rm sp}(Q_2)
}
\tag{8}
\]

for any two traces governed by the same `N` and `a`. More generally, every functional of the complete mixed parabolic `K`-jet can be rewritten as a functional of the pure spatial `K`-jet at that same slice. Time derivatives do not create a new instantaneous observation axis; they only repackage spatial derivatives already forced by the PDE.

The statement also holds for logarithmic jets wherever `Q!=0`. Writing `L=log Q`, equation `(3)` gives

\[
\boxed{
\partial_sL
=aN^2\left(
\partial_\beta^2L
+(\partial_\beta L)^2
-\partial_\beta L
\right).
}
\tag{9}
\]

Repeated differentiation shows that every mixed derivative `partial_s^p partial_beta^q L` is a universal differential polynomial in the spatial derivatives `partial_beta^m L` with `m<=2p+q`. Since the `p=0` entries are already present, the logarithmic mixed parabolic `K`-jet and the logarithmic spatial `K`-jet are again equivalent. Dividing both controls by the same known nonvanishing analytic reference does not change this conclusion: the reference contributes the same known jet to both sides.

## Derivation

On the `k`-th monomial of `(2)`, differentiation in `beta` acts diagonally:

\[
\partial_\beta
\left[E_k(s)(-e^{\beta/N})^k\right]
=
\frac{k}{N}
E_k(s)(-e^{\beta/N})^k.
\tag{10}
\]

Therefore

\[
N^2(\partial_\beta-\partial_\beta^2)
\left[E_k(s)(-e^{\beta/N})^k\right]
=
k(N-k)
E_k(s)(-e^{\beta/N})^k.
\tag{11}
\]

Comparing `(11)` with `partial_s E_k=-a k(N-k)E_k` proves `(3)` coefficientwise. No root condition, asymptotic estimate, or local approximation is involved.

The gauge `(4)` is the exact completion of the square for the drift operator. If `Q=e^{\beta/2-aN^2s/4}\widehat Q`, then

\[
(\partial_\beta^2-\partial_\beta)Q
=
e^{\beta/2-aN^2s/4}
\left(
\partial_\beta^2\widehat Q
-\frac14\widehat Q
\right),
\tag{12}
\]

and the `-aN^2/4` term from differentiating the time gauge cancels the potential in `(12)`. This proves `(5)`. Since `partial_s` and `partial_beta` commute, iteration immediately gives `(6)`.

If one prefers to stay in the ungauged trace, `(3)` yields the explicit formula

\[
\boxed{
\partial_s^p\partial_\beta^qQ
=(aN^2)^p
\sum_{j=0}^p
(-1)^{p-j}\binom pj
\partial_\beta^{q+p+j}Q.
}
\tag{13}
\]

Every spatial order on the right lies between `q+p` and `q+2p`. Thus whenever `2p+q<=K`, equation `(13)` uses only the spatial `K`-jet. This proves the forward implication in `(8)`, while the reverse implication is immediate because `p=0` is part of `J_K^par`.

The first two cases make the structure transparent:

\[
\partial_s\partial_\beta^qQ
=aN^2
\left(
\partial_\beta^{q+2}Q-
\partial_\beta^{q+1}Q
\right),
\tag{14}
\]

and

\[
\partial_s^2\partial_\beta^qQ
=(aN^2)^2
\left(
\partial_\beta^{q+4}Q
-2\partial_\beta^{q+3}Q
+\partial_\beta^{q+2}Q
\right).
\tag{15}
\]

Thus the natural parabolic weight `2p+q` in XF-141 is not merely suggested by the quadratic heat spectrum. It is the exact differential order induced by the generator.

For logarithms, `(9)` follows by dividing `(3)` by `Q` and using `Q_beta/Q=L_beta` and `Q_betabeta/Q=L_betabeta+L_beta^2`. Applying `partial_s` recursively and replacing every new `L_s` by `(9)` gives a differential polynomial whose maximal spatial derivative rises by exactly two per time derivative. This proves the logarithmic version of the same finite-jet reduction.

## Application to XF-141

The transition-slice identity in XF-141 is

\[
t_*\Delta Q_\beta(0)
=-2(-1)^{M+r}e^{\beta/2}
\sinh^{2r}\!\left(\frac{\beta}{2N}\right).
\tag{16}
\]

Consequently the two matched controls already have identical pure spatial derivatives through order `2r-1` at `(beta,s)=(0,0)`. By `(8)`, this alone implies

\[
\partial_s^p\partial_\beta^qQ_1(0,0)
=
\partial_s^p\partial_\beta^qQ_{\lambda_{r,\rho}}(0,0)
\qquad
(2p+q<2r),
\tag{17}
\]

and likewise for their logarithms. The two-variable barycentric moment calculation in XF-141 remains correct, but it is not needed to establish the mixed-jet vanishing: once the pure spatial contact in `(16)` is known, the PDE forces every lower parabolic coordinate to vanish automatically.

The same observation explains the sharp boundary. After the gauge `(4)`, the packet difference at `s=0` is a nonzero constant times

\[
\sinh^{2r}\!\left(\frac{\beta}{2N}\right),
\tag{18}
\]

whose first nonzero spatial derivative has order exactly `2r`. Equation `(6)` then shows that every boundary derivative with `2p+q=2r` is a known nonzero multiple of that same single spatial derivative. The entire first nonzero parabolic layer is one underlying spatial coefficient seen through different PDE-compatible coordinates.

At maximal depth `r=M-1`, XF-141 lists

\[
r(r+1)=\frac{N^2}{4}-\frac N2
\tag{19}
\]

mixed coordinates satisfying `2p+q<N-2`. Equation `(8)` shows that these are generated by only

\[
\boxed{2r=N-2}
\tag{20}
\]

pure spatial jet entries, namely orders `0,...,2r-1`. Thus `(19)` is a valid coordinate count but **not** an intrinsic information dimension. The apparent quadratic enlargement obtained by appending time derivatives at one slice is universally redundant.

## Checks / falsifier

A coefficientwise falsifier is immediate. Take a single mode

\[
Q_k(\beta,s)
=C\exp\!\left(
\frac{k}{N}\beta-a k(N-k)s
\right).
\tag{21}
\]

Then the right side of `(3)` equals

\[
aN^2\left[
\left(\frac{k}{N}\right)^2-
\frac{k}{N}
\right]Q_k
=-a k(N-k)Q_k
=\partial_sQ_k,
\tag{22}
\]

so the generator identity holds on every basis mode and hence on every polynomial trace. Equations `(14)` and `(15)` are direct low-order expansions of the same identity.

A falsifier of the jet-equivalence claim would therefore have to produce two solutions of the same coefficient heat flow whose spatial derivatives agree through order `K` at a point but some mixed derivative with `2p+q<=K` differs there. Formula `(13)` excludes this exactly. For logarithmic jets, the only additional hypothesis is local nonvanishing so that an analytic logarithm exists.

The theorem is deliberately instantaneous. Values at two distinct heat times are not forced by the spatial jet at only one of those times unless one knows an infinite analytic germ with sufficient control. Likewise, moving to a second spatial center supplies another spatial jet and can add information. The reduction says only that **time differentiation at a fixed slice and center is not an independent source of finite-order data**.

## Relation to prior work

The space-time jet correspondence for the ordinary heat equation is classical. A directed prior-art audit found an especially explicit neighboring formulation in Camille Laurent and Lionel Rosier, *Exact controllability of semilinear heat equations in spaces of analytic functions*, Ann. Inst. H. Poincare Anal. Non Lineaire 37 (2020), Section 3. In the linear heat case they record `partial_t^n y=partial_x^(2n)y` and the corresponding relation with one additional spatial derivative, then extend the idea to a semilinear equation. That is precisely the classical structural phenomenon exposed here after the gauge `(4)`.

No external theorem is load-bearing for XF-142. The periodic trace identity `(3)` follows directly from the internal coefficient flow, and the gauge `(4)` reduces it algebraically to the standard heat equation. The new research delta is therefore not a new PDE theorem in isolation; it is the consequence for the Xi-flow observability program: the instantaneous mixed heat jets introduced in XF-141 collapse to the same local spatial information class and cannot constitute a distinct repair of the matched-control obstruction. `SOURCES.md` therefore needs no new dependency anchor.

## Implications for the Xi-flow frontier

XF-141 left several nominal exits from its exact matched parabolic jet, including a genuinely positive heat-time interval, a different spatial center or shell, a nonlocal transform, and an Xi-specific restriction excluding the central packet. XF-142 removes one ambiguity from that list: **higher time derivatives at the same instantaneous slice are not a fifth route**. At any finite parabolic order they are generated by the spatial jet through the exact PDE compatibility relations.

This also changes how future negative results should be counted. A statement that matches `Theta(N^2)` mixed derivatives at one point may still represent only `Theta(N)` independent local data when those derivatives lie under a parabolic-order cutoff. Conversely, a positive criterion should not claim extra information merely from the number of space-time derivative coordinates unless it explicitly breaks the PDE compatibility, for example by sampling a nonzero time interval or by combining distinct spatial centers.

For the Gaussian/reference quotient clue, the consequence is neutral but clarifying. A common nonvanishing reference can improve source localization or normalization, but at a single slice it cannot turn time derivatives into new independent coordinates: subtracting the same reference log-jet preserves the equivalence. The clue therefore remains open at its current accepted status rather than being strengthened or closed by XF-142.

## Uncertainties / scope

The result is target-general for the finite periodic coefficient heat model but does not itself say which spatial jets are accessible from the true Xi source. It is an algebraic information-equivalence statement, not a stability theorem. The conversion coefficients in `(13)` contain powers of `aN^2`, so raw numerical conditioning can differ dramatically between spatial and temporal coordinates even though exact identifiability does not.

Nor does the theorem collapse a positive-time trace to a finite spatial jet. Analytic continuation in time may encode arbitrarily high spatial derivatives, and the degree-`N` polynomial state can ultimately be identifiable from sufficiently rich history as in XF-130. The point is narrower and exact: at one slice, finite mixed differentiation cannot escape the finite spatial Taylor ideal forced by the heat generator.

## Conclusion

The periodic logarithmic radial trace has a hidden simplification:

\[
\widehat Q=e^{aN^2s/4-\beta/2}Q
\quad\Longrightarrow\quad
\partial_s\widehat Q=aN^2\partial_\beta^2\widehat Q.
\]

Therefore a mixed derivative of parabolic order `2p+q` is exactly a spatial derivative of that same order after a known gauge. The complete instantaneous parabolic `K`-jet and the spatial `K`-jet are information-equivalent for every periodic target, not just for the central matched packet. In particular, XF-141's nearly quadratic family of equal mixed coordinates is generated by only a linear-size spatial jet. Any materially new Xi-flow observer must leave that one-slice differential algebra rather than append more time derivatives to it.