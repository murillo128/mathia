# NB-023 — Burnol scale rigidity forces exponential shell discrepancy

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + BURNOL-SCALE-RIGIDITY + EXPONENTIAL-DISCREPANCY-FLOOR + NEAR-OPTIMAL-RATE-POWER-RIGIDITY + MIXING-SCALE-BOUNDARY`. `NB-022` turns the intrinsic consecutive shell discrepancy `\Delta_N` of the canonical best residual into an upper bound for how much approximation quality can be gained from high generator indices. Burnol's classical zero-sensitive lower bound supplies the estimate in the opposite direction: a substantially shorter Nyman section cannot already have the same very small distance unless the shell discrepancy of the larger section is correspondingly large.

Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},\qquad
r_N=e-P_Ne,\qquad d_N=\|r_N\|,
\tag{1}
\]

and let `\Delta_N` be the consecutive discrepancy of the periodic harmonic-shell sequence of `r_N`, as in `NB-019`--`NB-022`. Define Burnol's critical-line constant

\[
\mathfrak B_\zeta
:=
\sum_{\Re\rho=1/2}\frac{m(\rho)^2}{|\rho|^2},
\tag{2}
\]

where the sum is over distinct non-trivial zeros on the critical line. In the discrete Nyman--Báez-Duarte normalization,

\[
\liminf_{K\to\infty}d_K^2\log K\ge\mathfrak B_\zeta.
\tag{3}
\]

Combining this with `NB-022` gives the finite cross-scale inequality: for every fixed `0<b<\mathfrak B_\zeta`, there is `K_b` such that for all integers `N>K\ge K_b`,

\[
\boxed{
\Delta_N
\ge
\frac K{60}
\left(\frac b{\log K}-d_N^2\right)_+^{1/2}.
}
\tag{4}
\]

On the closure branch `d_N\to0`, this can be optimized. For every fixed `0<b<\mathfrak B_\zeta` and `0<\theta<1`, all sufficiently large `N` satisfy

\[
\boxed{
\Delta_N
\ge
c_\theta d_N
\exp\!\left(\frac{\theta b}{d_N^2}\right),
\qquad
c_\theta=\frac1{120}\sqrt{\frac{1-\theta}{\theta}}.
}
\tag{5}
\]

Thus the intrinsic discrepancy is forced to grow at least exponentially in `1/d_N^2`, with every exponent strictly below the Burnol constant available. This is asymptotically much stronger than the polynomial floor `\Delta_N\gg d_N^{-3/2}` obtained in `NB-022` from the early Möbius coefficient core.

At the conjecturally optimal distance scale the consequence becomes almost linear in section size. If

\[
d_N^2\log N\longrightarrow\mathfrak B_\zeta,
\tag{6}
\]

then for every fixed `0<\alpha<1`,

\[
\boxed{
\Delta_N
\ge
\left(
\frac1{60}\sqrt{\frac{\mathfrak B_\zeta(1-\alpha)}{\alpha}}
-o(1)
\right)
\frac{N^\alpha}{\sqrt{\log N}}.
}
\tag{7}
\]

Consequently

\[
\boxed{
\liminf_{N\to\infty}\frac{\log\Delta_N}{\log N}\ge1,
}
\tag{8}
\]

or equivalently: for every fixed `\beta<1`, eventually `\Delta_N\ge N^\beta`. To obtain that last formulation from (7), choose any fixed `\alpha` with `\beta<\alpha<1`; the factor `N^{\alpha-\beta}/\sqrt{\log N}` then diverges. This corrects the tempting but invalid inference that the logarithmic factor in (7) could be absorbed while keeping the same exponent `\alpha`.

Bettin--Conrey--Farmer prove the saturation (6) under RH together with their reciprocal-`\zeta'` moment hypothesis. Under that established conditional model, the canonical shell residual is therefore forced to have almost linear discrepancy in power scale. This remains compatible with `\Delta_N=o(N)`; for example `N/\log N` has both properties.

## 1. A shorter-section distance floor becomes a discrepancy lower bound

`NB-022` proves the exact section-compression estimate

\[
0\le d_K^2-d_N^2
\le\frac{3600\Delta_N^2}{K^2},
\qquad 2\le K<N.
\tag{9}
\]

It comes from the shell-Fourier/Möbius estimate

\[
\left(\sum_{n=2}^N n^2|a_{N,n}|^2\right)^{1/2}
\le60\Delta_N
\tag{10}
\]

for the actual optimal coefficient vector, followed by a Hilbert-norm bound for the high-index tail of the `N`-section projection.

Burnol's bound (3) means that for every fixed `b<\mathfrak B_\zeta`,

\[
d_K^2\ge\frac b{\log K}
\tag{11}
\]

for all sufficiently large `K`. Combining (9) and (11) gives

\[
\frac b{\log K}-d_N^2
\le\frac{3600\Delta_N^2}{K^2},
\tag{12}
\]

and taking the positive part and square root proves (4). The positive part is essential: a comparison scale `K` gives information only when the larger `N`-section has actually crossed below the Burnol floor appropriate to `K`.

This is not a restatement of Burnol. Burnol constrains each section separately; the new ingredient is `NB-022`'s source-specific compression bridge, which makes the floor at one section size constrain the harmonic-shell geometry of a longer best residual.

## 2. The optimal comparison scale is exponential in inverse squared distance

Assume `d_N\to0`, fix `b<\mathfrak B_\zeta` and `0<\theta<1`, and put

\[
X_N=\exp\!\left(\frac{\theta b}{d_N^2}\right),
\qquad K_N=\lfloor X_N\rfloor.
\tag{13}
\]

For large `N`, Burnol at the section `N` gives `d_N^2\ge b/\log N`, hence

\[
X_N\le N^\theta.
\tag{14}
\]

Therefore `K_N<N`, while `d_N\to0` gives `K_N\to\infty`, so (4) applies. Since `K_N\le X_N`,

\[
\frac b{\log K_N}-d_N^2
\ge\left(\frac1\theta-1\right)d_N^2.
\tag{15}
\]

Also `K_N\ge X_N/2` eventually. Substitution in (4) yields

\[
\Delta_N
\ge
\frac{d_N}{120}
\sqrt{\frac{1-\theta}{\theta}}
\exp\!\left(\frac{\theta b}{d_N^2}\right),
\tag{16}
\]

which is (5).

The strict inequality `\theta<1` is load-bearing. At the formal endpoint `\theta=1`, the chosen comparison scale may sit exactly where the Burnol floor matches `d_N^2`, leaving no positive difference in (4). Any fixed strict fraction of the Burnol exponent leaves a definite relative gap.

## 3. Burnol saturation forces power-scale non-compressibility

Assume (6) and fix `0<\alpha<1`. Take `K_N=\lfloor N^\alpha\rfloor`. For every fixed `b<\mathfrak B_\zeta`,

\[
d_{K_N}^2
\ge
\frac b{\log K_N}
=
\frac{b/\alpha+o(1)}{\log N},
\tag{17}
\]

whereas

\[
d_N^2=rac{\mathfrak B_\zeta+o(1)}{\log N}.
\tag{18}
\]

Equation (9) therefore implies

\[
\frac{3600\Delta_N^2}{N^{2\alpha}}
\ge
\frac{b/\alpha-\mathfrak B_\zeta+o(1)}{\log N}.
\tag{19}
\]

Choose `b` with `\alpha\mathfrak B_\zeta<b<\mathfrak B_\zeta`, then let `b` approach `\mathfrak B_\zeta` after taking the asymptotic lower bound. This gives (7).

The interpretation is a genuine non-compressibility statement for the **actual target-selected section**. If its distance is already at the Burnol leading scale at `N`, then no fixed-power sub-section `N^\alpha` can carry essentially the same approximation quality unless the `N`-residual has shell discrepancy at least `N^\alpha/\sqrt{\log N}`. Letting the fixed power approach one gives (8), but no linear bound `\Delta_N\gg N` follows: Burnol's liminf theorem has no remainder strong enough here to take `\alpha=1-o(1)` uniformly.

## 4. Consequence for the live mixing/visibility route

`NB-019` gives the intrinsic mixing certificate

\[
\|Q_mr_N-\mu_Ne\|_\infty
\le\frac{2\Delta_N}{m}.
\tag{20}
\]

`NB-021` then shows that once `m` dominates the discrepancy, deep visible semigroup channels collapse; `NB-022` simultaneously shows that high generator indices beyond the same transition add negligible approximation gain under `\Delta_N=o(N)`.

Equation (5) now puts a much larger floor under that transition. If a sequence `m_N` is chosen so that the sufficient mixing error in (20) vanishes,

\[
\frac{\Delta_N}{m_N}\to0,
\tag{21}
\]

then on the closure branch, for every fixed `b<\mathfrak B_\zeta` and `\theta<1`,

\[
\frac{m_N}{d_N\exp(\theta b/d_N^2)}\to\infty.
\tag{22}
\]

Under Burnol saturation, (7) implies a simpler power statement. For every fixed `\beta<1`, choose `\alpha` with `\beta<\alpha<1`; then (7) gives `\Delta_N/N^\beta\to\infty`. Hence (21) forces

\[
\boxed{
\frac{m_N}{N^\beta}\to\infty
\qquad\text{for every fixed }\beta<1.
}
\tag{23}
\]

So near the expected optimal Nyman rate, the `\Delta_N=o(N)` branch cannot yield genuinely early fixed-power mixing. If that branch occurs at all, its transition is almost at full section scale in the logarithmic-power sense. The pre-mixing region in which the `NB-015` source-visible graph energy must be extracted correspondingly occupies essentially the whole polynomial hierarchy.

This still does not solve `NB-015`. Large consecutive discrepancy is cumulative one-dimensional shell variation, whereas visibility is a `G_N^{-1}`-weighted multiplicative edge energy. The remaining positive problem is precisely to convert some of the discrepancy forced by (4)--(5) into that graph energy before mixing destroys it, or to construct a source-faithful mechanism showing that even very large shell discrepancy can remain almost entirely invisible.

## 5. Prior-art boundary and falsification controls

The external approximation inputs are already anchored in `research/nyman_beurling/SOURCES.md`. Burnol supplies (3); Bettin--Conrey--Farmer supply the conditional optimality statement used only for interpreting (6). No new external theorem is load-bearing, so `SOURCES.md` is unchanged.

A targeted literature audit covered Burnol-type lower bounds, optimal Nyman coefficients and Dirichlet polynomials, finite-section approximation, numerical Nyman studies, generalized polynomial criteria, and recent Gram/block-compressibility work. The located sources discuss individual distance lower bounds, conditional optimal approximants, Gram conditioning, or basis compression, but no located source combined a shorter-section Burnol floor with the **consecutive shell discrepancy of the actual longer-section best residual** through an estimate equivalent to (4)--(5). Search absence is not a priority claim; the durable delta is the exact cross-scale implication obtained by combining the local section-compression theorem `NB-022` with the classical distance floor.

Several boundaries are load-bearing. The constant `60` is explicit but not optimized. Burnol supplies no upper approximation bound and does not imply `d_N\to0` or (6). The exponential estimate (5) is asserted only on the closure branch. The power-scale conclusion (8) is compatible with `\Delta_N=o(N)` and gives no positive linear fraction of `N`. Finally, large shell discrepancy does not itself lower-bound the `NB-015` visible fraction; no new approximation rate, zero-free region, or RH implication follows from this finding.

The finding is falsified by a failure of `NB-022`'s section-compression inequality (9), by a failure of Burnol's discrete lower bound in this normalization, or by an `N,K` pair satisfying the stated hypotheses but violating the elementary combination (12). A useful continuation should attack the pre-mixing conversion: determine whether the cross-scale discrepancy forced here necessarily leaves a quantitatively visible component in the `NB-017` multiplicative graph energy.