# RE-117 — finite-edge Robin recovery profiles collapse to stable-filter positive lobes

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + MACROSCOPIC-RECOVERY + UNIFORM-PROFILE + STABLE-FILTER-COLLAPSE + SYNDETIC-COMPATIBILITY + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED`.

Assume the finite attained off-critical edge regime of `RE-113`--`RE-116`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
c:=1-\Theta\in(0,1/2),
\tag{1}
\]

and retain the actual edge profile

\[
F(u)=F_\Theta(u),
\qquad
J(u):=\int_0^\infty e^{-cs}F(u+s)\,ds
=F(u)+G_\Theta(u).
\tag{2}
\]

The surviving finite-edge frontier after `RE-116` still allowed one apparently stronger move: couple the adaptive selector not just to its endpoint phase, but to the **whole macroscopic Robin recovery corridor** that follows it. At leading edge order, however, that recovery geometry supplies no new independent source coordinate.

Let `C` be a fixed-`b` adaptive witness of `RE-034`, with

\[
1-\Theta=c<b<\frac12,
\qquad
Y:=\log C,
\qquad
U:=\log Y,
\qquad
\lambda_Y:=h(C)Y^c\log Y.
\tag{3}
\]

For any later CA state `N` with

\[
X:=\log N,
\qquad
Y\le X\le AY
\tag{4}
\]

for one fixed `A>1`, put

\[
t:=\log(X/Y)\in[0,\log A].
\tag{5}
\]

Then, uniformly over all such crossed CA states,

\[
\boxed{
Y^c\log Y\,\bigl(h(C)-h(N)\bigr)
=
\int_0^t e^{-cs}F(U+s)\,ds+o(1).
}
\tag{6}
\]

The adaptive selector relations of `RE-114` give

\[
J(U)=\lambda_Y+o(1).
\tag{7}
\]

Using the stable-filter identity

\[
J(U)
=
\int_0^t e^{-cs}F(U+s)\,ds
+e^{-ct}J(U+t),
\tag{8}
\]

(6) therefore becomes the uniform recovery-profile formula

\[
\boxed{
Y^c\log Y\,h(N)
=
e^{-ct}J(U+t)+o(1).
}
\tag{9}
\]

Thus the entire leading-order Robin recovery corridor is just a translated positive lobe of the **same one-dimensional stable-filter state `J`** that already generates the Chebyshev/Mertens selector ray in `RE-114`--`RE-116`.

In particular, if `D` is the first later nonpositive CA state, `V=\log D`, the corridor stays in a fixed multiplicative range `V\le AY`, and the selected amplitude is nondegenerate (`\lambda_Y\asymp1`), then with

\[
r_Y:=\log(V/Y)
\tag{10}
\]

one has

\[
\boxed{
J(U+r_Y)=o(1),
\qquad
\inf_{0\le s<r_Y}J(U+s)\ge-o(1).
}
\tag{11}
\]

The first-recovery condition therefore becomes, at edge scale, **first exit from a positive component of `J`**.

This stronger selector-plus-recovery condition is still spectrally noncoercive. For every fixed `b` in (3), there are constants

\[
\delta>0,
\qquad R<\infty,
\qquad m>0
\tag{12}
\]

and a syndetic set of phases `u` such that

\[
\boxed{
K_b(u):=J'(u)+(b-c)J(u)=0,
\qquad
J(u)\ge m,
}
\tag{13}
\]

and, if `r(u)` denotes the first zero of `J` to the right of `u`, then

\[
\boxed{
\delta\le r(u)\le R,
\qquad
J(u+s)>0\quad(0\le s<r(u)),
\qquad
J(u+r(u))=0.
}
\tag{14}
\]

At the start of every such packet,

\[
F(u)=bJ(u),
\qquad
G_\Theta(u)=(1-b)J(u),
\tag{15}
\]

so the exact sign-correct adaptive mixed ray and a bounded-logarithmic-distance first-recovery endpoint coexist on the **actual** attained edge face with bounded gaps in the start phase.

Consequently, adding coarse macroscopic first-recovery geometry to the leading finite-edge spectral model does not escape the obstruction of `RE-114`--`RE-116`. Any closing theorem must use information not contained in the leading profile `J`: arithmetic placement of actual CA selectors inside these lobes, a quantitative restriction on the lobe length corresponding to the actual recovery constant, or lower-order/discrete source information capable of deciding the crossing beyond the `Y^{-c}/\log Y` edge scale.

## 1. The event staircase gives a uniform macroscopic recovery expansion

`RE-113` gives the global edge projection

\[
\Phi(x^-)
=
x-x^\Theta\bigl(F(\log x)+r(x)\bigr),
\qquad
\sup_{x\ge X}|r(x)|\longrightarrow0.
\tag{16}
\]

For a crossed event group `e`, let

\[
\eta_e
\tag{17}
\]

be its event coordinate,

\[
u_e:=\Phi(\eta_e^-)
\tag{18}
\]

its physical left coordinate, and `m_e` its total `log p` mass. Its physical mass interval is

\[
I_e=(u_e,u_e+m_e].
\tag{19}
\]

As in `RE-109`, the intervals crossed between two CA states partition the corresponding physical logarithmic-size interval, and the exact Robin quadrature identity is

\[
\boxed{
h(C)-h(N)
=
\sum_e\int_{I_e}
\bigl(g(s)-g(\eta_e)\bigr)\,ds,
\qquad
g(x)=\frac1{x\log x}.
}
\tag{20}
\]

All crossed event coordinates are comparable with `Y` when `X\le AY`, because `\Phi(x)/x\to1`. Equation (16) then gives uniformly

\[
\eta_e-u_e
=
\eta_e^\Theta\bigl(F(\log\eta_e)+o(1)\bigr)
=O(Y^\Theta).
\tag{21}
\]

The physical width of one simultaneous event group is negligible on the edge scale. A first-layer event contributes `O(log Y)` mass. Every higher-layer event in the corridor is contained in the total higher-layer mass below `O(Y)`, which `RE-109` bounds by

\[
O\!\left(Y^{1/2}(\log Y)^{3/2}\right).
\tag{22}
\]

Since `Theta>1/2`,

\[
\boxed{
\max_e m_e=o(Y^\Theta).
}
\tag{23}
\]

For `s\in I_e`, equations (21)--(23), boundedness and uniform continuity of `F`, and `\eta_e/s\to1` uniformly therefore give

\[
\boxed{
\eta_e-u_e
=s^\Theta\bigl(F(\log s)+o(1)\bigr),
}
\tag{24}
\]

uniformly over the whole fixed multiplicative corridor.

Taylor-expand the integrand in (20):

\[
g(s)-g(\eta_e)
=-g'(s)(\eta_e-s)
+O\!\left(
\frac{(\eta_e-s)^2}{Y^3\log Y}
\right).
\tag{25}
\]

Because

\[
\eta_e-s=(\eta_e-u_e)-(s-u_e),
\tag{26}
\]

the internal position inside each event jump contributes at most

\[
\ll
\frac1{Y^2\log Y}
\sum_e m_e^2
\le
\frac{\max_e m_e}{Y^2\log Y}
\sum_e m_e
=o\!\left(\frac{Y^{\Theta-1}}{\log Y}\right).
\tag{27}
\]

The quadratic Taylor remainder contributes

\[
O\!\left(
\frac{Y\,Y^{2\Theta}}{Y^3\log Y}
\right)
=
O\!\left(\frac{Y^{2\Theta-2}}{\log Y}\right)
=o\!\left(\frac{Y^{\Theta-1}}{\log Y}\right),
\tag{28}
\]

because `Theta<1`.

Substituting (24) into the surviving first-order term yields, uniformly for every crossed CA endpoint `X\le AY`,

\[
h(C)-h(N)
=
\int_Y^X
[-g'(s)]s^\Theta
\bigl(F(\log s)+o(1)\bigr)\,ds
+o\!\left(\frac{Y^{\Theta-1}}{\log Y}\right).
\tag{29}
\]

Now

\[
-g'(s)
=
\frac1{s^2\log s}
+
\frac1{s^2(\log s)^2}.
\tag{30}
\]

With `s=Ye^v`, `U=\log Y`, and `c=1-Theta`, multiplication by `Y^c\log Y` turns the first term in (30) into

\[
\int_0^t
 e^{-cv}
 \frac{\log Y}{\log Y+v}
 F(U+v)\,dv,
\tag{31}
\]

while the second term is uniformly `o(1)` on `0\le t\le\log A`. This proves (6).

No smooth surrogate for the event staircase has been inserted. The only smoothing is the exact physical-mass partition already present in the quadrature identity; (23), (27), and (28) show that event discreteness is below the attained-edge scale on a fixed multiplicative corridor.

## 2. The adaptive selector turns the convolution into one shifted state

For the fixed-`b` adaptive witness, `RE-114` proves

\[
F(U)=b\lambda_Y+o(1),
\qquad
G_\Theta(U)=(1-b)\lambda_Y+o(1).
\tag{32}
\]

Since `J=F+G_Theta`,

\[
J(U)=\lambda_Y+o(1),
\tag{33}
\]

which is (7).

The definition (2) splits exactly at any `t\ge0`:

\[
\begin{aligned}
J(U)
&=\int_0^t e^{-cs}F(U+s)\,ds
 +\int_t^\infty e^{-cs}F(U+s)\,ds\\
&=\int_0^t e^{-cs}F(U+s)\,ds
 +e^{-ct}J(U+t).
\end{aligned}
\tag{34}
\]

Combining (6), (33), and (34) proves (9). The representation point is important: the recovery convolution does not add a third edge coordinate beside `F` and `G`. It is exactly the difference between two samples of the same stable-filter state,

\[
\boxed{
\int_0^t e^{-cs}F(U+s)\,ds
=J(U)-e^{-ct}J(U+t).
}
\tag{35}
\]

Any proposed leading-edge recovery observable built only from this macroscopic quadrature is therefore reconstructible from `J` and a shifted copy of `J`.

## 3. A first CA recovery becomes a first zero of the positive lobe

Let `D` be the first later CA state with `h(D)\le0`, and suppose `V=\log D\le AY`. Consider first the overshoot at the crossing. One event group changes the normalized profile in (9) by `o(1)`: directly from (20)--(24), its absolute contribution after multiplication by `Y^c\log Y` is

\[
\ll \frac{m_e}{Y}=o(1).
\tag{36}
\]

The previous CA state has positive height and `D` has nonpositive height, so

\[
\boxed{
Y^c\log Y\,h(D)=o(1).
}
\tag{37}
\]

Putting `t=r_Y` in (9) gives the first statement in (11).

The same jump estimate makes the crossed CA states an `o(1)` mesh in the logarithmic phase `t`: the largest physical increment is `m_e=o(Y)`, hence the largest change of `log(X/Y)` is `o(1)`. Every CA state before `D` has positive height. Uniform continuity of `J` and the uniform profile (9) therefore imply

\[
\inf_{0\le s<r_Y}J(U+s)\ge-o(1),
\tag{38}
\]

proving the second statement in (11).

In the fixed-constant near-minimal regime isolated by `RE-113`, `\lambda_Y\asymp1` and the finite-edge lower bound makes `V-Y\gg Y`; any fixed-constant upper recovery bound makes `V/Y=O(1)`. Thus (11) applies after choosing one fixed `A`, and the whole surviving recovery is, at leading order, an approximately positive `J`-lobe ending at an approximate zero.

This conclusion is stronger than the scalar workload budget of `RE-110`--`RE-112`: it identifies the complete normalized shape of the macroscopic recovery, not just its required length or maximum forward defect.

## 4. The actual edge face already supplies exact selector-plus-recovery lobes

It remains to test whether the extra first-zero requirement can obstruct the actual attained edge spectrum. It cannot at this level.

For fixed `b>c`, `RE-114` proves that the exact ray roots

\[
K_b(u)=J'(u)+(b-c)J(u)=0
\tag{39}
\]

with

\[
J(u)\ge m>0
\tag{40}
\]

form a syndetic set for some fixed `m`.

The same finding proves that `J` is a nonzero real uniformly almost-periodic function with zero Bohr mean. Hence it assumes a strictly negative value, and recurrence of one such value gives constants `a>0` and `R<\infty` such that every interval of length `R` contains a point `v` with

\[
J(v)\le-a.
\tag{41}
\]

Starting from any positive ray root `u`, continuity and (41) give a first zero to the right at distance at most `R`. Moreover

\[
J'(u)=cJ(u)-F(u)
\tag{42}
\]

shows that `J'` is bounded. If

\[
B:=\sup|J'|<\infty,
\tag{43}
\]

then the amplitude floor (40) prevents a zero before distance `m/B` (with the trivial constant-function case already excluded by the existence of negative values). Thus the first-zero distance satisfies (14) with, for example,

\[
\delta=m/B.
\tag{44}
\]

By definition of the first zero, `J` remains positive between the ray root and that endpoint. Finally, at a ray root,

\[
F(u)=bJ(u),
\qquad
G_\Theta(u)=(1-b)J(u),
\tag{45}
\]

so the lobe begins at exactly the sign-correct selector phase required by `RE-114`.

Since the start roots themselves are syndetic, these exact selector-plus-first-zero packets have bounded gaps in their start phase. A one-frequency control already exhibits the mechanism. If

\[
J(u)=A\cos(\gamma u+\phi),
\tag{46}
\]

then `K_b=0` selects a fixed point inside each positive cosine lobe and the next zero of `J` supplies the recovery endpoint. The identity (35) makes the accumulated Robin drop exactly the start amplitude at that endpoint.

The obstruction therefore does not rely on a complicated multi-zero conspiracy. It is built into the stable-filter representation itself.

## 5. Adversarial boundaries and falsification tests

The result does **not** say that actual CA selectors occur at the exact spectral packets in (13)--(14). It says the opposite kind of thing: the leading edge face cannot exclude them. Arithmetic placement remains untouched.

Nor does the compatibility theorem prescribe the recovery ratio. It gives

\[
1<e^\delta\le \frac VY\le e^R
\tag{47}
\]

for the matched spectral packets, not a chosen constant and not necessarily the special cap `V\le2Y` used in one formulation of `RE-113`. Therefore a theorem controlling the **actual first-zero distance** selected by CA geometry could still be new information. The present result rules out only the coarser hope that adding `L\asymp Y`, bounded multiplicative recovery, or positivity up to the first crossing automatically breaks leading-edge recurrence.

Three tests are decisive.

1. **Event-jump test.** If a simultaneous event group could carry mass comparable with `Y^Theta`, the internal-position error (27) would survive at edge scale. Equation (23), using the first/higher-layer decomposition already proved in the line, excludes this precisely because `Theta>1/2`.
2. **Second-order test.** The Taylor remainder is smaller than the edge scale by the factor `Y^(Theta-1)`. This is exactly where `Theta<1` is used; the argument does not extend to the separate `Theta=1` branch.
3. **Representation test.** Any claimed extra leading-order recovery coordinate must survive (35). If it is only a fixed-window quadrature of the edge discrepancy against the Robin kernel, it is a two-sample function of `J`, not independent source information.

The `Theta=1` Korobov--Vinogradov branch of `RE-109`--`RE-111` remains separate, as does the non-attained finite-edge branch already constrained by `RE-113`.

## 6. Prior art and novelty boundary

Mantovanelli's August 2026 prime-layer workload preprint is the closest representation-level prior art. Its exact packet identity writes the change of the Robin quotient between regular self-tangent CA states as the prime-layer workload integrated against the Robin kernel, and its finite companion verifies that bookkeeping on certified packets. No novelty is claimed here for the workload identity, the event-mass representation, or integration against `g'`.

Likewise, explicit-formula edge profiles and recurrence of uniformly almost-periodic functions are classical boundaries already recorded in `RE-113`--`RE-116`. A directed current search found no Robin/CA result that combines the hypothetical attained off-critical edge projection with the event staircase to obtain the uniform macroscopic profile (9), nor one identifying first recovery with a positive lobe of the same stable-filter state that generates the adaptive mixed ray.

The line-specific delta is therefore the **representation collapse** (35) plus its CA consequence (9)--(14): at the finite attained edge, the leading-order selector and the leading-order macroscopic recovery are not independent constraints. No new external theorem is load-bearing, so `SOURCES.md` requires no change.

## 7. Consequence for the research line

`RE-114` showed that the full attained edge realizes every fixed adaptive Chebyshev/Mertens ray. `RE-115`--`RE-116` showed that moving the exponent to the natural edge scale, including the exact self-consistent `1/log Y` drift, still does not create a spectral contradiction. The remaining suggestion was that inter-block recovery geometry might couple to the selector more rigidly.

At leading edge order, `RE-117` removes the coarse version of that escape. The recovery corridor itself is

\[
e^{-ct}J(U+t)
\tag{48}
\]

up to `o(1)` after normalization, and the actual edge face has syndetic sign-correct ray points lying inside positive `J` lobes whose first zeros occur a bounded positive logarithmic distance later.

The finite attained-edge frontier must therefore use something finer than **leading-edge selector plus bounded macroscopic recovery**. The remaining plausible information classes are arithmetic placement of CA states relative to the lobe geometry, a quantitative law for the actual recovery distance rather than mere `Theta(Y)` scale, or a lower-order/discrete source term that survives after the edge profile `J` has been quotiented out.