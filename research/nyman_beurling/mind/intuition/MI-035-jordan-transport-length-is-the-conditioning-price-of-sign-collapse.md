# MI-035 — Jordan transport length is the conditioning price of sign collapse

**Evidence level:** exact synthesis from [NB-160](../../findings/NB-160-continuous-separated-jordan-samplers-still-export-an-adverse-zero-reservoir.md) and [NB-161](../../findings/NB-161-collapsing-jordan-transport-forces-conditioning-blowup.md), using only the elementary Lipschitz/coupling estimate for the exterior Poisson kernel.

After zero total mass removes the universal Hadamard background, opposite signs cannot be made arbitrarily close at bounded cost. For a zero-mass signed height measure `nu=nu^+-nu^-`, let `M=nu^+(R)=nu^-(R)`, `V=||nu||_TV=2M`, and define the mean optimal Jordan transport length

`ell(nu)=W_1(nu^+,nu^-)/M`.

At fixed horizontal offset `x in [a,a+1]`, the exterior Poisson kernel is Lipschitz in sampling height with constant at most `9/(8 sqrt(3) a^2)`. Coupling the two Jordan measures therefore gives the exact uniform bound

`|Q_nu(x,gamma)| <= (9/(16 sqrt(3) a^2)) V ell(nu)`.

If a sampler family has distinguished target scale `c_G`, conditioning `C_G=V_G/c_G`, and target response at least `q c_G`, then necessarily

`C_G ell(nu_G) >= (16 sqrt(3)/9) q a^2`.

Thus a coupling of opposite signs across a scale `epsilon_G->0` forces `C_G=Omega(1/epsilon_G)` whenever fixed target gain is retained. Fine signed cancellation is not a free nuisance quotient: its geometric cancellation scale and total-variation conditioning are reciprocal resources.

Combined with NB-160, this localizes the unresolved signed geometry. Large fixed Jordan-support separation gives an `Omega(log G)` adverse-zero reservoir; genuine transport collapse gives vanishing normalized target response under bounded conditioning. What remains is neither separated nor collapsed: the supports may interlace on `O(1)` Poisson widths, but their mass distributions must retain order-one optimal transport length. Minimum support distance alone does not distinguish this regime.

The next useful theorem must therefore analyze **fixed-width interlacing with noncollapsed transport**. It should decide whether the same local zero population can see positive and negative mass strongly enough to cancel the adverse reservoir while preserving bounded conditioning and order-one target gain, or whether a new target-conditioned occupancy/transport inequality closes that window.

**Boundary.** The transport estimate does not rule out order-one `ell(nu_G)` with densely overlapping supports, and it permits `ell(nu_G)->0` when conditioning grows at the reciprocal rate. It uses no zero-counting theorem and does not itself imply an adverse zero reservoir. Its content is the exact price of the collapse escape left open by NB-160.
