# AF-417 — Linear derivative shift renormalizes the left-tail Plancherel sectors

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `DERIVATIVE-SHIFT` · `PLANCHEREL-SECTOR` · `NO-NOVELTY-CLAIM`

## Claim

Keep the AF-412--AF-416 left-tail analytic germ

\[
h(x)=\frac{x}{2}-\sum_{k\ge1}\frac{B_{2k}}{2k(2k)!}x^{2k}
=\sum_{\alpha\in\mathcal A}c_\alpha x^\alpha,
\qquad
\mathcal A=\{1,2,4,6,\ldots\},
\]

and for integers `R>=1`, `s>=0` write

\[
D_R^{(s)}(x)=\det\bigl(h_{a+b+s}(x)\bigr)_{a,b=0}^{R-1},
\qquad h_j=(x\,d/dx)^j h.
\]

AF-416 gives the exact Cauchy--Binet expansion

\[
D_R^{(s)}(x)
=
\sum_{\substack{A\subset\mathcal A\\|A|=R}}
\left(\prod_{\alpha\in A}c_\alpha\alpha^s x^\alpha\right)
\Delta(A)^2.
\tag{1}
\]

Set `R=n+1`. In the subfamily of exponent sets containing the exceptional exponent `1`, the baseline is

\[
A_0=\{1,2,4,\ldots,2n\}.
\]

For a partition `\lambda` with `\ell(\lambda)\le n`, put

\[
k_i=i+\lambda_{n+1-i},\qquad 1\le i\le n,
\]

and

\[
A_\lambda=\{1,2k_1,\ldots,2k_n\}.
\]

Let `d=|\lambda|`, let `T_{n,\lambda}^{(s)}(x)` be the signed term of `(1)` indexed by `A_\lambda`, and let `E_n^{(s)}(x)=T_{n,\varnothing}^{(s)}(x)`.

Let `s_n` be any sequence of nonnegative integers and take the reciprocal-order left-tail diagonal

\[
x=\frac cn,
\qquad c>0.
\]

If

\[
\frac{s_n}{n}\longrightarrow\sigma\in[0,\infty),
\]

then for every fixed partition `\lambda`, locally uniformly for `c` in compact subsets of `(0,\infty)`, one has

\[
\boxed{
\frac{T_{n,\lambda}^{(s_n)}(c/n)}{E_n^{(s_n)}(c/n)}
\longrightarrow
(-1)^d
\frac{\bigl(e^\sigma c^2/(4\pi^2)\bigr)^d}{H_\lambda^2},
}
\tag{2}
\]

where `H_\lambda` is the product of hook lengths of `\lambda`.

Consequently, for every fixed excess degree `d`, summing over all partitions `\lambda\vdash d` gives

\[
\boxed{
\frac{\sum_{\lambda\vdash d}T_{n,\lambda}^{(s_n)}(c/n)}
{E_n^{(s_n)}(c/n)}
\longrightarrow
\frac{(-1)^d}{d!}
\left(\frac{e^\sigma c^2}{4\pi^2}\right)^d.
}
\tag{3}
\]

Thus the fixed-shift Plancherel law of AF-414 is stable for `s_n=o(n)`, but a linearly growing derivative shift changes its effective Cauchy parameter by the exact multiplicative factor `e^\sigma`.

The first correction already gives a sharp transition. For `\lambda=(1)`, exactly

\[
\boxed{
\frac{T_{n,(1)}^{(s)}(c/n)}{E_n^{(s)}(c/n)}
=
-\frac{c^2}{4\pi^2}
\left(\frac{n+1}{n}\right)^{s-1}
\frac{\zeta(2n+2)}{\zeta(2n)}
\left(\frac{2n+1}{2n-1}\right)^2.
}
\tag{4}
\]

Hence:

- if `s_n=o(n)`, the ratio in `(4)` tends to `-c^2/(4\pi^2)`;
- if `s_n/n\to\sigma<\infty`, it tends to `-e^\sigma c^2/(4\pi^2)`;
- if `s_n/n\to\infty`, its magnitude diverges.

So `s\asymp n` is the exact scale at which derivative depth becomes a new asymptotic resource for the fixed-excess left-tail hierarchy. This is a statement about normalized Cauchy--Binet sectors. It does not yet justify exchanging the large-`n` limit with the complete partition sum when `s_n` grows with `n`, and it does not establish a full-determinant limit or total positivity.

## 1. Exact Schur/Vandermonde ratio for arbitrary derivative shift

AF-416 derived, for the same exponent family and arbitrary nonnegative integer shift `s`,

\[
\frac{T_{n,\lambda}^{(s)}(x)}{E_n^{(s)}(x)}
=
(-1)^d
\left(\frac{x}{2\pi}\right)^{2d}
 s_\lambda(1^n)^2
 R_{n,\lambda}^{(s)},
\tag{5}
\]

where

\[
R_{n,\lambda}^{(s)}
=
\prod_{i=1}^{n}
\left(\frac{k_i}{i}\right)^{s-1}
\frac{\zeta(2k_i)}{\zeta(2i)}
\left(\frac{2k_i-1}{2i-1}\right)^2.
\tag{6}
\]

Only the first factor in `(6)` depends materially on a growing derivative shift. The zeta ratio and the odd-distance factor are the same as in AF-414.

For fixed `\lambda`, write its nonzero parts as `\lambda_j`, `1\le j\le\ell(\lambda)`. The corresponding shifted indices in `(6)` are

\[
i=n+1-j.
\]

Therefore

\[
\sum_{i=1}^n\log\frac{k_i}{i}
=
\sum_{j=1}^{\ell(\lambda)}
\log\left(1+\frac{\lambda_j}{n+1-j}\right).
\tag{7}
\]

Since `\lambda` is fixed,

\[
\sum_{j=1}^{\ell(\lambda)}
\log\left(1+\frac{\lambda_j}{n+1-j}\right)
=
\frac{|\lambda|}{n}+O_\lambda(n^{-2}).
\tag{8}
\]

If `s_n/n\to\sigma<\infty`, multiplying `(8)` by `s_n-1` gives

\[
(s_n-1)
\sum_i\log\frac{k_i}{i}
\longrightarrow
\sigma |\lambda|.
\tag{9}
\]

Thus

\[
\prod_i\left(\frac{k_i}{i}\right)^{s_n-1}
\longrightarrow e^{\sigma d}.
\tag{10}
\]

For the other factors in `(6)`, only finitely many indices near `n` differ from their baseline values. Hence

\[
\prod_i\frac{\zeta(2k_i)}{\zeta(2i)}\to1,
\qquad
\prod_i\left(\frac{2k_i-1}{2i-1}\right)^2\to1.
\tag{11}
\]

Combining `(10)` and `(11)` gives

\[
R_{n,\lambda}^{(s_n)}\to e^{\sigma d}.
\tag{12}
\]

## 2. Hook-content asymptotics and the deformed fixed-degree law

The hook-content formula gives, for fixed `\lambda` of size `d`,

\[
s_\lambda(1^n)
=
\frac{n^d}{H_\lambda}
\bigl(1+O_\lambda(n^{-1})\bigr).
\tag{13}
\]

Substitute `x=c/n` into `(5)`. The `n^{2d}` from the squared Schur dimension cancels the `n^{-2d}` from `x^{2d}`, while `(12)` supplies the new factor `e^{\sigma d}`. This proves `(2)`.

For fixed `d`, there are finitely many partitions of `d`, so the limit may be summed term by term. The classical hook-length formula and regular-representation identity give

\[
\sum_{\lambda\vdash d}\frac1{H_\lambda^2}=\frac1{d!}.
\tag{14}
\]

Equation `(3)` follows immediately.

The deformation is therefore degree-blind at fixed degree: every partition shape of size `d` receives the same additional factor `e^{\sigma d}`. The ordinary Plancherel proportions inside degree `d` are unchanged; only the total weight assigned to that degree is renormalized.

## 3. Degree one isolates the transition without any tail interchange

For `\lambda=(1)`, only the largest baseline index moves from `k_n=n` to `k_n=n+1`, and

\[
s_{(1)}(1^n)=n.
\]

Substitution into `(5)` gives `(4)` directly. Since

\[
\frac{\zeta(2n+2)}{\zeta(2n)}\to1,
\qquad
\left(\frac{2n+1}{2n-1}\right)^2\to1,
\tag{15}
\]

the transition is controlled exactly by

\[
\left(1+\frac1n\right)^{s_n-1}.
\tag{16}
\]

If `s_n/n\to\sigma`, `(16)` tends to `e^\sigma`. If `s_n/n\to\infty`, its logarithm is

\[
(s_n-1)\log(1+1/n),
\]

which tends to `+\infty`; therefore the degree-one correction alone overwhelms the baseline term in magnitude.

This last conclusion requires no assumption about the rest of the partition tail. It proves that a normalization based only on the smallest exponent set cannot remain a relative asymptotic once derivative depth grows superlinearly compared with determinant size.

## 4. Arithmetic-fidelity interpretation

AF-414--AF-416 showed that on `x=c/n` the fixed-shift hierarchy has a coherent partition organization and, after full resummation for the shifts needed by the Euler determinant decomposition, the left-tail diagonal remains positive. The present result isolates an additional resource that those fixed-shift theorems deliberately held constant: **derivative depth**.

At bounded or sublinear derivative depth, fixed excess degrees see the same normalized law. At linear depth, the law remembers the ratio `s_n/n` through `e^\sigma`. At superlinear depth, even the first neighboring exponent family loses baseline control. Thus a confluent/Hankel compression cannot be audited by determinant order and source scale alone when the derivative offset is also allowed to grow.

This is an Arithmetic Fidelity effect rather than a new RH criterion. It identifies a precise parameter that survives the asymptotic compression and changes the retained sector weights. Any all-order sign argument that moves through derivative-Hankel minors with growing offsets must control the joint scaling of source coordinate, determinant order, and derivative depth.

No rational-prime discriminator is used in `(1)`--`(16)`, and no statement about zeta zeros follows from this finding.

## Prior-art and novelty audit

The representation-theoretic ingredients are classical. The Schur measure and its relation to Plancherel-type partition weights belong to the established framework developed by Andrei Okounkov in *Infinite wedge and random partitions*, Selecta Mathematica 7 (2001), 57--81, DOI `10.1007/PL00001398`; the hook-content and hook-length identities used here are likewise standard symmetric-function and symmetric-group representation theory.

Large-size Hankel determinants with parameters varying simultaneously with matrix size are also a classical asymptotic theme. For example, Charlier and Deaño, *Asymptotics for Hankel Determinants Associated to a Hermite Weight with a Varying Discontinuity*, SIGMA 14 (2018), 018, DOI `10.3842/SIGMA.2018.018`, studies a critical transition when a Hankel-weight parameter varies with `n`; Lyu, Griffin, and Chen, *The Hankel determinant associated with a singularly perturbed Laguerre unitary ensemble*, Journal of Nonlinear Mathematical Physics 26 (2019), 24--53, DOI `10.1080/14029251.2019.1544786`, studies double scalings in which determinant size and perturbation parameters vary together.

Those works establish that varying-parameter/double-scaling behavior is not itself new. A targeted prior-art search did not supply the specific formula `(2)`--`(4)` for the AF-412 Bernoulli derivative-Hankel exponent family. No novelty is claimed for Schur functions, Plancherel measure, Cauchy--Binet, hook formulas, or the general idea of varying-parameter Hankel asymptotics. The durable contribution here is the exact specialization showing that the derivative offset has a sharp linear scale and renormalizes every fixed excess degree by `e^{\sigma d}`.

## Boundaries and falsification checks

- Equations `(2)` and `(3)` hold with `\lambda` or `d` fixed as `n\to\infty`. They do not justify a limit of the complete partition sum when `s_n` grows with `n`.
- AF-415's fixed-shift absolute Schur domination cannot simply be cited for `s_n\asymp n`; the factor `(k_i/i)^{s_n-1}` is no longer bounded by an `n`-independent constant to the excess degree over the entire partition range. A new uniform tail argument is required.
- Equation `(4)` is an exact finite-`n` check of the transition. Any indexing error in `(2)` changes the elementary factor `((n+1)/n)^{s-1}` immediately.
- The all-even exponent class and the other singular-block sectors from AF-416 are not analyzed here for a growing shift. Their fixed-shift negligibility does not automatically persist under arbitrary `s_n`.
- The result concerns the analytic left-tail germ and shifted derivative-Hankel minors. It does not decide the compact order-five gate, all-order Euler total positivity, or RH.

## Consequence for the research line

The reciprocal-order coordinate `x=c/n` is not by itself the complete large-order fidelity parameter. Once derivative depth is allowed to vary, the normalized local law has a second scale `s_n/n`. The fixed-excess hierarchy exhibits a sharp three-regime split: sublinear shifts preserve the AF-414 law, linear shifts deform it by an exact exponential parameter, and superlinear shifts destroy baseline dominance already at degree one.

The next nontrivial question is whether the **complete** exceptional-`1` partition sector has a locally uniform limit `exp(-e^\sigma c^2/(4\pi^2))` when `s_n/n\to\sigma`, and, beyond that, whether the omitted exponent and singular-block sectors remain negligible under the same coupled scaling. Those questions require new uniform control and are not consequences of the present fixed-degree theorem.