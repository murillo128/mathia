# VIS-370 — source-free commuting positive metrics are only spectral filters of the baseline Wang Gram

## Claim

Let

`A_W = B W^(1/2)`

be a Wang polynomial-coefficient map measured in an already priced positive coefficient metric `W>0`, and let

`G = A_W^* A_W`

be its source-free coefficient Gram operator. Let `C>0` be a positive Hermitian relative metric that commutes with `G`, and define

`H = W^(1/2) C W^(1/2)`.

Using the positive square root, write

`A_H = A_W C^(1/2)`.

Because `C` and `G` are commuting Hermitian matrices, they are simultaneously unitarily diagonalizable. Thus for some unitary `V`,

`G = V diag(lambda_i) V^*`,

`C = V diag(c_i) V^*`,

with `lambda_i>=0` and `c_i>0`. Then

`A_H^* A_H`
` = C^(1/2) G C^(1/2)`
` = C G`
` = V diag(lambda_i c_i) V^*`.

Therefore the squared singular values of `A_H` are exactly the multiset

`{lambda_i c_i}`,

and on every active sector `lambda_i=sigma_i^2>0` the new singular values are

`tau_i = sigma_i sqrt(c_i)`.

The nullspace of `A_W` remains the nullspace of `A_H`.

In particular, if the metric is generated from the source-free Gram by functional calculus,

`C = f(G)`

for a positive scalar function `f` on the spectrum of `G`, then

`tau_i = sigma_i sqrt(f(sigma_i^2))`.

So a positive metric fixed by a source-free spectral rule may change the apparent singular-value scale, even drastically, while adding **no new singular directions and no arithmetic source information**. It is exactly a spectral filter of the already existing Wang Gram geometry.

Two useful exact special cases make the accounting explicit.

On the active subspace, the power rule

`C_alpha = G^(-alpha)`

with `0<=alpha<=1` gives

`tau_i = sigma_i^(1-alpha)`.

At `alpha=1` the active spectrum is whitened to `tau_i=1`, while the corresponding relative metric eigenvalues are `sigma_i^(-2)`. Thus flattening a collapsing source-free singular direction transfers the full reciprocal-square cost into the coefficient metric.

Likewise the positive-definite ridge-whitening rule

`C_epsilon = (G + epsilon I)^(-1)`, `epsilon>0`,

gives

`tau_i = sigma_i / sqrt(sigma_i^2 + epsilon)`.

If the smallest active singular value is `sigma_min` and one demands `tau_min>=eta` for a fixed `0<eta<1`, then necessarily

`epsilon <= (eta^(-2)-1) sigma_min^2`,

and the relative metric eigenvalue in that weakest active direction obeys

`1/(sigma_min^2+epsilon) >= eta^2 sigma_min^(-2)`.

Hence increasingly strong ridge whitening of a collapsing Wang direction necessarily imports the reciprocal-square conditioning scale into the metric.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL SIMULTANEOUS DIAGONALIZATION/MATRIX FUNCTIONAL CALCULUS + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This proves no stronger estimate for the normalized Chebyshev-theta remainder, the prime number theorem remainder, zeta zeros, or RH.

## 1. The native object is the relative metric against the baseline Gram

`VIS-368` showed that a positive metric uniformly Loewner-comparable to the priced baseline changes Wang singular values only by bounded factors. `VIS-369` then showed the opposite extreme: if an arbitrary positive metric may align freely with the right-singular basis, it can prescribe any positive active singular spectrum.

The remaining wording-level loophole is subtler. A metric can be fixed by an apparently natural rule **before** the desired singular improvement is read off, while still being generated entirely from the source-free Wang operator itself. Whitening, inverse-Gram weighting, ridge normalization, fractional powers, and many regularized preconditioners have exactly this form.

The correct audit object is therefore the pair `(G,C)`, with

`G=A_W^*A_W`, `C=W^(-1/2) H W^(-1/2)`.

When `C` commutes with `G`, the metric respects every baseline singular eigenspace. The question is then not whether the rule was written down before plotting the new spectrum, but whether it introduces information external to the already priced source-free Gram geometry.

## 2. Commuting positive metrics admit an exact sectorwise classification

Since `G` and `C` are Hermitian and commute, the classical simultaneous spectral theorem gives a common orthonormal eigenbasis. In that basis,

`G=diag(lambda_i)`, `C=diag(c_i)`.

Moreover `C^(1/2)` is diagonal in the same basis, so

`A_H^*A_H = C^(1/2) G C^(1/2)=diag(lambda_i c_i)`.

No inequality or asymptotic estimate is used. Every baseline singular sector is merely multiplied by the positive square-root weight attached to that same sector.

Repeated singular values cause no difficulty. A commuting `C` preserves each eigenspace of `G`; diagonalizing `C` inside each repeated-eigenvalue block yields the same formula. The orientation of `C` inside such a block is immaterial to the baseline Gram because `G` is scalar there.

Thus a commuting positive metric cannot create cross-sector interference, a new rank direction, or a hidden cancellation between distinct baseline singular eigenspaces. Its entire effect is sectorwise spectral reweighting.

## 3. Metrics generated from `G` are deterministic spectral filters

The strongest source-free specialization is

`C=f(G)`.

Matrix functional calculus gives

`f(G)=V diag(f(lambda_i)) V^*`,

hence

`s_i(A_H)` as a multiset `= {sqrt(lambda_i f(lambda_i))}`.

Writing `lambda_i=sigma_i^2` gives the scalar transfer law

`Phi_f(sigma)=sigma sqrt(f(sigma^2))`.

The new spectrum can look qualitatively different from the old one. A power rule can change polynomial or exponential exponents; inverse-Gram weighting can whiten the spectrum; a ridge inverse can flatten well-resolved modes while leaving weak modes attenuated. None of that is evidence of arithmetic localization when `f` is chosen without arithmetic source data. The output is a deterministic transform of the source-free baseline singular values.

This is the metric-side analogue of classical spectral filtering. The point is not that every spectral filter is useless; it is that its conditioning effect must not be misidentified as newly extracted arithmetic information.

## 4. Whitening demonstrates the exact resource transfer

Take the active spectral rule

`f(lambda)=lambda^(-alpha)`.

Then

`lambda f(lambda)=lambda^(1-alpha)`,

so the active singular values become

`tau=sigma^(1-alpha)`.

For `alpha=1`, every active singular value becomes one. But the metric eigenvalue on that direction is

`c=sigma^(-2)`.

Thus a baseline direction of size `sigma` has not been made informative for free. It has been declared cheaper in the physical coefficient norm by exactly the reciprocal-square amount needed to compensate the baseline singular loss.

The ridge rule makes the same point without a singular metric:

`f_epsilon(lambda)=1/(lambda+epsilon)`.

Its active transfer law is

`Phi_epsilon(sigma)=sigma/sqrt(sigma^2+epsilon)`.

To keep a collapsing `sigma_min` at a fixed nonzero fraction `eta` of the whitened scale, `epsilon` must shrink on the order of `sigma_min^2`, and the relative metric weight on that direction grows on the order of `sigma_min^(-2)`. The apparent spectral rescue and the metric degeneration are the same resource written in two coordinate systems.

## 5. Wang consequence

The phrase “independently fixed positive metric” is therefore still too weak as a surviving mechanism after `VIS-369`.

A rule fixed independently of the **desired output spectrum** but constructed solely from the source-free Wang Gram, such as `C=f(G)`, is not a new arithmetic resource. More generally, any source-free positive metric commuting with `G` acts only by explicit sectorwise weights `c_i`, and those weights must be charged as the new resource.

This narrows the remaining positive-metric route. A genuinely meaningful candidate must do at least one of the following:

- be fixed by a physical coefficient/destination topology external to the baseline Wang Gram, with its relative sector weights and degeneration charged explicitly;
- depend on arithmetic source information not already contained in the source-free coefficient map, with the selection rule itself analyzed as a source estimate;
- fail to commute with the baseline Gram for an independently justified reason, while surviving the free-orientation control of `VIS-369`;
- or leave positive Hilbert geometry through a genuinely indefinite/non-Hilbert, nonlinear, noncompact/global, or infinite-dimensional mechanism whose physical norm is controlled.

A source-free spectral functional of `G` no longer qualifies merely because it is canonical, pre-registered, regularized, or physically convenient numerically.

## Prior-art audit

The algebra is classical. Commuting Hermitian matrices are simultaneously unitarily diagonalizable; see Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press (2013). Matrix functional calculus `f(G)` is standard; see Nicholas J. Higham, *Functions of Matrices: Theory and Computation*, SIAM (2008), DOI `10.1137/1.9780898717778`.

The interpretation as componentwise spectral filtering is also classical numerical linear algebra. Per Christian Hansen, James G. Nagy, and Dianne P. O'Leary, *Deblurring Images: Matrices, Spectra, and Filtering*, SIAM (2006), Chapter 6, DOI `10.1137/1.9780898718874.ch6`, treats regularization by singular-value spectral filter factors. The metric-side square-root filter here is not claimed to be a new regularization method or to coincide formula-for-formula with Tikhonov inversion; the reference bounds the prior-art concept that deterministic singular-sector reweighting is ordinary spectral filtering.

No novelty is claimed for simultaneous diagonalization, matrix functions, whitening, inverse-Gram metrics, ridge regularization, spectral filtering, or preconditioning. The Mathia-specific content is the negative-control consequence for the current Wang frontier: even a metric rule fixed in advance is non-identifying if the rule is generated entirely from the already priced source-free Wang Gram.

## Dependencies

- `VIS-354`: Wang tail coefficients form a source-free truncated Vandermonde moment map.
- `VIS-366`: fixed-depth positive compact polynomial sampling is priced by Vandermonde partition sums.
- `VIS-367`: growing compact depth has a universal Chebyshev/capacity conditioning baseline.
- `VIS-368`: uniformly comparable positive Hilbert metrics are bounded preconditioners.
- `VIS-369`: freely aligned degenerating positive metrics can prescribe the active singular spectrum.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this result.

## Research consequence

A pre-registered or canonical positive metric does not escape the Wang conditioning audit when it is built only from `G=A_W^*A_W`. **Every source-free commuting metric is an explicit sectorwise reweighting, and every spectral-functional metric `C=f(G)` is exactly a scalar filter of the baseline singular spectrum.** Whitening and regularized whitening demonstrate that dramatic spectral improvement can be obtained while paying the same inverse conditioning scale in the coefficient metric.

The positive-metric frontier should now require an external physical/source justification for the metric, not merely independence from the desired plotted spectrum. If the proposed metric is generated from the baseline Wang Gram, its effect is source-free preconditioning and must be quotiented before any arithmetic gain is credited.