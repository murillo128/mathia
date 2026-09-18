# PL-360 — Diagonal coefficient reweighting cannot both contain zeta and support critical-strip point evaluation

**Evidence:** `CLASSICAL-WEIGHTED-RKHS+EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-359`.

`PL-359` shows that the native unweighted coefficient Hardy space `\mathscr H^2` cannot contain a nonzero conductor-one Riemann functional-equation solution: the all-ones zeta coefficient vector is outside the `\ell^2` completion. The most immediate escape is to change the coefficient norm. For the broad class of **diagonal** Hilbert reweightings of the exponent-lattice basis, that escape fails before the functional equation or zero set is reached.

Let `w_n>0` and let `\mathcal H_w` be the Hilbert completion of Dirichlet polynomials for

\[
\left\|\sum_n a_n n^{-s}\right\|_w^2
=
\sum_{n\ge1}|a_n|^2w_n.
\tag{1}
\]

For `s_0=\sigma+it`, point evaluation on Dirichlet polynomials extends to a bounded functional on `\mathcal H_w` if and only if

\[
\sum_{n\ge1}\frac{n^{-2\sigma}}{w_n}<\infty.
\tag{2}
\]

If a coefficient vector `c=(c_n)` belongs to `\mathcal H_w` and evaluation at `s_0` is bounded, then Cauchy--Schwarz gives

\[
\sum_{n\ge1}|c_n|n^{-\sigma}
\le
\left(\sum_n|c_n|^2w_n\right)^{1/2}
\left(\sum_n\frac{n^{-2\sigma}}{w_n}\right)^{1/2}
<\infty.
\tag{3}
\]

Thus **membership of a target coefficient vector plus bounded point evaluation forces absolute convergence of that target's ordinary Dirichlet series at the same abscissa**.

For the zeta coefficient vector `c_n=1`, membership means

\[
\sum_{n\ge1}w_n<\infty.
\tag{4}
\]

Combining (2)--(4) would force

\[
\sum_{n\ge1}n^{-\sigma}<\infty.
\tag{5}
\]

Consequently

\[
\boxed{
(1,1,1,\ldots)\in\mathcal H_w
\quad\Longrightarrow\quad
\text{point evaluation is unbounded at every }s\text{ with }\Re s\le1.
}
\tag{6}
\]

In particular, no diagonal reweighting of the Dirichlet/exponent-vector basis can simultaneously make the formal zeta vector finite-norm and retain ordinary reproducing-kernel point evaluation anywhere in the critical strip.

## 1. The obstruction is exactly the diagonal RKHS duality

The criterion (2) is not a special property of a particular weight family. On the dense Dirichlet-polynomial subspace, evaluation at `s_0` is the coefficient functional

\[
(a_n)\longmapsto\sum_n a_n n^{-s_0}.
\tag{7}
\]

The dual norm in the weighted coefficient Hilbert space is therefore

\[
\|\operatorname{ev}_{s_0}\|^2
=
\sum_n\frac{|n^{-s_0}|^2}{w_n}
=
\sum_n\frac{n^{-2\sigma}}{w_n},
\tag{8}
\]

whenever finite. This is the standard reproducing-kernel formula for weighted Hilbert spaces of Dirichlet series. Stetler records the kernel as

\[
k(u,z)=\sum_{n\ge1}w_n^{-1}n^{-u-\bar z},
\tag{9}
\]

in the same weighted setup, building on the weighted Dirichlet Hilbert-space framework studied by McCarthy.

Equation (3) is then simply the pairing between the target vector and the evaluation kernel. It is stronger than a statement that a particular choice of polynomial weights fails: **every positive diagonal weight sequence is covered**.

## 2. Prime-lattice formulation

Under the Bohr lift, index `n` is the exponent vector `\alpha=v(n)` and the formal zeta vector is

\[
Z(z)=\sum_{\alpha\in\mathbb N_0^{(\mathcal P)}}z^\alpha,
\tag{10}
\]

with coefficient one on every lattice point. A diagonal lattice metric assigns a positive weight `w_\alpha=w_n` to each monomial, so

\[
\|Z\|_w^2=\sum_\alpha w_\alpha.
\tag{11}
\]

Along the arithmetic Bohr curve

\[
z_p=p^{-s},
\tag{12}
\]

bounded evaluation requires

\[
\sum_\alpha\frac{|z^\alpha|^2}{w_\alpha}<\infty.
\tag{13}
\]

If both (11) and (13) held, Cauchy--Schwarz would imply

\[
\sum_\alpha|z^\alpha|<\infty.
\tag{14}
\]

But

\[
\sum_\alpha|z^\alpha|
=
\sum_{n\ge1}n^{-\sigma},
\tag{15}
\]

so the Bohr curve can be a bounded evaluation locus for the finite-norm zeta vector only when `\sigma>1`. The absolute-convergence wall has reappeared as a purely Hilbert-geometric duality obstruction.

This is precisely the opposite of the desired repair after `PL-359`: shrinking the diagonal weights enough to admit the all-ones lattice vector necessarily enlarges the dual evaluation kernels enough to destroy bounded evaluation before analytic continuation begins.

## 3. What this does and does not rule out

The result rules out a large but sharply specified class of completion changes: **orthogonal exponent-lattice monomials with an arbitrary positive diagonal metric**, together with ordinary point evaluation obtained by continuously extending evaluation of Dirichlet polynomials. It therefore excludes polynomial, multiplicative, rapidly decaying, and otherwise irregular diagonal weights alike.

It does **not** rule out a non-diagonal Gram geometry on the lattice, a target-relative Nyman/Mellin space, model spaces, quotient constructions, rigged Hilbert or distributional completions, Banach topologies, or an unbounded/renormalized evaluation procedure. Those possibilities evade the two dual weighted `\ell^2` sums in (3). Nor does the result prevent an individual element of a weighted coefficient space from possessing an analytic continuation by external means; it says that such continuation values cannot be realized as bounded extension of the ordinary Dirichlet-polynomial evaluation at an abscissa where the target series is not absolutely convergent.

The argument also does not depend on zeta until (4). For any target coefficient vector `c_n`, diagonal Hilbert membership plus bounded evaluation forces absolute convergence `\sum |c_n|n^{-\sigma}<\infty`. This makes the obstruction structural rather than a disguised use of the zeta pole or of RH.

## 4. Prior-art and novelty audit

Weighted coefficient Hilbert spaces of Dirichlet series are classical. McCarthy studies Hilbert norms given by weighted `\ell^2` norms of Dirichlet coefficients. Stetler explicitly works with

\[
\mathcal H^w=\left\{\sum a_n n^{-s}:\sum|a_n|^2w_n<\infty\right\}
\tag{16}
\]

and records both the Cauchy--Schwarz point-evaluation condition and the reproducing kernel (9). Olsen develops the relation between positive weight asymptotics and the local analytic behavior of the resulting Dirichlet-series Hilbert spaces.

A targeted literature audit on 18 September 2026 searched weighted Hilbert spaces of Dirichlet series together with zeta, bounded point evaluations, coefficient weights, and absolute-convergence abscissae. It recovered this established RKHS framework and later weighted spaces with controlled point-evaluation half-planes, but no basis for treating (3)--(6) as a new theorem. **No theorem-level novelty is claimed.** The line-local contribution is the exact route restriction: the diagonal-topology escape explicitly left open by `PL-359` cannot move the zeta coefficient vector into the Hilbert space while preserving continuous evaluation into the continuation region.

### Sources

1. John E. McCarthy, “Hilbert spaces of Dirichlet series and their multipliers,” *Transactions of the American Mathematical Society* **356** (2004), 881--893. DOI: https://doi.org/10.1090/S0002-9947-03-03452-4.
2. Eric Stetler, “Multipliers on Hilbert Spaces of Dirichlet Series,” arXiv:1401.3286 (2014), especially the weighted space definition and reproducing kernel `k(u,z)=\sum w_n^{-1}n^{-u-\bar z`. https://arxiv.org/abs/1401.3286.
3. Jan-Fredrik Olsen, “Local properties of Hilbert spaces of Dirichlet series,” *Journal of Functional Analysis* **261** (2011), 2669--2696. arXiv:1011.3370; DOI: https://doi.org/10.1016/j.jfa.2011.07.007. Used as broader context for how coefficient weights control local analytic behavior.

## Research consequence

`PL-359` left “change the completion topology” as a live escape from native `\mathscr H^2`. The present result removes the most direct version of that escape. Merely changing the lengths of the exponent-basis vectors cannot work: if the zeta all-ones vector becomes finite-norm, ordinary RKHS evaluation is forced to stop at the same `Re(s)=1` absolute-convergence wall as the original Dirichlet series.

A viable completion must therefore change more than diagonal weights. It must introduce genuinely non-diagonal correlations between lattice points, use a target-relative/quotient geometry, or abandon bounded ordinary point evaluation in favor of a controlled continuation or distributional pairing. Any such proposal should be tested against (3): if its mechanism secretly reduces to a diagonal coefficient norm plus its Hilbert dual evaluation, it cannot reach the critical strip.