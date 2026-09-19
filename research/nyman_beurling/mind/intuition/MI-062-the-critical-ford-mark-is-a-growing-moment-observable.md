# MI-062 — The critical Ford mark is a growing-moment observable, not a fixed-moment statistic

**Evidence level:** exact positive reduction plus matched-control boundary from [NB-234](../../findings/NB-234-growing-depth-moment-hierarchy-reconstructs-critical-ford-mark.md), building on NB-230--NB-233.

At the carrier-width Ford transition, center depth as `d_rho=YD_rho-log J` and retain the exact profiled coefficient `b_rho=e^{iX(gamma-t)}F(Hv_rho)`. On every fixed layer `|d_rho|<=C`, the residue is `e^{-r} J^(-1) sum e^{-d_rho} b_rho`. Taylor expansion gives

`Z_C = e^{-r} sum_(m<=K) (-1)^m M_m(C)/m! + O_C(C^(K+1)/(K+1)!)`,

where `M_m(C)=J^(-1) sum d_rho^m b_rho`. Thus a hierarchy with `K(Q)->infinity` and uniform `max_(m<=K)|M_m|=o(1)` already controls the exact nonlinear Ford mark. For inverse-logarithmic approximation of the mark, the approximation side needs only very slowly growing order, roughly `log log J / log log log J`.

The necessity of growth is structural for the currently admitted source information. NB-234 embeds finite-difference packets in the same Bellotti-compatible carrier geometry: for every predetermined fixed `K`, all profiled moments through order `K` tend to zero while the exponentially marked residue stays order one. Adding another finite collection of polynomial depth statistics therefore cannot close the transition.

The reusable lesson is that **a nonlinear source mark may be reconstructible from simple statistics only when their resolution grows with the source capacity**. Fixed-order moment control and growing-order reconstruction are qualitatively different information channels. Here the approximation problem is cheap; the source theorem must pay the uniformity needed to control an expanding hierarchy on the exact short window.

**Boundary.** NB-234 is not a theorem that zeta supplies those growing moments. Its positive half is a reduction, and its negative half is a matched spectral control. The profile factor, local window and bounded transition layer are essential; dropping them returns to the projection losses already exposed by NB-231--NB-233. No Nyman--Beurling distance bound or RH consequence follows without a separate destination bridge.