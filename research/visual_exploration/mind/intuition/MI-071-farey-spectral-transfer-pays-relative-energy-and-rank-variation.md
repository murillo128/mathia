# MI-071 — Farey spectral transfer pays relative energy and rank variation separately

**Evidence level:** supported by the exact normalized-spectrum inequality of [VIS-447](../../findings/VIS-447-uniform-normalized-farey-transport-spectrum.md) and the capped variation bound of [VIS-465](../../findings/VIS-465-capped-variation-tariff-for-farey-transport-spectrum.md), applied to [FD-320](../../../farey_discrepancy/findings/FD-320-all-prime-farey-excursion-permutations-have-an-exact-transport-spectrum.md). These are classical finite-dimensional/Fourier mechanisms specialized to labeled excursion controls, not new arithmetic cancellation.

Fix a prime `p>=7`, `N=N_p=sum_(q<=p) phi(q)`, and a whole-excursion permutation `sigma`. The genuine Farey discrepancy `D` and reassembled discrepancy `y` obey

`y=P_sigma D+v`, `E=||D||_2^2=o(1)`, `T=||v||_2^2`.

Assume `T>0` and `y!=0`. For the orthonormal Dirichlet sine transform, put `pi_m(z)=|zhat_m|^2/||z||_2^2` and `F_J(z)=sum_(m in J) pi_m(z)`. The absolute vector error transports **every** normalized mode subset with no dimension loss:

`sup_J |F_J(y)-F_J(v)| = (1/2) sum_m |pi_m(y)-pi_m(v)| <= min(1,sqrt(E/T))`.

The denominator is essential: `E=o(1)` and `T=o(1)` alone do not identify the normalized spectrum. For a fixed comparator with its own expected fraction `f_null(J)>0`, the error in `S_J=F_J/f_null(J)` is at most `min(1,sqrt(E/T))/f_null(J)`. Thus even `E=o(T)` may be insufficient for a vanishing null fraction; `sqrt(E/T)=o(f_null(J))` suffices.

Extend `v` by `v_0=v_N=0`. Set

`V=sum_(j=1)^N |v_j-v_(j-1)|`, `R=N V^2/T`,

`B_q=V^2/(2NT) sum_(m=q+1)^(N-1) csc^2(pi m/(2N))`, `1<=q<N`.

Abel summation gives the tail majorant and Parseval gives its independent probability cap:

`1-F_{1,...,q}(v) <= min(1,B_q) <= min(1,R/(2q))`.

The cap applies to the bound on the tail; the uncapped majorant can exceed one. For `N=3`, `v=(1,-1)`, `q=1`, the tail is one while `B_q=16/9`. Combining the two mechanisms yields

`1-F_{1,...,q}(y) <= min(1,R/(2q)) + min(1,sqrt(E/T))`.

In particular `E/T->0` and `R=o(q_p)` suffice for low-band share tending to one. Conversely, if that share is at most `1-eta` and `sqrt(E/T)<eta`, then `R>=2q(eta-sqrt(E/T))`. Large roughness is necessary for transport-dominated depletion; it is not sufficient.

The roughness is computable without the within-excursion grid. With positive gap counts `ell_j`, `w_j=ell_j/N-1/p`, `U_j=sum_(i<j)w_i`, and `c_t=U_(sigma(t))-sum_(s<t)w_(sigma(s))`,

`T=sum_(t=1)^(p-2) ell_(sigma(t)) c_t^2`,

`V=|c_1|+sum_(t=1)^(p-3)|c_(t+1)-c_t|+|c_(p-2)|`.

Thus the controlling quantity is the size of cumulative displacement jumps relative to their weighted energy, not the count or near-integrality of Hall–Shiu defects. In VIS-465's reflected four-defect control, `R->16` and `T->3/(4pi^2)>0`, so every divergent full-mode cutoff captures asymptotically all normalized energy. Reflection kills odd sine modes: the first `q` even modes mean full cutoff `2q` and replace `R/(2q)` by `R/(4q)`. Unreflected controls require the full basis.

This is a one-sided criterion on artificial labeled-edge reassemblies. Genuine Farey order has `T=0`, outside the normalized transport comparison. Neither exact recovery of a reassembly nor bounded transport roughness proves suppression in the genuine Farey spectrum; a source-natural comparator still needs its own band normalization.
