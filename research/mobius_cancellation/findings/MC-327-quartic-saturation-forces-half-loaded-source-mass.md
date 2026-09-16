# MC-327 — Quartic saturation forces half-loaded source mass

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact reciprocal endpoint and common source-package notation of `MC-323`–`MC-326`. Let

\[
L=\langle\lambda_1,\ldots,\lambda_R\rangle\cong\mathbf F_2^R,
\qquad R\to\infty,
\]

and choose fixed lower-prime product representatives

\[
V_i\subseteq\{p\le y:p\text{ odd prime}\}
\qquad(1\le i\le R)
\]

for the independent generators. Put

\[
U:=\bigcup_{i=1}^R V_i,
\qquad
P:=\prod_{p\in U}p,
\qquad
m_i:=\prod_{p\in V_i}p,
\qquad
m_{ij}:=\prod_{p\in V_i\triangle V_j}p.
\tag{1}
\]

For each source prime `p in U`, write

\[
a_p:=\#\{i:p\in V_i\},
\qquad
u_p:=\frac{\log p}{\log P},
\qquad
u_p\ge0,
\qquad
\sum_{p\in U}\nu_p=1.
\tag{2}
\]

Define the logarithmically weighted **source-imbalance energy**

\[
\boxed{
\mathcal B_R
:=
\sum_{p\in U}
\nu_p
\left(\frac{2a_p-R}{R}\right)^2
\in[0,1].
}
\tag{3}
\]

Thus `B_R=0` exactly when every source column is loaded on `R/2` generators, while small `B_R` means that almost all source **logarithmic mass** lies on nearly half-loaded incidence columns.

Then the pair-distance double count of `MC-324` has the exact defect refinement

\[
\boxed{
\sum_{1\le i<j\le R}\log m_{ij}
=
\frac{R^2}{4}(1-\mathcal B_R)\log P.
}
\tag{4}
\]

Combining `(4)` with the varying-modulus prime Halász–Montgomery theorem already audited in `MC-323` gives, for every fixed `delta in (0,2)`,

\[
\boxed{
(1-\mathcal B_R)\frac{\log P}{\log y}
\ge
(4-2\delta)\left(1-\frac1R\right)
-O_\delta(R^{-2}).
}
\tag{5}
\]

Consequently, along every admissible sequence with `R->infinity`,

\[
\boxed{
\liminf
\left(1-\mathcal B_R\right)
\frac{\log P}{\log y}
\ge4.
}
\tag{6}
\]

This rigidifies the quartic floor of `MC-324`.

If a package **saturates** that floor,

\[
\frac{\log P}{\log y}=4+o(1),
\tag{7}
\]

then necessarily

\[
\boxed{\mathcal B_R\to0.}
\tag{8}
\]

Equivalently, for every fixed `epsilon>0`,

\[
\boxed{
\sum_{\substack{p\in U:\\ |a_p/R-1/2|\ge\epsilon}}
\frac{\log p}{\log P}
\longrightarrow0.
}
\tag{9}
\]

More generally, any persistent imbalance costs a strictly larger source exponent: if `liminf B_R>=beta>0`, then

\[
\boxed{
\liminf\frac{\log P}{\log y}
\ge\frac{4}{1-\beta}>4.
}
\tag{10}
\]

Thus the actual-source loophole left open by the universal minimax obstruction `MC-326` is not arbitrary. An economical common source package cannot avoid the high-loading incidence region. To remain at quartic cost, essentially all of its logarithmic source mass must concentrate on columns whose Hamming weight is `R/2+o(R)`, exactly where the pair-loading functional is asymptotically maximal.

There is a second saturation consequence. Under `(7)`, almost every generator and almost every pair mode also has package cost at the near-quadratic analytic horizon. For every fixed `epsilon>0`,

\[
\boxed{
\frac1R\#\left\{i:
\left|\frac{\log m_i}{\log y}-2\right|>\epsilon
\right\}\to0,
}
\tag{11}
\]

and

\[
\boxed{
\binom R2^{-1}
\#\left\{\{i,j\}:
\left|\frac{\log m_{ij}}{\log y}-2\right|>\epsilon
\right\}\to0.
}
\tag{12}
\]

The same convergence in density holds for the corresponding minimum primitive source conductors because `MC-323`–`MC-324` give the lower `y^(2-delta)` barrier for all but `O_delta(1)` modes and those primitive conductors are bounded above by their package representatives.

So quartic saturation is a **double near-equality regime**: source columns must be half loaded, and the selected generator/pair character costs must sit at the edge of the subquadratic Halász–Montgomery exclusion. No estimate for `M(x)` follows.

## 1. The Plotkin defect is exactly the source-imbalance energy

`MC-324` proved the exact weighted pair identity

\[
\sum_{i<j}\log m_{ij}
=
\sum_{p\in U}a_p(R-a_p)\log p.
\tag{13}
\]

Instead of discarding the distance-to-equality information through

\[
a_p(R-a_p)\le\frac{R^2}{4},
\]

use the exact identity

\[
a_p(R-a_p)
=
\frac{R^2}{4}
\left[
1-\left(\frac{2a_p-R}{R}\right)^2
\right].
\tag{14}
\]

Substitution into `(13)` gives

\[
\sum_{i<j}\log m_{ij}
=
\frac{R^2}{4}\log P
-
\frac{R^2}{4}
\sum_{p\in U}
\left(\frac{2a_p-R}{R}\right)^2\log p.
\]

Normalizing the second term by `log P` is exactly `(3)`, proving `(4)`.

This is the stability information hidden inside the classical Plotkin column count: every source coordinate away from half occupancy pays a **quadratic loss** in total pair distance. Here the coordinate has weight `log p`, so the natural stability variable is logarithmic source mass rather than the unweighted number of coordinates.

## 2. Pair conductor bills force the tradeoff

For the reciprocal endpoint, every pair mode satisfies

\[
x_{\lambda_i+\lambda_j}=1-\frac4R.
\]

As established in `MC-323` and applied in `MC-324`, for every fixed `delta>0` all but `E_delta=O_delta(1)` unordered pairs have minimum primitive source conductor greater than `y^(2-delta)`. Since the fixed package representative of `lambda_i+lambda_j` is the symmetric-difference product `m_ij`, one has

\[
m_{ij}>y^{2-\delta}
\tag{15}
\]

for all but `E_delta` pairs.

The exceptional terms are nonnegative, so

\[
\sum_{i<j}\log m_{ij}
\ge
\left(\binom R2-E_\delta\right)(2-\delta)\log y.
\tag{16}
\]

Combining `(4)` and `(16)` yields

\[
(1-\mathcal B_R)\frac{\log P}{\log y}
\ge
\frac{4(2-\delta)}{R^2}
\left(\binom R2-E_\delta\right),
\]

which is `(5)`. For each fixed `delta`, `E_delta/R^2->0`; taking `liminf` and only then letting the fixed `delta` tend to zero proves `(6)`. No moving `delta(y)` is inserted into the analytic theorem.

Equation `(6)` is stronger than the unrefined quartic lower bound because the combinatorial efficiency and source cost now appear multiplicatively. A package may use imbalanced source columns, but their Plotkin defect must be paid for by a larger total radical.

## 3. Near-quartic packages must concentrate on half-loaded columns

Assume `(7)`. From `(5)`, for every fixed `delta>0`,

\[
(1-\mathcal B_R)(4+o(1))
\ge4-2\delta-o(1).
\]

Hence

\[
\limsup\mathcal B_R\le\frac\delta2.
\]

Since `delta>0` is arbitrary, `(8)` follows.

For `(9)`, if `|a_p/R-1/2|>=epsilon`, then

\[
\left(\frac{2a_p-R}{R}\right)^2\ge4\epsilon^2.
\]

Therefore

\[
\sum_{|a_p/R-1/2|\ge\epsilon}\nu_p
\le
\frac{\mathcal B_R}{4\epsilon^2},
\tag{17}
\]

which tends to zero.

Conversely, if `B_R>=beta-o(1)`, equation `(5)` gives for every fixed `delta>0`

\[
\liminf\frac{\log P}{\log y}
\ge
\frac{4-2\delta}{1-\beta}.
\]

Letting `delta->0` proves `(10)`.

This is the direct answer to one surviving possibility in `MC-326`. The abstract minimax theorem could not exclude the actual arithmetic incidence set from avoiding high-loading source vectors. The present result says that such avoidance is expensive: at the quartic source frontier, the actual package is forced into the **maximally pair-loaded** Hamming band rather than away from it.

## 4. Quartic saturation also pins generator and pair costs to exponent two

Define

\[
t_p:=\frac{2a_p-R}{R}.
\]

Then `(3)` says `E_nu(t_p^2)=B_R`, and Cauchy–Schwarz gives

\[
\left|\sum_p\nu_p t_p\right|
\le\sqrt{\mathcal B_R}.
\tag{18}
\]

Since

\[
\frac{a_p}{R}=\frac{1+t_p}{2},
\]

under `(7)`–`(8)` one has

\[
\sum_p\nu_p\frac{a_p}{R}
=\frac12+o(1).
\tag{19}
\]

But

\[
\sum_{i=1}^R\log m_i
=
\sum_{p\in U}a_p\log p.
\tag{20}
\]

Dividing `(20)` by `R log y` and using `(7)` and `(19)` gives

\[
\boxed{
\frac1R\sum_{i=1}^R
\frac{\log m_i}{\log y}
=2+o(1).
}
\tag{21}
\]

Likewise, dividing `(4)` by `binom(R,2) log y` gives

\[
\boxed{
\binom R2^{-1}
\sum_{i<j}
\frac{\log m_{ij}}{\log y}
=2+o(1).
}
\tag{22}
\]

For every fixed `delta>0`, `MC-323` gives `log m_i/log y>2-delta` for all but `O_delta(1)` generators, and `MC-324` gives the same lower bound for all but `O_delta(1)` pairs. Equations `(21)`–`(22)` then force the upper tails to vanish as well.

For example, if a fraction `theta_R` of generators satisfies `log m_i/log y>=2+epsilon`, then outside `O_delta(1)` exceptions the remaining generators contribute at least `2-delta`. Thus

\[
2+o(1)
\ge
\theta_R(2+\epsilon)
+(1-\theta_R-o(1))(2-\delta),
\]

so

\[
\limsup\theta_R
\le\frac\delta{\epsilon+\delta}.
\]

Letting the fixed `delta` tend to zero gives `(11)`. The identical argument with `(22)` gives `(12)`.

This pinning is not an independent analytic theorem. It is the equality-case consequence of simultaneously saturating the pair-family conductor floor and the weighted Plotkin capacity.

## 5. Prior art and novelty boundary

The analytic input is exactly Schlage-Puchta's varying-modulus prime Halász–Montgomery theorem already audited in `MC-323`; no new character-sum estimate is claimed here.

The combinatorial input is the classical Plotkin pair-distance double count already used and bibliographically audited in `MC-324`: Morris Plotkin, *Binary codes with specified minimum distance*, IRE Transactions on Information Theory **6** (1960), no. 4, 445–450, DOI `10.1109/TIT.1960.1057584`. The standard proof maximizes a binary column's pair contribution at half occupancy. A fresh prior-art check on 16 September 2026 also found the usual balanced-column extremality and later Plotkin-bound refinements, but no source asserting the present logarithmically weighted near-equality consequence for this prime-source package.

No novelty is claimed for Plotkin's bound, its equality mechanism, the identity `(14)`, or generic stability of a concave quadratic around its maximum. The durable line-specific delta is their exact composition with the already established reciprocal endpoint pair spectrum and the near-quadratic varying-modulus conductor bills. That composition turns the quartic lower bound from a scalar cost statement into a structural rigidity theorem for the **actual source incidence distribution**.

## Boundaries and falsification tests

- **The balance is logarithmically weighted.** Equation `(9)` controls `sum log p`, not the raw number of source primes. A large collection of very small or collectively negligible source primes may remain highly imbalanced without contradicting the theorem.
- **Quartic saturation is an assumption for the rigidity conclusion.** The unconditional result inside this package is the tradeoff `(5)`–`(6)`. If an actual realization pays `P=y^(C+o(1))` with `C>4`, nonzero imbalance is compatible with the bound.
- **A common source package is load-bearing.** The identities `(4)`, `(20)`, and `(22)` use one fixed incidence matrix for all generators. A representation that cannot be written through common source columns lies outside this theorem.
- **The exact reciprocal endpoint is load-bearing for the current analytic bill.** The fixed pair bias `1-4/R` supplies the large-conductor conclusion from `MC-323`. A perturbed endpoint must retain enough uniformly biased pair modes before `(16)` remains valid.
- **The result does not classify which half-loaded columns occur.** There are exponentially many incidence vectors of weight near `R/2`. The theorem forces the Hamming band but does not yet expose an arithmetic distinction among vectors inside that band.
- **Signed/joint conductor inequalities remain open.** This result still uses separate positive conductor bills and a nonnegative pair-distance sum. A genuinely joint or signed analytic inequality could contain information not captured by `(5)`.
- **No Möbius realization or RH consequence is asserted.** The reciprocal endpoint remains a conditional candidate geometry. This finding only narrows what an economical realization of that candidate would have to look like.

The decisive checks are exact: `(4)` fails if the source-column double count is wrong; `(5)` fails if the `MC-324` pair conductor lower bound cannot be transferred to the chosen package products; `(8)`–`(10)` fail if the quadratic defect identity does not control the near-equality regime. The density conclusions `(11)`–`(12)` additionally require the all-but-`O_delta(1)` mode bounds from `MC-323`–`MC-324`.

## Consequence for the live frontier

`MC-326` showed that no universal source-blind nonnegative weighting can beat half loading, but left open the possibility that the actual arithmetic incidence set might occupy a favorable low-loading subset of source space. `MC-327` converts that qualitative loophole into a quantitative cost tradeoff. **Low-loading avoidance and quartic source efficiency are incompatible.**

At the current cost frontier, the source package must instead live almost entirely in the central Hamming band and simultaneously push almost every generator and pair character to the edge of the known subquadratic conductor exclusion. The next arithmetic discriminator therefore has to look *inside* that central band: restrictions on which half-loaded incidence columns can arise from actual lower-prime source characters, correlations between those columns, or a joint/signed character-family inequality. More universal averaging of separate conductor bills cannot exploit information that `(8)` has already forced into the Plotkin equality regime.