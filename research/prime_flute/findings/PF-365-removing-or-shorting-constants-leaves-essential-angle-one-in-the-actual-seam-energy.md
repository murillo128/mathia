# PF-365 — removing or shorting constants leaves essential angle one in the actual seam energy

**Status:** EXACT-DERIVED + CLASSICAL-CAUCHY-RESIDUAL-METHOD + ACTUAL-MEAN-ZERO-ANGLE-OBSTRUCTION.

For the sufficiently narrow fixed transition bands of PF-364, the actual prime-flute seam-energy angle still has **essential norm one** when constants are fixed to zero, or when all module constants are eliminated together with the transitions. First nonzero cosine modes replace PF-364's retained constants. Both assertions concern the completion of finitely supported traces in the actual positive-shift energy, with every transition face parity and tangential sine/cosine mode allowed.

The additional constant elimination costs a factor of order `L_i^(-4)` in the lower residual certificate. That polynomial loss is absorbed by PF-364's strict exponential margins. The two actual angles are not asserted to be unitarily equivalent: PF-360's exact model isometry is unnecessary and is not imported into the pant/seam form.

This closes the constant-removal escape for the stated narrow-band representation. It supplies no relative-resolvent, scattering, zeta-zero or RH conclusion.

## 1. Two operations and their common actual-energy setting

Use the natural seam cut and positive shift `Delta+1` of PF-364. Initially, traces have finite module support and finite Fourier support. Their energy is

\[
 M=Q+\Lambda_E,\qquad d_i=s_{i-1}^{-1}+s_i^{-1},\qquad b_0=19/80.
 \tag{1}
\]

All coordinates are the inherited centered zero-twist cuff coordinates of period `L_i`. Fix `kappa>0` and eliminate every sine/cosine transition with `kappa<|xi|<kappa+eta`, on both faces. Denote this algebraic space by `T_alg`. The retained nonconstant low and high spaces contain every mode with, respectively,

\[
 0<|\xi|\le\kappa,\qquad |\xi|\ge\kappa+\eta.
 \tag{2}
\]

Let `C_alg` be all finitely supported module constants on both faces. Distinguish:

- **Absent constants (`e=0`).** Complete the nonconstant algebraic traces in `M`; eliminate the closure of `T_alg` in this completion.
- **Shorted constants (`e=1`).** Complete all algebraic traces in `M`; eliminate the closure of `T_alg+C_alg`.

Write `E_e` for the respective closed eliminated space, `R_e=I-P_(E_e)`, and

\[
 \mathcal L_e=\overline{R_eL_{\rm alg}},\qquad
 \mathcal H_e=\overline{R_eH_{\rm alg}},\qquad
 Z_e=P_{\mathcal H_e}|_{\mathcal L_e}.
 \tag{3}
\]

These definitions do not require a bounded infinite Fourier matrix or an inverse on coefficient `ell^2`. In finite positive sections they are exactly the angles normalized by the diagonal blocks of the same shorted form. The absence condition is imposed before completion; no claim about every possible finite-energy trace space at infinity is made.

There is a `W_0>0` such that for each fixed `0<W<W_0`, all sufficiently small fixed `0<eta<W` satisfy

\[
 \boxed{\|Z_0\|_{\rm ess}=\|Z_1\|_{\rm ess}=1.}
 \tag{4}
\]

Witnesses need only the high strip `[kappa+eta,kappa+W]` and the low cosine `cos(2pi t/L_i)` on each cuff. Choose `W,eta` before taking the tail limit. Section 5 gives the strict sufficient margins; no optimal numerical width is claimed.

## 2. The actual coupled lower certificate with nonconstant carriers

First ground a sufficiently far tail and restrict to symmetric face traces. For a finitely supported coefficient vector `u`, put

\[
 f_{u,i}(t)=u_i\cos(\nu_i t),\qquad
 \nu_i=2\pi/L_i,\qquad a_i=\cosh(\pi\nu_i)=1+O(L_i^{-2}).
 \tag{5}
\]

Eventually `0<nu_i<kappa`. Let `A_(e,+)[u]` be the infimum of the actual symmetric energy of `f_u+z`, with all remote symmetric transitions free, and all remote symmetric constants free exactly when `e=1`.

For a positive node `a` near one define

\[
 n(a)=\frac{\pi(a+1)}{2a},\qquad \theta(a)=\frac{a-1}{a+1},
 \qquad Q_j(a)=\prod_{\xi\in\Xi_j}
       \left(\frac{a-\cosh(\pi\xi)}{a+\cosh(\pi\xi)}\right)^2,
 \quad Q_0(a)=1,
 \tag{6}
\]

where `Xi_j` is the complete positive transition lattice on cuff `j`. Set `q_i(a)=min(Q_(i-1)(a),Q_(i+1)(a))` and `chi_(e,i)=theta(a_i)^(2e)`, interpreting `chi_(0,i)=1`.

For every nonconsecutive support `I`,

\[
 \boxed{A_{e,+}[u]\ge c\sum_{i\in I} n(a_i)\chi_{e,i}Q_i(a_i)
 \left[s_{i-1}^{-1}Q_{i-1}(a_i)+s_i^{-1}Q_{i+1}(a_i)\right]|u_i|^2.}
 \tag{7}
\]

Here is the extension of PF-363's constant certificate. Its trace-preserving corridor bound (16) applies to arbitrary traces. For the present edge differences, PF-361's concentration estimate applies to both unequal transition lattices, the first nonzero cosines, and optional constants. The latter add only a bounded number of exponential terms; the small-width condition and growing embedded window remain valid. Thus every edge window controls a fixed fraction of the full `L^2(sech(t)dt)` norm, uniformly in all trial coefficients.

On an edge incident to `I` there is only one retained cosine. Independently relax the transition coefficients from its two ends and, for `e=1`, their constant difference. The scalar cosine Gram identity is

\[
 \langle\cos(\xi t),\cos(\zeta t)\rangle_{\operatorname{sech}}
 =\frac{\pi\sqrt{(x+1)(y+1)}}{x+y},
 \qquad x=\cosh(\pi\xi),\quad y=\cosh(\pi\zeta).
 \tag{8}
\]

The classical Cauchy distance product gives `n(a_i)` times the residual factors for the union of both transition sets. Counting any duplicate transition nodes twice only decreases this positive product. The optional constant is the node `1`, counted **once** even though both endpoints carry a free constant. Its factor is exactly `theta(a_i)^2`. Sines are odd and orthogonal to these even functions in the scalar full-line norm; no global reflection symmetry of `M` is assumed. Sum the resulting edge bounds and discard other nonnegative edges to get (7).

This argument bounds every global trial, not just a trial with remote traces fixed. Infima over the designated closures equal algebraic infima, so (7) survives completion. Different first-mode frequencies on different cuffs do not require any Diophantine separation.

The additional loss is explicit:

\[
 \theta(a_i)=\tanh^2(\pi^2/L_i),\qquad
 \chi_{1,i}=\tanh^4(\pi^2/L_i)\asymp L_i^{-4}.
 \tag{9}
\]

## 3. A complete-pant upper trial with constants absent or eliminated

Let `J_i` contain every positive lattice frequency in `(kappa,kappa+W]`, divided into transitions and the retained high strip. Define

\[
 P_i(a)=\prod_{\substack{\xi\in J_i\\\xi\ge\kappa+\eta}}
       \left(\frac{a-\cosh(\pi\xi)}{a+\cosh(\pi\xi)}\right)^2.
 \tag{10}
\]

Let `r_(e,i)` be the exact weighted least-squares residual of `cos(nu_i t)` against the `J_i` cosines, adding the constant to that minimizing space only for `e=1`. Equation (8) gives

\[
 H[r_{e,i}]=n(a_i)\chi_{e,i}Q_i(a_i)P_i(a_i),\qquad
 H[f]=\int_{\mathbb R}|f(t)|^2\operatorname{sech}t\,dt.
 \tag{11}
\]

We must also pay for the Fourier coefficients in actual energy. Let `G_i` be the physical cosine Gram matrix on `J_i`. PF-364 (10)–(11) proves, uniformly in lattice rounding, that for every fixed `a>a_0(W)`,

\[
 \lambda_{\min}(G_i)\ge e^{-aL_i},\qquad
 a_0(W)=O_\kappa\bigl(W\log(1/W)\bigr)\longrightarrow0.
 \tag{12}
\]

This is the single-cuff cluster bound, not an inverse estimate for neighboring nearly coincident lattices. When `e=0`, projection contractivity gives `||c_i||_2^2<=n(a_i)e^(aL_i)` for the compensating band coefficients.

For `e=1`, first project scalar functions off the constant. Applying the one-node Schur identity to (8) gives the residual band Gram matrix

\[
 G_i^{/1}=\Theta_iG_i\Theta_i,\qquad
 \Theta_i=\operatorname{diag}\left(
     \frac{\cosh(\pi\xi)-1}{\cosh(\pi\xi)+1}\right)_{\xi\in J_i}.
 \tag{13}
\]

Every diagonal entry is at least `tanh^2(pi kappa/2)>0`. The target's squared residual norm is `n(a_i)theta(a_i)^2`. Thus, for the same physical band coefficients,

\[
 \|c_i\|_2^2\le C_\kappa n(a_i)\theta(a_i)^2e^{aL_i}.
 \tag{14}
\]

The constant coefficient is fixed by orthogonality to `1`. Since `H[1]=pi` and `|<cos(xi t),1>|<=pi`, its absolute value is at most `1+sum|c_(i,xi)|`. In both cases the full coefficient absolute mass, including the retained cosine and optional compensating constant, therefore obeys

\[
 \mathcal A_{e,i}^2\le C(1+|J_i|e^{aL_i})\le C L_i e^{aL_i}.
 \tag{15}
\]

Only this scalar calculation uses (13). It does not assert that projection off all actual-energy constants acts cuffwise or commutes with pant assembly.

The complete single-module upper trial PF-364 (8), obtained from PF-344, is

\[
 M_{\rm sym}[f]\le C_Kd_iH[f_i]+C_KL_i\mathcal A_i^2
 \quad\text{for support on module }i,\quad |\xi|\le K.
 \tag{16}
\]

It includes both adjacent complete pants and the actual symmetric seam. With `K=kappa+1`, all the present trial modes are covered on a far tail. Apply (16) to `u_i r_(e,i)` and set other traces to zero. Energies add on nonconsecutive support because no pant sees two nonzero modules. If `F_(e,+)[u]` is the further infimum after freeing the bounded symmetric high strip, then

\[
 F_{e,+}[u]\le C\sum_{i\in I}
 \left[d_i n(a_i)\chi_{e,i}Q_i(a_i)P_i(a_i)
                 +L_i^2e^{aL_i}\right]|u_i|^2.
 \tag{17}
\]

In the absent-constant case this trial has zero periodic mean on every cuff. In the shorted-constant case its constants are precisely allowed eliminated variables.

## 4. Restoring every antisymmetric eliminated mode

PF-350's uniform face-parity estimate also holds when the eliminated band contains the constant on every module. Its proof uses only a bounded-frequency single-mode pant upper bound, a dimension count and the actual antisymmetric strip coercivity. The enlarged dimension is still

\[
 r_i=\eta L_i/\pi+O(1),
 \tag{18}
\]

now with one additional constant. The same upper bound `C_K(D_i+1)`, `D_i=d_i/L_i`, holds for the normalized constant. The lower bound `Q_(-,i)>=1/[w_i(1+w_i^2)]` also includes frequency zero; it is a positive-shift strip estimate, not division by the Fourier frequency.

Pant positivity gives `C<=2 direct-sum C_ii` for the collective antisymmetric pant block. Consequently

\[
 C\le b Q_-,\qquad
 b\le C_K\sup_{i\ge m} w_i(1+w_i^2)r_i(D_i+1)
      \le C_\kappa\eta+\epsilon_m,\qquad \epsilon_m\to0.
 \tag{19}
\]

The additional constant contributes only `O(L_i^(-1)+w_i)` to this bound, using `w_i d_i<=C`. PF-350's positive-block argument then yields the sandwich `(1+b)^(-1)S_sym<=S_full<=S_sym` after all symmetric eliminated variables are shorted, whether those are `T_+` or `T_++C_+`. It holds uniformly in section size and retained cutoff.

Let `A_e[u]` and `F_e[u]` be actual squared distances from `f_u` to, respectively, all eliminated variables and eliminated-plus-full-high variables. Taking algebraic infima over finite sections containing each trial, then passing to the declared closures, gives

\[
 A_e[u]\ge(1+b)^{-1}A_{e,+}[u],\qquad
 F_e[u]\le F_{e,+}[u].
 \tag{20}
\]

The upper bound needs only the symmetric trial. No model-to-actual unitary equivalence or compactness transfer under a fixed form error is used.

## 5. Polynomial mean-removal loss fits inside the strict margins

Fix any `R>40/19`. The established prime-cuff estimates used in PF-364 give eventually

\[
 L_i\to\infty,\qquad \max(L_{i-1},L_{i+1})\le R L_i,
 \qquad d_i\ge c e^{b_0L_i}.
 \tag{21}
\]

Define

\[
 \delta=-\frac2\pi\int_\kappa^{\kappa+\eta}
                    \log\tanh(\pi\xi/2)\,d\xi,\qquad
 \gamma=-\frac2\pi\int_{\kappa+\eta}^{\kappa+W}
                    \log\tanh(\pi\xi/2)\,d\xi.
 \tag{22}
\]

All transition/high nodes stay a fixed distance above one. The logarithmic derivative of each squared residual factor in (6) is `-4x/(x^2-a^2)`, uniformly bounded for `a` near one. Since `a_i-1=O(L_i^(-2))` and neighboring lengths are at most `R L_i`, the Riemann sums give

\[
 Q_j(a_i)=e^{-\delta L_j+O(1)}\quad (j=i-1,i,i+1),
 \qquad P_i(a_i)=e^{-\gamma L_i+O(1)}.
 \tag{23}
\]

Divide (17) by (7), and use (9), (20)–(23). Uniformly for nonzero `u` on nonconsecutive support `I`,

\[
 \boxed{\frac{F_e[u]}{A_e[u]}\le C\max_{i\in I}
 \left[e^{-(\gamma-R\delta)L_i}
       +L_i^{2+4e}e^{-[b_0-a-(1+R)\delta]L_i}\right].}
 \tag{24}
\]

The constant-elimination factor cancels from the weighted approximation term; it costs only `L_i^4` in the nonsingular geometric term. Choose `W` small enough that `a_0(W)<b_0`, choose `a_0(W)<a<b_0`, and then choose `eta>0` sufficiently small that the transition concentration applies and

\[
 \gamma>R\delta,\qquad a+(1+R)\delta<b_0.
 \tag{25}
\]

Such widths exist: for fixed `W`, as `eta->0`, `delta->0` and `gamma` tends to a positive number. The two polynomial factors in (24) do not change these strict margins. Both distance ratios tend uniformly to zero on progressively farther spatial-parity spans.

## 6. Infinite angle and finite head

Equation (7), followed by (20), makes each tail residual low span infinite dimensional. For `x=R_e f_u`, orthogonal distance in the actual energy gives

\[
 \|Z_ex\|_M^2/\|x\|_M^2=1-F_e[u]/A_e[u].
 \tag{26}
\]

The kernel of every finite-rank operator meets each such infinite-dimensional span in a unit vector. Equation (24) makes its image under `Z_e` arbitrarily close to norm one on far enough spans. Finite-rank approximation of compact operators, and contractivity of `Z_e`, prove essential norm one on the grounded tail.

To restore the full finite head, project off the closed tail eliminated space first. There are only finitely many head transitions and, in the second operation, finitely many head constants. Their residual span `B` is finite dimensional. On each infinite-dimensional tail residual low span impose orthogonality to `B`. This preserves infinite dimension and leaves the denominator unchanged by full-head shorting. The old tail high/eliminated trials remain admissible, so the numerator cannot increase. The finite-rank argument proves (4) in both full completions of Section 1.

This does not replace the designated completion by another condition at infinity, eliminate other low modes, or infer a unit eigenvector or an intersection of the two closed retained spaces.

## 7. Prior art, verification and mathematical boundary

The scalar distance product is classical Müntz/Cauchy Gram algebra: J. M. Almira, *Müntz Type Theorems I*, Surveys in Approximation Theory 3 (2007), Section 2.1, pp. 154–155 ([journal copy](https://www.maths.tcd.ie/EMIS/journals/SAT/papers/10/10.pdf), S31). The one-constant residual congruence is also already displayed in PF-360 for the corridor model. Equations (13)–(15) use it only for coefficient control of a finite scalar trial.

The separation-independent concentration input is the classical Turán–Nazarov inequality, as stated in Theorem 1.1 of O. Friedland and Y. Yomdin, *An observation on the Turán–Nazarov inequality* ([primary paper](https://arxiv.org/abs/1107.0039), S34). PF-361 explicitly includes first nonzero modes and constants in its bounded extra term count. Positive shorting has the classical Anderson–Trapp context, *Shorted Operators. II*, SIAM J. Appl. Math. 28 (1975), 60–71 ([publisher](https://epubs.siam.org/doi/10.1137/0128007)); the actual completion argument used here is given above. Wentworth's [DtN determinant gluing paper](https://arxiv.org/abs/2209.11863) is nearby surface prior art, not a theorem establishing this normalized infinite-chain angle.

The literature audit covered Cauchy residual projection, positive shorting, and mean-zero DtN degeneration. These standard tools are not new. The derived addition is the actual-energy constant-sector obstruction: the coupled lower bound with its `L_i^(-4)` factor, the coefficient-controlled actual upper trial, and uniform antisymmetric constant elimination. PF-364 retained constants; PF-360 treated a model. Neither alone proved (4), and the actual two operations are not declared equivalent.

Supplementary standard-library `Fraction` checks verified 24 scalar controls: target nodes `a=1+epsilon`, `epsilon in {1/10,1/100,1/10000}`, with `N=1,...,8` band nodes `2+j/100`, `j=0,...,N-1`. Exact elimination verified the residual products with and without node `1`, their ratio `theta(a)^2`, the residual Gram congruence, sequential projection coefficients and their inverse-trace coefficient bound. Sixteen grounded-path controls used `d=2,...,5` modules, nonconsecutive carriers `1+10^(-(i+2))`, shared transition nodes `{2,3}` or unequal nodes `{2+i/11,3+i/13}`, and constants absent or globally shorted. Interior conductances were `10^(2i-3)` (`i=1,...,d-1`), both endpoint conductances `10^(-6)`, with no added grounds. Rational positive-semidefinite elimination verified the corresponding lower certificate (7). All passed. These checks concern scalar/network algebra, not pant PDE solves, the infinite limit or independent approval; scratch remains under `/tmp`.

The proof depends on the actual trace-preserving corridor lower bound, complete single-module pant upper trial, nearest-neighbor assembly, and strip coercivity used in PF-350/PF-363/PF-364. A failure of one of those inputs breaks the transfer. Broad bands outside (25), elimination of a growing low-frequency band, other conditions at infinity, and different observables remain outside this result. Constants being fixed to zero and constants being minimized are distinct operations even though both fail to restore compactness here.

Comparable nonprime flutes obeying the same geometric estimates have the same obstruction. It rules out compact Schatten or weak-Schatten membership for these particular actual-energy angles; it identifies no primality-specific invariant and implies nothing about RH. A standalone formal transcription of the classical Cauchy identity would omit the load-bearing geometric and completion bridge, so no bounded Lean or compute handoff is proposed for this result.
