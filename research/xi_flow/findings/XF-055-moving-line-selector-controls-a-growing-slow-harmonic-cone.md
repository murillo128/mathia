# XF-055 — moving-line selector controls a growing slow-harmonic cone

**Status:** `EXACT-DERIVED` + `UNIFORM-MULTIBAND-SELECTOR` + `SOURCE-SPECIFIC-TRANSPORT` + `MATCHED-CONTROL`. XF-054 proves that the compact XF-050 memory statistic at one center `omega=Theta(1/log T)` is `o(1)` uniformly on every fixed positive heat interval. The same moving-line argument has more uniformity than that single-mode statement records. It controls a **growing family of distinct shrinking bands**, large enough to contain every arithmetic Cauchy harmonic whose linear damping rate stays below a constant multiple of `log log T`.

Use the XF-047/XF-050 scales

\[
\sigma_T=\frac{4\pi}{\log(T/4\pi)},
\qquad
q\asymp \log^2T,
\qquad
M=q^2,
\qquad
W=M\sigma_T\asymp\log^3T,
\tag{1}
\]

with the same bandlimited envelope `g`, `\widehat g=\chi\in C_c^\infty((-1,1))`. For an integer harmonic `ell>=1`, define

\[
\omega_{\ell,T}:=\frac{2\pi\ell}{q\sigma_T}
\tag{2}
\]

and

\[
f_{T,\ell}(x)
:=g\!\left(\frac{x-T}{W}\right)
 e^{-i(\omega_{\ell,T}(x-T)+\varphi_{\ell,T})}.
\tag{3}
\]

Let `mathcal Z_t` be the canonical positive-frequency Xi carrier of XF-051 and put

\[
\mathcal S_{T,\ell}(t)
:=\frac1{2\pi}
\left\langle
\mathcal Z_t(\xi),
\widehat f_{T,\ell}(-\xi)
\right\rangle.
\tag{4}
\]

Then for every fixed heat horizon `t_0>0` and every fixed `C>0`,

\[
\boxed{
\sup_{0\le t\le t_0}
\sup_{1\le\ell\le C\log\log T}
|\mathcal S_{T,\ell}(t)|
=o(1).
}
\tag{5}
\]

The phases `varphi_{ell,T}` may be arbitrary. The frequency windows remain pairwise separated, positive after reflection in (4), and eventually lie strictly below the first prime-power line `log 2/2`. Thus the endpoint selector transported in XF-054 is not merely a one-mode obstruction: it excludes a logarithmically growing cone of low positive harmonics.

This range is already enough to cover all linearly slow arithmetic Cauchy modes. In the exact `q`-periodic arithmetic control of XF-041/XF-047, harmonic `ell` has amplitude decay rate

\[
\rho_{\ell,q}
=
\frac{4\pi^2}{q^2\sigma_T^2}\ell(q-\ell)
=
\ell\,\rho_{1,q}\frac{q-\ell}{q-1}.
\tag{6}
\]

Since `rho_{1,q}=1/4+o(1)`, uniformly for `ell<=C log log T`,

\[
\boxed{
\rho_{\ell,q}
=\frac\ell4(1+o(1)).
}
\tag{7}
\]

At the edge of the selector cone, a fixed positive heat time therefore damps the arithmetic linear mode by a power of `log T`; beyond that edge the linear Cauchy damping is still faster. Conversely, every fixed harmonic that could retain an order-one fraction of its amplitude over fixed heat time lies inside (5).

The conclusion is still not a proof of `Lambda<=0`. What it removes is a specific compensation loophole left after XF-054: replacing the XF-047 first memory harmonic by any bounded number of nearby slow harmonics does not evade the transported source selector. The remaining transition-side burden is to convert these compact zero-field exclusions into low-mode control for the actual nonperiodic gap geometry and to combine that with coercivity of the high-mode Cauchy sector.

## 1. The compact bands stay prime-free uniformly over the growing cone

The Fourier transform of (3) is

\[
\widehat f_{T,\ell}(\xi)
=
W e^{-iT\xi-i\varphi_{\ell,T}}
\chi\!\bigl(W(\xi+\omega_{\ell,T})\bigr),
\tag{8}
\]

so `\widehat f_{T,ell}(-xi)` is supported in

\[
I_{T,\ell}
=
[\omega_{\ell,T}-W^{-1},
 \omega_{\ell,T}+W^{-1}].
\tag{9}
\]

For `ell>=1`,

\[
W\omega_{\ell,T}=2\pi\ell q,
\tag{10}
\]

so the lower endpoint is positive for all large `T`. If `ell<=C log log T`, then

\[
\omega_{\ell,T}
=O\!\left(\frac{\log\log T}{\log T}\right)
=o(1).
\tag{11}
\]

Hence every band (9) lies inside `(0,log 2/2)` for sufficiently large `T`, uniformly in the displayed harmonic range. At `t=0`, the Guinand--Weil prime samples therefore miss every one of these bands exactly, just as in XF-050; the archimedean contribution remains the only endpoint background.

The bands are also disjoint. Adjacent centers differ by

\[
\omega_{\ell+1,T}-\omega_{\ell,T}
=\frac{2\pi}{q\sigma_T}
\asymp\frac1{\log T},
\tag{12}
\]

whereas their half-width is `W^{-1}=Theta(log^{-3}T)`. Thus (5) is genuinely a growing family of separate spectral probes, not repeated sampling of one widening window.

## 2. The XF-054 moving line loses only a polylogarithmic factor

Fix `t_0`. Use exactly the XF-054 zero-free height

\[
a_T=A\log T
\tag{13}
\]

with fixed `A=A(t_0)>0` large enough for its reflected Euler-product estimate. Height independence of XF-051 gives the exact physical-space pairing

\[
\mathcal S_{T,\ell}(t)
=
\frac{i}{2\pi}
\int_{\mathbb R}
Q_{a_T}(x,t)f_{T,\ell}(x+i a_T)\,dx.
\tag{14}
\]

The vertically shifted probe is

\[
f_{T,\ell}(x+i a_T)
=
e^{a_T\omega_{\ell,T}-i\varphi_{\ell,T}}
 g\!\left(\frac{x-T}{W}+i\frac{a_T}{W}\right)
 e^{-i\omega_{\ell,T}(x-T)}.
\tag{15}
\]

The only new factor relative to XF-054 is the first exponential. From (1)--(2),

\[
a_T\omega_{\ell,T}
=O_A(\ell),
\tag{16}
\]

and therefore, uniformly for `ell<=C log log T`,

\[
\boxed{
e^{a_T\omega_{\ell,T}}
\le (\log T)^{K_{A,C}}
}
\tag{17}
\]

for a fixed constant `K_{A,C}`. Also

\[
\frac{a_T}{W}=O((\log T)^{-2}),
\tag{18}
\]

so every fixed derivative of the shifted `g` remains uniformly Schwartz.

XF-054 proves on `|x-T|<=T/2`, uniformly for `0<=t<=t_0`,

\[
Q_{a_T}(x,t)-Q^{\rm bg}_{a_T}(x,t)
=O(T^{-\kappa_A}(\log T)^B)
\tag{19}
\]

for some `kappa_A>0`, while the background satisfies

\[
Q^{\rm bg}_{a_T}=O(\log T),
\qquad
\partial_x^kQ^{\rm bg}_{a_T}
=O_{k,t_0}\!\left(
\frac{(\log T)^{B_k}}{T^k}
\right).
\tag{20}
\]

The arithmetic error in (14) is therefore

\[
O\!\left(
W T^{-\kappa_A}(\log T)^{B+K_{A,C}}
\right)
=o(1)
\tag{21}
\]

uniformly throughout the harmonic cone.

## 3. Oscillation beats the polylogarithmic height cost

For the deterministic background, integrate (14) by parts `N` times against

\[
e^{-i\omega_{\ell,T}(x-T)},
\]

where `N` is any fixed integer chosen after `A` and `C`. The term for which all derivatives fall on the envelope is bounded by

\[
O_{N,A,C}\!\left(
(\log T)^{1+K_{A,C}}
W\,(W\omega_{\ell,T})^{-N}
\right).
\tag{22}
\]

Using (1) and (10),

\[
W\asymp\log^3T,
\qquad
W\omega_{\ell,T}=2\pi\ell q\asymp \ell\log^2T.
\tag{23}
\]

Since `ell>=1`, choosing the fixed order `N` sufficiently large in terms of `A,C` makes (22) `o(1)` uniformly. Any term in which at least one derivative lands on `Q^{bg}` gains an additional factor `W/T`, up to fixed powers of `log T`, by (20), and is smaller.

Outside `|x-T|<=T/2`, the shifted envelope in (15) is uniformly Schwartz at real distance `Omega(T/W)`. The logarithmic derivative has only polynomial growth, as in XF-051/XF-054. Choosing a sufficiently large fixed Schwartz power absorbs the polylogarithmic factor (17), so the physical tails are also `o(1)` uniformly.

Combining the arithmetic term, deterministic background, and physical tails proves (5). The proof uses no root reality and is valid through collisions exactly as XF-054 is.

The `C log log T` scale is a proof boundary of this particular moving-line argument. With `a_T=A log T`, the vertical factor grows like `e^{O(ell)}` while the deterministic-background cancellation supplied by a `C_c^infty` envelope is super-polynomial only one fixed integration order at a time. Fixed multiples of `log log T` cost only fixed powers of `log T` and can be absorbed by choosing that order. This argument does not justify uniformity for `ell/log log T -> infinity`; it does not show that such a stronger range is false.

## 4. Every critical pure slow harmonic is detected with the same order-one margin

The widening theorem is not merely an upper bound whose usefulness deteriorates with `ell`. Consider the matched arithmetic control

\[
z_j
=T+j\sigma_T
+a_\ell\sin\!\left(
\frac{2\pi\ell j}{q}+\phi
\right),
\tag{24}
\]

with

\[
a_\ell
:=
\frac{\sigma_T\kappa/q^2}
{2\sin(\pi\ell/q)},
\qquad
\kappa>0\ \text{fixed}.
\tag{25}
\]

Its relative gap modulation has amplitude exactly `kappa/q^2`, the XF-047 critical scale. Pair it with the matching probe center (2), choosing the harmless probe phase to align the complex coefficient.

The Poisson-summation identities used in XF-050 remain exact for every `ell<=C log log T`: the zero, first, and second relevant harmonics stay far outside `supp chi` after rescaling. The linear response is therefore

\[
\left|\sum_j
f'_{T,\ell}(T+j\sigma_T)
\,a_\ell\sin\!\left(
\frac{2\pi\ell j}{q}+\phi
\right)
\right|
=
\frac12\omega_{\ell,T}a_\ell M.
\tag{26}
\]

But

\[
\omega_{\ell,T}a_\ell M
=
\kappa\,
\frac{\pi\ell}{q\sin(\pi\ell/q)}
=
\kappa(1+o(1))
\tag{27}
\]

uniformly because `ell/q ->0`. The quadratic Taylor remainder is still

\[
O(\kappa^2/q^2)=o(1)
\tag{28}
\]

uniformly in the same range: the factor `ell` in the probe frequency cancels the `1/ell` in the position amplitude (25). Hence

\[
\boxed{
\left|
\sum_j f_{T,\ell}(z_j)
\right|
=
\frac\kappa2+o(1)
}
\tag{29}
\]

uniformly for `1<=ell<=C log log T`.

Equations (5) and (29) give a clean matched-control separation. No critical pure harmonic in the growing cone can model the actual Xi source statistic over a fixed heat interval. The order-one margin does not collapse as the harmonic number grows within the proved range.

## 5. Relation to the Cauchy relaxation clock

For the arithmetic `q`-periodic gap flow, XF-041 gives (6). XF-047 records `rho_{1,q}=1/4+o(1)` in the source scaling. Therefore, for every `ell=o(q)`,

\[
\rho_{\ell,q}
=
\frac\ell4(1+o(1)),
\tag{30}
\]

with uniformity on the cone in (5).

This places the selector range at exactly the useful side of the relaxation spectrum. Fix any positive heat duration `tau`. Modes with harmonic distance

\[
m:=\min\{\ell,q-\ell\}
\ge C\log\log T
\tag{31}
\]

in the arithmetic linearization acquire a damping factor at most

\[
\exp\!\left(-\left(\frac14+o(1)\right)m\tau\right)
\le
(\log T)^{-C\tau/4+o(1)}
\tag{32}
\]

as long as `m=o(q)`; farther into the spectrum the exact eigenvalue is only larger until the symmetry point. For real gap fields, the `q-ell` mode is the complex conjugate of the positive `ell` mode, so it is enough to index the low side by `1<=ell<=q/2`.

Thus, at the arithmetic linear level, one may choose `C` as large as needed: all modes below `C log log T` are source-discriminated by (5), while all modes above that cutoff are strongly damped over fixed positive heat time. This does **not** yet transfer to the nonlinear nonperiodic Xi block. It identifies the missing bridge sharply: one needs a stable decomposition that turns the compact carrier bounds into control of the low transition-side gap modes while using the XF-038 Cauchy form to dissipate the complement.

## 6. Stress tests and evidence boundary

The first control is `ell=1`, which reduces to XF-054 and the XF-050/XF-047 memory mode. The second is the matched pure harmonic (24), for which (29) shows that moving the logarithmic-derivative line cannot make a genuine order-one coefficient disappear. The third is the cone edge `ell=C log log T`: the height factor is only a fixed power of `log T`, while `W omega` has gained an additional `log log T`; the proof therefore retains, rather than loses, oscillatory leverage.

Several stronger conclusions are **not** established. Equation (5) is a family of zero-field linear statistics; it is not yet an inverse theorem for an arbitrary gap configuration. A nonlinear, nonperiodic transition block can distribute shape among modes, sparse microfolds, boundary layers, and mixed `L_lambda`/`L_w` correlations that are not determined by these scalar pairings alone. XF-038 gives Cauchy quadratic-form rigidity only after the borderline flux-variation gate has been crossed; it does not supply the required low/high spectral decomposition before that gate. No estimate here signs the XF-031 mixed product, proves `M V_M=O(1)`, crosses a collision using ordered gaps, or bounds `Lambda`.

The theorem also does not claim a broadband positive-time prime-free support gap. The bands (9) remain separate compact probes, and their number grows only logarithmically. The result should therefore be used as a source-side spectral constraint, not as pointwise regularity of `mathcal Z_t` near `xi=0`.

## 7. Prior-art and novelty boundary

The external ingredients are unchanged from XF-051/XF-054: de Bruijn strip control, the Xi functional equation and Euler product, Stirling asymptotics, Gaussian heat propagation, and the half-plane Fourier--Laplace support principle already anchored in `research/xi_flow/SOURCES.md`. The Polymath15 high-zero work remains the closest source for effective positive-heat Xi asymptotics, but its published high-zero approximation is not stated as the uniform family of shrinking compact logarithmic-derivative bands in (5).

A targeted literature search over the de Bruijn--Newman heat-flow, logarithmic-derivative/Fourier, and Polymath15 formulations did not locate this particular growing-harmonic selector statement. No novelty is claimed for any classical analytic ingredient or for Fourier-mode damping of the arithmetic Cauchy operator. The durable line-specific delta is the **uniform scale coupling**: the same source-specific moving-line proof that excludes one XF-047 memory mode actually excludes every critical harmonic up to `C log log T`, while the arithmetic Cauchy relaxation rate grows linearly with the harmonic number.

No new load-bearing external source is introduced, so `SOURCES.md` does not require a change.

## 8. Consequence for `xi_flow`

The endpoint-to-transition program no longer has a credible escape based on replacing the first coherent memory wave by a finite packet of other comparably slow arithmetic harmonics. The transported Xi selector has a growing low-frequency cone, and the arithmetic Cauchy clock makes the complement increasingly fast.

The next constructive gate is therefore an **inverse/source-to-gap bridge**, not another endpoint transport estimate: on a real-simple high-zero block near the transition, derive a quantitative inequality that converts the family (5) into small low-mode gap coefficients on a memory-scale interior window, with errors stable under the source flattening and boundary regime. If that can be coupled to XF-038 form rigidity or an earlier bootstrap that supplies comparable Cauchy coercivity, the remaining high-frequency sector is already on the favorable side of the heat clock. A decisive negative should instead exhibit a source-compatible nonperiodic geometry whose entire selector cone is `o(1)` while a transition-relevant slow component survives outside every such inverse estimate.