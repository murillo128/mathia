# PF-267 — path Green correlations multiply and couple uniform amplitude to decay

**Status:** `LITERATURE+DERIVED + EXACT-PATH-CORRELATION + UNIFORM-NORMALIZED-GREEN-DECAY + MULTIPLICATIVE-AMPLITUDE-DECAY + FINITE-SEAM-ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-266-diagonal-capacity-recovers-uniform-mass-mode-green-amplitude|PF-266]] proves the uniform diagonal scale for the massive parity Green matrices

\[
G_{ij}^{(\varepsilon)}(a)
=\langle e_i,(L_\varepsilon+a^2)^{-1}e_j\rangle,
\qquad
\mu=\sqrt{1+a^2},
\]

namely

\[
G_{ii}^{(\varepsilon)}(a)
\asymp \frac1{\mu(i+1+\mu)}.
\tag{1}
\]

It deliberately stopped short of multiplying this amplitude by the mass-uniform off-diagonal recession from [[research/prime_flute/findings/PF-265-unbounded-gap-combes-thomas-makes-mass-mode-green-decay-uniform|PF-265]]. In a general positive operator that caution is necessary. For the exact PF parity operator, however, the missing correlation is forced by its **one-dimensional tridiagonal path structure**.

There are constants `c,C>0`, independent of parity, mass, and mode indices, such that for every `a>=0` and `0<=i<j`,

\[
\boxed{
\frac{G_{ij}^{(\varepsilon)}(a)}
{\sqrt{G_{ii}^{(\varepsilon)}(a)G_{jj}^{(\varepsilon)}(a)}}
\le
\exp\!\left[-c\sum_{m=i}^{j-1}
\min\!\left(1,\frac{\mu}{m+1}\right)\right].
}
\tag{2}
\]

Consequently PF-266's sharp amplitude and a uniform path-decay factor do occur in the **same bound**:

\[
\boxed{
G_{ij}^{(\varepsilon)}(a)
\le
\frac{C}{\mu\sqrt{(i+1+\mu)(j+1+\mu)}}
\exp\!\left[-c\Psi_{ij}(\mu)\right],
}
\tag{3}
\]

where

\[
\Psi_{ij}(\mu)
:=\sum_{m=i}^{j-1}
\min\!\left(1,\frac{\mu}{m+1}\right).
\tag{4}
\]

This is the normalized Green-correlation theorem left open in PF-266 and in `CLUE-relative-seam-intrinsic-six-fractional-window.md`. The proof is elementary once the correct object is isolated: cut the Jacobi chain at one edge, estimate the two one-sided endpoint capacities using PF-266's weighted form equivalence, convert the resulting Schur-complement gap into an adjacent correlation loss, and then multiply those losses exactly along the path.

The result still does **not** assert that the complete odd-mass series in PF-261 has the required endpoint-weighted `R>1` operator bound. That sum is now the direct next discriminator.

## Claim

Fix one parity `\varepsilon\in\{0,1\}` and write

\[
T_{a,\varepsilon}=L_\varepsilon+a^2,
\qquad
\mu=\sqrt{1+a^2},
\qquad
G=T_{a,\varepsilon}^{-1}.
\tag{5}
\]

As in PF-266, write the off-diagonal Jacobi coefficient between sites `m` and `m+1` as `-c_m^{(\varepsilon)}` with

\[
c_m^{(\varepsilon)}>0,
\qquad
c_m^{(\varepsilon)}\asymp(m+1)^2
\tag{6}
\]

uniformly over the two parities. Then:

1. for the Dirichlet restrictions obtained by cutting the edge `(m,m+1)`, their endpoint Green diagonals `g_m^-` and `g_{m+1}^+` satisfy
   \[
   \boxed{
   g_m^-\asymp g_{m+1}^+\asymp
   \frac1{(m+1)^2+\mu^2};
   }
   \tag{7}
   \]
2. if
   \[
   \rho_m
   :=\frac{G_{m,m+1}}{\sqrt{G_{mm}G_{m+1,m+1}}},
   \tag{8}
   \]
   then `0<rho_m<1` and
   \[
   \boxed{
   1-\rho_m^2
   \gtrsim
   \min\!\left(1,\frac{\mu}{m+1}\right);
   }
   \tag{9}
   \]
3. the normalized Green matrix is exactly multiplicative along the path:
   \[
   \boxed{
   \frac{G_{ij}}{\sqrt{G_{ii}G_{jj}}}
   =\prod_{m=i}^{j-1}\rho_m,
   \qquad i<j;
   }
   \tag{10}
   \]
4. equations (9)--(10) imply (2), and combining (2) with PF-266 equation (1) gives (3);
5. the same one-edge estimates also give
   \[
   \rho_m
   \lesssim
   \frac{(m+1)^2}{(m+1)^2+\mu^2},
   \tag{11}
   \]
   hence there are fixed `B,C>0` such that whenever `\mu>=B(j+1)`,
   \[
   \boxed{
   \frac{G_{ij}}{\sqrt{G_{ii}G_{jj}}}
   \le
   \left(\frac{C(j+1)^2}{\mu^2}\right)^{j-i}.
   }
   \tag{12}
   \]

All constants are independent of `a,i,j` and of the parity block. Equation (12) is only an auxiliary large-mass refinement; the load-bearing statement is the uniform product estimate (3).

## 1. Cutting one edge exposes the exact adjacent correlation

Fix `m>=0`. Split the parity chain into

\[
\mathcal H_-={\rm span}\{e_0,\dots,e_m\},
\qquad
\mathcal H_+=\overline{{\rm span}\{e_{m+1},e_{m+2},\dots\}}.
\]

Let `T_-` and `T_+` be the corresponding Dirichlet restrictions of `T_{a,\varepsilon}` and put

\[
g_m^-:=\langle e_m,T_-^{-1}e_m\rangle,
\qquad
g_{m+1}^+:=\langle e_{m+1},T_+^{-1}e_{m+1}\rangle.
\tag{13}
\]

PF-265 gives `L_\varepsilon>=I`, so `T_{a,\varepsilon}>=\mu^2I`; the same bound holds on both restrictions. Relative to this split the only coupling is the rank-two symmetric edge with entries `-c_m`. Standard block inversion therefore gives, with

\[
\eta_m:=c_m^2 g_m^-g_{m+1}^+,
\tag{14}
\]

\[
G_{mm}=\frac{g_m^-}{1-\eta_m},
\qquad
G_{m+1,m+1}=\frac{g_{m+1}^+}{1-\eta_m},
\tag{15}
\]

and

\[
G_{m,m+1}
=\frac{c_m g_m^-g_{m+1}^+}{1-\eta_m}.
\tag{16}
\]

Positivity of `T_{a,\varepsilon}` forces `0<=\eta_m<1`. Since the Jacobi chain is irreducible and its off-diagonal entries are negative, the below-spectrum Green matrix is strictly positive, so in fact `0<\eta_m<1`. Dividing (16) by the geometric mean of (15) yields the exact identity

\[
\boxed{
\rho_m=c_m\sqrt{g_m^-g_{m+1}^+},
\qquad
1-\rho_m^2
=\frac{g_m^-}{G_{mm}}
=\frac{g_{m+1}^+}{G_{m+1,m+1}}.
}
\tag{17}
\]

Thus the adjacent normalized correlation is controlled by the ratio between a **cut capacity** and the full diagonal Green scale. This is the structure that was invisible to the independent minimum of PF-265 and PF-266.

## 2. PF-266 already contains the one-sided cut-capacity scale

PF-266 proves the parity-uniform form lower bound

\[
\langle u,T_{a,\varepsilon}u\rangle
\ge C_0\left[
\sum_{n\ge0}(n+1)^2|u_{n+1}-u_n|^2
+\mu^2\sum_{n\ge0}|u_n|^2
\right].
\tag{18}
\]

For `u` supported on the left side of the cut, zero extension has `u_{m+1}=0`; the edge `m` term in (18) gives

\[
\langle u,T_-u\rangle
\gtrsim((m+1)^2+\mu^2)|u_m|^2.
\tag{19}
\]

The variational formula for the inverse diagonal therefore gives

\[
g_m^-\lesssim\frac1{(m+1)^2+\mu^2}.
\tag{20}
\]

The same zero-extension argument on the right uses the same cut edge and gives the corresponding upper bound for `g_{m+1}^+`.

For the reverse inequality it is enough to use the endpoint basis vector. PF-262/PF-266 give `q_n\lesssim(n+1)^2` uniformly over the finite prefix and asymptotic tail, hence

\[
\langle e_m,T_-e_m\rangle=q_m+a^2
\lesssim(m+1)^2+\mu^2.
\tag{21}
\]

The reciprocal variational principle gives the matching lower bound. At the right endpoint, `q_{m+1}\lesssim(m+2)^2`, which is comparable to `(m+1)^2`; this proves (7).

No new asymptotic recurrence theorem is required. The one-sided capacity is one derivative stronger than the full diagonal scale because cutting the path forces a Dirichlet jump across the severed edge.

## 3. The cut/full capacity ratio gives a uniform correlation gap

Use the first identity in (17), the lower half of (7), and PF-266's full diagonal upper bound

\[
G_{mm}\lesssim\frac1{\mu(m+1+\mu)}.
\tag{22}
\]

Then

\[
1-\rho_m^2
=\frac{g_m^-}{G_{mm}}
\gtrsim
\frac{\mu(m+1+\mu)}{(m+1)^2+\mu^2}.
\tag{23}
\]

Writing `x=m+1`, the scalar factor on the right is

\[
\frac{\mu(x+\mu)}{x^2+\mu^2}
\gtrsim \min\left(1,\frac\mu x\right).
\tag{24}
\]

This proves (9). Since `0<rho_m<1`,

\[
\rho_m
=\sqrt{1-(1-\rho_m^2)}
\le
\exp\!\left[-\frac12(1-\rho_m^2)\right],
\tag{25}
\]

and therefore

\[
\boxed{
\rho_m
\le
\exp\!\left[-c\min\!\left(1,\frac\mu{m+1}\right)\right].
}
\tag{26}
\]

There is also a useful upper estimate directly from (17), (6), and the upper half of (7):

\[
\rho_m
\lesssim
\frac{(m+1)^2}{(m+1)^2+\mu^2},
\tag{27}
\]

which proves (11).

## 4. One-dimensional Green matrices multiply normalized correlations exactly

The inverse of an irreducible tridiagonal matrix is a classical Green matrix: on one side of the diagonal its entries factor as one left sequence times one right sequence. In the present infinite Jacobi setting this is also the exact Weyl/regular-solution formula already used in PF-264:

\[
G_{ij}=\frac{r_i u_j}{W(r,u)},
\qquad i\le j,
\tag{28}
\]

where `r` is the left regular solution and `u` the right Weyl solution. Because the Green kernel is positive at `-a^2`, the relevant factors may be chosen with consistent positive signs.

Equation (28) immediately gives

\[
\rho_m
=\frac{G_{m,m+1}}{\sqrt{G_{mm}G_{m+1,m+1}}}
=\sqrt{\frac{r_m u_{m+1}}{u_m r_{m+1}}}.
\tag{29}
\]

Multiplication from `m=i` to `j-1` telescopes:

\[
\prod_{m=i}^{j-1}\rho_m
=\sqrt{\frac{r_i u_j}{u_i r_j}}
=\frac{G_{ij}}{\sqrt{G_{ii}G_{jj}}}.
\tag{30}
\]

This proves (10). Combining (30) with (26) gives (2), and PF-266 equation (1) then gives (3). Importantly, (3) is **not** obtained by multiplying two unrelated upper bounds: the factorization (30) supplies an exact correlation identity, while the diagonal amplitudes enter only after the correlation has been bounded.

PF-265's metric

\[
\Phi_{ij}(\mu)
=\sum_{m=i}^{j-1}\min\!\left(1,\frac{c_p\mu}{m+1}\right)
\]

is comparable, up to fixed constants, to `Psi_ij(mu)`. Thus (3) supplies precisely the type of amplitude-times-recession theorem requested after PF-266, now from path capacity rather than a stronger global Combes--Thomas conjugation.

Finally, if `\mu>=B(j+1)`, (27) gives uniformly for every `i<=m<j`

\[
\rho_m\le\frac{C(j+1)^2}{\mu^2}.
\]

Choosing fixed `B` large enough makes this factor strictly below one, and (10) proves (12). This gives an additional rapidly summable regime for the very massive tail of PF-261's odd ladder.

## 5. Consequence for the finite-seam discriminator

PF-261 gives, for separated same-parity physical modes, the exact off-diagonal identity

\[
\langle e_i,\mathcal R_{s,r}^0e_j\rangle
=-\frac{2}{rs^2\sqrt{\kappa_i\kappa_j}}
\sum_{k\ge0}a_k^2
\langle e_i,(L+a_k^2)^{-1}e_j\rangle,
\qquad
a_k=\frac{(2k+1)\pi}{2rs}.
\tag{31}
\]

PF-266 left two legitimate possibilities: the minimum of its amplitude estimate and PF-265's decay estimate might already sum with strict `R>1`, or a stronger normalized-correlation theorem might be needed. Equation (3) settles the second branch positively: the sharp diagonal scale and a fixed positive path-decay fraction coexist multiplicatively for every mass and every pair of modes.

The next step is therefore no longer another Green-function correlation theorem. It is to insert (3), together with the stronger massive-tail factor (12) where useful, into the **actual odd-mass sum (31)**, perform the mass sum before taking the separated weighted mode norm, and determine the resulting exponent. Only that summed statement can show whether the fixed-axis finite seam retains the strict `R>1` margin required by PF-243.

## 6. Prior art and novelty audit

The Green-matrix factorization itself is classical and is not claimed as new. Reinhard Nabben, *On Green's Matrices of Trees*, SIAM Journal on Matrix Analysis and Applications **22**(4) (2001), 1014--1026, DOI `10.1137/S0895479899365732`, states explicitly that the inverse of an irreducible nonsingular symmetric tridiagonal matrix is a Green matrix `G_ij=u_i v_j` for `i<=j`. Gérard Meurant, *A Review on the Inverse of Symmetric Tridiagonal and Block Tridiagonal Matrices*, SIAM Journal on Matrix Analysis and Applications **13**(3) (1992), 707--728, DOI `10.1137/0613045`, reviews the corresponding inverse formulas and decay bounds.

A modern probabilistic formulation appears in J. Baz, P. Alonso, J. M. Peña, and R. Pérez-Fernández, *Gaussian Markov Random Fields over graphs of paths and high relative accuracy*, Journal of Computational and Applied Mathematics **453** (2025), 116142, DOI `10.1016/j.cam.2024.116142`: for a Gaussian Markov field whose precision graph is a path, the normalized correlations are products of the adjacent correlations. That is the finite-dimensional statistical form of (30).

The project-specific content is therefore **not** path multiplicativity. It is the quantitative specialization obtained by combining that exact path law with PF-266's Prime-Flute weighted capacity scale: the severed-edge Green diagonal is uniformly `((m+1)^2+mu^2)^-1`, while the uncut Green diagonal is uniformly `[mu(m+1+mu)]^-1`. Their Schur-complement ratio forces the adjacent loss (9), and hence the all-mass amplitude-times-decay estimate (3). A targeted literature search found the classical Green-matrix/path-correlation structure but did not identify this PF-specific weighted-capacity specialization. The result should be read as an exact derived specialization, not as a new general theorem on tridiagonal inverses or Gaussian Markov fields.

## 7. Boundaries and adversarial checks

1. **The path structure is essential.** Equation (10) fails as an exact multiplicative law on a graph with loops or long-range mode couplings. It applies here because PF-247 proves exact parity tridiagonality.
2. **No unjustified product of upper bounds is used.** PF-265 and PF-266 could not simply be multiplied. The new product comes from the exact Green-matrix identity (30), with a separately proved adjacent-correlation gap.
3. **Dirichlet restrictions remain uniformly invertible.** They inherit `T_{a,\varepsilon}>=mu^2 I` by zero extension, so the Schur complements and endpoint Green functions are well defined for every mass.
4. **The finite prefix is harmless but not discarded.** Uniform comparability in (6)--(7) absorbs it; no asymptotic statement is used as a pointwise identity at small mode index.
5. **No sign cancellation is needed.** The parity Jacobi off-diagonals have one sign and the resolvent is evaluated strictly below the spectrum, so the Green entries are positive. The PF-261 physical off-diagonal sign is carried separately by its exact identity (31).
6. **Parity-chain and physical mode indices must not be confused.** Equations (1)--(30) use the parity-chain coordinate of PF-262--PF-266. Returning to the full Gegenbauer basis changes indices only by the fixed map `n=2i+varepsilon` and fixed comparability constants.
7. **No odd-ladder conclusion is hidden here.** The prefactor `2/(rs^2)`, the spacing of `a_k`, endpoint `A^-1/4` weights, and the coupled low/intermediate/high mass regimes must still be summed before claiming an `R>1` operator estimate.
8. **No Robin/global conclusion.** Even a positive summed fixed-axis theorem must still pass through PF-257's bounded Robin transform, PF-256's actual-corridor transport, PF-243's localized Poisson factorization and the global weak-trace reassembly. Nothing here establishes a scattering/determinant identity, a statement about zeta zeros, or RH.

The finding would fail if the PF parity operator were not exactly a one-dimensional irreducible Jacobi chain, if PF-266's uniform form/diagonal estimates were wrong, or if the edge-cut Schur complement did not reproduce the full adjacent Green correlation. Under the persisted PF-247/PF-266 hypotheses, the block inversion and Green-factorization identities make those dependencies explicit and independently checkable.

## Decisive next test

Insert (3) into PF-261 equation (31) with the **actual** odd masses and split the sum according to `mu_k` relative to the two mode indices. Use (12) for the genuinely large-mass tail rather than wasting its stronger path contraction. Perform the complete `k`-sum first, including the `a_k^2` coefficient and `s^-2` prefactor, and only then test the separated matrix against the weighted `R>1` norm required by PF-243.

If the summed product estimate leaves any strict `R>1` margin, the fixed-axis finite-seam Green gate is closed and research should move to propagation through the bounded Robin map and the actual corridor. If the sum remains critical, identify the exact mass/mode scaling responsible before asking for a still stronger pointwise Green theorem; the failure may lie in the odd-ladder summation or endpoint bookkeeping rather than in Green correlation itself.