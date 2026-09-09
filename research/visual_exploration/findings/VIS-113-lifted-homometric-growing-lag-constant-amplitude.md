# VIS-113 — a lifted homometric witness keeps constant growing-lag third-order amplitude

## Claim

For every integer `r>=1`, there are two binary words of the same length

`N_r = 29r`

that simultaneously have:

- the same initial and terminal `r`-context;
- the same complete length-`(r+1)` block inventory, hence the same exact order-`r` Markov type;
- the same complete aperiodic autocorrelation and therefore the same Fourier magnitude at every frequency;
- a different third-order correlation at lags proportional to the observation length;
- an **exact nonvanishing empirical-average separation** at those lags.

Start from the Fourier-homometric macro pair of `VIS-108`,

`a = 01000111001011`,

`b = 01001011100011`.

`VIS-108` proves that `a` and `b` have the same complete Fourier magnitude, and `VIS-109` proves

`C_a(1,4)=1`, `C_b(1,4)=0`,

for

`C_z(k,l)=sum_j z_j z_(j+k) z_(j+l)`.

For each `r`, define two length-`2r` emitted blocks

`E_r = 1^r 0^r`,

`Z_r = 0^(2r)`.

Both return the order-`r` overlap state `0^r` to itself. Replace every macro symbol `1` by `E_r` and every macro symbol `0` by `Z_r`, and prepend the common initial context `0^r`. Call the resulting words `x_r` and `y_r`.

Then with

`k_r=2r`, `l_r=8r`,

one has exactly

`C_(x_r)(k_r,l_r)=r`,

`C_(y_r)(k_r,l_r)=0`.

Because `N_r-l_r=21r`, the admissible-start empirical averages satisfy

`A_(x_r)(k_r,l_r)-A_(y_r)(k_r,l_r)=1/21`,

where `A_z(k,l)=C_z(k,l)/(N-l)`.

Moreover

`k_r/N_r=2/29`, `l_r/N_r=8/29`

for every `r`. Thus the distinguishing lags remain macroscopic while the normalized separation remains exactly constant.

Consequently there exists a growing-lag third-order family that escapes every uniformly fixed finite-block quotient **without** the empirical-average dilution exhibited by the sparse `VIS-111` witness, and the separation cannot be attributed to ordinary Fourier magnitude or two-point autocorrelation because those are exactly identical on the pair.

**Evidence/status:** `EXACT-DERIVED + POSITIVE INFORMATION-AND-AMPLITUDE WITNESS + FOURIER-HOMOMETRIC CONTROL + CLASSICAL DE-BRUIJN/PHASE-RETRIEVAL/POLYSPECTRAL INGREDIENTS + NO-SOURCE-SPECIFICITY + NO-NOVELTY-CLAIM`.

No zeta/CUE difference, natural zeta lag law, null-variance theorem, arithmetic anomaly, or RH implication is established.

## 1. Closed-block lifting preserves the exact order-`r` type

Use the binary order-`r` overlap graph with state `u=0^r`. Emitting either `E_r=1^r0^r` or `Z_r=0^(2r)` from `u` ends with `r` zeros and therefore returns to `u`. Each block is a closed walk based at the same state.

The macro words `a` and `b` each contain seven ones and seven zeros. Hence `x_r` and `y_r` each traverse exactly seven copies of the closed walk `E_r` and seven copies of the closed walk `Z_r`; only the assembly order differs.

Every emitted symbol traverses one edge of the order-`r` overlap graph, equivalently one occurrence of a length-`(r+1)` block. Reordering closed walks based at the same state preserves the total edge multiset exactly. The common prepended context is `0^r`, and every lifted word ends at the same state `0^r`.

Therefore `x_r` and `y_r` have the same complete length-`(r+1)` block inventory and the same initial/terminal `r`-contexts. They lie in one exact order-`r` Markov type.

In particular, for every fixed block length `L`, choosing `r>=L-1` makes all length-`L` block counts identical on the pair.

## 2. Fourier homometry survives the lift exactly

Let

`A(z)=sum_(q=0)^13 a_q z^q`,

`B(z)=sum_(q=0)^13 b_q z^q`.

`VIS-108` proves the exact Laurent identity

`A(z)A(z^(-1))=B(z)B(z^(-1))`,

so the macro words have equal Fourier magnitude on the unit circle.

Let

`U_r(z)=1+z+...+z^(r-1)`.

Because a macro `1` contributes a run of `r` ones at the start of its length-`2r` block and a macro `0` contributes no ones, the lifted generating polynomials are

`X_r(z)=z^r U_r(z) A(z^(2r))`,

`Y_r(z)=z^r U_r(z) B(z^(2r))`.

For `|z|=1`, the prefactor is common and `z^(2r)` remains on the unit circle. Hence

`|X_r(z)|=|Y_r(z)|`

for every `|z|=1`. Equivalently the complete aperiodic autocorrelation vectors of `x_r` and `y_r` are identical.

Thus the later third-order separation is not lower-order leakage through an ordinary power spectrum.

## 3. The macroscopic third-order coefficient has extensive raw separation

The lifted words consist of the common initial `r` zeros followed by fourteen macro blocks of length `2r`. Therefore

`N_r=r+14(2r)=29r`.

Take lags

`k_r=2r`, `l_r=8r=4(2r)`.

Every start inside the initial prefix contributes zero. For a start in macro block `q` at offset `t` with `0<=t<r`, the three sampled bits are exactly

`a_q`, `a_(q+1)`, `a_(q+4)`

for `x_r`, and the corresponding `b` bits for `y_r`. Starts with `r<=t<2r` lie in the trailing-zero half of the emitted block and contribute zero.

Summing over the `r` active offsets therefore gives

`C_(x_r)(2r,8r)=r C_a(1,4)=r`,

`C_(y_r)(2r,8r)=r C_b(1,4)=0`.

The raw distinguishing count is now `Theta(r)=Theta(N_r)`, not `O(1)` as in `VIS-111`.

The number of admissible starts is

`N_r-l_r=29r-8r=21r`,

so the empirical averages differ by exactly

`r/(21r)=1/21`.

This is a scale-stable normalized effect on the synthetic witness. No asymptotic approximation is used.

## 4. This removes the dilution as a necessary obstruction

`VIS-111` established that growing-lag third-order correlation can escape every fixed finite-block quotient. `VIS-112` then showed that its particular sparse witness has only one separating triple, so its natural empirical-average contrast shrinks as `2/N`.

The present construction proves that this dilution is **witness-specific rather than forced by the information boundary**. For any fixed block length `L`, take `r>=L-1`. The pair still has identical length-`L` block inventories and identical complete two-point autocorrelation, while its growing-lag empirical third-order statistic differs by `1/21` at the fixed macroscopic lag fractions `2/29` and `8/29`.

The three gates remain conceptually distinct:

- fixed-block information admission can hold;
- a chosen normalization can retain `O(1)` synthetic amplitude;
- source specificity can still fail completely.

Only the first two are witnessed here. Nothing in the construction says that Riemann-zero data should choose these lag fractions, this quantization, or this statistic.

## 5. Prior art and novelty assessment

The ingredients are classical. De Bruijn overlap graphs and Eulerian-circuit assembly are standard combinatorics-on-words machinery; `VIS-111` already records N. G. de Bruijn, **A combinatorial problem** (1946), and T. van Aardenne-Ehrenfest and N. G. de Bruijn, **Circuits and trees in oriented linear graphs** (1951), as the relevant historical boundary.

One-dimensional Fourier-magnitude ambiguity and reciprocal-factor homometry are classical phase-retrieval phenomena; `VIS-108` records the relevant Hayes--Lim--Oppenheim, Beinert--Plonka, and Edidin references. Third-order correlation and bispectral/polyspectral language are likewise classical; `VIS-109`--`VIS-112` record Brillinger and Nikias--Raghuveer.

A targeted literature check found the standard Eulerian/de Bruijn and phase-retrieval frameworks rather than a reason to claim a new general theorem for this block lift. The displayed construction is an elementary Mathia-specific composition of the already-audited homometric macro witness with closed overlap-graph blocks. **No novelty is claimed for block substitution, homometry, Eulerian assembly, third-order correlation, or bispectral normalization.**

## Boundary and falsification

The finding is a synthetic existence result. It proves that fixed-local equivalence, complete two-point homometry, macroscopic lag scale, and constant empirical third-order separation can coexist.

It does **not** establish that:

- every exact Markov type contains such a pair;
- the fractions `2/29` and `8/29` are natural for zeta zeros;
- the statistic remains nontrivial after conditioning on a block length that itself grows comparably with `N`;
- centered third-order cumulants, bicoherence, or another normalization behave identically;
- a finite-size CUE null has any particular fluctuation scale for the corresponding source statistic;
- zeta differs from CUE or another non-arithmetic source;
- quantization preserves the source information needed by RH;
- any higher-order spectral statistic yields an RH criterion.

Falsify the exact claim by finding an `r>=1` for which the lifted pair does not share its length-`(r+1)` block inventory, does not have equal complete autocorrelation, or does not satisfy the displayed correlation/average identities. The closed-walk edge decomposition, generating-polynomial factorization, and direct macro-offset sum establish all three identities exactly.

## Visual consequence

No canonical PNG is retained. A power-spectrum visualization of the pair would be exactly coincident and would hide the known distinction, while a lag-domain third-order plot would show a separation whose normalized height does not shrink with `r` at the displayed macroscopic coordinate. The exact algebra is more informative than a rendering for this gate.

## Research consequence

The accepted critical-strip multiscale clue no longer needs a stronger synthetic witness merely to show that nonlocal information and nonvanishing empirical amplitude can coexist after exact fixed-block and complete two-point controls. `VIS-113` supplies that witness.

The remaining hard step is **source specificity under a predeclared source statistic and matched null**. A future zeta/CUE experiment still has to motivate its lag law and normalization independently, freeze them before confirmation data, account for the exact lower-information quotient, calibrate finite-size null fluctuations, and replicate any residual on untouched material. The synthetic `1/21` separation is an admissibility certificate, not evidence that zeta occupies an unusual part of this channel.