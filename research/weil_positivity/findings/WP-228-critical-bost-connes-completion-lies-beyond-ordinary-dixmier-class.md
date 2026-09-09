# WP-228 — Critical Bost–Connes completion lies beyond ordinary Dixmier class

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-MODES + OPERATOR-IDEAL-CLASSIFICATION + WEAK-SCHATTEN-FAILURE + DIXMIER-IDEAL-FAILURE + SECOND-LOGARITHMIC-GROWTH + ENERGY-CUTOFF-ASYMPTOTIC + MATCHED-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-227` proves that the frequency-matched positive completion of the critical Bost--Connes finite Weil amplitudes exists as a bounded positive block, but its minimal auxiliary block is not trace class. The natural next escape is therefore to replace the ordinary trace by a standard singular trace, especially the usual Dixmier trace used at a critical spectral dimension.

That escape can be tested exactly. For the source-forced critical amplitudes

\[
c_{p,k}=(\log p)p^{-k/2},
\qquad
B_{\min}=C^*C,
\tag{1}
\]

the eigenvalues of the minimal positive auxiliary block are

\[
b_{p,k}=(\log p)^2p^{-k}.
\tag{2}
\]

The resulting operator sits at a sharper endpoint than `WP-227` records:

\[
\boxed{
B_{\min}\in \bigcap_{q>1}\mathcal S_q
\quad\text{but}\quad
B_{\min}\notin \mathcal S_1,
}
\tag{3}
\]

and, more strongly, it is outside both of the standard first-order weak trace ideals used in ordinary Dixmier-trace language. If `\mu_n(B_{\min})` denotes the decreasing singular-value sequence, then

\[
\boxed{
n\,\mu_n(B_{\min})\longrightarrow\infty
\ \text{along a cofinal sequence},
}
\tag{4}
\]

so `B_min` is not weak Schatten `\mathcal S_{1,\infty}`. Its Ky Fan sums satisfy the exact first-order asymptotic

\[
\boxed{
\sum_{n\le N}\mu_n(B_{\min})
\sim \frac12(\log N)^2,
}
\tag{5}
\]

so they are not `O(\log N)` and `B_min` is also outside the usual Macaev/Marcinkiewicz Dixmier ideal `\mathcal M_{1,\infty}`. Consequently the ordinary logarithmically normalized Dixmier trace is not merely noncanonical here: **it is not defined on the source-forced minimal completion in its standard domain**.

The Bost--Connes energy cutoff gives the same obstruction without ranking singular values. If

\[
H(p,k)=k\log p
\tag{6}
\]

and the auxiliary trace is truncated at `H\le T`, then

\[
\boxed{
\sum_{k\log p\le T}(\log p)^2p^{-k}
\sim \frac12T^2.
}
\tag{7}
\]

Thus the intrinsic divergence scale is quadratic in logarithmic energy. A generalized Marcinkiewicz normalization at scale `\psi(N)\asymp(\log N)^2` is compatible with the singular-value growth, but introducing such a second-logarithmic singular trace would be an additional renormalization choice. The asymptotic itself supplies neither the Gamma factor nor the polar terms, and its leading coefficient is already forced by ordinary prime density.

This closes the simplest singular-trace repair of `WP-227`: the missing finite--archimedean sector cannot be identified with an **ordinary** Dixmier-trace completion of the critical matched bath. Surviving routes must use a genuinely larger singular ideal/weight, a modular or semifinite geometry with a different natural notion of size, a distributional completion, or a non-diagonal source construction whose auxiliary cost is not `C^*C`. Any such route must still derive the archimedean and polar terms intrinsically and obtain the final Weil sign independently.

## 1. Exact Schatten boundary of the minimal completion

From `WP-227`, on the prime-power mode space

\[
J_\infty=\{(p,k):p\text{ prime},\ k\ge1\},
\tag{8}
\]

the diagonal critical coupling and minimal auxiliary block are

\[
Ce_{p,k}=c_{p,k}e_{p,k},
\qquad
B_{\min}e_{p,k}=b_{p,k}e_{p,k},
\tag{9}
\]

with (1)--(2). For every `q>0`,

\[
\operatorname{Tr}(B_{\min}^q)
=
\sum_p\sum_{k\ge1}(\log p)^{2q}p^{-kq}
=
\sum_p\frac{(\log p)^{2q}}{p^q-1}.
\tag{10}
\]

If `q>1`, then for large `p`

\[
\frac{(\log p)^{2q}}{p^q-1}
\ll
\frac{(\log p)^{2q}}{p^q},
\tag{11}
\]

and comparison with the convergent integer series

\[
\sum_{n\ge2}\frac{(\log n)^{2q}}{n^q}
\tag{12}
\]

gives

\[
B_{\min}\in\mathcal S_q
\qquad(q>1).
\tag{13}
\]

At `q=1`, `WP-227` already proves

\[
\sum_p\frac{(\log p)^2}{p-1}=+\infty,
\tag{14}
\]

so `B_min` is not trace class. Since its eigenvalues tend to zero, eventually `0<b_{p,k}<1`; for `0<q<1`, `b_{p,k}^q\ge b_{p,k}` on that tail. Hence the sum also diverges for every `q\le1`. This proves the exact boundary (3).

The same statement for the cross block is shifted by a square root:

\[
\sum_{p,k}|c_{p,k}|^q
=
\sum_p\frac{(\log p)^q}{p^{q/2}-1}.
\tag{15}
\]

Therefore

\[
\boxed{
C\in\mathcal S_q\ \text{for every }q>2,
\qquad
C\notin\mathcal S_q\ \text{for }0<q\le2.
}
\tag{16}
\]

So the critical matched cross channel is not just outside Hilbert--Schmidt; it is the endpoint of the entire Schatten scale at exponent `2`, while its positive companion is the corresponding endpoint at exponent `1`.

## 2. Prime modes force failure of weak Schatten class

It is not enough to know `B_min\notin S_1`, because the canonical domain of many singular traces is larger than trace class. The first standard enlargement is weak Schatten class.

Restrict first to the `k=1` eigenvalues

\[
d_p:=\frac{(\log p)^2}{p}.
\tag{17}
\]

The function `(\log x)^2/x` is decreasing for `x>e^2`, so after finitely many terms the decreasing rearrangement of this prime subsequence is simply `d_{p_n}`, where `p_n` is the `n`-th prime. The prime number theorem gives

\[
p_n\sim n\log n,
\tag{18}
\]

and therefore

\[
d_{p_n}
=
\frac{(\log p_n)^2}{p_n}
\sim
\frac{\log n}{n}.
\tag{19}
\]

The full spectrum of `B_min` contains this subsequence. Hence its `n`-th decreasing singular value is at least the `n`-th decreasing member of the subsequence, up to an irrelevant finite reindexing:

\[
\mu_n(B_{\min})\ge (1+o(1))\frac{\log n}{n}
\tag{20}
\]

along a cofinal sequence. Consequently

\[
\sup_n n\mu_n(B_{\min})=+\infty.
\tag{21}
\]

Under the convention

\[
\mathcal S_{1,\infty}
=
\{T:\sup_n n\mu_n(T)<\infty\},
\tag{22}
\]

we obtain

\[
\boxed{B_{\min}\notin\mathcal S_{1,\infty}.}
\tag{23}
\]

Likewise the `k=1` singular values of `C` are

\[
a_p=\frac{\log p}{\sqrt p},
\tag{24}
\]

and

\[
a_{p_n}\sim\sqrt{\frac{\log n}{n}}.
\tag{25}
\]

Therefore

\[
\sup_n n^{1/2}\mu_n(C)=+\infty,
\tag{26}
\]

so

\[
\boxed{C\notin\mathcal S_{2,\infty}.}
\tag{27}
\]

This is a stronger endpoint failure than the ordinary `S_2/S_1` statement of `WP-227`.

## 3. The usual Dixmier/Macaev ideal also fails

Notation around `L^{1,\infty}` is not uniform: some authors use it for weak Schatten class, while Dixmier traces in noncommutative geometry are commonly formulated on the larger Macaev/Marcinkiewicz ideal characterized, for positive compact operators, by

\[
\sup_{N\ge2}
\frac{1}{\log N}
\sum_{n\le N}\mu_n(T)<\infty.
\tag{28}
\]

The critical bath fails this larger condition too.

For the prime subsequence, partial summation and the prime number theorem give

\[
\sum_{p\le x}\frac{(\log p)^2}{p}
\sim
\frac12(\log x)^2.
\tag{29}
\]

The higher prime powers contribute finite total mass:

\[
\sum_p\sum_{k\ge2}(\log p)^2p^{-k}
=
\sum_p\frac{(\log p)^2}{p(p-1)}
<\infty.
\tag{30}
\]

Let `D_N` be the sum of the `N` largest `k=1` eigenvalues. By (18)--(19),

\[
D_N
\sim
\frac12(\log p_N)^2
\sim
\frac12(\log N)^2.
\tag{31}
\]

Adding the entire `k\ge2` sector can change any Ky Fan partial sum by at most the finite constant in (30). Conversely, the full `N`-term Ky Fan sum is at least `D_N`. Therefore

\[
\boxed{
\sum_{n\le N}\mu_n(B_{\min})
=
\frac12(\log N)^2+o((\log N)^2).
}
\tag{32}
\]

In particular,

\[
\frac1{\log N}
\sum_{n\le N}\mu_n(B_{\min})
\sim
\frac12\log N
\longrightarrow+\infty.
\tag{33}
\]

Thus

\[
\boxed{B_{\min}\notin\mathcal M_{1,\infty},}
\tag{34}
\]

where `M_{1,\infty}` denotes the ordinary logarithmic Marcinkiewicz/Macaev ideal supporting the standard Dixmier trace.

The conclusion is deliberately stronger than “the Dixmier trace diverges.” The standard Dixmier functional is defined by applying a generalized limit to the bounded logarithmic means in (28). For `B_min`, those means themselves diverge. The operator is outside that domain.

## 4. The source Hamiltonian sees quadratic energy growth

The singular-value calculation can be checked in the source's own logarithmic energy coordinate. The Bost--Connes mode `(p,k)` has energy

\[
E_{p,k}=k\log p.
\tag{35}
\]

Define the finite-energy auxiliary mass

\[
R(T)
:=
\sum_{k\log p\le T}(\log p)^2p^{-k}.
\tag{36}
\]

The `k=1` piece is

\[
R_1(T)
=
\sum_{p\le e^T}\frac{(\log p)^2}{p}
\sim
\frac12T^2
\tag{37}
\]

by (29). The complete contribution of `k\ge2` is bounded by the finite constant (30), uniformly in `T`. Hence

\[
\boxed{R(T)\sim\frac12T^2.}
\tag{38}
\]

This gives a source-coordinate interpretation of (32): the matched positive bath has **quadratic** trace growth in the logarithmic Bost--Connes energy cutoff. Ordinary Dixmier normalization would correspond to first-order logarithmic growth of ranked partial sums; it is one logarithm too small for this exact source-forced completion.

## 5. The natural larger scale is second-logarithmic, but it is not yet geometry

Equation (32) implies that the minimal bath does fit a larger Marcinkiewicz scale whose gauge grows like

\[
\psi(N)\asymp(\log N)^2.
\tag{39}
\]

At the level of singular-value asymptotics,

\[
\frac{1}{(\log N)^2}
\sum_{n\le N}\mu_n(B_{\min})
\longrightarrow\frac12.
\tag{40}
\]

General singular traces on Marcinkiewicz ideals are classical operator theory; this finding does **not** claim that such a trace construction is new. It also does not promote the particular gauge in (39) to a canonical archimedean object. The point is narrower and source-specific: if the `WP-227` minimal positive completion is to be assigned a finite singular “mass” by normalization of its eigenvalue sums, then the source itself forces a second-logarithmic rather than ordinary Dixmier scale.

This distinction matters for the research mandate. The number `1/2` in (40) is obtained entirely from the finite-prime mode density and the prime number theorem. No Gamma kernel, real-place representation, polar divisor, or completed explicit formula entered the derivation. A generalized prime system with the same first-order prime-counting law would reproduce the same leading quadratic-logarithmic growth. Thus the renormalized coefficient cannot by itself be interpreted as the missing Riemann archimedean counterterm.

The result therefore redirects rather than completes the route: a larger singular ideal may be mathematically admissible, but **choosing a second-logarithmic singular trace is extra structure unless Mathia independently derives that trace/weight from a geometric real-place completion**.

## 6. Aggressive falsification and escape routes

Several possible overclaims fail under matched controls.

First, (34) does not say that no singular trace can act on `B_min`. General Marcinkiewicz ideals and singular symmetric functionals extend far beyond the ordinary Dixmier ideal. The no-go is specifically against identifying the critical bath with the standard logarithmic Dixmier-trace object.

Second, the result does not say every positive completion has exactly the spectrum (2). `B_min=C^*C` is the sharp minimal companion in the unit-normalized block category of `WP-227`. A larger positive auxiliary block can only increase the finite-dimensional trace lower bounds, but a non-diagonal completion with a different ambient notion of weight, a modular trace, or a genuinely different source sector may leave this category.

Third, quadratic divergence is not evidence for the Gamma place. It survives a matched control which retains only first-order prime density. The archimedean sector still has to be derived rather than inferred from the need to renormalize.

Fourth, ordinary positive completion remains available: `WP-227` already constructs the bounded positive block. What is excluded is a specific attempt to turn its infinite auxiliary cost into a standard spectral-triple-style Dixmier integral without introducing new structure.

The surviving routes are therefore sharply delimited:

- a source-forced generalized Marcinkiewicz/singular weight at a larger scale;
- a semifinite or modular geometry in which the relevant positive weight is not the ordinary operator trace;
- a continuous/distributional auxiliary sector whose local density derives the Gamma and polar terms;
- a non-diagonal finite--archimedean incidence construction which changes the minimal companion rather than merely renormalizing `C^*C`.

Each must still pass the primary gate: one intrinsic geometry must produce the finite and archimedean/global pieces, and its positivity must be independent of RH or inserted zero data.

## 7. Prior-art and novelty audit

The Bost--Connes multiplicative Hamiltonian and its zeta partition function are classical and already anchored in `SOURCES.md`. The operator-ideal machinery used here is also classical. In particular, standard Dixmier traces act on logarithmic Marcinkiewicz/Macaev ideals, and the broader theory of singular symmetric functionals on general Marcinkiewicz spaces is established prior art; see Steven Lord, Aleksandr Sedaev, and Fyodor Sukochev, *Dixmier Traces as Singular Symmetric Functionals and Applications to Measurable Operators*, Journal of Functional Analysis 224 (2005), 72--106, DOI `10.1016/j.jfa.2005.01.002`, arXiv `math/0501131`.

A bounded literature audit around Bost--Connes systems, spectral triples, Dixmier traces, weak Schatten ideals, and generalized Marcinkiewicz traces did not expose a source identifying the particular `WP-227` matched critical Gram companion or computing its operator-ideal endpoint. The durable claim here is therefore **not** a new singular-trace theorem. It is the Mathia-specific classification of the exact source-forced completion:

\[
C:\ \mathcal S_{>2}\setminus\mathcal S_{2,\infty},
\qquad
C^*C:\ \mathcal S_{>1}\setminus\mathcal M_{1,\infty},
\tag{41}
\]

with the second-logarithmic asymptotic (32)/(38), and the resulting exclusion of ordinary Dixmier completion as the missing Weil-positive geometry.

This remains a negative/narrowing finding. It derives no global Weil quadratic form and proves no part of RH.
