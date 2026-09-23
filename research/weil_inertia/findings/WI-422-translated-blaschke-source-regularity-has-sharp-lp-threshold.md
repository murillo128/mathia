# WI-422 — Translated-Blaschke source regularity has a sharp `L^p` threshold at `p=2`

**Status:** `CLASSICAL-ANALYSIS + EXACT-DERIVED + STRUCTURAL-CONSTRAINT + DECISIVE-NEGATIVE`.

**Parents:** [WI-416](./WI-416-oracle-blaschke-targeting-has-zero-tv-infimum.md), [WI-417](./WI-417-bounded-density-restores-shallow-depth-blaschke-coercivity.md), [WI-421](./WI-421-carleson-regularity-still-has-zero-oracle-blaschke-cost.md).

## Claim

WI-421 shows that excluding no atoms is fatal: any source gauge that gives uniformly finite cost to point masses still has zero oracle cost on a finite defect set. A natural next question is whether replacing atomic measures by absolutely continuous source densities with a fixed `L^p` budget is automatically enough. It is not. The translated-Blaschke kernel has a sharp two-dimensional integrability threshold at `p=2`, and the obstruction above that threshold is no longer atomic concentration but diffuse far-field mass.

For

\[
q_{a,b}(\gamma,d)
=\frac12\log
\frac{(\gamma-b)^2+(a+d)^2}
     {(\gamma-b)^2+(a-d)^2},
\qquad a,d>0,
\tag{1}
\]

write `q_d` for the source-plane function `(a,b)\mapsto q_{a,b}(\gamma,d)`. Its distribution function, already obtained in WI-417, is

\[
\left|\{q_d>t\}\right|
=\pi d^2\operatorname{csch}^2 t.
\tag{2}
\]

Therefore its decreasing rearrangement is exactly

\[
\boxed{
q_d^*(u)
=\operatorname{arsinh}\frac{\sqrt\pi\,d}{\sqrt u},
\qquad u>0.
}
\tag{3}
\]

This yields the exact moment law

\[
\boxed{
\int q_d^s\,da\,db
=
\pi\,2^{2-s}\Gamma(s+1)\zeta(s-1)\,d^2,
\qquad s>2,
}
\tag{4}
\]

and the integral diverges for `0<s\le2`. At the endpoint,

\[
\boxed{
\|q_d\|_{L^{2,\infty}}
:=\sup_{t>0}t\,|\{q_d>t\}|^{1/2}
=\sqrt\pi\,d,
}
\tag{5}
\]

while `q_d\notin L^{2,r}` for every finite Lorentz index `r`.

Let `1\le p\le\infty` and let `p'` be the Hölder conjugate. The linear response

\[
f\longmapsto\int q_df
\tag{6}
\]

is bounded on the bare global source space `L^p((0,\infty)\times\mathbb R)` **if and only if**

\[
\boxed{1<p<2.}
\tag{7}
\]

For `1<p<2`, putting `s=p'>2`, its exact operator norm is

\[
\boxed{
\|q_d\|_{L^s}
=
\left[
\pi\,2^{2-s}\Gamma(s+1)\zeta(s-1)
\right]^{1/s}
 d^{2/s}.
}
\tag{8}
\]

For `p=2`, ordinary `L^2` control fails despite absolute continuity and complete exclusion of atoms; the kernel is only weak-`L^2`. For every `p>2`, and also for `p=\infty`, a fixed `L^p` norm can produce arbitrarily large target response by spreading source mass farther and farther through the half-plane. For `p=1`, the logarithmic pole makes the response unbounded by concentrating an absolutely continuous bump near the target.

Thus **atom exclusion is necessary but not sufficient for a one-norm source theory**. The critical obstruction at `p=2` comes from the `1/r` Green-function tail over a two-dimensional source plane, not from the local logarithmic singularity.

There is, however, a sharp endpoint repair. From (3),

\[
q_d^*(u)
\le \sqrt\pi\,d\,u^{-1/2}.
\tag{9}
\]

Hence Hardy--Littlewood rearrangement gives

\[
\boxed{
\int q_d|f|
\le
\sqrt\pi\,d
\int_0^\infty u^{-1/2}f^*(u)\,du.
}
\tag{10}
\]

So the Lorentz endpoint `L^{2,1}` controls a target even though `L^2` does not. This identifies the exact source-space side of the weak-`L^2` threshold without invoking a zeta-specific hypothesis.

Finally, when the source theory also retains the finite-TV budget that motivated WI-416--WI-417, **every** `L^p` density constraint with `p>1` restores positive one-target TV coercivity. The shallow-depth cost has three sharply different regimes: subcritical `1<p<2` eventually makes a fixed target quantum impossible, critical `p=2` forces exponential TV cost, and supercritical `p>2` forces a precise polynomial TV cost whose `p=\infty` limit recovers WI-417.

No zeta source measure is proved here to satisfy any of these `L^p` bounds. The result is a source-regularity classification for the translated-Blaschke mechanism, not an RH conclusion.

## 1. Exact distribution, rearrangement, and moments

Equation (2) gives `u=\pi d^2\operatorname{csch}^2 t`. Solving for `t` yields

\[
\sinh t=\frac{\sqrt\pi\,d}{\sqrt u},
\]

which proves (3).

For `s>0`, layer cake gives

\[
\int q_d^s
=s\int_0^\infty t^{s-1}|\{q_d>t\}|\,dt
=
\pi d^2 s\int_0^\infty t^{s-1}\operatorname{csch}^2t\,dt.
\tag{11}
\]

Near `t=0`, `\operatorname{csch}^2t\sim t^{-2}`, so (11) converges exactly when `s>2`; the logarithmic target singularity causes no additional restriction. For `s>2`, use

\[
\operatorname{csch}^2t
=4\sum_{n\ge1}n e^{-2nt}
\tag{12}
\]

and monotone convergence to obtain

\[
\begin{aligned}
\int q_d^s
&=4\pi d^2s
\sum_{n\ge1}n
\int_0^\infty t^{s-1}e^{-2nt}\,dt\\
&=\pi d^2\,2^{2-s}\Gamma(s+1)
\sum_{n\ge1}n^{1-s},
\end{aligned}
\]

which is (4).

For weak `L^2`, (2) gives

\[
t^2|\{q_d>t\}|
=
\pi d^2\left(\frac{t}{\sinh t}\right)^2
<\pi d^2,
\]

with equality in the supremum as `t\downarrow0`; this proves (5). Since `t|\{q_d>t\}|^{1/2}\to\sqrt\pi d` at the low-value tail, every finite secondary Lorentz exponent has the logarithmically divergent `dt/t` integral, so `q_d\notin L^{2,r}` for finite `r`.

## 2. The bare `L^p` phase transition

Let `1<p<\infty`, `s=p'`. Hölder shows

\[
\left|\int q_df\right|
\le \|q_d\|_s\|f\|_p.
\tag{13}
\]

By ordinary `L^p` duality this response functional is bounded exactly when `q_d\in L^s`, namely exactly when `s>2`, equivalently `1<p<2`. Formula (8) follows from (4). Compact truncations of the Hölder extremizer show sharpness even if one additionally insists that the test density have finite TV.

The failure outside this interval has two distinct causes.

For `p=1`, `s=\infty`, and `q_d` is unbounded at `(a,b)=(d,\gamma)`. Unit-`L^1` densities supported on successively smaller disks around that point have responses tending to infinity.

For `p\ge2`, the problem is instead the far field. In polar coordinates centered at `(0,\gamma)` inside the source half-plane,

\[
q_d(a,b)
=\frac{2ad}{a^2+(b-\gamma)^2}+O_d(r^{-2})
=\frac{2d\cos\theta}{r}+O_d(r^{-2}).
\tag{14}
\]

Thus `q_d\notin L^{p'}` when `p'\le2`. For `p>2`, one may put a normalized `L^p` density on expanding half-annuli; its response grows like a positive constant times `dR^{1-2/p}`. At `p=2`, one may equivalently take normalized compact truncations of `q_d`: because `\int q_d^2=\infty`, their unit-`L^2` responses tend to infinity. These constructions are diffuse and absolutely continuous. They survive every rule whose only purpose is to forbid source atoms.

The endpoint (10) follows directly from Hardy--Littlewood rearrangement and `\operatorname{arsinh}x\le x`. It is the natural Lorentz strengthening of `L^2` suggested by the exact weak-`L^2` kernel.

## 3. Exact finite-TV reduction under an `L^p` source budget

Now fix `1<p<\infty`, an `L^p` budget `C>0`, and a required response `Q>0`. Define

\[
\mathcal M_{p,C}(d,Q)
:=
\inf\left\{
\|f\|_1:
\|f\|_p\le C,
\left|\int q_df\right|\ge Q
\right\},
\tag{15}
\]

where `f` ranges over absolutely continuous finite-TV source densities. Because `q_d\ge0`, replacing `f` by `|f|` cannot increase either norm and cannot decrease the upper bound on absolute response, so it suffices to take `f\ge0`.

Put `s=p'` and, for `k>0`,

\[
J_k(t)
:=
\int (q_d-t)_+^k\,da\,db
=
\pi d^2\,j_k(t),
\tag{16}
\]

where layer cake and (2) give

\[
\boxed{
j_k(t)
=k\int_t^\infty
(u-t)^{k-1}\operatorname{csch}^2u\,du.
}
\tag{17}
\]

For every `t>0` and every admissible `f` with `M=\|f\|_1`,

\[
\begin{aligned}
\int q_df
&\le tM+\int(q_d-t)_+f\\
&\le tM+CJ_s(t)^{1/s}.
\end{aligned}
\tag{18}
\]

This family is sharp. Define

\[
f_t
=CJ_s(t)^{-1/p}(q_d-t)_+^{s-1}.
\tag{19}
\]

Then `\|f_t\|_p=C`, and

\[
\boxed{
M_t
=C(\pi d^2)^{1/s}
 j_{s-1}(t)j_s(t)^{-1/p},
}
\tag{20}
\]

\[
\boxed{
Q_t
=C(\pi d^2)^{1/s}
\bigl(j_s(t)+t j_{s-1}(t)\bigr)
 j_s(t)^{-1/p}.
}
\tag{21}
\]

Equality holds in both steps of (18) for `f_t`. As `t` varies, (20)--(21) therefore give the exact supporting family for the one-target TV capacity. In particular, whenever the requested `Q` lies in the feasible range, the unique threshold selected by `Q_t=Q` yields the sharp capacity `\mathcal M_{p,C}(d,Q)=M_t`. This is the `L^p` analogue of WI-417's `L^\infty` bathtub extremizer; the hard cutoff is replaced by a power of the excess kernel.

## 4. The three shallow-depth regimes

The exact reduction makes the shallow limit transparent.

### Subcritical source norms: `1<p<2`

Here `s=p'>2`. Even without a TV constraint, (8) gives the exact maximal response under `\|f\|_p\le C`:

\[
\sup_{\|f\|_p\le C}
\left|\int q_df\right|
=
C K_s d^{2/s},
\tag{22}
\]

where

\[
K_s
=
\left[
\pi\,2^{2-s}\Gamma(s+1)\zeta(s-1)
\right]^{1/s}.
\tag{23}
\]

Thus for fixed `C,Q>0`, all sufficiently shallow targets are **infeasible**, independently of how much TV mass is allowed:

\[
C K_s d^{2/s}<Q
\quad\Longrightarrow\quad
\mathcal M_{p,C}(d,Q)=+\infty.
\tag{24}
\]

### Critical source norm: `p=2`

Now `s=2`. The needed truncated moments are elementary:

\[
j_1(t)=\coth t-1,
\qquad
j_2(t)=2\bigl(t-\log(2\sinh t)\bigr).
\tag{25}
\]

As `t\downarrow0`,

\[
j_1(t)\sim t^{-1},
\qquad
j_2(t)\sim2\log(1/t).
\tag{26}
\]

Substituting into (20)--(21) and eliminating `t` gives the logarithmically exact capacity growth

\[
\boxed{
\log\mathcal M_{2,C}(d,Q)
\sim
\frac{Q^2}{2\pi C^2d^2}
\qquad(d\downarrow0).
}
\tag{27}
\]

Equivalently,

\[
\boxed{
\lim_{d\downarrow0}
\frac{2\pi C^2d^2}{Q^2}
\log\mathcal M_{2,C}(d,Q)=1.
}
\tag{28}
\]

So a fixed `L^2` budget alone cannot bound a target response, but a fixed `L^2` budget **together with finite TV** makes shallow oracle targeting exponentially expensive.

### Supercritical source norms: `p>2`

Here `s=p'\in(1,2)`. For every `0<k<2`, (17) and `\operatorname{csch}^2u\sim u^{-2}` give

\[
\boxed{
j_k(t)
\sim
\Gamma(k+1)\Gamma(2-k)t^{k-2}
\qquad(t\downarrow0).
}
\tag{29}
\]

Set

\[
G_s:=\Gamma(s)\Gamma(2-s).
\]

Then

\[
j_s(t)\sim sG_s t^{s-2},
\qquad
j_{s-1}(t)\sim(2-s)G_s t^{s-3}.
\tag{30}
\]

Using (20)--(21) and eliminating `t` yields

\[
\boxed{
\mathcal M_{p,C}(d,Q)
\sim
(2-s)
\left[
\frac{s^{s-1}Q^2}
{4\pi\,\Gamma(s)\Gamma(2-s)\,C^s d^2}
\right]^{1/(2-s)}
}
\tag{31}
\]

as `d\downarrow0`. The TV cost therefore grows like

\[
d^{-2/(2-s)}
=d^{-2(p-1)/(p-2)}.
\tag{32}
\]

The formal limit `p\to\infty` gives `s\to1` and reduces (31) to

\[
\frac{Q^2}{4\pi C d^2},
\]

exactly the leading `L^\infty` bounded-density capacity from WI-417. Thus WI-417 is the endpoint of one continuous `L^p+TV` coercivity family rather than an isolated phenomenon.

## 5. Stress tests and scope

Several controls are load-bearing.

First, target translation in `\gamma` changes none of the norms or capacities, so the result is not an artifact of centering. The depth dependence is exact under the two-dimensional scaling of the source half-plane.

Second, signed or complex source densities cannot improve the one-target capacity: `|\int q_df|\le\int q_d|f|`, while `L^1` and `L^p` norms depend only on `|f|`.

Third, the threshold `p=2` is a **far-field** threshold. The local singularity of `q_d` is logarithmic and belongs locally to every finite `L^s`; the failure at `s\le2` comes from the exact low-level-set law `|\{q_d>t\}|\sim\pi d^2t^{-2}` as `t\downarrow0`. This matters programmatically: a regularity condition can completely eliminate atoms and still fail because it allows too much diffuse mass at large source distance.

Fourth, the result is strictly one-target. WI-418--WI-420 show that a source budget may be heavily reused across nearby targets even under the stronger `L^\infty` cap. Nothing here makes costs additive across a hypothetical exceptional zero set.

Fifth, no arithmetic theorem currently supplies the required target-independent `L^p` source budget for the zeta factorization. The present result says exactly what such a theorem would buy; it does not assume that theorem.

## 6. Prior-art and novelty audit

The analytic ingredients are classical. The half-plane logarithmic Green/Blaschke kernel and its zeta role are classical potential-theory and Burnol--Kunik territory; WI-417 already derived the exact disk superlevel law (2). Hardy--Littlewood rearrangement is classical; a standard modern reference is Elliott Lieb and Michael Loss, *Analysis*, and the underlying rearrangement inequality goes back to Hardy and Littlewood. Lorentz spaces were introduced by G. G. Lorentz, *Some new functional spaces*, **Annals of Mathematics** 51 (1950), 37--55, DOI `10.2307/1969496`; endpoint Hölder/duality technology is classical, including R. A. Hunt, *On L(p,q) spaces*, **L'Enseignement Mathématique** 12 (1966), 249--276. Richard O'Neil's *Convolution operators and L(p,q) spaces*, **Duke Mathematical Journal** 30 (1963), 129--142, DOI `10.1215/S0012-7094-63-03015-1`, is neighboring classical Lorentz-space operator theory.

A targeted prior-art search also found modern Green-potential mapping theory formulated in Lorentz/weak spaces, reinforcing that the critical weak-space viewpoint is standard analysis rather than a new general functional-analytic principle. No priority claim is made for the Hardy--Littlewood, Lorentz, Green-kernel, or duality ingredients.

The durable line-specific content is the exact specialization to the translated-Blaschke defect kernel using WI-417's superlevel geometry: formulas (3)--(5), the sharp bare-source threshold (7)--(10), the exact finite-TV `L^p` supporting family (18)--(21), and the three shallow-depth regimes (24), (28), and (31). A targeted search did not locate these statements as a zeta/Blaschke source-budget theorem; absence from the search is not used as a priority claim.

## Consequence

The source-side frontier after WI-421 is now more precise. It is not enough to ask whether a proposed arithmetic source class excludes atoms. One must also ask whether it controls the diffuse `1/r` tail strongly enough, or whether an independent finite-TV budget is simultaneously available.

For the translated-Blaschke detector the hierarchy is exact:

\[
\boxed{
\begin{array}{c}
\text{atom-tolerant gauge}\;\Rightarrow\;\text{zero oracle cost};\\
L^p\text{ alone},\ 1<p<2\;\Rightarrow\;\text{shallow targets eventually impossible};\\
L^2\text{ alone}\;\Rightarrow\;\text{still unbounded response, but weak-}L^2;\\
L^{2,1}\text{ endpoint}\;\Rightarrow\;\text{bounded response};\\
L^p\text{ plus TV},\ p>1\;\Rightarrow\;\text{positive one-target coercivity}.
\end{array}
}
\]

Therefore an arithmetic route that only proves absolute continuity, or only an `L^2` density estimate without any separate mass/tail control, would still leave a genuine escape. A source theorem that gives `L^{2,1}`, any subcritical `L^p` with `1<p<2`, or a joint finite-TV plus `L^p` budget would cross the one-target regularity barrier and become worth testing against the multi-target Poisson-capacity reuse obstruction.