# MI-063 — Demodulation turns selected Ford energy into a window-bandlimited moving-center observable

**Evidence level:** exact harmonic-analysis synthesis from [NB-246](../../findings/NB-246-demodulation-bandlimits-ford-pair-energy-to-the-window-scale.md), interpreted against NB-243 and NB-245. The local-mean condition below is sufficient, not known to hold for zeta zeros.

Freeze the Ford parameters at a selected center `t_0` and retain the full smooth shell current while allowing only the observation center `t` to move. The apparent carrier frequency `X` is common to every summand. Multiplying by `e^{iXt}` removes it exactly, leaving center frequencies `Hu` with `u` in the fixed support of the shell profile. The demodulated current is therefore band-limited at scale `H`, and its squared magnitude has center-frequency support of width `O(H)`.

This does **not** coarsen the zero geometry to scale `1/H`. When the energy is expanded into zero pairs, the factor `e^{iX(gamma_j-gamma_k)}` remains, so ordinate differences at scale `1/X` are still resolved and the Ford depth marks remain in the coefficients. What changes is only how fast the already-formed smooth energy can vary as the observation center moves.

A reproducing kernel for the `O(H)` bandlimit gives an exact useful implication: the pointwise selected energy is bounded by a rapidly weighted local `L^2` mean of the same frozen current on center scale `1/H`. Thus one need not prove an estimate at one exact selected height if one can prove the corresponding local mean **uniformly around every possible selected center**.

The quantifier is load-bearing. A macroscopic height average or random-height convergence can still miss sparse exceptional windows, as NB-245 warns. The NB-246 average is shrinking, source-matched and uniform in the center. Likewise, replacing the smooth shell by a hard moving cutoff destroys compact frequency support and forfeits the implication.

**Boundary.** NB-246 supplies the harmonic reduction only. It does not prove the required uniform local second moment from known pair-correlation theorems, and current short-interval results do not contain the depth-marked Ford statistic at this shrinking scale.
