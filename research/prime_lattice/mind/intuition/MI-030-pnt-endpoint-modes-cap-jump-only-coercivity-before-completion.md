# MI-030 — The raw PNT edge is essential and rare, but canonical pole centering removes its bounded-frequency recurrence

**Evidence level:** exact synthesis from [PL-339](../../findings/PL-339-outer-source-shell-carries-unit-gap-coercivity.md), [PL-340](../../findings/PL-340-pnt-endpoint-jump-coercivity-ceiling.md), [PL-341](../../findings/PL-341-sharp-pnt-prime-block-half-mass-spectrum.md), [PL-342](../../findings/PL-342-sharp-prime-block-essential-spectrum.md), [PL-343](../../findings/PL-343-haar-rarity-of-recurrent-prime-edge.md), and [PL-344](../../findings/PL-344-bounded-modulation-pnt-edge-cancelled-by-pole.md), using the endpoint modes constructed in PL-051. The conclusion concerns the PNT-universal bounded prime profile and its canonical pole cancellation; it does not determine the centered residual or the spectrum of the full completed Weil operator.

PL-339--PL-341 determine the bounded PNT geometry. With `W_a=2e^a(1+o(1))`, the weighted compressed-shift sum has asymptotic spectral edges `+/-e^a`. PL-342 shows that those edges are already essential: high common modulations combined with Kronecker recurrence reproduce the endpoint Rayleigh values on weakly-null sequences. Finite-rank correction and bounded compact completion therefore cannot remove the sharp bounded edge by compactness alone.

PL-343 then shows that the same raw recurrence witnesses are extremely sparse. For the exact weighted endpoint phase observable `H_a`,

`mu_a{|H_a| >= eta e^a} <= 2 exp[-(eta^2/8+o(1)) e^(2a)/a]`.

Finite rational independence makes the physical prime-log orbit uniquely ergodic, so the same quantity controls long-time density for each fixed `a`. Raw edge recurrence is therefore topologically sufficient for essential spectrum yet exponentially rare in prevalence.

PL-344 demonstrates that prevalence still does not price the first hit. The endpoint weight has an explicit bounded-modulation PNT response

`F_a(tau)= [e^a/(1-e^-a)] * e^(2ia tau)/(1+i tau)^2 + o_T(e^a)`.

For any fixed `tau_0`, a phase-aligned `tau_a=tau_0+O(1/a)` gives

`H_a(tau_a)= +/- e^a/(1+tau_0^2)+o(e^a)`.

Thus edge-sized raw responses occur at uniformly bounded modulation even though their long-time density is exponentially small. This is a concrete warning that **existence, prevalence and first-hit time are different recurrence currencies**.

But the completed problem has an additional, decisive layer. The canonical zeta-pole quadratic form carries exactly the same leading bounded-frequency PNT profile with the opposite sign, so

`Q_pole(M_tau u_a^+) - H_a(tau)=o_T(e^a)`

through that regime. The surprisingly early raw recurrence is therefore a universal background effect removed by the canonical completion rather than a surviving completed instability.

The live quantity is the **centered arithmetic residual** after subtracting the PNT/pole profile. Any first-hit or recurrence theorem relevant to completed coercivity must be stated for that residual and compared, on the same state, with the unbounded logarithmic principal cost. A theorem about raw `H_a` alone can no longer settle the completed sign question, whether it gives recurrence existence, rarity or an early hit.

The matched-control warning is correspondingly stronger. PL-343 and PL-344 use PNT mass, rational independence and the canonical pole response, so their phenomena are reproduced by suitable generalized-prime controls. RH-facing information must enter through the rational-prime-specific centered remainder, a source-selected branch theorem for that remainder, or another nonuniversal coupling surviving completion.

**Boundary.** PL-344 does not prove that the centered residual is small, recurrent, nonrecurrent or coercive, and it gives no completed negative direction. It only identifies and cancels the leading bounded-frequency PNT profile. The remaining theorem must control the destination-surviving residual together with the unbounded principal term.