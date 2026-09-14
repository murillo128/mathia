# MI-018 — Actual zero-power packets have a stable annihilator gap; near-perfect capture must spend rank or horizontal depth

**Evidence level:** exact consequence of [NB-123](../../findings/NB-123-perfect-target-capture-by-a-finite-zero-packet-requires-logarithmic-confluent-rank.md) and [NB-124](../../findings/NB-124-weighted-annihilator-duality-gives-a-stable-target-angle-gap-for-finite-zero-packets.md), using the target equality/energy characterization of NB-117 and the elementary annihilating recurrence of finite confluent exponential-polynomial sequences. No RH consequence or uniform growing-rank zero-packet bound is claimed.

The matched controls of NB-119--NB-122 show that increasingly rich Nyman orthogonality and even the entire nested cutoff prefix do not exclude perfect visible target capture. NB-123 identifies the first exact separator coming from the **actual zero-power representation itself**.

For a finite packet `F` of actual nontrivial zeta zeros, let `d(F)` be its total confluent multiplicity. Sampling its primitive on a geometric grid `n=q^k` gives a finite exponential-polynomial sequence with characteristic roots `q^(-conj(rho))`. Perfect target capture forces its geometric block increments to be the pure missing mode `q^-k`, but every actual nontrivial zero has `Re rho<1`, so `q^-1` is not a characteristic root. NB-123 therefore gives `d(F)>=floor(log_q R)` for exact capture.

NB-124 makes this separator stable without reconstructing the packet parameters. Let

`A_(F,q)(z)=sum_(j=0)^d a_j z^j`

be the annihilator and define

`mathfrak s_(F,q)=(1-q^-1)|A_(F,q)(q^-1)|^2 / sum_(j=0)^d |a_j|^2 q^-j`.

The margin is strictly positive for every fixed actual finite packet. The annihilator applied to the first geometric block errors is an exact scalar functional whose right-hand side is proportional to `A_(F,q)(q^-1)`. Cauchy--Schwarz in the reciprocal block weights of the Nyman cell energy then gives, once `R>=q^(d+1)`,

`chi_(F,R) <= (1+mathfrak s_(F,q)/L_R)^-1 <= 1/(1+mathfrak s_(F,q)) < 1`.

Thus **every fixed finite actual zero packet is uniformly separated from perfect target capture** for all sufficiently large cutoffs. Node collisions may make Prony parameter recovery ill-conditioned, but they do not by themselves destroy this target-angle certificate because no parameter inversion is used.

There is also a coarse source-only lower bound. If `beta_F=max_(rho in F) Re rho`, then

`mathfrak s_(F,q) >= (1-q^-1)((q^-beta_F-q^-1)/(1+q^-1/2))^(2d)`.

Consequently, in any fixed strip `beta_F<=1-sigma`, polynomially near-perfect capture `chi_(F,R)>=1-R^-alpha` forces `d(F)>=c_(q,sigma,alpha) log R-O(1)`. The exact equality separator of NB-123 therefore extends to a quantitative near-perfect separator as long as horizontal approach to `Re s=1` is controlled.

The remaining degeneration has a concrete source geometry. The normalized missing-root margin can shrink because the confluent rank grows and/or because packet zeros move horizontally toward `Re s=1`, bringing the sampled zero radii toward `q^-1`. Fine phase separation may improve the crude bound, but generic Prony instability is no longer the identified obstacle.

The next theorem should therefore control `mathfrak s_(F,q)` for the actual endpoint-relevant zero packets, combine it with NB-116's height/horizontal-mass restrictions, or prove that any family with enough target access pays a rank/height/horizontal-depth cost incompatible with the continuum norm budget. Another nested source equation cannot substitute for that bound.

**Boundary.** NB-124 gives a uniform gap only for each fixed finite packet and a logarithmic rank consequence inside a fixed horizontal strip. It does not control arbitrary growing-rank packets whose rightmost zeros approach `Re s=1`, nor does it turn the finite-packet gap into an RH theorem. The durable resource is the annihilator margin in the same weighted geometry as the destination, not recurrence rank or zero separation alone.