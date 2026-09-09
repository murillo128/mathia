# VIS-111 — growing-lag third-order correlation escapes every fixed block quotient

## Claim

For every integer `r>=2`, there are two binary words of the same length

`N_r = 4r+6`

with the same initial and terminal `r`-context and the same complete length-`(r+1)` block inventory, but different third-order correlation at lags proportional to `N_r`.

Let `u=0^r` and define three closed emitted walks from `u` back to `u` in the binary order-`r` overlap graph:

`A_r = 1 0^r`,

`B_r = 11 0^r`,

`D_r = 111 0^r`.

Form

`x_r = 0^r A_r B_r D_r`,

`y_r = 0^r A_r D_r B_r`.

Because `A_r`, `B_r`, and `D_r` are individually closed at the same state `0^r`, swapping the order of `B_r` and `D_r` changes only the Eulerian assembly of the same edge multiset. Therefore `x_r` and `y_r` have exactly the same multiset of length-`(r+1)` blocks and the same initial/terminal `r`-context. In the terminology of `VIS-099`, they lie in the same exact order-`r` Markov type.

Now use the third-order correlation

`C_z(k,l)=sum_(j=0)^(N_r-1-l) z_j z_(j+k) z_(j+l)`

for `0<k<l<N_r`. At the growing lags

`k_r=r+1`,

`l_r=2r+3`,

one has exactly

`C_(x_r)(k_r,l_r)=1`,

`C_(y_r)(k_r,l_r)=0`.

Since

`k_r/N_r -> 1/4`,

`l_r/N_r -> 1/2`,

the distinguishing lag scale grows linearly with the observation window. Consequently the statistic family

`T_r(z)=C_z(r+1,2r+3)`

**does not factor through any fixed finite block inventory uniformly in `r`**. For every fixed block length `L`, choosing `r>=L-1` gives a pair with identical length-`L` block counts but different `T_r`.

This supplies an exact positive information-admission complement to `VIS-110`: bounded-lag higher-order correlations are finite-block statistics, while a deliberately growing-lag third-order family can escape every fixed local-block quotient.

**Evidence/status:** `EXACT-DERIVED + POSITIVE INFORMATION-ADMISSION + CLASSICAL DE-BRUIJN/POLYSPECTRAL INGREDIENTS + NO-SOURCE-SPECIFICITY + NO-NOVELTY-CLAIM`.

No zeta/CUE difference, arithmetic anomaly, RH implication, optimal lag law, or claim that this particular sparse statistic is useful on Riemann-zero data is established.

## 1. Closed-walk exchange preserves the exact order-`r` type

Represent a binary word by the usual order-`r` overlap graph whose vertices are binary `r`-blocks and whose directed edges are binary `(r+1)`-blocks: appending one symbol shifts the current `r`-context and traverses the corresponding `(r+1)`-block edge.

Starting from `u=0^r`, each emitted word

`1^m 0^r`

with `m>=1` returns to `u`. Indeed, after the run of ones, the final `r` emitted zeros shift every one out of the state. Thus `A_r`, `B_r`, and `D_r` are closed walks based at the same vertex.

The word `x_r` traverses the concatenated walk

`A_r B_r D_r`,

while `y_r` traverses

`A_r D_r B_r`.

Each emitted symbol corresponds to one traversed edge, hence one length-`(r+1)` block occurrence. Concatenating closed walks in a different order preserves the complete edge multiset exactly. Both words begin at `0^r` and return to `0^r`, so their initial and terminal contexts also agree.

Therefore the two words have the same exact order-`r` Markov type. In particular, every bounded-lag cylinder statistic with maximum lag at most `r` is identical on the pair by `VIS-110`.

They also have identical block counts at every shorter length `L<=r+1`. This follows either by marginalizing the common `(r+1)`-block inventory and using the common boundary contexts, or directly from the exact order-`r` type.

## 2. The growing-lag third-order coefficient separates the assemblies

Index the words from zero. The one-positions of `x_r` are

`r`, `2r+1`, `2r+2`, `3r+3`, `3r+4`, `3r+5`.

The one-positions of `y_r` are

`r`, `2r+1`, `2r+2`, `2r+3`, `3r+4`, `3r+5`.

For `x_r`, the start `j=r` contributes

`x_r[r] x_r[2r+1] x_r[3r+3] = 1`.

No other admissible start contributes, so

`C_(x_r)(r+1,2r+3)=1`.

For `y_r`, the analogous start fails because

`y_r[3r+3]=0`.

Every other admissible start contains at least one zero, hence

`C_(y_r)(r+1,2r+3)=0`.

The separation is therefore exact and requires no asymptotics, probability model, numerical fit, or rendering.

The scale is genuinely growing rather than merely a larger fixed local order. Since `N_r=4r+6`,

`(r+1)/N_r -> 1/4`,

`(2r+3)/N_r = 1/2` exactly.

The second lag is always half the word length and the first approaches one quarter.

## 3. No fixed finite-block quotient determines this family

Fix any block length `L`. Choose `r>=max(2,L-1)`. The pair `x_r,y_r` has the same length-`(r+1)` block inventory and therefore the same length-`L` block inventory, while

`T_r(x_r)=1 != 0=T_r(y_r)`.

Thus there is no fixed `L` and no deterministic map from the length-`L` block inventory to `T_r` that works for all sufficiently large members of this family.

This is the exact distinction left open by `VIS-110`. A statistic can be third-order yet local when its lag span is uniformly bounded; the same algebraic moment order can become nonlocal relative to every fixed finite-memory quotient when its lag geometry scales with the observation window.

The result is an **information statement**, not a source statement. It proves that this growing-lag family can retain assembly information that all fixed local block inventories eventually forget. It does not say that Riemann-zero data occupy an unusual part of that information channel.

## 4. Prior art and novelty assessment

The graph language is classical. N. G. de Bruijn, **A combinatorial problem**, *Proceedings of the Section of Sciences of the Koninklijke Nederlandse Akademie van Wetenschappen te Amsterdam* 49:7 (1946), 758–764, is the foundational binary de Bruijn-sequence reference. T. van Aardenne-Ehrenfest and N. G. de Bruijn, **Circuits and trees in oriented linear graphs**, *Simon Stevin* 28 (1951), 203–217, gives the classical directed-Eulerian circuit framework. `VIS-094`, `VIS-099`, and `VIS-110` already connect Mathia's local-block inventories and exact Markov types to this overlap/Eulerian viewpoint.

The third-order spectral language is also classical. David R. Brillinger, **An Introduction to Polyspectra**, *Annals of Mathematical Statistics* 36:5 (1965), 1351–1374, DOI `10.1214/aoms/1177699896`, develops higher-order spectra/polyspectra for stationary time series. C. L. Nikias and M. R. Raghuveer, **Bispectrum estimation: A digital signal processing framework**, *Proceedings of the IEEE* 75:7 (1987), 869–891, DOI `10.1109/PROC.1987.13824`, is a standard bispectral reference already used at the `VIS-109`/`VIS-110` boundary.

A targeted search over de Bruijn/Eulerian sequence assembly, fixed block counts/Markov types, third-order correlation, and bispectral formulations found these standard ingredients rather than a separate theorem that needs a novelty claim here. The closed-walk exchange and displayed correlation witness are elementary consequences specialized to Mathia's current information-audit question. **No general combinatorics-on-words, Markov-type, or polyspectral novelty is claimed.**

## Boundary and falsification

The claim concerns a deliberately constructed family of binary words and one direction-sensitive third-order lag statistic. It proves only non-factorization through every **fixed** finite block length as the observation scale grows.

It does not establish that:

- every growing-lag statistic escapes fixed block information;
- the full bispectrum is the right carrier for zeta-zero chronology;
- a lag proportional to `N/4` or `N/2` is mathematically natural for Riemann zeros;
- quantized gap sequences preserve the relevant continuous information;
- the distinguishing effect survives a matched finite-size CUE control;
- any source-positive result would be independent of known finite-height zeta corrections;
- any such statistic yields a new RH criterion.

A stronger lower-information control is also possible: conditioning on block lengths that themselves grow with `N` can absorb this witness once the conditioned block length reaches the distinguishing lag span. The theorem rules out only **uniformly fixed** finite-memory explanations.

Falsify the exact claim by finding an `r>=2` for which the displayed words do not share the complete length-`(r+1)` block inventory or for which the displayed third-order correlations are not `1` and `0`. The closed-walk edge accounting and direct one-position calculation rule out either failure.

## Visual consequence

No canonical PNG is retained. This is a pre-render information-admission theorem. A future growing-lag bispectral or lag-domain visualization can now be designed around a carrier known **in principle** not to collapse to every fixed local block inventory, instead of using visual richness as evidence of nonlocality.

The theorem also supplies a simple synthetic control family for such a visualization: the two assemblies have identical exact local type through order `r` but a known difference at a macroscopic third-order lag pair.

## Research consequence

The accepted critical-strip multiscale clue can now move past the purely representational admission question for one concrete class. `VIS-110` gives the negative bounded-lag boundary; `VIS-111` gives an exact growing-lag escape from every fixed block quotient.

The next coherent question is therefore **source specificity**, not whether a growing-lag third-order carrier can in principle retain nonlocal assembly information. Before inspecting new zeta-zero material, a continuation should predeclare a scaling law, a low-dimensional statistic derived from growing lags or an equivalent bispectral functional, the lower-information conditioning, the confirmation windows, and the matched finite-size CUE/non-arithmetic control. A positive result would still require fresh replication and an audit against known finite-height arithmetic corrections.