# VIS-355 — source-adaptive selection cannot evade a compact Wang moment floor

## Claim

Fix an asymptotic depth `q>=1`, a finite set of translation fibers `b`, and fixed scale counts `n_b`. For each fiber let

`x_(b,j)=a_(b,j)^(-1)`

be the inverse scales, and let

`V_b=(x_(b,j)^k)_(1<=k<=q,1<=j<=n_b)`.

Let `D_beta=diag(beta_1,...,beta_q)` be the fixed invertible Wang tail-coefficient matrix from `VIS-354`, and define the block moment map

`T_theta = direct_sum_b (D_beta V_b(theta))`,

where `theta` denotes the scale geometry.

Assume the geometry stays in a fixed compact nondegenerate family:

- `r <= x_(b,j) <= R` for fixed `0<r<R<infinity`;
- distinct inverse scales in the same fiber satisfy `|x_(b,j)-x_(b,l)|>=eta>0`;
- the numbers of fibers and active scales are fixed.

Then there is a constant `sigma>0`, depending only on this compact family and `q`, such that for every admissible `theta` and every coefficient vector `c`,

`||T_theta c||_2 >= sigma dist(c, ker T_theta)`.

Equivalently, the smallest **nonzero** singular value of the block Wang moment map has a uniform positive lower bound throughout the compact family.

This remains true if the bank is selected adaptively from the arithmetic source. For arbitrary source-dependent choices

`theta=theta(G)`, `c=c(G)`

that remain inside the same admissible compact family,

`||T_(theta(G)) c(G)||_2 >= sigma dist(c(G), ker T_(theta(G)))`

holds pointwise for every source realization `G` for which the selector is defined.

Therefore **source dependence of the selection rule alone cannot create an additional asymptotic Wang tail-coefficient gain inside a uniformly conditioned bounded family**. Any small coefficient vector must be paid for by one of the already visible resources:

- approach to the source-free moment-cancellation kernel;
- collision or escape of the inverse-scale geometry;
- growing scale count or tail depth;
- or a genuinely different source estimate entering outside this coefficient map.

If every `n_b<=q`, then `ker T_theta={0}` and the statement simplifies to

`||T_theta c||_2 >= sigma ||c||_2`

uniformly, even when `theta` and `c` are chosen from `G`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL SINGULAR-VALUE/PSEUDOINVERSE COMPACTNESS + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding does not rule out source-dependent banks whose geometry degenerates or grows with the asymptotic parameter, nonlinear operations on the source itself, infinite representations, or genuinely signed estimates for `G`. It only removes **adaptive selection inside the already-compact finite-bank class** as an independent resource.

## 1. Constant rank of the truncated moment map

For one fiber `b`, the matrix

`V_b=(x_j^k)`

has rank `min(q,n_b)` whenever the active inverse scales are distinct and nonzero.

If `n_b<=q`, the first `n_b` rows give the square determinant

`(prod_j x_j) prod_(j<l)(x_l-x_j)`,

which is nonzero. Hence `V_b` has full column rank.

If `n_b>q`, every `q` chosen columns form the same nonzero truncated Vandermonde minor, so `rank V_b=q`.

Multiplication by the fixed invertible diagonal matrix `D_beta` does not change rank or kernel. Thus every block has constant rank throughout the admissible parameter family, and the direct sum `T_theta` also has constant rank.

Its kernel is exactly the source-free scale-moment cancellation space already identified in `VIS-343` and `VIS-354`:

`sum_j c_(b,j) a_(b,j)^(-k)=0`, `k=1,...,q`,

fiber by fiber.

## 2. Compactness gives a uniform quotient lower bound

For a finite matrix `A`, singular-value decomposition gives

`||A c||_2 >= s_+(A) dist(c,ker A)`,

where `s_+(A)` is the smallest nonzero singular value.

The admissible ordered inverse-scale configurations form a compact set because they lie in `[r,R]` and obey the closed separation inequalities. Matrix entries depend continuously on the inverse scales, hence all singular values are continuous functions of the geometry.

Because the rank is constant, `s_+(T_theta)` never reaches zero on this compact set. Therefore

`sigma = min_theta s_+(T_theta) > 0`,

which proves

`||T_theta c||_2 >= sigma dist(c,ker T_theta)`

uniformly.

The quotient formulation is important when `n_b>q`: exact or approximate moment cancellation is not hidden conditioning. It is precisely motion into or toward the known kernel. After quotienting that kernel, there is no remaining compact-family coefficient collapse.

## 3. Source-adaptive choice does not alter a pointwise uniform inequality

Now allow the arithmetic source to choose the bank:

`G -> (theta(G),c(G))`.

No probabilistic, continuity, or measurability assumption on the selector is needed for the deterministic inequality itself. For each fixed `G`, the chosen pair is simply one admissible point of the same compact family, so the already-proved uniform estimate applies:

`||T_(theta(G)) c(G)||_2`
` >= sigma dist(c(G),ker T_(theta(G)))`.

Thus adaptive selection cannot manufacture a small Wang tail vector while staying a fixed positive distance from the classical moment-null space. The source may decide **which** admissible bank to use, but it cannot change the worst-case lower singular value of the admissible family.

This separates two very different notions of source dependence:

1. **selection dependence:** use `G` only to choose a member of a uniformly conditioned filter family;
2. **analytic dependence:** prove a new signed/quantitative property of `G`, or let the allowed geometry/dimension degenerate or grow in a way whose cost is itself controlled arithmetically.

Only the second can introduce a genuinely new asymptotic resource after the compact family has been uniformly quotiented.

## 4. Relation to the downstream phase geometry

`VIS-355` concerns the upstream map from bank weights to raw Wang tail polynomial coefficients. The next map sends those coefficients to the confluent exponential polynomial in log-frequency.

`VIS-351`--`VIS-353` already show that, after using stable divided-difference coordinates, a fixed bounded family of phase clusters has a uniform lower Riesz floor once every explicit collision scale has been charged. Consequently, if both the scale geometry here and the downstream phase geometry remain in their respective compact nondegenerate regimes, composing the two maps cannot create a new power gain merely because the choice of bank depends on `G`.

If a source-dependent selector drives a phase collision scale to zero, expands the spectral span, increases multiplicity/count, shrinks the working window, or otherwise leaves those compact assumptions, that degeneration is an explicit resource and must be priced by the earlier Wang ledger. The word “adaptive” does not make its cost disappear.

## 5. What remains genuinely open

This result closes only the weakest interpretation of the clue's source-dependent escape: **bounded adaptive choice among already-admissible finite filters**.

A live source-coupled mechanism must now do something stronger, for example:

- choose a geometry whose dimension, range, collision hierarchy, or phase complexity grows with the asymptotic parameter and prove that the growth cost is favorable;
- use coefficients depending on signed arithmetic information in a way that yields a new estimate for `G` rather than merely selecting a near-null filter;
- act nonlinearly on the source;
- use an infinite representation with controlled truncation and convergence;
- or prove direct cancellation of the actual source that survives the destination derivative repayment.

In each case the mathematical content lies in the new source estimate or escaping resource, not in source-adaptive selection by itself.

## Prior-art audit

The quotient inequality is standard finite-dimensional linear algebra. It is the singular-value/Moore--Penrose pseudoinverse statement that a matrix is bounded below on the orthogonal complement of its kernel; continuity on constant-rank matrix families gives uniform conditioning on compact parameter sets. A standard reference is Adi Ben-Israel and Thomas N. E. Greville, **Generalized Inverses: Theory and Applications**, 2nd ed., Springer, 2003, DOI `10.1007/b97366`.

The scale-moment specialization is already bounded by the prior-art audit in `VIS-343`/`VIS-354`, including Richardson/Vandermonde cancellation. The downstream clustered exponential stability is already bounded by `VIS-351`--`VIS-353`, including Avdonin--Ivanov and Avdonin--Moran on exponential divided differences and Riesz/Ingham inequalities.

No novelty is claimed for singular values, pseudoinverses, compactness, adaptive parameter selection, Vandermonde matrices, or Riesz lower bounds. The Mathia-specific content is the bookkeeping consequence for the current Wang frontier: **allowing the arithmetic source to choose a bank does not reopen a uniformly conditioned compact finite-bank mechanism**.

## Dependencies

- `VIS-343`: finite scale banks and the inverse-scale Vandermonde cancellation ceiling.
- `VIS-351`--`VIS-353`: stable phase-collision coordinates and bounded separated-block lower floors.
- `VIS-354`: exact source-free block Vandermonde map from weights to Wang tail coefficients.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose source-dependent branch is narrowed here.

## Research consequence

The accepted Wang clue can be narrowed again. Merely letting `G` choose coefficients, scales, or translations from a fixed compact nondegenerate finite family does **not** supply a new asymptotic cancellation resource: the same uniform quotient lower bound holds pointwise after selection.

Future work should not credit “adaptivity” unless it identifies and quantifies what actually leaves the compact ledger. A meaningful continuation must exhibit growing/degenerating geometry, infinite complexity, or a genuinely new signed property of `G` that survives the unchanged Wang destination audit.