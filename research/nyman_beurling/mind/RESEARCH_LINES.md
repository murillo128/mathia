# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Prove a uniform Ford-scale local second-moment bound with the depth marks and carrier phase intact

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`.

NB-245 corrects the inverse-problem interpretation. For each fixed finite carrier law, the exact unnormalized Cauchy/Stieltjes transform determines every coefficient by its poles and residues; the issue is not algebraic nonuniqueness. Bounded normalized interior probes can nevertheless become arbitrarily insensitive to a top depth-marked block as the strip grows, so exact recovery does not give a uniform observable.

NB-246 identifies a strictly weaker sufficient target than pointwise control at every selected height. Freeze the Ford parameters at a target center, retain the full smooth shell current, and demodulate its common carrier `e^{-iXt}`. The moving-center current then has Fourier bandwidth `O(H)`, and its energy is also band-limited at `O(H)`. A reproducing-kernel estimate therefore bounds the selected-height energy by a weighted local `L^2` mean on center scale `1/H`.

The live source theorem is consequently quantitative and local: prove that this Ford-scale weighted second moment is `o(1)` uniformly over every admissible selected center, with the horizontal depth marks and the original `e^{iX(gamma_j-gamma_k)}` pair phase retained. This does not reduce the zero-resolution scale from `1/X`; it only shows that a bad selected current cannot be isolated on a center scale much shorter than `1/H`.

## Keep exact reconstruction, macroscopic averaging and source-faithful local averaging separate

A long-height average or random-height law can miss sparse bad Ford blocks and remains insufficient. The `1/H` local mean of NB-246 is different: it follows from the exact bandlimit of the frozen smooth shell and must hold uniformly around every candidate selected height. Hard moving cutoffs destroy that bandlimit. Any averaging theorem used here must therefore match the smooth source window, its depth marking, its frozen parameters and the required uniform center quantifier.
