# RE-043 — adjacent first-layer fan switches straddle their generating prime

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + FIRST-LAYER-EVENT-QUANTIZATION + SELECTOR-PLACEMENT + HALF-LOGARITHMIC-BRACKETING + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-042` identified two independent obstacles to exploiting the physical first-layer prime/event staggering: the uniform translated-race error is not yet known below the individual-prime scale `log Z/sqrt(Z)`, and the adaptive selector had not been shown to sample the two sides of the same prime jump. The second obstacle disappears at every **adjacent first-layer threshold switch** of the compact fan from `RE-040`.

Assume RH is false, fix

\[
J=[b_0,b_1]\Subset(1-\Theta,1/2),
\]

and work on the sufficiently late common positive CA counterexample blocks supplied by `RE-040`. Fix `b in J`. Suppose two adjacent CA states

\[
C_-<C_+
\]

are both maximizers of

\[
A_b(C)=Y^b\bigl(e^{h(C)}-1\bigr),
\qquad
Y=\log C,
\qquad
h(C)=\log G(C)-\gamma>0,
\]

and suppose their adjacent CA transition is one ordinary first-layer prime atom `p`, so that

\[
C_+=pC_-,
\qquad
Y_+-Y_-=\log p.
\tag{1}
\]

Let `eta_p` be the first-layer CA event coordinate of `p`,

\[
g(\eta_p)=m_{p,1}
:=\frac{\log(1+p^{-1})}{\log p},
\qquad
g(x)=\frac1{x\log x},
\tag{2}
\]

and let `Z_-`, `Z_+` be the two adaptive tangent parameters from `RE-040`,

\[
g(Z_\pm)
=g(Y_\pm)-\frac{b(1-e^{-h(C_\pm)})}{Y_\pm}.
\tag{3}
\]

Then

\[
\boxed{Z_-<\eta_p<Z_+.}
\tag{4}
\]

More sharply, uniformly for `b in J` along any such sequence of switches escaping to infinity,

\[
\boxed{
\eta_p-Z_-
=\left(\frac12+o_J(1)\right)\log p,
\qquad
Z_+-\eta_p
=\left(\frac12+o_J(1)\right)\log p.
}
\tag{5}
\]

Hence

\[
\boxed{
Z_+-Z_-
=(1+o_J(1))\log p,
\qquad
\frac{Z_-+Z_+}{2}
=\eta_p+o_J(\log p).
}
\tag{6}
\]

Combining (5) with `RE-042`,

\[
\eta_p
=p+\frac12+o(1),
\tag{7}
\]

gives the source-specific placement statement

\[
\boxed{Z_-<p<\eta_p<Z_+}
\tag{8}
\]

for all sufficiently large switches of this type. Thus an adjacent first-layer breakpoint of the adaptive Robin fan cannot sit entirely on one side of the ordinary prime discontinuity: its two tied CA selectors automatically bracket the very prime that generates their common CA transition.

This closes the **placement** half of the local obstruction in `RE-042`, but only on the stated adjacent first-layer subfamily. It does not improve the `RE-040` residual rate, does not prove that infinitely many fan switches have this form, and does not prevent the logarithmic selector bracket from containing other ordinary primes. The remaining local problem is therefore quantitative race resolution, while the remaining global problem is to force sufficiently many source-quantized switches or aggregate them coherently.

## 1. A tied adaptive maximum puts both CA endpoints on one concave barrier

Let

\[
c:=A_b(C_-)=A_b(C_+)>0
\tag{9}
\]

and define the exact adaptive barrier used in `RE-034` and `RE-040`,

\[
\tau(x):=\log(1+cx^{-b}),
\qquad
H(x):=\log\log x+\tau(x).
\tag{10}
\]

Because `c=Y_\pm^b(e^{h(C_\pm)}-1)`,

\[
h(C_\pm)=\tau(Y_\pm).
\tag{11}
\]

Writing `rho(C)=sigma(C)/C`, the definition of `G` gives

\[
\log\rho(C_\pm)=\gamma+H(Y_\pm).
\tag{12}
\]

The adjacent CA transition has supporting slope

\[
\varepsilon_p
=
\frac{\log\rho(C_+)-\log\rho(C_-)}{Y_+-Y_-}.
\tag{13}
\]

For a single first-layer atom, the classical CA threshold formula gives

\[
\varepsilon_p=m_{p,1}=g(\eta_p).
\tag{14}
\]

Equations (12)--(14) therefore identify the physical event slope with the exact secant of the adaptive barrier:

\[
\boxed{
g(\eta_p)
=\frac{H(Y_+)-H(Y_-)}{Y_+-Y_-}.}
\tag{15}
\]

On the late blocks of `RE-040`, the small-height estimate is uniform across the compact fan and yields

\[
\frac{\tau''(x)}{|g'(x)|}=o_J(1)
\tag{16}
\]

through every neighboring CA interval. Since

\[
H''(x)=g'(x)+\tau''(x),
\tag{17}
\]

`H` is strictly concave there. The secant in (15) consequently satisfies

\[
H'(Y_-)>g(\eta_p)>H'(Y_+).
\tag{18}
\]

But (3) is exactly

\[
g(Z_\pm)=H'(Y_\pm).
\tag{19}
\]

As `g` is strictly decreasing, (18)--(19) immediately give (4). This argument also shows why the placement statement is special to a genuine tied adjacent transition: the physical event slope is then the same secant slope that the two adaptive maxima expose.

## 2. The event is asymptotically centered between the two tangent parameters

Put

\[
\Delta:=Y_+-Y_-=\log p.
\tag{20}
\]

For a twice differentiable concave function, secant-minus-tangent errors have exact integral forms. From (15),

\[
H'(Y_-)-g(\eta_p)
=
\frac1\Delta
\int_{Y_-}^{Y_+}
(Y_+-t)\bigl(-H''(t)\bigr)\,dt,
\tag{21}
\]

and

\[
g(\eta_p)-H'(Y_+)
=
\frac1\Delta
\int_{Y_-}^{Y_+}
(t-Y_-)\bigl(-H''(t)\bigr)\,dt.
\tag{22}
\]

Before treating the curvature as constant, the relevant scales must be bootstrapped without assuming `log p=o(Y)`. From (3) and the uniform small-height estimate in `RE-040`,

\[
\frac{H'(Y_\pm)}{g(Y_\pm)}
=1-b(1-e^{-h(C_\pm)})\log Y_\pm
=1-o_J(1).
\tag{23}
\]

Equations (18) and (23) imply

\[
g(\eta_p)<g(Y_-)
\quad\Longrightarrow\quad
\eta_p>Y_-,
\tag{24}
\]

while

\[
g(\eta_p)>(1-o_J(1))g(Y_+).
\tag{25}
\]

Because `g(x)=1/(x log x)` is regularly varying with index `-1`, (25) gives

\[
\eta_p\le(1+o_J(1))Y_+.
\tag{26}
\]

`RE-042` gives `eta_p~p`; hence `p=O(Y_+)`, and therefore

\[
\Delta=\log p=O(\log Y_+)=o(Y_+).
\tag{27}
\]

Using `Y_-=Y_+-Delta`, we obtain

\[
Y_-\sim Y_+.
\tag{28}
\]

Now (24), (26), and (28) yield

\[
\eta_p\sim Y_-\sim Y_+.
\tag{29}
\]

Finally `RE-040` gives `Z_\pm/Y_\pm->1` uniformly over the compact fan, so

\[
\boxed{Z_\pm\sim\eta_p\sim Y_\pm\sim p.}
\tag{30}
\]

This removes any circular dependence between the shortness of the CA interval and the comparison of the event/tangent scales.

The logarithmic derivative of

\[
|g'(x)|
=\frac{\log x+1}{x^2(\log x)^2}
\tag{31}
\]

is `O(1/x)`. Equations (27)--(30) therefore give uniformly on the CA interval

\[
|g'(t)|=(1+o_J(1))|g'(\eta_p)|.
\tag{32}
\]

Using (16)--(17),

\[
-H''(t)
=(1+o_J(1))|g'(\eta_p)|
\tag{33}
\]

uniformly for `Y_-<=t<=Y_+`. Substitution into (21)--(22) yields

\[
H'(Y_-)-g(\eta_p)
=\left(\frac12+o_J(1)\right)
|g'(\eta_p)|\Delta,
\tag{34}
\]

\[
g(\eta_p)-H'(Y_+)
=\left(\frac12+o_J(1)\right)
|g'(\eta_p)|\Delta.
\tag{35}
\]

Now apply the mean-value theorem to `g` between `Z_-` and `eta_p`, and between `eta_p` and `Z_+`. By (30), the intermediate derivatives are again `(1+o_J(1))g'(eta_p)`. With (19), equations (34)--(35) therefore become

\[
\eta_p-Z_-
=\left(\frac12+o_J(1)\right)\Delta,
\qquad
Z_+-\eta_p
=\left(\frac12+o_J(1)\right)\Delta,
\tag{36}
\]

which proves (5)--(6).

The factor `1/2` is not imported from the half-unit physical offset in `RE-042`. It is the universal first-order secant-versus-tangent factor for a barrier whose curvature varies negligibly over an adjacent CA interval. The two scales are very different: the physical prime/event staggering is asymptotically `1/2`, whereas the adaptive tangent bracket has radius `(1/2) log p`.

## 3. The logarithmic bracket necessarily crosses the generating prime

`RE-042` proves

\[
\eta_p
=p+\frac{\log p}{2(\log p+1)}+O(p^{-1})
=p+\frac12+o(1).
\tag{37}
\]

Combining this with (36),

\[
Z_-
=p+\frac12
-\left(\frac12+o_J(1)\right)\log p
+o(1),
\tag{38}
\]

\[
Z_+
=p+\frac12
+\left(\frac12+o_J(1)\right)\log p
+o(1).
\tag{39}
\]

Since `log p -> infinity`, (38)--(39) imply (8). Therefore a first-layer threshold switch supplies exactly the selector-side comparison that `RE-042` could not obtain from an arbitrary fan state: one tied selector lies before the ordinary-prime jump and the other lies after both the prime and its delayed CA event.

The width in (6) is itself informative. It is asymptotic to the natural mean prime spacing `log p`. Consequently the bracketing theorem does **not** isolate the prime `p`: nearby ordinary primes may also lie between `Z_-` and `Z_+`. Any attempt to convert (8) directly into a race contradiction must therefore control a short interval of logarithmic length, not merely the single discontinuity at `p`.

## 4. What this removes from the RE-042 obstruction, and what remains

`RE-042` separated two missing inputs for a one-prime common-source argument:

1. a placement theorem showing that selected adaptive parameters sample opposite sides of the same prime jump;
2. translated-race accuracy finer than the jump scale `log p/sqrt(p)`.

For adjacent first-layer fan switches, (8) supplies the first input automatically from the exact CA secant geometry. No extra prime-gap theorem and no RH-strength estimate is needed. Moreover the two sample points are only logarithmically separated, so the comparison is genuinely local on the prime scale.

The second input remains untouched. `RE-040` gives only

\[
\sup_{b\in J}|\mathcal R_b(Z_b)|\to0,
\tag{40}
\]

whereas `RE-042` shows that one prime changes the nonlinear residual by only

\[
\asymp\frac{\log p}{\sqrt p}=o(1).
\tag{41}
\]

Equation (8) therefore cannot be inserted into (40) to force a contradiction at present. In addition, a threshold fan may skip adjacent CA states, may switch across a higher-layer transition, or may cross a tied multi-atom CA event. This finding proves no lower bound on the number of adjacent first-layer switches inside a counterexample block.

The sharpened local target is now precise: either obtain a rate for the uniform `RE-040` residual that resolves the logarithmic bracket **and** its possible extra primes, or prove that the compact fan contains enough adjacent first-layer switches for a multi-switch aggregate whose common-source signal survives the square-root normalization. A proof based only on the existence of the fan or on abstract support capacity remains excluded by `RE-039` and `RE-041`.

## 5. Prior-art boundary

The first-layer critical CA slope `log(1+1/p)/log p` and the variational exponent thresholds are classical Alaoglu--Erdos structure already anchored in `SOURCES.md`. The prime-layer event/support formulation is also bounded by the Mantovanelli preprint already recorded there. The secant-versus-tangent identities (21)--(22) are elementary calculus and carry no novelty claim.

A targeted prior-art search found the classical CA threshold formulas, neighboring work on consecutive CA quotients, and the recent exact prime-layer workload framework, but no source deriving the adaptive Robin-amplitude **two-sided tangent placement** (5)--(8) at a threshold tie. The line-specific content claimed here is only this combination of `RE-040`'s common-block adaptive fan with the physical first-layer event quantization isolated by `RE-041`--`RE-042`. No new external theorem is load-bearing, so `SOURCES.md` does not require expansion.

## Consequence

The naive local quantization route is narrower than after `RE-042`: at an adjacent first-layer fan switch, selector placement is no longer an independent unknown. The generating prime is forced inside an asymptotically centered selector bracket of width `log p`. The unresolved arithmetic is now concentrated in **race resolution on that logarithmic window** and in proving that enough such physical switches occur to matter.