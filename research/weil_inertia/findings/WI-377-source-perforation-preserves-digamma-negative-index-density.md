# WI-377 — Source perforation preserves the digamma negative-index density

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + SOURCE-CONDITIONED-NEGATIVE-INDEX + DECISIVE-REPAIR-BARRIER + CLASSICAL-ARITHMETIC + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

The true arithmetic source slots in Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* do not merely preserve the sharp gamma-corrected bulk floor found in WI-376. They preserve the entire fixed-depth **certified macroscopic negative-index profile** from WI-373.

Let

\[
A_k=\log(k+1),
\qquad
S_k=\bigcup_{\substack{2\le n\le k\\ \Lambda(n)>0}}
\left[\log k-\log n,\ \log(k+1)-\log n\right),
\]

and let `\mathcal A_{A_k}` be the corrected archimedean form in physical logarithmic coordinates from WI-369. Put

\[
C_\Gamma=\frac\pi2+\gamma+\log(8\pi),
\]

\[
h(s)=\frac{e^{-s/2}}{1-e^{-2s}},
\qquad
H(z)=\int_z^\infty h(s)\,ds,
\]

and

\[
d(q)=2\int_0^\infty h(s)(1-\cos qs)\,ds,
\qquad
m(q)=d(q)-C_\Gamma
=\operatorname{Re}\psi\!\left(\frac14+\frac{iq}{2}\right)-\log\pi.
\]

For `0\le\eta<C_\Gamma`, let `q_\eta>0` be the unique solution of

\[
m(q_\eta)=-\eta.
\tag{1}
\]

Define the source-zero depth index variationally by

\[
\iota^{\rm src}_{\eta,k}
:=
\sup\left\{
\dim V:
V\subset \mathcal D(\mathcal A_{A_k}),
\ F=0\ \text{a.e. on }S_k\ (F\in V),
\ \mathcal A_{A_k}[F]\le-\eta\|F\|_2^2\ (F\in V)
\right\}.
\tag{2}
\]

Then

\[
\boxed{
\liminf_{k\to\infty}
\frac{\iota^{\rm src}_{\eta,k}}{A_k}
\ge \frac{q_\eta}{\pi}
\qquad(0\le\eta<C_\Gamma).
}
\tag{3}
\]

At depth zero this gives

\[
\boxed{
\liminf_{k\to\infty}
\frac{\iota^{\rm src}_{0,k}}{\log(k+1)}
\ge \frac{q_0}{\pi}
=2.0021169777\ldots,
}
\tag{4}
\]

using the numerical orientation for `q_0` already recorded in WI-373.

Thus the exact source-zero constraint does not remove a sublinear residue of bad gamma directions. For every fixed spectral depth below `C_\Gamma`, there are still linearly many negative directions in the physical logarithmic length. In particular, any **additive** source-conditioned repair that makes the corrected block nonnegative must have positive rank `\Omega(A_k)`; more sharply, at every fixed depth `0<t<C_\Gamma` it must supply at least `(q_t/\pi+o(1))A_k` positive spectral directions above level `t`.

The statement is deliberately scoped. It concerns the corrected archimedean block after imposing the true source-zero constraints. It does not say that Desogus's full inherited-core/source/polar network is additive, finite-rank, or incapable of supplying the required extensive coercivity, and it does not establish or refute RH.

## 1. Exact physical-log decomposition and the unconstrained profile

WI-369 gives, on `(0,A)`,

\[
\boxed{
\mathcal A_A[F]+C_\Gamma\|F\|_2^2
=D_A[F]+E_A[F]+J_A[F],
}
\tag{5}
\]

with

\[
D_A[F]
=\frac12\iint_{(0,A)^2}
h(|s-t|)|F(s)-F(t)|^2\,ds\,dt,
\tag{6}
\]

\[
E_A[F]
=\int_0^A\bigl(H(s)+H(A-s)\bigr)|F(s)|^2\,ds,
\tag{7}
\]

and

\[
J_A[F]
=\iint_{(0,A)^2}h(s+t)F(s)\overline{F(t)}\,ds\,dt.
\tag{8}
\]

All three remainders are nonnegative. WI-373 retains the exact whole-line symbol of the screened difference form. If `G` is supported in an interior interval and extended by zero to the line, then

\[
D_A[G]\le \widetilde D[G]
:=\frac12\iint_{\mathbb R^2}
h(|s-t|)|G(s)-G(t)|^2\,ds\,dt,
\tag{9}
\]

and

\[
\widetilde D[G]
=\frac1{2\pi}\int_{\mathbb R}d(\xi)|\widehat G(\xi)|^2\,d\xi.
\tag{10}
\]

Because `q\mapsto d(\sqrt q)` is increasing and concave, Jensen gives

\[
\frac{\widetilde D[G]}{\|G\|_2^2}
\le
 d\!\left(\frac{\|G'\|_2}{\|G\|_2}\right).
\tag{11}
\]

WI-373 uses the first Dirichlet modes on a macroscopic interior interval to obtain the unconstrained lower density `q_\eta/\pi`. The only new issue here is whether forcing zero values on all true arithmetic source slots destroys that band of trial directions. It does not.

## 2. On every fixed macroscopic interior, the source perforations have vanishing screened capacity

Fix

\[
0<\delta<\frac12
\]

and write

\[
I_{k,\delta}
=[\delta A_k,(1-\delta)A_k],
\qquad
L_{k,\delta}=(1-2\delta)A_k.
\tag{12}
\]

Every Desogus source slot has the same logarithmic width

\[
\varepsilon_k
=\log\left(1+\frac1k\right)
\le \frac1k.
\tag{13}
\]

If a source slot `J_{k,n}` intersects `I_{k,\delta}`, then its right endpoint is at least `\delta A_k`, hence

\[
\log n\le(1-\delta)A_k,
\qquad
n\le(k+1)^{1-\delta}.
\tag{14}
\]

Let `M_{k,\delta}` be the number of active prime-power slots meeting `I_{k,\delta}`. The classical prime-power count gives

\[
M_{k,\delta}
=O\!\left(\frac{k^{1-\delta}}{\log k}\right).
\tag{15}
\]

Consequently the total removed logarithmic length in this fixed macroscopic interior is

\[
\boxed{
|S_k\cap I_{k,\delta}|
=O\!\left(\frac{k^{-\delta}}{\log k}\right)=o(1).
}
\tag{16}
\]

More importantly for the nonlocal form, the holes have vanishing **screened capacity cost**. Let `\chi_{k,\delta}` equal zero on the source slots meeting `I_{k,\delta}` and one away from them; enlarge the slots by a fixed multiple of `\varepsilon_k` if a smooth cutoff is desired. For a single interval of length `O(\varepsilon_k)`,

\[
\frac12\iint h(|s-t|)
|\chi(s)-\chi(t)|^2\,ds\,dt
\le
C\int_0^{C\varepsilon_k}H(x)\,dx.
\tag{17}
\]

Since

\[
H(x)=\log2+\frac\pi4-\frac12\log x+o(1)
\qquad(x\downarrow0),
\tag{18}
\]

summing (17) over all relevant slots gives

\[
\boxed{
\kappa_{k,\delta}
:=
\frac12\iint_{\mathbb R^2}h(|s-t|)
|\chi_{k,\delta}(s)-\chi_{k,\delta}(t)|^2\,ds\,dt
=O(k^{-\delta})=o(1).
}
\tag{19}
\]

This is the step that strengthens WI-376. If one works all the way to a fixed physical distance from the left endpoint, there are `O(k/\log k)` holes and their aggregate screened jump cost is only `O(1)`. By retreating a fixed *fraction* `\delta A_k` into the bulk, only prime powers up to `k^{1-\delta+o(1)}` can occur, so the aggregate cost actually tends to zero. The full density is recovered only after the limit `k\to\infty` by sending `\delta\downarrow0`.

## 3. Masking a linear Dirichlet band costs `o(1)` uniformly

Let `V_{k,\delta,m}` be the span of the first `m` Dirichlet modes on `I_{k,\delta}`. For every `G\in V_{k,\delta,m}`,

\[
\frac{\|G'\|_2}{\|G\|_2}
\le \frac{m\pi}{L_{k,\delta}},
\tag{20}
\]

and the elementary reproducing-kernel bound for the sine basis gives

\[
\boxed{
\|G\|_\infty^2
\le \frac{2m}{L_{k,\delta}}\|G\|_2^2.
}
\tag{21}
\]

Take

\[
F=\chi_{k,\delta}G.
\tag{22}
\]

The removed mass estimate (16) and (21) imply, uniformly on the whole `m`-dimensional band whenever `m=O(A_k)`,

\[
\|F\|_2^2
=(1-o(1))\|G\|_2^2.
\tag{23}
\]

For the screened energy, use for any `\tau>0`

\[
|\chi(s)G(s)-\chi(t)G(t)|^2
\le
(1+\tau)|G(s)-G(t)|^2
+(1+\tau^{-1})|G(t)|^2|\chi(s)-\chi(t)|^2.
\tag{24}
\]

Equations (19), (21), and (24) yield

\[
\widetilde D[F]
\le
(1+\tau)\widetilde D[G]
+(1+\tau^{-1})
\frac{2m}{L_{k,\delta}}
\kappa_{k,\delta}\|G\|_2^2.
\tag{25}
\]

Choosing, for example,

\[
\tau=\sqrt{\kappa_{k,\delta}},
\]

and using `m/L_{k,\delta}=O(1)` shows uniformly on the band that

\[
\boxed{
\frac{D_{A_k}[F]}{\|F\|_2^2}
\le
 d\!\left(\frac{m\pi}{L_{k,\delta}}\right)+o(1).
}
\tag{26}
\]

The endpoint and Hankel remainders are unchanged in character by the mask. Since every `F` is supported in `I_{k,\delta}`,

\[
\frac{E_{A_k}[F]+J_{A_k}[F]}{\|F\|_2^2}
\le
2H(\delta A_k)
+A_k(1-2\delta)h(2\delta A_k)
=o(1).
\tag{27}
\]

The indicator cutoff in (22) has finite screened energy because the kernel has only the logarithmically integrable jump cost quantified in (17). If one wants to remain on a smooth form core, first enlarge each source slot by `O(\varepsilon_k)`, interpolate smoothly across the added margins, and use the same estimates; finite-dimensional Dirichlet-band approximation then gives the identical asymptotic conclusion while preserving exact zero values on the original slots.

## 4. Min-max gives the source-conditioned index density

Fix `0\le\eta<C_\Gamma` and choose `\delta>0`. Let

\[
c<\frac{(1-2\delta)q_\eta}{\pi}
\tag{28}
\]

and set

\[
m_k=\lfloor cA_k\rfloor.
\tag{29}
\]

Then

\[
\frac{m_k\pi}{L_{k,\delta}}
\longrightarrow
\frac{c\pi}{1-2\delta}
<q_\eta.
\tag{30}
\]

By strict monotonicity of `d`, equations (1) and (30) leave a fixed margin `\mu>0` such that for all sufficiently large `k`,

\[
d\!\left(\frac{m_k\pi}{L_{k,\delta}}\right)
\le C_\Gamma-\eta-\mu.
\tag{31}
\]

Combining (5), (26), (27), and (31) gives

\[
\mathcal A_{A_k}[F]
\le-(\eta+\mu/2)\|F\|_2^2
\tag{32}
\]

for every nonzero masked vector `F` in the image of `V_{k,\delta,m_k}`, once `k` is large enough. Equation (23) shows that the masking map is injective there, so this image still has dimension `m_k` and lies in the source-zero form domain. Hence

\[
\liminf_{k\to\infty}
\frac{\iota^{\rm src}_{\eta,k}}{A_k}
\ge c.
\]

First let `c` increase to `(1-2\delta)q_\eta/\pi`, then let `\delta\downarrow0`. This proves (3).

The same argument at `\eta=0`, always keeping a strict `c< (1-2\delta)q_0/\pi` before the limits, proves (4).

## 5. Consequence for corrected common-cut repairs

WI-376 proved that true source slots leave the constrained form bottom asymptotic to `-C_\Gamma`. The present result rules out a substantially stronger hope: source perforation also fails to collapse the extensive negative sector to a few exceptional directions.

Suppose, only for this corollary, that a proposed repair on the source-zero space can be represented by a bounded self-adjoint additive form `K_k` with

\[
\mathcal A_{A_k}^{\rm src}+K_k\succeq0.
\tag{33}
\]

For every fixed `0<t<C_\Gamma`, min-max applied to (3) gives

\[
\boxed{
\liminf_{k\to\infty}
\frac{N_k^+(t)}{A_k}
\ge\frac{q_t}{\pi},
}
\tag{34}
\]

where `N_k^+(t)` counts positive eigenvalues of `K_k` above `t` on the constrained space. In particular a uniformly finite-rank or `o(A_k)`-rank correction cannot repair the source-zero archimedean block.

This is the source-conditioned analogue of the additive spectral gate in WI-373. It does **not** classify Desogus's actual rooted Schur network as additive. Rather, it sharpens the remaining burden exposed by WI-375--WI-376: any valid corrected common-cut theorem must import genuinely extensive coercivity from the inherited/global/arithmetic form before the source-complement infimum, or use an exact elimination whose admissible complement is smaller than the source-zero space studied here.

## 6. Primary-source and prior-art audit

**Primary source under audit.** Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1, submitted 17 September 2026, https://arxiv.org/abs/2609.20367. The arXiv record was rechecked on 21 September 2026 and remained at version 1. The source routing in Gate II is the origin of the exact intervals `J_{k,n}`; WI-368--WI-376 independently audit the gamma-retaining form and the downstream common-cut dependency. No RH conclusion from the preprint is imported here.

**Internal exact inputs.** WI-369 supplies the corrected positive-remainder decomposition and `C_\Gamma`; WI-373 supplies the exact digamma symbol, its strict monotonicity, and the unconstrained Dirichlet-band negative-index argument; WI-376 supplies the exact source-slot geometry and establishes the weaker source-constrained bottom result. The new step is the macroscopic-interior count (14)--(19) and the uniform band masking (21)--(32), which upgrade the bottom obstruction to a fixed-depth extensive index obstruction.

**Classical arithmetic.** The only number-theoretic estimate added here is the standard count of prime powers `Q(x)=O(x/\log x)`. No prime correlation theorem, zero-density estimate, or RH-dependent input is used.

**Perforated-domain context.** There is a substantial homogenization literature for local operators on perforated domains, and Pereira--Rossi, *Nonlocal problems in perforated domains* (Proc. Roy. Soc. Edinburgh A 150 (2020), arXiv:1804.10234), studies Dirichlet holes for nonlocal integral operators. That paper assumes a nonsingular kernel and analyzes weak limits/periodic perforations; it does not supply the singular screened-kernel estimate, the arithmetic source geometry, or the digamma negative-index statement used here. The present proof therefore uses the direct capacity estimate (17)--(19) rather than importing a homogenization theorem.

A targeted web audit on 21 September 2026 found the Desogus preprint still at v1 and no public correction or independent technical discussion deriving the source-perforated digamma index profile (3). Search absence is recorded only as an audit result; no priority claim is made.

## Research consequence

The remaining Desogus repair gate is narrower than after WI-376. The exact source slots cannot cure the gamma problem by removing a thin set of bad coordinates: after source-zero conditioning, the corrected block still carries the full WI-373 **certified** fixed-depth negative-index density. A repaired common-cut argument therefore needs a coercive inherited/global channel with macroscopic spectral content, or a genuinely different elimination that removes those bulk modes before the ordinary variational short. A scalar reserve, finite-rank patch, or sublinear-rank additive correction is structurally incapable of doing so.
