# XF-121 — fixed target-time Toeplitz frame enables full-q transition insertion with only O(K) reserved roots

**Status:** `EXACT-DERIVED` + `DYNAMIC-REDUCTION` + `FULL-Q-SCALE` + `CONDITIONAL-TRANSITION-NONIDENTIFIABILITY` + `SHARP-MOMENT-CONE-BUDGET`. XF-120 showed that the full q-scale Xi source prefix can be realized exactly on a transition slice and can even reserve `1-o(1)` of the root slots for simultaneous double collisions. Its explicit remaining gap was time coherence: at a prescribed later target time `tau>0`, must one preserve the full XF-118 near-isometry in order to repeat the construction? No. The exact budget calculation is much cheaper.

Let `c_m(t)` denote the normalized canonical periodic power-sum trajectory through the admitted prefix, let

\[
T_K(c(t))=(c_{j-i}(t))_{0\le i,j\le K},
\qquad c_0(t)=1,
\tag{1}
\]

and keep the XF-118 scaling

\[
N=2q^2,\qquad K\asymp a^3\log a,\qquad N\asymp a^4,
\qquad \frac KN\to0.
\tag{2}
\]

Fix a target time `tau>0`. To force the periodic Newman threshold to equal `tau`, it is enough to reserve **only** `2R` root slots with `R>K`, rather than a positive fraction of the degree. If `n=N-2R` is the carrier degree and its normalized target moments are

\[
d_0=1,\qquad d_m=\frac Nn c_m(\tau)\quad(1\le |m|\le K),
\tag{3}
\]

then the associated Toeplitz section satisfies the exact affine identity

\[
\boxed{
T_K(d)=\frac Nn T_K(c(\tau))-\left(\frac Nn-1\right)I.
}
\tag{4}
\]

Consequently

\[
\boxed{
\lambda_{\min}(T_K(d))
=
\frac Nn\lambda_{\min}(T_K(c(\tau)))-\frac{2R}{n},
}
\tag{5}
\]

so positivity of the reserved-budget carrier moment problem is possible exactly when

\[
\boxed{
\lambda_{\min}(T_K(c(\tau)))\ge \frac{2R}{N}.
}
\tag{6}
\]

For the minimal invisible crystal choice `R=K+1`, the moment-cone price is only

\[
\boxed{
\frac{2(K+1)}N
\asymp \frac KN
\asymp \frac{\log a}{a}
\to0.
}
\tag{7}
\]

Thus the dynamic gate left by XF-120 is not preservation of asymptotic identity. At the truncated moment-cone level, only an `O(K/N)` lower spectral margin is needed to reserve a collision block invisible to the entire q-scale prefix. For an **exact prescribed-node equal-weight carrier**, a fixed two-sided Toeplitz frame at the target slice is already sufficient; no `o(1)` near-isometry is required.

## 1. The reserve cost is an exact Toeplitz eigenvalue identity

Suppose `2R<N`, put `n=N-2R`, and ask for `n` unit-circle carrier nodes `nu_1,...,nu_n` whose raw power sums equal the degree-`N` target data:

\[
\sum_{j=1}^n \nu_j^m=Nc_m(\tau),
\qquad 1\le m\le K.
\tag{8}
\]

Normalizing by the carrier degree forces exactly `(3)`. Since the Toeplitz diagonal is fixed at one, scaling only the nonzero moments gives

\[
T_K(d)-I
=
\frac Nn\bigl(T_K(c(\tau))-I\bigr),
\tag{9}
\]

which is equivalent to `(4)`. Every eigenvalue therefore transforms by

\[
\lambda\mapsto
1+\frac Nn(\lambda-1)
=
\frac Nn\lambda-\frac{2R}{n}.
\tag{10}
\]

This proves `(5)` and `(6)`. In particular the budget cost is not an artefact of Gershgorin, a coefficientwise estimate, or the Poisson regularization used later. If

\[
\lambda_{\min}(T_K(c(\tau)))<\frac{2R}{N},
\tag{11}
\]

then `T_K(d)` has a negative direction, so there is not even a positive representing measure with moments `d_m`, much less an equal-weight `n`-node realization. At equality the scaled problem lies on the boundary of the truncated moment cone. Hence `2R/N` is the **sharp cone-level price** of reserving `2R` root slots within this additive moment decomposition.

The collision block must have `R>K` in order to be invisible through degree `K`; therefore the smallest possible choice is

\[
R=K+1,
\tag{12}
\]

and `(7)` is the smallest cone-level reserve cost for the standard roots-of-unity double-collision mechanism. This is already much smaller than the static freedom exhibited in XF-120, which deliberately drove `2R/N` to one in order to show collision saturation.

## 2. A fixed Toeplitz frame is enough for exact equal weights

The sharp condition `(6)` guarantees only membership in the positive truncated moment cone. To obtain exactly `n` equal atoms without a boundary regularity theorem, impose the stronger but still very weak target-slice hypothesis that for some fixed constants

\[
0<\eta\le M<\infty
\tag{13}
\]

independent of the q-scale,

\[
\boxed{
\eta I\preceq T_K(c(\tau))\preceq M I.
}
\tag{14}
\]

This is a **fixed frame condition**, not the XF-118 conclusion `T_K=I+o_{op}(1)`. With `R=K+1`, equations `(2)` and `(4)` give `N/n=1+o(1)`, hence for all sufficiently large scales

\[
\frac\eta2 I\preceq T_K(d)\preceq 2M I.
\tag{15}
\]

The XF-119 Poisson-deconvolution argument extends from near-isometry to any such uniformly conditioned frame. The required modification is quantitative but elementary. Let

\[
r_K=e^{-\gamma/K},
\qquad
\widetilde d_m=r_K^{-m}d_m.
\tag{16}
\]

The inflated Toeplitz matrix is obtained from `T_K(d)` by the Schur multiplier

\[
A_{ij}=e^{\gamma|i-j|/K}.
\tag{17}
\]

For the difference multiplier `A-1`, the periodic Fourier multiplier estimate used in XF-119 has norm `omega(gamma)` with

\[
\omega(\gamma)\to0\qquad(\gamma\downarrow0)
\tag{18}
\]

uniformly in `K`: the periodic function `e^{\gamma|x|}-1` on `[-1,1]` has absolutely summable Fourier coefficients with total variation `O(\gamma)` as `gamma->0`. Choose fixed `gamma=gamma(eta,M)>0` so small that the Schur perturbation is less than `eta/4`. Then

\[
\frac\eta4 I\preceq T_K(\widetilde d)\preceq C_{\eta,M}I.
\tag{19}
\]

Truncated Herglotz therefore gives a positive representing measure `sigma_K` for `widetilde d`. Testing `(19)` against the degree-`K` Fejer packets gives uniform local mass at angular scale `1/K`; for fixed constants `c_{eta,M},C_{eta,M}>0`, every arc `I` of length comparable to `1/K` satisfies

\[
\frac{c_{\eta,M}}K
\le \sigma_K(I)
\le \frac{C_{\eta,M}}K.
\tag{20}
\]

Convolving with the Poisson kernel of radius `r_K` then produces a density `W_K` with

\[
0<c'_{\eta,M}\le W_K(\theta)\le C'_{\eta,M}<\infty
\tag{21}
\]

uniformly in `K`, while its first `K` moments are restored **exactly**:

\[
\widehat W_K(m)
=r_K^m\widetilde d_m
=d_m.
\tag{22}
\]

Thus `W_K` belongs to a fixed periodic doubling class. The Gilboa--Peled theorem already anchored in XF-085/XF-119 gives an equal-weight trigonometric quadrature of degree `K` for every prescribed node count

\[
L\ge C_{\eta,M}K.
\tag{23}
\]

Here the requested count is exactly

\[
n=N-2(K+1),
\tag{24}
\]

and `(2)` gives `n/K->infinity`. Hence for all sufficiently large q there are **exactly `n` unit-circle nodes** satisfying `(8)`.

The distinction between `(6)` and `(14)` is important. Equation `(6)` is the exact positive-measure reserve threshold. The fixed frame `(14)` is a convenient sufficient condition that supplies the uniform regularity needed by the presently available prescribed-node quadrature bridge. Closing the gap between these two conditions would strengthen the realization theorem, but is not required to obtain arbitrary-time nonidentifiability from any fixed target-slice frame.

## 3. O(K) reserved roots insert an exact transition at the target time

Take `R=K+1` and let `A_\tau(w)` be the degree-`n` carrier from Section 2. Choose a phase `phi` avoiding the finitely many carrier roots and define

\[
C_\phi(w)=(w^R-e^{i\phi})^2,
\qquad
F_\tau(w)=A_\tau(w)C_\phi(w).
\tag{25}
\]

The crystal has `R` distinct simple double roots and raw power sums

\[
P_m^{C_\phi}=0,
\qquad 1\le m<R.
\tag{26}
\]

Because `R=K+1`, the whole collision block is exactly invisible through the admitted q-scale. Therefore `F_tau` has degree `N`, all roots on the unit circle, and

\[
\boxed{
P_m^{F_\tau}=Nc_m(\tau),
\qquad 1\le m\le K.
}
\tag{27}
\]

Only

\[
2R=2K+2=o(N)
\tag{28}
\]

root slots are consumed by the transition gadget. Collision saturation is unnecessary: a **vanishing fraction of the divisor** already suffices to put the matched realization exactly on a transition slice.

Now evolve `F_tau` by the exact periodic polynomial heat flow, using target time `tau` as the observation slice. XF-087 gives the autonomous triangular power-sum dynamics through degree `K`. Since `(27)` matches the canonical target prefix exactly, uniqueness of that finite triangular ODE implies that the first `K` moments of the backward trajectory coincide exactly with the canonical admitted history on the whole interval from the source slice to `tau`. No factorization of the heat evolution into carrier and crystal sectors is needed.

At time `tau`, every root is on the unit circle and the crystal sites are exact double roots separated from the carrier by the choice of `phi`. The same collision-safe local discriminant law used in XF-099/XF-101/XF-120 makes the corresponding pair nonreal immediately below `tau`, while the periodic Pólya--Benz real-zero-preserver input makes the whole polynomial real-rooted for every later time. Hence

\[
\boxed{
\Lambda_{\rm per}(F)=\tau.
}
\tag{29}
\]

Therefore, under the target-slice frame hypothesis `(14)`, the **complete full-q-scale moment history admitted by the autonomous prefix is compatible with an arbitrary prescribed positive periodic transition time**. This is the full-q analogue of the XF-101/XF-104 nonidentifiability mechanism, obtained without requiring collision saturation and without requiring target-time near-isometry.

## 4. Stress tests and exact evidence boundary

There are three places where an overstatement would be easy.

First, positivity of `T_K(c(tau))` by itself is not being promoted to an exact `n`-node equal-weight theorem. The exact cone calculation only says that the scaled carrier is a positive truncated moment sequence once `(6)` holds. The prescribed-node step currently uses the uniform two-sided frame `(14)` to manufacture a bounded doubling density. A future boundary quadrature theorem could reduce that extra regularity, but it is not assumed here.

Second, this finding does not prove that the actual Xi q-scale Toeplitz section satisfies `(14)` at every fixed `tau>0`. XF-118 proves the much stronger near-isometry only at its source slice. The new conclusion is a reduction of the dynamic problem: **one no longer needs to propagate `o(1)` closeness to identity.** It is enough to retain any fixed two-sided Toeplitz frame at the chosen target slice. At the raw moment-cone level the required lower margin is smaller still, only `2(K+1)/N=o(1)`.

Third, the triangular closure does not assert that the full polynomial trajectory is the Xi function. It says exactly what the finite periodic interface says: once a target polynomial matches the first `K` canonical moments, its first `K` backward heat history is forced to match the admitted canonical prefix history. Information outside that prefix may still distinguish Xi from this control. Consequently the theorem rules out transition identification from the **full autonomous q-scale prefix plus a fixed target-time frame**, not from the entire Xi deformation.

The sharpness check is `(11)`: below the reserve threshold no positive carrier measure exists, so the `2R/N` cost cannot be improved by a more clever quadrature argument while keeping the same additive invisible-crystal decomposition. At the opposite extreme, XF-120 has `T_K(c(0))=I+o(1)` and therefore pays this cost with enormous room to spare, explaining why it could reserve `N-o(N)` rather than merely `O(K)` roots.

## 5. Consequence for the live Xi-flow fork

The time-coherence obstruction left by XF-120 is now substantially narrower. To extend the q-scale static counterexample to every fixed positive target time, it is **not** necessary to prove that the XF-118 Toeplitz section stays asymptotically equal to identity. A fixed target-time frame

\[
\eta I\preceq T_K(c(\tau))\preceq MI
\tag{30}
\]

already gives exact equal-weight realization after reserving the minimal invisible crystal, and the triangular heat law then supplies the exact prefix history and transition time. Even before that regularity step, the exact moment-cone obstruction only begins when

\[
\lambda_{\min}(T_K(c(\tau)))
\lesssim
\frac{K}{N}
\asymp\frac{\log a}{a}.
\tag{31}
\]

Thus a positive continuation of the Xi-flow program must now locate a genuinely dynamic loss of information large enough to drive the q-scale Toeplitz section close to the **boundary** of the moment cone, or use information outside the autonomous first-`K` power sums. Merely losing source near-isometry is not enough. Conversely, proving any uniform target-slice frame along a fixed positive heat interval would immediately push the XF-101 transition-nonidentifiability conclusion to the full natural q-scale.

## 6. Prior art and novelty boundary

No new external theorem is load-bearing. The prescribed-node equal-weight step uses the Gilboa--Peled doubling-weight theorem already anchored in `SOURCES.md` by XF-085 and reused in XF-119. The real-zero-preserver and collision inputs are likewise already anchored by the earlier periodic heat findings. A targeted prior-art audit did not identify an external result matching the line-specific affine reserve identity `(4)`--`(7)` or its composition with the autonomous Xi-prefix heat dynamics.

The new content is the exact **degree-reserve/spectral-margin law** `lambda_min > 2R/N`, the observation that the minimal invisible transition gadget costs only `2K+2=o(N)` root slots, and the extension of the XF-119 regularization argument from source near-isometry to any fixed two-sided target-time Toeplitz frame. `SOURCES.md` therefore needs no change. No active clue is resolved by this theorem: it sharpens the post-XF-120 dynamic gate rather than closing one of the older selector clues.