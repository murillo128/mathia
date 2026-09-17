# MC-343 — Gaussian readout noise prices the inverse-precision loophole

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-340` shows that bounded-energy dephasing requires a transcript carrying a linear amount of joint reciprocal-source information. `MC-341` prices that information by Euclidean spread when distinct transcript states must remain metrically separated, while `MC-342` shows that bounded range, one-sided Lipschitz control, and every fixed positive-moment forward source-gradient budget still allow all source bits to be hidden at exponentially fine analog resolution.

A canonical **noisy readout** closes exactly that loophole.

Keep the reciprocal source notation of `MC-340`. Let `X` be the joint source vector, let

\[
T=\Phi(X)\in\mathbf R^d
\]

be any deterministic Euclidean transcript, and expose it only through an independent isotropic Gaussian readout

\[
Z=T+N,
\qquad
N\sim\mathcal N(0,\sigma^2 I_d),
\qquad
N\perp X.
\tag{1}
\]

Assume that the complete admitted coefficient observation `Y` is downstream of that noisy readout:

\[
X\longrightarrow T\longrightarrow Z\longrightarrow Y.
\tag{2}
\]

Write

\[
V_T:=\mathbf E\|T-\mathbf ET\|_2^2,
\qquad
D_T:=\operatorname{diam}(\operatorname{supp}T).
\tag{3}
\]

Then

\[
\boxed{
I(X;Y)
\le
\frac d2\log\!\left(1+\frac{V_T}{d\sigma^2}\right)
\le
\frac{V_T}{2\sigma^2}.
}
\tag{4}
\]

Since

\[
V_T
=\frac12\mathbf E\|T-T'\|_2^2
\le\frac{D_T^2}{2},
\tag{5}
\]

where `T'` is an independent copy, this also gives

\[
\boxed{
I(X;Y)
\le
\frac d2\log\!\left(1+\frac{D_T^2}{2d\sigma^2}\right)
\le
\frac{D_T^2}{4\sigma^2}.
}
\tag{6}
\]

Thus a bounded-range analog transcript no longer has unlimited source capacity once its readout has a fixed nonzero noise scale.

For the bounded-energy dephasing regime of `MC-340`, define

\[
L_R(\eta,C)
:=
\left[
\frac R2
\left(
\frac{\eta^2}{C}-\frac1{m^2}
\right)
-
\operatorname{TC}(X)
\right]_+,
\qquad
m=2^R-1.
\tag{7}
\]

If

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\tag{8}
\]

then `MC-340` forces `I(X;Y)>=L_R(eta,C)`. Combining this with `(4)`--`(6)` yields the necessary noise-resolution conditions

\[
\boxed{
\frac{V_T}{\sigma^2}
\ge
 d\left(e^{2L_R(\eta,C)/d}-1\right)
\ge
2L_R(\eta,C)
}
\tag{9}
\]

and, using only transcript diameter,

\[
\boxed{
\frac{D_T}{\sigma}
\ge
\sqrt{2d\left(e^{2L_R(\eta,C)/d}-1\right)}
\ge
2\sqrt{L_R(\eta,C)}.
}
\tag{10}
\]

For fixed `eta>0` and `C<infinity`, the reciprocal source law has `TC(X)=O(1)`, so

\[
L_R(\eta,C)
=
\frac{\eta^2}{2C}R+O(1).
\tag{11}
\]

Consequently any noisy Euclidean transcript capable of fixed nontrivial dephasing at bounded coefficient energy must obey at least

\[
\frac{D_T}{\sigma}=\Omega(\sqrt R).
\tag{12}
\]

If `d=O(1)`, the stronger first inequality in `(10)` forces

\[
\boxed{
\frac{D_T}{\sigma}
=
\exp(\Omega(R/d)).
}
\tag{13}
\]

More generally, `d=o(R/\log R)` forces superpolynomial signal-to-noise separation. Thus the exponentially fine scalar precision exposed by `MC-341`--`MC-342` reappears automatically when distinguishability is required to survive a fixed-dimensional noisy channel.

At the matched-filter floor there is an even sharper conclusion. `MC-340` proves that

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon
\]

requires

\[
I(X;Y)
\ge
J_R(\varepsilon)
:=
\left[
H(X)-R h\!\left(\varepsilon-\frac{\varepsilon^2}{2}\right)
\right]_+.
\tag{14}
\]

Therefore `(9)`--`(10)` remain valid with `L_R` replaced by `J_R`. For every fixed `0<=epsilon<1`,

\[
J_R(\varepsilon)
=
R\left[
\log2-h\!\left(\varepsilon-\frac{\varepsilon^2}{2}\right)
\right]+O(1),
\tag{15}
\]

so near-exact unit-energy dephasing also requires a growing noise-resolution budget.

At `epsilon=0`, `MC-340` requires `I(X;Y)=H(X)`. But for every `sigma>0` and every finite transcript alphabet, Gaussian kernels centered at distinct transcript values have overlapping positive densities everywhere. Hence `H(X|Z)>0`, so

\[
I(X;Y)
\le I(X;Z)
< H(X).
\tag{16}
\]

Thus

\[
\boxed{
\sigma>0,\quad \mathcal E(W)\le1
\quad\Longrightarrow\quad
\delta(W)>0
}
\tag{17}
\]

under the noisy-readout Markov architecture `(2)`. Exact matched-filter dephasing is a genuinely zero-noise idealization.

No estimate for `M(x)` follows. This is a finite reciprocal-endpoint conditioning theorem. Its role is to turn the qualitative “inverse precision must matter” conclusion of `MC-342` into an explicit Shannon-capacity budget.

## 1. Gaussian maximum entropy gives the transcript-capacity bound

Because `T` is deterministic from `X` and `Z` depends on `X` only through `T`,

\[
I(X;Z)=I(T;Z).
\tag{18}
\]

Data processing through `(2)` gives

\[
I(X;Y)\le I(X;Z)=I(T;T+N).
\tag{19}
\]

Let `Sigma_T=Cov(T)`. Then

\[
I(T;T+N)
=h(T+N)-h(N).
\tag{20}
\]

Among random vectors with a fixed covariance matrix, the Gaussian has maximal differential entropy. Therefore

\[
h(T+N)
\le
\frac12
\log\!\left((2\pi e)^d
\det(\Sigma_T+\sigma^2 I_d)
\right),
\tag{21}
\]

while

\[
h(N)
=
\frac12
\log\!\left((2\pi e)^d\sigma^{2d}\right).
\tag{22}
\]

Subtracting gives

\[
I(T;T+N)
\le
\frac12
\log\det\!\left(I_d+\frac{\Sigma_T}{\sigma^2}\right).
\tag{23}
\]

If `lambda_1,...,lambda_d` are the eigenvalues of `Sigma_T`, then concavity of `log(1+x)` gives

\[
\begin{aligned}
I(T;T+N)
&\le
\frac12\sum_{j=1}^d
\log\!\left(1+\frac{\lambda_j}{\sigma^2}\right)\\
&\le
\frac d2
\log\!\left(
1+
\frac{\sum_j\lambda_j}{d\sigma^2}
\right)\\
&=
\frac d2
\log\!\left(1+\frac{V_T}{d\sigma^2}\right).
\end{aligned}
\tag{24}
\]

Finally `log(1+u)<=u` proves the second inequality in `(4)`.

The estimate is the ordinary finite-dimensional additive-white-Gaussian-noise capacity converse, applied to the actual transcript distribution rather than optimized over inputs.

## 2. Diameter supplies a representation-scale invariant signal budget

For an independent copy `T'`,

\[
\mathbf E\|T-T'\|_2^2
=2\mathbf E\|T-\mathbf ET\|_2^2
=2V_T.
\tag{25}
\]

If the transcript support has diameter `D_T`, then `||T-T'||<=D_T` almost surely, proving `(5)`.

Substituting `(5)` into `(4)` gives `(6)`. Importantly, the resulting resource is the ratio `D_T/sigma`, not the raw diameter or raw noise variance. A simultaneous rescaling of the transcript and its physical readout noise leaves the statement unchanged. This avoids the trivial normalization defect that would arise from bounding `D_T` alone.

The dimension-free inequality

\[
I(X;Y)\le\frac{D_T^2}{4\sigma^2}
\tag{26}
\]

also shows that adding arbitrarily many Euclidean coordinates does not create unlimited capacity when the **total transcript diameter** and per-coordinate noise scale remain fixed. To transport `Theta(R)` source information, the total signal-to-noise resource itself must grow.

## 3. Composition with MC-340 gives the inverse-resolution price

Under `(8)`, `MC-340` gives

\[
I(X;Y)\ge L_R(\eta,C).
\tag{27}
\]

Combining `(27)` with the variance form of `(4)` gives

\[
L_R
\le
\frac d2
\log\!\left(1+\frac{V_T}{d\sigma^2}\right).
\tag{28}
\]

Exponentiating and rearranging proves the first inequality in `(9)`. The second follows from `e^u-1>=u`.

Likewise, combining `(27)` with `(6)` gives `(10)`. Since the explicit reciprocal source total correlation computed in `MC-340` is `O(1)`, equation `(11)` follows.

The two scales in `(10)` are complementary rather than contradictory:

- without restricting transcript dimension, the general information budget forces at least a square-root growth of `D_T/sigma`;
- when `d` is fixed or sublinear enough, finite-dimensional Gaussian capacity converts the same linear source-information requirement into exponentially or superpolynomially fine relative noise resolution.

This is exactly the operational distinction left open by `MC-342`: forward smoothness does not price tiny displacements, but noisy distinguishability does.

## 4. The dyadic control of MC-342 now pays its hidden cost

For even `R`, `MC-342` uses the scalar encoding

\[
T_R(B)=\sum_{i=1}^R2^{-i}B_i
\]

on the punctured binary source law. It has `d=1`, `D_T<1`, full source entropy, bounded forward Lipschitz constant, and bounded fixed-`p` source-gradient energies.

Suppose this scalar transcript is read only through Gaussian noise and then used by a unit-energy architecture with `delta(W)<=epsilon`. Equation `(14)` and the scalar form of `(10)` imply

\[
\boxed{
\sigma
\le
\frac{D_T}
{\sqrt{2\left(e^{2J_R(\varepsilon)}-1\right)}}.
}
\tag{29}
\]

For fixed `epsilon<1`, this is exponentially small in `R`. As `epsilon->0`,

\[
J_R(\varepsilon)\to H(X)
=\log(2^R-1),
\tag{30}
\]

so the required noise scale approaches the order of the least significant dyadic spacing `2^{-R}`. The precise constants differ because `(29)` is a channel-capacity converse rather than a nearest-neighbor decoding bound, but the exponential resolution currency is the same.

This shows that the `MC-342` encoder does not defeat a noise-robust capacity theorem. It defeats only forward-smoothness criteria that treat arbitrarily small nonzero displacements as perfectly distinguishable.

## 5. Positive Gaussian noise forbids exact source recovery

For completeness, assume the reciprocal source vector has at least two values with positive probability, as it does for every nontrivial rank here. Conditional on `X=x`, the noisy readout has density

\[
p_{Z|X=x}(z)
=
(2\pi\sigma^2)^{-d/2}
\exp\!\left(
-\frac{\|z-\Phi(x)\|_2^2}{2\sigma^2}
\right).
\tag{31}
\]

For `sigma>0` this density is strictly positive for every `z` and every source state `x`. Hence no observed `z` can assign posterior probability one to a source state while another source state has positive prior probability. Therefore

\[
H(X|Z)>0,
\qquad
I(X;Z)<H(X).
\tag{32}
\]

Data processing gives `(16)`. Combined with the exact unit-energy rigidity of `MC-340`, this proves `(17)`.

This strict statement is stronger than taking the limit of the coarse capacity upper bound: even an astronomically large but finite signal-to-noise ratio cannot provide **exact** recovery through a Gaussian channel. It can only make the residual conditional entropy arbitrarily small.

## 6. Prior art and novelty boundary

The information-theoretic mechanism is classical. Claude Shannon's 1948 *A Mathematical Theory of Communication* established channel capacity and the Gaussian-channel framework (Bell System Technical Journal **27**, 379–423 and 623–656; DOI `10.1002/j.1538-7305.1948.tb01338.x` and `10.1002/j.1538-7305.1948.tb00917.x`).

Thomas Cover and Joy Thomas, *Elements of Information Theory*, 2nd ed. (Wiley, 2006), Chapter 9, develops the additive Gaussian channel and its power-constrained capacity; the same text's maximum-entropy theorem gives the covariance-constrained entropy inequality used in `(21)`. Relevant Wiley chapter records are DOI `10.1002/0471200611.ch10` for the earlier-edition Gaussian-channel chapter and DOI `10.1002/047174882X.ch12` for maximum entropy.

A targeted prior-art audit on 17 September 2026 found no basis for claiming novelty for Gaussian maximum entropy, AWGN capacity, data processing, covariance trace bounds, or the fact that positive Gaussian noise prevents exact decoding of a finite constellation with zero error.

The durable Mathia delta is the composition with the independently derived reciprocal-source lower bound `MC-340`: equations `(9)`--`(13)` convert required Möbius-side source information into an explicit **relative noise-resolution budget**, and `(29)` shows that the artificial dyadic encoder of `MC-342` pays exactly the kind of exponentially fine readout precision that its forward regularity concealed. No claim is made that this composition is a new information-theory theorem outside this research program.

Primary/authoritative audit links:

- Shannon 1948, Bell System Technical Journal: `https://doi.org/10.1002/j.1538-7305.1948.tb01338.x` and `https://doi.org/10.1002/j.1538-7305.1948.tb00917.x`.
- Cover and Thomas, Gaussian channel chapter: `https://doi.org/10.1002/0471200611.ch10`.
- Cover and Thomas, maximum entropy chapter: `https://doi.org/10.1002/047174882X.ch12`.

## Boundaries and falsification tests

- **The noise geometry is an assumption, not an arithmetic theorem.** Additive isotropic Gaussian noise is meaningful only after a Euclidean transcript and its scale have been canonically tied to the analytic construction. An arbitrary nonlinear re-encoding can change what “additive Gaussian” means. This finding therefore closes the precision loophole conditionally on a source-natural noisy-readout model; it does not manufacture that model.
- **Independent post-transcript noise is essential.** The Markov chain `(2)` is load-bearing. Side information that bypasses `Z` can carry source information around the capacity bound.
- **Gaussianity is used explicitly.** The entropy calculation exploits the exact Gaussian noise entropy. A different noise law requires its own channel-capacity bound; covariance alone is not enough to substitute an arbitrary noise distribution into `(4)`.
- **Dimension is accounted for.** The exponential conclusion needs fixed or sufficiently small `d`. Without such a restriction, the always-valid consequence is the total signal-to-noise requirement `(9)` or the dimension-free diameter bound `(12)`.
- **Diameter is not required.** The sharper intrinsic statement is `(4)` in terms of transcript variance `V_T`. Diameter is only a convenient robust upper bound when the support is bounded.
- **No finite-noise exact decoder loophole exists.** Equation `(17)` does not rely on the capacity upper bound being tight; it follows from strict overlap of Gaussian kernels.
- **The theorem prices distinguishability, not arithmetic naturalness.** A future Möbius argument still has to prove that its actual admitted transcript is constrained by a canonical variance/diameter/noise scale. Choosing a convenient Euclidean chart externally would merely move the problem.
- **No RH-scale arithmetic estimate follows.** The theorem constrains a finite reciprocal-endpoint architecture and does not bound `M(x)`, prove a zero-free region, or exclude an off-critical zero.

## Consequence for the research line

`MC-340`--`MC-343` now separate four distinct resources cleanly. Joint source information is unavoidable; finite-dimensional metric support prices it through spread; forward smoothness cannot stop hierarchical sub-resolution encoding; but a canonical noisy readout converts sub-resolution coding into an explicit Shannon-capacity cost.

The live arithmetic question is therefore no longer whether “robustness” in the abstract can close the analog loophole. It is whether an actual Möbius-derived transcript comes with a **source-forced observation metric/noise or finite-resolution structure** for which `V_T/sigma^2`, `D_T/sigma`, dimension, or an analogous channel-capacity quantity can be bounded independently of the desired dephasing. Without that canonical bridge, noise can be imposed only as an external coordinate choice; with it, the endpoint obstruction becomes quantitatively coercive.