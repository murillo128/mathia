# PF-272 — sublinear output windows restore a strict finite-seam exponent

**Status:** `EXACT-DERIVED + FIXED-SEAM-BLOCK-ASYMPTOTIC + SUBLINEAR-LOW-OUTPUT-LEAKAGE + FIRST-POLE-SHARPNESS + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-268-lowest-finite-seam-pole-forbids-bare-supercritical-separated-weighting|PF-268]] proves that at every fixed finite seam scale the naked relative seam has a proportional high-high block of order `N^{-1}` in operator norm, so a bare input weight `R>1` is impossible. [[research/prime_flute/findings/PF-271-separated-propagation-only-needs-sublinear-low-output-leakage|PF-271]] shows, however, that later positive separation does not consume a proportional-block estimate: it only needs decay from input scale `N` into an output window growing strictly sublinearly in `N` (or logarithmically when the remaining propagator is exactly exponential).

The fixed-axis Green results now determine that missing geometry sharply. For fixed `r,s>0`, put

\[
a_0=\frac{\pi}{2rs},
\qquad
\mu_0=\sqrt{1+a_0^2}>1.
\tag{1}
\]

Inside either parity chain, let `E_N` project onto indices `N\le j<2N` and let `F_{N,\theta}` project onto `0\le i\le N^\theta`, `0<\theta<1`. Then the exact fixed-axis relative seam from PF-261 satisfies

\[
\boxed{
\|F_{N,\theta}\,\mathcal R_{s,r}^0\,E_N\|
\asymp_{r,s,\theta}
N^{-\alpha_s(\theta)},
\qquad
\alpha_s(\theta)
=\mu_0(1-\theta)+\frac{1+\theta}{2}.
}
\tag{2}
\]

In particular

\[
\boxed{
\alpha_s(\theta)-1
=(1-\theta)\left(\mu_0-\frac12\right)>0
\qquad(0<\theta<1).
}
\tag{3}
\]

Thus the same lowest pole that is exactly critical on proportional blocks becomes **strictly supercritical as soon as the output window is sublinear**. For every fixed `s>0` and every `\theta<1`, there are `R>1` and `\varepsilon>0` with

\[
\|F_{N,\theta}\mathcal R_{s,r}^0E_N\|
\lesssim N^{-R-\varepsilon},
\tag{4}
\]

which is precisely the type of low-output leakage consumed by PF-271 before the nonlinear Robin/reflection factors are inserted.

For a logarithmic window `M_N=A\log N`, the same argument gives the sharper two-sided scale

\[
\boxed{
\|F_{M_N}\mathcal R_{s,r}^0E_N\|
\asymp_{r,s,A}
N^{-\mu_0-1/2}(\log N)^{\mu_0-1/2}.
}
\tag{5}
\]

Consequently every exponent `R<\mu_0+1/2` can be paid, with positive room, in the logarithmic PF-271 leakage test at fixed seam scale.

This does **not** close the PF-243 Robin--Poisson gate. Equation (2) is for the naked fixed-axis relative seam `\mathcal R_{s,r}^0`, while the physical pre-separation conversion also contains the square-root source factor `X(I+X^*X)^{-1}`, Robin reflections, transports, density/congruence corrections, and eventually the sheared/variable corridor. The new conclusion is narrower and useful: **the finite-seam positive Green mixture itself is not a deep-low-output obstruction at fixed `s`; the remaining obstruction must be created by the nonlinear conversion/transport or by failure of uniformity in the parameters needed by the actual corridor.**

## Claim

Fix `r,s>0` and a parity `\varepsilon\in\{0,1\}`. Write `f_j=e_{2j+\varepsilon}` for the parity basis and let

\[
E_N^{(\varepsilon)}
=\sum_{N\le j<2N}|f_j\rangle\langle f_j|,
\qquad
F_M^{(\varepsilon)}
=\sum_{0\le i\le M}|f_i\rangle\langle f_i|.
\tag{6}
\]

Let `\mathcal R_{s,r}^{0,\varepsilon}` denote the parity restriction of the fixed-axis relative seam from PF-261. Then:

1. for every `0<\theta<1`, with `\alpha_s(\theta)` as in (2), there are constants `0<c<C<\infty` and `N_0` depending only on `r,s,\theta,\varepsilon` such that
   \[
   cN^{-\alpha_s(\theta)}
   \le
   \|F_{N^\theta}^{(\varepsilon)}\mathcal R_{s,r}^{0,\varepsilon}E_N^{(\varepsilon)}\|
   \le
   CN^{-\alpha_s(\theta)}
   \qquad(N\ge N_0);
   \tag{7}
   \]
2. for every fixed `A>0`,
   \[
   \|F_{A\log N}^{(\varepsilon)}\mathcal R_{s,r}^{0,\varepsilon}E_N^{(\varepsilon)}\|
   \asymp
   N^{-\mu_0-1/2}(\log N)^{\mu_0-1/2};
   \tag{8}
   \]
3. opposite parity blocks vanish, so the same exponents hold for the full fixed-axis seam after combining the two parity sectors;
4. replacing parity index by the fixed-axis transverse scale `K_s^0=sA^{1/2}` changes only constants because, at fixed `s`, its eigenvalues are comparable to `s(j+1)` on each parity block;
5. the exponent in (7) tends to the PF-268 critical value `1` as `\theta\uparrow1`, while every strict sublinear window has positive supercritical room.

No uniformity in `s`, shear parameter, corridor index, or Robin homotopy parameter is asserted.

## 1. The lowest pole fixes the sublinear block scale from below

PF-261 gives, for distinct same-parity modes,

\[
\langle f_i,\mathcal R_{s,r}^{0,\varepsilon}f_j\rangle
=-\frac{2}{rs^2\sqrt{\kappa_i\kappa_j}}
\sum_{k\ge0}a_k^2G_{ij}^{(\varepsilon)}(a_k),
\qquad
a_k=\frac{(2k+1)\pi}{2rs},
\tag{9}
\]

where every Green entry is positive. Hence there is no cancellation between mass poles. PF-264 proves for the first fixed mass, uniformly once both indices are in its asymptotic tail,

\[
G_{ij}^{(\varepsilon)}(a_0)
\asymp
 i^{-1/2+\mu_0}j^{-1/2-\mu_0},
\qquad i\le j,
\tag{10}
\]

and `\kappa_{2j+\varepsilon}\asymp j+1`. Therefore on the rectangle

\[
\frac12N^\theta\le i\le N^\theta,
\qquad
N\le j<2N,
\tag{11}
\]

all sufficiently large entries have the same sign and satisfy

\[
|\langle f_i,\mathcal R_{s,r}^{0,\varepsilon}f_j\rangle|
\gtrsim
i^{\mu_0-1}j^{-\mu_0-1}.
\tag{12}
\]

Apply the block to the normalized constant vector on the input shell. There are `\asymp N` input indices and `\asymp N^\theta` output indices in (11), so (12) gives

\[
\|F_{N^\theta}\mathcal R_{s,r}^0E_N\|
\gtrsim
N^{-\mu_0-1/2}
(N^\theta)^{\mu_0-1/2}
=N^{-\alpha_s(\theta)}.
\tag{13}
\]

The same calculation with an output block of length `\asymp\log N` proves the lower half of (8).

This is the exact analogue of PF-268's proportional-block witness, but with the output scale allowed to fall below the input scale. The exponent changes continuously from the critical `1` at `M\asymp N` to `\mu_0+1/2` at bounded/logarithmic output.

## 2. Every fixed low mass has the same or faster upper exponent

Choose a finite mass threshold `B>\mu_0`. There are only finitely many odd masses with `\mu_k\le B`. For each such fixed mass, PF-264 gives the moving-source upper asymptotic

\[
G_{ij}^{(\varepsilon)}(a_k)
\lesssim_{r,s,B}
 i^{-1/2+\mu_k}j^{-1/2-\mu_k}
\tag{14}
\]

once `i,j` are large. The finitely many rows below that asymptotic range are covered by PF-262's fixed-source Green tail, after enlarging the constant. Thus the corresponding relative-seam summand obeys on `i<j`

\[
|R_{ij}^{(k)}|
\lesssim_{r,s,B}
(i+1)^{\mu_k-1}(j+1)^{-\mu_k-1}.
\tag{15}
\]

Hilbert--Schmidt summation on `i\le N^\theta`, `N\le j<2N` gives

\[
\begin{aligned}
\|F_{N^\theta}R^{(k)}E_N\|
&\le \|F_{N^\theta}R^{(k)}E_N\|_{\mathcal S_2}\\
&\lesssim
(N^\theta)^{\mu_k-1/2}N^{-\mu_k-1/2}\\
&=N^{-\alpha_k(\theta)},
\end{aligned}
\tag{16}
\]

where

\[
\alpha_k(\theta)
=\mu_k(1-\theta)+\frac{1+\theta}{2}.
\tag{17}
\]

Because `\mu_k` increases with `k` and `\theta<1`, the slowest exponent is exactly `\alpha_0(\theta)=\alpha_s(\theta)`. Summing the finite low-mass family preserves the upper scale in (7). For `M=A\log N`, the same Hilbert--Schmidt computation gives

\[
\|F_MR^{(k)}E_N\|
\lesssim
N^{-\mu_k-1/2}M^{\mu_k-1/2},
\tag{18}
\]

again with the first pole slowest.

## 3. The remaining mass ladder can be pushed below any prescribed power

It remains to justify that the infinitely many higher poles cannot replace the first-pole exponent by a slower block scale. This is exactly where PF-265 and PF-267 supply the missing uniformity.

PF-267 gives, uniformly in mass and parity,

\[
G_{ij}^{(\varepsilon)}(a)
\lesssim
\frac{1}{\mu\sqrt{(i+1+\mu)(j+1+\mu)}}
\exp[-c\Psi_{ij}(\mu)],
\tag{19}
\]

with

\[
\Psi_{ij}(\mu)
=\sum_{m=i}^{j-1}\min\left(1,\frac{\mu}{m+1}\right).
\tag{20}
\]

After multiplying by `a^2` and PF-261's endpoint weights, the scalar prefactor in (19) is at most a constant times `(ij)^{-1/2}`. For `i\le N^\theta`, `j\asymp N`, monotonicity in `\mu` gives, for every fixed `B` and all `\mu\ge B`,

\[
\Psi_{ij}(\mu)
\ge \Psi_{ij}(B)
\ge B(1-\theta)\log N-O_B(1).
\tag{21}
\]

There are only `O_{r,s}(N)` odd masses with `B\le\mu_k\le C N`. Hence their complete contribution has Hilbert--Schmidt norm

\[
O_{r,s,B}\!\left(
N^{1-cB(1-\theta)}\sqrt{\log N}
\right).
\tag{22}
\]

By choosing the fixed threshold `B` large enough, (22) is smaller than any prescribed power, in particular smaller than `N^{-\alpha_s(\theta)}`.

For the remaining region `\mu_k\ge CN`, choose `C` beyond the large-mass threshold in PF-267. Its path-correlation refinement gives

\[
\frac{G_{ij}}{\sqrt{G_{ii}G_{jj}}}
\le
\left(\frac{C_1(j+1)^2}{\mu_k^2}\right)^{j-i}.
\tag{23}
\]

Taking `C` larger if necessary makes the parenthesis uniformly smaller than one, while `j-i\ge N-N^\theta\asymp N`. PF-266's diagonal amplitude then makes the infinite mass tail absolutely summable, and its total block norm is exponentially small in `N`. This completes the upper bound in (7). Replacing `N^\theta` by `A\log N` only increases the path separation and gives the upper half of (8).

The proof deliberately splits **mass before operator norm**. It does not commit the invalid interchange warned against in PF-261: the low-mass part is finite, and the infinite tail is controlled by the uniform PF-265/PF-267 estimates before summation.

## 4. The proportional obstruction and the PF-271 window are the same exponent at different aspect ratios

Equation (2) makes the PF-268/PF-271 relationship quantitative. If the output dimension scales like `M=N^\theta`, the first-pole block exponent is

\[
\alpha_s(\theta)
=1+(1-\theta)\left(\mu_0-\frac12\right).
\tag{24}
\]

At the proportional boundary `\theta=1`, the gain vanishes and `\alpha_s(1)=1`, exactly the operator-norm scale behind PF-268's no-go for every bare weight `R>1`. But the PF-271 dangerous cone has `\theta<1`; every such cone opens a strict margin.

Therefore PF-268 is not merely *compatible* with PF-271. The same first pole that proves the former also proves, after changing the aspect ratio of the block, the sharp positive leakage exponent needed by the latter for the **raw fixed-axis seam**.

The logarithmic limit is even cleaner. Since `M=A\log N=N^{o(1)}`, the polynomial part of the first-pole exponent reaches `\mu_0+1/2`, leaving only the explicit logarithmic factor in (5). Any target `R<\mu_0+1/2` can absorb that factor with a positive polynomial remainder.

## 5. Representation and transport boundary

The estimates above are first proved in PF-247's parity index, where `L` is Jacobi and the PF-261 Green expansion is exact. At fixed `s`, the physical fixed-axis scale `K_s^0=sA^{1/2}` is diagonal in the same Gegenbauer basis and its parity eigenvalues are comparable to `s(j+1)`. Passing from index shells to `K_s^0` spectral shells therefore changes only fixed constants and not the exponents in (2) or (5).

This statement must **not** be transported silently to the actual corridor scale `K_a`, to a sheared basis, or through a Robin square-root factor. PF-255/PF-256 provide controlled coordinate/graph transports, but the complete PF-243 pre-separation conversion has more structure than `\mathcal R_{s,r}^0`. The present result is evidence only for the fixed-axis relative-seam component.

## 6. Prior art and novelty audit

No new abstract Jacobi or matrix-localization theorem is claimed. PF-264's fixed-mass Wronskian asymptotic is built from classical Jacobi Green theory and Birkhoff--Adams asymptotics; PF-265 imports the unbounded-gap Green estimates of Janas, Naboko, and Silva; PF-267 supplies the path-capacity correlation product. A fresh targeted audit again found the expected general Green-matrix decay literature, including Janas--Naboko--Silva's 2018 unbounded-gap theorem and the broader classical localized-matrix theory represented by Jaffard. None states this Prime-Flute block consequence because the exponent (24) uses the specific PF-261 odd-pole decomposition, PF-264 first-pole law, and PF endpoint normalization.

The project-specific delta is the two-sided **aspect-ratio law** (2): it turns the PF-268 lowest-pole obstruction into a positive theorem on exactly the smaller output sector isolated by PF-271. No novelty is claimed for Hilbert--Schmidt domination, dyadic/spectral block decompositions, Combes--Thomas estimates, or the underlying Jacobi asymptotics.

No new source entry is required because all external ingredients used in the proof are already audited and persisted in PF-264--PF-267 and PF-271.

## 7. Boundaries and adversarial checks

1. **Fixed seam only.** Constants in (7)--(8) may depend badly on `s`; no uniform `s\downarrow0`, corridor-index, or Robin-homotopy estimate is proved.
2. **Raw relative seam only.** The theorem does not say that `X(I+X^*X)^{-1}`, Robin reflections, or their products preserve the same low-output exponent.
3. **Fixed-axis basis only.** Transfer to the actual `K_a` scale must use the established geometric transports without identifying distinct spectral projections by analogy.
4. **Strictly sublinear window.** The proof gains a strict exponent only for `\theta<1`; the limit `\theta=1` is critical and agrees with PF-268 rather than contradicting it.
5. **No cancellation is used.** Positivity of every massive Green term supplies the lower bound; the upper bound controls the complete positive ladder. A hidden sign cancellation cannot be responsible for the gain.
6. **Finite low rows are included.** PF-264 handles moving tail rows, while PF-262 handles the finitely many rows below the moving-source asymptotic range. Omitting those rows would not justify the operator block statement.
7. **No hidden mass-limit interchange.** Only finitely many masses use fixed-mass asymptotics. The infinite remainder is bounded with PF-265/PF-267 uniformly before summing.
8. **No endpoint claim.** Equation (4) uses `R+\varepsilon<\alpha_s(\theta)`; boundedness at the exact exponent `R=\alpha_s(\theta)` is not inferred from PF-271.
9. **No global consequence.** Nothing here closes the sheared PF-243 estimate, weak trace reassembly, finite-pant completion, scattering/determinants, prime/control separation, zeta-zero statements, or RH.

## Decisive next test

Insert the **actual fixed-axis normalized Robin source factor and reflection factors** around the relative seam and repeat the PF-271 low-output block test before any variable-corridor/shear transfer. The raw seam now has the required strict sublinear leakage at each fixed `s`; the next discriminator is whether the nonlinear square-root/rational conversion preserves a comparable exponent or creates a new deep high-to-low channel.

If that fixed-axis combined conversion passes, the remaining hard requirement is parameter-uniform transport to the PF-243 family: constants and a common `R>1` must survive the canonical tail, the actual `K_a` scale, all pre-separation reflections/congruences, and `0\le t\le1`. If it fails, a meaningful negative must exhibit deep low-output leakage generated by the **combined** conversion, not merely re-use PF-268's proportional `N^{-2}` entry floor.