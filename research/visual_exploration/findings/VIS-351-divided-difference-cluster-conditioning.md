# VIS-351 — divided-difference coordinates remove fixed-multiplicity phase-collision ill-conditioning

## Claim

Fix a finite real interval `I` with positive length and an integer `r>=0`. For real nodes

`mu_0,...,mu_r`

write

`phi_k^(mu)(x)=[mu_0,...,mu_k](lambda -> exp(-i lambda x))`, `0<=k<=r`,

where repeated nodes are interpreted by generalized divided differences. For every fixed cluster radius `rho>0` there is a constant

`kappa=kappa(I,r,rho)>0`

such that, for every real cluster center `b`, every node tuple satisfying

`|mu_j-b|<=rho`,

and every coefficient vector `u=(u_0,...,u_r)`,

`|| sum_(k=0)^r u_k phi_k^(mu) ||_(L^2(I)) >= kappa ||u||_2`.

Consequently,

`sup_(x in I) |sum_k u_k phi_k^(mu)(x)| >= kappa |I|^(-1/2) ||u||_2`.

The constant is uniform as any subset of the phases collide. In particular, raw exponential coefficients may diverge like inverse powers of phase gaps while the cluster-adapted divided-difference coordinates remain bounded and the represented function remains uniformly normed.

Applied to the confluent Wang tail from `VIS-349`--`VIS-350`, this gives a stricter accounting rule: **fixed-multiplicity phase coalescence is not by itself a genuine conditioning resource.** Before crediting a small reference norm `H_X` to phase collision, rewrite each bounded collision cluster in generalized divided-difference coordinates. Any actual collapse must then appear as small cluster-adapted coefficients, growing cluster multiplicity/radius, cancellation between distinct cluster subspaces, or degeneration in the map from the Wang moment data to those stable coordinates.

**Evidence/status:** `LITERATURE+DERIVED + CLASSICAL DIVIDED-DIFFERENCE CONDITIONING + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not give a global lower frame bound for an arbitrarily growing collection of clusters, nor does it bound the Wang moment-to-divided-difference coordinate map. It therefore narrows but does not close the norming problem left by `VIS-350`.

## 1. Translation removes the moving cluster center

Let

`nu_j=mu_j-b`.

Divided differences are linear in the sampled function, and

`exp(-i(b+nu)x)=exp(-ibx) exp(-inu x)`.

Therefore

`phi_k^(mu)(x)=exp(-ibx) phi_k^(nu)(x)`.

Multiplication by `exp(-ibx)` is unitary on `L^2(I)`, so all norming constants depend only on the relative nodes `nu_j`, not on the absolute translation `b`. The moving center of a Wang phase cluster is thus irrelevant to this local conditioning question.

## 2. Generalized divided differences stay regular through collisions

For the function of the spectral parameter

`f_x(lambda)=exp(-i lambda x)`,

generalized divided differences depend continuously on their nodes, including repeated-node limits. At complete confluence,

`mu_0=...=mu_k=b`,

one has

`phi_k(x)=f_x^(k)(b)/k! = (-i x)^k exp(-ibx)/k!`.

Hence the collision limit is the ordinary confluent exponential basis

`exp(-ibx), x exp(-ibx), ..., x^r exp(-ibx)`

up to nonzero constants. These functions are linearly independent on every interval of positive length.

More generally, the generalized divided differences

`phi_0^(mu),...,phi_r^(mu)`

are linearly independent for arbitrary real node tuples, with repeated nodes interpreted by multiplicity. This is classical divided-difference/Riesz-basis theory; it is not a Mathia novelty claim.

## 3. Compact Gram argument gives a uniform lower bound

After the translation reduction, the allowed parameter set is the compact cube

`K=[-rho,rho]^(r+1)`.

Let `G(mu)` be the `(r+1)x(r+1)` Gram matrix

`G_jk(mu)=int_I phi_j^(mu)(x) conj(phi_k^(mu)(x)) dx`.

Continuity of generalized divided differences implies continuity of every entry of `G(mu)` on `K`. Linear independence implies that `G(mu)` is positive definite for every `mu in K`; therefore its smallest eigenvalue is a positive continuous function on a compact set. Thus

`lambda_* = min_(mu in K) lambda_min(G(mu)) > 0`.

For

`F_mu(x)=sum_k u_k phi_k^(mu)(x)`,

one has

`||F_mu||_2^2 = u^* G(mu) u >= lambda_* ||u||_2^2`.

Taking `kappa=sqrt(lambda_*)` proves the stated uniform `L^2` inequality. Since

`||F_mu||_2 <= |I|^(1/2) sup_I |F_mu|`,

the `L^infinity` lower bound follows immediately.

The important point is not the existence of a new inequality but the coordinate choice: collision singularities in the raw exponential Vandermonde coordinates disappear in the generalized divided-difference basis.

## 4. Two-phase model makes the bookkeeping explicit

Take two phases `b` and `b+h` and

`F_h(x)=c_0 exp(-ibx)+c_1 exp(-i(b+h)x)`.

With

`phi_0(x)=exp(-ibx)`,
`phi_1(x)=[exp(-i(b+h)x)-exp(-ibx)]/h`,

write

`u_0=c_0+c_1`,
`u_1=h c_1`.

Then exactly

`F_h=u_0 phi_0+u_1 phi_1`.

As `h->0`,

`phi_1(x)->-i x exp(-ibx)`

uniformly on `I`. A finite derivative mode therefore has raw coefficients `c_1=u_1/h` and `c_0=u_0-u_1/h`, which may diverge like `1/h`, while `(u_0,u_1)` and the function norm stay finite and uniformly controlled.

So a large raw coefficient norm near a phase collision is not automatically a cost paid by the mechanism. It may be only the singular coordinate representation of an ordinary confluent derivative mode. Conversely, making the function genuinely small requires the stable divided-difference coordinates themselves, or their interaction with other clusters, to become small.

## 5. Consequence for the Wang norming problem

`VIS-350` leaves the ratio

`H_X/D_(q,X)`

as the unresolved conditioning channel for

`E_(q,X)(xi)=sum_b exp(-ib xi) Q_(b,q,X)(xi)`.

The present result changes how one should audit that ratio. If several active phases approach one another while the collision multiplicity stays bounded, do not compare `H_X` directly with raw exponential coefficients or a Vandermonde-conditioned coefficient vector. First replace each collision cluster by generalized divided differences. For fixed cluster multiplicity and bounded cluster diameter, the coefficient-to-function map inside the cluster has a uniform lower norming constant on the chosen reference interval.

Thus a proposed finite-bank gain cannot be justified merely by saying that phases coalesce and the raw coefficient system becomes ill-conditioned. After quotienting that coordinate artifact, at least one genuine resource must remain:

- the cluster-adapted Wang coefficient vector itself becomes small relative to the source/moment data;
- cluster multiplicity or cluster diameter leaves the fixed compact regime;
- several separated cluster subspaces cancel on the reference interval;
- the number of clusters/effective dimension grows;
- or the map from the original scale/translation moments into divided-difference coordinates becomes singular in a way that carries the claimed power of `X`.

The last two bullets are real quantitative questions. The first raw-Vandermonde blow-up is not.

## Prior-art audit

S. A. Avdonin and S. A. Ivanov, **Exponential Riesz bases of subspaces and divided differences**, *St. Petersburg Mathematical Journal* 13 (2001), 339--351; arXiv `math/0103160`, develops generalized divided differences for exponential families with colliding spectral points. Their Theorem 2 records continuity in the nodes, linear independence, basis behavior for distinct nodes, translation covariance, and uniform basis behavior for clustered points. In particular, their framework explicitly treats divided differences as the natural stable coordinates when ordinary exponentials cease to be uniformly minimal under collisions.

S. Avdonin and W. Moran, **Ingham-type inequalities and Riesz bases of divided differences**, *International Journal of Applied Mathematics and Computer Science* 11:4 (2001), 803--820, gives the corresponding Ingham/Riesz-basis theory for exponential divided differences under clustered nonharmonic spectra.

No new divided-difference or Riesz-basis theorem is claimed. The Mathia-specific consequence is the accounting correction for `VIS-350`: raw coefficient explosion caused solely by bounded phase collision is a coordinate artifact and should be removed before measuring whether a Wang tail has genuinely purchased a small reference norm.

## Dependencies

- `VIS-349`: exact reduction of the first `q` interacting Wang tail orders to a confluent exponential polynomial.
- `VIS-350`: measurable Turan--Nazarov propagation by total multiplicity and isolation of the remaining reference-norm/conditioning problem.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed here.

## Research consequence

The finite-bank conditioning question is now smaller. Fixed-multiplicity phase collision does not by itself explain a small Wang reference norm once the cluster is expressed in generalized divided-difference coordinates. Future finite-bank work should measure the map from Wang moment data to these stable cluster coordinates and then the interaction among distinct clusters, rather than treating raw confluent-Vandermonde coefficient blow-up as an independent smoothing resource.

A genuinely surviving escape must therefore exhibit a scale-dependent loss in the **cluster-adapted** norming map, growing effective multiplicity/cluster complexity, inter-cluster cancellation, or source/frequency dependence beyond the finite scalar bank.