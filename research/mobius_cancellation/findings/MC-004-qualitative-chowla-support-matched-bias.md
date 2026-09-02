# MC-004 — Qualitative Chowla with exact square-free support permits near-linear bias

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`.

## Claim

There exists a deterministic sequence

\[
a:\mathbb N\to\{-1,0,1\}
\]

with **exactly the same zero set as the Möbius function**,

\[
|a(n)|=\mu(n)^2\qquad(n\ge1),
\tag{1}
\]

which has the full qualitative index-two Chowla property but nevertheless has almost-linear anchored partial sums along an infinite subsequence.

More precisely, for every fixed choice

\[
0\le h_0<h_1<\cdots<h_r,
\qquad e_j\in\{1,2\},
\]

with the exponents not all equal to `2`, one has

\[
\frac1X\sum_{n\le X}
\prod_{j=0}^r a(n+h_j)^{e_j}
\longrightarrow0,
\tag{2}
\]

while for some sequence `X_j -> infinity`,

\[
\left|\sum_{n\le X_j}a(n)\right|
\gg \frac{X_j}{\log X_j}.
\tag{3}
\]

Consequently, **full qualitative fixed-shift Chowla cancellation, even when combined with Möbius's exact square-free support, does not imply any fixed power saving for the summatory function**. For every fixed `c>0`, properties (1)–(2) alone are compatible with failure of

\[
\sum_{n\le X}a(n)=O(X^{1-c}).
\tag{4}
\]

The missing hypothesis in this matched control is multiplicativity: the constructed sequence is deliberately not multiplicative. Thus the result does not model all of Möbius. It proves a narrower information-loss statement: an RH-relevant argument cannot treat qualitative fixed-shift Chowla correlations plus square-free support as a sufficient black-box substitute for the arithmetic relations among Möbius values. It needs quantitative uniformity, multiplicative structure, or another datum that ties the fixed-shift limits to the anchored sum at a polynomial rate.

## 1. A Chowla base with the exact square-free support

Write

\[
q(n)=\mu(n)^2,
\]

so `q(n)` is the indicator of the square-free integers. Let `(epsilon_n)` be independent Rademacher variables, each taking `+1` and `-1` with probability `1/2`, and define

\[
b(n)=q(n)\epsilon_n.
\tag{5}
\]

The variables `b(n)` are independent, take values in `{-1,0,1}`, and satisfy

\[
\mathbb E[b(n)]=0
\qquad\text{for every }n.
\tag{6}
\]

Shi's Proposition 5.7 (`MC-S10`) applies to independent, not necessarily identically distributed, variables in `S^1 union {0}`. In the index-two case the only nontrivial index moment is the first moment, so (6) implies that almost surely `(b(n))` has the Chowla property. Definition 3.3 of the same paper states precisely (2) for `{-1,0,1}` sequences.

Choose one realization `b` from this probability-one set. It is now a deterministic Chowla sequence and, pointwise,

\[
|b(n)|=q(n)=\mu(n)^2.
\tag{7}
\]

No assertion about Möbius itself has entered: the random signs supply only an existence base on the same deterministic support.

## 2. Sparse coherent blocks preserve every fixed Chowla correlation

Choose integers `N_j` growing so rapidly that, for example,

\[
N_{j+1}\ge (N_j+L_j)^3,
\qquad
L_j=\left\lfloor\frac{N_j}{\log N_j}\right\rfloor,
\tag{8}
\]

with `N_1` sufficiently large. Let

\[
I_j=(N_j,N_j+L_j]\cap\mathbb N,
\qquad
D=\bigcup_j I_j.
\]

Then `D` has natural density zero. Indeed, inside the `j`-th block its newly accumulated mass is at most

\[
\frac{L_j}{N_j}=\frac1{\log N_j}+o(1),
\]

and the super-polynomial separation makes the total mass of all earlier blocks negligible relative to `N_j`; between blocks the ratio only decreases.

Construct `a` recursively. Outside `D`, put `a(n)=b(n)`. At the start of block `I_j`, let

\[
A(N_j)=\sum_{n\le N_j}a(n)
\]

and choose

\[
\sigma_j=
\begin{cases}
+1,&A(N_j)\ge0,\\
-1,&A(N_j)<0.
\end{cases}
\tag{9}
\]

For `n in I_j`, set

\[
a(n)=\sigma_j q(n).
\tag{10}
\]

Thus only signs at square-free positions are changed, and (1) remains exact.

Now fix one Chowla pattern `(h_0,...,h_r;e_0,...,e_r)`. The corresponding product for `a` can differ from that for `b` only for starting indices `n` such that at least one `n+h_k` lies in `D`. Up to `X`, the number of such starts is at most

\[
(r+1)\,|D\cap[1,X+h_r]|+O(1)=o(X).
\tag{11}
\]

Every product has modulus at most one, hence the difference of the two normalized correlations is `o(1)`. Since the correlation for `b` tends to zero, the correlation for `a` also tends to zero. The argument works separately for every fixed finite pattern, so `a` retains the full qualitative Chowla property (2).

This preservation step is the Chowla analogue of a standard phenomenon for normal binary sequences: Pincus and Singer (`MC-S11`) record that changing `o(N)` symbols preserves normality, while allowing arbitrarily slow decay of finite-prefix bias. That literature is prior-art precedent for the information-loss mechanism; it is not being used to infer anything arithmetic about Möbius.

## 3. The same sparse blocks force `X/log X` partial sums

Let

\[
X_j=N_j+L_j
\]

and denote by

\[
Q_j=\sum_{N_j<n\le X_j}q(n)
\]

the number of square-free integers in the `j`-th block. From (9)–(10),

\[
A(X_j)=A(N_j)+\sigma_j Q_j,
\]

and the sign was chosen to reinforce the existing prefix, so

\[
|A(X_j)|=|A(N_j)|+Q_j\ge Q_j.
\tag{12}
\]

The classical square-free counting estimate (`MC-S12`)

\[
Q(x):=\sum_{n\le x}\mu(n)^2
=\frac6{\pi^2}x+O(\sqrt x)
\tag{13}
\]

is already more than sufficient. Because `L_j=N_j/log N_j+O(1)` is much larger than `sqrt(N_j)`, subtracting (13) at the two endpoints gives

\[
Q_j
=\frac6{\pi^2}L_j+O(\sqrt{N_j})
=\left(\frac6{\pi^2}+o(1)\right)
\frac{N_j}{\log N_j}.
\tag{14}
\]

Since `X_j=N_j(1+o(1))`, (12)–(14) prove (3). Finally, for every fixed `c>0`,

\[
\frac{X/\log X}{X^{1-c}}
=\frac{X^c}{\log X}\longrightarrow\infty,
\]

so no estimate (4) can follow from (1)–(2) alone.

Notice that the one-point case of the Chowla property already forces `A(X)=o(X)`. The construction is therefore not evading qualitative mean cancellation; it makes that convergence deliberately slow enough to remain above every fixed power-saving scale along a subsequence.

## Prior art and novelty assessment

The Chowla property and the random-sequence criterion used to obtain the base are established sequence-theoretic prior art (`MC-S10`). Density-zero perturbations preserving qualitative finite-pattern equidistribution, together with arbitrarily slow bias, have a close explicit precedent in the theory of normal sequences (`MC-S11`). Square-free density is classical (`MC-S12`). No novelty is claimed for those ingredients or for the generic observation that a qualitative limit need not provide a rate.

The line-specific contribution is the **support-matched synthesis**: retain the exact Möbius zero set `mu^2`, retain all fixed finite Chowla correlations, and still force an anchored bias of order `X/log X` along a subsequence. A targeted search found the general Chowla-sequence constructions and the normal-sequence perturbation precedent, but did not justify a claim that this particular support-matched formulation is new sequence theory. It is therefore stored as a matched-control obstruction, not as a standalone novelty claim.

Modern arithmetic Chowla results contain information that this counterexample intentionally discards. Matomäki–Radziwiłł–Tao (`MC-S13`) average correlations over a family of shifts whose range grows with `X` and obtain quantitative decay of roughly logarithmic strength; later higher-uniformity results strengthen related almost-all statements. Such uniform quantitative estimates are not consequences of the fixed-pattern limits in (2), so this finding does not rule out extracting additional cancellation from their proof-level structure.

## Boundaries and failure modes

The decisive boundary is **multiplicativity**. The coherent sign overwrite in (10) breaks multiplicative consistency, and no claim is made that a multiplicative `{-1,0,1}` sequence with Möbius's exact support can realize the same construction.

Accordingly, this finding does not show that Chowla's conjecture for Möbius would be useless, nor that quantitative Chowla estimates cannot contribute to RH. It rules out only deductions that retain no more than:

1. the exact square-free support `|a|=mu^2`; and
2. the qualitative vanishing of every fixed Chowla correlation.

A proposed escape must identify which additional arithmetic datum blocks the sparse coherent perturbation. Candidate data include:

- a quantitative rate uniform over a growing family of shifts;
- multiplicative identities coupling distant scales and preventing arbitrary sign overwrites;
- signed multiscale relations strong enough to constrain an anchored prefix rather than only translation averages;
- correlation estimates with a polynomial information budget after exceptional sets and averaging losses are included.

Merely adding more **fixed** correlation limits does not help: the constructed `a` already satisfies all of them.

## Relation to MC-001 and MC-002

`MC-001` showed that short-interval magnitude plus exceptional-set measure loses too much information when window signs are discarded. `MC-002` showed that one standard pretentious scalar has only `O(log log x)` dynamic range. `MC-004` closes a different tempting loophole: replacing those compressed summaries by the entire collection of **qualitative fixed-shift Chowla limits** still does not supply a polynomial rate, even after matching Möbius's square-free support exactly.

The common frontier is now sharper. An RH-relevant local/correlation route needs not merely stronger pseudorandomness language but an explicitly quantitative carrier whose scale grows strongly enough, or a specifically multiplicative constraint that rules out the density-zero coherent blocks used here.