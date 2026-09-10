# MI-003 — Moving-tail adjacency is a certified target-poor nuisance sector

**Evidence level:** exact Rayleigh, closure, Gram-whitened occupation, and orthogonal-complement controls through NB-032

## Core intuition

Small Gram energy is useful only after target occupation is measured in the same Hilbert geometry. The full adjacent-difference family remains too large to quotient because it spans the entire Nyman closure, but its **moving-tail** portion is genuinely different: after Gram whitening it becomes target-poor, and removing it preserves the full target distance asymptotically.

This turns a previous negative warning into a positive separator. Nuisance structure can be removed safely when target poverty is established in the correct metric and the resulting quotient is checked against the actual approximation distance.

## Strongest justified principle

NB-024--NB-026 show that low-Rayleigh directions are plentiful and can be target-poor. NB-027 finds real Möbius-locked coefficient geometry, while NB-028--NB-029 show that quotienting all adjacent differences destroys the target-bearing closure because those differences topologically generate the whole canonical dictionary.

NB-030 demonstrates why raw coefficient loading cannot repair this: low normalized Gram energy and large Euclidean target coefficients can coexist with nearly maximal Gram-whitened target alignment. NB-031 then proves that adjacent sectors translated sufficiently far into the tail are genuinely target-poor after whitening. NB-032 completes the quotient audit by showing that the orthogonal complement of the moving-tail adjacent sector retains the full target distance asymptotically.

## Program consequence

Use the moving-tail sector as the canonical nuisance control. Measure what remains in its orthogonal complement and ask whether Möbius locking or the canonical coefficient law forces a quantitatively distinguished head/source component there. A useful extension would enlarge the certified target-poor sector across scales while proving, in the same Gram geometry, that the Nyman distance is preserved.

Do not use raw coefficient loading or unrestricted adjacent spans as substitutes for this audit.

## Counterevidence / boundary

NB-031--NB-032 do not show that every low-Rayleigh adjacent combination is target-poor, nor that the certified moving-tail quotient alone exposes an arithmetic lower bound. The surviving orthogonal complement may still contain universal low-energy structure. Möbius coefficient separation has not yet been converted into a quantitative Gram spectral occupation theorem.

## Epistemic status

**Exact positive boundary: moving-tail adjacent differences form a Gram-whitened target-poor nuisance sector whose removal preserves the Nyman target distance, while the unrestricted adjacent family remains non-quotientable.**

## Falsification criterion

Show that the NB-031 moving-tail sector has nonvanishing Gram-whitened target occupation in the stated regime, or that projecting it away changes the asymptotic target distance contrary to NB-032.
