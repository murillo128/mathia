# WP-085 — Cover-range principal-angle defect is positive, but its log-degree response is reference-relative

**Status:** `EXACT-DERIVED + POSITIVE-CANDIDATE + DECISIVE-NEGATIVE + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-084` leaves open a concrete escape from the diagonal fixed-shift obstruction: introduce a **noncommuting Mathia-native operation before scalar readout**. The pointed cover isometries from `WP-073`,

\[
W_n e_k=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r},
\qquad
W_mW_n=W_{mn},
\]

commute as a semigroup, but their range projections

\[
P_n:=W_nW_n^*
\]

do not generally commute. This produces an intrinsic positive principal-angle defect

\[
\Delta_{m,n}
:=P_m(I-P_n)P_m\big|_{\operatorname{Ran}P_m}
\succeq0.
\]

On one `lcm(m,n)` cell its reduced determinant can be evaluated exactly. Writing

\[
g=(m,n),\qquad
a=\min(m/g,n/g),\qquad b=\max(m/g,n/g),
\]

one gets

\[
\boxed{
\det{}'\Delta_{m,n}
=\frac{((a-1)!)^2}{a^{a-2}b^{a-1}}.
}
\]

In particular, for the least nontrivial reference cover `m=2`,

\[
\boxed{
-\log\det{}'\Delta_{2,n}
=\begin{cases}
\log n,&n\text{ odd},\\
0,&n\text{ even}.
\end{cases}}
\]

Thus the noncommuting cover geometry really does contain a new **positive local source of logarithmic degree** that is independent of the inverse-scale trace construction of `WP-074`. It uses no zeta function, zero data, analytic continuation, fitted kernel, or inserted arithmetic sign.

The route nevertheless fails the global Weil mandate for several exact reasons. The determinant is only a per-period invariant: on the full Hardy space the same finite principal-angle block repeats infinitely often. The dyadic reference is blind to every even degree, and its Möbius primitive is, for `n>2`, exactly

\[
\Lambda(n)-\mathbf1_{2\mid n}\Lambda(n/2),
\]

the same parity-twisted Mangoldt shadow already found by the independent Hardy/Hilbert relative trace `PC-076` (up to its factor `1/2`; the level `n=2` differs because the projection-angle defect is nested and vanishes). More fundamentally, the nonnegative pairwise scalar

\[
F(m,n):=-\log\det{}'\Delta_{m,n}
\]

is **not** a positive kernel and is not even conditionally of one sign on zero-sum degree combinations. The operator positivity of each `\Delta_{m,n}` therefore does not descend to a positive quadratic form on the degree/test-function variables required by Weil.

This closes only the canonical **range-projection principal-angle / reduced-logdet** implementation of the noncommuting escape. It does not rule out an operator-valued cross-cover construction formed before determinant, a nonperiodic boundary coupling, or a genuinely nonseparable finite--archimedean object with its own independent sign theorem.

## 1. Exact range projections are block conditional expectations

From the normalized pointed cover model,

\[
P_n=W_nW_n^*.
\]

In the basis `e_0,e_1,...`, this is the orthogonal projection onto sequences constant on each consecutive block of length `n`:

\[
(P_n)_{ij}
=\begin{cases}
1/n,&\lfloor i/n\rfloor=\lfloor j/n\rfloor,\\
0,&\text{otherwise}.
\end{cases}
\tag{1}
\]

Hence `P_m` and `P_n` are ordinary finite-partition conditional-expectation projections repeated along `N_0`. They commute when the corresponding partitions are nested, but not in general. For example, `P_2P_3\ne P_3P_2`.

For every pair `m,n`, let

\[
L=\operatorname{lcm}(m,n).
\]

The cell

\[
E_L:=\operatorname{span}\{e_0,\ldots,e_{L-1}\}
\tag{2}
\]

reduces both projections. On `\operatorname{Ran}(P_m|_{E_L})`, define

\[
\boxed{
\Delta_{m,n}^{(L)}
:=I-P_mP_nP_m.
}
\tag{3}
\]

For every vector `x` in this finite-dimensional range,

\[
\langle x,\Delta_{m,n}^{(L)}x\rangle
=\|(I-P_n)x\|^2\ge0.
\tag{4}
\]

Thus positivity is a direct Hilbert-space theorem. It is present **before** any arithmetic interpretation.

The nonzero eigenvalues of `\Delta` are the squared sines of the principal angles between the two block-constant subspaces, together with possible unit eigenvalues coming from a dimension mismatch. Consequently

\[
0<\det{}'\Delta_{m,n}^{(L)}\le1,
\qquad
F(m,n):=-\log\det{}'\Delta_{m,n}^{(L)}\ge0,
\tag{5}
\]

where `det'` is the product of positive eigenvalues and the empty product is `1`.

## 2. Exact principal-angle determinant

First suppose `(m,n)=1` and `2\le m\le n`; the cases `m=1` and `m=n` follow by the same formula with the empty-product convention.

Partition the cell `\{0,\ldots,mn-1\}` into consecutive `m`-blocks `A_i` and consecutive `n`-blocks `B_j`. Use the normalized block indicators

\[
f_i=\frac{\mathbf1_{A_i}}{\sqrt m},
\qquad i=0,\ldots,n-1,
\]

and

\[
g_j=\frac{\mathbf1_{B_j}}{\sqrt n},
\qquad j=0,\ldots,m-1.
\]

The overlap matrix is

\[
R_{ij}=\langle f_i,g_j\rangle
=\frac{|A_i\cap B_j|}{\sqrt{mn}}.
\tag{6}
\]

In the `f_i` basis,

\[
P_mP_nP_m=RR^*,
\qquad
\Delta_{m,n}^{(mn)}=I_n-RR^*.
\tag{7}
\]

The nonunit spectrum of `I_n-RR^*` is the nonzero spectrum of `I_m-R^*R`. Because `m\le n`, each `m`-block crosses at most one interior `n`-boundary. The boundary at `jn`, `1\le j<m`, lies strictly inside an `m`-block at residue

\[
r_j\equiv jn\pmod m,
\qquad 1\le r_j<m.
\tag{8}
\]

A direct overlap calculation gives

\[
I_m-R^*R=L_{\rm path}(w_1,\ldots,w_{m-1}),
\tag{9}
\]

the weighted path Laplacian on `m` vertices with conductances

\[
\boxed{
w_j=\frac{r_j(m-r_j)}{mn}.}
\tag{10}
\]

Indeed, the only off-diagonal overlap between adjacent `n`-blocks occurs in the unique `m`-block cut by their common boundary, producing `-w_j` in (9), while the diagonal entries are the sums of incident conductances. The row sums vanish because the global constant vector belongs to both block-constant ranges.

For a weighted path, deletion of one row and column leaves determinant `\prod_jw_j` because the path has a unique spanning tree. Since a connected `m`-vertex Laplacian has one zero eigenvalue, its reduced determinant is `m` times any cofactor. Therefore

\[
\det{}'(I_m-R^*R)
=m\prod_{j=1}^{m-1}w_j.
\tag{11}
\]

Because multiplication by `n` permutes the nonzero residue classes modulo `m`, both `r_j` and `m-r_j` run through `1,\ldots,m-1`. Hence

\[
\prod_{j=1}^{m-1}r_j(m-r_j)=((m-1)!)^2,
\]

and

\[
\boxed{
\det{}'\Delta_{m,n}^{(mn)}
=\frac{((m-1)!)^2}{m^{m-2}n^{m-1}}.
}
\tag{12}
\]

For general `g=(m,n)`, write `m=ga`, `n=gb`. All interval overlaps are multiplied by `g`, while their normalization `\sqrt{mn}` is also multiplied by `g`. Thus the normalized overlap matrix is exactly that of the coprime pair `(a,b)`. Symmetrizing in the smaller and larger reduced degrees yields

\[
\boxed{
\det{}'\Delta_{m,n}^{(L)}
=\frac{((a-1)!)^2}{a^{a-2}b^{a-1}},
\quad
a=\min(m/g,n/g),\ b=\max(m/g,n/g).
}
\tag{13}
\]

Direct finite-matrix checks on `(2,3),(3,4),(3,5),(4,5),(4,6),(6,10)` give respectively

\[
\frac13,\ \frac1{12},\ \frac4{75},\ \frac9{500},\ \frac13,\ \frac4{75},
\tag{14}
\]

in agreement with (13). These checks are controls only; the claim rests on the exact derivation.

## 3. The least nontrivial reference cover gives an exact odd-degree logarithm

Take `m=2`. If `n` is odd, the reduced pair is `(2,n)`, and (13) gives

\[
\det{}'\Delta_{2,n}=rac1n.
\tag{15}
\]

If `n` is even, `P_n\le P_2`: the partitions are nested after the gcd reduction, the defect has only zero and unit eigenvalues, and

\[
\det{}'\Delta_{2,n}=1.
\tag{16}
\]

Therefore

\[
\boxed{
F(2,n)
=-\log\det{}'\Delta_{2,n}
=\mathbf1_{2\nmid n}\log n.
}
\tag{17}
\]

For odd `n`, the finite-cell defect has one nontrivial principal-angle eigenvalue `1/n`, one zero eigenvalue from the common constant mode, and `n-2` unit eigenvalues. The entire logarithmic response is thus concentrated in a **single positive principal angle**.

This is not a restatement of `WP-074`. There, `log n` is the trace of an inverse-scale cover cocycle built from the unbounded ladder `L`. Here, for odd degree, `log n` is a reduced log-determinant of two bounded noncommuting range projections. The equality is forced by interval overlap geometry.

It is nevertheless reference-cover relative. The least nontrivial cover `2` is distinguished only by degree ordering, and precisely that choice makes all even covers nested and therefore invisible. More generally, (13) depends on the reduced pair after removing the gcd, not on `n` alone.

For a fixed coprime reference `m<n`, (13) gives

\[
F(m,n)
=(m-1)\log n
+(m-2)\log m
-2\log((m-1)!),
\tag{18}
\]

so logarithmic degree is present, but with a reference-dependent slope and offset. Extracting a universal `log n` requires a normalization or differencing rule external to the positive defect.

## 4. Möbius primitivization returns the known parity-twisted Mangoldt shadow

Because (17) is an exact arithmetic function, one can ask whether the standard semigroup primitive repairs its even blind spot. Define

\[
M_2(n)
:=\sum_{d\mid n}\mu(n/d)F(2,d).
\tag{19}
\]

Since `F(2,d)=log d` on odd `d` and vanishes on even `d`, elementary Möbius inversion gives, for every `n>2`,

\[
\boxed{
M_2(n)
=\Lambda(n)-\mathbf1_{2\mid n}\Lambda(n/2).
}
\tag{20}
\]

At `n=2`, `M_2(2)=0` because both `F(2,1)` and `F(2,2)` vanish.

Thus the primitive support is

- `+log p` on odd prime powers `p^k`;
- `-log p` on twice an odd prime power;
- `0` on `2^k` and on the remaining composites;
- `0` at the exceptional level `2`.

For `n>2`, equation (20) is exactly **twice** the parity-twisted von Mangoldt law found independently in `PC-076` as the first Hardy/Hilbert relative trace. The two operators are different, so this is a useful cross-check rather than an identity of constructions. It also downgrades the arithmetic novelty: the noncommuting angle geometry reaches the same local parity shadow already exposed by a separate Hardy trace mechanism.

Most importantly, Möbius primitivization is signed. It does not preserve the operator positivity in (4), and it still does not produce the missing dyadic prime ray.

## 5. Pairwise positivity does not assemble into a positive degree kernel

A tempting next move is to use the nonnegative scalar `F(m,n)` itself as a kernel on cover degrees. This fails before any archimedean question.

First,

\[
F(m,m)=0
\tag{21}
\]

while, for example,

\[
F(2,3)=\log3>0.
\tag{22}
\]

A positive-semidefinite kernel with zero diagonal at an index has zero in the entire corresponding row by Cauchy--Schwarz. Hence `F` cannot be PSD.

Nor is `F` a conditionally negative distance kernel whose negative could become positive on a primitive/zero-sum subspace. On the degrees `(2,3,4,5)`, use the zero-sum coefficient vector

\[
c=(-2,0,1,1).
\]

From

\[
F(2,4)=0,
\qquad
F(2,5)=\log5,
\qquad
F(4,5)=\log(500/9),
\]

one obtains

\[
\boxed{
\sum_{i,j}c_ic_jF(n_i,n_j)
=2\log(20/9)>0.
}
\tag{23}
\]

But for the zero-sum vector supported on degrees `2` and `5`, `(1,0,0,-1)`,

\[
\sum_{i,j}c_ic_jF(n_i,n_j)
=-2\log5<0.
\tag{24}
\]

Therefore `F` is **indefinite even on the zero-sum subspace**. Neither sign supplies a Hodge/Schoenberg-style conditional sign theorem.

The exponentiated scalar does not help. Put

\[
G(m,n):=e^{-F(m,n)}=\det{}'\Delta_{m,n}.
\tag{25}
\]

Then

\[
G(2,2)=G(4,4)=G(2,4)=1
\]

because the `2`- and `4`-cover ranges are nested, but

\[
G(2,3)=\frac13,
\qquad
G(4,3)=\frac1{12}.
\]

If `G` were a PSD correlation kernel, equality `G(2,4)=\sqrt{G(2,2)G(4,4)}=1` would force the `2` and `4` Gram vectors to coincide and hence force equal correlations with degree `3`. They do not. Thus `G` is not PSD either.

The independent operator inequality `\Delta_{m,n}\succeq0` is therefore genuinely **pairwise/local**; taking its principal-angle determinant does not manufacture a positive quadratic pairing on the arithmetic degree labels.

## 6. On the full Hardy space the determinant is only a periodic density

The finite-cell restriction is not cosmetic. Since `L=lcm(m,n)` is divisible by both block sizes, the full Hardy space decomposes as

\[
\ell^2(\mathbb N_0)
=\bigoplus_{q\ge0}E_{q,L},
\qquad
E_{q,L}:=\operatorname{span}\{e_{qL},\ldots,e_{(q+1)L-1}\},
\tag{26}
\]

and the pair `(P_m,P_n)` restricts to the **same** finite pair on every cell. Consequently the full principal-angle defect is an infinite orthogonal sum of identical copies of (3).

In particular its common-range kernel contains one common mode per `L`-cell, equivalently the whole range of `P_L`, and every nontrivial principal-angle eigenvalue is repeated infinitely many times. For a nonnested pair with `F(m,n)>0`, the ordinary global reduced log-determinant therefore diverges:

\[
-\log\det{}'\Delta_{m,n}^{\rm full}=+\infty.
\tag{27}
\]

Equation (13) is a **per-period determinant density**. One may normalize by the number of periods, or place the construction in a periodic operator algebra, but that is an additional global readout; it does not turn the local positive block into a Weil quadratic form.

This is a structural difference from the target. The Weil functional is global in the test function and couples finite prime data to archimedean and polar counterterms. The angle determinant has only repeated finite cover combinatorics.

## 7. Matched controls and failure of the global completion test

Nothing in Sections 1--6 uses primality, prime powers, zeta zeros, the functional equation, or a special analytic property of the integers. The derivation uses only:

1. normalized degree-`n` block-cover isometries;
2. their range projections;
3. interval overlaps;
4. finite-dimensional Hilbert-space positivity.

The same formula holds in a matched model in which the degree labels are treated as generic positive integers with no prime interpretation. In particular `F(2,n)=log n` for **every odd integer**, not just prime powers. Prime-power support appears only after the signed Möbius operation (19), which immediately produces the parity-twisted negative controls in (20).

The construction also produces no intrinsic Gamma/digamma or polar contribution. The half-weight `n^{-1/2}` is present in the normalization of the cover isometry, but it cancels into the principal-angle overlap matrix and does not emerge as the critical Weil coefficient `Lambda(n)/sqrt(n)`. Reattaching that factor after the determinant would be a separate conductor weighting, not a consequence of (4).

Thus the route fails all three strongest global gates simultaneously:

```text
local operator sign:          yes, Delta_{m,n} >= 0
intrinsic logarithmic degree: yes, exactly on suitable relative covers
positive degree-space form:   no
prime-power support by sign:  no; requires signed Mobius primitive
archimedean/polar sector:     absent
full-space determinant:       divergent periodic repetition
```

It therefore does not evade `WP-043`'s broader warning about determinant positivity: an exact positive spectral/geometric determinant may contain logarithmic arithmetic data while living in the wrong pairing category.

## 8. Prior-art and novelty audit

The general ingredients are classical. Products of two orthogonal projections are governed by principal angles/canonical correlations of subspaces; finite partition conditional expectations are standard orthogonal projections; and the determinant of a weighted path Laplacian is the elementary path case of the weighted Matrix--Tree theorem. No novelty is claimed for any of those facts.

A directed search around principal angles of block-averaging/conditional-expectation projections, overlap matrices of interval partitions, and weighted path-Laplacian pseudodeterminants located the standard surrounding theories but no authoritative source for the exact consecutive-block specialization (13). Absence of that exact formula in a bounded search is not evidence of theorem-level novelty.

The durable Mathia contribution is narrower:

- inserting the exact pointed cover projections into principal-angle geometry;
- deriving the closed gcd-reduced determinant (13);
- identifying the canonical dyadic response (17);
- showing that its Möbius primitive lands on the already-known `PC-076` parity shadow; and
- proving by (23)--(25) that the scalar angle response cannot itself be the positive degree-space pairing sought by the Weil-positivity mandate.

This is therefore a **Mathia-specific classification and obstruction**, not a claim of a new general theorem about projections.

## 9. Exact falsification surface

The finding is falsified if any of the following fails under the `WP-073` cover normalization.

1. Equation (1) is not the range projection of `W_n`.
2. The `lcm(m,n)` cells fail to reduce both `P_m` and `P_n`.
3. The overlap representation (6)--(7) is incorrectly normalized.
4. In the coprime case, `I-R^*R` is not the weighted path Laplacian with conductances (10).
5. The residues `jn mod m` do not permute `1,...,m-1` when `(m,n)=1`.
6. The gcd scaling does not leave the normalized overlap matrix unchanged.
7. The dyadic specialization (17) or Möbius identity (20) fails.
8. Either explicit zero-sum calculation (23)--(24) has the wrong sign.
9. The infinite Hardy pair is not the orthogonal repetition of the finite `lcm` cell.

All of these are finite or elementary operator checks. No statement about zeta zeros is used to establish the sign or the obstruction.

## Research consequence

The first canonical noncommuting construction tested after `WP-084` is mathematically nontrivial:

\[
\boxed{
P_m,P_n\text{ noncommuting}
\to
P_m(I-P_n)P_m\succeq0
\to
\det{}'\Delta_{m,n}\text{ exactly computable}
\to
F(2,n)=\mathbf1_{2\nmid n}\log n.
}
\]

So noncommutativity **can** preserve a genuine independent geometric sign while exposing logarithmic degree. What it does not do is assemble that sign globally. The reduced log-determinant is periodic, reference-relative, nonlinear, non-PSD as a degree kernel, and archimedean-blind; Möbius extraction returns the known parity-twisted signed shadow rather than a new positive Weil form.

A viable continuation must therefore keep more of the **operator-valued cross-cover geometry before determinant/scalarization** and must couple it to a nonperiodic/global sector before asking for positivity. Merely taking principal-angle determinants or their scalar transforms is exhausted by the obstruction above.