# RE-011 — clean self-tangent selection forces a mixed-race value-slope law

**Status:** `EXACT-DERIVED + CONTINUOUS-MIXED-RACE-INTERPOLATION + SELF-TANGENT-DIFFERENTIAL-LAW + VALUE-SLOPE-SELECTION + ROBIN-HEIGHT-COUPLING + PRIOR-ART-BOUNDED`. `RE-009` identifies the square-root-normalized endpoint-subtracted Mertens remainder with the classical mixed reciprocal/standard prime-race coordinate, while `RE-010` proves that its value at the boundary of a clean self-tangent CA peak controls the Robin sign through the threshold `2 sqrt(2)`. The same source geometry imposes a second constraint that is invisible in the value threshold alone. The exact endpoint subtraction makes the underlying mixed remainder **continuous across every ordinary prime**, so it has a canonical smooth interpolation on the prime-free interval containing the intrinsic self-tangent coordinate. At that coordinate, self-tangency fixes its derivative.

For real `x>=2`, put

\[
E(x):=\sum_{r\le x}-\log(1-r^{-1})-\gamma-\log\log x,
\qquad
\Delta(x):=\vartheta(x)-x,
\]

\[
h(x):=\frac{-\log(1-x^{-1})}{\log x},
\qquad
k(x):=\frac1{x\log x},
\]

and extend the `RE-008` remainder to real input by

\[
\mathcal M_*(x):=E(x)-\Delta(x)h(x).
\tag{1}
\]

Define its Robin-scale normalization

\[
s(x):=\sqrt x\log x,
\qquad
\mathscr Y(x):=s(x)\mathcal M_*(x).
\tag{2}
\]

Let `C` run through any unbounded sequence of sufficiently large **clean regular self-tangent CA local peaks**, put `X=log C`, and let `p<X<q` be the consecutive first-layer boundary primes of `RE-006`. Then `mathscr Y` is differentiable at `X` and the CA selection law forces

\[
\boxed{
X\mathscr Y'(X)
=\left(\frac12+\frac1{\log X}\right)\mathscr Y(X)
-\sqrt2+o(1).
}
\tag{3}
\]

Thus clean self-tangent selection does not merely choose **where** the mixed prime race is sampled. It constrains the selected pair consisting of its value and its local logarithmic slope.

The same identity can be coupled directly to the Robin height. Along the same clean peak sequence,

\[
\boxed{
\sqrt X\log X\,\bigl(\log G(C)-\gamma\bigr)
=\mathscr Y(X)-2\sqrt2+o(1),
}
\tag{4}
\]

and eliminating the value term between (3) and (4) gives

\[
\boxed{
X\mathscr Y'(X)-\frac{\mathscr Y(X)}{\log X}
=\frac12\sqrt X\log X\,\bigl(\log G(C)-\gamma\bigr)+o(1).
}
\tag{5}
\]

Equation (3), not merely (5), is the new source-side restriction: it follows from clean self-tangency before assuming the sign of the Robin height. A generic large excursion of the mixed prime race need not obey this selected value--slope law. Therefore the remaining clean-chamber obstruction can be sharpened from a selected **value** problem to a selected **value--slope** problem. A clean counterexample sequence must hit the `2 sqrt(2)` value threshold while lying asymptotically on the differential line (3).

## 1. Endpoint subtraction makes the mixed remainder continuous at every prime

The two terms in (1) are individually discontinuous at ordinary primes. At a prime `r`, the jump of the logarithmic Mertens error is

\[
E(r^+)-E(r^-)
=-\log(1-r^{-1}).
\tag{6}
\]

The Chebyshev discrepancy has jump

\[
\Delta(r^+)-\Delta(r^-)=\log r.
\tag{7}
\]

But the weight was chosen in `RE-008` so that

\[
h(r)\log r=-\log(1-r^{-1}).
\tag{8}
\]

Consequently the jumps cancel **exactly**:

\[
\boxed{
\mathcal M_*(r^+)=\mathcal M_*(r^-)
\qquad(r\ \text{prime}).
}
\tag{9}
\]

Thus `mathcal M_*`, and hence `mathscr Y`, has a canonical continuous real interpolation; no arbitrary smoothing of the prime race is being introduced.

On every open interval containing no prime, `E'(x)=-k(x)` and `Delta'(x)=-1`. Differentiating (1) therefore gives the exact identity

\[
\boxed{
\mathcal M_*'(x)
=h(x)-k(x)-\Delta(x)h'(x).
}
\tag{10}
\]

Here

\[
h'(x)
=-\frac1{x(x-1)\log x}
-\frac{-\log(1-x^{-1})}{x(\log x)^2}<0.
\tag{11}
\]

Equation (10) is elementary finite prime bookkeeping. Its relevance appears only after evaluating it at the source-selected self-tangent coordinate.

## 2. Clean self-tangency fixes the derivative at the intrinsic coordinate

For a clean regular self-tangent local peak, `RE-006` proves

\[
p<X<q
\tag{12}
\]

and the exact layer balance

\[
X=\vartheta(p)+\Phi_{\ge2}(X).
\tag{13}
\]

Because there is no ordinary prime in `(p,q)`, one has `vartheta(X)=vartheta(p)`. Hence

\[
\boxed{
\Delta(X)=\vartheta(X)-X=-\Phi_{\ge2}(X).
}
\tag{14}
\]

In particular `X` is prime-free, so (10) is differentiable there. Substitution of (14) gives the exact selected derivative formula

\[
\boxed{
\mathcal M_*'(X)
=h(X)-k(X)+\Phi_{\ge2}(X)h'(X).
}
\tag{15}
\]

This is stronger than reading the mixed error at the left boundary prime. The value of the ordinary global race may be free to oscillate, but at a clean self-tangent return its local derivative is tied to the same higher-layer mass that defines the CA state.

Differentiate (2). Since

\[
\frac{Xs'(X)}{s(X)}
=\frac12+\frac1{\log X},
\tag{16}
\]

(15) yields the exact finite-`X` relation

\[
\boxed{
X\mathscr Y'(X)
=\left(\frac12+\frac1{\log X}\right)\mathscr Y(X)
+Xs(X)\left[h(X)-k(X)+\Phi_{\ge2}(X)h'(X)\right].
}
\tag{17}
\]

No Robin-sign hypothesis has entered (14)--(17).

## 3. The source term in the differential law tends to `-sqrt(2)`

The elementary logarithm expansion gives

\[
h(x)-k(x)
=\frac1{2x^2\log x}
+O\!\left(\frac1{x^3\log x}\right),
\tag{18}
\]

while differentiating the same expansion gives

\[
h'(x)
=-\frac1{x^2\log x}
-\frac1{x^2(\log x)^2}
+O\!\left(\frac1{x^3\log x}\right).
\tag{19}
\]

`RE-007` proves, on the exact CA event scale,

\[
\Phi_{\ge2}(X)=\sqrt{2X}+o(\sqrt X).
\tag{20}
\]

Equations (18)--(20) imply

\[
Xs(X)\bigl(h(X)-k(X)\bigr)=o(1)
\tag{21}
\]

and

\[
Xs(X)\Phi_{\ge2}(X)h'(X)
=-\sqrt2+o(1).
\tag{22}
\]

Substitution in (17) proves (3).

The constant has a transparent source. The selected derivative sees the second CA layer through `Phi_(>=2)(X)~sqrt(2X)`, while the local derivative of the endpoint-subtraction kernel contributes `-1/(X^2 log X)` at leading order. After multiplication by the Robin normalization and one logarithmic-time derivative `X d/dX`, their product is exactly `-sqrt(2)`.

## 4. The Robin height can be centered at `X` without an endpoint correction

The clean interval `(p,q)` contains no prime, so the Euler product over primes at `X` is exactly the product over `r<=p`. Therefore

\[
\log G(C)-\gamma
=E(X)-T(C),
\tag{23}
\]

with the exponent-tail correction `T(C)` of `RE-008`--`RE-010`.

At self-tangency, (14) turns (1) into

\[
\mathcal M_*(X)
=E(X)+\Phi_{\ge2}(X)h(X).
\tag{24}
\]

Thus the height has the exact intrinsic-coordinate form

\[
\boxed{
\log G(C)-\gamma
=\mathcal M_*(X)-\Phi_{\ge2}(X)h(X)-T(C).
}
\tag{25}
\]

This is the `X`-centered counterpart of the `p`-centered identity in `RE-008`; the small positive correction `Q(p,X)` disappears because both the Mertens normalization and endpoint subtraction are now evaluated at the actual self-tangent coordinate.

From (20) and `h(X)=(1+o(1))/(X log X)`,

\[
s(X)\Phi_{\ge2}(X)h(X)\longrightarrow\sqrt2.
\tag{26}
\]

`RE-010` proves

\[
\sqrt p\log p\,T(C)\longrightarrow\sqrt2.
\tag{27}
\]

Since `p<X<q` are consecutive primes, the prime number theorem gives `X/p->1`, so `s(X)/s(p)->1`; hence

\[
s(X)T(C)\longrightarrow\sqrt2.
\tag{28}
\]

Multiplying (25) by `s(X)` and using (26)--(28) proves (4).

## 5. Value and slope carry the same selected Robin sign

Subtract `mathscr Y(X)/log X` from (3):

\[
X\mathscr Y'(X)-\frac{\mathscr Y(X)}{\log X}
=\frac12\mathscr Y(X)-\sqrt2+o(1).
\tag{29}
\]

Equation (4) says

\[
\frac12\mathscr Y(X)-\sqrt2
=\frac12s(X)\bigl(\log G(C)-\gamma\bigr)+o(1),
\tag{30}
\]

and (5) follows.

This produces a useful falsification target. For any fixed `delta>0`, along clean self-tangent peaks,

\[
s(X)\bigl(\log G(C)-\gamma\bigr)\ge\delta
\]

forces

\[
X\mathscr Y'(X)-\frac{\mathscr Y(X)}{\log X}
\ge\frac\delta2+o(1),
\tag{31}
\]

while a normalized safe margin at most `-delta` forces the opposite sign with the same half-margin. In particular, an unbounded clean Robin-counterexample sequence necessarily satisfies

\[
\liminf\left(
X\mathscr Y'(X)-\frac{\mathscr Y(X)}{\log X}
\right)\ge0,
\tag{32}
\]

although the inequality may be asymptotically sharp because the Robin excess itself could tend to zero faster than the natural square-root scale.

A fixed positive slope margin is therefore **not** claimed for every hypothetical counterexample. The durable point is the joint constraint (3): selected counterexamples cannot be modeled by arbitrary large values of the global mixed race without simultaneously reproducing the CA-prescribed local slope.

## 6. Prior art and audit boundary

The individual prime-counting errors and their global correlation are prior art. Bhattacharya--Martin--Simpson, already anchored in `SOURCES.md`, study the normalized standard/reciprocal error pair, prove that one-sided global bounds for the relevant mixed difference are RH-equivalent, and under RH+LI determine its joint limiting distribution. `RE-009` supplies the exact dictionary from their mixed difference to `mathscr Y` up to the harmless endpoint factor. Those results do not condition on CA self-tangent coordinates and do not supply the selected differential relation (17).

The CA event measure and exact self-tangent workload are likewise prior art at the representation level through Mantovanelli's August 2026 preprint, also already anchored in `SOURCES.md`. Its public companion verifies the event sweep, self-tangent returns, packet identities, moments, and prime-frontier decomposition. A targeted search of the currently available manuscript/companion descriptions and the mixed-prime-race literature did not locate the exact continuous endpoint-subtracted interpolation (9)--(10) or the selected value--slope coupling (3). No blanket novelty claim is made: continuity (9), differentiation (10), and the asymptotic kernel expansions are elementary once the two existing structures are spliced.

No new literature theorem is load-bearing here, so `SOURCES.md` does not change. The substantive Mathia delta is the source-selection consequence: after the `RE-009` global-race classicalization and the `RE-010` value threshold, clean self-tangency supplies a second, local observable constraint on the same mixed race.

Several boundaries are load-bearing. First, the **clean first-layer** hypothesis is needed to place `X` strictly between consecutive ordinary primes and to obtain (14). At a higher-layer/tied boundary the same derivative test is not justified. Second, the derivative is the ordinary derivative of the canonical continuous interpolation `mathscr Y(x)` on a prime-free interval; no derivative of the raw discontinuous normalized errors of prior art is asserted. Third, (3) holds only along self-tangent selected coordinates and is not a global differential equation for `mathscr Y`.

Finally, a global distribution statement for `mathscr Y` alone does not control the sparse selector. Even under a model in which values and slopes have a smooth ambient joint distribution, proving that the arithmetic CA-selected coordinates avoid the high-value branch of (3) requires a genuine source-selection theorem. The present result therefore does not prove Robin's inequality, bound the global mixed race, or eliminate the exceptional higher-layer chamber.

## 7. Research consequence

`RE-010` leaves the clean route at the question whether CA-selected boundary primes can make the mixed race cross `2sqrt(2)` infinitely often. `RE-011` shows that such a crossing is not the whole event: the clean self-tangent state forces the mixed race onto the asymptotic line

\[
X\mathscr Y'(X)
-\left(\frac12+\frac1{\log X}\right)\mathscr Y(X)
=-\sqrt2+o(1).
\tag{33}
\]

The next positive theorem may therefore exploit **joint value--slope selection** rather than a forbidden global bound. One route would show that sufficiently high positive mixed-race excursions cannot meet (33) at clean CA self-tangent coordinates infinitely often; a falsifying route would construct or justify such simultaneous alignments. Either outcome is more discriminating than another marginal bound on `mathscr Y`.

The other branch of the program is unchanged: hypothetical counterexample peaks may in principle concentrate on the zero-count-density higher-layer/tied event chamber of `RE-004`. A complete Robin argument still has to exclude that exceptional concentration as well as the clean selected value--slope event.