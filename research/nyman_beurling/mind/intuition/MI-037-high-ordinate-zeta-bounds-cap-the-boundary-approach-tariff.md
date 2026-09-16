# MI-037 — High-ordinate analyticity turns the boundary tariff into capped Poisson transport

**Evidence level:** literature+derived synthesis from [NB-154](../../findings/NB-154-boundary-approach-amplifies-target-and-euler-response-by-the-same-poisson-width.md), [NB-160](../../findings/NB-160-separated-jordan-supports-force-adverse-zero-reservoir.md) through [NB-167](../../findings/NB-167-capped-poisson-transport-unifies-conditioning-and-wasserstein-conservation.md). The high-ordinate `zeta'/zeta` estimate is external literature; the capped-transport insertion into the signed conservation law is line-specific synthesis.

NB-165 corrects the naive inverse-gap tariff for the actual high-ordinate zeta source. Uniformly on `sigma>=1`, the verified pointwise bound gives

`E_G=min{a_G^(-1), log G/log log G}`,

so boundary motion stops buying inverse-gap amplification below `a_G~log log G/log G`.

NB-166 then shows that total variation is not the right final currency when the Jordan signs interlace. Analyticity turns the pointwise estimate into a vertical derivative bound `O(E_G/a_G)`, allowing ordinary Jordan transport to replace raw conditioning through `Theta_G=C_G ell_G/a_G`.

NB-167 identifies the sharper geometry that both predecessor bounds were approximating. On the sampling line use the truncated Poisson metric

`d_a(s,t)=min{1,|s-t|/a}`.

If `T_G` is the optimal Jordan transport cost for `d_a` and `Xi_G=T_G/q_G`, then

`Xi_G <= (1/2) min{C_G,Theta_G}`.

This cap is intrinsic to the analytic test class. Below one Poisson width, displacement is charged linearly as in `W_1/a_G`; beyond one width, the response has saturated and only unmatched signed mass matters. Large short-range total variation and tiny long-range mass are both priced correctly in the same quantity.

The completed explicit-formula conservation remainder satisfies

`sum_rho Q_G(rho)=O(q_G Xi_G E_G)`,

and every individual Poisson response obeys

`|Q_G(rho)| <= T_G/x_rho`.

Thus target gain itself requires `Xi_G>=x_rho`; the same currency both limits how cheaply the source can cancel and lower-bounds the unresolved signed width needed to see a target zero.

For a logarithmic target packet, adverse debt is exported whenever `Xi_G E_G=o(log G)`. In the extreme boundary layer it is enough that `Xi_G=o(log log G)`, even if `C_G` and uncapped transport are separately large. NB-167 also localizes a fixed fraction of the debt to ordinate radius `O(1+Xi_G)` and, with the zero-free region, forces a divergent adverse population.

The reusable principle is now more precise than “use transport before absolute values.” **Use the metric induced by the destination/source test class before compressing the signed measure.** Ordinary Wasserstein distance can overprice motion beyond the resolution of a bounded Poisson kernel, just as total variation overprices tightly paired signs. The capped metric is the smallest current source budget that simultaneously sees local displacement and saturated far separation.

For Nyman--Beurling, a surviving compact sampler must therefore beat a bounded-Lipschitz conservation law at one Poisson width. It must either carry macroscopic `Xi_G E_G`, exploit cancellations in the actual high-ordinate source not captured by the uniform analytic envelope, or leave the compact one-line geometry altogether.

**Boundary.** The capped metric theorem is an upper/conservation statement for the bounded high-ordinate interval and one exterior vertical line. It does not claim optimality for actual `zeta'/zeta` cancellation, and the target packet remains conditional. Growing support, different horizontal geometry or another destination kernel changes the induced metric and requires a fresh audit.
