# Prime-flute mathematical questions

## Prove defect-scale source avoidance after low screening

**Linked intuitions:** `MI-008-complete-cut-transmission-needs-extension-mass-not-only-boundary-impedance`, `MI-009-bidirectional-scalar-survival-is-killed-by-accumulated-pant-loss`, `MI-010-scalar-green-response-is-killing-normalized-markov-averaging`.

PF-303--PF-308 close scalar depth, global-angle control, and full killing-normalized constant-sector boundedness as missing mechanisms. PF-309--PF-311 show that the explicit reservoir is genuinely physical-low and that direct residual high conversion is already small after low screening. PF-312 then proves that inversion creates no second normalized angle: the diagonal-normalized mixed Green block has exactly the singular values of the post-low angle `T_H`.

PF-313 turns the remaining diagonal-strength problem into an exact source criterion. If the post-low block is `[[S,E],[E*,R]]>0`, `T=S^(-1/2)ER^(-1/2)`, and `F_C=S-ER^(-1)E*`, then

`||G_C^(1/2) J_C||^2 = sup_(x!=0) ||J_C* x||^2/<x,F_C x>`

and uniform boundedness is equivalent to

`J_C J_C* <= K^2 F_C`,

or, after whitening, `Jhat_C Jhat_C* <= K^2(I-TT*)`.

Hence on a singular direction with value `sigma`, every uniformly controlled physical source must vanish at least like `sqrt(1-sigma^2)` in the corresponding near-unit left singular direction. The symmetric criterion holds on the high/reassembly side. Diagonal Green control is therefore exactly **defect-scale source avoidance**, not another inverse estimate.

PF-313 also gives an explicit audit on the PF-308 screened traces: any source family with bounded source-weighted Green strength must have normalized overlap with those traces tending to zero at the fully-shorted-energy rate. If the actual physical source retains order-one overlap along such a subsequence, the diagonal Green factor necessarily diverges.

The live theorem is now concrete: identify the actual physical `J_C,J_H` and prove the corresponding defect-scale domination on source-reached near-unit `T_H` directions, or show that angle/multiplicity/ideal decay or signed reassembly compensates when one of the diagonal strengths diverges. A return-potential theorem matters only insofar as it proves this domination.

## Global heavy-range projection counts after strength/angle factorization

For the PF-287 heavy low/high extension-range projection product, can the source-reached post-low singular directions have vanishing essential norm or the required singular-value counting law once PF-313's exact defect-scale source factors are separated from the unchanged `T_H` angle? The burden is localized in source-weighted diagonal strength, normalized angle, signed reassembly, and multiplicity—not scalar return depth, a new inverse angle, physical-high entrance leakage, or absolute first residual conversion.

## Prime realization within the resolved upstream-memory window

Can consecutive prime-gap isolation realize the moderate graded neck ratios of MI-001, or can the surface-to-graph error be sharpened enough to resolve `w_j^2/w_(j-1)` in the hierarchies already known to occur? Arbitrarily strong separation is not the required condition: the correction must still dominate `w_j sqrt(w_1)`.

The fixed-axis `q>1` Robin leakage route is excluded by MI-007, not an outstanding estimate. Generic conservative `L1` rigidity is excluded by MI-005; a construction matching only the particular canonical germ is a different claim.
