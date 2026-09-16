# AF-382 — Adjacent prime-ratio minors determine order-two translation total nonnegativity

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF2` · `LOG-CONCAVITY` · `PRIME-LOGS` · `LOCAL-TO-GLOBAL` · `CLASSICAL-ADJACENT` · `NO-NOVELTY-CLAIM`

## Claim

At determinant order two, the prime-ratio certificate of AF-381 can be compressed much further without losing the target. For a strictly positive continuous translation profile, it is enough to test only **nearest-neighbor rectangles in the ordered prime sequence**.

Let

\[
e_n=\log p_n,
\]

where `p_n` is the `n`-th prime, and let `f:\mathbb R\to(0,\infty)` be continuous. For any fixed `N`, the following are equivalent:

1. the translation kernel
   \[
   K_f(u,x)=f(u-x)
   \]
   is totally nonnegative of order two on `\mathbb R\times\mathbb R`;
2. every adjacent prime-log rectangle in the tail has nonnegative determinant,
   \[
   \det
   \begin{pmatrix}
   f(e_i-e_j) & f(e_i-e_{j+1})\\
   f(e_{i+1}-e_j) & f(e_{i+1}-e_{j+1})
   \end{pmatrix}
   \ge0
   \qquad(i,j\ge N).
   \tag{1}
   \]

Equivalently, writing `p^+` and `q^+` for the successor primes of `p` and `q`, eventual validity of

\[
f\!\left(\log\frac pq\right)
 f\!\left(\log\frac{p^+}{q^+}\right)
\ge
f\!\left(\log\frac p{q^+}\right)
 f\!\left(\log\frac{p^+}{q}\right)
\tag{2}
\]

for all sufficiently large prime pairs `p,q` already forces every real order-two translation minor to be nonnegative.

Since a strictly positive continuous profile is `PF_2` exactly when it is log-concave, `(1)` is also an arithmetic sampling characterization of global log-concavity:

\[
\log f\text{ is concave on }\mathbb R
\quad\Longleftrightarrow\quad
\text{all sufficiently far-out adjacent prime rectangles satisfy }(1).
\tag{3}
\]

Thus order-two target fidelity does **not** require all prime pairs from AF-381. A two-index nearest-neighbor family already determines the full four-location inequality. The mechanism is not special to primes: it is discrete supermodularity plus vanishing sampling mesh.

## Local-to-global proof on the sampled grid

The forward implication is immediate. Assume conversely that `(1)` holds. Set

\[
A_{ij}=f(e_i-e_j)>0,
\qquad
B_{ij}=\log A_{ij}.
\tag{4}
\]

Because all entries are positive, `(1)` is equivalent to

\[
B_{ij}+B_{i+1,j+1}
\ge
B_{i,j+1}+B_{i+1,j}
\qquad(i,j\ge N).
\tag{5}
\]

This is the local supermodular, or inverse-Monge, inequality for the logarithmic sampled array. Define its elementary mixed difference

\[
\delta_{ij}
:=B_{ij}+B_{i+1,j+1}-B_{i,j+1}-B_{i+1,j}.
\tag{6}
\]

For arbitrary tail indices

\[
N\le i<i',
\qquad
N\le j<j',
\]

telescoping over the rectangle gives the exact identity

\[
B_{ij}+B_{i'j'}-B_{ij'}-B_{i'j}
=
\sum_{r=i}^{i'-1}\sum_{s=j}^{j'-1}\delta_{rs}.
\tag{7}
\]

Every summand is nonnegative by `(5)`, hence

\[
B_{ij}+B_{i'j'}\ge B_{ij'}+B_{i'j}.
\tag{8}
\]

Exponentiating yields

\[
A_{ij}A_{i'j'}\ge A_{ij'}A_{i'j},
\tag{9}
\]

which is precisely nonnegativity of **every** sampled `2\times2` minor using arbitrary prime-log rows and columns in the tail.

So nearest-neighbor rectangles are not merely a heuristic local proxy. For positive sampled matrices they generate every order-two rectangle inequality exactly by additive telescoping after taking logarithms. This is the familiar local-recognition mechanism for Monge/supermodular arrays, specialized here to multiplicative determinant inequalities.

## Vanishing prime-log mesh closes the remaining continuum gap

It remains to pass from arbitrary tail prime-log minors to arbitrary real translation minors. The prime number theorem gives

\[
e_{n+1}-e_n
=
\log\frac{p_{n+1}}{p_n}
\longrightarrow0.
\tag{10}
\]

Deleting finitely many samples does not change this property. Therefore the tail

\[
E_N=\{e_n:n\ge N\}
\]

has vanishing mesh at infinity.

Fix arbitrary real rows and columns

\[
a_1<a_2,
\qquad
b_1<b_2.
\]

Translate the four target locations by a common large `T`. Because the tail mesh tends to zero, choose prime-log samples

\[
u_1<u_2,
\qquad
x_1<x_2,
\qquad
u_i,x_j\in E_N,
\]

so that, after the common translation is removed,

\[
u_i-x_j\to a_i-b_j
\qquad(i,j\in\{1,2\}).
\tag{11}
\]

Equation `(9)` says the sampled determinant is nonnegative. Continuity of `f` and of the determinant lets the samples tend to the target configuration, giving

\[
\det\bigl(f(a_i-b_j)\bigr)_{i,j=1}^2\ge0.
\tag{12}
\]

The target rows and columns were arbitrary, so `K_f` is globally `TN_2`.

This is the order-two specialization of the joint-pattern closure mechanism in AF-381, but with a genuine compression before closure: AF-381 assumes all sampled order-two rectangles; AF-382 shows that positivity of the sampled profile lets those rectangles themselves be reconstructed from only adjacent ones.

## Log-concavity equivalence

The global target in `(12)` has the standard one-dimensional description. Put

\[
g=\log f.
\]

For any `t\in\mathbb R` and `h,k>0`, an order-two translation determinant has the sign of

\[
g(t)+g(t+h-k)-g(t-k)-g(t+h).
\tag{13}
\]

If `g` is concave, its increments over a fixed positive step decrease with the base point, so `(13)` is nonnegative. Conversely, taking `h=k` in `(13)` gives midpoint concavity,

\[
2g(t)\ge g(t-h)+g(t+h),
\tag{14}
\]

and continuity upgrades midpoint concavity to ordinary concavity. Hence

\[
K_f\in TN_2
\quad\Longleftrightarrow\quad
f\text{ is log-concave}
\tag{15}
\]

for strictly positive continuous `f`.

Combining `(1)`--`(15)` yields `(3)`: eventual adjacent-prime inequalities characterize a global analytic shape constraint even though no finite interval of primes is privileged and no arbitrary prime tuple is tested directly.

## Fidelity interpretation

AF-372 showed that no fixed determinant order can certify the all-order Pólya-frequency target on the unrestricted class. AF-381 then showed that, at each retained order, all prime-ratio minors are topologically target-complete because prime logarithms have vanishing mesh.

AF-382 identifies a second, independent compression axis. **Within order two, location arity can collapse from arbitrary rectangles to nearest-neighbor rectangles without losing target fidelity.** The retained resource is the local mixed increment `(6)`. Positivity makes multiplication additive under `log`, and rectangle inequalities then compose by exact telescoping.

This matters for the line's broader compression question because it separates two kinds of apparent complexity:

- unbounded determinant order is genuinely load-bearing for the unrestricted `PF_\infty` target, by AF-372;
- at fixed order two, the huge family of spatial placements is highly redundant: a local generating family determines all placements.

So "many inequalities" is again the wrong information measure. The relevant question is whether the retained inequalities generate the target relations under operations intrinsic to the category. At order two they do; across determinant orders they do not.

The arithmetic labels still do not create arithmetic discrimination. Any increasing unbounded sampling sequence with vanishing tail mesh satisfies the same theorem. Rational primes supply one such sequence through `(10)`, but composites, suitable generalized-prime systems, or nonarithmetic meshes with the same closure property can carry the identical order-two certificate. Prime specificity would have to enter in a mechanism that proves `(1)` or in additional source structure, not in the determining power of the sampling grid itself.

## Riemann-facing consequence

The Schoenberg/Gröchenig route reviewed in AF-371 requires all-order Pólya-frequency structure for the reciprocal transform attached to `Xi`; order two is only one necessary layer. AF-382 therefore gives no evidence for RH and does not weaken AF-372's unbounded-arity obstruction.

It does sharpen what an arithmetic route would have to provide at its first nontrivial total-positivity layer. If the relevant transform profile is known independently to be strictly positive and continuous, then establishing the successor-prime inequalities `(2)` eventually is already enough to settle **every** order-two inequality and hence global log-concavity. Proving arbitrary order-two prime-ratio minors separately would add no target information.

The next structural question is therefore not whether more order-two placements should be retained, but whether higher-order total positivity admits comparably small generating families under assumptions that are actually available for the RH-facing profile. Classical strict-TP recognition by contiguous minors suggests a neighboring mechanism, but nonnegative all-order Pólya-frequency structure has zero-pattern and closure issues that prevent importing the strict finite-matrix criterion without a separate audit.

## Prior-art and novelty audit

- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968). Role: classical reference for Pólya-frequency functions, total positivity of translation kernels, and the `PF_2`/log-concavity framework.
- I. J. Schoenberg, **“On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms,”** *Journal d'Analyse Mathématique* **1** (1951), 331–374, DOI `10.1007/BF02790092`. Role: foundational translation-total-positivity and Pólya-frequency theory underlying the target class.
- Rainer E. Burkard, Bettina Klinz and Rüdiger Rudolf, **“Perspectives of Monge Properties in Optimization,”** *Discrete Applied Mathematics* **70**(2) (1996), 95–161, DOI `10.1016/0166-218X(95)00103-X`. Role: standard Monge-array recognition background; local adjacent quadrangle inequalities generate global rectangle inequalities by telescoping.
- Shaun M. Fallat and Charles R. Johnson, ***Totally Nonnegative Matrices***, Princeton University Press (2011), Chapter 3. Role: modern matrix reference for contiguous/initial-minor recognition of total positivity and the broader fact that structured families of local minors can generate global positivity constraints.

The `PF_2`/log-concavity equivalence and local-to-global Monge telescoping are classical. No novelty is claimed for either. A focused search did not identify a published theorem stated specifically as the eventual successor-prime criterion `(2)` for a continuous translation profile. That arithmetic specialization is an elementary composition of classical local Monge recognition with the prime-log determining mechanism already established in AF-381, so no standalone novelty claim is warranted.

The durable Arithmetic Fidelity result is the **certificate-compression boundary**: after two-sided prime sampling has already become target-complete, order-two positivity needs only local successor relations, whereas the all-order target still provably requires unbounded relational arity on the unrestricted class.

## Boundaries and falsification checks

Strict positivity of `f` is part of the theorem, not cosmetic. The proof uses `B_{ij}=\log A_{ij}` to turn multiplicative minor inequalities into additive mixed differences. With zeros, adjacent nonnegative minors do not generically determine all nonadjacent minors for arbitrary matrices, and an extension would need explicit support/zero-pattern hypotheses appropriate to translation kernels.

Continuity is used only in the final passage from the prime-log grid to the real translation kernel. The discrete statement `(1) => (9)` on the sampled positive matrix is exact and needs no regularity of `f` beyond positivity at the sampled points.

Vanishing tail mesh is a sufficient closure resource, not a claim of necessity. Analytic source rigidity can make a sparser set determining even when geometric pattern closure fails, as the earlier Ganzburg-based findings already show.

The theorem is only order two. It must not be extrapolated to `PF_\infty`: AF-372 supplies exact kernels in `TN_r\setminus TN_{r+1}` for every finite `r`, so no argument that controls merely the adjacent `2\times2` layer can certify the all-order target without additional source-specific structure.

Finally, the prime specialization is a matched-control warning as much as a positive reduction. If a non-prime sampling sequence has the same vanishing-mesh property, the identical local-to-global theorem applies. Any claim that `(2)` is intrinsically arithmetic must therefore identify extra structure in how those inequalities are proved, not merely point to the occurrence of prime symbols in them.