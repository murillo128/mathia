# NB-024 — Möbius locking forces target-selected normalized Gram ill-conditioning

**Status:** `EXACT-DERIVED + TARGET-AWARE-MOBIUS-LOCKING + NORMALIZED-GRAM-ILL-CONDITIONING + TARGET-SELECTED-NEAR-NULL-MASS + NEGATIVE/METHOD-BOUNDARY`. `NB-001` shows that generator Gram data alone cannot determine the fixed Nyman target distance, while `NB-020` shows that a small canonical residual forces an inverse-distance block of projection coefficients toward the Möbius pattern. Combining those two facts with the exact harmonic-shell size of the canonical generators gives a one-way spectral consequence that is useful for the finite-section program: **good Nyman approximation forces the canonically normalized discrete Gram system to become ill-conditioned.**

Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},\qquad
r_N=e-P_Ne,\qquad d_N=\|r_N\|,
\tag{1}
\]

and write

\[
P_Ne=\sum_{n=2}^N a_{N,n}g_n.
\tag{2}
\]

Normalize the individual canonical generators by

\[
\phi_n:=\frac{g_n}{\|g_n\|},
\qquad
\widetilde G_N=(\langle\phi_j,\phi_k\rangle)_{2\le j,k\le N},
\tag{3}
\]

and put

\[
\alpha_{N,n}:=a_{N,n}\|g_n\|,
\qquad
P_Ne=\sum_{n=2}^N\alpha_{N,n}\phi_n.
\tag{4}
\]

There are absolute constants `c,C>0` such that, with

\[
X_N:=\left\lfloor\min\left\{N,\frac{c}{d_N}\right\}\right\rfloor,
\tag{5}
\]

whenever `X_N>=C`,

\[
\boxed{
\|\alpha_N\|_2^2\ge c\log X_N.
}
\tag{6}
\]

Since

\[
\alpha_N^*\widetilde G_N\alpha_N
=\|P_Ne\|^2
=1-d_N^2,
\tag{7}
\]

the **target-selected Rayleigh quotient** therefore satisfies

\[
\boxed{
\mathcal R_N
:=\frac{\alpha_N^*\widetilde G_N\alpha_N}{\|\alpha_N\|_2^2}
\le\frac{C}{\log X_N}.
}
\tag{8}
\]

Consequently

\[
\boxed{
\lambda_{\min}(\widetilde G_N)
\le\frac{C}{\log X_N},
\qquad
\kappa_2(\widetilde G_N)
\ge c\log X_N.
}
\tag{9}
\]

The conclusion is stronger than existence of an abstract small eigenvalue: the actual target-selected coefficient vector is forced into the low spectral sector. If `\Pi_N` denotes the spectral projector of `\widetilde G_N` onto eigenvalues at most `2\mathcal R_N`, then

\[
\boxed{
\|\Pi_N\alpha_N\|_2^2
\ge\frac12\|\alpha_N\|_2^2.
}
\tag{10}
\]

Thus at least half of the Euclidean mass of the normalized best-approximation coefficient vector lies in modes whose eigenvalue is `O(1/log X_N)`.

This is deliberately one-way. It does **not** say that Gram ill-conditioning implies good approximation, nor that the small-eigenvalue sector carries a fixed fraction of the Hilbert projection energy. `NB-001`'s matched inner-factor control forbids that reversal without target information. The result instead closes a natural canonical-basis shortcut: a uniformly Riesz-stable normalized discrete Nyman family is incompatible with `d_N->0`.

## 1. The Möbius-locked indices have logarithmic harmonic mass

`NB-020` supplies absolute constants `c_0,C_0,x_0>0` and, for all sufficiently large `x`, the set

\[
\mathcal S(x)
:=\{n\le x:\mu(n)^2=1,\ \sigma(n)\le C_0n\}
\tag{11}
\]

with the weighted-density estimate

\[
\sum_{n\in\mathcal S(x)}n\ge c_0x^2.
\tag{12}
\]

It also proves the exact target-residual locking bound

\[
|a_{N,n}+\mu(n)|\le2d_N\sigma(n)
\qquad(2\le n\le N).
\tag{13}
\]

Choose the absolute constant `c` in (5) small enough that `2C_0c<=1/2`. Then every `n in S(X_N)` obeys

\[
|a_{N,n}+\mu(n)|\le\frac12,
\]

and because those indices are squarefree,

\[
\boxed{|a_{N,n}|\ge\frac12.}
\tag{14}
\]

For the normalized Gram problem, weighted density by `n` is not yet the right statistic: the generator norm has size at least a constant times `n^{-1/2}`. What is needed is harmonic mass. That already follows from (12) with no additional number theory.

Fix an absolute `R>1` so large that `R^{-2}<=c_0/4`. For sufficiently large `y`,

\[
\sum_{n\le y/R}n\le\frac{c_0}{2}y^2.
\tag{15}
\]

Subtracting this crude upper bound from (12) gives

\[
\sum_{\substack{n\in\mathcal S(y)\\y/R<n\le y}}n
\ge\frac{c_0}{2}y^2.
\tag{16}
\]

Since every index in this annulus is at most `y`, it contains at least `(c_0/2)y` good indices, and hence

\[
\sum_{\substack{n\in\mathcal S(y)\\y/R<n\le y}}\frac1n
\ge\frac{c_0}{2}.
\tag{17}
\]

Apply (17) on the disjoint geometric annuli with endpoints
`X_N,X_N/R,X_N/R^2,...` until the fixed threshold `x_0` is reached. There are `asymp log X_N` such annuli, so

\[
\boxed{
\sum_{n\in\mathcal S(X_N)}\frac1n
\ge c_1\log X_N
}
\tag{18}
\]

for an absolute `c_1>0` once `X_N` is large. This logarithmic extraction is the extra step needed to pass from the coefficient core of `NB-020` to a scale-normalized Gram statement.

## 2. Canonical generator normalization costs exactly the harmonic weight needed above

In Bagchi's harmonic-shell realization,

\[
g_n|_{I_t}=\left\{\frac tn\right\},
\qquad
I_t=\left(\frac1{t+1},\frac1t\right],
\qquad
|I_t|=\frac1{t(t+1)}.
\tag{19}
\]

For `1<=t<n`, the fractional part is `t/n`, so

\[
\begin{aligned}
\|g_n\|^2
&\ge
\sum_{t=1}^{n-1}
\frac{(t/n)^2}{t(t+1)}\\
&=\frac1{n^2}
\sum_{t=1}^{n-1}\frac{t}{t+1}\\
&\ge\frac{n-1}{2n^2}
\ge\frac1{4n}
\qquad(n\ge2).
\end{aligned}
\tag{20}
\]

Combining (14), (18), and (20),

\[
\begin{aligned}
\|\alpha_N\|_2^2
&=\sum_{n=2}^N|a_{N,n}|^2\|g_n\|^2\\
&\ge
\sum_{n\in\mathcal S(X_N)}
\frac14\cdot\frac1{4n}\\
&\ge c_2\log X_N,
\end{aligned}
\tag{21}
\]

which proves (6).

The normalization in (3) matters. The unnormalized Gram matrix can be made better or worse conditioned by trivial diagonal rescaling of the generators. Equation (21) removes that particular artifact: every dictionary atom has norm one before the spectral statement is made. It does **not** make the spectrum invariant under arbitrary invertible recombination of the finite span; an orthonormal basis of `V_N` would of course have Gram matrix equal to the identity.

## 3. The best-approximation vector itself witnesses the small spectral scale

The canonical generators are linearly independent, so `\widetilde G_N` is positive definite. By (4),

\[
\alpha_N^*\widetilde G_N\alpha_N
=\left\|\sum_{n=2}^N\alpha_{N,n}\phi_n\right\|^2
=\|P_Ne\|^2
=1-d_N^2.
\tag{22}
\]

Dividing by (21) proves (8), and the variational characterization of the smallest eigenvalue gives the first half of (9).

Every diagonal entry of `\widetilde G_N` equals one, so

\[
\operatorname{tr}\widetilde G_N=N-1.
\tag{23}
\]

Therefore `lambda_max(\widetilde G_N)>=1`, and the second half of (9) follows.

For the spectral concentration statement, diagonalize `\widetilde G_N` and decompose `\alpha_N` into its eigenbasis. Let `H` be the coefficient mass on eigenvalues greater than `2\mathcal R_N`. Then

\[
\alpha_N^*\widetilde G_N\alpha_N
>2\mathcal R_N H.
\tag{24}
\]

But the left side is exactly `\mathcal R_N\|\alpha_N\|_2^2`, so `H<=\|\alpha_N\|_2^2/2`. This proves (10).

The distinction between coefficient mass and Hilbert energy is load-bearing. Equation (10) does not imply that half of `1-d_N^2` is contributed by the low-eigenvalue sector; multiplication by the eigenvalues can suppress its Hilbert contribution strongly. The theorem says that the canonical least-squares coefficients must pay growing Euclidean mass in weak Gram directions as the target is approximated more accurately.

## 4. Consequences for closure and quantitative-rate scenarios

If the discrete Nyman criterion closes, so that

\[
d_N\longrightarrow0,
\tag{25}
\]

then both arguments of the minimum in (5) tend to infinity. Hence (9) gives immediately

\[
\boxed{
\kappa_2(\widetilde G_N)\longrightarrow\infty.
}
\tag{26}
\]

In particular **RH implies that the norm-normalized canonical Báez-Duarte finite dictionaries are not uniformly Riesz stable.** This is a necessary geometric consequence of closure, not evidence for closure.

Burnol's unconditional distance floor sharpens the parameter in (5) on any closure subsequence. For sufficiently large `N`,

\[
d_N^2\gg\frac1{\log N},
\tag{27}
\]

so `d_N^{-1}=O(\sqrt{\log N})=o(N)`. Therefore, whenever `d_N->0`, the inverse-distance branch in (5) is eventually the active one and

\[
\boxed{
\kappa_2(\widetilde G_N)
\ge c\log\frac1{d_N}.
}
\tag{28}
\]

Under a Burnol-saturating scenario

\[
d_N^2\log N\longrightarrow B>0,
\tag{29}
\]

which includes the conditional optimal scale studied by Bettin--Conrey--Farmer when their hypotheses hold, (28) yields

\[
\boxed{
\kappa_2(\widetilde G_N)\gg\log\log N.
}
\tag{30}
\]

No claim is made that this lower bound is sharp. Numerical or analytic Gram conditioning may deteriorate much faster. The point is logical: **uniform canonical conditioning is unavailable on the very branch the Nyman criterion seeks to prove.** Any finite-section argument that needs an `N`-independent lower Riesz bound for the norm-normalized canonical generators would therefore be incompatible with closure rather than a route to it.

## 5. Prior-art boundary and adversarial controls

The load-bearing mathematics is internal to the current Nyman line plus the classical sources already anchored in `SOURCES.md`: Bagchi's harmonic-shell realization, Burnol's distance floor, and the target-selected coefficient locking established in `NB-020`. No new external theorem is required, so `SOURCES.md` is unchanged.

A targeted prior-art check covered classical numerical Nyman--Beurling finite-section work, Ehm's 2024 Gram-kernel analysis (`arXiv:2405.06349`), recent Gram block-compressibility work (`arXiv:2510.18132`), searches for normalized Gram condition numbers, Riesz-sequence formulations, and optimal-coefficient conditioning. The located work studies Gram formulas, numerical approximation, or generator-geometry decay, but the search did not locate the implication (6)--(10) from the target-selected Möbius coefficient core. Search absence is not a novelty proof, and this finding is classified `EXACT-DERIVED`, not as a claim of literature priority.

Several controls prevent overinterpretation.

First, condition number is still a dictionary-coordinate quantity. Unit-norm normalization removes arbitrary **diagonal** scaling, but an arbitrary invertible basis change can alter the spectrum, and an orthonormalized basis has condition number one. The result concerns the canonical arithmetic dictionary, not the abstract subspace `V_N` alone.

Second, (9) is only a necessary consequence of small `d_N`. Large condition number does not imply a small target distance. This is exactly consistent with `NB-001`, which constructs common-inner matched controls with identical generator Gram data and radically different target distances.

Third, (10) concerns Euclidean coefficient mass, not target projection energy. It cannot be substituted for a lower bound on `b_N^*G_N^{-1}b_N`, a visibility fraction, or the `NB-015` enrichment budget.

Fourth, the logarithmic harmonic-mass extraction depends on the positive weighted-density subset in `NB-020`; weakening that input to isolated Möbius-locked indices would not suffice. Conversely no prime number theorem, zero-density estimate, or unproved cancellation hypothesis enters (18).

Finally, (28)--(30) use Burnol only to identify the active inverse-distance branch and interpret a quantitative closure scenario. The finite theorem (6)--(10) is independent of Burnol.

## 6. Research consequence

The target-aware finite-section route now has a sharper conditioning boundary. `NB-001` says Gram geometry without target alignment is non-identifying; this finding adds that **even after canonical norm normalization, the best target coefficients themselves force increasing occupancy of near-null Gram modes whenever the Nyman distance closes.** Therefore a successful spectral method cannot simply prove that the canonical Gram family stays uniformly well conditioned and then invert it stably. It must instead control how the fixed target threads through a progressively ill-conditioned arithmetic dictionary, or reorganize the span into a genuinely different multiscale basis while transporting the target data exactly.

This does not resolve the accepted scale-coupled visibility clue. It narrows one of its possible supporting strategies: any proposed source-specific visibility estimate that passes through a uniform Riesz lower bound for the normalized canonical generators is incompatible with the desired closure branch. A useful continuation must exploit target-weighted small modes rather than trying to eliminate them.