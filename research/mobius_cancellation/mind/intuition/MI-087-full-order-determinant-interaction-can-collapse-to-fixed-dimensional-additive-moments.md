# MI-087 — Full-order determinant interaction can collapse to fixed-dimensional additive moments

**Evidence level:** exact algebraic synthesis from [MC-439](../../findings/MC-439-principal-minor-determinant-full-interaction-fixed-rank-collapse.md), sharpening the full-interaction gate in MC-437--MC-438.

A divisor statistic can have a genuinely nonzero full Boolean interaction and still fail to retain high-dimensional relational source data. MC-439 gives an exact determinant example. If `K` is an `r x r` matrix indexed by the prime factors of squarefree `n=p_1...p_r` and

`A(prod_(i in T) p_i)=det K[T]`,

then Möbius convolution extracts

`(mu*A)(n)=(-1)^r det(K-I_r)`.

So the determinant survives the top-interaction test that annihilates bounded-degree and additive local-chain statistics.

But if the kernel has fixed separable feature rank `d`, `K=UV^T`, Sylvester's identity reduces the same full-order interaction to

`(mu*A)(n)=(-1)^r det(I_d-V^T U)`.

Every entry of `V^T U` is just an additive feature moment over the prime factors, of the form `sum_i g_a(p_i) f_b(p_i)`. The apparently `r`-body determinant therefore factors through only `d^2` additive coordinates when `d` is fixed. Nonzero top Boolean degree is necessary for survival through divisor Möbius projection, but it is not a certificate of high-dimensional relational retention.

This closes a tempting nonadditive escape from MC-438. A determinant or principal-minor statistic becomes interesting only if its effective feature rank grows at a source-relevant rate, if the retained fixed-dimensional moments themselves provably carry the required discriminator, or if the kernel depends on the selected set in a way that cannot be represented as principal minors of one fixed low-rank pair kernel.

**Boundary.** The collapse is specific to principal-minor determinants of a fixed separable finite-rank kernel. MC-439 does not rule out growing-rank kernels, set-dependent matrices, other global nonlinear functionals or downstream operations different from divisor Möbius convolution. Nor does a surviving high-rank determinant by itself provide signed analytic cancellation.