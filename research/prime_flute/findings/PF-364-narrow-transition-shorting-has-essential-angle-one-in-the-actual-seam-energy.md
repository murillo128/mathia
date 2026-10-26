# PF-364 — narrow transition shorting has essential angle one in the actual seam energy

**Status:** EXACT-DERIVED + CLASSICAL-APPROXIMATION-AND-SHORTING + ACTUAL-ENERGY-COMPLETION-OBSTRUCTION.

For every fixed lower physical cutoff `kappa>0`, sufficiently narrow fixed positive-width transition bands fail to compactify the low/high angle of the actual positive-shift prime-flute seam form. In the energy completion of finitely supported Fourier traces, eliminating the entire transition space, including both face parities and both sine/cosine sectors, leaves a canonical-correlation operator of **essential norm one**. Retained symmetric constants and a bounded high strip already witness this result.

The missing upper trial after PF-363 can be paid for. The optimal weighted cosine compensator on a narrow transition-plus-high band has coefficient cost with exponent tending to zero as the combined width tends to zero. The corridor conductance grows with a fixed positive exponent. Choosing the transition width smaller still makes both the high-approximation error and the nonsingular pant/seam cost negligible relative to PF-363's lower certificate against every remote transition.

This is an obstruction for a specified boundary-energy angle, not a Laplacian spectral, scattering, or RH theorem. It does not assert a global two-sided equivalence between the actual energy and the difference-only corridor model.

## 1. Actual form, completed space, and quantified statement

Use PF-205's fixed admissible natural seam cut, PF-214's exact nearest-neighbor pant assembly, and the shift `Delta+1`. The artificial-boundary parameters are inherited cuff coordinates centered at the zero-twist finite-finite perpendicular. Put

\[
 M=Q+\Lambda_E,\qquad
 d_i=s_{i-1}^{-1}+s_i^{-1},\qquad b_0=19/80.
 \tag{1}
\]

Initially take fields supported on finitely many modules, with finitely many Fourier modes on each face. Their actual minimized strip-plus-pant energy is positive definite. Let `H_M` be its Hilbert completion. One can first ground a sufficiently far tail by setting all earlier traces to zero and retaining the bordering pant. Section 6 removes that finite-head restriction within the same full energy completion.

For fixed `kappa>0` and `eta>0`, the eliminated algebraic transition space contains **every** physical sine and cosine with

\[
 \kappa<|\xi|<\kappa+\eta
 \tag{2}
\]

on each module and both seam faces. Let `T` be its closure in `H_M`, and `R_T=I-P_T`. Let `L_alg` and `H_alg` contain, respectively, every mode with `|xi|<=kappa` and `|xi|>=kappa+eta`, again on both faces. Define

\[
 \mathcal L=\overline{R_TL_{\rm alg}},\qquad
 \mathcal H=\overline{R_TH_{\rm alg}},\qquad
 Z=P_{\mathcal H}|_{\mathcal L}.
 \tag{3}
\]

Thus `Z` is a contraction. In a strictly positive finite section its singular data are those of the mixed block normalized by the **same shorted form's** two diagonal blocks. Formula (3) defines the infinite object without assuming bounded inverses for infinite Fourier matrices or convergence of independently normalized finite sections.

There exist `W_0>0` and, for each fixed `0<W<W_0`, an `eta_0(W)>0` such that

\[
 \boxed{\quad 0<\eta<\eta_0(W)\quad\Longrightarrow\quad
                 \|Z\|_{\rm ess}=1.\quad}
 \tag{4}
\]

Here `eta_0(W)<W`; witnesses use only the retained high frequencies in `[kappa+eta,kappa+W]`. The widths are fixed before the tail limit. The theorem establishes existence of an admissible range, not a numerical optimal cutoff.

## 2. Two actual geometric estimates with different jobs

Write `M_sym[f]` for the restriction to traces with equal values `f_i(t)` on both faces. Fixed parity normalization factors are absorbed into constants. For a finitely supported vector `u` let `f_u` be the field of constant values `u_i`. Let

\[
 A_+[u]=\inf_{z\in T_{+,\rm alg}}M_{\rm sym}[f_u+z],
 \tag{5}
\]

where all symmetric sine/cosine transitions throughout the tail are free. For the positive transition frequencies `Xi_i` put

\[
 Q_i=\prod_{\xi\in\Xi_i}\tanh^4(\pi\xi/2),\qquad Q_0=1.
 \tag{6}
\]

For `eta` sufficiently small, PF-363 (18)–(19) gives, on every nonconsecutive support `I`,

\[
 A_+[u]\ge c\pi\sum_{i\in I}
  Q_i(s_{i-1}^{-1}Q_{i-1}+s_i^{-1}Q_{i+1})|u_i|^2.
 \tag{7}
\]

This is a lower bound against **every** remote symmetric transition trial. Its ingredients are the trace-preserving actual corridor chart, restriction of the full pant energy, and PF-361's concentration on the union of two neighboring transition lattices. Even-weight orthogonality removes sines only in the relaxed scalar lower certificate; no global sine/cosine invariance of `M` is required here. The concentration restriction is on the transition width `eta`, since no high mode occurs in (5).

The separate upper estimate is PF-344 (13). In the present **unnormalized trace-value convention**, if `f` is supported on a single module and

\[
 f_i(t)=\sum_j a_j\cos(\xi_jt),\qquad 0\le\xi_j\le K,
 \quad \mathsf H[f_i]=\int_{\mathbb R}|f_i(t)|^2\operatorname{sech}t\,dt,
\]

then

\[
 M_{\rm sym}[f]\le C_K d_i\mathsf H[f_i]
                  +C_K L_i\Big(\sum_j|a_j|\Big)^2.
 \tag{8}
\]

Indeed multiply PF-344's normalized-trace bound by `L_i/2`; `w_i=O(1)` is absorbed. This upper trial already extends through both complete adjacent pants and includes the actual symmetric seam energy. It is not an extension of an uncompleted local quadrilateral minimizer.

For fields on nonconsecutive modules the energies in (8) add: no pant sees two nonzero retained/trial traces, and `Q` is module diagonal. This is the reason to use a spatial parity subspace. No global upper bound on a coupled arbitrary field is needed.

## 3. The weighted optimizer has a sufficiently small coefficient exponent

Fix `0<W<1`. On cuff `i` let `J_i` be every positive Fourier lattice point in `(kappa,kappa+W]`. These are consecutive with spacing `h=2pi/L_i`; put `N=|J_i|` and `m=N-1`. On the tail `N>=2` and `hm=W+O(L_i^{-1})`.

The exact weighted cosine Gram matrix is

\[
 G_{jk}=\frac{\pi\sqrt{(x_j+1)(x_k+1)}}{x_j+x_k},
 \qquad x_j=\cosh(\pi\xi_j).
 \tag{9}
\]

Set

\[
 K=\kappa+1,\quad R_0=\cosh(\pi K),\quad
 v_0=\pi\sinh(\pi\kappa/2),\quad B_0=2R_0/v_0.
\]

The constants use only `kappa`, not the chosen sufficiently small width. Cauchy elimination gives

\[
 (G^{-1})_{jj}=\frac{2x_j}{\pi(x_j+1)}
    \prod_{k\ne j}\left(\frac{x_j+x_k}{x_j-x_k}\right)^2.
\]

Since `x_j+x_k<=2R_0`, `|x_j-x_k|>=v_0 h|j-k|`, and
`j!(m-j)!>= (m/(2e))^m`, positivity and the inverse trace bound give

\[
 \lambda_{\min}(G)\ge\frac{\pi}{2N}
                  \left(\frac{hm}{2eB_0}\right)^{2m}.
 \tag{10}
\]

This is PF-348's narrow-cluster estimate applied to the **combined** transition/high band. Define

\[
 a_0(W)=\frac W\pi\log\frac{2eB_0}{W}\longrightarrow0.
 \tag{11}
\]

For every fixed `a>a_0(W)`, (10) implies `lambda_min(G)>=exp(-a L_i)` after a finite head.

Let `r_i=1+sum_(xi in J_i) a_(i,xi) cos(xi t)` be the exact weighted least-squares residual of the constant. Write

\[
 P_i=\prod_{\substack{\xi\in J_i\\\xi\ge\kappa+\eta}}
                    \tanh^4(\pi\xi/2).
\]

The transition/high partition covers all of `J_i`, including a lattice point exactly at the upper cutoff in the high sector. The classical Cauchy distance product yields

\[
 \mathsf H[r_i]=\pi Q_iP_i.
 \tag{12}
\]

Coefficient size requires a second argument: the compensating sum is minus the orthogonal projection of `1`, so

\[
 a_i^*G a_i\le\mathsf H[1]=\pi,\qquad
 \|a_i\|_2^2\le\pi e^{aL_i}.
\]

Consequently its full coefficient absolute mass satisfies

\[
 \boxed{\quad
 \mathcal A_i^2:=\left(1+\sum_{\xi\in J_i}|a_{i,\xi}|\right)^2
       \le2+2\pi N e^{aL_i}\le C L_i e^{aL_i}.\quad}
 \tag{13}
\]

This uses the smallest eigenvalue of the **single-cuff high/transition cluster**, not that of two potentially almost coincident neighboring lattices, and not that of a cluster containing the distant constant node. Projection bounds its norm before the coefficient conversion. Arbitrarily small frequency differences between different cuffs never enter (10)–(13).

## 4. Both errors vanish relative to the globally shorted denominator

Let `F_+[u]` be the infimum of `M_sym[f_u+z+y]` over all algebraic symmetric transitions and the chosen bounded symmetric high strip. On each `i in I`, use `u_i r_i` as a trial and set every other trace to zero. Equations (8), (12), and (13) give

\[
 F_+[u]\le C\sum_{i\in I}
       \left(d_iQ_iP_i+L_i^2e^{aL_i}\right)|u_i|^2.
 \tag{14}
\]

In particular the nonsingular pant cost has been retained, with its coefficient amplification. Put `q_i=min(Q_(i-1),Q_(i+1))`. Dividing (14) by (7) proves

\[
 \frac{F_+[u]}{A_+[u]}
 \le C\max_{i\in I}
 \left\{\frac{P_i}{q_i}
        +\frac{L_i^2e^{aL_i}}{d_iQ_iq_i}\right\}.
 \tag{15}
\]

For the exact prime cuffs, PF-348/PF-359 give

\[
 d_i\ge c e^{b_0L_i},\qquad L_i\to\infty,\qquad
 \max(L_{i-1},L_{i+1})\le R L_i
 \tag{16}
\]

eventually, for any fixed `R>40/19`. The deliberately conservative exponent `b_0=19/80` suffices. The inputs are the exact cuff law, the elementary positive gap lower bound, and Baker–Harman–Pintz's `21/40` upper gap exponent. No adjacent gap-ratio estimate is used.

Define

\[
 \delta=-\frac2\pi\int_\kappa^{\kappa+\eta}
                    \log\tanh(\pi\xi/2)\,d\xi,
 \quad
 \gamma=-\frac2\pi\int_{\kappa+\eta}^{\kappa+W}
                    \log\tanh(\pi\xi/2)\,d\xi.
 \tag{17}
\]

Riemann sums with uniformly bounded endpoint errors give
`Q_i=exp(-delta L_i+O(1))` and `P_i=exp(-gamma L_i+O(1))`. Hence (15) is at most the maximum over the support of

\[
 \boxed{C\left[
   e^{-(\gamma-R\delta)L_i}
   +L_i^2e^{-[b_0-a-(1+R)\delta]L_i}\right].}
 \tag{18}
\]

Both exponents can be made strictly positive. First choose `W` small enough that `a_0(W)<b_0/2`, and choose `a_0(W)<a<b_0`. Then take `eta>0` sufficiently small that PF-363's transition concentration applies and

\[
 \gamma>R\delta,\qquad a+(1+R)\delta<b_0.
 \tag{19}
\]

For fixed `W`, `delta->0` as `eta->0`, while `gamma` tends to a positive integral. Thus (19) holds for all sufficiently small positive `eta`. The first margin pays for neighboring transition relaxation; the second pays for the full geometric trial's coefficient cost. Qualitative weighted completeness or a raw `o(d_i)` error would supply neither margin.

## 5. Full transition parity and one infinite-space angle

Fix a sufficiently far grounded tail. Let `A[u]` be the squared distance of `f_u` from the full transition space, and `F[u]` its squared distance from transition plus full retained high space, in the actual energy completion.

PF-350's comparison, uniform over every finite support interval, gives

\[
 A[u]\ge(1+b)^{-1}A_+[u],\qquad F[u]\le F_+[u],
 \tag{20}
\]

with a finite constant `b<=C_kappa eta+epsilon_tail`. To pass the first bound to the infinite infimum, apply the finite-section comparison on any interval containing the support of `f_u` and any chosen transition trial, then take the infimum over all such intervals. Algebraic trials are dense in the designated transition closure. The second bound simply uses the symmetric high/transition trial as an admissible full-parity trial. No identification between the actual completion and the corridor-model completion is made.

Equations (18)–(20) imply `F[u]/A[u]->0` uniformly on the spans of constants supported on progressively farther parts of either spatial parity. The positive lower bound (7), together with (20), makes each residual span infinite dimensional. In (3), for `x=R_T f_u`,

\[
 \frac{\|Zx\|_M^2}{\|x\|_M^2}=1-\frac{F[u]}{A[u]}.
 \tag{21}
\]

Every finite-rank map has a nonzero kernel vector in each such span. Equation (21) therefore puts the distance from `Z` to every finite-rank map arbitrarily close to one. Finite-rank maps are norm dense in compact maps between Hilbert spaces; contractivity supplies the opposite bound. This proves (4).

Notice that a fixed parity-comparison loss does not prevent essential norm one: it multiplies the **vanishing distance ratio** in (20). Subtracting a fixed error from a single pairwise correlation would give a weaker conclusion. Enlarging the retained low/high spaces preserves these witnesses, so unbounded retained high frequencies and retained antisymmetric modes cannot repair compactness. The eliminated space remains exactly (2).

## 6. A finite head cannot remove the witnesses

In the full energy completion, let `T_tail` be the closed transition space on the chosen tail. Tail-supported algebraic fields have exactly the grounded-tail energy used above, including the bordering pant; their completion embeds isometrically into `H_M`.

Only finitely many Fourier modes satisfy (2) on the finitely many head cuffs. Let `E` be their residual span after projection off `T_tail`. It is finite dimensional and orthogonal to `T_tail`, and the full transition space is `T_tail op E`.

On each infinite-dimensional tail residual low span, impose orthogonality to `E`. This removes at most `dim(E)` dimensions. For the remaining vectors, projection off the full transition space equals projection off `T_tail`, so the denominator is unchanged. The old tail high/transition trials are still admissible, so the numerator cannot increase. The finite-rank argument in Section 5 applies again. Thus (4) holds with all head transition variables restored, in the completion specified in Section 1.

This argument does not identify that completion with every possible finite-energy trace space or every condition at infinity. It does not vary the original finite-head geometry or free additional nontransition variables as eliminated variables.

## 7. Prior art, controls, and evidence boundary

The scalar distance product and Gram-determinant method are classical; see J. M. Almira, *Müntz Type Theorems I*, Surveys in Approximation Theory 3 (2007), Section 2.1, pp. 154–155 ([journal copy](https://www.maths.tcd.ie/EMIS/journals/SAT/papers/10/10.pdf)). The exponential/power substitution and the diagonal cosine congruence yield (9), (12); the inverse diagonal and factorial bound are displayed above. Orthogonal-projection contractivity gives (13). None is claimed as a new general approximation theorem.

The concentration input underlying (7) is the classical Turán–Nazarov inequality as stated in Theorem 1.1 of O. Friedland and Y. Yomdin, *An observation on the Turán–Nazarov inequality* ([primary paper](https://arxiv.org/abs/1107.0039)), applied in PF-361/PF-363. The energy-space interpretation of shorting has classical context in W. N. Anderson, Jr. and G. E. Trapp, *Shorted Operators. II*, SIAM J. Appl. Math. 28 (1975), 60–71 ([publisher](https://doi.org/10.1137/0128007)). The projection and completion passages actually used here are proved in Sections 5–6.

R. A. Wentworth, *A Meyer-Vietoris formula for the determinant of the Dirichlet-to-Neumann operator on Riemann surfaces* ([primary paper](https://arxiv.org/abs/2209.11863)), supplies nearby DtN gluing/degeneration context. Its determinant theorem does not supply this growing-lattice, infinite-chain normalized-angle conclusion. The geometry used here remains exactly the canonical PF-344/PF-363 estimates. The prior-art audit covered Cauchy/Müntz approximation, weighted exponential concentration, positive shorting, and thin-gap/surface DtN degeneration. The contribution is the actual-energy transfer with the two independent margins (19), not a novelty claim about those classical tools.

Supplementary standard-library `Fraction` calculations checked 24 rational Cauchy controls: target node `1`, dimensions `1,...,12`, and nodes `x_j=2+j h`, `j=0,...,N-1`, for `h=1/100` and `1/10`. Exact elimination verified the residual product, every inverse diagonal, projection norm, the coefficient bound `||a||_2^2 <= (1/2) Tr(G^{-1})`, and its coefficient-absolute-mass consequence. All passed. These are exact checks of the exponential-kernel algebra, not numerical pant solves, prime-lattice computations, or validation of the infinite limit. Scratch remains outside Git. The proof, with the cited canonical geometric inputs, is the evidence; no Lean or independent adversarial approval is claimed.

The assumptions expose the relevant falsifiers. Failure of the coupled actual-trace lower certificate, the complete single-module upper trial, exact nearest-neighbor assembly, or uniform full-parity comparison would break the transfer. Removing the positive growth margin in (16), enlarging the transition band beyond the conditions (19), or eliminating additional low sectors requires a new argument. In particular this result does not decide the **actual** mean-zero or further-constant-shorted angle, even though PF-360 treats those operations in the corridor model.

The theorem applies equally to nonprime flutes satisfying the same geometric and period-growth estimates. It rules out compactness, and hence every compact Schatten/weak-Schatten class, for the stated transition-shorted angle. It does not decide relative resolvent ideals, wave operators, determinants, scattering, zeta zeros, or RH. A fixed wide transition band or a different observable remains outside this obstruction. The local clue therefore remains accepted for those distinct residual questions; its sufficiently narrow constant-retaining completed-angle repair is closed.

A small formal transcription of the classical Cauchy algebra would omit the load-bearing actual geometric estimates and completion bridge; the combined surface theorem is not proposed here as a bounded Lean task.
