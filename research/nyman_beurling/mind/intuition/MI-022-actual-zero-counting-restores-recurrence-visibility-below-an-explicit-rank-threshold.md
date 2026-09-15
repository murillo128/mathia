# MI-022 — Actual zero counting can restore recurrence visibility below an explicit rank threshold

**Evidence level:** source-specific derived consequence of explicit zeta zero counting, functional-equation symmetry and the existing recurrence certificate from [NB-132](../../findings/NB-132-explicit-zero-counting-restores-recurrence-visibility-for-narrow-polynomial-height-packets.md)

The formal interpolation obstruction of NB-130--NB-131 depends on allowing the packet rank to grow as fast as the observed natural prefix. Genuine off-critical zeta zeros cannot realize that rank inside every narrow polynomial-height ordinate band.

Let `F` be a packet of genuine zeros with `Re rho>1/2`, positive ordinates in `(T,T+W]`, true multiplicities, and `T+W<=R^A`. Functional-equation symmetry pairs each right-half zero with a distinct left-half zero at the same ordinate. Combining this with the explicit zero-counting error gives

`d(F) <= A(W/(4 pi)+0.10076) log R + 0.24460 log log R + O_(A,W)(1)`.

The `q`-geometric recurrence of a confluent packet of rank `d` becomes visible inside the natural cutoff once `R>=q^(d+1)`, equivalently `d+1<=log_q R`. Therefore, whenever

`A(W/(4 pi)+0.10076) < 1/log q`,

the actual-zero packet eventually lies below the recurrence-visibility threshold. The annihilator from NB-124 is then an admissible dual certificate and gives a strict packet-specific target-angle gap.

This is a genuine source separator. NB-130 can place rank `R` formal zero powers in an arbitrarily narrow band at arbitrarily high ordinate and interpolate the whole prefix; NB-132 proves that genuine zeta zeros in the stated polynomial-height/narrow-band regime can supply only logarithmic confluent rank, with a coefficient small enough that the hidden recurrence becomes observable.

The gain is qualitative rather than yet Burnol-scale quantitative. Visibility of the recurrence does not control the ratio between the missing-root margin and the weighted annihilator coefficient norm as the packet changes with `R`. That conditioning can still collapse. Likewise the argument does not cover superpolynomial heights or ordinate widths large enough to consume the recurrence budget.

The reusable distinction is therefore **rank visibility versus quantitative coercivity**. Source-specific counting can invalidate a formal high-rank interpolation control without yet providing the uniform target margin needed by the final Nyman--Beurling estimate.
