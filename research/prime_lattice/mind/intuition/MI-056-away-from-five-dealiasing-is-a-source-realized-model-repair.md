# MI-056 — Away-from-five de-aliasing is a source-realized model repair

**Evidence level:** exact model/source synthesis from [PL-412](../../findings/PL-412-prime-5-dealiasing-rh-analyticity.md) and [PL-413](../../findings/PL-413-away-from-p-singular-series-endpoint-conditioning.md), refining the cancellation caveat in PL-411.

A zeta denominator in a continued model does not by itself certify a zero detector. PL-412 audits the remaining Euler factors of the PL-411 endpoint Mellin transform and finds a unique RH-relevant local alias: among odd primes, only the `p=5` factor can vanish at a transformed zero with `1/2<Re(rho)<1`. Deleting that one Bernoulli coordinate removes the local ambiguity; a functional-equation descent then prevents numerator cancellation from persisting indefinitely.

For the conditioned endpoint law this gives an exact model statement:

`RH iff N_5(s)-2/(5(s+1)) is holomorphic in Re(s)>-7/4`.

The finite-prime deletion is not merely post hoc. PL-413 proves that restricting the original singular-series/Ramanujan source to denominators coprime to `p` transports exactly to conditioning the endpoint law on `p` not dividing `M`. For `p=5`, the repaired Mellin model is therefore the endpoint image of the standard source operation “singular series away from 5”.

This gives a reusable two-gate audit for model analyticity criteria. First audit every numerator and local Euler factor at the candidate pole; then require any de-aliasing used to restore the criterion to have a source-side meaning before treating it as arithmetic evidence. Here both gates can be passed exactly, but the actual-prime transfer remains absent.

**Boundary.** The criterion lives on the singular-series endpoint model. PL-413 identifies a canonical source observable that realizes the conditioning, but it does not prove that actual prime-pair statistics track that observable with the required signed and uniform error. The result therefore repairs provenance inside the model/source chain without supplying an RH proof.