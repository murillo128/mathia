# NB-023 — Burnol scale rigidity forces exponential shell discrepancy

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + BURNOL-SCALE-RIGIDITY + EXPONENTIAL-DISCREPANCY-FLOOR + NEAR-OPTIMAL-RATE-POWER-RIGIDITY + MIXING-SCALE-BOUNDARY`. `NB-022` turns the intrinsic consecutive shell discrepancy `\Delta_N` of the canonical best residual into an upper bound for how much approximation quality can be gained from high generator indices. Burnol's classical zero-sensitive lower bound supplies the missing estimate in the opposite direction: a substantially shorter Nyman section cannot already have the same very small distance unless the shell discrepancy of the larger section is correspondingly large.

The combination is much stronger than the polynomial discrepancy floor in `NB-022`. Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},\qquad
r_N=e-P_Ne,\qquad d_N=\|r_N\|,
\tag{1}
\]

and let `\Delta_N` denote the consecutive discrepancy of the periodic harmonic-shell sequence of `r_N`, as in `NB-019`--`NB-022`. Write

\[
\mathfrak B_\zeta
:=
\sum_{\Re\rho=1/2}
\frac{m(\rho)^2}{|\rho|^2},
\tag{2}
\]

where the sum is over the distinct non-trivial zeros on the critical line and `m(\rho)` is multiplicity. Burnol's bound, in the discrete Nyman--Báez-Duarte normalization used here, gives

\[
\liminf_{K\to\infty} d_K^2\log K\ge \mathfrak B_\zeta.
\tag{3}
\]

Consequently, for every fixed `0<b<\mathfrak B_\zeta`, there is `K_b` such that for all integers `N>K\ge K_b`,

\[
\boxed{
\Delta_N
\ge
\frac{K}{60}
\left(\frac{b}{\log K}-d_N^2\right)_+^{1/2}.
}
\tag{4}
\]

This is a finite cross-scale rigidity inequality. It says that whenever the `N`-section beats the Burnol floor appropriate to a shorter section `K`, the difference must be paid by shell discrepancy in the `N`-section.

On the closure branch `d_N\to0`, (4) can be optimized without any assumed upper approximation rate. Fix `0<b<\mathfrak B_\zeta` and `0<\theta<1`. Then, for all sufficiently large `N`,

\[
\boxed{
\Delta_N
\ge
c_\theta d_N
\exp\!\left(\frac{\theta b}{d_N^2}\right),
\qquad
c_\theta:=\frac1{120}\sqrt{\frac{1-\theta}{\theta}}.
}
\tag{5}
\]

Thus the intrinsic discrepancy is not merely forced to grow like a power of `d_N^{-1}`. Every successful sequence of best Nyman approximants must develop shell discrepancy at least **exponential in `1/d_N^2`**, with any exponent strictly below the Burnol constant available.

There is a particularly transparent consequence at the conjecturally optimal distance scale. If

\[
d_N^2\log N\longrightarrow\mathfrak B_\zeta,
\tag{6}
\]

then for every fixed `0<\alpha<1`, taking `K=\lfloor N^\alpha\rfloor` in (4) and then letting `b\uparrow\mathfrak B_\zeta` gives

\[
\boxed{
\Delta_N
\ge
\left(
\frac1{60}
\sqrt{\frac{\mathfrak B_\zeta(1-\alpha)}{\alpha}}
+o(1)
\right)
\frac{N^\alpha}{\sqrt{\log N}}.
}
\tag{7}
\]

In particular

\[
\boxed{
\Delta_N\ge N^{1-o(1)}
}
\tag{8}
\]

in the logarithmic-power sense: for every fixed `\alpha<1`, eventually `\Delta_N\ge N^\alpha` after absorbing the logarithmic factor. Bettin--Conrey--Farmer prove the saturation (6) under RH together with their reciprocal-`\zeta'` moment hypothesis, so under that established conditional model the canonical shell residual is forced to have almost linear discrepancy in power scale.

This does not contradict the still-open alternative `\Delta_N=o(N)` from `NB-021`--`NB-022`; quantities such as `N/\log N` are both sublinear and `N^{1-o(1)}`. It does show that, near the expected optimal Nyman rate, any sublinear-discrepancy regime must be extremely close to the full section scale. In particular the intrinsic mixing certificate

\[
\|Q_mr_N-\mu_Ne\|_\infty\le\frac{2\Delta_N}{m}
\tag{9}
\]

cannot become effective at a genuinely fixed power below `N` under (6). Any scale with `\Delta_N/m_N\to0` must satisfy `m_N\gg N^\alpha` for every fixed `\alpha<1` in that regime. This sharply narrows the idea that useful source transport might arise simply by waiting for shell mixing at an intermediate polynomial depth.

## 1. Section compression converts every shorter-distance floor into a discrepancy lower bound

`NB-022` proves the exact section-compression estimate

\[
0\le d_K^2-d_N^2
\le\frac{3600\Delta_N^2}{K^2},
\qquad 2\le K<N.
\tag{10}
\]

Its proof is intrinsic to the canonical harmonic-shell model: shell Fourier inversion and finite Möbius inversion give

\[
\left(\sum_{n=2}^N n^2|a_{N,n}|^2\right)^{1/2}
\le60\Delta_N,
\tag{11}
\]

which in turn controls the Hilbert norm of the high-index part of the actual `N`-section projection. No approximation-rate theorem is used in (10).

Burnol's result is the complementary source-independent distance floor. In the standard discrete Báez-Duarte formulation it implies (3). Equivalently, for every fixed `b<\mathfrak B_\zeta`,

\[
d_K^2\ge\frac b{\log K}
\tag{12}
\]

for all sufficiently large `K`. This is exactly the form already used qualitatively in `NB-020` and `NB-022`, but retaining the scale `K` rather than replacing it by a coarse absolute constant is decisive here.

Combining (10) and (12) gives

\[
\frac b{\log K}-d_N^2
\le
\frac{3600\Delta_N^2}{K^2}.
\tag{13}
\]

Taking the positive part and square root proves (4). The positive part is load-bearing: when the larger-section distance has not dropped below the Burnol floor at `K`, that particular comparison says nothing about discrepancy.

Equation (4) is therefore not a reformulation of Burnol. Burnol constrains each section separately; `NB-022` supplies the new bridge that makes a short-section floor constrain the shell geometry of a longer section.

## 2. Optimizing the comparison scale gives an exponential inverse-distance barrier

Assume `d_N\to0`, fix `b<\mathfrak B_\zeta` and `0<\theta<1`, and define

\[
X_N:=
\exp\!\left(\frac{\theta b}{d_N^2}\right),
\qquad
K_N:=\lfloor X_N\rfloor.
\tag{14}
\]

For sufficiently large `N`, both the Burnol bound at `N` and at `K_N` are available. The bound at `N` gives

\[
d_N^2\ge\frac b{\log N},
\tag{15}
\]

and hence

\[
X_N\le N^\theta.
\tag{16}
\]

Therefore `K_N<N` eventually, while `d_N\to0` also gives `K_N\to\infty`, so this is an admissible comparison scale in (4).

Since `K_N\le X_N`,

\[
\log K_N
\le
\frac{\theta b}{d_N^2},
\tag{17}
\]

and therefore

\[
\frac b{\log K_N}-d_N^2
\ge
\left(\frac1\theta-1\right)d_N^2.
\tag{18}
\]

For large `N`, `X_N\ge2`, so `K_N\ge X_N/2`. Substituting (18) into (4) yields

\[
\Delta_N
\ge
\frac{K_Nd_N}{60}
\sqrt{\frac{1-\theta}{\theta}}
\ge
\frac{d_N}{120}
\sqrt{\frac{1-\theta}{\theta}}
\exp\!\left(\frac{\theta b}{d_N^2}\right),
\tag{19}
\]

which is (5).

The use of `\theta<1` is not cosmetic. At the formal endpoint `\theta=1`, the comparison scale is where the Burnol floor and `d_N^2` can coincide, so (4) may have no positive gap. Any strict fraction of the Burnol exponent leaves a fixed relative gap and gives the exponential lower bound.

The earlier floor in `NB-022`,

\[
\Delta_N\gg d_N^{-3/2},
\tag{20}
\]

comes from forcing a Möbius-shaped coefficient core and then applying the shell Fourier estimate. Equation (5) is asymptotically stronger on the closure branch: it uses not just the local coefficient core but the impossibility, imposed by Burnol, of compressing a very accurate `N`-section approximant into an exponentially shorter section without paying a norm loss.

## 3. Burnol saturation forces almost full power-scale shell complexity

Assume (6), and fix `0<\alpha<1`. Let

\[
K_N=\lfloor N^\alpha\rfloor.
\tag{21}
\]

For every fixed `b<\mathfrak B_\zeta`, Burnol gives

\[
d_{K_N}^2
\ge
\frac b{\log K_N}
=
\frac{b/\alpha+o(1)}{\log N}.
\tag{22}
\]

Meanwhile (6) says

\[
d_N^2
=
\frac{\mathfrak B_\zeta+o(1)}{\log N}.
\tag{23}
\]

Thus (10) implies

\[
\frac{3600\Delta_N^2}{N^{2\alpha}}
\ge
\frac{b/\alpha-\mathfrak B_\zeta+o(1)}{\log N}.
\tag{24}
\]

Choose `b` with

\[
\alpha\mathfrak B_\zeta<b<\mathfrak B_\zeta.
\tag{25}
\]

The right side is then positive for large `N`. Letting `b` approach `\mathfrak B_\zeta` after the fixed-`\alpha` inequality gives exactly (7).

Because `\alpha<1` was arbitrary, (7) implies (8). The statement is deliberately a **power-scale** conclusion rather than `\Delta_N\asymp N`: the available Burnol theorem is a liminf lower bound with no quantitative remainder strong enough to pass uniformly to `\alpha=1-o(1)`. Nothing here rules out `\Delta_N=N/L(N)` for a slowly growing `L`.

Bettin--Conrey--Farmer show, assuming RH and

\[
\sum_{|\Im\rho|\le T}
\frac1{|\zeta'(\rho)|^2}
\ll T^{3/2-\delta},
\tag{26}
\]

that the discrete Nyman distance has the Burnol-optimal leading constant. Under their assumptions (which in particular entail simple zeros in the form they use), (7)--(8) are therefore unconditional consequences of their approximation theorem plus `NB-022`'s exact finite geometry. This is a compatibility statement, not a new proof of their asymptotic or of RH.

## 4. Consequence for the live visibility and mixing route

The live `NB-015` program seeks a source-visible semigroup defect whose accumulated section decrements contradict a positive limiting Nyman distance. `NB-021` shows that if `\Delta_N=o(N)`, then after a discrepancy-dependent transition every deep channel mixes toward zero and its visible/full defect ratio collapses. `NB-022` adds that the same hypothesis makes high generator indices contribute negligibly once `K\gg\Delta_N`.

Equation (5) now puts a source-scale floor under that transition. Any use of the intrinsic estimate (9) with a scale `m_N` satisfying

\[
\frac{\Delta_N}{m_N}\longrightarrow0
\tag{27}
\]

must, on the closure branch, also satisfy for every fixed `b<\mathfrak B_\zeta` and `\theta<1`,

\[
\frac{m_N}
{d_N\exp(\theta b/d_N^2)}
\longrightarrow\infty
\quad\text{up to the fixed factor }c_\theta.
\tag{28}
\]

Under Burnol saturation (6), equation (7) makes the geometric content simpler: (27) forces

\[
m_N\gg N^\alpha
\qquad\text{for every fixed }\alpha<1.
\tag{29}
\]

Thus the apparently favorable branch `\Delta_N=o(N)` is not, near the expected optimal approximation rate, a route to early polynomial-depth mixing. Its transition can occur only at an almost-full-section power scale. The pre-mixing region in which useful source-visible energy would have to be extracted correspondingly occupies almost the whole polynomial hierarchy.

This does not solve the visibility problem. A large `\Delta_N` is only cumulative shell variation; `NB-022` already warns that it need not become large `G_N^{-1}`-weighted multiplicative graph energy. The finding instead removes a plausible simplification: one cannot simultaneously have near-Burnol-optimal approximation, strongly compress the useful generator section to `N^\alpha` for fixed `\alpha<1`, and retain small intrinsic shell discrepancy.

## 5. Prior-art boundary and falsification controls

The external approximation-rate inputs are classical and already anchored in `research/nyman_beurling/SOURCES.md`. Burnol supplies the multiplicity-weighted lower constant (3). Bettin--Conrey--Farmer supply the conditional optimality statement used only to interpret the saturation regime (6). No new external estimate is required, so `SOURCES.md` is unchanged.

A targeted literature audit covered Burnol-type lower bounds, optimal Nyman coefficients and Dirichlet polynomials, finite-section approximation, numerical Nyman studies, generalized polynomial criteria, and recent Gram/block-compressibility work. The located sources discuss individual distance lower bounds, conditional optimal approximants, Gram conditioning or basis compression, but no located source combined a shorter-section Burnol floor with the **consecutive shell discrepancy of the actual longer-section best residual** through an estimate equivalent to (4)--(5). Search absence is not a priority claim; the durable delta here is the exact implication obtained by combining the local section-compression theorem `NB-022` with the classical scale-dependent distance floor.

Several boundaries are essential:

- Equation (4) inherits the constant `60` from `NB-022`; it is explicit but not optimized. Improving that constant does not change the exponential mechanism.
- Burnol gives a lower bound on best approximation distance. It supplies no upper bound and therefore does not by itself imply `d_N\to0` or the saturation hypothesis (6).
- Equation (5) is asserted on the closure branch `d_N\to0`; it does not say that such a branch has been proved.
- Equation (8) under saturation is compatible with `\Delta_N=o(N)`. It forces near-linear **power-scale** growth, not a positive linear fraction of `N`.
- Large shell discrepancy does not imply useful section visibility. The missing `NB-015` quantity remains the source-aware `G_N^{-1}`-weighted multiplicative edge energy, not discrepancy alone.
- The result does not improve the Burnol lower bound, the Nyman approximation rate, a zero-free region, or the RH criterion.

The finding is falsified by a canonical finite residual violating the section-compression inequality (10), by a failure of Burnol's discrete lower bound (3) in the normalization used here, or by an `N,K` pair satisfying the hypotheses but violating the elementary combination (13). A positive continuation should now attack the remaining conversion at the pre-mixing scale: determine whether the discrepancy forced by (4)--(5) necessarily leaves a quantitatively visible component in the `NB-017` multiplicative graph energy, or construct a source-faithful residual mechanism showing that even exponentially large shell discrepancy can remain invisible to `NB-015`.