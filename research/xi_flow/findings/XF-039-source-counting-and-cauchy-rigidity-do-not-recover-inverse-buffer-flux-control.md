# XF-039 — source counting and Cauchy rigidity do not recover inverse-buffer flux control

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `STRUCTURAL/THRESHOLD`. XF-036--XF-038 show that the source-side hypothesis `M V_M=O(1)` has strong downstream consequences: translated Xi counting flattens the gaps, the total logarithmic gap variation `D_M` vanishes, and the full cross-ratio conductance network becomes asymptotically Cauchy on every sub-buffer scale. The converse direction fails sharply. Even if one imposes the translated fixed-fraction span laws used by XF-036 together with `D_M=o(1)` and hence the XF-038 Cauchy recovery, the decisive inverse-buffer bound `M V_M=O(1)` need not follow.

There is an explicit alternating microcorrugation showing this. For every `M>=2`, choose a mean gap `s_M>0` and a parameter `epsilon_M>0`, set

\[
\tau_M:=\tanh\epsilon_M,
\]

and define `2M` positive gaps by

\[
\boxed{
 g_k
 =s_M\bigl(1+(-1)^k\tau_M\bigr)
 =s_M\frac{e^{(-1)^k\epsilon_M}}{\cosh\epsilon_M},
 \qquad 0\le k<2M.
}
\tag{1}
\]

Every consecutive even-length block has **exactly** mean spacing `s_M`, while an odd-length block of `L` gaps differs from `L s_M` by only `s_M tau_M`:

\[
\boxed{
\sum_{k=q}^{q+L-1}g_k
=
\begin{cases}
L s_M,&L\text{ even},\\[3pt]
 s_M\bigl(L+(-1)^q\tau_M\bigr),&L\text{ odd}.
\end{cases}}
\tag{2}
\]

At the same time the logarithmic contrasts alternate exactly,

\[
 d_k:=\log\frac{g_{k+1}}{g_k}
 =-2(-1)^k\epsilon_M,
\tag{3}
\]

so

\[
\boxed{
D_M:=\sum_{k=0}^{2M-2}|d_k|
=2(2M-1)\epsilon_M.
}
\tag{4}
\]

Let `phi_k=F'(d_k)` be the normalized-triple flux of XF-030/031. Since `F` is even, `F'` is odd, and therefore consecutive fluxes have opposite signs. Writing

\[
p_M:=|F'(2\epsilon_M)|,
\]

one obtains the exact total flux variation

\[
\boxed{
V_M:=\sum_{k=0}^{2M-3}|\phi_{k+1}-\phi_k|
=4(M-1)p_M.
}
\tag{5}
\]

XF-030 gives

\[
F'(2\epsilon)=-3\epsilon+O(\epsilon^3),
\tag{6}
\]

hence

\[
V_M=12M\epsilon_M\,(1+o(1))
\tag{7}
\]

whenever `epsilon_M->0`.

Now choose

\[
\boxed{
\epsilon_M=M^{-1-\alpha},
\qquad 0<\alpha<1.
}
\tag{8}
\]

Then all of the downstream rigidity quantities vanish,

\[
\max_k\left|\log\frac{g_k}{s_M}\right|=O(M^{-1-\alpha}),
\qquad
D_M=4M^{-\alpha}(1+o(1)),
\tag{9}
\]

and every fixed-fraction translated block has relative mean-spacing error `O(M^{-2-\alpha})`. Consequently the XF-038 cross-ratio estimate gives uniform Cauchy recovery throughout the whole block. Nevertheless

\[
\boxed{
V_M=12M^{-\alpha}(1+o(1))\to0,
\qquad
M V_M=12M^{1-\alpha}(1+o(1))\to\infty.
}
\tag{10}
\]

Thus neither source-like translated span rigidity, nor vanishing total log-gap variation, nor asymptotic Cauchy form of the long-range network can be bootstrapped statically back into the `M V_M=O(1)` hypothesis that produced them. The missing resource is genuinely a microscopic `ell^1`/bounded-variation control on the triple flux.

This is a **static matched control**, not an Xi zero block known to occur dynamically. It does not obstruct a theorem deriving `M V_M=O(1)` from the exact Xi-flow evolution; instead it shows that such a theorem must use dynamical information or a stronger source statistic sensitive to microscopic alternation rather than only the already-derived source-rigidity package.

## 1. The translated span law is stronger than the one needed in XF-036

Equation (1) can be rewritten as

\[
g_{2j}=s_M(1+\tau_M),
\qquad
g_{2j+1}=s_M(1-\tau_M).
\tag{11}
\]

Each adjacent pair therefore has sum exactly `2s_M`. Pairing a translated block proves (2): if `L` is even every term is paired, while if `L` is odd there is one unpaired gap whose excess or deficit from `s_M` is exactly `s_M tau_M`. Hence

\[
\left|
\frac{1}{L s_M}\sum_{k=q}^{q+L-1}g_k-1
\right|
\le\frac{\tau_M}{L}.
\tag{12}
\]

To compare directly with the Xi source scale of XF-036, take

\[
M=R(T)\log^2T,
\qquad
R(T)\to\infty,
\qquad
R(T)=o(T/\log T),
\qquad
s_M=h_T:=\frac{4\pi}{\log T}.
\tag{13}
\]

For every fixed `delta in (0,1]` and `L=floor(delta M)`, equations (8) and (12) give uniformly in the translated start `q`

\[
\sum_{k=q}^{q+L-1}g_k
=h_TL\left(1+O_\delta(M^{-2-\alpha})\right).
\tag{14}
\]

The full `2M`-gap span is exactly `2M h_T=O(R(T)\log T)=o(T)`. Therefore one may place the block at height `T` and it satisfies, at the deterministic finite-gap level, every translated fixed-fraction main-term span relation used in XF-036 with much smaller relative error than that argument requires.

This does **not** assert that the block is realized by the zeros of `H_t`. The point is falsificatory: translated counting constraints alone cannot distinguish this microcorrugation from the flattened source geometry at the scale on which XF-036 uses them.

## 2. The same block is uniformly Cauchy-rigid

From (1),

\[
\log\frac{g_k}{s_M}
=(-1)^k\epsilon_M-\log\cosh\epsilon_M,
\tag{15}
\]

so the gap profile converges uniformly to the mean. Equation (3) gives (4) exactly, and the choice (8) yields `D_M=o(1)`.

XF-038 proves for every pair of active gap indices `i<k`, with `r=k-i`,

\[
\frac{e^{-3D_M}}{r^2}
\le w_{ik}\le
\frac{e^{3D_M}}{r^2}.
\tag{16}
\]

Therefore the present family satisfies

\[
\boxed{
\sup_{0\le i<k<2M}|r^2w_{ik}-1|=O(M^{-\alpha})=o(1).
}
\tag{17}
\]

On every supported interval of `N=o(M)` gaps lying a fixed-fraction distance from the buffer edge, the quadratic-form conclusion of XF-038 also applies:

\[
\mathcal E_w(f)=(1+o(1))\mathcal E_C(f)
\tag{18}
\]

uniformly over all test fields on that interval. Thus the failure of (10) is not caused by an order-one deformation of the long-range cross-ratio kernel. It survives after precisely the Cauchy recovery that XF-038 identifies as the downstream source-rigid normal form.

## 3. Flux variation still accumulates over microscopic alternation

The exact triple shape `F` is even because exchanging the two adjacent gaps sends `d` to `-d` without changing the normalized three-root discriminant. Hence `F'` is odd. Equations (3) and (5) follow immediately: the flux has constant magnitude `p_M` and flips sign at every site.

The Taylor law (6) is the XF-030 expansion `F'(d)=-3d/2+O(d^3)` evaluated at `d=2epsilon`. Substituting (8) into (4)--(7) gives

\[
D_M\asymp M^{-\alpha},
\qquad
V_M\asymp M^{-\alpha},
\tag{19}
\]

but the inverse-buffer target multiplies the latter by another factor of `M`. The distinction is therefore not whether flux variation vanishes: it does. The distinction is whether it vanishes at the much stronger `1/M` rate needed by XF-036--XF-037.

This also explains why the microcorrugation evades the fixed-rescaled-slope exclusion in XF-037. Here

\[
M|d_k|=2M^{-\alpha}\to0
\tag{20}
\]

at every site. There is no positive-density set carrying an order-one rescaled slope. Instead, a much smaller alternating slope occupies the whole block, and its tiny local jumps accumulate in `ell^1` just slowly enough that `M V_M` diverges.

## 4. No fixed `ell^p`, `p>1`, substitutes for the flux-BV gate

XF-031 gives at every interior gap index

\[
(L_\lambda h)_i=\phi_{i-1}-\phi_i,
\qquad h_i=1/g_i.
\tag{21}
\]

For the alternating family every one of the `2M-2` interior entries has magnitude `2p_M`. Thus for every fixed `1<p<\infty`,

\[
\boxed{
\|L_\lambda h\|_{\ell^p}
=(2M-2)^{1/p}\,2p_M
=O\!\left(M^{1/p-1-\alpha}\right),
}
\tag{22}
\]

while

\[
\|L_\lambda h\|_{\ell^\infty}=2p_M=O(M^{-1-\alpha}).
\tag{23}
\]

Given any fixed `p>1`, choose

\[
\frac1p<\alpha<1.
\tag{24}
\]

Then

\[
\boxed{
\|L_\lambda h\|_{\ell^p}=o(1/M)
\quad\text{but}\quad
M V_M\to\infty.
}
\tag{25}
\]

For `p=infinity`, any `0<alpha<1` already has the same property. By contrast, on the interior block

\[
\boxed{
V_M=\|L_\lambda h\|_{\ell^1}.
}
\tag{26}
\]

So the threshold isolated by XF-035--XF-037 is genuinely an `ell^1`/BV requirement. Even a fixed `ell^p`, `p>1`, estimate that is asymptotically smaller than `1/M` does not prevent a long train of tiny sign alternations from accumulating too much total flux variation.

This is stronger than the fixed-amplitude tent control of XF-035 in a different direction. The tent showed that merely vanishing unweighted bulk norms and shape deficit do not force macroscopic geometric stability when only reduced source data are kept. The present family already has the full zeroth-order source flattening and Cauchy rigidity, yet still separates all fixed `p>1` norms from the required flux-BV scale.

## 5. Stress tests and what the obstruction does not say

There are no collisions in the construction: for small `epsilon_M`, all gaps lie between `s_M(1-\tau_M)` and `s_M(1+\tau_M)` with ratio tending to one. No endpoint dynamic range is used, and every fixed-fraction translated mean is asymptotically exact. The obstruction is therefore microscopic oscillation rather than a hard edge, geometric ramp, tent fold, or deformed long-range network.

The family is also deliberately **not** a persistence claim for the Xi dynamics. XF-007 shows that high-frequency lattice modes are strongly damped forward in heat time. An alternating mode is therefore exactly the kind of configuration for which the dynamical equation may provide information absent from static counting. This finding rules out only the circular inference

\[
\text{translated source flattening + }D_M=o(1)+\text{ Cauchy recovery}
\Longrightarrow M V_M=O(1).
\tag{27}
\]

It does not rule out deriving `M V_M=O(1)` from time-integrated dissipation, an evolution inequality for the triple flux, a signed `L_lambda`/`L_w` correlation estimate, or a stronger unconditional Xi statistic that sees microscopic alternation.

Likewise, the construction is finite and local. It can be embedded as an ordered positive-gap block with the source-scale spans in (13)--(14), but no claim is made that it extends to a global real-entire function with the Xi heat deformation or survives for an interval of heat time. Those are precisely the additional structures a successful positive argument is now forced to use.

## 6. Prior-art and novelty boundary

The abstract distinction between bounded variation and fixed `ell^p` control of discrete differences, and the use of rapidly alternating sequences as compactness counterexamples, are classical. A targeted audit of discrete difference/Kolmogorov and BV literature confirms that this is standard functional-analytic territory. No external theorem is needed for (1)--(26), and no general novelty is claimed for the alternating-sequence construction or for the norm separation itself.

The durable Mathia-local content is the exact placement of that elementary obstruction inside the active Xi-flow scale hierarchy: the same finite gap family simultaneously passes the translated source-span tests used in XF-036, has the `D_M=o(1)` rigidity of XF-037, enters the Cauchy quadratic-form regime of XF-038, and nevertheless violates the `M V_M=O(1)` gate by an arbitrarily growing factor. No new literature anchor is load-bearing, so `SOURCES.md` does not require modification.

## 7. Consequence for `xi_flow`

The current constructive frontier cannot close by feeding XF-038 backward into XF-037. Cauchy recovery of `L_w` is a downstream normal form, not a substitute for the missing compactness estimate on `L_lambda h`. Any proof of the borderline resource must control the `ell^1` accumulation of triple-flux curvature rather than merely show small pointwise force, small fixed-`p` force, uniform gap flattening, or long-range spectral equivalence.

The positive route is therefore more sharply dynamical. Once the source has rigidified `L_w` to the Cauchy form, one should seek an evolution or coercive estimate that turns the strong damping of microscopic Cauchy modes into an `ell^1` bound for `L_lambda h`, while treating the low-frequency geometric mode through the translated source constraints and retaining XF-028 collision coverage. A negative continuation would need a source-compatible configuration that is not only statically Cauchy-rigid but can sustain excessive flux variation under the actual nonlinear zero flow for a source-relevant time interval.