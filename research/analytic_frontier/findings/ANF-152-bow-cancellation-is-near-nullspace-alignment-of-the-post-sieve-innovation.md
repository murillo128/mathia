# ANF-152 — bow cancellation is near-nullspace alignment of the post-sieve innovation

**Status:** `EXACT-DERIVED + GRAM-NORMAL-FORM + SPECTRAL-NECESSITY + SOURCE-SPECIFIC-GATE`. `ANF-149` reduced the bow branch to the fixed source `r_X=vartheta-Q_R`; `ANF-150` and `ANF-151` then showed that a sieve-conditioned independent control can match the finite Ramanujan pair profile and even a slowly growing Hardy--Littlewood local hierarchy while retaining the full diagonal bow variance. The remaining requirement can be sharpened beyond “some negative centered covariance.” The exact moving-window quadratic form is a Gram form. After normalizing its diagonal, the off-diagonal operator has universal lower spectral floor `-1`, and the bow target `V_X(U;K)=o(XK log X)` forces the actual post-sieve innovation to **asymptotically saturate that floor**. Equivalently, its diagonally weighted coefficient vector must concentrate in the vanishing-eigenvalue subspace of the normalized moving-window Gram matrix. Thus a viable source theorem must prove directional alignment with a near-kernel selected jointly by the window and the distinguished logarithmic twist; generic decorrelation, local tuple statistics, or merely negative covariance do not suffice.

## 1. The exact bow form is a normalized Gram Rayleigh quotient

Retain the source-normal form of `ANF-149`,

\[
r_X(n)=\vartheta(n)-Q_R(n)=Q_R(n)\eta_R(n),
\tag{1}
\]

and the exact bow seminorm

\[
V_X(U;K)
:=
\int_X^{2X}
\left|
\sum_{x<n\le x+K}r_X(n)n^{-iU}
\right|^2dx.
\tag{2}
\]

Let `I=I_{X,K}` be the finite set of integers whose moving-window atom is nonzero on `[X,2X]`, and define

\[
\phi_n(x)
:=
1_{[X,2X]}(x)
1_{\{x<n\le x+K\}}
 n^{-iU},
\qquad n\in I.
\tag{3}
\]

Then

\[
V_X(U;K)
=
\left\|
\sum_{n\in I}r_X(n)\phi_n
\right\|_{L^2([X,2X])}^2.
\tag{4}
\]

Write

\[
G_{mn}:=\langle\phi_n,\phi_m\rangle.
\tag{5}
\]

Up to the harmless convention for which index is conjugated,

\[
G_{mn}
=
\omega_K(m,n)
\left(\frac nm\right)^{-iU},
\tag{6}
\]

where `omega_K` is precisely the moving-window overlap from `ANF-102` and `ANF-149`. In particular `G` is Hermitian positive semidefinite because it is a Gram matrix. Its diagonal is

\[
d_n:=G_{nn}=\omega_K(n,n)>0
\qquad(n\in I).
\tag{7}
\]

The bow diagonal is therefore

\[
D_X(U;K)
:=
\sum_{n\in I}d_n|r_X(n)|^2,
\tag{8}
\]

which is independent of `U` and satisfies, by the established bow normalization,

\[
D_X(U;K)=(1+o(1))XK\log X.
\tag{9}
\]

Normalize the Gram matrix by its diagonal:

\[
C_{mn}
:=
\frac{G_{mn}}{\sqrt{d_md_n}},
\qquad
z_n:=\sqrt{d_n}\,r_X(n).
\tag{10}
\]

Then `C` is Hermitian positive semidefinite with unit diagonal, and the two quantities of interest become exactly

\[
\boxed{
V_X(U;K)=z^*Cz,
\qquad
D_X(U;K)=z^*z.
}
\tag{11}
\]

Thus the normalized bow variance is the Rayleigh quotient

\[
\boxed{
q_X(U;K)
:=
\frac{V_X(U;K)}{D_X(U;K)}
=
\frac{z^*Cz}{z^*z}
\ge0.
}
\tag{12}
\]

No asymptotic argument is used in (11)--(12); only (9) invokes the established arithmetic normalization.

## 2. The required negative covariance must saturate the universal floor

Separate the diagonal by writing

\[
B:=C-I.
\tag{13}
\]

The matrix `B` has zero diagonal. Because `C>=0`,

\[
\boxed{B\ge-I.}
\tag{14}
\]

The exact off-diagonal contribution in `ANF-149` is

\[
\mathcal C_X(U;K):=z^*Bz,
\tag{15}
\]

so (11) gives

\[
V_X=D_X+\mathcal C_X.
\tag{16}
\]

After division by `D_X`,

\[
\boxed{
\rho_X(U;K)
:=
\frac{\mathcal C_X(U;K)}{D_X(U;K)}
=q_X(U;K)-1
\ge-1.
}
\tag{17}
\]

Consequently the bow target is equivalent to

\[
\boxed{
V_X(U;K)=o(XK\log X)
\iff
q_X(U;K)=o(1)
\iff
\rho_X(U;K)=-1+o(1).
}
\tag{18}
\]

The last formulation is stronger conceptually than asking for “negative covariance.” The normalized off-diagonal term has an absolute floor `-1`, imposed only by positivity of the full Gram form, and the actual source must approach that floor asymptotically. For example, if one can prove merely

\[
\rho_X(U;K)\ge-1+\delta
\tag{19}
\]

for some fixed `delta>0` along the proposed bow sequence, then automatically

\[
V_X(U;K)\ge\delta D_X(U;K)
=(\delta+o(1))XK\log X,
\tag{20}
\]

which kills the bow target on that sequence. Conversely a theorem giving `rho_X=-c+o(1)` for any fixed `c<1`, even though macroscopically negative, is still insufficient.

For the actual post-sieve source, (1) makes the vector whose direction matters completely explicit:

\[
\boxed{
z_n
=\sqrt{\omega_K(n,n)}\,Q_R(n)\eta_R(n).}
\tag{21}
\]

Thus the unresolved arithmetic content is not an unspecified covariance of primes. It is extremal alignment of the deterministic centered innovation `eta_R`, under the positive rough weight `Q_R` and the exact edge weight, with a geometry determined by the distinguished logarithmic carrier.

## 3. Vanishing bow variance forces concentration in the near-kernel of the Gram matrix

The Rayleigh form yields a quantitative spectral necessity that is not visible in the scalar ledger alone. Let

\[
C=\sum_j\lambda_j u_ju_j^*,
\qquad
\lambda_j\ge0,
\tag{22}
\]

be a spectral decomposition, and for `tau>0` let `P_{>tau}` denote the spectral projector of `C` onto eigenvalues strictly larger than `tau`. From (12),

\[
q_X
=
\frac{\sum_j\lambda_j|\langle u_j,z\rangle|^2}
{\|z\|_2^2}.
\tag{23}
\]

Every term is nonnegative, so

\[
q_X
\ge
\tau
\frac{\|P_{>\tau}z\|_2^2}{\|z\|_2^2}.
\tag{24}
\]

Hence

\[
\boxed{
\frac{\|P_{>\tau}z\|_2^2}{\|z\|_2^2}
\le
\frac{q_X}{\tau}.
}
\tag{25}
\]

If the bow target holds, then for every fixed `tau>0`,

\[
\boxed{
\frac{\|P_{>\tau}z\|_2^2}{\|z\|_2^2}\longrightarrow0.
}
\tag{26}
\]

More quantitatively, whenever `q_X>0`, choosing

\[
\tau_X:=\sqrt{q_X}
\tag{27}
\]

gives

\[
\boxed{
\frac{\|P_{>\sqrt{q_X}}z\|_2^2}{\|z\|_2^2}
\le\sqrt{q_X}.
}
\tag{28}
\]

So a successful bow sequence forces `1-o(1)` of the weighted source energy into eigenspaces whose normalized Gram eigenvalues themselves tend to zero. In terms of `B=C-I`, the same statement says that the source must concentrate on eigenvalues of `B` approaching its universal floor `-1`.

This is a useful falsification criterion. If a proposed arithmetic input implies, for some fixed `tau,delta>0`,

\[
\|P_{>\tau}z\|_2^2\ge\delta\|z\|_2^2,
\tag{29}
\]

then (24) yields

\[
V_X(U;K)\ge\tau\delta\,D_X(U;K),
\tag{30}
\]

and the bow route fails. Thus even a very weak source-delocalization statement against the low-eigenvalue subspace would be decisive.

## 4. This separates geometric availability from arithmetic selection

The normalized matrix `C` depends on the moving-window geometry, the integer sites, and the twist `U`, but not on the values of the residual coefficients. The vector `z`, by contrast, contains the entire source law. This separates two questions that were mixed together earlier in the bow branch:

1. does the geometry possess low-Rayleigh directions at all?;
2. does the actual arithmetic source select them?

`ANF-146`--`ANF-148` already show why the first question cannot by itself prove anything favorable: relaxed coefficient choices can exploit the moving-window geometry, even with real coefficients, the exact logarithmic carrier, and actual prime sites. `ANF-150`--`ANF-151` then show that imposing increasingly rich local prime statistics still need not select the required direction. Equation (28) identifies the remaining requirement as a **directional** source statement rather than another marginal or local-main-term statement.

The sieved-Cramer control makes the contrast exact at the quadratic level. Its centered innovations are independent, so the expectation of every off-diagonal term vanishes and

\[
\mathbb E\,\mathcal C_X^{\rm rnd}(U;K)=0,
\qquad
\mathbb E\,V_X^{\rm rnd}(U;K)
=
\mathbb E\,D_X^{\rm rnd}(U;K).
\tag{31}
\]

Thus the control does not preferentially populate the near-floor directions in the signed aggregate, despite matching the local hierarchy established in `ANF-151`. The actual primes must display the opposite behavior at the distinguished `U`: their deterministic post-sieve innovation has to align almost maximally with the negative off-diagonal geometry.

This also rules out a misleading proof strategy. Showing that the post-sieve innovations are “random-like,” weakly correlated, or asymptotically decorrelated in a sense strong enough to imply

\[
\mathcal C_X=o(D_X)
\tag{32}
\]

would not move toward the bow target. It would imply instead

\[
V_X=(1+o(1))D_X,
\tag{33}
\]

which is the full diagonal obstruction. Any successful randomness principle would therefore have to be anisotropic and phase-sensitive enough to force the near-null alignment (26), not independence-like decorrelation.

## 5. Prior-art boundary and stress tests

The linear algebra in (11)--(28) is classical Gram-matrix/Rayleigh--Ritz theory, and no novelty is claimed for positive semidefinite correlation matrices or spectral projectors. The broader relation between prime variance in short intervals and two-point correlation is also classical: the Goldston--Montgomery line of work and its later refinements make second moments and pair correlations central objects, while Montgomery--Soundararajan show that actual prime short-interval fluctuations depart materially from naive Cramer heuristics. The literature audit therefore does not support presenting “variance equals a pair-correlation quadratic form” as new.

The Mathia-specific delta is narrower. `ANF-149`--`ANF-151` have already isolated the exact MRSTT post-sieve residual and eliminated a growing local Hardy--Littlewood hierarchy as the missing input. In that setting, (17)--(28) turn the remaining scalar sign condition into a quantitative **near-nullspace selection law for the actual deterministic source**. No external theorem is used in the derivation, so no new load-bearing literature dependency is introduced and `SOURCES.md` need not change.

The main stress tests are as follows. The normalization uses only indices with `d_n>0`; zero atoms are irrelevant to (2). Edge effects are retained exactly inside `omega_K`, so no Toeplitz or translation-invariant approximation is being assumed. The phase convention in (6) may be conjugated relative to the lag convention of `ANF-149`, but `G` remains the same Hermitian Gram form and its real quadratic value is unchanged. Equation (26) is a necessary condition for a successful bow sequence, not a claim that low-eigenvalue geometry alone forces arithmetic cancellation. Finally, expectation (31) for the random control is not a statement that every realization has Rayleigh quotient one; it is only the exact ensemble cancellation already used in `ANF-150`--`ANF-151`.

## 6. Consequence for the analytic bow frontier

The first unsupported bow implication can now be stated more sharply than “prove a negative centered covariance.” Let `C_{X,K,U}` be the exact diagonally normalized moving-window Gram matrix and let

\[
z_{X,K}(n)
=\sqrt{\omega_K(n,n)}Q_R(n)\eta_R(n).
\tag{34}
\]

A successful distinguished twist must satisfy

\[
\boxed{
\frac{z_{X,K}^*C_{X,K,U}z_{X,K}}
{\|z_{X,K}\|_2^2}
\longrightarrow0,
}
\tag{35}
\]

and hence the spectral concentration law (26). This provides two clean directions for the next source-specific step. One can try positively to prove that arithmetic structure places `z` in the near-kernel, perhaps through a signed bilinear/explicit-formula representation preserving the special logarithmic phase. Or one can try to kill the bow route by proving any nontrivial spectral delocalization such as (29). Both tests retain exactly the information that the conditioned independent controls discard.

For `analytic_frontier`, the bow branch is therefore no longer asking whether the primes possess some local anti-Bernoulli statistic. It asks whether the actual post-sieve innovation is an **asymptotically extremal vector for a specific positive-semidefinite moving-window operator**. That is a narrower, quantitative and directly falsifiable source gate.