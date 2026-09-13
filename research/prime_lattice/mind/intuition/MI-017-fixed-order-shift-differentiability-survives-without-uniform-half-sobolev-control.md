# MI-017 — Fixed-order shift differentiability survives without a uniform half-Sobolev moment

**Evidence level:** supported by [PL-297](../../findings/PL-297-renormalized-hadamard-stress-hhalf-decoupling.md) and [PL-298](../../findings/PL-298-fixed-order-fractional-shift-autocorrelation-c1.md). The `s->0+` limit for the actual completed-Weil eigenbranch remains open.

PL-297 separates two singular resources in the small-order fractional control. For the interval principal eigenfunction, the renormalized boundary stress has the exact limit

`Gamma(1+s)^2 tau_s^2=(s/R) lambda_(1,s)`, hence `tau_s/sqrt(s)->R^(-1/2)`,

while the zero extensions satisfy

`||E u_s||_(H^(1/2)) -> infinity`.

A finite Hadamard boundary stress therefore does not imply the critical Fourier first moment needed by the routine absolute-differentiation route. Boundary variation and half-Sobolev frequency control are distinct channels.

PL-298 then shows that the missing `H^(1/2)` moment is not needed for fixed positive order. If `u` is compactly supported in `W^(1,1) cap L^infty`, its translation autocorrelation is `C^1` with

`C_u'(h)=int u(x) overline(u'(x+h)) dx`,

and for support `[-1,1]`, both `C_u(+-2)` and `C_u'(+-2)` vanish. Fractional Dirichlet states at every fixed `s>0` have exactly this physical-space regularity because `u~delta^s` and `u'~delta^(s-1)` at the boundary. Prime-power shift terms therefore turn on `C^1` across their activation apertures: the discrete arithmetic source creates no fixed-`s` first-derivative cusp.

The live singularity has moved to **uniform passage as `s->0+`**. One must control the actual regularized completed-Weil branch strongly enough to pass the physical-space shift derivatives and completion/remainder terms to zero order. PL-297 forbids replacing that step by a uniform `H^(1/2)` bound, while PL-298 shows that the fixed-order derivative itself is not the obstruction.

**Boundary.** The `W^(1,1)` constants may deteriorate with `s`; no compactness of the derivative family is proved. These findings concern differentiability of the discrete shift channel and its boundary stress, not the source-specific ground-state sign theorem.