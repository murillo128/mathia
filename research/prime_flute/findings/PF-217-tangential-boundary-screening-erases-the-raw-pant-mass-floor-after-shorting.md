# PF-217 — tangential boundary screening erases the raw pant mass floor after shorting

**Status:** `EXACT-DERIVED + ASYMPTOTIC-DERIVED + NEGATIVE/ROUTE-NARROWING`. PF-216 identifies a growing positive-shift mass/conductance floor when the simultaneous PF-205 exterior precision is compressed to the raw low-symmetric constant module vectors. It explicitly leaves open whether that floor survives the correct variational elimination of the complementary boundary modes. It does **not** survive with any uniform positive fraction. On long tail blocks one can replace the constant boundary value by a tangential bump supported near the finite-finite common-perpendicular foot. The zero-twist marking lets the same bump be used on both sides of each thin seam strip, so its strip energy costs only `O(w_n R)`; inside the neighboring tight pant the bump avoids the growing-corridor ends that created PF-216's `O(1)` same-sign mass. A slowly varying discrete envelope makes the remaining narrow-gap conductance cost only `O(log N)` over `N` modules. Consequently, for the shorted low form

\[
\mathfrak s_{\rm low}[x]
=\inf_{y\in Q\operatorname{Dom}(\mathfrak a)}\mathfrak a[x+y],
\qquad
\mathfrak a[f]=\|f\|^2+\mathfrak k[f],
\]

there are finite-support low vectors with

\[
\boxed{
\frac{\mathfrak s_{\rm low}[x]}
{\sum_n |x_n|^2/q_n}\longrightarrow0.
}
\]

Thus the decisive fixed-fraction coercivity test proposed after PF-216 is false. This does **not** show that the effective Schur factor lacks PF-213-compatible locality: the screened form may still retain a useful variable-conductance or weighted structure. It shows that any such proof must analyze the actually shorted boundary form rather than inherit PF-216's raw onsite floor. PF-204's unsmoothed native factorization and the independent PF-183 true-short-collar splice are unaffected.

## Claim

Use the simultaneous natural-width seam cut of PF-205 on the prime flute. With PF-214 notation, let

\[
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0,
\qquad
\mathfrak a[f]=\|f\|^2+\mathfrak k[f]
\tag{1}
\]

be the closed form of `I+K` on the normalized boundary-energy space

\[
\mathcal B=\bigoplus_n\mathcal B_n.
\]

For each seam module let

\[
\mathbf1_n=(1,1),
\qquad
q_n=\langle\mathbf1_n,\Lambda_{Q,n}\mathbf1_n\rangle,
\qquad
u_n=\frac{\Lambda_{Q,n}^{1/2}\mathbf1_n}{\sqrt{q_n}},
\tag{2}
\]

as in PF-216. Let `P` be the orthogonal projection onto the closed span of the `\nu_n`, and put `Q=I-P`. For finitely supported

\[
x=\sum_n x_n\nu_n,
\]

define the raw PF-216 mass currency

\[
\mathfrak m_0[x]
:=\sum_n\frac{|x_n|^2}{q_n}
\tag{3}
\]

and the effective shorted form

\[
\mathfrak s_{\rm low}[x]
:=\inf_{y\in Q\operatorname{Dom}(\mathfrak a)}
\mathfrak a[x+y].
\tag{4}
\]

Then

\[
\boxed{
\inf_{0\ne x\in P\mathcal B,\;x\text{ finitely supported}}
\frac{\mathfrak s_{\rm low}[x]}{\mathfrak m_0[x]}=0.
}
\tag{5}
\]

More concretely, there are tail vectors `x^{(N)}` supported in modules `N\le n\le2N` and some `\delta>0` such that

\[
\boxed{
\mathfrak m_0[x^{(N)}]\ge cN,
\qquad
\mathfrak s_{\rm low}[x^{(N)}]
\le C\bigl(1+\log N+NP_N^{-\delta}\bigr),
}
\tag{6}
\]

where `P_n=p_{n-1}` is the prime label used in PF-205--PF-216. Hence the ratio in (5) tends to zero.

The conclusion is deliberately narrower than failure of Schur locality. It rules out a tail estimate of the form

\[
\mathfrak s_{\rm low}[x]\ge c\mathfrak m_0[x]
\tag{7}
\]

with fixed `c>0`. It does not rule out a weaker effective form whose inverse still satisfies PF-213's transport budget.

## 1. The normalized form is exactly total cut energy

The useful simplification is to work before taking the low/high Schur complement. If `\varphi` is physical Dirichlet data on the simultaneous cut and

\[
f=\Lambda_Q^{1/2}\varphi,
\tag{8}
\]

then by definition of `K`,

\[
\boxed{
\mathfrak a[f]
=\langle\varphi,\Lambda_Q\varphi\rangle
+\langle\varphi,\Lambda_E\varphi\rangle.
}
\tag{9}
\]

Thus any explicit boundary profile plus any admissible strip/pant extensions give an upper bound for the shorted form after projecting `f` onto `P`.

The PF-205 strip metric is translation invariant in the cuff coordinate `s`, and PF-212 uses exactly this Fourier separation. Therefore the symmetric constant datum `\mathbf1_n` is a tangential zero-mode eigenvector of the two-sided strip DtN form. If the same boundary function `\phi_n(s)` is prescribed on both sides of module `Q_n`, then the coefficient of `P\Lambda_{Q,n}^{1/2}\phi_n` is determined only by its tangential mean:

\[
P\Lambda_{Q,n}^{1/2}\phi_n
=t_n\sqrt{q_n}\,\nu_n,
\qquad
 t_n=\frac1{L_n}\int_0^{L_n}\phi_n(s)\,ds.
\tag{10}
\]

In particular

\[
\frac{|x_n|^2}{q_n}=|t_n|^2.
\tag{11}
\]

This is the key reason a nonconstant boundary profile can screen the exterior energy without losing its low-symmetric projection.

## 2. A central tangential bump keeps a macroscopic low projection

PF-215/PF-216 give, after a finite head,

\[
w_n\asymp P_n^{-1},
\qquad
s_n\asymp h_n+h_{n+1},
\qquad
s_n\le CP_n^{-0.475},
\tag{12}
\]

and the elementary gap lower bound together with `h_n=(g_n/P_n)(1+o(1))` gives

\[
s_n\ge cP_n^{-1}.
\tag{13}
\]

Also

\[
L_n=2a_n,
\qquad
a_n=-\log\tanh(h_n/4),
\tag{14}
\]

so (12)--(13) imply the two-sided logarithmic comparison

\[
\boxed{c\log P_n\le L_n\le C\log P_n.}
\tag{15}
\]

Fix a small absolute `\varepsilon>0`, for example `\varepsilon=1/20`, and on the index block `N\le n\le2N` put

\[
R_N=\varepsilon\log P_N.
\tag{16}
\]

Let `\chi\in C_c^\infty((-1,1))` be nonnegative, equal to one on `[-1/2,1/2]`, and set

\[
\chi_N(s)=\chi(s/R_N).
\tag{17}
\]

The BHP upper gap bound in (12) implies

\[
T_{s_n}\sim\log(1/s_n)\ge(0.475-o(1))\log P_n,
\tag{18}
\]

where `T_{s_n}` is PF-216's growing embedded Fermi corridor. Hence the support `|s|\le R_N` lies strictly inside that corridor for every module in the block once `N` is large. It also lies well inside one cuff period by (15).

Choose the discrete sine envelope

\[
z_n=
\begin{cases}
\sin\!\bigl(\pi(n-N)/N\bigr),&N\le n\le2N,\\
0,&\text{otherwise}.
\end{cases}
\tag{19}
\]

Then

\[
\sum_n z_n^2\asymp N,
\qquad
\sum_n|z_{n+1}-z_n|^2=O(N^{-1}).
\tag{20}
\]

Use the zero-twist seam marking to center the same function

\[
\phi_n(s)=z_n\chi_N(s)
\tag{21}
\]

at the finite-finite common-perpendicular foot on **both** artificial boundary circles of module `Q_n`. Zero twist is load-bearing here: it identifies those seam origins across the cuff, so (21) has a constant-in-the-normal-direction strip extension rather than an `O(w_n^{-1})` phase-welding cost.

Let

\[
I_\chi=\int_{-1}^1\chi(t)\,dt>0.
\]

Equation (10) gives

\[
t_n=z_n\frac{I_\chi R_N}{L_n}.
\tag{22}
\]

Classical explicit `n`th-prime bounds give `P_n\asymp n\log n` up to fixed constants on `N\le n\le2N`; together with (15), `\log P_n\asymp\log P_N` uniformly on that block. Therefore

\[
\boxed{|t_n|\asymp |z_n|}
\tag{23}
\]

with constants depending only on the fixed `\varepsilon,\chi`. If

\[
f^{(N)}=\Lambda_Q^{1/2}\varphi^{(N)},
\qquad
x^{(N)}=Pf^{(N)},
\tag{24}
\]

then (11), (20), and (23) prove

\[
\boxed{
\mathfrak m_0[x^{(N)}]
=\sum_n t_n^2
\ge cN.
}
\tag{25}
\]

## 3. The thin strip pays only the support length

On the signed Fermi strip

\[
g=\frac{dx^2}{1+x^2}+(1+x^2)ds^2,
\qquad d\mu=dx\,ds,
\]

extend (21) constantly in `x`. The positive shifted energy gives

\[
\langle\varphi_n,\Lambda_{Q,n}\varphi_n\rangle
\le
Cw_nz_n^2\left(R_N+R_N^{-1}\right).
\tag{26}
\]

The essential point is that the cost is proportional to the **occupied tangential length** `R_N`, not the full `L_n` and not `L_n/w_n` cells. Since `w_n\asymp P_n^{-1}` and `P_n\gtrsim n\log n`, summing (26) on `N\le n\le2N` gives

\[
\boxed{
\sum_n
\langle\varphi_n,\Lambda_{Q,n}\varphi_n\rangle
=O(1).
}
\tag{27}
\]

The omitted `R_N^{-1}` contribution is smaller.

This is the cheap complementary-mode currency that PF-216's constant compression does not see. Replacing a constant by a long but localized tangential bump changes the normalized low projection only by a fixed factor, while the seam energy still vanishes modulewise.

## 4. The bump avoids the pant ends that create the PF-216 mass floor

Consider the one-cusp pant core `E_n` between modules `n` and `n+1`. PF-216 proves on its growing central corridor that the remaining normal-ray length satisfies

\[
c s_n\cosh t
\le \ell_n(t)
\le C s_n\cosh t
\tag{28}
\]

for `|t|\le T_{s_n}`. On the smaller support `|t|\le R_N`, use a trial function which interpolates linearly along each normal ray between the two boundary bump values. The exact hyperbolic normal correspondence between the two finite cuffs is `C^1`-close to the identity on this central window: from PF-215's explicit ultraparallel-geodesic formula its displacement is

\[
O\!\left(s_n^2e^{2R_N}\right).
\tag{29}
\]

For the chosen `\varepsilon`, this tends to zero polynomially, so the mismatch it creates is absorbed below.

Uniform boundedness of the Fermi metric on the corridor and the elementary linear-interpolation estimate yield

\[
\boxed{
\mathcal E_{E_n}^{\rm trial}
\le
C\left[
\frac{|z_{n+1}-z_n|^2}{s_n}
+s_ne^{R_N}(z_n^2+z_{n+1}^2)
\right]
+\operatorname{err}_n,
}
\tag{30}
\]

where

\[
\sum_{N\le n\le2N}|\operatorname{err}_n|
\le CNP_N^{-\delta}
\tag{31}
\]

for some fixed `\delta>0` after reducing `\varepsilon` if necessary.

The two terms in (30) have transparent origins. The transverse derivative costs

\[
|z_{n+1}-z_n|^2
\int_{-R_N}^{R_N}\frac{dt}{s_n\cosh t}
\le \frac{C|z_{n+1}-z_n|^2}{s_n},
\tag{32}
\]

while the positive-shift mass and tangential derivatives cost at most

\[
C(z_n^2+z_{n+1}^2)
\int_{-R_N}^{R_N}s_n\cosh t\,dt
\le Cs_ne^{R_N}(z_n^2+z_{n+1}^2).
\tag{33}
\]

Equation (33) is exactly where the PF-216 raw floor disappears. For constant data on the whole growing corridor, the integral reaches order one because the corridor extends to `T_s\sim\log(1/s)`. The screening profile stops at `R_N\ll T_s`, so

\[
s_ne^{R_N}
\le CP_N^{-(0.475-\varepsilon)}\longrightarrow0.
\tag{34}
\]

The form-level DtN energy is the minimum over interior extensions, so (30) is an upper bound for the actual `\Lambda_E` contribution.

## 5. A slow block envelope makes the remaining conductance sublinear

From (13),

\[
s_n^{-1}\le CP_n.
\tag{35}
\]

The classical Rosser--Schoenfeld bound `p_n=O(n\log n)` therefore gives on `N\le n\le2N`

\[
\max s_n^{-1}\le CN\log N.
\tag{36}
\]

Combining (20) and (36),

\[
\boxed{
\sum_{N\le n\le2N}
\frac{|z_{n+1}-z_n|^2}{s_n}
=O(\log N).
}
\tag{37}
\]

Meanwhile (34) gives

\[
\boxed{
\sum_{N\le n\le2N}
s_ne^{R_N}(z_n^2+z_{n+1}^2)
\le CNP_N^{-\delta}
}
\tag{38}
\]

for some `\delta>0`.

Equations (27), (30)--(31), and (37)--(38), inserted into the exact total-energy identity (9), show

\[
\mathfrak a[f^{(N)}]
\le C\bigl(1+\log N+NP_N^{-\delta}\bigr).
\tag{39}
\]

Write

\[
f^{(N)}=x^{(N)}+y^{(N)},
\qquad x^{(N)}=Pf^{(N)},\quad y^{(N)}=Qf^{(N)}.
\tag{40}
\]

Then `y^{(N)}` is an admissible competitor in (4), so

\[
\mathfrak s_{\rm low}[x^{(N)}]
\le\mathfrak a[f^{(N)}].
\tag{41}
\]

Together with (25),

\[
\frac{\mathfrak s_{\rm low}[x^{(N)}]}
{\mathfrak m_0[x^{(N)}]}
\le
C\left(
\frac{1+\log N}{N}+P_N^{-\delta}
\right)
\longrightarrow0,
\tag{42}
\]

which proves (5)--(6).

## 6. What the negative result does and does not say

PF-216's raw compression remains correct. Its growing onsite coefficient is a genuine property of constant boundary data before the complementary boundary directions are optimized. PF-217 shows that the raw compression is **not a reducing low model** and that the missing variational step is not benign: nonconstant tangential profiles can move the same low projection away from the corridor ends responsible for the positive-shift mass floor.

The smooth-interface route is therefore narrowed again. A proof of PF-213-compatible locality can no longer proceed by showing that a fixed fraction of

\[
\sum_nq_n^{-1}|x_n|^2
\]

survives shorting. The next meaningful target is the actual effective form after screening. In particular, one should determine whether its dominant scale is a variable-conductance path form, a weaker screened onsite term, or another weighted nonlocal form, and then estimate the Green kernel in the **physical `d_n` module-weight currency** required by PF-213.

Nothing here proves that `D=(I+K)^{-1}` is nonlocal, that the smooth PF-205 architecture fails, or that the full first relative resolvent misses `\mathcal S_{1,\infty}`. PF-204's unsmoothed native two-Hilbert factorization remains a separate route, and PF-183's true-short-collar splice remains an independent global gate.

## 7. Prior-art and novelty audit

The abstract operation in (4) is classical. W. N. Anderson Jr., *Shorted Operators*, SIAM Journal on Applied Mathematics **20** (1971), 520--525, DOI `10.1137/0120053`, identifies finite-dimensional shorting with a Schur-complement/network reduction. W. N. Anderson Jr. and G. E. Trapp, *Shorted Operators. II*, SIAM Journal on Applied Mathematics **28** (1975), 60--71, DOI `10.1137/0128007`, develops the positive-operator short in Hilbert space. PF-216 already records nearby DtN/network degeneration literature, including Borcea--Gorb--Wang and Wentworth. Rosser--Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois Journal of Mathematics **6** (1962), 64--94, DOI `10.1215/ijm/1255631807`, supplies a convenient classical `p_n=O(n\log n)` bound for (36).

No novelty is claimed for shorted operators, Schur complements, DtN minimization, narrow-corridor trial functions, or explicit bounds for the `n`th prime. A structure-directed literature search found the expected general shorting/network/DtN framework but no result used as a substitute for the construction above. Search absence is not novelty evidence. The project-specific deduction is only this: **on the canonical zero-twist PF-205 thin seam geometry, the particular growing PF-216 raw low-symmetric mass floor can be screened to an asymptotically vanishing fraction by admissible tangential boundary data.**

## 8. Falsification and boundary checks

A later adversary should attack the result at the following points.

1. Verify that zero Fenchel--Nielsen twist really identifies the finite-finite seam origins used in (21). A fixed nonzero phase mismatch across the shrinking strip would invalidate the cheap constant-normal extension (26).
2. Reproduce the Fourier-zero projection identity (10) from the exact two-sided PF-205 strip DtN form; the denominator in (25) depends on this being the true `P` projection, not a heuristic boundary average.
3. Check the two-sided bounds (12)--(15), including the elementary prime-gap lower bound and BHP upper envelope, and verify `R_N<T_{s_n}` uniformly on `N\le n\le2N`.
4. Derive the normal-coordinate mismatch estimate (29) from PF-215's exact ultraparallel-geodesic formula and confirm that its energy contribution satisfies (31).
5. Build the trial extension leading to (30) on the **seam-removed** pant core, not on an idealized flat rectangle, and check that metric coefficients remain uniformly controlled on the chosen central corridor.
6. Verify the strip estimate (26) using the signed Fermi metric and ensure no hidden `w_n^{-1}` cost appears; this relies on the same profile being prescribed on both strip sides.
7. Check the Rosser--Schoenfeld `p_n=O(n\log n)` input and the discrete sine estimates (20), yielding the `O(\log N)` conductance budget in (37).
8. Keep the conclusion at failure of the **fixed-fraction raw PF-216 floor**. Do not infer failure of all weaker effective coercivity, failure of PF-213 inverse transport, or noncompactness of the Schur factor.
9. Keep PF-204's unsmoothed route, PF-183's true-short-collar splice, prime/clone separation, scattering, determinants, resonances, and RH outside this finding.

## Consequences for the research line

The PF-215--PF-217 sequence now gives a sharper picture of the smooth seam Schur problem. PF-215 shows that normalized nearest-neighbor hopping is large; PF-216 shows that on raw constants the same geometry supplies an equally important positive-shift mass/conductance floor; PF-217 shows that **the raw floor is not stable under the variational elimination that the actual Schur problem requires**.

Further work on this branch should therefore stop trying to prove a uniform inequality `\mathfrak s_{\rm low}\gtrsim\mathfrak m_0`. The useful next calculation is to identify the leading screened effective form itself and ask whether its inverse still obeys a weighted transport estimate strong enough for PF-213. A negative answer there would be a genuine smooth-route obstruction; the present finding only removes the most direct coercivity completion of PF-216.