# PF-349 — local full-parity transition shorting retains the narrow-band angle

**Status:** EXACT-DERIVED + LOCAL-PDE-FORM-COMPARISON + NARROW-BAND-OBSTRUCTION + GLOBAL-TRANSITION-ANGLE-OPEN.

PF-348 retains an order-one edge correlation after shorting the symmetric cosine transition modes of an actual two-pant Dirichlet module. Here the same obstruction survives freeing **both face parities and all sine/cosine modes in the local transition band**. The antisymmetric seam penalty controls its relaxation in relative form order, before the potentially ill-conditioned symmetric transition block is eliminated. Tangential reflection makes the sine sector irrelevant to the even witnesses.

All other cuff traces remain zero. This removes the local parity restriction, but does not establish a lower bound after transition variables on neighboring modules are freed. It is not a global noncompactness or RH result.

## Exact local object and statement

Use the natural simultaneous seam cut, positive shift, and common zero-twist physical coordinate of PF-205/PF-216/PF-340. Fix `kappa>0`. For `0<eta<1`, set

\[
L=L_n,\quad w=w_n,\quad d=2\pi/L,\quad
\alpha=d\lfloor\kappa/d\rfloor,\quad
\beta=d\lceil(\kappa+\eta)/d\rceil,
\]
\[
J=\{\alpha,\alpha+d,\ldots,\beta\},\quad
X=\{\alpha,\beta\},\quad T=J\setminus X,\quad N=|J|.
\tag{1}
\]

For large `n`, `T` is precisely the positive Fourier lattice in `(kappa,kappa+eta)`, and

\[
N=\frac{\eta L}{2\pi}+O(1).
\tag{2}
\]

Let `e_alpha,e_beta` be the normalized symmetric two-face cosine modes. Prescribe their coefficients `x=(x_alpha,x_beta)`, set every other nontransition boundary coefficient to zero, and free every transition mode on **both faces of this module only**. Let `S_n^loc` be the resulting positive two-dimensional form:

\[
x^*S_n^{\rm loc}x
=\min_{t\in\mathcal T_n^{\rm full}}
\mathcal E_{Q+\Lambda_E}(x_\alpha e_\alpha+x_\beta e_\beta+t),
\tag{3}
\]

where `mathcal T_n^full` includes both face parities and both tangential sine/cosine sectors at the frequencies in `T`. This is a local Dirichlet finite section, not an exterior relaxation of the other cuffs.

There exists `eta_1>0`, independent of `n`, such that for each fixed `0<eta<eta_1`, after a finite head depending on `eta`,

\[
\boxed{\frac{|(S_n^{\rm loc})_{12}|}
{\sqrt{(S_n^{\rm loc})_{11}(S_n^{\rm loc})_{22}}}\ge\frac14.}
\tag{4}
\]

More precisely, if `S_n^D` denotes PF-348's symmetric-cosine-only shorting, then

\[
\boxed{(1+b_n)^{-1}S_n^D\le S_n^{\rm loc}\le S_n^D,
\qquad b_n\le C\eta+o(1).}
\tag{5}
\]

The constant `C` can be chosen uniformly for `0<eta<1`, with fixed `kappa`. The tail limit in (5) is at fixed `eta`; it is not a shrinking-band theorem.

## 1. Tangential reflection and face parity are different decompositions

Each adjacent one-cusp pant has the natural reflection fixing its orthogeodesics. It acts by `t -> -t` in the cuff coordinate centered at the finite-finite seam foot. Its constant-distance strip removals and the zero boundary values on the other cuff are invariant. The positive shifted Dirichlet energy is therefore invariant, so the pant self-DtN form commutes with this reflection. The seam metric has the same invariance. Zero twist aligns the two origins.

Consequently the local complete form is an orthogonal sum of its even cosine and odd sine forms. For an even retained datum, minimizing over odd transition modes gives zero odd datum and does not change the energy. This argument uses reflection within each pant, **not** equality or exchangeability of the two adjacent pants.

In the even sector, let `A_-` and `A_+` be the two actual pant self-DtN matrices compressed to `J`, with the other finite boundaries held at zero. PF-340 gives the exact face decomposition `A_- direct-sum A_+`. Under the orthogonal change from individual faces to symmetric/antisymmetric faces it becomes

\[
\begin{pmatrix}A&B\\B&A\end{pmatrix},\qquad
A=\tfrac12(A_-+A_+)>0,\quad B=\tfrac12(A_--A_+).
\tag{6}
\]

The actual seam is diagonal in face parity. Thus the full even matrix on `J` is

\[
\mathcal M=
\begin{pmatrix}H&B\\ B&A+Q_-\end{pmatrix},
\qquad H=A+Q_+,\quad Q_+\ge0.
\tag{7}
\]

The subscripts on `Q_+` and `Q_-` denote seam parity, not adjacent pants. No commutation between `A` and `B` is assumed.

## 2. A stiff complementary block gives a relative bound

For any finite matrices as in (6)--(7), suppose `Q_- >= q I`, with `q>0`, and let `m=||A||`, `b=m/q`. Shorting **all** antisymmetric coordinates gives

\[
F=H-B(A+Q_-)^{-1}B.
\tag{8}
\]

Since `A+B=A_- >=0` and `A-B=A_+ >=0`, the selfadjoint matrix `A^(-1/2) B A^(-1/2)` is a contraction. Hence

\[
BA^{-1}B\le A.
\tag{9}
\]

Also `A<=mI`, so

\[
A+Q_-\ge A+qI\ge(1+q/m)A.
\]

Inverse order and (9) imply

\[
0\le B(A+Q_-)^{-1}B\le\frac{b}{1+b}A,
\]
\[
\boxed{(1+b)^{-1}H\le F\le H.}
\tag{10}
\]

Let `F_T` instead free only antisymmetric coordinates in `T`, holding its two edge coordinates at zero. Variational inclusion gives `F<=F_T<=H`, so (10) also holds for `F_T`. Shorting the symmetric transition coordinates next preserves the same sandwich:

\[
(1+b)^{-1}H^{/T}\le(F_T)^{/T}\le H^{/T}.
\tag{11}
\]

Successive minima equal the simultaneous minimum, hence `H^( /T)=S_n^D` and `(F_T)^( /T)=S_n^loc`. The temporary relaxation of the antisymmetric edge coordinates was only a lower comparison; they remain fixed at zero in (3).

The estimate depends on the **largest** eigenvalue of `A` relative to `q`. It has no inverse-smallest-eigenvalue factor for `A` or its transition compression. This is why it remains useful after very small residual diagonal energies are produced.

## 3. The prescribed seam and narrow-band dimension bound the loss

PF-317's full hyperbolic/flat strip comparison and the flat antisymmetric eigenvalue give, uniformly on `J`,

\[
q_-^{\rm hyp}(\xi,w)
\ge(1+w^2)^{-1}\sqrt{1+\xi^2}\,
\coth\bigl(w\sqrt{1+\xi^2}\bigr)
\ge\frac1{w(1+w^2)}.
\tag{12}
\]

Thus take `q=1/[w(1+w^2)]`. This uses the actual hyperbolic seam, not equality with its flat model.

Write `s_-=s_(n-1)`, `s_+=s_n` and `D=(s_-^(-1)+s_+^(-1))/L`. PF-344's individual bounded-frequency trials, with common fixed bound `K=kappa+2`, give

\[
A_{jj}\le C_K(D+1),\qquad
\|A\|\le\operatorname{Tr}A\le C_KN(D+1).
\tag{13}
\]

Only positivity and the diagonal trial bounds are needed here; (13) controls the entire growing band. Therefore

\[
b_n=w_n(1+w_n^2)\|A\|
\le C_K\left[
\frac NL\,w_n(s_-^{-1}+s_+^{-1})+w_nN\right].
\tag{14}
\]

Both adjacent separations satisfy `s_-,s_+ >= h_n/2` by PF-216. PF-205 gives `w_n/h_n=O(1)` because `w_n asymp P_n^(-1)`, `h_n asymp g_n/P_n`, and `g_n>=2`. Also `w_nL_n -> 0`. With (2), (14) proves

\[
b_n\le C(\eta+L_n^{-1})+Cw_n(\eta L_n+1)
\le C\eta+o(1).
\tag{15}
\]

This comparison requires no neighboring-gap-ratio hypothesis and no new prime-gap theorem. The stronger geometric growth input used to obtain PF-348's correlation remains part of that dependency.

## 4. Normalize only after both relaxations

Put `S=S_n^D`, `U=S_n^loc` and `delta=b_n/(1+b_n)`. Equation (11) gives

\[
0\le S-U\le\delta S.
\tag{16}
\]

Cauchy--Schwarz for the positive difference bounds its mixed entry by `delta sqrt(S_11 S_22)`. Consequently, whenever `rho(S)>delta`,

\[
\rho(U)
\ge\rho(S)-\delta,
\qquad \rho(V):=\frac{|V_{12}|}{\sqrt{V_{11}V_{22}}}.
\tag{17}
\]

Indeed the reverse triangle inequality bounds the numerator from below by `(rho(S)-delta) sqrt(S_11 S_22)`, while `U_jj<=S_jj` bounds the denominator from above. PF-348 gives `rho(S)>=1/2` for every sufficiently small fixed `eta` on its tail. Choose `eta_1` still smaller so that (15) eventually gives `b_n<=1/3`, hence `delta<=1/4`. Equation (17) proves (4).

This controls the change relative to the **shorted** diagonal energies. A raw `o(D)` entry error, or an estimate on the antisymmetric seam alone without (9), would not prove it.

## Prior art, checks, and mathematical delta

Positive block contraction, inverse order, and monotone homogeneous shorting are classical. The proof (8)--(11) is elementary finite-dimensional Schur theory, within the framework of Anderson and Trapp, *Shorted Operators. II* (1975), [DOI](https://doi.org/10.1137/0128007), already S24. Angle comparison under equivalent positive forms is likewise classical (S25); (17) is proved directly. No new matrix inequality is claimed.

The pant reflection, including cusped and equidistantly truncated Y-pieces, is described in Section 2.3 of Buser, Makover, Muetzel and Silhol, *Energy distribution of harmonic 1-forms and Jacobians of Riemann surfaces with a short closed geodesic*, Mathematische Zeitschrift 297 (2021), 1899–1952, [DOI](https://doi.org/10.1007/s00209-020-02584-8). Only that geometric symmetry is used, not their harmonic-form estimates.

The line-specific delta is (14)--(15): the prescribed seam width and the actual pant trace bound convert **small physical transition width** into a dimension-independent relative bound for the entire parity relaxation. Combining it with PF-348 closes a previously excluded local freedom. PF-347 concerns adding the small symmetric seam to a Gram model; it does not control eliminating an antisymmetric block from the actual pant form.

Supplementary exact-rational checks covered twelve noncommuting positive block controls of sizes `N=3,5,7`, using bounds `b=1/100,1/10,1/4,1`. Construct `A=R^t diag(10^(-2j)) R` and `B=R^t diag(10^(-2j)(-1)^j(j+1)/(N+1)) R`, with unit upper-triangular `R` and entries above its diagonal drawn from `{-2,-1,0,1,2}` using Python's `Random(349)`. Set `Q_+=10^(-14)I`, `q=Tr(A)/b`, and `Q_-=q diag(1,...,N)`. Exact Fraction arithmetic verified (10)--(11) for all-coordinate and transition-only antisymmetric relaxation, and equality of simultaneous/sequential shorting; the retained indices were the first and last. These finite controls check algebra, not the pant PDE or its geometric constants. The proof establishes the assertions independently of them.

## Boundaries and consequence

- The other cuffs remain Dirichlet. Freeing their transition data destroys the direct sum of self-responses used in (6); no analogue of (14) for that collective relaxation is established. PF-348's positive finite control already shows that a large local correlation need not survive further relaxation.
- Both parity sectors are now included for the complete local transition band. This does not free all bounded or unbounded exterior modes, change the retained low/high split, or prove an infinite-section limit.
- Reflection, zero twist, the natural seam width, and fixed bounded physical frequencies are load-bearing. A different twist, a wider seam, or an unbounded band requires a new estimate. The theorem is for sufficiently narrow **fixed** positive width, not arbitrary fixed width.
- Nonprime controls obeying the same geometric and spectral bounds satisfy the same argument. No primality-specific invariant, scattering theorem, or RH implication follows.

A falsification would require a failure of the local reflection/parity decomposition, of the actual antisymmetric seam lower bound, of the bounded-frequency pant trial, or of PF-348's independently stated local comparison. Merely showing that global relaxation is stronger does not contradict this local theorem. For the live clue, local parity freedom cannot repair the narrow-band obstruction; the remaining decisive freedom is transmission through neighboring modules, or a representation outside this narrow-band regime.
