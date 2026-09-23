# VIS-413 — real Wang shells quantize finite-window Bargmann phase to 0 or pi

## Claim

Keep the strict near-band Wang dyadic shells from `VIS-313` and `VIS-412`,

`F_M(T)=sum_(lambda in Lambda_M) B_lambda exp(-i lambda T)`,

with

`B_(log(q/r))=a_q a_r K_H(log(q/r))`,

`K_H(lambda)=integral_0^H exp(-iu lambda) du`,

and real positive coefficient weights `a_q`.

Then every shell function is real-valued on the real `T` axis:

`F_M(T) in R` for every real `T`.

Indeed the shell support is symmetric under `lambda -> -lambda`, and

`B_(-lambda)=conjugate(B_lambda)`.

Consequently, for **any real nonnegative window or taper** `w(T)` with `0<integral w<infinity`, the weighted finite-window Gram entry

`G_(MN)^(w) = (integral w(T) F_M(T) F_N(T) dT)/(integral w(T) dT)`

is real. Hence every weighted Bargmann cycle

`Delta_C^(w)=G_(i_1 i_2)^(w) ... G_(i_m i_1)^(w)`

is real. Whenever the product is nonzero,

`arg Delta_C^(w) in {0, pi}`;

when it vanishes, its phase is undefined.

Thus the finite-window/tapered escape left open by `VIS-412` **cannot recover a genuinely complex `U(1)` Bargmann holonomy while the Wang shells remain in their canonical real scalar representation and the observation window is real-weighted**. Finite windows may create nonzero cross-shell edges, but their projective cycle phase collapses to a `Z_2` sign invariant.

This does not prove that finite-window shell relations are useless. The cycle sign itself can vary and may contain source-dependent information. It proves only that a continuously varying complex geometric phase cannot be extracted from this real shell geometry without adding a genuinely complex structure whose mathematical/source meaning must be justified separately.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-REAL-BARGMANN-PHASE + REPRESENTATION-BOUNDARY + NO-NOVELTY-CLAIM`.

## 1. Wang's reversed ratios give conjugate Fourier coefficients

For a strict near-band oriented pair `(q,r)`, put

`lambda=log(q/r)`.

Reversing the pair gives `(r,q)`, hence frequency `-lambda`. The reverse pair stays in the same dyadic shell because `max(q,r)` is unchanged, and it stays in the strict near band because `|lambda|` is unchanged. Therefore

`Lambda_M = -Lambda_M`.

The arithmetic prefactor is symmetric and real:

`a_q a_r = a_r a_q`.

Also

`K_H(-lambda)`
` = integral_0^H exp(iu lambda) du`
` = conjugate(K_H(lambda))`.

So

`B_(-lambda)=conjugate(B_lambda)`.

Pairing the `lambda` and `-lambda` terms gives

`B_lambda exp(-i lambda T) + B_(-lambda) exp(i lambda T)`
` = 2 Re(B_lambda exp(-i lambda T))`,

which is real. Summing the finitely many frequencies in a fixed dyadic shell proves

`F_M(T) in R`.

The conclusion is exact and does not depend on a long-window limit, a spacing estimate, or cancellation between different shell frequencies.

## 2. Every real-weighted finite-window Gram matrix is real symmetric

Let `w(T)>=0` be real, integrable, and not identically zero. This includes the sharp interval weight from `VIS-412`, translated intervals, and ordinary real tapers such as smooth compactly supported windows.

Because both shell functions are real,

`conjugate(F_M(T)) F_N(T)=F_M(T)F_N(T) in R`.

Therefore

`G_(MN)^(w) in R`,

and symmetry gives

`G_(NM)^(w)=G_(MN)^(w)`.

The width, center, and detailed shape of the real window may change the magnitude and sign of an overlap, and may create an edge where the Bohr Gram matrix has none. None of those choices can make the overlap intrinsically complex.

This strengthens the representation boundary in `VIS-412`. The sinc formula there shows how finite windows destroy exact Bohr orthogonality. The present result shows that, for the actual Wang scalar shells, this leakage remains inside a real Gram geometry.

## 3. Bargmann holonomy collapses from `U(1)` to `Z_2`

`VIS-411` identifies the gauge-invariant phase information of a complex Gram family with closed-cycle products. For the present real Gram matrix, every factor in such a cycle is real, so

`Delta_C^(w) in R`.

If all cycle edges are nonzero, the only possible phases are

- `0` when the product is positive;
- `pi` when the product is negative.

If any edge vanishes, the product vanishes and its argument is undefined, exactly as in the Bohr-orthogonal case of `VIS-412`.

Thus finite-windowing can change the frame graph from edgeless to connected without restoring a general complex cycle phase. The residual projective phase information is a signed-graph parity: after real vertex sign choices, a negative cycle product is the remaining `Z_2` obstruction.

Allowing arbitrary complex shell rephasings does not change this conclusion. Individual Gram entries can then be made complex, but the Bargmann product is gauge invariant and stays equal to the same real number computed in the canonical real representatives.

## 4. A complex-looking packetization needs an additional source justification

One can manufacture complex shell representatives from the real functions, for example by taking an analytic signal, a one-sided frequency projection, a complex wavelet transform, or another complex packetization. Such a representation can support non-real pairwise overlaps and nontrivial Bargmann phases.

But that would be a **new mathematical ingredient**, not a recovery of phase already hidden in the real finite-window Gram matrix. Under the representation discipline of this line, a complexified visualization is admissible only if the added complex structure has a recoverable source meaning or if the claim is shown to be invariant under the relevant representation choices.

Similarly, using a complex-valued observation kernel changes the sesquilinear structure itself. A phase produced by that kernel must be separated from a phase forced by Wang's arithmetic source before it can be interpreted as an arithmetic relation.

The exact negative statement here therefore applies to the natural class of real scalar Wang shell functions observed through real nonnegative windows/tapers.

## 5. Prior art and novelty boundary

The general Bargmann-invariant and projective-frame theory is already classicalized in `VIS-411`, including Chien--Waldron's finite-frame reconstruction and the geometric-phase literature of Mukunda et al. No new projective invariant theorem is claimed here.

The `0`/`pi` quantization for real-state loops is also standard geometric-phase behavior. Rajeev Singh, Navneet Kumar Karn, Rahul Bhowmick, and Sourin Das, **Topology of quadrupolar Berry phase of a Qutrit**, arXiv `2301.09476` (2023), explicitly discuss the real-state subspace and the resulting zero-or-`pi` geometric phase using Bargmann invariants. The present proof needs only the elementary fact that inner products of real representatives are real.

The Mathia-specific contribution is the source reduction: the reversed prime-power ratios and the conjugation identity for `K_H` force every `VIS-313` Wang shell into that real subspace. Therefore the finite-window route proposed as an escape in `VIS-412` is not a route to a general complex holonomy unless an additional complex representation is introduced.

A targeted prior-art check found the real-state `0`/`pi` phenomenon to be established and found no reason to claim novelty for it. No novelty is claimed for real Gram matrices, signed cycle parity, real projective geometry, or geometric-phase quantization.

## 6. Boundaries and falsification

The result concerns the scalar near-band shell functions inherited from `VIS-313`. It uses the full `+/-lambda` pair in each shell. A deliberately one-sided or otherwise complex packet representation is outside the claim and must be assessed as a new representation.

The weight `w` is real and nonnegative so that it defines the ordinary weighted Hilbert inner product. A real signed weight would still make all displayed overlaps real but need not define a positive inner product. A genuinely complex kernel is outside the claim.

This finding does not show that the finite-window **sign** cycle is universal or uninformative. A stable sign pattern could still become a source-specific relational statistic if it survives window perturbations and matched controls. That is a separate research question rather than evidence supplied here.

Falsify the core claim by exhibiting a `VIS-313` shell frequency whose reverse does not lie in the same shell, a failure of `B_(-lambda)=conjugate(B_lambda)`, a non-real value of a canonical shell function on real `T`, or a non-real weighted Gram entry produced by a real nonnegative window.

## Dependencies

- `VIS-313`: strict near-band Wang ratio shells and their unique oriented cross-base frequencies.
- `VIS-411`: shell-phase gauge and Bargmann cycle invariants.
- `VIS-412`: exact Bohr orthogonality and the finite-window non-orthogonality escape boundary.

## Research consequence

The Wang shell program now has a sharper projective boundary. In canonical Bohr geometry there are no cross-shell edges (`VIS-412`); with ordinary finite real windows the edges may reappear, but all cycle holonomies are restricted to `0` or `pi`.

A next positive phase-sensitive route must therefore either show that the residual `Z_2` cycle signs themselves carry stable arithmetic information, or justify a genuinely complex source-derived packetization whose non-real cycle invariants survive representation and matched-control tests. Merely shrinking, shifting, or smoothly tapering a real observation window cannot create the missing continuous Bargmann phase.