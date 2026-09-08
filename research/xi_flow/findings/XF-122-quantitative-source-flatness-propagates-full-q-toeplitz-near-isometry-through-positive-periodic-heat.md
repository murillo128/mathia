# XF-122 — quantitative source flatness propagates full-q Toeplitz near-isometry through positive periodic heat

**Status:** `EXACT-DERIVED` + `SOURCE-SPECIFIC` + `FULL-Q-SCALE` + `UNIFORM-POSITIVE-TIME-PROPAGATION` + `TARGET-FRAME-CLOSURE` + `TRANSITION-NONIDENTIFIABILITY`. XF-121 reduced arbitrary-target transition insertion at the full XF-118 cutoff to a target-slice Toeplitz frame hypothesis. That hypothesis is in fact automatic for the actual Xi source prefix. The point is not a generic monotonicity theorem for Toeplitz eigenvalues. Instead, the proof of XF-118 contains substantially more quantitative decay than its headline `o(1)`, and the exact triangular heat law of XF-087 has a finite upper-Toeplitz formulation whose nonlinear Duhamel kernel has only logarithmic total multiplier mass.

Let

\[
T_K(c(t))=(c_{j-i}(t))_{0\le i,j\le K},
\qquad c_0(t)=1,
\tag{1}
\]

be the normalized periodic moment trajectory of XF-087, started from the full q-scale Xi prefix of XF-118. Keep

\[
N=2q^2,\qquad
\Delta^2\asymp q^{-3},\qquad
A:=N\Delta\asymp q^{1/2},
\tag{2}
\]

and

\[
K=\left\lfloor\frac{\log A+O(1)}{\Delta}\right\rfloor
\asymp A^3\log A,
\qquad
N\asymp A^4,
\qquad
\frac KN\to0.
\tag{3}
\]

Then the exact conclusion is

\[
\boxed{
\sup_{t\ge0}
\|T_K(c(t))-I\|_{\rm op}
\longrightarrow0.
}
\tag{4}
\]

More quantitatively, if

\[
\varepsilon_K:=\|T_K(c(0))-I\|_{\rm op},
\qquad
L_K:=\log(K+2),
\tag{5}
\]

then the following general propagation criterion holds whenever `K<N/2`:

\[
\boxed{
\varepsilon_K L_K^4=o(1)
\quad\Longrightarrow\quad
\sup_{t\ge0}\|T_K(c(t))-I\|_{\rm op}
\ll L_K^2\varepsilon_K=o(1).
}
\tag{6}
\]

The proof of XF-118 gives, after retaining its explicit Vinogradov--Korobov rates rather than collapsing them to `o(1)`,

\[
\boxed{
\varepsilon_K
\ll_B (\log A)^{-B}
\quad\text{for every fixed }B>0.
}
\tag{7}
\]

Since `L_K\asymp\log A`, `(7)` supplies the hypothesis of `(6)` with enormous room. Thus the fixed frame required conditionally in XF-121 is present at **every positive periodic heat time**, uniformly in the target time. Combining `(4)` with XF-121 removes its last target-frame assumption: for every prescribed fixed `tau>=0`, the complete autonomous first-`K` q-scale history is compatible with a degree-`N` periodic matched control whose periodic Newman threshold is exactly `tau`.

This is a negative structural conclusion for the current interface. The full natural q-scale autonomous moment history does not identify the transition time. Any positive Xi-flow theorem must now use information outside that prefix, couple the prefix to a larger scale in a way not closed by the triangular Volterra law, or invoke genuinely global entire-function/zero geometry.

## 1. XF-118 actually gives super-polylogarithmic operator flatness

XF-118 states only

\[
\|T_K(c(0))-I\|_{\rm op}=o(1),
\tag{8}
\]

because no rate was needed there. Its proof is stronger. Recall its smooth-carrier transform

\[
\mathfrak H_A(y)
=\frac1A\int\chi_A(\xi)e^{iy\xi}\,dS(\xi).
\tag{9}
\]

On every polynomial frequency window, the only off-critical amplification appearing in the paired zero sum is bounded by

\[
(\log A)^{O(1)}
\exp(-d_A\ell),
\qquad
 d_A\ell
\asymp
\frac{(\log A)^{1/3}}{(\log\log A)^{1/3}}.
\tag{10}
\]

This is `o((log A)^(-B))` for every fixed `B`. The paired non-amplified boundary terms, the resonant blocks and the endpoint correction are only `A^{-1}` times polylogarithms. The far-zero tail can be made `A^{-C}` by taking the integration-by-parts order large enough. Therefore the proof of XF-118 equation `(11)` may be retained quantitatively as

\[
\boxed{
\sup_{|y|\le A^C}|\mathfrak H_A(y)|
\ll_{B,C}(\log A)^{-B}
}
\tag{11}
\]

for every fixed `B,C>0`.

The Fourier-lift step in XF-118 loses no dimension factor. For an arbitrary unit vector `v`, its autocorrelation is converted into the positive periodic density `|P_v|^2`, whose mass over one period is exactly one, while the fixed cardinal multiplier is Schwartz and summable over aliases. Splitting the Fourier integral at `|s|=A`, equation `(11)` controls the central part and arbitrary Schwartz decay controls the tail. Re-running XF-118 equations `(36)`--`(42)` therefore yields

\[
\sup_{\|v\|_2=1}
|v^*(T_K(c(0))-I)v|
\ll_B(\log A)^{-B},
\tag{12}
\]

which is exactly `(7)`.

This quantitative extraction is load-bearing below. Merely knowing `epsilon_K=o(1)` would not suffice for the argument because one-sided diagonal projections on `(K+1)`-dimensional matrices have an unavoidable logarithmic norm loss. The source proof beats every such logarithmic loss.

## 2. The exact triangular heat law closes on one nilpotent Toeplitz matrix

Normalize the XF-087 power sums by

\[
c_m(t):=\frac{P_m(t)}N.
\tag{13}
\]

Its exact collision-safe ODE becomes

\[
\boxed{
 c_m'
 =-\Delta^2m(N-m)c_m
 -\Delta^2Nm\sum_{i=1}^{m-1}c_i c_{m-i},
 \qquad 1\le m\le K.
}
\tag{14}
\]

No mode above `m` enters. Let `S` be the nilpotent unilateral shift on `C^{K+1}`, with `S^{K+1}=0`, and define the strictly upper Toeplitz matrix

\[
U(t):=\sum_{m=1}^{K}c_m(t)S^m.
\tag{15}
\]

Then

\[
T_K(c(t))-I=U(t)+U(t)^*.
\tag{16}
\]

If `Dcal(S^m)=mS^m`, equation `(14)` is the exact finite matrix equation

\[
\boxed{
U'
=-\Delta^2N\,\mathcal D(U+U^2)
+\Delta^2\mathcal D^2U.
}
\tag{17}
\]

The truncation in the quadratic term is automatic: powers `S^m` with `m>K` are zero. Thus `(17)` is not a model, an infinite-series formalism or an approximation to XF-087. It is precisely the first-`K` autonomous periodic heat system.

Put

\[
\lambda_m:=\Delta^2m(N-m).
\tag{18}
\]

The variation-of-constants formula for `(17)` is

\[
\boxed{
U(t)
=\mathcal M_tU(0)
-\int_0^t\mathcal B_{t-s}(U(s)^2)\,ds,
}
\tag{19}
\]

where the two diagonal multipliers are

\[
\mathcal M_r(S^m)=e^{-\lambda_m r}S^m,
\tag{20}
\]

and

\[
\mathcal B_r(S^m)
=\Delta^2Nm\,e^{-\lambda_m r}S^m.
\tag{21}
\]

The remaining proof is an operator-norm estimate on these two explicit multipliers.

## 3. One-sided Toeplitz multipliers cost only logarithms

Let

\[
R_\theta=\operatorname{diag}(1,e^{i\theta},\ldots,e^{iK\theta}).
\tag{22}
\]

Conjugation by `R_theta` multiplies the `m`-th upper diagonal by a phase. Consequently every diagonal multiplier

\[
\mathcal A\!\left(\sum_{m=1}^Kx_mS^m\right)
=\sum_{m=1}^Ka_mx_mS^m
\tag{23}
\]

has the elementary Fourier representation

\[
\mathcal A(X)
=\frac1{2\pi}\int_{-\pi}^{\pi}
k_A(\theta)
R_\theta X R_\theta^*\,d\theta,
\qquad
k_A(\theta)=\sum_{m=1}^Ka_me^{im\theta},
\tag{24}
\]

up to the immaterial phase convention. Hence

\[
\|\mathcal A\|_{op\to op}
\le\frac1{2\pi}\|k_A\|_{L^1}.
\tag{25}
\]

Abel summation and the classical `L^1` bound for the one-sided Dirichlet kernel give

\[
\|k_A\|_{L^1}
\ll L_K\left(
|a_1|+\sum_{m=1}^{K-1}|a_{m+1}-a_m|+|a_K|
\right).
\tag{26}
\]

This same representation controls the initial analytic half of the Hermitian Toeplitz deviation. If

\[
H_0:=T_K(c(0))-I,
\tag{27}
\]

then projection onto its strictly upper diagonals is obtained by integrating the unitary orbit `R_theta H_0 R_theta^*` against the one-sided Dirichlet kernel. Therefore

\[
\boxed{
\|U(0)\|_{op}
\ll L_K\varepsilon_K.
}
\tag{28}
\]

For the linear heat multiplier `(20)`, `K<N/2` makes `m(N-m)` strictly increasing on `1<=m<=K`. Thus its coefficient sequence is positive decreasing and `(26)` gives, uniformly for `r>=0`,

\[
\boxed{
\|\mathcal M_r\|_{op\to op}
\ll L_K.
}
\tag{29}
\]

For `(21)` define

\[
b_m(r):=\Delta^2Nm\,e^{-\Delta^2m(N-m)r},
\qquad
b_*(r):=\max_{1\le m\le K}b_m(r).
\tag{30}
\]

The continuous envelope `x exp(-Delta^2 r x(N-x))` has logarithmic derivative

\[
\frac1x-\Delta^2r(N-2x),
\tag{31}
\]

whose derivative has only one turning point on `(0,K]`. Hence the envelope has at most two critical points and total variation `O(sup)`. Sampling at the integers preserves that bound, so `(26)` yields

\[
\boxed{
\|\mathcal B_r\|_{op\to op}
\ll L_K b_*(r).
}
\tag{32}
\]

The crucial fact is that the total mass of `b_*` is logarithmic, not proportional to `K`. Put

\[
\beta:=\Delta^2(N-K).
\tag{33}
\]

Since `N-m>=N-K`,

\[
b_m(r)\le\Delta^2Nm e^{-\beta mr}.
\tag{34}
\]

For `0<=r<=(beta K)^{-1}`, use `b_*<=Delta^2NK`; for `(beta K)^{-1}<r<=beta^{-1}`, maximize `m e^{-beta mr}` continuously; for `r>=beta^{-1}`, compare with the geometric tail. This gives

\[
\boxed{
\int_0^\infty b_*(r)\,dr
\ll
\frac{N}{N-K}(1+\log K)
\ll L_K.
}
\tag{35}
\]

Thus even an arbitrarily long positive heat interval presents only `O(log K)` total nonlinear multiplier mass to the first-`K` upper-Toeplitz algebra.

## 4. A small-data bootstrap propagates near-isometry for all positive time

Fix `T>0` and put

\[
X_T:=\sup_{0\le t\le T}\|U(t)\|_{op}.
\tag{36}
\]

Equations `(19)`, `(28)`, `(29)`, `(32)` and `(35)`, together with `||U^2||<=||U||^2`, give

\[
X_T
\le
C L_K^2\varepsilon_K
+C L_K^2 X_T^2.
\tag{37}
\]

Set

\[
A_K:=CL_K^2\varepsilon_K,
\qquad
B_K:=CL_K^2.
\tag{38}
\]

If `epsilon_K L_K^4=o(1)`, then `A_KB_K=o(1)`. For sufficiently large scale, the quadratic barrier in `(37)` therefore has a small branch below `2A_K`. Since `U(t)` is continuous and begins below that branch, the standard bootstrap/continuation argument gives

\[
\boxed{
X_T\le2A_K
\ll L_K^2\varepsilon_K.
}
\tag{39}
\]

The constants do not depend on `T`. Letting `T->infinity` proves

\[
\boxed{
\sup_{t\ge0}\|U(t)\|_{op}
\ll L_K^2\varepsilon_K.
}
\tag{40}
\]

Finally `(16)` gives

\[
\boxed{
\sup_{t\ge0}
\|T_K(c(t))-I\|_{op}
\le2\sup_{t\ge0}\|U(t)\|_{op}
\ll L_K^2\varepsilon_K.
}
\tag{41}
\]

This proves the general criterion `(6)`. Applying the super-polylogarithmic Xi source bound `(7)` proves `(4)`.

There is no root-separation assumption anywhere in this propagation. Equation `(14)` is the coefficient-level XF-087 law and remains valid through collisions and complex-root intervals. For the positive-time trajectory started from the exact unit-circle realization of XF-119, the existing real-zero-preserver input additionally says the actual periodic roots remain real modulo the period, but the operator estimate itself does not need root labels.

## 5. XF-121's target-frame hypothesis is therefore automatic

Fix any prescribed `tau>=0`. Equation `(4)` gives

\[
T_K(c(\tau))=I+o_{op}(1),
\tag{42}
\]

so for all sufficiently large q, for example,

\[
\frac12I\preceq T_K(c(\tau))\preceq\frac32I.
\tag{43}
\]

This is stronger than the fixed two-sided frame assumed in XF-121. Take its minimal invisible transition reserve

\[
R=K+1,
\qquad
n=N-2(K+1).
\tag{44}
\]

Because `K/N->0`, the rescaled carrier moments remain uniformly framed; XF-119/XF-121 Poisson deconvolution and prescribed-node quadrature then produce exactly `n` unit-circle carrier roots matching the raw degree-`N` target moments through `K`. Multiplying by

\[
(w^{K+1}-e^{i\phi})^2
\tag{45}
\]

uses only `2K+2=o(N)` additional root slots, changes none of the first `K` moments and inserts exact simple double collisions at the target slice.

The XF-087 triangular law then forces the first `K` backward moment history of this target polynomial to agree exactly with the canonical periodic q-scale history through the entire interval from the source slice to `tau`. The existing collision normal form makes the reserved pairs nonreal immediately below `tau`, while the periodic real-zero preserver keeps the polynomial real-rooted for every later time. Hence

\[
\boxed{
\Lambda_{\rm per}=\tau.
}
\tag{46}
\]

for a degree-`N` matched control carrying the complete autonomous first-`K` Xi q-scale history.

Thus the conditional statement at the end of XF-121 becomes unconditional **within the finite periodic q-scale interface**:

\[
\boxed{
\text{full autonomous q-scale Xi moment history}
\not\Longrightarrow
\text{its periodic transition time}.
}
\tag{47}
\]

The target time was fixed only to match the intended Xi-flow interpretation. The frame estimate `(4)` itself is uniform over all `t>=0`.

## 6. Stress tests and evidence boundary

**Qualitative source coercivity alone is not being overused.** The proof loses logarithms twice before the bootstrap and twice in the quadratic smallness condition. The sufficient hypothesis is explicitly `epsilon_K log^4 K->0`, not merely `epsilon_K->0`. XF-118 satisfies the stronger condition because its underlying Vinogradov--Korobov estimate is super-polylogarithmic. A generic near-identity Toeplitz sequence with no quantitative rate is not covered.

**No hidden high-mode feedback is discarded.** The nonlinear coefficient of mode `m` in `(14)` uses only modes `1,...,m-1`. In the nilpotent shift algebra, `U^2` performs exactly that convolution and terms above `K` vanish only after they have already ceased to affect the admitted prefix. This is the same exact triangular closure used in XF-087/XF-101/XF-121.

**The logarithmic multiplier bound is not an unproved spectral monotonicity principle.** The argument never claims that `lambda_min(T_K(c(t)))` is monotone. It bounds the whole analytic upper-Toeplitz sector by an explicit Duhamel formula and unitary-orbit Fourier multipliers. Numerical or abstract counterexamples to monotonicity of individual nonextremal Toeplitz quadratic forms would therefore not affect the proof.

**Long time does not accumulate a linear-in-time error.** The key estimate `(35)` integrates the damped nonlinear multiplier over `[0,infinity)`. The total is only `O(log K)`, which is why `(40)` is genuinely uniform in positive time rather than a fixed-time Gronwall statement.

**This remains a finite periodic nonidentifiability theorem, not a theorem that Xi itself has arbitrary Newman constant.** The matched controls reproduce exactly the degree, equal-weight divisor geometry and complete first-`K` autonomous moment history admitted by the current interface. Information outside that interface may still distinguish Xi. Equation `(47)` says that such extra information is now logically necessary if the program is to obtain transition coercivity.

## 7. Consequence for the live Xi-flow fork

XF-118 closed the full q-scale source Toeplitz cone, XF-119 converted it to exact equal-weight real-divisor realization, XF-120 showed that a single slice could be collision-saturated, and XF-121 reduced arbitrary-target insertion to target-time frame retention. Equation `(4)` closes that last frame gate.

The current first-`K` power-sum architecture has therefore reached a clean negative endpoint: **even its complete exact positive-time history, at the full natural q-scale, is compatible with every prescribed fixed positive periodic transition time.** A further source-side or autonomous-prefix refinement cannot distinguish `Lambda` unless it introduces data that are not functions of those first `K` moments alone.

The surviving productive directions are consequently cross-scale or genuinely global: constrain how the q-scale prefix embeds into higher moments; use an observable whose heat evolution is not closed below `K`; or exploit Xi-specific entire-function/zero geometry that excludes the collision insertion despite exact agreement of the autonomous prefix. This is sharper than the previous statement that one merely needed a dynamic loss of Toeplitz coercivity: the actual positive periodic heat dynamics does **not** produce that loss.

## 8. Prior art and novelty boundary

No new external theorem is load-bearing. The Vinogradov--Korobov zero-free input needed for `(7)` is already anchored in `SOURCES.md` by XF-114/XF-118. The real-zero-preserver and equal-weight quadrature inputs used in the final transition insertion are already anchored by the earlier periodic heat and XF-085/XF-119 findings.

The `O(log K)` one-sided matrix projection and bounded-variation multiplier estimates are classical Fourier/triangular-truncation phenomena, and a targeted audit found the expected general triangular-projection and Toeplitz Schur-multiplier literature. Here the exact estimates needed in `(24)`--`(35)` are derived directly from unitary diagonal conjugation, Abel summation and the one-sided Dirichlet kernel, so no additional external result is used as evidence. `SOURCES.md` therefore needs no change.

The new line-specific content is the combination of three facts that had not previously been joined: the **super-polylogarithmic rate latent in the XF-118 source proof**, the **nilpotent upper-Toeplitz Duhamel form of the exact XF-087 triangular heat law**, and the **finite total nonlinear multiplier mass** that propagates source near-isometry uniformly for all positive time. Together they discharge the conditional target-frame gate of XF-121.