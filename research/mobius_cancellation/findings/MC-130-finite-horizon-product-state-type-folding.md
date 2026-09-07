# MC-130 — Finite-horizon product-state path types fold into longer one-step types

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISMS`, `NO-NOVELTY-CLAIM`.

## Claim

The joint product-state obstruction in `MC-129` already covers a substantially larger class than one-step observables. Any empirical finite-horizon path type of a smaller local-memory/modular state is exactly a one-step product-state type after enlarging the local context by the horizon.

Fix integers

\[
k_0,h,q\ge 1,
\qquad
K=k_0+h-1\ge 2.
\tag{1}
\]

For a bounded-increment word `Z=(z_1,\ldots,z_N)` with `z_j in {+1,-1}`, write

\[
S_Z(j)=\sum_{i\le j}z_i,
\]

and let `C_Z^{(k_0)}(j-1)` denote the preceding `k_0-1` increments before step `j`. For one of the coarse bins used in `MC-129`, define the terminal-binned `h`-step product-state path tensor

\[
H_{Z,t}^{(k_0,h)}(u,a;\varepsilon_1,\ldots,\varepsilon_h)
\]

to be the number of starting positions `j` for which

\[
C_Z^{(k_0)}(j-1)=u,
\qquad
S_Z(j-1)\equiv a\pmod q,
\qquad
(z_j,\ldots,z_{j+h-1})=(\varepsilon_1,\ldots,\varepsilon_h),
\tag{2}
\]

and whose terminal step `j+h-1` lies in bin `t`.

Now instantiate the `MC-129` construction with local parameter `k=K`, the same modulus `q`, and arbitrary admissible repetition/bin parameters `r,b`. Let `J_{Z,t}^{(K)}` be its one-step joint tensor coupling the preceding `K-1` symbols, the partial sum modulo `q`, and the next increment. Then for every admissible tuple in `(2)`,

\[
\boxed{
H_{Z,t}^{(k_0,h)}(u,a;\varepsilon_1,\ldots,\varepsilon_h)
=
J_{Z,t}^{(K)}
\left(
 u\varepsilon_1\cdots\varepsilon_{h-1},
 a+\sum_{i=1}^{h-1}\varepsilon_i,
 \varepsilon_h
\right),
}
\tag{3}
\]

where the second argument is read modulo `q`.

The map in `(3)` is bijective: from the enlarged context and terminal residue one recovers the initial context `u`, the first `h-1` increments, and

\[
a\equiv
\left(a+\sum_{i<h}\varepsilon_i\right)
-
\sum_{i<h}\varepsilon_i
\pmod q.
\tag{4}
\]

Therefore the two words `U,W` supplied by `MC-129` with parameter `K` satisfy, in every corresponding bin,

\[
\boxed{
H_{U,t}^{(k_0,h)}=H_{W,t}^{(k_0,h)}
}
\tag{5}

for the complete `h`-step path type. This includes the empirical count of every finite trajectory of the coupled state consisting of local context, additive residue, and increments. Every scalar statistic that factors through this empirical `h`-step path histogram is consequently identical for `U` and `W`.

Nevertheless their mean-absolute excursions remain those of `MC-129` with `k=K`. In particular, set

\[
K=R^{\kappa+o(1)},
\qquad
q=R^{\beta+o(1)},
\qquad
b=R^{\gamma+o(1)},
\qquad
\ell=\max(\kappa,\beta),
\tag{6}
\]

and choose

\[
r=R^{1-\kappa-\ell-\gamma+o(1)}.
\tag{7}
\]

Whenever

\[
\ell<\frac12,
\qquad
\kappa+\gamma<\frac12,
\tag{8}
\]

`MC-129` gives `N=R^(1+o(1))` together with

\[
D_1(U)=N^{1-\kappa-\gamma+o(1)}
      =N^{1/2+\Omega(1)},
\tag{9}
\]

and

\[
D_1(W)=N^{\ell+o(1)}
      =N^{1/2-\Omega(1)}.
\tag{10}
\]

Thus **complete finite-horizon empirical product-state path information remains excursion-blind whenever its effective context length**

\[
K=k_0+h-1
\tag{11}
\]

and the time/modular resolutions stay in the explicit sub-square-root regime `(8)`.

This is a representation-level matched-control obstruction, not an arithmetic counterexample. The words are not claimed to satisfy Möbius multiplicativity, the actual square-free support pattern, prime values, or divisor relations.

## 1. Exact folding of a path into one enlarged transition

Let the terminal index be

\[
n=j+h-1.
\]

The preceding `K-1` symbols before `n` begin at

\[
n-K+1
=j+h-1-(k_0+h-1)+1
=j-k_0+1.
\tag{12}
\]

They are therefore exactly

\[
C_Z^{(K)}(n-1)
=
C_Z^{(k_0)}(j-1)\,
\varepsilon_1\cdots\varepsilon_{h-1}.
\tag{13}
\]

Likewise the additive state just before the terminal step is

\[
S_Z(n-1)
=
S_Z(j-1)+\sum_{i=1}^{h-1}\varepsilon_i.
\tag{14}
\]

The terminal increment is `epsilon_h`. Equations `(13)` and `(14)` prove `(3)` pointwise and hence the equality of the full empirical tensors after summation.

Nothing probabilistic or asymptotic enters this reduction. It is simply the deterministic fact that an `h`-step finite-state trajectory can be represented as one transition after adjoining the preceding `h-1` symbols to the state. In particular, all intermediate modular residues and shorter local contexts along the path are functions of the tuple in `(2)`, so matching `H` also matches the empirical distribution of the complete coupled trajectory, not merely the increment block.

## 2. Bin-boundary conventions do not create an escape

The terminal-binned definition is exact without discarding boundary paths: an `h`-step segment is assigned to the bin containing its terminal step. `MC-129` already matches the enlarged one-step tensor in every such bin, including the states reached from the common bin-boundary product state.

If instead one insists that both the starting and terminal steps lie in the same bin, remove the first `h-1` terminal positions of each bin. This does not break equality for the `MC-129` controls. With construction parameter `K`, each bin begins from the same context `+^(K-1)` and the same lifted height, while both words begin the bin with the common positive macro-cycle `P=+^L`. Since `L>=K>=h`, the removed first `h-1` terminal events agree pointwise. Thus the wholly-contained `h`-step path types are also identical.

The obstruction is therefore not an artifact of assigning cross-boundary windows to one bin or the other.

## 3. Higher-order Markov types are not a new information class here

The classical method-of-types language already treats higher-order empirical dependence by increasing the context. Neri Merhav, Michael Gutman and Jacob Ziv, *On the Estimation of the Order of a Markov Chain and Universal Data Compression*, IEEE Transactions on Information Theory 35 (1989), no. 5, 1014–1019, DOI `10.1109/18.42210`, defines the `k`-th order Markov type of a word as the empirical matrix counting the current symbol jointly with its preceding `k`-symbol state.

That established representation is precisely the abstract operation used in `(3)`: a finite block/path statistic becomes an ordinary one-step type on a longer context. `MC-S41` gives the adjacent first-order Markov-type language in terms of balanced transition counts and directed multigraphs. The de Bruijn/product-state component is already audited in `MC-125` and `MC-129`.

Accordingly, **no novelty is claimed** for higher-order Markov types, state augmentation, block-to-context conversion, or finite-memory recoding. The durable result is the exact consequence for the existing `MC-129` matched controls: simply replacing a one-step product-state histogram by a finite or growing finite-horizon path histogram does not recover excursion amplitude below the effective square-root scale.

## 4. Consequence for the mean-absolute transfer frontier

Before this corollary, the accepted transfer clue still listed generic “higher-order/noncommutative cross-time structure” as a possible escape from `MC-129`. The phrase was too broad. A statistic does not escape merely because it records paths of length `h>1` or several consecutive product-state transitions. If it finally forgets occurrence order and keeps only the empirical finite-horizon path type, `(3)` folds it into the already-matched enlarged one-step tensor.

The relevant resource is therefore **effective ordered memory**, not the nominal order of the statistic. For polynomially growing `k_0` and `h`, the exponent of `K=k_0+h-1` is the larger of their exponents; distributing a sub-square-root memory budget between starting context and finite look-ahead does not evade the obstruction.

A surviving path-based mechanism must retain something that does not factor through an empirical finite-horizon type, for example exact transition timestamps, the order of occurrences of path types, a nested or genuinely noncommutative multiscale relation that cannot be flattened into one longer finite context at the same information budget, a critical-or-larger effective horizon, non-additive state, or Möbius-specific arithmetic constraints that forbid the common-cycle reorderings.

## Boundaries and falsification tests

- The result matches **empirical path histograms**, not the full ordered trajectory. Two words with the same type may list the same path fragments in a different macro-order, and that order is exactly where the excursion separation lives.
- The source state is finite/growing local memory crossed with the additive state modulo `q`. Non-additive arithmetic state, exact integer height, prime/divisor labels, and multiplicative constraints are not represented.
- The exponent boundary belongs to this explicit `MC-129` construction. No positive reconstruction theorem is asserted when `K`, `q`, or the relevant combined resolution reaches square-root scale.
- The terminal-binning convention and the wholly-contained convention are both covered as explained above; arbitrary position weights or exact timestamps are outside the quotient.
- Matching a finite collection of several horizons gives no extra escape if their maximum effective context still fits under one admissible `K`: all shorter types are projections of the longest-context type.
- No RH assumption, `1/zeta` identity, contour shift, probabilistic independence, or numerical evidence enters the derivation.

## Consequence for the line

`MC-129` showed that contemporaneous local-context/modular-state cross-tabulation can forget macroscopic cycle order. The present corollary closes the immediate finite-horizon repair: **higher-order empirical path counts are only longer-context one-step counts for this purpose**.

The source-to-mean-absolute problem therefore remains open but narrower. A new candidate should identify an arithmetic or genuinely ordered carrier whose information cannot be flattened into a sub-square-root empirical context/path type before attempting a transfer to `D_M`.