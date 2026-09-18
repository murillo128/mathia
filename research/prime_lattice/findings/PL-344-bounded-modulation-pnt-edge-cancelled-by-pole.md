# PL-344 — Bounded modulation already reaches the raw PNT edge, but the completed pole cancels it

**Evidence:** `EXACT-DERIVED + PNT + COMPLETED-POLE-MATCH + DECISIVE-NEGATIVE`

**Status:** `RAW-FIRST-HIT-CLOSED + ENDPOINT-LAYER-ONE-DIMENSIONALIZATION + COMPLETED-CANCELLATION + CENTERED-RECURRENCE-GATE-REMAINS + NO-RH-CONSEQUENCE`

## Precise claim

`PL-343` quantified the exponentially small Haar/time density of edge-scale values for the independently phased outer-prime endpoint observable, while deliberately leaving first-hit time open. For the actual one-parameter physical modulation, that raw first-hit problem has a simple deterministic answer: the `PL-341` endpoint weight collapses the dominant prime shell to an `O(1)` logarithmic boundary layer, and on that layer the many prime phases reduce to one elementary Fourier--Laplace profile.

Let

\[
c_a=\frac{e^{-a}}{1-e^{-a}},
\qquad
\delta_n=2a-\log n,
\]

and define the complexified `PL-343` endpoint response

\[
F_a(\tau)
:=c_a\sum_{e^a\le n<e^{2a}}
\Lambda(n)\,\delta_n\,e^{i\tau\log n},
\qquad
H_a(\tau)=\Re F_a(\tau).
\tag{PL344-1}
\]

Then for every fixed `T<infinity`, uniformly for `|tau|<=T`,

\[
\boxed{
F_a(\tau)
=
\frac{e^a}{1-e^{-a}}
\frac{e^{2ia\tau}}{(1+i\tau)^2}
+o_T(e^a).
}
\tag{PL344-2}
\]

Consequently, for every fixed `tau_0>=0` and every phase `phi`, there are choices

\[
\tau_a=\tau_0+O(a^{-1})
\]

with `2a tau_a = phi (mod 2 pi)` and hence

\[
\frac{H_a(\tau_a)}{e^a}
\longrightarrow
\Re\!\left(
\frac{e^{i\phi}}{(1+i\tau_0)^2}
\right).
\tag{PL344-3}
\]

Choosing `phi` to align or anti-align with `(1+i tau_0)^(-2)` gives

\[
\boxed{
H_a(\tau_a)
=
\pm\frac{e^a}{1+\tau_0^2}+o(e^a).
}
\tag{PL344-4}
\]

Thus, for every fixed `0<eta<1`, edge-scale values `|H_a|>=eta e^a` occur at uniformly bounded modulation times as `a->infinity` (choose `tau_0` with `(1+tau_0^2)^(-1)>eta`). The exponentially small long-time density in `PL-343` therefore cannot be converted into a large first-hit lower bound for the **raw** endpoint observable.

This does **not** produce a dangerous completed-Weil mode. On the same endpoint profiles, the zeta-pole quadratic form has exactly the same leading bounded-`tau` response,

\[
Q_{\rm pole}(M_\tau u_a^+)
=
\frac{e^a}{1-e^{-a}}
\Re\!\left(
\frac{e^{2ia\tau}}{(1+i\tau)^2}
\right)
+o_T(e^a),
\tag{PL344-5}
\]

with the convention that `M_tau` is modulation in the unscaled physical interval `(-a,a)`. The prime contribution to the completed form has the opposite sign, so

\[
\boxed{
Q_{\rm pole}(M_\tau u_a^+)-H_a(\tau)=o_T(e^a)
}
\tag{PL344-6}
\]

uniformly on bounded `tau`-sets. This is the moving-profile version of the canonical pole/PNT boundary cancellation in `PL-059`.

The RH-facing gate therefore moves one level deeper: not the first edge hit of the raw positive prime block, but the first order-one recurrence of the **canonically centered atomic-minus-PNT residual** after the pole mode has been removed. That distinction is exactly compatible with `PL-065`, whose large lower bound concerns strong weighted recurrence of the centered boundary defect rather than the universal raw PNT profile.

## 1. PNT turns the weighted prime shell into an elementary Laplace transform

Write

\[
\Psi(x)=\sum_{n\le x}\Lambda(n)=x+o(x).
\]

Equation (PL344-1) is the Stieltjes integral

\[
F_a(\tau)
=
c_a\int_{e^a}^{e^{2a}}
(2a-\log x)x^{i\tau}\,d\Psi(x),
\tag{PL344-7}
\]

up to the immaterial convention at the two endpoints. Put

\[
E(x)=\Psi(x)-x,
\qquad
\varepsilon_a:=\sup_{x\ge e^a}\frac{|E(x)|}{x}.
\]

The prime number theorem gives `epsilon_a->0`. For

\[
f_{a,\tau}(x)=(2a-\log x)x^{i\tau},
\]

integration by parts against `dE` gives, uniformly for `|tau|<=T`,

\[
\int_{e^a}^{e^{2a}} f_{a,\tau}(x)\,dE(x)
=o_T(e^{2a}).
\tag{PL344-8}
\]

Indeed the endpoint terms are bounded by `epsilon_a a e^a`, while

\[
|f'_{a,\tau}(x)|
\le
\frac{1+T(2a-\log x)}x,
\]

and therefore

\[
\int_{e^a}^{e^{2a}}|E(x)f'_{a,\tau}(x)|\,dx
\le
\varepsilon_a
\int_{e^a}^{e^{2a}}
\bigl(1+T(2a-\log x)\bigr)\,dx
=o_T(e^{2a}).
\]

Hence

\[
F_a(\tau)
=
c_a\int_{e^a}^{e^{2a}}
(2a-\log x)x^{i\tau}\,dx
+o_T(e^a).
\tag{PL344-9}
\]

Set `u=2a-log x`. Then

\[
\begin{aligned}
\int_{e^a}^{e^{2a}}
(2a-\log x)x^{i\tau}\,dx
&=
e^{2a(1+i\tau)}
\int_0^a u e^{-(1+i\tau)u}\,du\\
&=
e^{2a(1+i\tau)}
\frac{1-(1+(1+i\tau)a)e^{-(1+i\tau)a}}
{(1+i\tau)^2}.
\end{aligned}
\tag{PL344-10}
\]

Since `c_a=e^{-a}/(1-e^{-a})`, the truncated-tail term contributes only `O_T(a)` after normalization, and (PL344-2) follows.

This derivation uses only the PNT for the finite von-Mangoldt shell. No Euler product is continued, and no zero information is inserted.

## 2. The high-dimensional torus collapses on the dominant endpoint layer

The asymptotic has a direct geometric interpretation. Put again

\[
u=2a-\log n.
\]

After the `PL-341` endpoint profile cancels the square-root Weil weight, the PNT density contributes an `e^{-u}` factor. Hence the normalized raw edge is carried by `u=O(1)`, even though the full outer shell has logarithmic thickness `a`.

On this dominant layer,

\[
e^{i\tau\log n}
=e^{2ia\tau}e^{-i\tau u}.
\]

Thus the observable does not require a positive-density set of independent prime coordinates to align near the torus identity. Its leading value is the one-dimensional endpoint transform

\[
\int_0^\infty u e^{-(1+i\tau)u}\,du
=\frac1{(1+i\tau)^2},
\tag{PL344-11}
\]

multiplied by the global phase `e^(2ia tau)`.

This does not contradict `PL-343`. For each **fixed** `a`, unique ergodicity still implies that edge-scale values occupy exponentially small asymptotic density along the infinite-time Kronecker orbit. A tiny-density set can nevertheless be hit very early. Equations (PL344-2)--(PL344-4) identify precisely such an early family as `a` varies. Nor does this replace `PL-342`: the essential-spectrum argument there keeps `a` fixed and sends the modulation to infinity, whereas the present statement is a joint `a->infinity` bounded-physical-frequency asymptotic.

## 3. The same endpoint transform is exactly the zeta-pole mode

The early raw edge is universal PNT structure, not an atomic recurrence residual. This can be checked directly on the pole term rather than inferred heuristically.

Work on the physical interval `(-a,a)` and put `N_a=1-e^{-a}`. The normalized endpoint functions corresponding under dilation to the `PL-341` vectors are

\[
f_a(-a+s)=N_a^{-1/2}e^{-s/2},
\qquad
g_a(a-t)=N_a^{-1/2}e^{-t/2},
\qquad 0<s,t<a,
\tag{PL344-12}
\]

with `u_a^+=(f_a+g_a)/sqrt(2)`. Let

\[
(M_\tau v)(x)=e^{i\tau x}v(x).
\]

As in `PL-059`, define

\[
V_{\pm1/2}(v)=\int v(x)e^{\pm x/2}\,dx,
\qquad
Q_{\rm pole}(v)
=2\Re\bigl(V_{1/2}(v)\overline{V_{-1/2}(v)}\bigr).
\tag{PL344-13}
\]

For `v=M_tau u_a^+`, direct integration gives

\[
V_{1/2}(v)
=\frac1{\sqrt{2N_a}}
\left[
 e^{-a/2-ia\tau}J_a(\tau)
 +e^{a/2+ia\tau}A_a(\tau)
\right],
\tag{PL344-14}
\]

where

\[
A_a(\tau)=\frac{1-e^{-(1+i\tau)a}}{1+i\tau},
\qquad
J_a(\tau)=\int_0^a e^{i\tau s}\,ds.
\tag{PL344-15}
\]

Symmetry gives `overline(V_(-1/2)(v))=V_(1/2)(v)`. Therefore

\[
Q_{\rm pole}(v)
=\frac1{N_a}
\Re\!\left[
\left(
 e^{a/2+ia\tau}A_a(\tau)
 +e^{-a/2-ia\tau}J_a(\tau)
\right)^2
\right].
\tag{PL344-16}
\]

Uniformly for bounded `tau`, `A_a(tau)=(1+i tau)^(-1)+O_T(e^{-a})` and `|J_a(tau)|<=a`. Hence

\[
Q_{\rm pole}(M_\tau u_a^+)
=
\frac{e^a}{N_a}
\Re\!\left(
\frac{e^{2ia\tau}}{(1+i\tau)^2}
\right)
+O_T(a),
\tag{PL344-17}
\]

which is (PL344-5). Taking real parts in (PL344-2) shows that the raw prime endpoint quotient has the same leading term. Since the completed Weil form contains the pole and prime pieces with opposite signs, their difference is `o_T(e^a)`.

This is stronger than merely observing that `PL-059` cancels one unmodulated rank-one vector: the entire bounded-physical-frequency family selected by the `PL-341` endpoint layer is swallowed by the same completed pole/PNT mechanism.

## 4. What survives after completion

The raw first-hit question proposed at the end of `PL-343` is therefore not the correct quantitative gate for the completed problem. There are two distinct mechanisms:

- the **universal endpoint continuum mode**, which already gives `Theta(e^a)` values at bounded physical modulation and is canceled by the zeta pole;
- the **centered atomic recurrence defect**, which survives compact/pole completion and requires genuinely nonuniform prime-phase information.

`PL-065` addresses the second mechanism. Its observable is explicitly the atomic boundary shell minus the PNT continuum model. Strong weighted coherence of that centered defect forces modulation beyond its zero-free sampling barrier. Equation (PL344-6) explains why the bounded-`tau` family found here does not contradict that result: after canonical completion its leading term is gone.

Accordingly, the next useful quantitative question is not

\[
\text{how early can }|H_a(\tau)|\asymp e^a\text{ occur?}
\]

That answer is now bounded time. The surviving question is whether a moving family can make the **completed centered residual plus archimedean/scalar sector** compete at low spectral energy, and whether any such family survives the zero-free sampling barriers and matched generalized-prime controls already established in `PL-061`--`PL-066`.

## 5. Adversarial, matched-control, and novelty audit

**No conflict with Haar rarity.** `PL-343` is a fixed-`a`, long-time density theorem. The present result is a joint large-`a` first-hit construction. Density does not imply first-return bounds, and `PL-343` explicitly warned against that inference.

**No conflict with essential-spectrum recurrence.** `PL-342` needs modulation tending to infinity at fixed aperture to produce weakly-null vectors and a Calkin witness. Bounded physical modulation while `a->infinity` is a different limit and does not alter the fixed-`a` essential-spectrum statement.

**No completed-Weil negative direction.** The leading prime response is canceled by the pole on exactly the same states. Nothing here proves negativity, positivity failure, a low eigenvalue, or any statement equivalent to RH.

**Matched generalized-prime control.** The asymptotic (PL344-2) uses only `Psi(x)=x(1+o(1))`. Any generalized-prime system with the same PNT law has the same bounded-modulation raw endpoint profile. If its completed explicit formula contains the matching simple-pole main term, the same leading cancellation occurs. The mechanism is therefore universal residue/PNT geometry, not rational-prime rigidity.

**Analytic-continuation boundary.** The prime calculation is a finite von-Mangoldt sum plus PNT partial summation. The pole calculation is performed directly in the already-completed Weil functional. No identity for an Euler product is used outside `Re(s)>1`.

**Prior-art audit.** The twisted PNT asymptotic used here is an elementary consequence of `Psi(x)~x` by Stieltjes partial summation; no novelty is claimed for it. The pole-versus-PNT cancellation is classical explicit-formula structure and was already isolated operatorially in `PL-059`, anchored there to Weil, Bombieri, and Suzuki in `SOURCES.md`. A targeted literature search around von-Mangoldt Mellin twists, logarithmic endpoint weights, and Weil pole/prime cancellation did not locate this exact moving `PL-341` endpoint specialization. Search absence is not treated as evidence of originality. The durable contribution is the line-specific negative redirect: `PL-343`'s raw first-hit gate collapses to bounded modulation, and those early edge values are exactly the universal component removed by completion.

## Consequence for the research line

The endpoint ledger is now sharper:

\[
\text{raw prime edge at bounded physical modulation}
\quad\sim\quad
\text{PNT endpoint Laplace mode}
\quad\stackrel{\text{pole}}{\longrightarrow}\quad
0
\quad\text{at leading }e^a\text{ scale}.
\]

What remains noncompact and potentially relevant is the centered atomic discrepancy, not the raw edge. Future recurrence estimates should therefore be formulated directly for the completed/centered residual. Haar rarity of the independently phased raw observable is still a correct prevalence statement, but it is no longer a candidate first-hit mechanism for controlling the completed operator.