# VIS-371 — every unitary-equivariant positive metric rule built from one Gram is spectral filtering

## Claim

Let `G>=0` be a Hermitian matrix on a finite-dimensional coefficient space, and let `F` be a rule assigning a positive-definite Hermitian matrix `F(G)` to every Hermitian positive-semidefinite input. Assume only unitary conjugation equivariance:

`F(U G U^*) = U F(G) U^*`

for every unitary `U`.

Write the spectral decomposition

`G = sum_lambda lambda P_lambda`.

Then there are positive scalars `c_lambda(G)>0`, one for each distinct eigenvalue of `G`, such that

`F(G) = sum_lambda c_lambda(G) P_lambda`.

In particular,

`[F(G),G]=0`.

Equivalently, for each fixed `G` there is a positive scalar function `f_G` defined on `spec(G)` with

`F(G)=f_G(G)`.

The values `f_G(lambda)` may depend on the complete spectrum of `G`; the theorem does **not** require one universal one-variable function `f` to work for every input. What is forced is the spectral character of the output: a basis-free rule whose only matrix input is `G` cannot select a preferred direction inside an eigenspace or mix distinct eigenspaces.

For a Wang coefficient map `A_W` with source-free Gram

`G=A_W^*A_W`

and relative positive metric

`C=F(G)`,

`VIS-370` therefore applies automatically. If `sigma_i^2=lambda_i` is an active baseline Gram eigenvalue, then the corresponding metric-modified singular value is

`tau_i = sigma_i sqrt(c_lambda_i(G))`.

Thus **every positive metric obtained from the source-free Gram alone by a unitary-equivariant, coordinate-free rule is only spectral filtering of the baseline Wang geometry**, even when the rule is not presented explicitly as `C=f(G)` and even when its coefficients depend on the full spectrum.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL ISOTROPIC/EQUIVARIANT MATRIX-FUNCTION REPRESENTATION + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This proves no stronger estimate for the normalized Chebyshev-theta remainder, the PNT remainder, zeta zeros, or RH.

## 1. Stabilizer equivariance forces block preservation

Fix `G` and let

`K_G={U unitary : U G U^*=G}`

be its stabilizer. Equivariance gives

`F(G)=U F(G) U^*`

for every `U in K_G`.

The stabilizer contains independent phase rotations on the distinct eigenspaces of `G`. If `lambda!=mu`, choose a unitary that acts by `e^(it)` on `ran(P_lambda)` and by the identity on `ran(P_mu)` and the remaining eigenspaces. From

`P_lambda F(G) P_mu = e^(it) P_lambda F(G) P_mu`

for every `t`, one gets

`P_lambda F(G) P_mu=0`.

So `F(G)` is block diagonal in the spectral decomposition of `G`.

No continuity, differentiability, polynomial form, or spectral simplicity is required.

## 2. Degenerate eigenspaces cannot carry a preferred orientation

Now fix one eigenspace `E_lambda=ran(P_lambda)`. Because `G` is scalar on `E_lambda`, every unitary acting arbitrarily inside `E_lambda` and identically on its orthogonal complement belongs to `K_G`.

Hence the block

`C_lambda=P_lambda F(G) P_lambda`

commutes with the full unitary group of `E_lambda`. The commutant of the full unitary group consists only of scalar multiples of the identity, so

`C_lambda=c_lambda(G) P_lambda`.

Positivity of `F(G)` gives `c_lambda(G)>0`.

Combining the blocks yields

`F(G)=sum_lambda c_lambda(G)P_lambda`.

Therefore `F(G)` commutes with `G`, including at repeated eigenvalues. The repeated-eigenvalue case is actually the stronger part of the statement: a genuinely coordinate-free rule cannot secretly choose an orientation inside a degenerate singular sector.

The same proof works over real coefficient spaces with orthogonal conjugation equivariance, replacing unitary rotations by the orthogonal stabilizer.

## 3. Spectral filtering is forced even without an explicit scalar formula

`VIS-370` treated positive metrics `C` that commute with the source-free Wang Gram and highlighted the familiar subclass `C=f(G)`. The present result removes a wording-level escape: a rule can be algorithmically complicated, depend on the whole spectrum, solve an optimization problem, or be advertised as a canonical normalization without being written down as an elementary scalar function.

If the rule uses **only** the matrix `G` and is invariant under a change of orthonormal coefficient coordinates, its output is nevertheless

`C=sum_lambda c_lambda(G)P_lambda`.

For a fixed `G`, define `f_G(lambda)=c_lambda(G)` on its finite spectrum. Then `C=f_G(G)` by the ordinary spectral functional calculus. The coefficients may be global spectral statistics—for example a weight assigned to `lambda_i` may depend on `tr(G)`, the condition number, all eigenvalue gaps, or another symmetric spectral summary—but the action remains sectorwise filtering.

Consequently a source-free metric rule does not become a new Wang mechanism merely because it is described through an invariant optimization or a global spectral normalization rather than a closed formula `f(lambda)`.

## 4. What a genuinely noncommuting source-free metric must import

Suppose a proposed positive metric `C` does **not** commute with `G`.

By the theorem, `C` cannot be produced from `G` alone by a unitary-equivariant rule. At least one additional structure must enter. Examples include a preferred coefficient basis, an ordering of packet labels, node locations retained separately from the Gram, another operator, a physical inner product, boundary data, or arithmetic source information.

That observation does not make the extra structure invalid. It changes the accounting. The surviving mechanism must identify the extra input explicitly and show why it is mathematically or physically fixed independently of the desired Wang spectral gain. If the extra structure is freely selectable, `VIS-369` remains the control: orientation against the right-singular basis can manufacture an arbitrary active singular spectrum. If the extra structure is arithmetic source data, the selection rule must be analyzed as part of the source estimate rather than credited as free geometry.

Thus the positive-Hilbert frontier sharpens from

“find a canonical noncommuting metric”

to

“identify the additional non-Gram structure that canonically fixes the noncommuting metric, and repay its information and norm cost.”

## Prior-art audit

The representation mechanism is classical. Isotropic tensor-function theory studies matrix/tensor-valued maps satisfying conjugation covariance and, for one symmetric tensor argument, represents the output in the algebra generated by that tensor. Classical sources include R. S. Rivlin and J. L. Ericksen, **Stress-deformation relations for isotropic materials**, *Indiana University Mathematics Journal* 4 (1955), 323–425, and G. F. Smith, **On isotropic functions of symmetric tensors, skew-symmetric tensors and vectors**, *International Journal of Engineering Science* 9 (1971), 899–916. Ken Kamrin and Sanjay Govindjee, **Clarifying the representation of isotropic symmetric tensor-valued functions of two symmetric tensors**, *Mathematics and Mechanics of Solids* 31:1 (2026), 172–182, DOI `10.1177/10812865251340424`, explicitly recalls the especially simple one-input representation and its historical lineage.

The proof used here is the elementary finite-dimensional stabilizer/commutant argument rather than a claim of a new general representation theorem. Standard spectral-theorem and matrix-functional-calculus background is also covered by Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press (2013), and Nicholas J. Higham, *Functions of Matrices: Theory and Computation*, SIAM (2008), DOI `10.1137/1.9780898717778`.

No novelty is claimed for isotropic/equivariant tensor-function representation, stabilizer commutants, spectral projectors, or functional calculus. The Mathia-specific consequence is the Wang negative-control boundary: a “canonical, basis-free” positive metric derived only from the already priced source-free Gram is forced into the spectral-filter class already closed by `VIS-370`.

## Dependencies

- `VIS-368`: uniformly comparable positive Hilbert metrics are bounded preconditioners.
- `VIS-369`: freely aligned degenerating positive metrics can prescribe the active singular spectrum.
- `VIS-370`: source-free commuting positive metrics are sectorwise spectral filters of the baseline Wang Gram.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this result.

## Research consequence

A source-free positive metric cannot evade the `VIS-370` filter audit merely by being called coordinate-free, canonical, invariant, or algorithmically defined. **If the only matrix input is the Wang Gram and the rule respects unitary changes of coefficient coordinates, commutation with the Gram is forced.**

Therefore a meaningful noncommuting positive-metric continuation must expose an additional structure not contained in the Gram alone. That structure—not the resulting singular-value improvement—is now the object that must be justified and charged. Positive-Hilbert localization based solely on invariant processing of the source-free Gram is closed as a standalone arithmetic mechanism.