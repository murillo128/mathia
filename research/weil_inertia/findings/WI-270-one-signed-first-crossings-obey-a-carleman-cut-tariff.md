# WI-270 — one-signed first crossings obey a Carleman cut tariff

## Status

- **Evidence:** `EXACT-DERIVED + CLASSICAL-HILBERT-CARLEMAN + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** a quantitative necessary condition on the **one-signed branch** of a hypothetical first unrestricted Suzuki null mode. It turns the signed-source PSD family of `WI-269` into a pointwise-in-cut alternative: either a cut sees positive prime-power overlap, or the mode must carry a definite amount of short-range mass on both sides of that cut. Under complete prime-lag screening this becomes an explicit local-concentration constraint. It does not prove RH and does not control sign-changing null modes.
- **Novelty boundary:** the Carleman/Hilbert integral inequality and its sharp constant `pi` are classical. Suzuki supplies the localized Weil form; `WI-253`/`WI-269` supply firstness and the exact source-ground-state transform. The Mathia deduction is their cutwise combination with the unique sign change of the zeta archimedean source, yielding the tariff (12) and screened concentration consequences (14)--(16). No priority claim is made.

## Claim

Assume RH is false and let

\[
a=a_*:=\inf\{r>0:\lambda_r\le0\}
\]

be the first global crossing of Suzuki's unrestricted localized Weil ground-state energy. Let `v` be a normalized real null mode

\[
\|v\|_2=1,\qquad A_av=0,\qquad q_a\ge0,
\tag{1}
\]

extended by zero outside `(-a,a)`. In this finding assume the one-signed branch; after replacing `v` by `-v` if necessary,

\[
v\ge0\quad\text{a.e.}
\tag{2}
\]

For `h>0` use the exact source weight from `WI-269`,

\[
w(h)=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2},
\tag{3}
\]

and let `h_0=\log\rho`, where `\rho^3-\rho-1=0`. Then

\[
w(h)>0\quad(0<h<h_0),\qquad
w(h)<0\quad(h>h_0).
\tag{4}
\]

For a cut `t\in(-a,a)` define

\[
J_t(h):=\int_{t-h}^{t}v(x+h)v(x)\,dx\ge0,
\tag{5}
\]

\[
P_t:=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}J_t(\log n),
\tag{6}
\]

and the total and short local masses

\[
M_L(t)=\int_{-a}^{t}v(x)^2dx,\qquad
M_R(t)=\int_t^a v(x)^2dx,
\tag{7}
\]

\[
m_L(t)=\int_{t-h_0}^{t}v(x)^2dx,\qquad
m_R(t)=\int_t^{t+h_0}v(x)^2dx.
\tag{8}
\]

Write

\[
r_L(t)=\frac{a+t}{2},\qquad r_R(t)=\frac{a-t}{2}.
\tag{9}
\]

For almost every cut `t`, the two sharp truncations belong to the localized form domain, and the null equation gives the common cut energy

\[
Q_t
:=q_a(v\,1_{(-\infty,t)})
=q_a(v\,1_{(t,\infty)})
=P_t+\int_0^{2a}w(h)J_t(h)\,dh.
\tag{10}
\]

Firstness and translation invariance imply

\[
Q_t\ge
\max\!\left\{
\lambda_{r_L(t)}M_L(t),
\lambda_{r_R(t)}M_R(t)
\right\}.
\tag{11}
\]

The positive short-range archimedean term can be bounded by the classical Carleman operator, while the long-range archimedean term has the favorable sign. Therefore every admissible cut satisfies the exact tariff

\[
\boxed{
P_t+\frac{\pi}{2}\sqrt{m_L(t)m_R(t)}
\ge
\max\!\left\{
\lambda_{r_L(t)}M_L(t),
\lambda_{r_R(t)}M_R(t)
\right\}.
}
\tag{12}
\]

Thus a one-signed first null mode cannot simultaneously make the prime cut overlap small and evacuate short-range mass from one side of the same cut.

In particular, suppose the mode completely screens every active prime-power autocorrelation,

\[
C_v(\log n)
:=\int_{\mathbb R}v(x+\log n)v(x)dx=0
\qquad(\log n<2a,\ \Lambda(n)>0).
\tag{13}
\]

Because `v>=0`, (13) forces `v(x+\log n)v(x)=0` a.e. at every active prime-power lag, hence `P_t=0` for every cut. Then for almost every admissible `t`,

\[
\boxed{
m_L(t)m_R(t)
\ge
\frac{4}{\pi^2}
\max\!\left\{
\lambda_{r_L(t)}^2M_L(t)^2,
\lambda_{r_R(t)}^2M_R(t)^2
\right\}.
}
\tag{14}
\]

There is in particular a median `t_0` with `M_L(t_0)=M_R(t_0)=1/2` for which

\[
\boxed{
m_L(t_0)m_R(t_0)
\ge
\left(\frac{\lambda_{a/2}}{\pi}\right)^2.
}
\tag{15}
\]

Since `a/2<a`, firstness gives `\lambda_{a/2}>0`. Complete prime screening on the one-signed branch therefore forces quantitatively nonzero `L^2` mass within distance `h_0` on **both** sides of a median cut. More generally, (14) is a local propagation constraint at almost every cut.

A topological corollary is that a completely prime-screened one-signed first mode cannot have an internal essential-support gap of length at least `2h_0` separating positive mass on its two sides: choosing an admissible cut in the middle of such a gap makes `m_Lm_R=0` while the right side of (14) is positive.

## 1. Sharp half-cuts are admissible almost everywhere

The indicator multiplier is not assumed admissible at an arbitrary prescribed cut. The needed almost-everywhere statement follows by the same layer-cake mechanism used for the sharp radial cutoffs in `WI-251`, now in its simpler one-sided form.

Let `H_t(x)=1_{x>t}`. For fixed `x,y`,

\[
\int_{\mathbb R}|H_t(x)-H_t(y)|^2dt=|x-y|.
\tag{16}
\]

The positive mean-form kernels in `WI-269` are exponentially decaying resolvent kernels `K_\alpha(x-y)`. Integrating the additional jump contribution of `H_tv` over `t\in(-a,a)` therefore introduces the finite first moment

\[
\int_{\mathbb R}|h|K_\alpha(h)\,dh<\infty.
\]

The part where both points lie on the same side is controlled by the original form energy of `v`. At fixed aperture the prime/density source perturbation is `L^2`-bounded, as used already in `WI-269`. Hence

\[
H_tv,\ (1-H_t)v\in\operatorname{Dom}(q_a)
\]

for almost every `t`. For such a cut the weak null equation gives

\[
q_a(v,H_tv)=q_a(v,(1-H_t)v)=0.
\]

Using `H_t^2=H_t`, the ground-state-transform algebra of `WI-269` extends to the sharp cut and leaves exactly the edges crossing `t`. This is (10). The two complementary cuts have the same squared multiplier difference, hence the same `Q_t`.

No pointwise regularity of `v` or endpoint trace is used.

## 2. Firstness supplies the lower side of the tariff

The left truncation is supported in an interval of length `a+t`, hence radius `r_L=(a+t)/2`; the right truncation is supported in an interval of radius `r_R=(a-t)/2`. Both radii are strictly below `a` for an interior cut. By translation invariance of the global Weil form and the definition of the first crossing,

\[
q_a(vH_t)\ge\lambda_{r_R}\|vH_t\|_2^2
=\lambda_{r_R}M_R,
\]

and similarly

\[
q_a(v(1-H_t))\ge\lambda_{r_L}M_L.
\]

Since both energies equal `Q_t`, (11) follows. This is the part of the argument that uses **firstness**, not merely `q_a>=0`.

The monotonicity from domain inclusion gives `\lambda_r\ge\lambda_{a/2}` whenever `r\le a/2`. At every cut one of `r_L,r_R` is at most `a/2`, which will be used for the median consequence.

## 3. The short positive archimedean source is a Carleman kernel

On `(0,h_0)`,

\[
0<w(h)<\kappa(h)
=\frac{e^{-h/2}}{e^{2h}-1}
\le\frac1{2h},
\tag{17}
\]

because `e^{2h}-1>=2h`. Since `J_t(h)>=0` and `w(h)<0` for `h>h_0`, (10) yields

\[
Q_t
\le P_t+
\frac12\int_0^{h_0}\frac1h
\int_{t-h}^{t}v(x+h)v(x)\,dx\,dh.
\tag{18}
\]

Put `u=t-x` and `y=x+h-t`, so `u,y>=0` and `h=u+y`. Then the continuous term in (18) is at most

\[
\frac12
\int_0^{h_0}\!\int_0^{h_0}
\frac{v(t-u)v(t+y)}{u+y}\,du\,dy.
\tag{19}
\]

The classical Hilbert--Carleman integral inequality gives

\[
\int_0^\infty\!\int_0^\infty
\frac{f(u)g(y)}{u+y}\,du\,dy
\le\pi\|f\|_2\|g\|_2.
\tag{20}
\]

For completeness, the constant needed here follows directly from Schur's test with weight `p(x)=x^{-1/2}`:

\[
\int_0^\infty\frac{p(y)}{x+y}dy
=\pi p(x),
\]

using `\int_0^\infty t^{-1/2}(1+t)^{-1}dt=\pi`. Applying (20) to the restrictions of `v(t-u)` and `v(t+y)` to `[0,h_0]` gives

\[
Q_t\le P_t+\frac\pi2\sqrt{m_L(t)m_R(t)}.
\tag{21}
\]

Combining (11) and (21) proves (12).

The constant `pi` is not a zeta-specific estimate. The Carleman operator

\[
(Cf)(x)=\int_0^\infty\frac{f(y)}{x+y}dy
\]

has spectrum `[0,pi]`; see D. R. Yafaev, **Spectral and scattering theory for perturbations of the Carleman operator**, arXiv:1210.5709v2 (2012), equations (1.2)--(1.4). Thus improving the `pi/2` term for arbitrary `L^2` functions would require extra structure of the Suzuki null mode, not a better generic integral inequality.

## 4. Complete screening converts the tariff into local mass

Under (13), nonnegativity of the integrand implies each active translated product vanishes almost everywhere. Hence every prime crossing term `J_t(log n)` vanishes, not merely its center average. Setting `P_t=0` in (12) gives (14).

To obtain (15) without assuming that a particular median cut itself belongs to the almost-everywhere sharp-cut domain, fix `delta>0`. The cumulative mass `M_L(t)` is continuous and runs from `0` to `1`, so the set

\[
\{t:|M_L(t)-1/2|<\delta\}
\]

is a nonempty open set. Choose an admissible cut `t_delta` in it. One of its two support radii is at most `a/2`, and both corresponding side masses are at least `1/2-delta`; therefore (14) gives

\[
m_L(t_\delta)m_R(t_\delta)
\ge
\left(\frac{(1-2\delta)\lambda_{a/2}}{\pi}\right)^2.
\tag{22}
\]

Choose a convergent subsequence as `delta->0`. Continuity under translation of the `L^1` function `v^2` makes `m_L(t)` and `m_R(t)` continuous, and the limiting cut has `M_L=M_R=1/2`. Passing to the limit proves (15).

The support-gap corollary follows directly from (14): in a gap of length at least `2h_0`, an interior admissible cut can be chosen whose two `h_0`-neighborhoods contain no mass, while positive mass on both sides makes both truncated supports nonzero and firstness gives a positive right-hand side.

## 5. What this does and does not buy

`WI-267` proves that the exact Suzuki null equation forbids a support gap untouched by active prime translations, but support activity alone does not force a nonzero prime autocorrelation. `WI-269` strengthens the interface to a PSD signed-source Laplacian but leaves open whether long-range negative archimedean edges can screen all arithmetic overlap.

Equation (12) identifies a sharper one-signed obstruction. Long-range negative archimedean coupling cannot help a cut pay its strictly positive firstness cost: after dropping it, the only remaining currencies are **prime crossing overlap** and **short-range archimedean mass on both sides of the cut**. If the arithmetic currency is set identically to zero, (14)--(15) force quantitative spatial concentration instead of allowing a purely topological screen.

This is a possible bootstrap interface rather than a contradiction. The number `\lambda_{a/2}` is positive but no useful uniform lower bound is asserted here; a screened mode could in principle satisfy the tariff by concentrating enough mass around every relevant cut. The next decisive question is therefore source-specific: can the Suzuki null equation and the family (14) propagate this forced local mass until it collides with a prime-power translate, or can one construct a genuine null geometry that remains one-signed, prime-screened, and Carleman-concentrated?

The sign assumption is load-bearing. For sign-changing `v`, `J_t(h)` is no longer nonnegative and the step dropping the `h>h_0` part is invalid; `WI-269`'s nodal tariff remains the appropriate constraint there. Likewise, no conjectural correlation, wider Fourier support, or unproved zeta statistic is used.

## 6. Prior-art and novelty audit

- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), is the primary source for the localized Weil form and first-crossing operator framework. This finding uses it only through the source decomposition and firstness already audited in `WI-253` and `WI-269`.
- D. R. Yafaev, **Spectral and scattering theory for perturbations of the Carleman operator**, arXiv:1210.5709v2 (2012), records the classical Carleman operator with kernel `(x+y)^{-1}`, diagonalizes it by Mellin transform, and gives spectrum `[0,pi]`. The inequality (20) is also proved directly above by Schur's test.
- A targeted search for `Suzuki + Weil quadratic form + Carleman`, localized-Weil multiplier cuts, and equivalent Hilbert-kernel formulations located Suzuki's operator paper and general Carleman/Hankel literature, but no matching zeta-specific cut tariff. Search absence is context only and is not used as evidence of priority.
- Local duplication audit: `WI-251` supplies the sharp-cut layer-cake precedent; `WI-253` supplies first-crossing localization; `WI-267` shows why support coverage is weaker than overlap; `WI-269` supplies the exact signed-source multiplier transform. None of them contains the Carleman overlap-versus-concentration inequality (12) or the screened mass bound (15).

## Research consequence

The accepted first-crossing clue can now be split more sharply. On the **one-signed** branch, complete prime screening is no longer a free cancellation scenario: it must satisfy the cutwise concentration family (14), with the explicit median cost (15). Any future positive argument can try to feed that forced local mass back into the Suzuki null equation to obtain an actual prime overlap. The **sign-changing** branch remains governed by `WI-269`'s opposite-sign tariff and still requires a different effective-resistance/source argument.
