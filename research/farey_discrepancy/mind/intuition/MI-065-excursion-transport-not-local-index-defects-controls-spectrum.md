# MI-065 — Excursion permutation spectra are controlled by cumulative length transport, not local Farey-index defects

**Evidence level:** exact permutation identity and uniform prime-order asymptotic from [FD-319](../../findings/FD-319-four-vanishing-farey-index-defects-carry-macroscopic-energy.md) and [FD-320](../../findings/FD-320-all-prime-farey-excursion-permutations-have-an-exact-transport-spectrum.md).

For prime-order Farey excursions `E_j` of geometric width `1/p` and gap count `ell_j`, set `w_j=ell_j/N_p-1/p`, `U_j=sum_(i<j)w_i`, and `U_t^sigma=sum_(s<t)w_(sigma(s))`. Reassemble any permutation `sigma` while retaining each directed denominator-edge gap. The full rank discrepancy vector satisfies the **exact** transport identity
`D^sigma=P_sigma D+v^sigma` with `||v^sigma||_2^2=T_p(sigma)=sum_t ell_(sigma(t))(U_(sigma(t))-U_t^sigma)^2`.
As the true Farey `||D||_2=o(1)`, uniformly in permutations,
`|sqrt(E_p^sigma)-sqrt(T_p(sigma))|<=sqrt(E_p)=o(1)`.
The discrete sine transform carries the same uniform `l^2` approximation over *all modes*.

The local Hall--Shiu defect count is instead the number of nonconsecutive boundaries in the excursion permutation. FD-319 exhibits a reflection-symmetric permutation with **four** defects, each distance `1/p` from integer index one, but `T_p->3/(4pi^2)`; FD-320 also builds reflection-symmetric permutations with diverging defect counts and `T_p->0`. Neither total index distance nor defect count controls the transported spectral energy in this class.

The exact destination-side condition for asymptotically vanishing energy is `T_p(sigma)->0`, not approximate local index integrality. Nothing here turns an artificial reassembled grid into another canonical Farey sequence or changes the true Farey identity; the gap is whether natural source restrictions enforce small **weighted cumulative** excursion displacement.
