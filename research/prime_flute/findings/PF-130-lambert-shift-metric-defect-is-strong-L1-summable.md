# PF-130 — the Lambert shift comparison has summable strong-`L^1` metric defect

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. PF-121 constructs an explicit near-isometric map between the one-parameter ideal Lambert quadrilaterals `Q(a)` and `Q(a+delta)` but records only the uniform `1+O(delta)` bilipschitz bound. The present calculation integrates the **actual PF-121 deformation** and finds a stronger localization effect: its metric/density defect has total `L^1` mass `O(delta/sinh(a))`. For the exact prime/shift-clone half-cuffs these masses are summable. Thus the reciprocal-prime cuff displacement that produced only a weak-`L^1` conclusion under PF-126's coarse fixed-area pant bound does not force a strong-`L^1` divergence inside the isolated Lambert bodies. No global `L^1` marking, Schatten class, wave operator, scattering, determinant, or RH conclusion is claimed; boundary synchronization, interfaces, noncanonical thin geometry, and global assembly remain separate gates.

## Claim

Let `Q(a)` be the PF-119/PF-121 ideal Lambert quadrilateral, let

\[
a' = a+\delta,
\qquad a\ge A,
\qquad 0\le\delta\le\delta_0,
\tag{1}
\]

for fixed sufficiently large `A` and fixed small `delta_0`, and let

\[
F_{a,a'}:Q(a)\longrightarrow Q(a')
\]

be the explicit PF-121 comparison, smoothed in a fixed neighborhood of its internal splice if desired. Put `g_a` and `g_{a'}` for the hyperbolic metrics and define, away from a measure-zero piecewise-smooth locus,

\[
D_{a,a'}
:=
\left\|g_a^{-1}F_{a,a'}^*g_{a'}-I\right\|_{\rm op}
+
\left|
\frac{d\operatorname{vol}_{F_{a,a'}^*g_{a'}}}
     {d\operatorname{vol}_{g_a}}-1
\right|.
\tag{2}
\]

Then there is an absolute tail constant `C` such that

\[
\boxed{
\int_{Q(a)}D_{a,a'}\,d\operatorname{vol}_{g_a}
\le
C\frac{\delta}{\sinh a}.}
\tag{3}
\]

Now specialize to the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1`. Write

\[
a_n=\frac{\ell_n}{2},
\qquad
a_n^+=a_n+\delta_n.
\tag{4}
\]

PF-107 gives `delta_n=O(1/p_n)` up to the harmless one-index shift used in that finding, while the exact collar relation used in PF-114 gives

\[
\frac1{\sinh a_n}=\sinh\frac{h_n}{2},
\qquad
\sum_n h_n^2<\infty.
\tag{5}
\]

Consequently

\[
\boxed{
\sum_n
\int_{Q(a_n)}D_{a_n,a_n^+}\,d\operatorname{vol}_{g_{a_n}}
<\infty.}
\tag{6}
\]

The same conclusion holds for the reflected/right Lambert pieces, with only a fixed multiplicity. Equation (6) is therefore a genuine strong-`L^1` budget for the **independent one-parameter Lambert-body comparisons** underlying the prime/shift pants decomposition.

## 1. PF-121's tail map has a pointwise defect that decays into the large-`a` body

PF-121 uses log-polar coordinates

\[
z=e^{u+i\theta},
\qquad
w=\frac\pi2-\theta,
\]

in which

\[
\boxed{
g_a=\frac{du^2+dw^2}{\cos^2w}}
\tag{7}
\]

is parameter-independent and

\[
Q(a)
\cong
D_a
:=
\left\{(u,w):0\le u\le a,
\ 0\le w\le W_a(u)\right\},
\quad
W_a(u)=\arcsin\frac{\cosh u}{\cosh a}.
\tag{8}
\]

Put

\[
A_a:=\cosh a,
\qquad
S_a:=\sinh a,
\qquad
c:=\frac{\cosh a'}{\cosh a}.
\tag{9}
\]

On `u>=1`, the exact PF-121 map is

\[
F(u,w)=(f(u),w),
\qquad
f(u)=\operatorname{arcosh}(c\cosh u),
\tag{10}
\]

and obeys

\[
W_{a'}(f(u))=W_a(u)
\tag{11}
\]

exactly. Its derivative satisfies the exact identity

\[
\boxed{
1-f'(u)^2
=
\frac{c^2-1}{c^2\cosh^2u-1}.}
\tag{12}
\]

Because (7) is independent of `a`, the two relative metric eigenvalues of `F^*g_{a'}` with respect to `g_a` on this tail are `f'(u)^2` and `1`, while the area-density ratio is `f'(u)`. For bounded small `delta`, `0<f'<=1`, so

\[
D_{a,a'}(u,w)
\le
C\bigl(1-f'(u)^2\bigr)
\le
C\frac{c^2-1}{c^2\cosh^2u-1}.
\tag{13}
\]

This is sharper than the uniform `O(delta)` bound retained in PF-121: the deformation decays with the log-radial coordinate.

## 2. The tail integral is `O(delta/sinh(a))`

The cross-sectional hyperbolic area at fixed `u` is exact:

\[
\begin{aligned}
\int_0^{W_a(u)}\sec^2w\,dw
&=\tan W_a(u)\\
&=
\frac{\cosh u}
{\sqrt{\cosh^2a-\cosh^2u}}.
\end{aligned}
\tag{14}
\]

Since `c>=1`,

\[
c^2\cosh^2u-1\ge\sinh^2u.
\tag{15}
\]

Combining (13)--(15), the contribution from `1<=u<=a` is bounded by

\[
I_{\rm tail}
\le
C(c^2-1)
\int_1^a
\frac{\cosh u}
{\sinh^2u\sqrt{\cosh^2a-\cosh^2u}}\,du.
\tag{16}
\]

Set

\[
y=\sinh u,
\qquad y_0=\sinh1.
\]

Then `dy=cosh(u)du` and

\[
\cosh^2a-\cosh^2u=S_a^2-y^2.
\]

Therefore

\[
\begin{aligned}
I_{\rm tail}
&\le
C(c^2-1)
\int_{y_0}^{S_a}
\frac{dy}{y^2\sqrt{S_a^2-y^2}}\\
&=
C(c^2-1)
\frac{\sqrt{S_a^2-y_0^2}}{S_a^2y_0}\\
&\le
C\frac{c^2-1}{S_a}.
\end{aligned}
\tag{17}
\]

For `0<=delta<=delta_0`,

\[
\frac{\cosh(a+\delta)}{\cosh a}
=\cosh\delta+\tanh a\,\sinh\delta,
\]

so uniformly in `a`,

\[
0\le c^2-1\le C_{\delta_0}\delta.
\tag{18}
\]

Equations (17)--(18) give

\[
\boxed{I_{\rm tail}\le C\delta/\sinh a.}
\tag{19}
\]

The gain is geometric: although the tail extends all the way to the ideal vertex, the part on which the parameter change is appreciable has cross-sectional hyperbolic area suppressed by the large half-cuff scale.

## 3. The compact base strip has the same suppressed area

On `0<=u<=1`, PF-121's explicit graph-rescaling map has bilipschitz constant `1+O(delta)`. Hence its metric and density defect in (2) is pointwise `O(delta)`.

But the base strip does **not** have order-one area as `a->infinity`. Using (14),

\[
\begin{aligned}
\operatorname{area}
\bigl(D_a\cap\{0\le u\le1\}\bigr)
&=
\int_0^1
\frac{\cosh u}
{\sqrt{\cosh^2a-\cosh^2u}}\,du\\
&=
\arcsin\frac{\sinh1}{\sinh a}\\
&=O\left(\frac1{\sinh a}\right).
\end{aligned}
\tag{20}
\]

Therefore

\[
\boxed{I_{\rm base}\le C\delta/\sinh a.}
\tag{21}
\]

PF-121's two formulas meet continuously at `u=1`. If a smooth comparison is desired, interpolate them in a fixed `u`-width neighborhood of that splice. On such a bounded-`u` strip the same area estimate as (20) is `O(1/sinh a)`, and the interpolation can retain `I+O(delta)` differential control. Thus smoothing changes neither the order nor the conclusion of (3).

Combining (19) and (21) proves (3).

## 4. The exact prime/shift Lambert-body masses are summable

For the shift clone, PF-107 gives on the tail

\[
|\delta_n|\le\frac{C}{p_n}
\tag{22}
\]

up to an index shift, and hence

\[
\sum_n\delta_n^2<\infty.
\tag{23}
\]

PF-032/PF-114 give the exact collar conversion

\[
\sinh a_n\,\sinh\frac{h_n}{2}=1,
\tag{24}
\]

and PF-114 proves

\[
\sum_n h_n^2<\infty.
\tag{25}
\]

Since `h_n->0`, equation (24) implies

\[
\frac1{\sinh a_n}
=
\sinh\frac{h_n}{2}
\le C h_n
\tag{26}
\]

on a tail. Cauchy--Schwarz now gives

\[
\begin{aligned}
\sum_n\frac{|\delta_n|}{\sinh a_n}
&\le
C\sum_n|\delta_n|h_n\\
&\le
C
\left(\sum_n\delta_n^2\right)^{1/2}
\left(\sum_n h_n^2\right)^{1/2}
<\infty.
\end{aligned}
\tag{27}
\]

Applying (3) termwise proves (6). No prime number theorem is needed; square-summability of the reciprocal-prime displacement and the already-established square-summability of the logarithmic mesh are enough.

## 5. What this changes in the relative-operator frontier

PF-126 used PF-125's uniform pantwise estimate

\[
\sup_{P_n}D=O(1/p_n)
\]

and the fixed pant area `2pi`, obtaining weak `L^1` and strong `L^r` only for `r>1`. That conclusion remains correct for that coarse estimate and that explicit global marking, but PF-130 shows that the endpoint is **not forced by the isolated Lambert geometry itself**.

For the more geometry-adapted PF-121 pieces,

\[
\boxed{
\text{reciprocal-prime amplitude}
\times
\text{effective Lambert deformation area}
\sim
\frac{\delta_n}{\sinh a_n},
}
\tag{28}
\]

and the total is summable. Therefore a future failure of strong global `L^1`, global `S_r` for `r>1`, or the Güneysu--Thalmaier wave criterion cannot be justified merely by saying that every pant carries an order-`1/p_n` deformation over order-one area.

The surviving obstruction has to be more specific. The PF-121 maps were constructed independently on one-parameter Lambert pieces. PF-125 later changed their traces to achieve exact split-ray and zero-twist coherence; PF-129 separately optimized cusp synchronization. PF-130 does **not** prove that one can impose all of those boundary conditions while retaining (3). Nor does unweighted `L^1` control dominate the inverse-unit-ball-volume weight in regions intersecting globally thin collars. Thus the remaining targets are genuinely the boundary/interface and infinite-assembly terms, together with any noncanonical thin channels not covered by PF-128.

This sharpens both accepted operator clues without resolving either one.

## 6. Prior art and novelty audit

No novelty is claimed for Lambert quadrilateral geometry, quasiconformal comparison, change of variables, or elementary integral estimates. Vuorinen--Wang, *Hyperbolic Lambert quadrilaterals and quasiconformal mappings*, Ann. Acad. Sci. Fenn. Math. 38 (2013), 433--453, DOI `10.5186/aasfm.2013.3845`, studies sharp hyperbolic-distance inequalities and quasiconformal images of Lambert quadrilaterals. Alessandrini--Disarlo, *Generalizing Stretch Lines for Surfaces with Boundary*, IMRN 2022(23), 18919--18991, DOI `10.1093/imrn/rnab222`, develops Lipschitz/arc-metric geometry for hyperbolic surfaces with boundary. Neither audited result supplies an integrated coefficient-defect estimate for the PF-121 one-parameter degeneration.

Directed searches by structure -- Lambert quadrilateral quasiconformal maps, long-boundary pants comparisons, integrated metric distortion, and Lipschitz stretch maps with boundary -- located no theorem giving (3) or the shift-clone summation (6). Absence of matching wording is not a novelty claim. The durable Mathia content is the project-specific observation that the **already-persisted exact PF-121 map** has a hidden `1/sinh(a)` area gain, and that this gain composes with PF-107/PF-114 to cross the strong-`L^1` summability endpoint on the isolated Lambert-body sector.

## 7. Audit / falsification core

A later adversary can check PF-130 through a finite chain:

1. import only PF-121's exact domain (8), tail map (10), graph identity (11), derivative identity (12), and `1+O(delta)` base estimate;
2. verify that on the tail the relative metric eigenvalues are `f'^2,1` and the density ratio is `f'`;
3. integrate the cross-section exactly using `tan(W_a(u))` as in (14);
4. substitute `y=sinh u` and verify the elementary integral in (17);
5. bound `c^2-1=O(delta)` uniformly in large `a`;
6. compute the base-strip area exactly as (20), and check that smoothing near `u=1` occurs in another `O(1/sinh a)` area strip;
7. specialize only at the end, using PF-107 for `delta_n in ell^2`, PF-114 for `h_n in ell^2`, and the exact collar relation (24) to prove (27);
8. do **not** infer a global strong-`L^1` metric comparison, Schatten membership, or wave/scattering equivalence without constructing boundary-coherent maps and controlling the ambient thin-part weight.

A refutation would need to break the PF-121 differential formula, the hyperbolic area calculation, the smoothing estimate, or the square-summability inputs. Failure to assemble the independent Lambert maps globally would not refute PF-130; it would identify precisely the interface/global mechanism excluded from its claim.
