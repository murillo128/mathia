# RE-036 — adaptive CA selectors lie in a bounded nonlinear prime-race tube

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + ADAPTIVE-THRESHOLD-CA + NONLINEAR-PRIME-RACE-NORMAL-FORM + BOUNDED-NORMALIZED-TUBE + FINITE-SPECTRAL-CONTROL + NEGATIVE/OBSTRUCTION + PRIOR-ART-BOUNDED`. `RE-034` shows that the adaptive Robin maxima forced by hypothetical RH failure lie asymptotically on the standard/reciprocal prime-race ray

\[
\frac{\mathcal E_{\pi_\ell}(Z)}{-\mathcal E_\vartheta(Z)}
\longrightarrow \frac{1-b}{b}.
\tag{1}
\]

At finer resolution that ray is not the exact deterministic target. Retaining the exact adaptive tangent rather than linearizing it produces a universal **nonlinear curve** in the two prime-race coordinates. The actual adaptive CA-selected points lie within bounded distance of that curve after square-root normalization. In particular, the first omitted correction to (1) is an explicit `1/(b log Z)` change of slope, which can be much larger than the bounded residual.

This removes all deterministic inverse-logarithmic tangent and `log log` normalization error at once. It does **not** produce a contradiction: the finite dominant spectral packets used as controls in `RE-035` still intersect this stricter nonlinear curve with bounded gaps in logarithmic phase. Thus neither the linear ray nor its exact nonlinear CA calibration is a coefficient-level obstruction; the remaining burden is the arithmetic placement of the CA selector or genuinely nonuniform top-edge spectral structure.

Assume RH is false and fix

\[
1-\Theta<b<\frac12,
\qquad
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho.
\tag{2}
\]

Take the unbounded sequence of rightmost adaptive block maxima supplied by `RE-034`. For such a state `C`, write

\[
Y:=\log C,
\qquad
h:=\log G(C)-\gamma>0,
\tag{3}
\]

and let `Z>Y` be its adaptive tangent parameter, so that

\[
Y=\Phi(Z)
\tag{4}
\]

and

\[
\frac1{Z\log Z}
=
\frac1{Y\log Y}
-
\frac{b(1-e^{-h})}{Y}.
\tag{5}
\]

Put

\[
\ell:=\log Z,
\qquad
U(Z):=\frac{Z-\vartheta(Z)}{\sqrt Z}
=-\mathcal E_\vartheta(Z),
\tag{6}
\]

\[
E(Z):=
\sum_{p\le Z}-\log(1-p^{-1})-\gamma-\log\log Z,
\qquad
V(Z):=E(Z)\sqrt Z\,\ell
=\mathcal E_{\pi_\ell}(Z).
\tag{7}
\]

For `q` with `|ell q|` sufficiently small, define

\[
s_\ell(q):=-\log(1-\ell q),
\tag{8}
\]

\[
A_{b,\ell}(q)
:=
\frac1b
\left(
q+
\frac{s_\ell(q)}{\ell(\ell-s_\ell(q))}
\right),
\tag{9}
\]

and

\[
\boxed{
\Psi_{b,\ell}(q)
:=
-\log\bigl(1-A_{b,\ell}(q)\bigr)
-
\log\frac{\ell}{\ell-s_\ell(q)}.
}
\tag{10}
\]

Then along the `RE-034` adaptive sequence,

\[
\boxed{
V(Z)
=
\sqrt Z\,\ell\,
\Psi_{b,\ell}
\left(
\frac{U(Z)}{\sqrt Z\,\ell}
\right)
+O_b(1).
}
\tag{11}
\]

The tube in (11) is genuinely finer than the asymptotic ray. Since

\[
\Psi_{b,\ell}(0)=0,
\qquad
\Psi'_{b,\ell}(0)
=
\frac{1-b}{b}+rac1{b\ell},
\tag{12}
\]

and, uniformly for `|ell q|=o(1)`,

\[
\Psi_{b,\ell}(q)
=
\left(
\frac{1-b}{b}+rac1{b\ell}
\right)q
+O_b(\ell q^2),
\tag{13}
\]

we obtain the corrected linear form

\[
\boxed{
V(Z)
=
\left(
\frac{1-b}{b}+rac1{b\log Z}
\right)U(Z)
+O_b\left(1+\frac{U(Z)^2}{\sqrt Z}\right).
}
\tag{14}
\]

Thus the `RE-034` ray has a deterministic drift of size approximately `U/(b log Z)` before one reaches the bounded-width nonlinear normal form. Finite inverse-log expansions can successively approximate this curve, but (10) packages all of those deterministic corrections without truncation.

## 1. The exact adaptive tangent is a one-parameter nonlinear curve

Let

\[
s:=\log\frac ZY>0,
\qquad
q_0:=\frac{Z-Y}{Z\ell}.
\tag{15}
\]

Since `Y=Ze^{-s}`,

\[
q_0=\frac{1-e^{-s}}\ell,
\qquad
s=s_\ell(q_0).
\tag{16}
\]

Multiply (5) by `Z e^{-s}`. The exact tangent equation becomes

\[
\frac1{\ell-s}-\frac{e^{-s}}\ell
=b(1-e^{-h}).
\tag{17}
\]

The left side admits the exact decomposition

\[
\frac1{\ell-s}-\frac{e^{-s}}\ell
=
\frac{1-e^{-s}}\ell
+
\frac{s}{\ell(\ell-s)}
=
q_0+
\frac{s}{\ell(\ell-s)}.
\tag{18}
\]

Consequently

\[
A_{b,\ell}(q_0)=1-e^{-h},
\tag{19}
\]

and therefore

\[
\boxed{
h
=-\log\bigl(1-A_{b,\ell}(q_0)\bigr).
}
\tag{20}
\]

On the other hand, the exact Euler-product factorization from `RE-034` is

\[
h
=E(Z)-\delta_\ell(Z)-T(C)
+
\log\frac{\log Z}{\log Y},
\tag{21}
\]

where

\[
\delta_\ell(Z)=O(Z^{-1})
\tag{22}
\]

is the possible first-layer endpoint correction and

\[
T(C)
:=-\sum_{p\mid C}\log(1-p^{-(a_p+1)})
\tag{23}
\]

is the finite-exponent Euler-product tail. Since `log Y=ell-s`, equations (20)--(21) give the exact identity

\[
\boxed{
E(Z)
=
\Psi_{b,\ell}(q_0)
+T(C)+\delta_\ell(Z).
}
\tag{24}
\]

No prime-number-theorem approximation has entered. The function `Psi` is simply the exact adaptive tangent and the exact `log log C` normalization written in the displacement coordinate `q_0`.

`RE-034` proves on this sequence that `h log Z -> 0` and

\[
Z-Y\sim b h Z\log Z.
\tag{25}
\]

Hence `s=o(1)`, `ell q_0=o(1)`, and all expressions above are eventually in a fixed analytic neighborhood of `q=0`.

## 2. The CA-side structural errors are only `O(1)` after prime-race normalization

The bounds used in `RE-034` can be sharpened at exactly the scale needed by (11). Let `Phi_{>=2}(Z)` be the total mass of active prime-power layers of depth at least two. For the CA layer increment

\[
\lambda_{r,j}
=
\log\frac{1-r^{-(j+1)}}{1-r^{-j}},
\tag{26}
\]

one has the elementary upper bound

\[
0<\lambda_{r,j}\le r^{-j}.
\tag{27}
\]

An active layer therefore satisfies

\[
r^j\log r\le Z\ell.
\tag{28}
\]

For `j=2`, (28) puts every active prime below `sqrt(2Z)` for all sufficiently large `Z`, so Chebyshev's elementary bound `vartheta(x)=O(x)` gives

\[
\Phi_2(Z)=O(\sqrt Z).
\tag{29}
\]

For `j>=3`, the same inequality gives a first contribution `O((Z ell)^(1/3))`; all depths `j>=4` together contribute `O(ell (Z ell)^(1/4))`, because the largest possible active depth is `O(ell)`. Both are `o(sqrt Z)`. Hence

\[
\boxed{
\Phi_{\ge2}(Z)=O(\sqrt Z).
}
\tag{30}
\]

The exponent tail admits a matching improvement over the deliberately coarse `O(Z^{-1/2})` estimate recorded in `RE-034`:

\[
\boxed{
T(C)=O\left(\frac1{\sqrt Z\,\ell}\right).
}
\tag{31}
\]

Indeed, if `a_r=1`, the second layer is inactive. The lower bound already used in `RE-034`,

\[
\lambda_{r,2}\ge\frac1{4r^2},
\tag{32}
\]

forces `r>sqrt(Z)/3` for all sufficiently large `Z`. Chebyshev's bound `pi(x)=O(x/log x)` and partial summation then give

\[
\sum_{a_r=1}-\log(1-r^{-2})
\ll
\sum_{r>\sqrt Z/3}r^{-2}
=O\left(\frac1{\sqrt Z\,\ell}\right).
\tag{33}
\]

If `a_r>=2`, put `j=a_r+1>=3`. The next layer is inactive, and the lower bound

\[
\lambda_{r,j}\ge\frac1{4r^j}
\tag{34}
\]

used in `RE-034` yields

\[
r^{-j}\ll\frac{\log r}{Z\ell}.
\tag{35}
\]

At the same time the active second layer puts `r<sqrt(2Z)`. Since `-log(1-r^{-j})<<r^{-j}` for `j>=3`, Chebyshev's bound for `vartheta` gives

\[
\sum_{a_r\ge2}-\log(1-r^{-(a_r+1)})
\ll
\frac1{Z\ell}
\sum_{r\le\sqrt{2Z}}\log r
=O\left(\frac1{\sqrt Z\,\ell}\right).
\tag{36}
\]

Equations (33) and (36) prove (31). No RH-strength prime estimate is involved.

Now the exact event identity in `RE-034` is

\[
Z-\vartheta(Z)
=(Z-Y)+\Phi_{\ge2}(Z)-\delta_\vartheta(Z),
\qquad
0\le\delta_\vartheta(Z)\le\ell.
\tag{37}
\]

Therefore, with

\[
q:=\frac{Z-\vartheta(Z)}{Z\ell}
=\frac{U(Z)}{\sqrt Z\,\ell},
\tag{38}
\]

we have from (30)

\[
\boxed{
q-q_0
=O\left(\frac1{\sqrt Z\,\ell}\right).
}
\tag{39}
\]

On the analytic neighborhood `|ell q|=o(1)`, direct differentiation of (8)--(10) gives

\[
\Psi'_{b,\ell}(q)=O_b(1).
\tag{40}
\]

Combining (24), (31), (39), (40), and (22) yields

\[
E(Z)
=
\Psi_{b,\ell}(q)
+O_b\left(\frac1{\sqrt Z\,\ell}\right).
\tag{41}
\]

Multiplying by `sqrt(Z) ell` proves the bounded normalized tube (11).

This bounded error is a deterministic CA-side statement. It is substantially smaller than either selected prime-race coordinate, because `RE-034` gives

\[
U(Z),V(Z)
\gg_b Z^{1/2-b}\log Z\to\infty.
\tag{42}
\]

## 3. The asymptotic ray misses an explicit first logarithmic correction

The exact curve is analytic at `q=0`. From (8),

\[
s_\ell'(0)=\ell.
\tag{43}
\]

Differentiating (9) at zero gives

\[
A'_{b,\ell}(0)
=\frac1b\left(1+\frac1\ell\right),
\tag{44}
\]

while

\[
\left.
\frac d{dq}
\log\frac\ell{\ell-s_\ell(q)}
\right|_{q=0}
=1.
\tag{45}
\]

Hence (12) follows. A second differentiation on any fixed neighborhood with `|ell q|<=1/4` gives

\[
\Psi''_{b,\ell}(q)=O_b(\ell),
\tag{46}
\]

which proves (13) and therefore (14).

Two resolution levels should be kept distinct. The old linear ray (1) is correct at relative `o(1)` scale. At the next deterministic level its residual is not generally bounded: the universal shift `U/(b log Z)` is present. The nonlinear curve (10) removes that shift and every further tangent/normalization correction generated by the same exact geometry, leaving only the genuinely discrete higher-layer and exponent-tail terms, which are bounded after normalization.

Thus taking more inverse-log terms can improve the linear approximation, but no finite order is the canonical object. The exact normal form is (10)--(11).

## 4. Finite dominant zero packets still realize the nonlinear curve syndetically

The stronger calibration must be tested against the finite spectral controls of `RE-035`. Let `P` be a nonempty finite conjugate-paired packet with rightmost real part

\[
\beta_*>1-b,
\qquad
a_*:=\beta_*-\frac12\in(0,1/2),
\tag{47}
\]

and retain the `RE-035` standard and reciprocal packet coordinates

\[
\Theta_P(x),
\qquad
L_P(x).
\tag{48}
\]

Put

\[
U_P(x):=-\Theta_P(x),
\qquad
V_P(x):=L_P(x).
\tag{49}
\]

`RE-035` constructs a fixed robust interval in logarithmic phase and a relatively dense set of its almost-periodic translates on which

\[
U_P(x)\gg_P x^{a_*},
\qquad
V_P(x)\gg_P x^{a_*},
\tag{50}
\]

while the linear-ray residual

\[
K_{P,b}(x)
:=bV_P(x)-(1-b)U_P(x)
\tag{51}
\]

has opposite signs at the two endpoints, each with magnitude `>>_P x^(a_*)`.

On those same bounded logarithmic windows, (13) gives uniformly

\[
\begin{aligned}
&\sqrt x\log x\,
\Psi_{b,\log x}
\left(
\frac{U_P(x)}{\sqrt x\log x}
\right)
-
\frac{1-b}{b}U_P(x)\\
&\qquad
=
\frac{U_P(x)}{b\log x}
+O_b\left(\frac{U_P(x)^2}{\sqrt x}\right)
=o_P(x^{a_*}),
\end{aligned}
\tag{52}
\]

because `a_*<1/2`. Therefore the nonlinear residual

\[
H_{P,b}(x)
:=
V_P(x)
-
\sqrt x\log x\,
\Psi_{b,\log x}
\left(
\frac{U_P(x)}{\sqrt x\log x}
\right)
\tag{53}
\]

has the same opposite endpoint signs as `K_{P,b}/b` on every sufficiently late recurrent window. The intermediate value theorem gives an exact zero of (53) in every such window. Consequently there are constants `eta>0`, `L<infinity`, and `u_0` such that every interval `[U,U+L]` with `U>=u_0`, after absorbing the fixed robust-window width exactly as in `RE-035`, contains `u` with `x=e^u` satisfying

\[
\boxed{
V_P(x)
=
\sqrt x\log x\,
\Psi_{b,\log x}
\left(
\frac{U_P(x)}{\sqrt x\log x}
\right),
}
\tag{54}
\]

and

\[
\boxed{
U_P(x),V_P(x)\ge\eta x^{a_*}.
}
\tag{55}
\]

Thus exact intersections with the nonlinear adaptive curve remain **syndetic in `log x`** for every finite rightmost packet beyond the threshold line.

The stability extension of `RE-035` also survives. If an infinite lower spectral contribution is `o(x^(a_*))` uniformly relative to the same finite rightmost face, then it perturbs both the robust endpoint margins in (51) and the nonlinear correction in (52) by `o(x^(a_*))`. The same intermediate-value argument still produces syndetic exact intersections. Merely replacing a finite packet by a finite top face plus a uniformly negligible infinite tail therefore does not create an obstruction.

## 5. Resolution consequence and falsification boundary

Equation (11) is stronger than an all-fixed-orders inverse-log expansion: it removes the entire deterministic adaptive tangent exactly and leaves an `O(1)` normalized structural tube. Against a rightmost spectral face of size `Z^(beta_*-1/2)`, that is a genuine relative power saving

\[
O\left(Z^{-(\beta_*-1/2)}\right).
\tag{56}
\]

This is precisely the sort of scale that the resolution discussion in `RE-031` showed to be absent from a bare little-`o` phase law. However, the matched control (54) shows why gaining such resolution is not itself enough: finite spectral dynamics can hit the fully corrected target exactly and recurrently. A closing argument must constrain **which** of those recurrent windows the discrete CA selector can occupy, rather than only how accurately one can write the target curve.

The finding does not claim that the true zeta explicit formula has a finite rightmost face, that actual CA selectors realize the control packet, or that the nonlinear intersections correspond to admissible prime sequences. The packet construction is a falsification control for coefficient-geometry arguments. Nor does (11) prove Robin's inequality: it is a necessary condition on the adaptive counterexample sequence whose existence was derived conditionally from hypothetical RH failure in `RE-034`.

The `O(1)` tube also depends on retaining the exact nonlinear curve. If one truncates (10) after finitely many Taylor terms, the discarded deterministic term can again dominate `O(1)` on sufficiently large off-critical excursions. Claims of bounded distance to a **finite-order** corrected ray therefore require their own quantitative remainder; they do not follow from (14).

## 6. Prior-art boundary and research consequence

A current literature audit rechecked the three nearest boundaries already anchored in `SOURCES.md`. Mantovanelli's August 2026 prime-layer workload develops the ordinary self-tangent CA event representation, not the blockwise adaptive tangent of `RE-034`. Kalyabin's March 2026 work relates maximal Gronwall values at fixed greatest prime to a modified Mertens remainder, but does not couple that remainder to an adaptive CA Chebyshev coordinate through (10). Bhattacharya--Martin--Simpson study the joint standard/reciprocal prime races and their global support/correlation; their paper is now listed online in *Acta Arithmetica*, but it does not impose the CA selector or derive this adaptive nonlinear target. No new external theorem is load-bearing here, so no source-anchor expansion is required.

The durable narrowing is therefore negative but precise. `RE-034` converted quantitative Robin failure into an exact asymptotic ray; `RE-035` showed that finite spectral packets recurrently realize that ray. `RE-036` now removes the possible loophole that the ray was simply too coarse: the adaptive selector actually lies in a bounded normalized tube around a fully explicit nonlinear curve, **and the same finite spectral controls recurrently realize that stricter curve as well**.

The next viable source-side target must use information absent from these controls: arithmetic placement of the adaptive CA states inside the recurrent logarithmic windows, a nonuniform top-edge spectral tail that cannot be reduced to a finite face plus `o` remainder, or another exact selector invariant that couples separate logarithmic windows. Further deterministic tangent expansion by itself is exhausted by (10).