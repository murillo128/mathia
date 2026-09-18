# MI-056 — Bounded shell signals make zero mean and support width explicit Mellin currencies

**Evidence level:** exact synthesis from [NB-215](../../findings/NB-215-signed-fixed-shell-preconditioning-can-only-export-the-mellin-tariff.md) and [NB-216](../../findings/NB-216-bounded-shell-signals-price-zero-mean-and-growing-width-escapes.md).

The absolute Mellin reconstruction tariff is not tied to a nonzero mean. Let `h` be supported on a logarithmic shell `[0,Delta]`, let `psi` be any bounded reference pattern with `||psi||_infinity<=1`, and let

`M_psi(h)=int_0^Delta psi(y)h(y)dy`.

After `j>=1` ordinary Mellin primitive transfers, with

`K_(X,j)(v)=int_0^Delta (X+y)^j h(y)e^(ivy)dy`,

NB-216 proves

`||K_(X,j)||_1/|M_psi(h)| >= 2pi/I_j(X,Delta)`,

where `I_j(X,Delta)=int_0^Delta (X+y)^(-j)dy`. This is a source-normalized Fourier-dual obstruction: signs, phases and the detailed shell shape do not matter once the destination-visible source coordinate is a bounded shell pairing.

For one primitive, `I_1=log(1+Delta/X)`. A growing shell can therefore dilute the tariff, but only by paying in actual logarithmic support width. Reaching subpolynomial cost on the Vinogradov--Korobov diagonal requires `Delta >= X Q^(-o(1))`, and bounded cost requires `Delta=Omega(X)`. In physical coordinates that abandons the original fixed multiplicative neighbourhood. For `j>=2`, the reciprocal multiplier is integrable and widening cannot remove the residual lower bound `Omega(X^(j-1))`.

Zero mean is therefore not itself an escape. If the replacement signal is any normalized bounded higher moment, for example `psi_r(y)=(y/Delta)^r`, the same inequality applies. The only way a zero-mean construction evades this theorem is by changing the source functional class itself: a distributional/derivative signal or another functional whose natural norm grows with `X` or `Delta` must explicitly pay that stronger normalization.

The reusable lesson is that **mean cancellation and shell widening are currencies, not free representation changes**. Once the source signal is normalized, the inverse Mellin multiplier prices how much support width or functional norm is needed to make absolute reconstruction cheap. After one primitive there is a genuine locality-versus-cost tradeoff; after two or more primitives the tradeoff saturates.

For Nyman--Beurling the live escape is now narrower than the boundary of NB-215. A new asymptotic class must exploit correlation with the actual zeta primitive before absolute values, identify a destination-visible source functional genuinely outside bounded shell duality and price its norm, or change support geometry so substantially that it is a different observable.

**Boundary.** The theorem is a global `L1` reconstruction bound, not a lower bound for the true oscillatory zeta integral. It does not supply a central-neighbourhood export theorem for every bounded `psi`, and it does not prove that a near-optimal Nyman approximant realizes any particular shell signal. Destination coupling remains a separate load-bearing theorem.