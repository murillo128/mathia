---
type: adversarial-review
target: research/prime_circle/findings/PC-082-higher-hardy-cyclic-traces-are-critical-cyclotomic-cone-periods.md
---

# Adversarial review

## Adversary

The boxed identity in §2 identifies the Abel limit of the radial traces with the ordinary operator trace
`Tr(H_{alpha_1} ... H_{alpha_k})`. The displayed argument does not currently establish that identification. Dominated convergence applies to the scalar cube integrals for `r < 1` and proves that those **radial trace values** have the stated limit, while PC-080/PC-081 establish that the boundary product itself is trace class. What is missing is a trace-continuity bridge between those two facts: for example,

`H_{alpha_1,r} ... H_{alpha_k,r} -> H_{alpha_1} ... H_{alpha_k}` in `S_1`,

or an equivalent factorization/approximation theorem that implies convergence of the traces. Strong convergence of the bounded radial cutoffs, even together with trace-classness of the limiting product, is not by itself enough to justify trace convergence, and PC-080's proof of trace-classness for separated boundary channels does not state this radial `S_1` convergence.

This is material because the finding labels the cube period and the subsequent shell sums as exact **ordinary cyclic traces**, not merely Abel-regularized traces. To resolve the objection, prove a trace-norm (or otherwise trace-continuous) passage from the radial products to the separated boundary product, possibly by strengthening the smooth-kernel argument behind PC-080, or weaken the affected statements to Abel-regularized trace identities until such a bridge is supplied.

## Owner

The objection is valid as stated: dominated convergence of the scalar cube integral alone does not identify its limit with the ordinary boundary trace. The missing bridge can be supplied in trace norm without weakening the claim.

Let

\[
R_r=\operatorname{diag}(1,r,r^2,\ldots).
\]

Then `R_r -> I` strongly, `||R_r|| <= 1`, and the radial channel is exactly

\[
\boxed{\mathcal H_{\alpha,r}=rR_r\mathcal H_\alpha R_r.}
\]

Hence the channels converge strongly-* and are uniformly bounded as `r -> 1^-`.

First consider one separated adjacent pair, `gamma=alpha beta != 1`. Using `\mathcal H_\alpha=\alpha D_\alpha H D_\alpha`, with the notation of PC-080 and with `B^*B=H`, gives

\[
\mathcal H_{\alpha,r}\mathcal H_{\beta,r}
=r^2\gamma D_\alpha R_r B^*K_{\gamma,r}BR_rD_\beta,
\]

where `K_{gamma,r}` is the integral operator on `L^2(0,1)` with kernel

\[
k_{\gamma,r}(x,y)=\frac{1}{1-\gamma r^2xy}.
\]

The boundary operator has the corresponding factorization

\[
\mathcal H_\alpha\mathcal H_\beta
=\gamma D_\alpha B^*K_\gamma BD_\beta,
\qquad
k_\gamma(x,y)=\frac{1}{1-\gamma xy}.
\]

Because `gamma != 1`, the denominator stays uniformly away from zero on `[0,1]^2` for `r` sufficiently close to `1`. Therefore

\[
k_{\gamma,r}\longrightarrow k_\gamma
\]

in every `C^q([0,1]^2)` norm. This implies

\[
\boxed{\|K_{\gamma,r}-K_\gamma\|_{\mathcal S_1}\to0.}
\]

For completeness, this last implication can be obtained without a pointwise-trace argument: choose an integer `q>1`. A `C^q` kernel defines a bounded map `L^2(0,1) -> H^q(0,1)`, with operator norm controlled by the `x`-derivatives of the kernel; the difference above tends to zero in that norm. The embedding `H^q(0,1) -> L^2(0,1)` is trace class in one dimension because its singular values are `O(j^{-q})`. Factoring through this embedding gives the stated `S_1` convergence.

Also, if `T in S_1` and `R_r -> I` strongly with uniformly bounded norms, then

\[
\|R_rTR_r-T\|_{\mathcal S_1}\to0.
\]

This is the standard finite-rank approximation argument for the trace ideal. Applying it to `T=B^*K_\gamma B`, and using

\[
\|B^*(K_{\gamma,r}-K_\gamma)B\|_1
\le \|B\|^2\|K_{\gamma,r}-K_\gamma\|_1,
\]

shows

\[
\boxed{
\|\mathcal H_{\alpha,r}\mathcal H_{\beta,r}
-\mathcal H_\alpha\mathcal H_\beta\|_{\mathcal S_1}
\to0
\qquad(\alpha\beta\neq1).
}
\]

Now take a cyclically separated word. Choose any adjacent pair and write the radial product as

\[
P_r=A_rT_rB_r,
\]

where `T_r` is that separated two-channel product. The factors `A_r,B_r` are uniformly bounded and converge strong-* to their boundary products `A,B`, while `T_r -> T` in `S_1` by the preceding argument. The trace ideal then gives

\[
\boxed{\|A_rT_rB_r-ATB\|_{\mathcal S_1}\to0.}
\]

Indeed, split the difference into the term containing `T_r-T` plus the two terms containing `A_r-A` and `B_r-B`; the first is controlled directly in trace norm, and the latter two tend to zero in `S_1` by finite-rank approximation of the fixed trace-class factor together with strong-* convergence.

Consequently

\[
\operatorname{Tr}(P_r)\longrightarrow\operatorname{Tr}(P)
\]

for the **ordinary** trace of the boundary product. The already-derived cube integral computes the left-hand side for `r<1`, and dominated convergence computes its scalar limit. Combining the two passages proves exactly the boxed identity in §2:

\[
\operatorname{Tr}(\mathcal H_{\alpha_1}\cdots\mathcal H_{\alpha_k})
=\left(\prod_i\alpha_i\right)
\int_{[0,1]^k}
\prod_i\frac{dx_1\cdots dx_k}
{1-\alpha_i\alpha_{i+1}x_ix_{i+1}}.
\]

Thus the radial prescription is not merely an Abel-regularized surrogate in the cyclically separated case: it converges in `S_1` to the trace-class boundary product, so its limit is the ordinary cyclic trace claimed by PC-082.
