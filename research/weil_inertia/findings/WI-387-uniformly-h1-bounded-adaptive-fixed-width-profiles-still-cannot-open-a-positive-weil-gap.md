# WI-387 — Uniformly H1-bounded adaptive fixed-width profiles still cannot open a positive Weil gap

**Status:** `EXACT-DERIVED + CLASSICAL-WEIL-SPECTRAL-SIDE + CLASSICAL-BOHR-RECURRENCE + PRIME-POWER-SPARSITY + DECISIVE-COERCIVITY-BARRIER + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-386 showed that replacing the first-Dirichlet cosine by any one fixed sufficiently regular even profile does not rescue the fixed-width Desogus source-zero trial: under RH the Weil value still has subsequences tending to zero. The fixed-profile hypothesis is not load-bearing either. Arbitrary endpoint-dependent changes of shape are still unable to open a uniform positive Weil gap as long as the family remains spectrally tight; in particular, a uniform `H^1` bound is sufficient.

Fix `L>0`. For every integer `k` let

\[
g_k\in C_c^2((-L/2,L/2);\mathbb R),
\qquad g_k(-s)=g_k(s),
\qquad \|g_k\|_2=1,
\tag{1}
\]

and suppose

\[
\sup_k\|g_k'\|_2\le M<\infty.
\tag{2}
\]

Set

\[
A_k=\log(k+1),
\qquad
f_k^0(y)=g_k(y-A_k/2)-g_k(y+A_k/2),
\tag{3}
\]

and let `f_k` be the corresponding exact source-zero trial obtained by imposing, lobe by lobe, the same prime-power source-slot cutoffs and screened smoothing convention used in WI-377, WI-380, WI-384, and WI-386. Then, **if RH holds**,

\[
\boxed{
\liminf_{k\to\infty}\mathcal W[f_k]=0.
}
\tag{4}
\]

Consequently no such uniformly `H^1`-bounded, fixed-width, endpoint-adaptive profile family can provide a positive asymptotic Gate-II coercivity tariff. Any escape through fixed-width shape adaptation must leave every bounded-`H^1` class; more intrinsically, it must destroy uniform spectral tightness at the zeta-zero frequencies.

The stronger abstract statement is the real mechanism. Write

\[
G_k(z)=\int_{\mathbb R}g_k(s)e^{zs}\,ds.
\tag{5}
\]

If a normalized fixed-width even family satisfies

\[
\lim_{T\to\infty}\sup_k
\sum_{|\gamma|>T}m_\gamma |G_k(i\gamma)|^2=0,
\tag{6}
\]

then the unperforated trials already satisfy

\[
\boxed{
\liminf_{k\to\infty}\mathcal W[f_k^0]=0
}
\qquad\text{under RH}.
\tag{7}
\]

Condition (2) is only a convenient sufficient condition for (6).

## 1. Spectral formula and a coefficient-independent recurrence argument

Under RH, the same Weil spectral identity used in WI-385 and WI-386 gives, for every `k`,

\[
\mathcal W[f_k^0]
=
4\sum_{\gamma}m_\gamma |G_k(i\gamma)|^2
\sin^2\!\left(\frac{\gamma A_k}{2}\right).
\tag{8}
\]

Evenness is used here to keep `G_k(i\gamma)` real and the separated odd-pair contribution manifestly nonnegative. The important change from WI-386 is that the coefficients
`|G_k(i\gamma)|^2` may now vary arbitrarily with `k`.

Fix `T>0`. There are only finitely many ordinates `\gamma` with `|\gamma|\le T`. By the classical simultaneous Bohr/Kronecker recurrence for a finite family of frequencies, for every `\eta>0` there are arbitrarily large `\tau` for which

\[
\max_{|\gamma|\le T}
\left|e^{i\gamma\tau}-1\right|<\eta.
\tag{9}
\]

This recurrence depends only on the frequencies, not on the coefficients of the trigonometric sum. That is precisely why endpoint-dependent profiles do not defeat it.

The endpoint lattice becomes asymptotically dense in the separation coordinate:

\[
A_{k+1}-A_k
=
\log\!\left(1+\frac1{k+1}\right)
\longrightarrow0.
\tag{10}
\]

Hence the arbitrarily large common return times in (9) can be approximated by a subsequence `A_{k_j}` with an error tending to zero. On the finite low-frequency set, the uniform support and normalization imply

\[
|G_k(i\gamma)|
\le \|g_k\|_1
\le \sqrt L\,\|g_k\|_2
=\sqrt L.
\tag{11}
\]

Thus choosing the common phase error sufficiently small makes the contribution of every `|\gamma|\le T` to (8) uniformly small, regardless of how `g_k` changes with `k`. Assumption (6) makes the complementary tail uniformly small. First choose `T` for the tail, then a common return for the finite head, and finally an exact endpoint `A_k` close to that return. Diagonalizing these choices proves (7).

This is stronger than a slow-variation statement: no continuity, convergence, or bounded step-to-step change of the profiles is used. Uniform spectral tightness is the only compactness property needed by the recurrence step.

## 2. A uniform H1 bound forces spectral tightness

Because every `g_k` is compactly supported in the same interval, integration by parts gives for `\gamma\ne0`

\[
|G_k(i\gamma)|
\le
\frac{\|g_k'\|_1}{|\gamma|}
\le
\frac{\sqrt L\,M}{|\gamma|}.
\tag{12}
\]

The classical zero-counting estimate `N(T)=O(T\log T)` and partial summation then yield

\[
\sum_{|\gamma|>T}\frac{m_\gamma}{\gamma^2}
=O\!\left(\frac{\log T}{T}\right).
\tag{13}
\]

Combining (12) and (13), uniformly in `k`,

\[
\sum_{|\gamma|>T}m_\gamma |G_k(i\gamma)|^2
\ll
LM^2\frac{\log T}{T}
\longrightarrow0.
\tag{14}
\]

Therefore every family satisfying (1)-(2) satisfies the abstract tightness hypothesis (6), and the unperforated zero-floor conclusion follows.

The contrapositive is useful for route design. If a fixed-width adaptive family is to avoid this recurrence obstruction, then it cannot remain uniformly spectrally tight. Within the natural Sobolev class above this forces

\[
\sup_k\|g_k'\|_2=\infty,
\tag{15}
\]

so any surviving fixed-width construction must develop increasing high-frequency or rough-profile complexity along some subsequence. Equation (15) is necessary for escaping this theorem, not sufficient for producing a positive Weil gap.

## 3. Exact source-slot perforation is uniformly negligible

It remains to check that the exact source-zero requirement does not reintroduce a positive margin. The estimates in WI-377, WI-384, and WI-386 are uniform over the present bounded-`H^1` family.

Let `x=k+1`. On either fixed-width translated lobe, WI-384 gives total source-hole measure

\[
\mu_k
=O_L\!\left(\frac1{\sqrt x\log x}\right),
\tag{16}
\]

while the screened cutoff-capacity accounting used in WI-377/WI-386 gives

\[
\kappa_k=O_L(x^{-1/2}).
\tag{17}
\]

The one-dimensional Sobolev inequality, together with (1)-(2), supplies a uniform `L^\infty` bound on `g_k`. If `\chi_k` denotes the smooth source cutoff on a lobe, put `p_k=\chi_k g_k` and `r_k=(1-\chi_k)g_k`. Then

\[
\|r_k\|_1=O_{L,M}(\mu_k),
\qquad
\|r_k\|_2^2=O_{L,M}(\mu_k).
\tag{18}
\]

For the corrected screened gamma seminorm `D`, the same decomposition used in WI-386 is now uniform because

\[
|g_k(s)-g_k(t)|^2
\le |s-t|\,\|g_k'\|_2^2
\le M^2|s-t|,
\tag{19}
\]

`u h(u)` is integrable for the screened kernel, the profile sup norm is uniform, and the cutoff-capacity term is bounded by `O_{L,M}(\kappa_k)`. Hence

\[
D[r_k]\to0,
\qquad
D[p_k]-D[g_k]\to0
\tag{20}
\]

uniformly along the endpoint sequence.

The arithmetic and polar comparisons also remain uniform. Writing `q_k=g_k*g_k`, convolution with the removed part changes the relevant profile by `O_{L,M}(\mu_k)` in sup norm. The same-lobe prime-power sum in a fixed logarithmic window contains only the fixed finite local set controlled in WI-384, while the critical-annulus coefficient mass is `O_L(\sqrt x)` by the Chebyshev estimate. Therefore the annular perturbation is

\[
O_{L,M}(\mu_k\sqrt x)
=O_{L,M}(1/\log x)
=o(1).
\tag{21}
\]

The polar moments have the same `O(\mu_k)` perturbation and hence the same `O(1/\log x)` endpoint effect. Cross-lobe/Hankel terms remain exponentially small because the lobe width is fixed and all needed profile norms are uniformly bounded. Consequently

\[
\boxed{
\mathcal W[f_k]-\mathcal W[f_k^0]\longrightarrow0.
}
\tag{22}
\]

Combining (7), nonnegativity under RH, and (22) proves (4).

## 4. What this closes and what it does not

WI-386 explicitly left genuinely `k`-dependent fixed-width profiles as a possible escape from its fixed-profile recurrence obstruction. The present argument closes that escape for every uniformly spectrally tight family, and therefore for every normalized uniformly `H^1`-bounded family on a fixed compact support. The obstruction is not that the profile happens to be a cosine, nor that it is unchanged with the endpoint: a finite low-frequency head has common coefficient-independent return times, while bounded Sobolev complexity prevents spectral mass from escaping indefinitely into the high-zero tail.

This does **not** rule out fixed-width families with unbounded `H^1` complexity, growing-width or multiscale trials, nonlocal constructions, or restrictions of the admissible graph/domain that alter the recurrence problem itself. It also does not prove the non-RH `-\infty` alternative from WI-385/386 for adaptive families: because `G_k` now changes with `k`, a family could in principle suppress selected off-line pole contributions. The theorem here is deliberately only the RH-compatible coercivity barrier needed to test this route.

No statement about the established simple-critical-zero proportion changes.

## Prior-art and novelty audit

The simultaneous recurrence input is classical Bohr/Kronecker theory for finitely many frequencies. The surrounding use of almost periodicity in zeta problems is already represented in the line's source ledger and in WI-386, including the Kaczorowski--Ramaré neighborhood. The Weil spectral identity, zero counting, and partial-summation tail estimate are classical ingredients. The exact prime-power source-slot and screened-capacity estimates are inherited from WI-377/WI-384/WI-386.

Internally, WI-318 already proves a bounded-`H^1` adaptation barrier for a different scalar-localizer architecture, but by a different high-carrier mechanism; it neither contains nor implies the coefficient-independent zeta-zero recurrence argument above. WI-386 proves the source-zero recurrence barrier for one fixed profile, not an arbitrary endpoint-dependent family.

A targeted audit around zeta almost periodicity, Weil-form source-zero trials, varying trigonometric coefficients, and bounded-Sobolev adaptive localizers found no source stating the combined implication (6)-(7) or its source-perforated consequence (4). That negative search result is **not** a priority claim. The mathematical contribution recorded here is the exact deduction that uniform spectral tightness makes the WI-386 recurrence obstruction coefficient-independent, plus the verification that a uniform fixed-width `H^1` bound is sufficient and survives the exact source-slot transfer.

## Evidence boundary

- **Classical / literature-backed:** Weil spectral formula under RH; finite-frequency Bohr/Kronecker simultaneous recurrence; `N(T)=O(T\log T)`; partial summation; Sobolev and Fourier integration-by-parts bounds; source sparsity and screened-capacity estimates already established in WI-377/WI-384/WI-386.
- **Exact deduction here:** uniform spectral tightness implies `\liminf \mathcal W[f_k^0]=0` even when the profile coefficients vary arbitrarily with `k`; uniform fixed-width `H^1` boundedness implies that tightness; the prior source-perforation estimates are uniform on this family, hence the exact source-zero trials also have zero lower envelope.
- **Conditional:** the nonnegative spectral representation and hence the coercivity barrier are asserted under RH, exactly as in WI-385/WI-386.
- **Not claimed:** an unconditional positivity result, a non-RH adaptive-family dichotomy, a new simple-zero proportion, or a barrier for unbounded-complexity/growing-width/nonlocal/domain-restricted trials.

## Consequence for the research program

A routine endpoint-by-endpoint retuning of the shape inside a fixed physical window is no longer a credible way around the WI-386 saturation mechanism if the retuned profiles have bounded Sobolev complexity. A viable continuation must use genuinely increasing profile complexity so that zeta-zero spectral mass is not uniformly tight, or must change the geometry of the trial (growing width, multiscale/nonlocal coupling, or domain restrictions). This is a decisive route-pruning result rather than a proportion improvement.