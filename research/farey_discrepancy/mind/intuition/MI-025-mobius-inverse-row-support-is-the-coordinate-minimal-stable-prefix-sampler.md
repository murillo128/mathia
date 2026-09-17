# MI-025 — Partial Farey recovery is relative to the observation family

**Evidence level:** exact synthesis from [FD-168](../../findings/FD-168-prefix-mobius-rows-give-coordinate-minimal-stable-partial-farey-sampling.md) and [FD-169](../../findings/FD-169-unrestricted-mixed-measurements-collapse-to-target-rank.md), building on the divisor inversion and complete-field conditioning of FD-117 and FD-167.

For horizon `H` and a target prefix `1<=r<=R<=floor(sqrt H)`, write `k_r=floor(H/r)`. The exact divisor inverse for the cumulative source coordinate `M(r)` uses only Fourier data

`Y_H(d)=1+2 pi i d hat D_H(d)`

at divisors `d|k_r` with `mu(k_r/d)!=0`. Let `S_(H,R)` be the union of those nonzero inverse-row supports.

FD-168 proves that, **when the observation family is restricted to raw positive Fourier coordinates**, `S_(H,R)` is exactly the coordinate-minimal sampler for the prefix, even if the decoder is nonlinear. The same support also carries the complete-field inverse modulus:

`max_(r<=R)|A(r)-M(r)| <= sqrt(30) ||Pi_(H,R) E_H||_2`.

Moreover `R<=|S_(H,R)|<=R H^(o(1))`, so for every fixed `delta>0`, `R<=H^(1/2-delta)` gives `|S_(H,R)|=o(sqrt H)`. Exact algebraic support and stable inverse geometry coincide.

FD-169 identifies the boundary of that statement. Let `T_(H,R)` be the linear target map from the full formal Fourier-skeleton space to the first `R` cumulative source coordinates. It has rank `R`. If the acquisition operator itself may be an arbitrary linear map `L` with any downstream decoder, exact recovery is possible exactly when

`ker L subset ker T_(H,R)`,

or equivalently when the row space of `L` contains the row space of the target. In that case `T_(H,R)=B L` for a linear decoder `B`, regardless of whether the originally proposed decoder was nonlinear. Hence unrestricted mixed measurement complexity is exactly

`m_min=R`,

attained by taking `L=T_(H,R)` itself.

This does not improve the raw sampler. It shows that **measurement count has no representation-independent meaning unless the acquisition family is fixed**. The difference between `|S_(H,R)|` and `R` is the price of insisting that measurements are pre-existing Fourier coordinates. Once the sensor is allowed to implement arbitrary target-aware mixtures, the Möbius inverse can simply be moved into acquisition and the apparent compression problem collapses to output rank.

The reusable audit is therefore two-stage. First specify the admissible observation operators and quotient their kernel against the target. Only then count measurements or study conditioning. For unrestricted linear acquisition the kernel criterion closes the count immediately. Nontrivial continuation requires additional structure: spatial samples or local averages of the Farey field, geometrically local/coarsened operators, horizon-uniform or source-oblivious measurements, positivity/bounded-weight restrictions, a fixed noise normalization, or a genuinely smaller arithmetic source class.

**Boundary.** FD-169 is a theorem about the full formal real source space and unrestricted linear measurements. It does not show that `R` physical Farey observations suffice, does not preserve the FD-168 `sqrt(30)` stability modulus under arbitrary normalization, and does not rule out source-specific nonlinear compression on the actual Möbius class. Exact coefficient recovery remains separate from coercivity of the Franel--Landau destination.