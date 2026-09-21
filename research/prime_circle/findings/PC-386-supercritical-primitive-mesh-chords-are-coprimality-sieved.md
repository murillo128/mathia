# PC-386 — supercritical primitive-shell mesh chords are coprimality-sieved lattice kernels

**Status:** `EXACT-DERIVED` + `ASYMPTOTIC-DERIVED` + `LITERATURE-ANCHORED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the exact-order primitive restriction of the mesh-scale inverse-chord branch classified for full root fibers in PC-384--PC-385.

PC-384--PC-385 show that inverse-power common-anchor chord kernels on the full `m`-th root fiber have universal mesh/submesh laws depending on the analytic singularity and scale, not on the arithmetic of `m`. That conclusion does **not** survive restriction to the exact-order primitive shell. The primitive mask reintroduces arithmetic at mesh scale, but in the supercritical range it does so in a completely identifiable way: the boundary layer is just the one-dimensional lattice kernel with a coprimality sieve.

This is a useful correction of scope rather than a new RH mechanism. The primitive shell genuinely distinguishes prime from highly composite degree at the natural singular scale, but the retained information is exactly Möbius/Ramanujan divisibility data. At inverse square and zero cutoff it collapses to the Jordan totient `J_2`, and after normalization by the primitive-shell size it is Dedekind's `psi`, whose primorial extreme-value criterion is already classically RH-equivalent.

## 1. Primitive restriction is exact Möbius/Ramanujan filtering

For `alpha>0`, `eta>0`, define the primitive-shell common-anchor energy

\[
S_m(\alpha,\eta)
:=\sum_{\substack{1\le a<m\\(a,m)=1}}
\bigl[2(\cosh\eta-\cos(2\pi a/m))\bigr]^{-\alpha}.
\tag{1}
\]

If `g` is any function for which the finite sums below are defined, the exact-order decomposition of roots of unity gives

\[
\sum_{\operatorname{ord}(w)=m}g(w)
=\sum_{d\mid m}\mu(m/d)\sum_{w^d=1}g(w).
\tag{2}
\]

Thus the primitive observable is not a new independent geometric object layered on top of the full fiber: it is the Möbius extraction of exact order from full-root observables. For `eta>0`, where the Fourier series is absolutely convergent, the same fact is

\[
S_m(\alpha,\eta)
=\sum_{k\in\mathbb Z}\widehat g_{\alpha,\eta}(k)c_m(k),
\qquad
 g_{\alpha,\eta}(\theta)
=[2(\cosh\eta-\cos\theta)]^{-\alpha},
\tag{3}
\]

with `c_m(k)` the Ramanujan sum. Equations (2)--(3) are classical structure and are the first novelty control: any arithmetic retained by primitive restriction must survive this explicit divisor/Fourier description.

## 2. Supercritical mesh-scale limit

Set the regularization at one root-spacing,

\[
\eta_m=\frac{\tau}{m},\qquad \tau\ge0,
\tag{4}
\]

and suppose `alpha>1/2`. Let `m_j -> infinity` be a sequence along which, for every fixed prime `p`, the indicator `1_(p|m_j)` eventually stabilizes. Every degree sequence has such a subsequence by a diagonal extraction. Define

\[
\mathcal P_\infty
:=\{p:\ p\mid m_j\ \text{eventually}\}.
\tag{5}
\]

Then

\[
\boxed{
 m_j^{-2\alpha}S_{m_j}(\alpha,\tau/m_j)
 \longrightarrow
 2\sum_{\substack{r\ge1\\p\nmid r\ \forall p\in\mathcal P_\infty}}
 (\tau^2+4\pi^2r^2)^{-\alpha}.
}
\tag{6}
\]

The proof is elementary but exposes exactly where the arithmetic survives. Pair `a` with `m-a`. For fixed `a`,

\[
m^2\,2\bigl(\cosh(\tau/m)-\cos(2\pi a/m)\bigr)
\longrightarrow \tau^2+4\pi^2a^2.
\tag{7}
\]

For `1<=a<=m/2`,

\[
2(\cosh(\tau/m)-\cos(2\pi a/m))
\ge 4\sin^2(\pi a/m)
\ge 16a^2/m^2,
\tag{8}
\]

so after multiplying by `m^(-2 alpha)` the summand is bounded by `16^(-alpha)a^(-2 alpha)`. This is summable exactly in the present range `alpha>1/2`. Finally, for each fixed `a`, the finite set of prime divisors of `a` sees only stabilized divisibility decisions in (5), hence

\[
\mathbf 1_{(a,m_j)=1}
\longrightarrow
\mathbf 1_{p\nmid a\ \forall p\in\mathcal P_\infty}.
\tag{9}
\]

Dominated convergence gives (6). The result is therefore sequence-dependent, unlike the full-fiber law, but its entire sequence dependence is the limiting prime-divisor sieve.

Two controls make the distinction sharp. Along distinct primes `m_j=p_j -> infinity`, no fixed prime survives in `mathcal P_infty`, and (6) becomes

\[
2\sum_{r\ge1}(\tau^2+4\pi^2r^2)^{-\alpha}.
\tag{10}
\]

Along primorials `m_j=\prod_{p\le x_j}p`, every fixed prime eventually belongs to `mathcal P_infty`, so only `r=1` survives:

\[
2(\tau^2+4\pi^2)^{-\alpha}.
\tag{11}
\]

Thus primitive restriction really does defeat the degree-blind universality of PC-384--PC-385. What replaces it, however, is not a new spectral law but a coprimality-sieved lattice sum.

At `tau=0`, (6) reduces to the Euler-product form

\[
2(2\pi)^{-2\alpha}\zeta(2\alpha)
\prod_{p\in\mathcal P_\infty}(1-p^{-2\alpha}),
\qquad \alpha>\tfrac12.
\tag{12}
\]

For a finite limiting sieve and `|tau|<2 pi`, expansion of (6) likewise produces only positive-real values `zeta(2 alpha+2j)` multiplied by finite Euler factors. There is no free complex spectral parameter, completed-zeta symmetry, or critical-line selector in this scalar boundary layer.

## 3. Exact inverse-square formula

The case `alpha=1` can be evaluated before taking any limit. For `eta>0`, the full `d`-root average of the Poisson-type kernel is

\[
\sum_{a=0}^{d-1}
\frac{1}{2(\cosh\eta-\cos(2\pi a/d))}
=\frac{d}{2\sinh\eta}\coth\!\left(\frac{d\eta}{2}\right).
\tag{13}
\]

Applying (2) yields the exact primitive-shell identity

\[
\boxed{
S_m(1,\eta)
=\frac{1}{2\sinh\eta}
\sum_{d\mid m}\mu(m/d)d\,
\coth\!\left(\frac{d\eta}{2}\right).
}
\tag{14}
\]

For `m>1`, the common singular terms cancel under Möbius inversion as `eta -> 0`. Expanding `coth` gives

\[
\boxed{
S_m(1,0)
=\sum_{\substack{1\le a<m\\(a,m)=1}}
|1-\zeta_m^a|^{-2}
=\frac{J_2(m)}{12}.
}
\tag{15}
\]

Since `J_2(m)/phi(m)=psi(m)`, where

\[
\psi(m)=m\prod_{p\mid m}(1+1/p)
\tag{16}
\]

is Dedekind's psi function, the energy per primitive vertex is exactly

\[
\boxed{
\frac{S_m(1,0)}{\phi(m)}=\frac{\psi(m)}{12}.
}
\tag{17}
\]

This endpoint is compatible with PC-020's anchored-jet classification by Jordan totients: the singular chord observable has not escaped that classical arithmetic layer. For the prime control in the mesh limit, (10) at `alpha=1` can also be summed explicitly,

\[
2\sum_{r\ge1}(\tau^2+4\pi^2r^2)^{-1}
=\frac{1}{2\tau}\coth(\tau/2)-\frac1{\tau^2},
\tag{18}
\]

with the removable `tau=0` limit understood.

## 4. Novelty audit and RH consequence

The exact-order extraction (2), Ramanujan representation (3), and Jordan-totient endpoint (15) are classical arithmetic mechanisms. Recent work of Liu--Xin systematizes broad families of root-of-unity weighted trigonometric power sums using constant-term and Bernoulli/Euler-polynomial methods; it is further evidence that finite trigonometric power sums themselves are not a novel RH bridge. I did not locate a source stating exactly the subsequential mesh-limit formulation (6), so (6) is useful as a prime-circle boundary theorem, but its surviving arithmetic mechanism is visibly the standard coprimality sieve rather than a new source of zeta zeros.

There is an especially strong prior-art control at `alpha=1`. Solé--Planat prove that for primorials `N_n`, the inequality

\[
\frac{\psi(N_n)}{N_n\log\log N_n}
>\frac{e^\gamma}{\zeta(2)}
\tag{19}
\]

for all `n>=3` is equivalent to the Riemann hypothesis. Therefore any RH-sensitive threshold extracted from the normalized zero-cutoff scalar (17) along primorials is already the known Dedekind-psi criterion in geometric notation; it cannot count as a new prime-circle mechanism.

The decisive boundary is consequently two-sided. Full-root mesh-scale inverse-power chords are arithmetic-blind (PC-384--PC-385), while exact-order primitive restriction restores arithmetic but only as Möbius/Ramanujan coprimality filtering of a universal one-dimensional boundary kernel. A surviving RH mechanism would have to organize this primitive boundary-layer information **before scalarization** -- for example through genuinely cross-level, tensorial, phase-sensitive, nonnormal, or otherwise nonseparable structure -- in a way that cannot be reduced to the sieve in (6).

The theorem is deliberately scoped to `alpha>1/2`, where the endpoint boundary layer is summable. No claim is made here that the critical or subcritical primitive-shell regimes `alpha<=1/2` obey the same normalized limit.

## Sources

- Patrick Solé and Michel Planat, *Extreme values of the Dedekind Psi function*, arXiv:1011.1825 (2010): https://arxiv.org/abs/1011.1825 . In particular, the primorial Dedekind-psi criterion used in (19).
- Jiahang Liu and Guoce Xin, *Root-of-unity weighted trigonometric power sums: a constant term approach*, arXiv:2607.29130 (2026): https://arxiv.org/abs/2607.29130 . Prior-art control for finite root-of-unity weighted trigonometric power sums.
- The line source registry `research/prime_circle/SOURCES.md` supplies the standing cyclotomic, Möbius/Ramanujan, harmonic-root, and related prior-art anchors used throughout this research line.
