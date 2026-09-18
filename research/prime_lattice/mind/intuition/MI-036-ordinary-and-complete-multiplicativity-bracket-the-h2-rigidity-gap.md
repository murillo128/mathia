# MI-036 — Ordinary and complete multiplicativity bracket the native H2 rigidity gap

**Evidence level:** exact synthesis from [PL-357](../../findings/PL-357-complete-multiplicativity-collapses-to-bohr-kernels.md) and [PL-358](../../findings/PL-358-ordinary-multiplicativity-local-zero-programmability.md), within the standard Hardy space of Dirichlet series `mathscr H^2`.

There are two canonical multiplicative completions of the coefficient law, and they fail in opposite directions.

Under **complete multiplicativity**, `a_(mn)=a_m a_n` for all `m,n`, square summability forces the prime coordinates `alpha_p=a_p` into `D^infinity cap l2`. The Bohr lift factorizes as

`BF(z)=prod_p (1-alpha_p z_p)^(-1)`,

which is exactly the product Szegő reproducing kernel at the point `bar alpha`. Equivalently, the coefficient vector is a simultaneous eigenvector of every backward prime shift. In the native evaluation region `Re s>1/2`, Cauchy--Schwarz gives absolute convergence and the Euler product is finite and nonzero. Complete multiplicativity therefore removes zero-set flexibility by collapsing the whole family to zero-free kernel vectors.

Under **ordinary multiplicativity**, only coprime products are coupled. The prime-power strings remain free:

`f_p(z)=sum_(k>=0) a_(p^k) z^k`,

and the Bohr lift is the restricted tensor product `prod_p f_p(z_p)`. In `Re s>1/2`, every zero is exactly a zero of one local factor. PL-358 makes the freedom quantitative: for any prescribed `s_0` with `1/2<Re s_0<1`, one can choose a bounded finite polynomial in the `p=2` coordinate that vanishes at `2^(-s_0)`, keep all other prime directions active with square-summable coefficients, and obtain a multiplicative `mathscr H^2` series with `|a_n|<=1` and `F(s_0)=0`.

So the useful intermediate law cannot be “multiplicativity” in either naive sense. Ordinary multiplicativity is too local: a single prime-power factor can program an arbitrary native critical-strip zero. Complete multiplicativity is too rigid: it forces every local factor to be geometric and destroys native zeros altogether.

The surviving target is an **infinite relation among prime-power strings that is genuinely cross-degree or cross-prime**. It must prevent one-coordinate zero planting without reducing all local factors to `(1-alpha_p z)^(-1)`. Completion/functional-equation coupling, target-relative Nyman/Weil constraints, or another global relation are plausible categories only insofar as they survive the declared `H^2`/destination topology and remain nontrivial.

**Boundary.** This is a classification inside the native `mathscr H^2` evaluation half-plane. It says nothing about zeros created or removed by a separately supplied meromorphic continuation, and it does not classify all intermediate nonlinear source laws. The result only brackets two canonical endpoints sharply enough that a future proposal must state what couples the prime-power strings beyond ordinary multiplicativity and why that coupling does not collapse to the reproducing-kernel manifold.