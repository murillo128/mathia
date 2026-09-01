# PC-120 — divergent scalar Hardy amplification destroys det2 normality

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-117 proves that the canonically normalized arbitrary-conductor one-new-prime Hardy corrector

\[
X_{p,q}:=\frac{G_{p,q}}{\sqrt{\varphi(q)}},
\qquad p\nmid q,
\]

is self-adjoint and, along every joint path `p,q -> infinity` with `p` prime,

\[
\boxed{\|X_{p,q}\|\longrightarrow0},
\qquad
\boxed{\|X_{p,q}\|_{\mathcal S_2}^2\longrightarrow c_H},
\qquad
c_H:=\gamma-4+5\log2>0.
\]

PC-119 deliberately leaves divergent scalar amplification outside its bounded-preconditioning theorem. That escape can be classified completely for real conductor-dependent scalar rescalings. Let `a_{p,q} in R` and form

\[
Y_{p,q}:=a_{p,q}X_{p,q},
\qquad
F_{p,q}(z):=\det{}_2(I-zY_{p,q}).
\]

Equivalently, this is the conductor-dependent spectral zoom `z -> a_{p,q}z` applied to the canonical PC-117 determinant. Then there are only two possible asymptotic regimes:

1. if `a_{p,q}` remains bounded, every scalar-convergent subsequence `a_{p,q}->a` has the locally uniform limit

\[
\boxed{
F_{p,q}(z)\longrightarrow
\exp\!\left(-\frac{c_Ha^2}{2}z^2\right),
}
\]

which is entire and zero-free;
2. if `|a_{p,q}|->infinity`, then for every fixed real `y!=0`,

\[
\boxed{
|F_{p,q}(iy)|^2
\ge
1+y^2a_{p,q}^2\|X_{p,q}\|_{\mathcal S_2}^2
\longrightarrow\infty.
}
\]

Hence a divergent real scalar zoom is not merely outside the PC-119 estimate: the canonical Carleman--Fredholm determinant fails even pointwise to remain finite on the nonzero imaginary axis. For an arbitrary real scalar sequence, every locally uniform finite entire cluster function therefore comes from a bounded scalar subsequence and is a zero-free Gaussian; every unbounded scalar subsequence contains a further divergent-modulus subsequence on which no finite canonical `det_2` limit exists.

This closes the most direct singular escape left by PC-117/119. A conductor-dependent real scalar normalization by itself cannot turn the exact Prime-Circle Hardy corrector into a finite entire Fredholm determinant carrying a Riemann-like zero divisor. A surviving repair would need additional geometry-forced renormalization beyond scalar amplification, a genuinely non-scalar unbounded transformation, or a construction made before the PC-117 infinitesimal-corrector limit. No abstract novelty is claimed for the regularized determinant product formula; it is standard trace-ideal theory, with Barry Simon's *Trace Ideals and Their Applications* already anchored in `research/prime_circle/SOURCES.md`. The durable contribution is the exact Prime-Circle boundary classification of the divergent scalar escape explicitly left open by PC-119.

## 1. Bounded scalar amplification gives only the PC-117 Gaussian family

Take any subsequence on which

\[
a_{p,q}\longrightarrow a\in\mathbb R.
\]

Then

\[
\|Y_{p,q}\|
=|a_{p,q}|\,\|X_{p,q}\|
\longrightarrow0,
\]

while self-adjointness gives

\[
\operatorname{Tr}(Y_{p,q}^2)
=a_{p,q}^2\operatorname{Tr}(X_{p,q}^2)
=a_{p,q}^2\|X_{p,q}\|_{\mathcal S_2}^2
\longrightarrow a^2c_H.
\]

For every `k>=3`,

\[
|\operatorname{Tr}(Y_{p,q}^k)|
\le
\|Y_{p,q}\|^{k-2}\|Y_{p,q}\|_{\mathcal S_2}^2
\longrightarrow0.
\]

Therefore the standard regularized trace expansion used in PC-117 gives, locally uniformly on `C`,

\[
\log\det{}_2(I-zY_{p,q})
=-\frac{z^2}{2}\operatorname{Tr}(Y_{p,q}^2)+o(1),
\]

and consequently

\[
\boxed{
\det{}_2(I-zY_{p,q})
\longrightarrow
\exp\!\left(-\frac{c_Ha^2}{2}z^2\right).
}
\]

Thus bounded scalar rescaling does not create a new spectral regime. It only changes the variance of the zero-free Gaussian already identified by PC-117. The case `a=0` gives the constant function `1`.

If the bounded scalar sequence itself does not converge, compactness of bounded subsets of `R` ensures scalar-convergent subsequences, and every such subsequence has one of these Gaussian limits. In particular no bounded real scalar normalization can yield a finite entire cluster function with nontrivial zeros.

## 2. Exact imaginary-axis formula for divergent amplification

Now suppose

\[
|a_{p,q}|\longrightarrow\infty.
\]

At every finite conductor, `X_{p,q}` is finite-rank, self-adjoint and Hilbert--Schmidt. Write its real eigenvalues as `lambda_{p,q,k}`. The canonical Hilbert--Schmidt regularized determinant has the standard product representation

\[
F_{p,q}(z)
=
\prod_k
(1-za_{p,q}\lambda_{p,q,k})
\exp(za_{p,q}\lambda_{p,q,k}).
\]

Fix any real `y!=0` and set `z=iy`. Since `a_{p,q}` and every `lambda_{p,q,k}` are real, each regularizing exponential has modulus one. Hence

\[
\begin{aligned}
|F_{p,q}(iy)|^2
&=
\prod_k
\left|1-iya_{p,q}\lambda_{p,q,k}\right|^2\\
&=
\boxed{
\prod_k
\left(1+y^2a_{p,q}^2\lambda_{p,q,k}^2\right).
}
\end{aligned}
\]

All factors are at least one. For nonnegative `t_k`,

\[
\prod_k(1+t_k)\ge1+\sum_k t_k,
\]

so

\[
\boxed{
|F_{p,q}(iy)|^2
\ge
1+y^2a_{p,q}^2
\sum_k\lambda_{p,q,k}^2
=
1+y^2a_{p,q}^2\|X_{p,q}\|_{\mathcal S_2}^2.
}
\]

PC-117 supplies the strictly positive limiting Hilbert--Schmidt mass `c_H`. Therefore

\[
\boxed{
\forall y\in\mathbb R\setminus\{0\},\qquad
|F_{p,q}(iy)|\longrightarrow\infty.
}
\]

No information about the detailed eigenvalue distribution is needed. The obstruction is forced solely by the coexistence of vanishing individual spectral scale and nonzero total quadratic mass.

## 3. Divergent scalar zoom cannot have a finite entire canonical determinant limit

Local uniform convergence of entire functions to a finite entire function implies pointwise convergence at every fixed point. Section 2 shows that a divergent-modulus scalar sequence violates even this weakest necessary condition at every nonzero point of the imaginary axis. Therefore

\[
\boxed{
|a_{p,q}|\to\infty
\quad\Longrightarrow\quad
\det{}_2(I-za_{p,q}X_{p,q})
\text{ has no locally uniform finite entire limit.}
}
\]

This is stronger than merely saying that the PC-119 bounded proof no longer applies. The canonical `det_2` family itself leaves the locally finite Fredholm-determinant regime.

Combining Sections 1 and 2 yields a complete subsequential classification for arbitrary real scalar amplifications. Given any sequence `a_{p,q}`:

- every bounded subsequence has a further scalar-convergent subsequence whose `det_2` limit is a zero-free Gaussian;
- every unbounded subsequence has a further subsequence with `|a_{p,q}|->infinity`, and along that subsequence the canonical determinant diverges at each fixed `iy`, `y!=0`.

Hence every finite entire locally uniform cluster function of the scalar-amplified canonical determinant is necessarily zero-free.

## 4. Why this is an RH-relevant negative rather than another normalization choice

The singular scalar escape was mathematically natural because `\|X_{p,q}\|->0` while `\|X_{p,q}\|_{\mathcal S_2}` stays finite: one might hope to zoom the collapsing individual eigenvalues back to finite locations by choosing `a_{p,q}->infinity`. The exact product formula shows the cost. Any such scalar zoom simultaneously amplifies the nonzero quadratic mass to

\[
\|a_{p,q}X_{p,q}\|_{\mathcal S_2}^2
=a_{p,q}^2\|X_{p,q}\|_{\mathcal S_2}^2
\longrightarrow\infty,
\]

and the canonical regularized determinant loses local finiteness before a Riemann-like entire divisor can emerge from this procedure alone.

This does **not** prove that the finite-stage rescaled eigenvalue sets themselves have no interesting subsequential statistics. It proves the narrower and durable statement relevant to the Fredholm route: scalar spectral zoom alone cannot produce a finite entire canonical `det_2` object whose zeros could be compared with the nontrivial zeros of `zeta`.

Nor does the argument forbid multiplying `F_{p,q}` by an additional conductor-dependent zero-free entire factor, subtracting further divergent trace counterterms, changing the regularization, or using a non-scalar singular transform. Those operations add new structure. Under the canonical Prime-Circle mandate they require an independent intrinsic geometric derivation and cannot be counted as progress merely because an arbitrary renormalizer can force a desired function class.

## 5. Falsification checks and exact boundary

1. **Reality of the scalar is used.** The imaginary-axis modulus identity uses a real scalar amplification of the self-adjoint corrector. This is the natural class for a real spectral zoom and self-adjoint spectral interpretation. The finding does not claim the same pointwise bound for arbitrary complex conductor-dependent scalars.
2. **Joint Hardy regime only.** The input is exactly the PC-117 joint `p,q -> infinity` asymptotic. Fixed-`q` microlocal regimes such as PC-113/114 are not covered.
3. **Positive Hilbert--Schmidt mass is essential.** If the quadratic mass also vanished, the lower bound would not force blowup. Here the exact Prime-Circle constant `c_H=gamma-4+5 log 2` is strictly positive.
4. **`det_2`, not an arbitrary renormalized determinant.** An extra conductor-dependent zero-free factor can change function convergence without changing finite-stage zeros. Such a factor is outside scalar amplification itself and must be justified independently.
5. **Bounded oscillatory scalars are harmless.** They can create several Gaussian cluster functions through different scalar accumulation points, but every one remains zero-free.
6. **Unbounded but non-divergent sequences are included subsequentially.** Any unbounded real scalar sequence contains a subsequence whose modulus tends to infinity, so it cannot have a unique finite locally uniform entire limit along the original full sequence.

The exact frontier left after PC-120 is therefore not simply “allow an unbounded normalization.” A candidate must supply additional structure capable of reorganizing or renormalizing the diverging Hilbert--Schmidt mass in a way forced by the Prime-Circle geometry itself, or leave the scalar-amplified PC-117 determinant framework entirely.

## 6. Prior-art and novelty audit

The analytic machinery is classical. For Hilbert--Schmidt operators, the Carleman--Fredholm determinant `det_2` has the canonical product

\[
\det{}_2(I-zA)
=
\prod_k(1-z\lambda_k)e^{z\lambda_k},
\]

and the logarithmic trace expansion begins at quadratic order. These facts, together with the Schatten norm identities used above, belong to standard trace-ideal theory; Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., AMS (2005), is already recorded in `research/prime_circle/SOURCES.md` for this branch. No theorem-level historical novelty is claimed for them.

The Prime-Circle contribution is the application of that standard machinery to the exact PC-117 asymptotic pair

\[
\|X_{p,q}\|\to0,
\qquad
\|X_{p,q}\|_{\mathcal S_2}^2\to c_H>0,
\]

which was derived from the intrinsic one-new-prime Hardy geometry. PC-119 identified divergent scalar amplification as the sharpest elementary escape from its bounded-preconditioning no-go. The present argument closes that escape for the canonical regularized determinant without adding arithmetic assumptions or an arbitrary spectral wrapper:

\[
\boxed{
\text{real scalar Hardy amplification}
\Longrightarrow
\begin{cases}
\text{bounded scale: zero-free Gaussian cluster},\\
\text{divergent scale: no finite canonical det}_2\text{ limit}.
\end{cases}
}
\]

What survives must therefore derive a genuinely new renormalization or operator mechanism from the Prime-Circle geometry rather than merely choosing a conductor-dependent scalar spectral scale.