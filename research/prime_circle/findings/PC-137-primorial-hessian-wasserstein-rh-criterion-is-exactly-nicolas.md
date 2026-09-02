# PC-137 — primorial Hessian Wasserstein RH criterion is exactly Nicolas

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-RH-EQUIVALENCE` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY`. PC-136 showed that the canonical cross-shell-only resultant Hessian on the primorial common refinement has an exact Wasserstein-1 defect from the universal full-polygon spectrum, and that this defect is a Mertens-squared Euler product. A natural remaining question is whether the finite defect itself, rather than its universal limiting bulk law, carries a genuinely new RH-sensitive spectral criterion.

It does carry an exact RH-equivalent inequality. However, after one elementary factorization, that inequality is **identically the classical Nicolas primorial criterion for Euler's totient function**. Even replacing the finite correction by its limiting constant preserves only an eventual form of the same Nicolas mechanism. Thus the finite spectral defect is arithmetically RH-sensitive, but the sensitivity is not a new prime-circle spectral mechanism: it enters entirely through the classical primorial Euler product `phi(N)/N`.

## 1. Start from the exact PC-136 spectral defect

Let

\[
N_k:=\prod_{j\le k}p_j
\]

be the `k`th primorial, and let

\[
W_k:=W_1(\nu_{N_k}^\times,\nu_{N_k}^{\rm full})
\]

be the exact Wasserstein-1 distance between the normalized empirical spectrum of the cross-shell-only Hessian and that of the full regular-polygon inverse-square Laplacian, in the notation of PC-136.

PC-136 proved, for squarefree `N`,

\[
W_1(\nu_N^\times,\nu_N^{\rm full})
=\frac1{12}
\left[
\prod_{p\mid N}
\left(1-\frac2p+\frac2{p^3}\right)
-\frac1{N^2}
\right].
\]

Therefore

\[
\boxed{
12W_k+N_k^{-2}
=
\prod_{j\le k}
\left(1-\frac2{p_j}+\frac2{p_j^3}\right).
}
\]

Factor each local term as

\[
1-\frac2p+\frac2{p^3}
=\left(1-\frac1p\right)^2q_p,
\qquad
q_p:=\frac{p^3-2p^2+2}{p(p-1)^2}
=1-\frac{p-2}{p(p-1)^2}.
\]

Writing

\[
Q_k:=\prod_{j\le k}q_{p_j},
\]

and using

\[
\frac{\varphi(N_k)}{N_k}
=\prod_{j\le k}\left(1-\frac1{p_j}\right),
\]

we obtain the exact identity

\[
\boxed{
12W_k+N_k^{-2}
=Q_k\left(\frac{\varphi(N_k)}{N_k}\right)^2.
}
\]

No asymptotic estimate enters this identity. The entire finite spectral discrepancy separates into an absolutely convergent correction `Q_k` and the square of the classical primorial totient product.

As a finite control, `N_2=6` gives

\[
Q_2=\frac{11}{12},
\qquad
\left(\frac{\varphi(6)}6\right)^2=\frac19,
\]

so

\[
12W_2+\frac1{36}=\frac{11}{108},
\qquad
W_2=\frac1{162},
\]

in agreement with the PC-136 formula.

## 2. The apparent spectral RH criterion is exactly Nicolas

For `x>=2`, Nicolas uses

\[
f(x)
:=e^\gamma\log\theta(x)
\prod_{p\le x}\left(1-\frac1p\right),
\]

where `theta` is Chebyshev's function. At a prime endpoint `x=p_k`,

\[
\theta(p_k)=\log N_k,
\]

hence

\[
\boxed{
f(p_k)
=e^\gamma\log\log N_k\,
\frac{\varphi(N_k)}{N_k}.}
\]

Jean-Louis Nicolas proved in 1983 that

\[
\boxed{
\mathrm{RH}
\iff
\frac{N_k}{\varphi(N_k)}
>e^\gamma\log\log N_k
\quad\text{for every }p_k>2.
}
\]

Equivalently,

\[
\mathrm{RH}\iff f(p_k)<1
\quad\text{for every }p_k>2.
\]

Combining this with the exact PC-136 factorization gives

\[
\boxed{
\mathcal N_k
:=
\frac{e^{2\gamma}(\log\log N_k)^2}{Q_k}
\left(12W_k+N_k^{-2}\right)
=f(p_k)^2.
}
\]

Therefore

\[
\boxed{
\mathrm{RH}
\iff
\mathcal N_k<1
\quad\text{for every }p_k>2.
}
\]

This is an exact RH criterion written solely in terms of the primorial conductor, the PC-136 spectral Wasserstein defect, and the elementary finite factor `Q_k`. But the displayed equality proves at the same time that it is not a new spectral criterion in the mechanism sense: `mathcal N_k` is literally the square of Nicolas' classical function at prime endpoints.

The direction of information flow is therefore

\[
\boxed{
W_k
\longleftrightarrow
Q_k\left(\frac{\varphi(N_k)}{N_k}\right)^2
\longrightarrow
f(p_k)^2
\longrightarrow
\text{Nicolas RH criterion}.
}
\]

There is no independent zero divisor, spectral parameter, functional equation, gamma factor, or critical-line symmetry created by the Hessian spectrum.

## 3. The convergent correction cannot hide an independent RH scale

The factors `q_p` satisfy

\[
1-q_p=\frac{p-2}{p(p-1)^2}=O(p^{-2}),
\]

so

\[
C:=\prod_pq_p
\]

converges absolutely to a positive constant and

\[
\log\frac{Q_k}{C}
=-\sum_{p>p_k}\log q_p
=O(p_k^{-1}).
\]

Thus even the finite correction between the spectral defect and the squared totient product is asymptotically much smoother than the RH-sensitive Nicolas fluctuation scale.

This can be made precise. Define the constant-normalized quantity

\[
\Xi_k
:=
\frac{e^{2\gamma}(\log\log N_k)^2}{C}
\left(12W_k+N_k^{-2}\right)
=\frac{Q_k}{C}f(p_k)^2.
\]

Nicolas' later quantitative analysis shows two facts sufficient here:

1. under RH, the positive primorial gap

\[
\frac{N_k}{\varphi(N_k)}-e^\gamma\log\log N_k
\]

is of order at least `1/sqrt(log N_k)` along the primorials (indeed his normalized quantity `c(N_k)` is bounded below by a positive constant), which gives

\[
1-f(p_k)\gg \frac1{\sqrt{p_k}\log p_k};
\]

2. if RH fails, Nicolas' 1983 analysis gives, for some `0<b<1/2`,

\[
\log f(x)=\Omega_\pm(x^{-b}).
\]

Since `log(Q_k/C)=O(1/p_k)`, this correction is negligible compared with either scale. Consequently,

\[
\boxed{
\mathrm{RH}
\iff
\Xi_k<1
\quad\text{for all sufficiently large }k.
}
\]

If RH holds, the Nicolas gap dominates the positive `Q_k/C-1` tail correction and forces `Xi_k<1` eventually. If RH fails, `f(p_k)>1` infinitely often by the `Omega_+` statement, and because `Q_k/C>1`, the same subsequence has `Xi_k>1`.

This constant-normalized version is useful as an information audit: even after removing the full finite product `Q_k` and retaining only one universal constant, the RH sensitivity remains exactly the classical primorial Mertens/Nicolas fluctuation. It does not reveal a separate spectral scale.

## 4. Prior-art and novelty audit

The RH equivalence is classical. The primary source is:

- Jean-Louis Nicolas, *Petites valeurs de la fonction d'Euler*, Journal of Number Theory **17** (1983), 375--388, DOI `10.1016/0022-314X(83)90055-0`.

A later quantitative treatment is:

- Jean-Louis Nicolas, *Small values of the Euler function and the Riemann hypothesis*, Acta Arithmetica **155** (2012), 311--321, DOI `10.4064/aa155-3-7`, arXiv:`1202.0729`.

The 2012 paper explicitly recalls the 1983 equivalence, defines the same `f(x)`, records `log f(x)=Omega_+/- (x^{-b})` for some `0<b<1/2` if RH fails, and gives effective bounds under RH. These are precisely the ingredients needed for the constant-tail observation above.

Directed searches for a Nicolas criterion formulated through Wasserstein spectra, primorial Hessians, inverse-square chord Laplacians, or cross-shell roots-of-unity Hessian aggregates did not reveal this exact prime-circle packaging. That absence is not evidence of historical priority and is not being used as a novelty claim. The arithmetic content of the criterion is visibly classical because the exact finite identity factors through `phi(N_k)/N_k` before any RH statement is invoked.

This is analogous in research role to PC-007 and PC-105: an intrinsic geometric or spectral statistic can be RH-equivalent and still fail the mandate's novelty test when the equivalence is exactly a known arithmetic criterion under a reversible change of coordinates.

## 5. Research consequence

PC-136 left open whether its vanishing bulk discrepancy could nevertheless contain a useful RH-sensitive subleading statistic. For its **exact trace/Wasserstein defect**, the answer is now classified:

\[
\boxed{
\text{cross-shell primorial Hessian spectral defect}
\longrightarrow
\text{squared primorial totient product}
\longrightarrow
\text{Nicolas criterion}.
}
\]

So the finite defect is not arithmetically trivial: after the correct normalization it is RH-equivalent. But that is exactly why it must not be counted as a new spectral bridge. All RH sensitivity has already collapsed to the classical Euler product before the criterion is stated.

This closes the natural branch in which one tries to extract RH from the **first spectral moment / exact Wasserstein-1 distance** of the canonical PC-136 primorial aggregate. It does not close the spectral-edge questions PC-136 deliberately left open: extreme eigenvalues, outliers, eigenvectors, localized modes, higher nonlinear spectral statistics not determined by the trace, weighted divisor-pair operators, Schur complements, or cross-level constructions retaining more than this one scalar defect remain outside the result.

A future claim based on this PC-136 scalar must therefore pass a simple guard: if it can be algebraically reduced to `W_k`, `Q_k`, and `N_k`, then the identity above should be applied first. Any RH-equivalent threshold obtained after that reduction is a Nicolas/Mertens reformulation unless genuinely new information enters before the scalar compression.

## 6. Falsification surface

1. For each primorial `N_k`, direct construction of the PC-136 spectra must reproduce

\[
12W_k+N_k^{-2}
=Q_k(\varphi(N_k)/N_k)^2.
\]

2. The equality

\[
\mathcal N_k=f(p_k)^2
\]

is a finite algebraic identity. A discrepancy at any `k` would refute the claimed classicalization independently of RH.
3. The exact all-`k` RH equivalence uses Nicolas' theorem and must not be generalized from primorials to arbitrary refinement sequences.
4. The constant-normalized eventual criterion uses `Q_k/C=1+O(1/p_k)` plus Nicolas' quantitative RH/non-RH estimates. It is weaker in finite form than the exact `Q_k` criterion and must not be presented as an all-`k` inequality.
5. None of these scalar identities determines spectral edges or eigenvectors. A future edge/outlier mechanism cannot be rejected merely because the first moment is Nicolas data.
