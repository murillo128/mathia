# WI-129 — bounded-strip Riesz-basis theory cannot block Lamzouri screening

**Status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`. WI-128 shows that a positive-density bounded-depth off-line sector can make Lamzouri's horizontal remainder subextensive only if the normalized reciprocal-node Vandermonde develops a macroscopic near-null spectral sector. A natural attempted obstruction is to invoke scalar Paley--Wiener complete-interpolation / Pavlov--Muckenhoupt theory and deduce a uniform Riesz lower bound for the bounded-strip complex exponentials. That route is unavailable for the full conjugation-invariant Lamzouri family: the classical bounded-imaginary-part reduction sends every non-real conjugate pair to two identical real frequencies, so the projected scalar exponential family is not a Riesz basis. The correct neighboring prior art is therefore grouped/confluent exponential theory (exponential divided differences), not scalar complete interpolation.

This is a barrier on a proof strategy, not evidence that the WI-128 screening configuration actually exists. It does not construct a macroscopic near-null sector, quantify its possible density, or weaken WI-128. It rules out only the generic scalar-Riesz-basis shortcut for excluding such a sector.

## 1. Exact classical bounded-strip interface

Lyubarskii--Seip characterize complete interpolating sequences for Paley--Wiener spaces by a Muckenhoupt condition; for `p=2` their characterization coincides with the classical descriptions of unconditional bases of complex exponentials in `L^2(-pi,pi)` due to Pavlov, Nikol'skii, and Minkin.

For the particular bounded-strip reduction needed here, Semmler records the following exact theorem, attributing it to Corollary 1 of Section 8, Chapter 4 of R. M. Young's *An Introduction to Nonharmonic Fourier Series*: as long as the imaginary parts of a sequence `lambda_n` are bounded,

\[
\{e^{i\,\operatorname{Re}\lambda_n t}\}
\text{ is a Riesz basis of }L^2(-\pi,\pi)
\quad\Longleftrightarrow\quad
\{e^{i\lambda_n t}\}
\text{ is a Riesz basis of }L^2(-\pi,\pi).
\tag{1}
\]

The exact published quotation used here is Semmler (2010), which cites Young for the theorem. The present audit did not independently recover that numbered corollary from Young's book, so (1) is attributed at the evidence level actually checked: Semmler's peer-reviewed statement with Young provenance.

Sources:

- Gunter Semmler, *Complete interpolating sequences, the discrete Muckenhoupt condition, and conformal mapping*, Ann. Acad. Sci. Fenn. Math. 35 (2010), 23--46, DOI `10.5186/aasfm.2010.3502`.
- Yurii I. Lyubarskii and Kristian Seip, *Complete interpolating sequences for Paley-Wiener spaces and Muckenhoupt's (A_p) condition*, Rev. Mat. Iberoam. 13 (1997), 361--376, DOI `10.4171/RMI/224`, arXiv:`math/9511212`.
- R. M. Young, *An Introduction to Nonharmonic Fourier Series*, Academic Press, 1980; revised edition, Academic Press, 2001. The bounded-strip equivalence is cited by Semmler as Chapter 4, Section 8, Corollary 1.

## 2. Conjugation symmetry makes the scalar projected family degenerate

Consider one non-real zero label in Lamzouri's normalized frequency coordinates,

\[
\lambda=x+ib,\qquad \bar\lambda=x-ib,\qquad b\ne0.
\tag{2}
\]

The line's bounded-depth regime is precisely the hypothesis relevant to (1): `|b|` is uniformly bounded. But the real projections of the two labels coincide,

\[
\operatorname{Re}\lambda=\operatorname{Re}\bar\lambda=x.
\tag{3}
\]

Hence the projected scalar exponential family contains the same vector twice,

\[
e^{ixt},\qquad e^{ixt}.
\tag{4}
\]

A Riesz basis must satisfy a lower synthesis inequality

\[
A\sum_n|c_n|^2
\le
\left\|\sum_n c_n e^{i\mu_n t}\right\|_2^2
\qquad(A>0)
\tag{5}
\]

for finitely supported coefficients. On the two duplicate vectors in (4), choosing coefficients `(1,-1)` makes the right-hand side zero while the coefficient norm squared is `2`. Thus the projected family cannot be a Riesz basis. By (1), the full bounded-strip complex exponential family containing both members of every conjugate pair cannot be a scalar Riesz basis either.

Lamzouri's raw functions include a common envelope,

\[
f_z(u)=\eta(u)e^{-2\pi iuz}.
\tag{6}
\]

This does not restore the scalar Riesz-basis shortcut. Multiplication by the bounded function `eta` is a bounded operator on `L^2`; any sequence of coefficient vectors that drives the unweighted synthesis norm to zero also drives the weighted synthesis norm to zero up to the factor `\|\eta\|_\infty`. No lower Riesz bound can therefore be recovered merely by applying the common Lamzouri envelope.

The conclusion is deliberately limited to the full scalar family at critical complete-interpolation density. It does not say that every finite subfamily is ill-conditioned, nor that no carefully chosen subsequence can be a Riesz sequence.

## 3. Consequence for the WI-128 near-null sector

WI-128 proves that if `k/P >= rho > 0`, the off-line depths remain bounded, and the Lamzouri horizontal charge satisfies

\[
\frac{R_H}{PM}\longrightarrow0,
\tag{7}
\]

then the bottom `k` singular directions of the normalized reciprocal-node Vandermonde satisfy

\[
\frac1k
\sum_{\ell=P-k+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2
\longrightarrow0.
\tag{8}
\]

One might try to contradict (8) by proving that the complex nodes form a uniformly stable scalar complete-interpolating sequence in a fixed strip and then transfer its lower Riesz constant to finite sections. Equations (1)--(5) show why that cannot be the generic argument: conjugation symmetry itself already prevents the full scalar complex-frequency family from lying in the Riesz-basis class to which the Pavlov/Muckenhoupt characterization applies.

Therefore the following implication is invalid as a general route:

\[
\text{bounded off-line depth}
\Longrightarrow
\text{scalar complete interpolation with a uniform lower Riesz constant}
\Longrightarrow
\text{no WI-128 spectral-tail collapse}.
\tag{9}
\]

The first arrow fails structurally whenever a positive number of non-real conjugate pairs are retained in the full scalar family. This failure occurs before any special arithmetic property of zeta zeros is used.

Importantly, (9) being unavailable is not a construction of screening. A scalar system may fail to be a Riesz basis for reasons much weaker than the positive-density near-null condition (8). WI-128 therefore remains a genuine rigidity statement: a successful off-line screen must still arrange an extensive finite-section collapse, not merely fail a global basis criterion.

## 4. The correct neighboring theory is grouped / divided-difference stability

Lamzouri does not treat the conjugate pair as two unrelated scalar directions. It uses the adapted combinations

\[
g_z=\frac{f_z+f_{\bar z}}2,
\qquad
h_z=\frac{f_z-f_{\bar z}}{2i}.
\tag{10}
\]

This points directly toward the classical theory of exponential divided differences. Avdonin--Ivanov study clustered exponential frequencies whose scalar exponential basis degenerates as nodes approach one another and replace each cluster by suitable divided-difference combinations, obtaining Riesz-basis descriptions for the grouped system. Avdonin--Moran develop corresponding Ingham-type inequalities and generalized divided differences for finite unions of uniformly discrete sequences.

The match is especially transparent in the near-line limit. With `z=x+ib`,

\[
\frac{h_z(u)}b
=
\frac{\eta(u)e^{-2\pi iux}}{2ib}
\left(e^{2\pi bu}-e^{-2\pi bu}\right)
\longrightarrow
-2\pi i\,u\,\eta(u)e^{-2\pi iux},
\tag{11}
\]

which is the derivative/confluent exponential direction up to the conventional scalar. Thus when a mirror pair coalesces toward the critical line, the normalized anti-invariant direction is exactly of divided-difference type.

Sources:

- S. A. Avdonin and S. A. Ivanov, *Exponential Riesz bases of subspaces and divided differences*, Algebra i Analiz 13:3 (2001), 1--17; English translation St. Petersburg Math. J. 13:3 (2002), 339--351; arXiv:`math/0103160`.
- S. Avdonin and W. Moran, *Ingham-type inequalities and Riesz bases of divided differences*, Int. J. Appl. Math. Comput. Sci. 11:4 (2001), 803--820.

For fixed depth bounded away from zero, (10) is simply an invertible two-by-two change of columns within each pair; it does not create a scalar complete-interpolation theorem that was absent for the raw family. What is needed for the WI-128 program is instead a quantitative statement about grouped/subspace finite sections: either a lower bound on the relevant anti-invariant residual sector, or a theorem showing that positive-density collapse of that sector forces additional geometric structure incompatible with zeta.

## 5. What remains open

This audit closes only the scalar complete-interpolation shortcut. Three routes remain logically live:

1. derive quantitative finite-section bounds for the `g/h` grouped system from divided-difference or vector-valued interpolation theory, strong enough to control a positive-density singular-value tail rather than a single determinant or `sigma_min`;
2. use zeta-specific spacing/correlation information to rule out the collective reciprocal-node geometry required by WI-128; or
3. combine Lamzouri's horizontal remainder with a second invariant that survives the scalar basis degeneracy and produces a defect-to-zero bootstrap.

The near-line limit (11) makes the first route substantially better targeted than a generic search for scalar `A_2` conditions. A useful future theorem must distinguish the expected pairwise confluent degeneracy from the much stronger macroscopic collective collapse demanded by WI-128.

## 6. Novelty and claim boundary

The scalar Paley--Wiener/Muckenhoupt theory and exponential divided-difference theory are classical prior art and are not claimed as new. The Mathia contribution in this finding is the exact application to the WI-128 screening program: conjugation symmetry kills the proposed scalar complete-interpolation obstruction and identifies grouped/confluent finite-section stability as the correct adjacent theorem surface.

No unconditional zeta-zero proportion changes. No existence of off-line screening is asserted. No claim of priority is made for the observation beyond recording the route audit for this research line.