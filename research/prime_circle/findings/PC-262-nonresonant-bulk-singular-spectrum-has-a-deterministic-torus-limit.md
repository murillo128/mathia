# PC-262 — nonresonant bulk singular spectrum has a deterministic torus limit

**Status:** `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY` for the nonresonant bulk spectral-distribution part of the growing shared-upper cocycle left after PC-257--PC-261.

Let

\[
2<p_n<r_n<q_n
\]

be distinct primes with `q_n -> infinity`, and write

\[
\alpha_n=\frac{p_n}{q_n}\longrightarrow\alpha,
\qquad
\beta_n=\frac{r_n}{q_n}\longrightarrow\beta,
\qquad
0<\alpha<\beta<1.
\tag{1}
\]

Assume

\[
\boxed{1,\alpha,\beta\ \text{are linearly independent over }\mathbb Q.}
\tag{2}
\]

For the native shared-upper defect of PC-251,

\[
D_n=D_{p_n,r_n;q_n},
\qquad
\Delta_n=\frac{D_n}{q_n\sqrt{p_nr_n}},
\tag{3}
\]

let `sigma_1(Delta_n),...,sigma_{p_n}(Delta_n)` be its singular values, including zeros, and define the singular-square empirical measure

\[
\nu_n
=\frac1{p_n}\sum_{j=1}^{p_n}
\delta_{\sigma_j(\Delta_n)^2}.
\tag{4}
\]

Then there is a probability measure `nu_{alpha,beta}` such that

\[
\boxed{\nu_n\Longrightarrow\nu_{\alpha,\beta}.}
\tag{5}
\]

The limit is determined entirely by the induced Haar return process of the torus translation

\[
T_{\alpha,\beta}(x,y)=(x+\alpha,y+\beta)\pmod1
\tag{6}
\]

to the PC-258 collision rectangle

\[
W_{\alpha,\beta}=[1-\alpha,1)\times[1-\beta,1),
\tag{7}
\]

together with the explicit Green weight

\[
\rho(x,y)
=\sqrt{\alpha\beta}\,
G\!\left(\frac{1-x}{\alpha},\frac{1-y}{\beta}\right),
\qquad
G(u,v)=\min(u,v)-uv.
\tag{8}
\]

In particular, the **entire normalized bulk singular-value distribution** is sequence-independent once the irrational limiting ratios `(alpha,beta)` are fixed. It is therefore not a prime-specific carrier: the same limit is obtained by the corresponding pairwise-coprime rational-partition controls with the same nonresonant limiting ratios. This is stronger than PC-256's fixed-moment classicalization but deliberately weaker than a full no-go for the long cocycle. Spectral edges, Lyapunov/log-determinant observables, fine spacing, and other non-bulk quantities remain outside (5).

## 1. Rational independence automatically gives the PC-258 nonresonance condition

PC-258 proves Haar equidistribution of the finite rational torus orbit provided every fixed nonzero Fourier mode eventually stops resonating. Condition (2) implies exactly that.

Fix `(h,k) in Z^2 \setminus {(0,0)}`. If infinitely many `n` satisfied

\[
q_n\mid hp_n+kr_n,
\tag{9}
\]

then along a subsequence

\[
\frac{hp_n+kr_n}{q_n}=\ell_n\in\mathbb Z.
\tag{10}
\]

The left side is bounded, so a further subsequence has `ell_n=ell` constant. Passing to the limit gives

\[
h\alpha+k\beta=\ell,
\tag{11}
\]

contradicting (2). Hence for every fixed nonzero `(h,k)`, (9) fails eventually. PC-258 therefore gives

\[
\mu_n:=\frac1{q_n}\sum_{u=0}^{q_n-1}
\delta_{T_{\alpha_n,\beta_n}^{u}(0,0)}
\Longrightarrow m_{\mathbb T^2},
\tag{12}
\]

and the collision count `k_n` obeys

\[
\boxed{\frac{k_n}{q_n}\longrightarrow\alpha\beta.}
\tag{13}
\]

No Diophantine rate is required for the bulk conclusion below. Rational independence is used only to remove every fixed bounded Fourier resonance in the limit.

## 2. Successive collision returns have a uniform finite raw-window bound

A fixed collision-index neighborhood must be reducible to a fixed raw torus window before PC-258's local equidistribution can be applied. In the irrational limit this follows from minimality.

By (2), the translation (6) is minimal. Choose a closed rectangle `W^circ` strictly inside the interior of (7). Since every orbit of a minimal compact dynamical system visits every nonempty open set, the sets

\[
T_{\alpha,\beta}^{-j}(\operatorname{int}W^\circ),
\qquad j\ge0,
\tag{14}
\]

cover `T^2`. Compactness gives a finite subcover. Consequently there is an `L<infinity` such that every point of the limit torus hits `W^circ` within at most `L` forward iterates.

This finite cover is robust. Because the finitely many translations in (14) and the collision rectangle vary continuously with `(alpha,beta)`, after shrinking `W^circ` once if necessary the same finite family remains a cover for all sufficiently large `(alpha_n,beta_n)`. Since `W^circ` then lies inside `W_{alpha_n,beta_n}`, every sufficiently large rational orbit has a collision at least once in every `L` consecutive raw cells.

Thus for every fixed integer `s`, a window of `s` consecutive collision events is determined by at most `sL+O(1)` consecutive raw torus iterates. The determining rule is piecewise continuous in the starting torus point and in `(alpha_n,beta_n)`; its discontinuity set lies in a finite union of translated rectangle boundaries and therefore has Haar measure zero.

This step is where the nonresonant irrational hypothesis matters. PC-261 shows that at a rational resonant limiting point the exact bounded resonance lift can change the complete normalized defect by `O(1)` even when the limiting ratios agree, so no statement like (5) can be inferred there from the ratio pair alone.

## 3. Every fixed spectral moment is a bounded local return observable

Use the PC-251/PC-254 ordered collision factorization

\[
D_n=-U_nW_nV_n^T.
\tag{15}
\]

After native normalization put

\[
R_n=\operatorname{diag}(\rho_{n,1},\ldots,\rho_{n,k_n}),
\qquad
\rho_{n,a}=\frac{w_{n,a}}{q_n\sqrt{p_nr_n}}.
\tag{16}
\]

Then

\[
\Delta_n=-U_nR_nV_n^T.
\tag{17}
\]

PC-257 gives the two path Gram matrices

\[
G_{p,n}=U_n^TU_n,
\qquad
G_{r,n}=V_n^TV_n,
\tag{18}
\]

with diagonal entries `2` and nearest-neighbor off-diagonals `-epsilon_a` and `-eta_a`. The nonzero squared singular values of `Delta_n` are therefore the eigenvalues of

\[
M_n=R_nG_{r,n}R_nG_{p,n}.
\tag{19}
\]

For every fixed `m>=1`,

\[
\int x^m\,d\nu_n(x)
=\frac1{p_n}\operatorname{tr}(M_n^m).
\tag{20}
\]

The matrix `M_n` has bandwidth two. Hence the diagonal entry `(M_n^m)_{aa}` depends only on the weights and adjacency bits in a collision-index neighborhood of radius at most `2m`. By Section 2, for sufficiently large `n` this neighborhood is determined by a raw torus window of length bounded only by `m`, not by `n`.

The PC-258 formulas make every local coefficient explicit. A collision at raw cell `u` has

\[
\rho_{n,u}
=\sqrt{\alpha_n\beta_n}\,
G\!\left(
\frac{1-\{u\alpha_n\}}{\alpha_n},
\frac{1-\{u\beta_n\}}{\beta_n}
\right),
\tag{21}
\]

while the adjacency bits are finite-return functions of the same mechanical boundary words. Therefore `(M_n^m)_{aa}` is a bounded piecewise-continuous function of a fixed finite torus orbit segment. Its discontinuity set has Haar measure zero.

Equation (12), applied to the finite partition generated by that window, gives convergence of its empirical average. Combining this with (13) and `p_n/q_n -> alpha` yields, for every fixed `m`, a deterministic limit

\[
\boxed{
\lim_{n\to\infty}\int x^m\,d\nu_n(x)
=\mathcal M_m(\alpha,\beta),
}
\tag{22}
\]

where `M_m(alpha,beta)` is the corresponding induced-Haar integral. In particular, it depends only on `(alpha,beta)` and the universal return/Green rules, not on which prime sequence approaches those ratios.

This is the all-bulk extension of PC-256. There, every fixed moment was shown to be a finite shifted collision correlation but the complete spectral distribution was left open. Here the nonresonant torus limit fixes **all** those moments simultaneously, one fixed degree at a time.

## 4. Uniform compact support turns moment convergence into spectral-measure convergence

Moment convergence alone would not determine a measure on an unbounded interval. The native Prime-Circle normalization supplies a uniform support bound.

Each column of `U_n` or `V_n` is a first-difference vector on a path. Consequently `G_{p,n}` and `G_{r,n}` are principal submatrices of path-incidence Gram matrices, whose operator norm is at most `4`. Hence

\[
\|U_n\|\le2,
\qquad
\|V_n\|\le2.
\tag{23}
\]

The Green kernel satisfies `0<=G(u,v)<=1/4`, so PC-258 gives

\[
0\le\rho_{n,a}\le\frac{\sqrt{\alpha_n\beta_n}}4.
\tag{24}
\]

From (17),

\[
\boxed{
\|\Delta_n\|
\le\|U_n\|\,\|R_n\|\,\|V_n\|
\le\sqrt{\alpha_n\beta_n}<1.
}
\tag{25}
\]

Thus all measures `nu_n` are eventually supported in one fixed compact interval, for example `[0,1]`. The Hausdorff moment problem on a compact interval is determinate. The limits (22), together with total mass one, therefore define a unique probability measure `nu_{alpha,beta}`, and polynomial approximation of continuous functions gives the weak convergence (5).

There is also a forced structural zero sector. PC-251 gives `rank D_n=k_n`, so (13) implies

\[
\frac{p_n-k_n}{p_n}\longrightarrow1-\beta.
\tag{26}
\]

Hence

\[
\nu_{\alpha,\beta}(\{0\})\ge1-\beta.
\tag{27}
\]

Equality is **not** asserted: positive finite-volume singular values may themselves accumulate at zero. This is precisely one reason log-determinant and Lyapunov questions are not consequences of the bulk weak limit.

## 5. Prior art: the mechanism is an integrated-density-of-states mechanism

The abstract mechanism behind (5) is classical spectral dynamics, not a new arithmetic construction. Uniform ergodic theorems for strictly/uniquely ergodic finite-pattern systems and existence of deterministic integrated densities of states for finite-range equivariant operators are standard. Direct anchors include:

- Daniel Lenz, **Uniform ergodic theorems on subshifts over a finite alphabet**, *Ergodic Theory and Dynamical Systems* 22:1 (2002), 245--255, DOI `10.1017/S0143385702000111`, arXiv:`math/0005067`.
- Daniel Lenz and Peter Stollmann, **An ergodic theorem for Delone dynamical systems and existence of the integrated density of states**, *Journal d'Analyse Mathematique* 97 (2005/2006), 1--24, DOI `10.1007/BF02807400`, arXiv:`math-ph/0310017`.
- Daniel Lenz, Fabian Schwarzenberger and Ivan Veselic, **A Banach space-valued ergodic theorem and the uniform approximation of the integrated density of states**, *Geometriae Dedicata* 150 (2011), 1--34, DOI `10.1007/s10711-010-9491-x`, arXiv:`1003.3620`.

Those papers are broader operator/ergodic frameworks; they are not cited as containing the specific Prime-Circle collision matrix. The project-local derivation above instead uses PC-251's exact Green-weighted matching, PC-257's finite interaction width, and PC-258's rational-torus coding to place this source-forced carrier inside the classical IDS paradigm.

No novelty is claimed for unique ergodicity, finite-range spectral moments, the Hausdorff moment problem, or integrated density of states. The durable consequence is the exact boundary for Mathia: after bounded resonances are removed by (2), the normalized **bulk** spectrum of this surviving collision carrier loses dependence on the particular prime approximants and is fixed by ordinary torus dynamics.

## 6. Matched controls and RH-facing consequence

The derivation of Sections 2--4 uses only the uniform rational partitions, coprimality needed to avoid boundary degeneracies, the Green collision weight, and the limiting torus ratios. None of those steps uses a property that distinguishes prime labels from pairwise-coprime integer controls. The same proof therefore applies to any admissible pairwise-coprime rational-partition sequence with the same irrational limiting `(alpha,beta)`.

Consequently, a proposed RH mechanism based only on the weak limiting histogram of normalized singular values, any fixed continuous test of that histogram, or any finite collection of its moments cannot recover source-specific prime information in this regime. It sees an IDS-type object of the classical induced torus system.

This does **not** close the long-cocycle frontier left by PC-257. Weak empirical spectral convergence is insensitive to several quantities that can depend on rare or exponentially amplified behavior. Still open are, in particular:

- the extreme singular values and possible sequence-dependent outliers;
- fine eigenvalue spacing and edge scaling;
- normalized log determinants or Lyapunov exponents, where the singularity at zero invalidates passage from weak convergence alone;
- rotation/winding/discriminant data of the growing transfer product not expressible as a continuous bulk spectral statistic;
- regimes approaching rational resonance, where PC-261 already proves ratio-only universality false.

Thus the surviving question is narrower than after PC-261: **any genuinely new nonresonant invariant must live beyond the ordinary bulk density of states.** It must exploit an edge, a singular/noncontinuous functional, or another global cocycle feature and still distinguish the prime-circle source from its rational-partition control.

## 7. Falsification and boundary audit

The claim can be attacked at several independent points.

1. For a fixed `m`, construct two prime sequences satisfying (1)--(2) for which the normalized moment in (20) has different limits. This would falsify the local-return reduction or its equidistribution step.
2. Exhibit arbitrarily long collision-free raw intervals along sufficiently close approximants to a fixed rationally independent `(alpha,beta)`. This would contradict the robust syndetic-return argument in Section 2.
3. Produce a collision chain for which `(M_n^m)_{aa}` depends on data outside a radius `2m`, contrary to the bandwidth-two form (19).
4. Violate the uniform norm bound (25) using the exact PC-251 factorization and PC-258 Green weights.
5. Construct an admissible pairwise-coprime rational-partition control with the same limiting torus data but a different bulk limit while preserving the same local return rules.

The theorem makes no assertion at rationally dependent limiting ratios and no uniform statement as `(alpha,beta)` approaches a resonance. It also makes no claim that `nu_{alpha,beta}` alone contains enough information to reconstruct the transfer cocycle. Those exclusions are essential rather than technical: PC-261 already supplies an all-prime resonant counterexample to ratio-only operator universality.