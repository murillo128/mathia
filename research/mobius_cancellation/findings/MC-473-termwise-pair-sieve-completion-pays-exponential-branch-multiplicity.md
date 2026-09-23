# MC-473 — Termwise pair-sieve completion pays exponential branch multiplicity

**Status:** `EXACT-DERIVED` · `CLASSICAL-INGREDIENTS` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The incomplete rough×rough discrepancy isolated in `MC-472` admits an exact Möbius expansion, but the most direct way to combine that expansion with the classical square-root complete-sum bound is quantitatively unusable at the live sieve scale. The obstruction is not the translated-ratio phase itself; it is the number of local pair-sieve branches created before cancellation between divisor levels is retained.

Let `p` be prime, let `chi` be a nonprincipal character modulo `p`, let `h not= 0 (mod p)`, and let `W` be square-free with `(W,p)=1`. Write

\[
K_h(n)=\chi(n+h)\overline{\chi(n)},
\qquad
A_{W,h}(n)=\mathbf 1_{(n(n+h),W)=1},
\]

and let

\[
\delta_W(h)=\prod_{q\mid W}\left(1-\frac{\nu_q(h)}q\right),
\qquad
\nu_q(h)=\begin{cases}1,&q\mid h,\\2,&q\nmid h.\end{cases}
\]

For an integer interval `I` of length `H`, recall the centered discrepancy

\[
\mathcal D_{W,h}(I)
=
\sum_{n\in I}K_h(n)A_{W,h}(n)
+\frac{H}{p}\delta_W(h).
\tag{1}
\]

For each divisor `d|W`, let

\[
\mathcal R_d(h)=\{a\bmod d:a(a+h)\equiv0\pmod d\},
\qquad
\nu_d(h)=|\mathcal R_d(h)|=\prod_{q\mid d}\nu_q(h).
\tag{2}
\]

Exact inclusion-exclusion gives

\[
A_{W,h}(n)
=
\sum_{\substack{d\mid W\\d\mid n(n+h)}}\mu(d).
\tag{3}
\]

For `a in R_d(h)`, put

\[
N_{d,a}(I)=\#\{n\in I:n\equiv a\pmod d\}
\]

and

\[
E_{d,a}(I)
=
\sum_{\substack{n\in I\\n\equiv a\pmod d}}K_h(n)
+\frac{N_{d,a}(I)}p.
\tag{4}
\]

Because `d` is invertible modulo `p`, the progression `n=a+dm` turns the phase in `(4)` into the same bounded-complexity translated-ratio character phase on an affine coordinate. The complete `p`-sum is `-1`, and the nonzero additive Fourier coefficients satisfy the classical Weil bound `O(sqrt(p))`, exactly as in `MC-448`. Fourier completion of the residual interval therefore gives the uniform bound

\[
\boxed{
|E_{d,a}(I)|\ll \sqrt p\log(2p)
}
\tag{5}
\]

for every `d|W`, every admissible residue `a`, and every interval length `H`. Complete `p`-blocks contribute zero after the centering in `(4)`, so no restriction `H<=p` is needed for `(5)`.

Substitution into `(1)` yields the exact decomposition

\[
\mathcal D_{W,h}(I)
=
\sum_{d\mid W}\mu(d)
\sum_{a\in\mathcal R_d(h)}E_{d,a}(I)
+
\frac1p
\sum_{d\mid W}\mu(d)
\left(
\frac{H\nu_d(h)}d-\sum_{a\in\mathcal R_d(h)}N_{d,a}(I)
\right).
\tag{6}
\]

Since each residue-class count differs from `H/d` by less than one, taking absolute values **term by term** in `(6)` gives

\[
\boxed{
|\mathcal D_{W,h}(I)|
\ll
\left(\sqrt p\log(2p)+\frac1p\right)
\mathcal B_W(h),
}
\tag{7}
\]

where the exact branch multiplicity is

\[
\boxed{
\mathcal B_W(h)
:=\sum_{d\mid W}\nu_d(h)
=
\prod_{q\mid W}\bigl(1+\nu_q(h)\bigr).
}
\tag{8}
\]

For the primorial pair sieve `W=W_z` of `MC-472`, every local factor in `(8)` is either `2` or `3`. Consequently

\[
\boxed{
2^{\omega(W_z)}
\le \mathcal B_{W_z}(h)
\le 3^{\omega(W_z)}.
}
\tag{9}
\]

More precisely,

\[
\mathcal B_W(h)
=2^{\omega((h,W))}
 3^{\omega(W)-\omega((h,W))}.
\tag{10}
\]

Thus exact full inclusion-exclusion followed by separate Fourier/Weil completion of every congruence branch destroys the pair-sieve structure before the character estimate is used. In the source regime `H<=p`, this route can beat the trivial `O(H)` bound only if

\[
\mathcal B_W(h)
\ll \frac{H}{\sqrt p\log p}
\le \frac{\sqrt p}{\log p}.
\tag{11}
\]

The lower bound in `(9)` makes `(11)` impossible once the primorial contains more than `O(log p)` sieve primes. In particular, if the sieve cutoff is a fixed positive power of `p`, then `omega(W_z)=pi(z)+O(1)` and the prime number theorem makes `2^{omega(W_z)}` superpolynomial in `p`; the termwise route is then not merely short of a conductor-power saving but much worse than the trivial estimate.

For the concrete empty-vector upper-sieve parameters of `MC-470`,

\[
z=D^{\varepsilon^2}.
\tag{12}
\]

Hence in any subregime where `D>=p^kappa` for fixed `kappa>0` and fixed sieve parameter `epsilon>0`, `(9)` already makes the full-inclusion-exclusion/termwise-completion strategy catastrophically noncompetitive. This conditional specialization is only a method audit; no assumption is made here that every live source cell satisfies such a relation between `D` and `p`.

The conclusion is deliberately method-specific. Equation `(7)` does **not** say that the actual discrepancy is large. It says that a proof which expands the exact pair sieve completely and then takes absolute values after estimating each divisor/residue branch independently has discarded the cancellation needed to make the sieve affordable. Any viable sieve/trace-function estimate must preserve additional structure across divisor levels, use a truncated/factorable sieve with a quantitatively controlled approximation error, or create a bilinear/dispersion estimate before branchwise absolute values.

No estimate for `M(x)`, no zero-free region, and no RH consequence follows.

## 1. Exact divisor and residue decomposition

Because `W` is square-free,

\[
\mathbf 1_{(n(n+h),W)=1}
=
\sum_{d\mid(n(n+h),W)}\mu(d),
\]

which is `(3)`. For each prime `q|d`, the congruence `q|n(n+h)` has exactly `nu_q(h)` solutions modulo `q`; CRT therefore gives `(2)`.

Summing `(3)` against `K_h(n)` on `I` gives

\[
\sum_{n\in I}K_h(n)A_{W,h}(n)
=
\sum_{d\mid W}\mu(d)
\sum_{a\in\mathcal R_d(h)}
\sum_{\substack{n\in I\\n\equiv a\pmod d}}K_h(n).
\tag{13}
\]

Also the Euler product in `MC-472` expands as

\[
\delta_W(h)
=
\sum_{d\mid W}\mu(d)\frac{\nu_d(h)}d.
\tag{14}
\]

Adding the centering term from `(1)`, then adding and subtracting `N_{d,a}(I)/p` in every residue branch, proves `(6)` exactly.

The second term in `(6)` is only the ordinary finite-interval discrepancy of the pair-sieve residue classes. Since

\[
\left|N_{d,a}(I)-\frac Hd\right|<1,
\]

its absolute contribution is at most `p^(-1) sum_{d|W} nu_d(h)`. The expensive factor therefore appears even before any subtle endpoint analysis.

## 2. Each individual progression is easy

Write `n=a+dm`. Modulo `p`, multiplication by `d` is invertible. The phase becomes

\[
\chi(a+dm+h)\overline{\chi(a+dm)},
\]

which is an affine reparametrization of the rational phase used in `MC-448`. Over a complete `m (mod p)` period its sum is exactly `-1`. For nonzero additive frequency, the mixed multiplicative/additive transform is a fixed-degree rational character sum and has size `O(sqrt(p))` by the same classical Weil estimate anchored in `MC-S55`.

Fourier completion gives

\[
\sum_{m\in J}K_h(a+dm)+\frac{|J|}{p}
\ll
\frac{\sqrt p}{p}
\sum_{t\ne0}
\left|\sum_{j=1}^{|J|}e_p(tj)\right|
\ll \sqrt p\log(2p),
\tag{15}
\]

for a residual interval `J` shorter than `p`. If the original progression segment is longer, split it into complete `p`-blocks plus one residual segment; the centered contribution of every complete block is exactly zero. This proves `(5)` for arbitrary `H`.

So the branchwise character problem is not hard. The loss occurs when the independently easy branches are recombined with a triangle inequality.

## 3. The pair-sieve branching cost is exponential in the number of sieve primes

Multiplicativity of `nu_d(h)` over square-free `d|W` gives

\[
\sum_{d\mid W}\nu_d(h)
=
\prod_{q\mid W}(1+\nu_q(h)),
\]

proving `(8)`. A prime dividing `h` contributes `2`; every other sieve prime contributes `3`, proving `(9)`--`(10)`.

This is materially different from the complete-period calculation of `MC-472`. There, CRT factorization is beneficial because the entire local sieve product is kept intact and contributes only the density `delta_W(h)`. Here the full Möbius expansion exposes every local forbidden-class choice separately; taking absolute values converts those choices into the branch count `B_W(h)`.

The same distinction explains why the result is not contradicted by the existence of classical sifted-character-sum estimates. Those estimates do not normally pay for all exact inclusion-exclusion branches independently; they use truncated sieve weights, averaging, bilinear structure, or another device that preserves cancellation/approximation across divisor levels.

## 4. Prior art and novelty boundary

The mathematical ingredients of `(3)`--`(15)` are classical. Möbius inclusion-exclusion and CRT are elementary sieve theory. The complete rational-character Fourier estimate is the same bounded-complexity Weil input already anchored by Cochrane and Pinner in `MC-S55` and used in `MC-448`.

A targeted literature check on 23 September 2026 also reconfirmed that **sifted character sums are an established subject**, so no broad no-go is claimed. Jan-Christoph Schlage-Puchta, *Sifted character sums and free quotients of Bianchi groups*, Mathematical Proceedings of the Cambridge Philosophical Society 141 (2006), 205--207, DOI `10.1017/S0305004106009261`, derives an estimate for a sifted character sum for a different arithmetic application. Modern sieve treatments likewise combine fundamental-lemma weights with character-sum input rather than paying full exact inclusion-exclusion branchwise.

Accordingly, the durable result is narrower: for the **specific two-sided pair-sieve discrepancy of `MC-472`**, the exact branch multiplicity `(8)` shows quantitatively why full inclusion-exclusion followed by independent completion cannot supply the desired conductor-power estimate at a growing primorial sieve cutoff. No novelty is claimed for the underlying sieve or Weil estimates.

## Boundaries and falsification tests

- **This is a no-go for a proof architecture, not for the discrepancy.** Large `B_W(h)` is an upper-bound tariff created by taking absolute values; it is not a lower bound for `|D_{W,h}(I)|`.
- **Structured sieve weights remain live.** A beta/linear sieve, Buchstab decomposition, Heath-Brown/Vaughan-type identity, or factorable divisor decomposition may retain cancellation across divisor levels and avoid `(8)`. Such a route must quantify its approximation/error against the oscillatory phase rather than infer it from positivity alone.
- **Bilinear and dispersion routes remain live.** If divisor branches are coupled before Cauchy/triangle closure, `(7)` does not apply.
- **The fixed-power specialization is conditional.** The statement after `(12)` assumes `D>=p^kappa`; cells outside that relation require their own parameter accounting.
- **Shift divisibility only changes bases `3` to `2`.** Even maximal degeneration cannot make the full branch count polynomial in the number of sieve primes; the exact formula `(10)` must be used rather than a generic-density heuristic.
- **The centering is essential.** The `+N_{d,a}/p` term in `(4)` removes the exact complete mean `-1/p`. Dropping it would mix the already-solved complete bias of `MC-472` into the incomplete error.
- **No claim is made for boundary channels.** The mixed `R_zE`, `ER_z`, and `EE` terms of `MC-471` have different combinatorics and are not estimated here.

## Consequence for the research line

The rough×rough branch should no longer spend effort on **full exact Möbius expansion of both roughness constraints followed by a separate Pólya--Vinogradov/Weil completion on every congruence branch**. The individual character sums are easy, but the branch count destroys the conductor saving.

The next viable rough×rough test must keep the sieve compressed while the character phase is still oscillatory. Concretely, it should ask whether a truncated/factorable pair-sieve representation can achieve a sufficiently small approximation error and a divisor-level character estimate simultaneously, or whether a bilinear/dispersion transform can couple the divisor branches before absolute values. That is a strictly narrower target than the generic incomplete discrepancy posed after `MC-472`.