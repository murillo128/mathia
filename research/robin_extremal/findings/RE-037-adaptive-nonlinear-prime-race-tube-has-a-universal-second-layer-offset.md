# RE-037 — adaptive nonlinear prime-race tube has a universal second-layer offset

**Status:** `EXACT-DERIVED + UNCONDITIONAL-CA-CALIBRATION + QUANTITATIVE-RH-FAILURE + VANISHING-WIDTH-NONLINEAR-TUBE + SECOND-LAYER-DOMINANCE + FINITE-SPECTRAL-CONTROL + PRIOR-ART-BOUNDED`. `RE-036` places every adaptive CA selector forced by hypothetical RH failure inside an `O_b(1)` tube around an exact nonlinear standard/reciprocal prime-race curve. The bounded remainder is not arbitrary. **Its leading value is universal and comes entirely from the same second prime-power layer that produces the classical square-root CA tax.**

Assume RH is false and fix

\[
1-\Theta<b<\frac12,
\qquad
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho.
\tag{1}
\]

Take the unbounded regular adaptive sequence of `RE-034`--`RE-036`. For one selected state `C`, write

\[
Y:=\log C,
\qquad
h:=\log G(C)-\gamma>0,
\tag{2}
\]

and let `Z>Y` be the adaptive tangent parameter, so that

\[
Y=\Phi(Z),
\qquad
\frac1{Z\log Z}
=
\frac1{Y\log Y}
-
\frac{b(1-e^{-h})}{Y}.
\tag{3}
\]

Put

\[
L:=\log Z,
\qquad
U(Z):=\frac{Z-\vartheta(Z)}{\sqrt Z},
\tag{4}
\]

\[
E(Z):=
\sum_{p\le Z}-\log(1-p^{-1})-\gamma-\log\log Z,
\qquad
V(Z):=E(Z)\sqrt Z\,L.
\tag{5}
\]

Retain the exact nonlinear function `\Psi_{b,L}` of `RE-036`. Then the `O_b(1)` tube there sharpens to

\[
\boxed{
V(Z)
=
\sqrt Z\,L\,
\Psi_{b,L}\!\left(
\frac{U(Z)}{\sqrt Z\,L}
\right)
-
\frac{\sqrt2\,(1-2b)}{b}
+o_b(1).
}
\tag{6}
\]

Equivalently,

\[
\boxed{
V(Z)-
\sqrt Z\,L\,
\Psi_{b,L}\!\left(
\frac{U(Z)}{\sqrt Z\,L}
\right)
\longrightarrow
\sqrt2\,\frac{2b-1}{b}.
}
\tag{7}
\]

Thus the adaptive CA selector lies not merely in a bounded nonlinear tube but in a **vanishing-width tube around one explicitly translated nonlinear curve**. Since `b<1/2`, the translation is strictly negative.

The two deterministic CA contributions that survive at this scale are

\[
\boxed{
\frac{\Phi_{\ge2}(Z)}{\sqrt Z}\longrightarrow\sqrt2,
\qquad
\sqrt Z\,L\,T(C)\longrightarrow\sqrt2,
}
\tag{8}
\]

where `\Phi_{\ge2}` is the mass of active layers of depth at least two and

\[
T(C):=-\sum_{p\mid C}\log(1-p^{-(a_p+1)})
\tag{9}
\]

is the finite-exponent Euler-product tail. The first copy of `sqrt(2)` shifts the prime-counting coordinate from the continuous CA displacement to the physical Chebyshev coordinate; the second copy is the exponent-one Euler-product tail. The nonlinear curve converts the former with asymptotic slope `(1-b)/b`, producing exactly the constant in (7).

## 1. Start from the exact `RE-036` identity before the bounded estimate

Put

\[
s:=\log\frac ZY,
\qquad
q_0:=\frac{Z-Y}{ZL},
\qquad
q:=\frac{Z-\vartheta(Z)}{ZL}
=\frac{U(Z)}{\sqrt Z\,L}.
\tag{10}
\]

`RE-036` derives the exact identities

\[
E(Z)=\Psi_{b,L}(q_0)+T(C)+\delta_\ell(Z),
\qquad
\delta_\ell(Z)=O(Z^{-1}),
\tag{11}
\]

and

\[
Z-\vartheta(Z)
=(Z-Y)+\Phi_{\ge2}(Z)-\delta_\vartheta(Z),
\qquad
0\le\delta_\vartheta(Z)\le L.
\tag{12}
\]

Hence

\[
\boxed{
q-q_0
=
\frac{\Phi_{\ge2}(Z)-\delta_\vartheta(Z)}{ZL}.
}
\tag{13}
\]

The adaptive construction also gives

\[
hL\to0,
\qquad
Lq_0\to0,
\tag{14}
\]

while `RE-036` gives `\Phi_{\ge2}(Z)=O(\sqrt Z)`. Therefore `Lq=o(1)` as well.

Subtract the nonlinear curve from (11) and multiply by `\sqrt ZL`:

\[
\begin{aligned}
\mathcal R_b(Z)
&:=V(Z)-\sqrt ZL\,\Psi_{b,L}(q)\\
&=\sqrt ZL\,T(C)
+\sqrt ZL\,\delta_\ell(Z)
-\sqrt ZL\bigl(\Psi_{b,L}(q)-\Psi_{b,L}(q_0)\bigr).
\end{aligned}
\tag{15}
\]

This identity isolates exactly what the `O_b(1)` in `RE-036` was hiding.

## 2. The active higher-layer mass has the universal limit `sqrt(2)`

The second-layer abundance increment is

\[
\lambda_{r,2}
=
\log\frac{1-r^{-3}}{1-r^{-2}}
=
\log\left(1+\frac1{r(r+1)}\right)
=r^{-2}(1+O(r^{-1})).
\tag{16}
\]

Let `y_2=y_2(Z)` be the real second-layer cutoff defined by

\[
\frac{\lambda_{y_2,2}}{\log y_2}
=
\frac1{ZL}.
\tag{17}
\]

Then

\[
y_2^2\log y_2=ZL(1+o(1)).
\tag{18}
\]

Writing `\ell_2:=\log y_2`, equation (18) implies

\[
\ell_2\sim\frac L2,
\qquad
\frac{y_2}{\sqrt Z}
=\sqrt{\frac L{\ell_2}}(1+o(1))
\longrightarrow\sqrt2.
\tag{19}
\]

The active second-layer primes form an initial prime segment up to this cutoff, apart from an immaterial endpoint convention. The prime number theorem gives the largest such prime `P_2\sim y_2` and `\vartheta(P_2)\sim P_2`, hence

\[
\boxed{
\frac{\Phi_2(Z)}{\sqrt Z}\longrightarrow\sqrt2.
}
\tag{20}
\]

All deeper layers vanish after the same normalization. Indeed the elementary necessary condition for an active `(r,j)` layer,

\[
r^j\log r\le ZL,
\tag{21}
\]

and the logarithmic bound on maximal active depth give

\[
\Phi_{\ge3}(Z)
\ll (ZL)^{1/3}+L(ZL)^{1/4}
=o(\sqrt Z).
\tag{22}
\]

Consequently

\[
\boxed{
\frac{\Phi_{\ge2}(Z)}{\sqrt Z}\longrightarrow\sqrt2.
}
\tag{23}
\]

This is the same second-layer square-root geometry isolated to all logarithmic orders in `RE-016`, but no self-tangency or clean first-layer chamber is needed here: (16)--(23) depend only on the ordinary CA layer selector at the external parameter `Z`.

## 3. The exponent tail contributes the second copy of `sqrt(2)`

Let `P_1` be the largest active first-layer prime. The first-layer cutoff satisfies `P_1\sim Z`. Apart from a possible boundary prime, the exponent-one primes of `C` are exactly

\[
P_2<p\le P_1.
\tag{24}
\]

Thus their contribution is

\[
T_1(C)
=
\sum_{P_2<p\le P_1}-\log(1-p^{-2}).
\tag{25}
\]

The prime number theorem and partial summation give the classical reciprocal-square prime tail

\[
\sum_{p>x}\frac1{p^2}
\sim\frac1{x\log x}.
\tag{26}
\]

Since `-\log(1-p^{-2})=p^{-2}+O(p^{-4})`, while the omitted tail above `P_1\sim Z` is negligible after multiplication by `\sqrt ZL`, equations (19), (25), and (26) yield

\[
\boxed{
\sqrt ZL\,T_1(C)\longrightarrow\sqrt2.
}
\tag{27}
\]

The part coming from exponents at least two is smaller. The layer-by-layer estimate already reconstructed in `RE-016`, which uses only the next inactive CA threshold and not self-tangency, gives

\[
T_{\ge2}(C)=O(Z^{-2/3})
\tag{28}
\]

at the precision needed here. Therefore

\[
\sqrt ZL\,T_{\ge2}(C)=o(1),
\tag{29}
\]

and

\[
\boxed{
\sqrt ZL\,T(C)\longrightarrow\sqrt2.
}
\tag{30}
\]

Equations (23) and (30) are structurally symmetric: at square-root resolution the whole deep CA tower collapses to the second-layer frontier on the selector side and to the exponent-one tail immediately above that same frontier on the Euler-product side.

## 4. The nonlinear displacement converts the two limits into one explicit offset

`RE-036` gives, uniformly when `|Lq|=o(1)`,

\[
\Psi'_{b,L}(0)
=
\frac{1-b}{b}+\frac1{bL},
\qquad
\Psi''_{b,L}(q)=O_b(L).
\tag{31}
\]

By the mean-value theorem there is a point `\xi_Z` between `q_0` and `q` such that

\[
\Psi_{b,L}(q)-\Psi_{b,L}(q_0)
=
\Psi'_{b,L}(\xi_Z)(q-q_0).
\tag{32}
\]

Since `Lq_0=o(1)` and `L(q-q_0)=O(Z^{-1/2})`, (31) implies

\[
\boxed{
\Psi'_{b,L}(\xi_Z)
\longrightarrow\frac{1-b}{b}.
}
\tag{33}
\]

Combining (13) and (32),

\[
\sqrt ZL\bigl(\Psi(q)-\Psi(q_0)\bigr)
=
\Psi'_{b,L}(\xi_Z)
\frac{\Phi_{\ge2}(Z)-\delta_\vartheta(Z)}{\sqrt Z}.
\tag{34}
\]

The endpoint term in (11) satisfies

\[
\sqrt ZL\,\delta_\ell(Z)=o(1),
\tag{35}
\]

and `\delta_\vartheta(Z)/\sqrt Z\to0`. Inserting (23), (30), (33)--(35) into (15) gives

\[
\begin{aligned}
\mathcal R_b(Z)
&=\sqrt2
-\frac{1-b}{b}\sqrt2
+o_b(1)\\
&=\sqrt2\,\frac{2b-1}{b}+o_b(1),
\end{aligned}
\tag{36}
\]

which proves (6)--(7).

The sign is worth recording. Because `b<1/2`, the change from the continuous CA displacement `Z-Y` to the physical Chebyshev displacement `Z-\vartheta(Z)` is amplified by a nonlinear-curve slope greater than one, while the compensating Euler-product tail contributes only one unit of the same `sqrt(2)` scale. The net offset is therefore negative.

## 5. The stronger calibration is still not a finite-packet spectral obstruction

The new constant makes the deterministic target sharper, but it does not revive the finite-mode route already falsified by `RE-033`--`RE-036`.

For a finite dominant zero packet with rightmost real part `\beta_*>1-b`, `RE-035` and Section 4 of `RE-036` provide relatively dense logarithmic windows on which the standard and reciprocal packet coordinates have the required signs and the residual against the nonlinear curve changes sign with endpoint magnitude of order `x^{\beta_*-1/2}`. That magnitude tends to infinity.

Therefore the same intermediate-value argument survives replacement of the zero target by **any fixed bounded additive target**. In particular, on every sufficiently late member of those recurrent windows there is a point satisfying

\[
V_P(x)-
\sqrt x\log x\,
\Psi_{b,\log x}\!\left(
\frac{U_P(x)}{\sqrt x\log x}
\right)
=
\sqrt2\,\frac{2b-1}{b},
\tag{37}
\]

with the same sign-correct large packet coordinates. Thus the translated curve in (6) is also finitely spectrally realizable with bounded gaps in logarithmic phase.

This matters for interpretation: (6) is a genuine narrowing of the **actual CA selector**, not a contradiction from zero-coefficient geometry. Any successful continuation must use the arithmetic placement of the discrete CA selector relative to these recurrent spectral windows, or a genuinely nonuniform/infinite top-edge contribution that invalidates the finite-packet control.

## 6. Prior-art boundary and research consequence

The ingredients entering (8) are classical or already bounded by the line's source anchors. The prime number theorem controls the moving layer cutoffs. Mantovanelli's prime-layer workload is the nearest source for the CA event selector and its layer decomposition. Kalyabin's 2026 preprint gives a sharp fixed-greatest-prime Gronwall/modified-Mertens calibration with the familiar square-root exponent geometry. Bhattacharya--Martin--Simpson give the current joint standard/reciprocal prime-race framework. No novelty is claimed for those ingredients, for the `sqrt(2)` second-layer scale by itself, or for the reciprocal-square prime tail.

The line-specific delta is narrower: `RE-036` left an unspecified bounded error after removing the exact adaptive tangent and `log log` geometry; equations (6)--(7) identify that entire leading bounded error, on the actual `RE-034` adaptive sequence, as the explicit universal translation

\[
-\frac{\sqrt2(1-2b)}b.
\tag{38}
\]

The prior-art search found no source deriving this adaptive CA-selected nonlinear standard/reciprocal prime-race offset. In particular, the neighboring fixed-prime and global prime-race results do not impose the adaptive threshold equation (3), which is what turns the two second-layer contributions into the coefficient `(2b-1)/b`.

The live obstruction is now sharper than the `RE-036` bounded tube: **under RH failure, the arithmetic CA selector must hit a prescribed translated nonlinear prime-race curve to `o(1)` additive accuracy while both coordinates diverge at least on the `Z^{1/2-b}\log Z` scale.** Finite spectral packets still pass this test continuously and syndetically, so the next useful theorem has to exploit selector placement at sub-unit residual resolution rather than another finite-mode sign or slope condition.