# AF-195 — Minimal moment-flat stencils are exactly divided-difference controls

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-CONTROL`, `SOURCE-CLASS-CLASSIFICATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-182--AF-194 use the parity-split binomial cluster as a sharp matched control for bounded-band and Euler-harmonic fidelity. Those results deliberately did not claim that the parity family is extremal among arbitrary positive source pairs. There is nevertheless an exact source-class statement that removes one degree of arbitrariness: **once one fixes the smallest possible number of distinct nodes capable of cancelling all polynomial observables below order `m`, the signed control is forced by interpolation theory.** On an equally spaced stencil, the forced control is exactly the parity-split binomial family used in AF-182.

Let

\[
u_0<u_1<\cdots<u_m
\tag{1}
\]

be `m+1` distinct real nodes and define the barycentric/divided-difference weights

\[
\lambda_j
=
\frac{1}{\prod_{\ell\ne j}(u_j-u_\ell)},
\qquad 0\le j\le m.
\tag{2}
\]

Then:

1. for every polynomial `P` of degree `<m`,
   \[
   \boxed{
   \sum_{j=0}^m\lambda_j P(u_j)=0;
   }
   \tag{3}
   \]
2. for `P(u)=u^m`,
   \[
   \boxed{
   \sum_{j=0}^m\lambda_j u_j^m=1;
   }
   \tag{4}
   \]
3. if real coefficients `c_0,\ldots,c_m`, not all zero, satisfy
   \[
   \sum_{j=0}^m c_jP(u_j)=0
   \qquad
   \text{for every }P\in\mathcal P_{m-1},
   \tag{5}
   \]
   then there is a unique nonzero scalar `C` such that
   \[
   \boxed{c_j=C\lambda_j\quad(0\le j\le m);}
   \tag{6}
   \]
4. no nonzero signed measure supported on these `m+1` nodes can annihilate every polynomial of degree at most `m`.

Thus order `m` is the **maximum exact polynomial-cancellation order available to a nonzero signed control on `m+1` distinct fixed nodes**, and the control attaining that order is unique up to scale.

Because the nodes are ordered, the signs alternate:

\[
\operatorname{sgn}(\lambda_j)=(-1)^{m-j}.
\tag{7}
\]

Equation `(3)` at `P=1` shows that the total positive and negative masses agree. Writing

\[
A(u_0,\ldots,u_m)
=
\sum_{\lambda_j>0}\lambda_j
=
-\sum_{\lambda_j<0}\lambda_j
>0,
\tag{8}
\]

there is therefore a canonical mutually singular probability pair

\[
\mu_+
=
\frac1A\sum_{\lambda_j>0}\lambda_j\,\delta_{u_j},
\qquad
\mu_-
=
\frac1A\sum_{\lambda_j<0}(-\lambda_j)\,\delta_{u_j},
\tag{9}
\]

whose signed difference is

\[
\nu=\mu_+-\mu_-
=
\frac1A\sum_{j=0}^m\lambda_j\delta_{u_j}.
\tag{10}
\]

Up to swapping the two sides, `(9)` is the **unique mutually singular probability pair on the declared nodes whose moments agree through degree `m-1` and whose signed difference uses all `m+1` nodes**. Adding common mass to both measures is a representation redundancy and is excluded by the mutually singular/minimal-support formulation.

For every function `f` defined on the nodes,

\[
\boxed{
\sum_{j=0}^m\lambda_j f(u_j)
=f[u_0,\ldots,u_m],
}
\tag{11}
\]

where the right side is the classical `m`-th divided difference. Hence the observation discrepancy of the canonical pair is exactly

\[
\boxed{
\int f\,d(\mu_+-\mu_-)
=
\frac{f[u_0,\ldots,u_m]}{A(u_0,\ldots,u_m)}.
}
\tag{12}
\]

This identifies the minimal moment-flat matched control intrinsically: it is not merely *similar to* a finite difference; it is the normalized divided-difference functional determined by the source nodes.

## Equispaced specialization recovers AF-182 exactly

Take

\[
u_j=x+j\delta,
\qquad \delta>0.
\tag{13}
\]

Then

\[
\prod_{\ell\ne j}(u_j-u_\ell)
=
\delta^m(-1)^{m-j}j!(m-j)!,
\tag{14}
\]

so

\[
\lambda_j
=
\frac{(-1)^{m-j}}{\delta^m j!(m-j)!}
=
\frac{(-1)^{m-j}}{m!\delta^m}\binom mj.
\tag{15}
\]

The positive and negative halves of a binomial row each have total coefficient `2^{m-1}`, hence

\[
A
=
\frac{2^{m-1}}{m!\delta^m}.
\tag{16}
\]

Substituting `(15)`--`(16)` into `(10)` gives

\[
\boxed{
\mu_+-\mu_-
=
2^{1-m}
\sum_{j=0}^m
(-1)^{m-j}\binom mj\delta_{x+j\delta},
}
\tag{17}
\]

which is exactly the normalized parity-split control of AF-182 and its descendants.

Similarly, the classical relation between divided and forward differences gives

\[
f[x,x+\delta,\ldots,x+m\delta]
=
\frac{\Delta_\delta^m f(x)}{m!\delta^m},
\tag{18}
\]

and `(12)` becomes

\[
\boxed{
\int f\,d(\mu_+-\mu_-)
=
2^{1-m}\Delta_\delta^m f(x).
}
\tag{19}
\]

Therefore the finite-difference multiplier that drives AF-182--AF-194 is **forced** by three explicit source-class choices: `m+1` distinct equally spaced nodes, exact cancellation of every polynomial degree below `m`, and minimal/mutually singular positive realization. It is not forced if any of those resource declarations is removed.

For the Euler local logarithm

\[
F_s(u)=-\log(1-e^{-su}),
\qquad \Re s>0,
\tag{20}
\]

`(19)` immediately recovers the exact harmonic response

\[
\boxed{
\int F_s\,d(\mu_+-\mu_-)
=
2^{1-m}
\sum_{k\ge1}
\frac{e^{-ksx}}{k}
\left(e^{-ks\delta}-1\right)^m.
}
\tag{21}
\]

Hence AF-189--AF-194 do not describe an arbitrarily selected binomial witness inside this minimal equispaced moment-flat class: they describe the **only** normalized signed source difference in that class.

## Derivation

### 1. Lagrange interpolation gives the annihilator explicitly

Let `P` be any polynomial of degree at most `m`. Its Lagrange interpolation formula on the `m+1` nodes is exact:

\[
P(u)
=
\sum_{j=0}^m
P(u_j)
\prod_{\ell\ne j}
\frac{u-u_\ell}{u_j-u_\ell}.
\tag{22}
\]

The coefficient of `u^m` in the `j`-th Lagrange basis polynomial is precisely `\lambda_j`. Taking the coefficient of `u^m` on both sides of `(22)` yields

\[
[u^m]P
=
\sum_{j=0}^m\lambda_jP(u_j).
\tag{23}
\]

If `\deg P<m`, the left side is zero, proving `(3)`. If `P(u)=u^m`, it equals one, proving `(4)`. The same coefficient identity is the standard explicit formula for the highest divided difference, giving `(11)`.

### 2. Vandermonde rank proves uniqueness and maximality

Condition `(5)` is equivalent to the `m` equations

\[
\sum_{j=0}^m c_j u_j^r=0,
\qquad r=0,1,\ldots,m-1.
\tag{24}
\]

The `m\times(m+1)` truncated Vandermonde matrix in `(24)` has rank `m`: any `m` selected columns form a square Vandermonde matrix on distinct nodes and are invertible. Its kernel is therefore one-dimensional. Since `(3)` shows that `\lambda=(\lambda_0,\ldots,\lambda_m)` lies in that kernel and every `\lambda_j` is nonzero, `(6)` follows.

If cancellation were extended through degree `m`, the coefficient vector would lie in the kernel of the full `(m+1)\times(m+1)` Vandermonde matrix. Its determinant is

\[
\prod_{0\le i<j\le m}(u_j-u_i)\ne0,
\tag{25}
\]

so the only such vector is zero. This proves maximality of the cancellation order.

### 3. Ordered nodes force an alternating positive split

For ordered nodes, exactly `m-j` factors in the denominator of `(2)` are negative. This proves `(7)`. Since the constant polynomial is annihilated, `\sum_j\lambda_j=0`, so the positive and negative coefficient masses in `(8)` are equal.

Any mutually singular probability pair supported on the same nodes and matching all moments below degree `m` has a signed difference `c=(c_j)` satisfying `(24)`. By one-dimensionality, `c=C\lambda`. Mutual singularity fixes each node to the sign-compatible side, and probability normalization fixes `|C|=1/A`. The remaining sign corresponds only to swapping `\mu_+` and `\mu_-`.

This is the precise uniqueness statement. Without mutual singularity, one may add the same nonnegative common measure to both sides; that changes the pair representation while leaving the signed difference and every observation discrepancy unchanged.

## Source-class consequence for Arithmetic Fidelity

The parity controls used since AF-182 were introduced as explicit adversarial examples. AF-195 turns them into a **classification theorem at fixed minimal combinatorial complexity**.

If source complexity is measured by the number of distinct support nodes and the adversary is required to annihilate all polynomial observables through degree `m-1`, then:

- at least `m+1` distinct nodes are necessary for a nonzero signed control;
- with exactly `m+1` nodes, the signed control is unique up to scale and equals the divided-difference functional;
- on an arithmetic progression, positivity normalization forces exactly the AF-182 parity split;
- adding a further node changes the geometry qualitatively: the moment-annihilator kernel has dimension at least two, so the parity witness is no longer unique.

This supplies a real but deliberately narrow converse to the construction side of AF-182--AF-194. It shows that **cancellation order `m` cannot be achieved with fewer distinct nodes**, and that the existing witness exhausts the minimal equispaced class. It does **not** show that this class is minimax-optimal for a finite vertical band, for the Euler logarithm, or among arbitrary positive source pairs of comparable transport diameter.

The next genuinely stronger inverse-fidelity question is therefore no longer whether some different coefficient choice on the same minimal grid can beat the parity split; it cannot. The open source-class question is whether allowing nonuniform node placement, extra nodes, approximate rather than exact moment cancellation, or a different complexity budget can produce strictly smaller Euler-band discrepancy at the same declared source separation.

## Falsification and boundaries

The classification depends on the exact resource model.

- **Distinct fixed nodes matter.** Coalescing nodes lead to Hermite/confluent divided differences and a different multiplicity model.
- **Exact polynomial cancellation matters.** Approximate moment matching has a conditioning problem governed by singular values of a Vandermonde/moment map rather than a one-dimensional nullspace.
- **Minimal support matters.** With `N>m+1` nodes, the nullspace of the first `m` moment rows has dimension at least `N-m`, so uniqueness disappears.
- **Equispacing matters only for the binomial formula.** Arbitrary distinct nodes still have a unique minimal moment-flat control, but its weights are the barycentric coefficients `(2)`, not binomial coefficients.
- **Mutual singularity/minimal representation matters for uniqueness of the positive pair.** Common mass may be added to both sides without changing the signed control.
- **Maximal moment order is not minimax observation optimality.** A control that annihilates the largest polynomial space need not minimize a particular nonlinear or bandlimited observation norm when node positions themselves are free.
- **No rational-prime specificity follows.** The result is a source-geometry classification for generalized Euler-generator controls and applies equally to non-prime matched systems.

These boundaries prevent the theorem from being promoted into the still-open broad converse requested by the local frontier. Its useful role is to remove one false degree of freedom and isolate where a stronger counterexample or recovery theorem would actually have to differ from the AF-182 family.

## Prior art and novelty assessment

The mathematical core is classical interpolation and numerical differentiation.

- Carl de Boor, **“Divided Differences,”** *Surveys in Approximation Theory* 1 (2005), 46--69, arXiv:`math/0502036`, develops the standard univariate divided-difference calculus, including Lagrange/Newton representations and the Genocchi--Hermite viewpoint. The identity `(11)` and its polynomial-annihilation consequences belong to this classical theory.
- Bengt Fornberg, **“Generation of Finite Difference Formulas on Arbitrarily Spaced Grids,”** *Mathematics of Computation* 51(184) (1988), 699--706, DOI `10.1090/S0025-5718-1988-0935077-0`, develops finite-difference weights of prescribed derivative/order accuracy on arbitrary one-dimensional node sets. This is direct prior art for viewing moment conditions as a finite-difference weight problem rather than as a new coefficient construction.
- Ordinary Lagrange interpolation and Vandermonde unisolvence supply `(22)`--`(25)` directly; no novelty is claimed for the barycentric weights, moment identities, divided-difference formula, or minimal-node uniqueness.

A targeted prior-art audit found the entire interpolation-theoretic mechanism to be standard. The durable Arithmetic Fidelity content is therefore **not a new interpolation theorem**. It is the exact source-class interpretation relative to AF-182--AF-194: the positive parity-split Euler control is the unique normalized maximal-moment-cancellation difference on its minimal equispaced stencil, so any stronger minimax counterexample must spend a different resource (node placement, support cardinality, approximate cancellation, metric, or bandwidth) rather than merely retune the same coefficients.

## Dependencies and evidence boundary

- **AF-182:** defines the normalized parity-split positive Euler-generator controls, proves their lower-moment matching and exact `W_1=\delta`, and derives their finite-difference Euler response.
- **AF-186:** optimizes cancellation order for this family under a general derivative envelope but explicitly stops short of a converse theorem for the source class.
- **AF-189--AF-194:** determine increasingly sharp Euler-harmonic discrepancy laws for the same parity family in isolated, finite-overlap, and moving-saddle regimes; AF-194 explicitly leaves broad source-pair minimax optimality open.
- **This finding:** closes only the coefficient/support-minimality question. It does not establish a recovery modulus or an Euler-band minimax theorem over arbitrary node configurations.