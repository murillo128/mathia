# Prime-lattice research lines

This file records the current mathematical questions that survive the Prime-Lattice evidence. It is not a roadmap, task queue, status page, or history.

## Control the source-adapted mod-5 Schur gate through its stationary reflection lens and anisotropic remainder

PL-407--PL-428 reduce the local-factor gate to a finite covariance problem. At `p=5`, image admission is equivalent to the normalized residue correlation matrix satisfying the `1/4` Loewner threshold. Real same-shift character variances determine only `Re K`; imaginary coherences can change the cone verdict, so ordinary real scalar products in the character basis do not determine admission.

PL-429--PL-433 show that the missing orientation is representable without artificial complex source coefficients. Vertical modulation recovers complex coherence from real scalar responses; for the dyadic prime source a single quarter-turn shift `t_X=-pi/(2 log X)` together with `t=0` suffices, and Abel--Stieltjes transport controls the deformation using multiscale `L^2` norms. The vanishing physical shift is nevertheless a fixed microscopic displacement on the zero scale, so unshifted zero-side continuity is not enough when one works through the character/vertical-shift representation.

PL-434 identifies the unconditional theorem-strength gap: the directly matched MRSTT short-interval theorem already handles the quarter-turn twist and fixed mod-5 progression channels, but at density/first-moment scale rather than the covariance scale required to preserve the cone margin. Stronger logarithmic savings in the same norm do not close the polynomial transfer loss on polynomial short intervals.

PL-437 reduces the unresolved oriented sector to two coordinates. Reality and the residue diagonal determine the other imaginary combination, leaving

` s = Im(K_01+K_21) ` and ` f = Im K_13 `.

The residual Hermitian perturbation has operator norm `sqrt(s^2+f^2)`, giving a simple Weyl sufficient condition. PL-438 shows that this Euclidean disk is not the exact source-adapted gate. In an explicit residue-space `1+2+1` normal form, write the visible blocks as `gamma`, `A`, `b`, `a`, `w`; on the strict branch `gamma>0`, set

`E=A-bb^T/gamma`, `mu=(w/gamma)b`, `alpha=a-w^2/gamma`.

For `E` positive definite, the exact remaining cone condition is the ellipse

`(g-mu)^T E^(-1)(g-mu) <= alpha`,

with `g=2^(-1/2)(s-f,s+f)^T`. Its center, axes and radius budget are fixed by visible real-product data plus the residue diagonal. PL-438 gives an admissible positive covariance for which this ellipse certifies the cone while the PL-437 Weyl disk fails, so the strengthening is genuine. It does **not** prove that the actual prime covariance lies in the ellipse.

PL-439 sharpens the source side of this reduction. For the centered real residue signal `R=(R_0,R_1,R_2,R_3)` in the established order `(1,2,4,3)`, let `J(w)=int (w^T R)^2 dmu`. Then the entire oriented sector is recovered from two paired differences of four fixed real sign probes:

`Delta_s = J(1,-1,1,1)-J(1,1,1,-1) = 8s`,

`Delta_f = J(1,1,-1,-1)-J(1,-1,-1,1) = 8f`.

All four sign vectors have coordinate squares equal to one, so the full diagonal self-energy cancels identically inside each difference, even when the four residue variances are unequal. Thus the unresolved vector can be written directly as

`g=(1/(8 sqrt(2)))(Delta_s-Delta_f, Delta_s+Delta_f)^T`.

PL-440 then identifies the source symmetry carried by these two differences. After extending the four probes by zero at residue `0 mod 5`, the pair defining `Delta_s` has identical circular lag autocorrelation, while the pair defining `Delta_f` differs by exactly `4 chi_5(h)`. Therefore every residue-translation-stationary lag kernel contributes **zero** to `Delta_s`, whereas its contribution to `Delta_f` is exactly one quadratic-character lag projection. In source terms, `s` is a reflection/start-residue anisotropy channel, while `f` contains a single `chi_5` lag channel plus any nonstationary anisotropic remainder. This split is exact but does not assert that the actual moving prime covariance is stationary or that either surviving term is small.

PL-441 solves the image gate exactly on the lag-stationary slice. Writing the stationary covariance by diagonal variance `d`, lag-one value `u`, lag-two value `v`, and setting `m=(u+v)/2`, `f=u-v`, reflection block-diagonalization gives the exact conditions

`3d/4-m >= (sqrt(5)/2)|f|`,

`3d/4+m >= (1/2)sqrt(f^2+16m^2)`.

For `d>0`, with `x=m/d` and `y=f/d`, the feasible set is the compact wedge--ellipse

`-1/4 <= x <= 3/4`,

`|y| <= (2/sqrt(5))(3/4-x)`,

`y^2 <= 12(3/4-x)(x+1/4)`.

On this slice `Delta_s=0` and `Delta_f=8f`, so the quadratic-character mode has an exact admissible budget tied to the mean nonzero-lag correlation rather than a free “smallness” target. The two symmetric extremes already fail: raw common mode has `m/d=1`, while perfectly centered isotropic common mode has `m/d=-1/3`.

PL-441 also gives the correct approximate-stationarity gate. If the actual covariance is `S_stat+E`, then the dephasing map `Phi(A)=A-(1/4)Diag(A)` satisfies `||Phi(E)||_op <= (5/4)||E||_op`. A stationary model lying inside the wedge--ellipse with spectral margin `eta` therefore transfers positivity whenever `||E||_op<(4/5)eta`; a stationary model outside by a comparable margin cannot be repaired by a smaller anisotropic perturbation.

PL-442 removes the ambiguity in what stationary surrogate should be used. The ordinary Frobenius projection of the restricted `4x4` covariance onto the lag-stationary family need not remain positive semidefinite. By contrast, zero-extending to `Z/5Z`, averaging over cyclic shifts and then compressing back to the four nonzero residues gives a canonical Reynolds stationarization that preserves covariance positivity exactly. If `(m_F/d_F,f_F/d_F)` are the normalized restricted Frobenius coordinates and `(m_R/d_R,f_R/d_R)` the Reynolds ones, then

`(m_R/d_R,f_R/d_R)=(3/4)(m_F/d_F,f_F/d_F)`.

The same projection supplies the exact anisotropy energy

`||S_tilde-C||_F^2 = ||S||_F^2-(D^2+2U^2+2V^2)/5`,

which bounds the operator-norm remainder and can be compared directly with the PL-441 stationary spectral margin. Positivity of the Reynolds covariance itself is still weaker than the dephasing wedge--ellipse, so stationarization does not solve the arithmetic gate automatically.

The live arithmetic question is now concrete and representation-fixed: evaluate the **canonical cyclic Reynolds surrogate** of the centered fixed-mod-5 prime covariance, place its normalized `(m_R/d_R,f_R/d_R)` coordinates relative to the PL-441 wedge--ellipse, and prove that the exact Reynolds anisotropy energy is small enough compared with the dephasing spectral margin. Exact stationarity is not inherited from the source, positivity of the stationary surrogate is not enough, `Delta_s=0` alone does not imply stationarity, and a bound on the single quadratic-character probe is insufficient without the remaining covariance geometry. If the Reynolds surrogate has a robust interior margin and the anisotropy certificate fits inside it, the local-factor gate follows; if it lies robustly outside, small anisotropy cannot repair it.

The adversarial boundary remains load-bearing. Translation stationarity is a model slice, not a theorem about the whole source; centering and interval endpoints can create precisely the anisotropy measured by `Delta_s`; and identifying a nonprincipal character projection does not by itself supply a variance-scale saving. Existing first-moment or almost-all progression technology cannot be substituted for the required second-order fixed-source estimate.

## Keep representation completeness, exact cone geometry and arithmetic theorem strength distinct

The representation problem is now sharply separated from the number-theoretic one. PL-429--PL-432 show how the oriented sector can be observed through character-side vertical modulation; PL-437 compresses it to two coordinates; PL-438 identifies the exact strict-branch feasible ellipse; PL-439 realizes those coordinates as real signed-residue energy differences; PL-440 resolves their symmetry types; PL-441 identifies the exact stationary cross-section and the operator-norm tolerance for deviations from it; and PL-442 supplies a canonical covariance-preserving stationary projection plus an exact anisotropy budget. None of these results supplies the required arithmetic covariance estimate.

Any proposed completion should therefore state the exact branch hypotheses (`gamma>0`, `E` positive definite where the inverse ellipse is used), the centering convention, the cyclic zero-extension/Reynolds projection, how its stationary `(m/d,f/d)` coordinates sit in the PL-441 lens, how the exact anisotropy energy compares with the spectral margin, and the unconditional arithmetic input. A scalar theorem that sees only unshifted real products in the character basis is information-theoretically incomplete; a full complex-matrix theorem is stronger than representation requires; a restricted Frobenius-best stationary fit can leave the covariance cone; and positivity of the canonical Reynolds surrogate remains weaker than the actual dephasing condition.

## Which covariance estimate avoids the moment zero-free prerequisites?

**Linked intuitions:** [MI-064](intuition/MI-064-the-mod5-first-moment-premise-is-a-zero-free-input.md), [MI-065](intuition/MI-065-seam-filtering-recovers-sparse-arithmetic-poles-from-dyadic-variance.md) and [MI-063](intuition/MI-063-the-live-prime-lattice-gate-is-a-complex-polarized-lower-frame-at-covariance-scale.md).

For `H=floor X^theta`, PL-459--PL-463 and PL-466 distinguish the following unproved actual-prime inputs. The first three rows require every sufficiently large real `X`; the fourth requires every sufficiently large dyadic `X=2^j` only:

| Moment input | Fixed exponent range | Forced mod-5 zero-free half-plane |
| --- | --- | --- |
| Four-channel `int P_a-XH/4=o(X log X)` | `0<theta<1/2` | `Re s>1-theta` |
| Identity-residue raw `int P_1^2<=XH^2/16+O(XH log X)` | `0<theta<=1/2` | `Re s>1-theta` |
| Empirical `int (P_1-bar P_1)^2=O(XH(log X)^A)`, fixed finite `A>=0` | `0<theta<1` | `Re s>1-theta/2` |
| Same empirical bound at all sufficiently large dyadic scales | `0<theta<1` | `Re s>1-theta/2` |

Here integrals run over `[X,2X]`, `P_a` is the von-Mangoldt window in residue `a mod 5`, and `bar P_1` is its mean over that interval. The raw hypothesis at `theta=1/2` implies joint GRH; the empirical hypothesis there excludes zeros only in `Re s>3/4`. The first-moment family approaching `1/2` is equivalent to joint GRH, whereas the centered family implies joint GRH when its fixed exponents approach `1`. No converse is asserted for either second-moment hypothesis.

PL-461 shows that PL-458's single identity-diagonal pair input (B) already supplies the raw ceiling for `1/6<theta<1/2`, without the separate centering input (A). PL-462 preserves that ceiling under one selected twist per scale of size `|t_X|=O(X sqrt(log X)/H^(3/2))`. PL-463 closes the constant-mean escape by mean-zero Mellin probes and finite box-average inversion; fitting the observed mean does not erase nonconstant zero modes. PL-466 removes the all-real-scale requirement for the dyadic family: seam-vanishing weights give `D_m=Q_m+J_m F+G`, with `F` periodic and `G` holomorphic in the target half-plane. Sublinear arithmetic zero density excludes a pole progression of `F` and then excludes the polynomial residue sequences annihilated by the filter. A positive dyadic density with a full vertical pole progression passes the same variance bound, so this is an arithmetic rigidity theorem, not a generic sparse-scale interpolation principle.

[MI-066](intuition/MI-066-relative-frames-transfer-frontiers-but-admit-common-off-critical-poles.md) specifies what a relative frame can and cannot replace. For the actual prime source, PL-465 turns `S_X>=c_theta Diag(S_X)` at all sufficiently large real scales into `Theta_max-Theta_min<=1-theta` for the four character zero suprema. Exponents approaching `1` force a common supremum, not its value `1/2`. PL-467 realizes that escape with one bounded positive integer-supported source having finite symmetric off-critical pole sets and the `1/4` frame for every fixed `1-beta<theta<1`. Its variance is `asymp H^2 X^(2beta-1)`, exceeding `XH(log X)^A` whenever `beta>1-theta/2`. Thus even sparse noncancelling poles do not turn a relative floor into the absolute ceiling.

[MI-067](intuition/MI-067-two-box-lengths-recover-smooth-pole-tests-at-macroscopic-scale.md) retains a separate measurement repair. PL-474's full-zero-set test gives a floor on every large block for one length through `X/[log X (log log X)^r]`, `r>1`; a diagonal ceiling on any unbounded scale set at that near-linear length already implies joint GRH. PL-475 changes the operator to two lengths `H` and `K=floor(sqrt(2)H)`. Compact distributional deconvolvers give uniformly bounded mean-zero smooth tests; rounding contributes only `O(log X)` to the source pairing. Hence `V_1(X,H)/H^2+V_1(X,K)/K^2 >= c X^(2beta-1)` for every integer `1<=H<=X/20` whenever a mod-5 function has a zero of real part `beta>1/2`. The macroscopic conclusion requires both ceilings on the same base block, not a chosen small member of the pair. Rational-ratio common zeros and Liouville small divisors explain why merely adding another length is insufficient.

Can the actual source supply joint retained energies and deletion counts for this pair? PL-476, retained in MI-067, permits separate masks of whole integer starts and separate constant centers: the exact jump bound `|Delta S_L|<=log(3X)` recovers the complete tests at cost `(sqrt(X W_H)+B_H^2 log(3X))/H+(sqrt(X W_K)+B_K^2 log(3X))/K`. At `H=floor(X/20)`, an unbounded integer scale set and mask/center families fixed before epsilon, satisfying both `W_i<<_epsilon X^(1+epsilon)L_i` and `B_i<<_epsilon X^(3/4+epsilon)` for every epsilon, are equivalent to joint GRH modulo 5. The converse uses the prime-counting estimate under joint GRH with empty masks and centers `L_i/4`; it does not import a short-window Möbius estimate. PL-477 narrows the remaining question: can prime arithmetic reduce this bill when the same geometric gaps persist? Two fixed positive residue-supported sources, with leading density `1/4` and bounded jumps, give identical retained values for both lengths under one common mask but a signed smooth-target separation `asymp B^2/X`. Balanced packets have zero mass and first moment `-5m^2/4`; masking their primitive and both endpoint translates hides that response. For `B asymp X^gamma`, `gamma>3/4`, it exceeds square-root size while retained energies stay `O(X)`. Thus shared-source consistency, common masks and signed targets alone cannot save a power. These controls are not von Mangoldt coefficients and establish neither the necessity of the logarithmic factor nor an optimal prime deletion exponent.

PL-478 gives a second precise observation question in MI-067: can the actual prime source bound both ordinary sample-centered averages `Q_i/q_X <<_epsilon X^(1+epsilon)` on the prescribed grid of spacing `floor(sqrt X)`, on one unbounded integer scale set fixed before epsilon? This is equivalent to joint GRH modulo 5 despite a vanishing retained fraction. Nearest-sample cell weights give `(sqrt(X Wtilde_i)+log(3X)D_i)/L_i`, with `D_i=O(X^(3/2))` and maximal weight `O(sqrt X)` on that grid. The converse uses the GRH pointwise prime-counting estimate, not a complete mean square. Clustered gaps in PL-477 pay `D_i asymp B^2`, so count-based ambiguity does not contradict the grid criterion. Can prime arithmetic supply the required energies or reduce signed recovery cost at fixed geometry? Neither an optimal prime sample count nor the necessity of the logarithmic loss is established.

Alternatively, can the source satisfy the PL-438/PL-441 dephasing cone through a direct complex-polarized **relative lower frame** with an independent absolute input? One bounded character energy would control every residue variance through `E_chi>=c_theta tr S_X`; supplying that energy is a separate obligation. The PL-467 control has neither prime support nor an Euler product or completed functional equation. Neither paired inversion nor a relative frame supplies a variance ceiling. Any alternative source identity must specify its center, scale quantifiers and pole control. Empirical centering over base points remains distinct from the across-residue common-mode projection excluded by MI-062.

[MI-068](intuition/MI-068-empirical-energy-controls-prime-pole-tests-with-quarter-power-random-starts.md) uses `2ceil(X^(1/4))` independent uniform starts per channel to control bounded mean-zero tests at cost `sqrt(V_i)+sqrt(X)(log X)^3`. The joint empirical-energy ceiling on any common unbounded scale set fixed before epsilon is almost surely equivalent to joint mod-5 GRH. PL-483 excludes saving a sample-count power in uniform signed recovery using only positivity, prime-power support, bounded relative weights and PNT: one fixed pair of such sources has identical sampled windows on `X_k=4^k` almost surely eventually, yet smooth targets differ by `asymp X_k^(2kappa-1)`, `3/4<kappa<1-alpha`, for sample exponent `alpha<1/4`. Their common energy is the exact prime baseline's, not proved small. Which constraint specific to the canonical coefficients or which mandatory scale coverage excludes these balanced prime-capacity packets? This remains distinct from proving the actual energy ceiling or a necessary exponent for its criterion.
