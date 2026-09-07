# MC-134 — Divisor-filtration persistent homology is an exact dyadic barcode

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Let `Delta_n` be Björner's simplicial complex from `MC-133`: its simplices are the prime-factor sets `P(q)` of squarefree integers `q<=n`, and the filtration parameter is the integer product itself. Fix any field `F` and take reduced homology.

The full one-parameter persistent homology of

\[
\Delta_1\subseteq\Delta_2\subseteq\Delta_3\subseteq\cdots
\]

has an exact barcode. For every odd squarefree integer `m>1`, with `r=Omega(m)`, there is exactly one bar

\[
\boxed{[m,2m)\quad\text{in degree }r-1,}
\tag{1}
\]

and these are all reduced-homology bars. Equivalently, for integers `a<=b`,

\[
\boxed{
\operatorname{rank}\!\left(
\widetilde H_k(\Delta_a;F)\to\widetilde H_k(\Delta_b;F)
\right)
=
\#\left\{
\begin{array}{c}
m\text{ odd squarefree},\\
\Omega(m)=k+1,\\
b/2<m\le a
\end{array}
\right\}.
}
\tag{2}
\]

In particular,

\[
\widetilde H_k(\Delta_a;F)\longrightarrow
\widetilde H_k(\Delta_b;F)
\quad\text{is the zero map whenever }b\ge2a.
\tag{3}
\]

Thus every reduced class has multiplicative lifetime exactly `2`, or additive lifetime exactly `log 2` after the logarithmic change of scale. Ordinary one-parameter persistent homology does **not** reveal a long-lived inter-scale topological carrier hidden by the single-scale Betti numbers of `MC-133`: the persistence module is completely decomposed into dyadic birth/death pairs.

The barcode is still arithmetically rich because its birth times recover the odd squarefree integers together with `Omega(m)`. But the parity-signed population alive at time `n` is precisely the same terminal-annulus Möbius sum already isolated in `MC-133`. Persistence therefore supplies no independent sign estimate merely by retaining the inclusion maps.

## 1. The integer filtration is simplex-wise and face-compatible

A finite set of primes `S` is a simplex of `Delta_n` exactly when

\[
q(S)=\prod_{p\in S}p\le n.
\]

Hence every squarefree integer `q>1` contributes exactly one simplex `P(q)` at filtration value `q`; a nonsquarefree integer contributes none. If `T` is a proper face of `S`, then `q(T)` is a proper divisor of `q(S)` and therefore `q(T)<q(S)`. Ordering simplices by their integer products is consequently a valid strict filtration order.

This simple observation lets the persistence pairing be read directly from the filtered simplicial boundary matrix.

## 2. Every odd simplex is paired with its doubling simplex

Let `m>1` be odd and squarefree, with prime set `P(m)` and `r=Omega(m)`. The simplex `P(m)` has dimension `r-1`. Its doubled integer `2m` is squarefree and contributes the `r`-simplex

\[
P(2m)=P(m)\cup\{2\}.
\]

The codimension-one faces of `P(2m)` have products

\[
m
\quad\text{and}\quad
\frac{2m}{p}\qquad(p\mid m).
\tag{4}
\]

Because every prime divisor `p` of the odd integer `m` satisfies `p>=3`,

\[
\frac{2m}{p}<m.
\tag{5}
\]

Therefore the latest boundary face of the simplex entering at `2m` is exactly the row indexed by `m`, with coefficient `+1` or `-1` and hence nonzero over every field.

More importantly, **no earlier simplex column can contain row `m` at all**. A simplex having `P(m)` as a codimension-one face must have product `mp` for a prime `p` not dividing `m`. The smallest possible such prime is `2`, so the first coface of `P(m)` in the filtration is exactly `P(2m)` at time `2m`. Any odd new prime gives a coface at least `3m`.

Consequently every linear combination of boundary columns with filtration value `<2m` has zero coefficient in row `m`. In the standard left-to-right persistence reduction, the column for `2m` therefore cannot cancel its row-`m` pivot. Its reduced lowest/latest nonzero row is exactly `m`:

\[
\operatorname{low}(2m)=m.
\tag{6}
\]

The standard persistence pairing theorem then pairs the simplex born at `m` with the killing simplex at `2m`. This proves `(1)`. As an independent consistency check, Björner's formula

\[
\beta_k(n)=\sigma^{\mathrm{odd}}_{k+1}(n)-
\sigma^{\mathrm{odd}}_{k+1}(n/2)
\tag{7}
\]

shows exactly the same event: at an odd squarefree `m` with `Omega(m)=k+1`, `beta_k` jumps up by one, while at `2m` it jumps down by one.

Every squarefree simplex except the initial vertex `2` is of one of these two forms: an odd `m>1` is a birth simplex, and an even squarefree integer is uniquely `2m` with `m` odd squarefree and is its death simplex. The vertex `2` is the sole essential ordinary `H_0` component and disappears from reduced homology. Hence no additional reduced bars remain.

## 3. Rank invariant and finite persistence horizon

A bar `[m,2m)` contributes one dimension to the map from time `a` to time `b>=a` exactly when it has already been born at `a` and is still alive at `b`:

\[
m\le a,
\qquad
b<2m.
\]

This is equivalent to `b/2<m<=a`, giving `(2)` immediately.

If `b>=2a`, then every `m<=a` satisfies `2m<=2a<=b`, so no bar alive at `a` survives to `b`. This proves `(3)`. On logarithmic scale `t=log n`, every interval becomes

\[
[\log m,\log m+\log2),
\]

so all reduced persistent lifetimes are exactly the same constant `log 2`.

This is stronger than the static statement in `MC-133`: it determines not only the dimensions of every homology group but all linear transport maps of the ordinary one-parameter persistence module over a field.

## 4. The barcode still stores the same Möbius parity burden

At time `n`, the degree-`k` bars alive are exactly the odd squarefree integers

\[
n/2<m\le n,
\qquad
\Omega(m)=k+1.
\]

Thus the number of live degree-`k` bars is Björner's `beta_k(n)`. Taking the alternating degree parity gives

\[
\sum_k(-1)^{k-1}\beta_k(n)
=
\sum_{\substack{n/2<m\le n\\2\nmid m}}\mu(m)
=M(n),
\tag{8}
\]

as derived in `MC-133`.

So the complete barcode has two sharply different aspects:

- **transport topology is rigid:** every reduced class dies at exactly twice its birth scale and all maps across a factor-two scale gap vanish;
- **birth data are arithmetic:** the set of birth times and their dimensions encodes odd squarefree support and prime-factor parity, so the signed live-bar count reconstructs the Mertens target.

A persistence statistic that forgets the degree parity loses the required cancellation and remains on linear mass; a statistic retaining enough parity to recover `(8)` has not made the Mertens estimate cheaper merely by changing representation.

## Prior art and novelty assessment

Anders Björner, *A cell complex in number theory*, Advances in Applied Mathematics 46 (2011), 71–85, DOI `10.1016/j.aam.2010.09.007`, arXiv `1101.5704`, is the primary source for the complexes `Delta_n`, their shifted/wedge-of-spheres structure, the Betti formula `(7)`, and the Euler-characteristic/Mertens relation used here. `MC-133` already audited those static results.

Afra Zomorodian and Gunnar Carlsson, *Computing Persistent Homology*, Discrete & Computational Geometry 33 (2005), 249–274, DOI `10.1007/s00454-004-1146-y`, is the standard persistence-module and filtered-boundary-matrix reference. The only persistence machinery used above is the classical rule that a nonzero reduced boundary column with pivot row `i` pairs the simplex in row `i` with that column's simplex.

Targeted searches for Björner's number-theoretic complex together with persistent homology/barcodes, and for persistent homology of squarefree/divisibility filtrations tied to the number-theoretic Möbius function, did not locate this exact dyadic-barcode statement. That search result is **not** a novelty claim. The mathematical contribution recorded here is the direct derivation `(1)`--`(3)` from Björner's filtration plus the standard persistence pairing algorithm.

## Boundaries and falsification tests

- The claim concerns **ordinary one-parameter reduced persistent homology over a field**. It does not rule out chain-level structures, arithmetic labels on cycles, cohomological operations, multiparameter filtrations, spectral constructions, or another invariant that does not factor through this persistence module.
- The complete barcode itself is not a low-information summary: its births encode every odd squarefree integer and `Omega(m)`. A proposed use of the full barcode must therefore show an estimate genuinely cheaper than reconstructing the original Möbius parity data.
- Equation `(3)` kills long-lived ordinary homology classes, not every possible correlation between different short bars. Such correlations are already a function of the arithmetic birth process and require a separate estimate.
- Reduced homology removes the single essential ordinary `H_0` component born at the vertex `2`. No RH-facing information is hidden in that universal component.
- The proof is coefficient-independent over fields because the decisive face coefficient is `+-1`, hence nonzero in every characteristic.

A finite falsification test is immediate: build the filtered boundary matrix through any cutoff `N`, reduce it over any field, and check that every finite reduced pair is `(m,2m)` with `m>1` odd squarefree and that every expected pair with `2m<=N` occurs. A counterexample to that pairing would refute `(1)`.

## Consequence for the line

`MC-133` left the inclusion maps of the filtration as a genuine residual. This finding closes that residual at the level of **ordinary one-parameter persistent homology**. The divisor filtration does not contain a hidden long-range homology class: all reduced persistence dies within one dyadic step, and the full persistence module is just the direct sum of the explicit intervals `(1)`.

A surviving divisor-topology route must therefore use structure not determined by this barcode—such as a genuinely different filtration parameter, chain-level arithmetic relations, additional labels/operations, or another Möbius-specific inter-scale object—and must still prove that the retained statistic constrains first-absolute Mertens excursion without simply re-encoding `mu` or `M`.