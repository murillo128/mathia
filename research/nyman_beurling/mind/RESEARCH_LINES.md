# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price height adaptation by source-resolvable motion, repertoire and approximate linear complexity

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-046-euler-frequency-support-is-not-source-fidelity-without-amplitudes`.

NB-165--NB-167 isolate the capped Poisson transport metric actually seen by a compact signed sampler near `Re s=1`. NB-168 shows one fixed stationary template cannot produce logarithmic Euler rescue on positive density under the subcritical transport budget. NB-169--NB-171 then price ordered height adaptation by refresh count, total variation and finite `p`-variation measured at that same source resolution.

NB-172 removes temporal regularity entirely: the rescue density is controlled by the internal covering number of the template range in capped Poisson transport. NB-173 gives a different compression when the range lies exactly in a stationary linear span. NB-174 unifies those unordered compressions at the resolution the arithmetic source actually sees through the approximate linear complexity `mathfrak L_T(epsilon)`.

NB-175 supplies a dual nuclear-response lower certificate. NB-176 makes one such witness source-native using the actual Euler frequencies and amplitudes. NB-177 then finds an intrinsic compactness ceiling for that jointly Hilbert-contracting witness: its square-summed Euler spectrum can under-certify the true approximate source complexity even though the primal quantity remains large.

NB-178 separates the witness ceiling from the full coordinatewise dual geometry. If `K` scalar probes are each individually capped-transport contractive, their nuclear response pays an explicit factor `K`; duplication or simple separation does not help, but an `N x N` dense phase code with `sqrt N` singular values can repay the tariff and certify linear complexity.

NB-179 supplies the necessary matched control. Bare capped-Poisson geometry already realizes the maximal phase-code behavior with no arithmetic input. On `2N` Poisson-width-separated points, `N` signed dipoles and explicit scalar Lipschitz probes produce exactly a Sylvester Hadamard response, and the corresponding packed-range complexity is

`mathfrak L^(pack)_(a,q,X)(epsilon)=N(X-epsilon)_+^2`.

For shrinking Poisson width one can take `N asymp_B a^(-1)`. Thus Hadamard-scale coordinatewise response is generic metric coding capacity, not by itself coherent prime-phase evidence.

NB-180 sharpens the falsifier against the most obvious arithmetic repair. Restricting the probes to genuine Euler **frequency support** still does not make the response source-selective if every frequency may be normalized independently. One prime-power tower `p^m` gives the exact progression `m log p`; at explicit widths this produces a DFT code on the same generic dipoles with all singular values on the `sqrt N` scale. Restoring the actual Euler amplitudes `(log p)p^{-m(1+a)}` collapses the nuclear response exponentially. The arithmetic datum is therefore not just where a channel sits in frequency, but how strongly the source exposes it.

NB-181 closes the corresponding bounded-Hilbert escape. With the actual Euler amplitudes retained, any response built from acquisition vectors in the natural feature Hilbert space satisfies a nuclear bound of the form `||A||_* <= X sqrt(NK) G`, where `G` is the RMS Hilbert acquisition norm. Unit-norm probes therefore cannot sustain an `N x N` Hadamard-scale spectrum; doing so forces `G` to grow like `sqrt N`. The genuine Euler scalar readout is not a counterexample: its phase vector is not in `ell^2`, and absolute convergence is supplied by the stronger weighted Dirichlet/`ell^1` structure.

The post-NB-181 target is therefore narrower than “retain Euler amplitudes.” Define a **source-natural acquisition class outside the bounded Hilbert dual** that still carries the actual Euler amplitudes and phases, assign it a finite conditioning/capacity budget, and compare its spectral response with a matched Poisson-packing control under the same budget. A negative theorem could show that every bounded-Hilbert realization is necessarily sub-Hadamard, while any successful arithmetic channel must explicitly pay for the non-Hilbert functional that the Euler product actually uses.

## Keep target conditioning and arithmetic-source persistence separate

NB-168--NB-181 are source-side persistence/resource theorems. NB-177 shows that one canonical square-summed Euler witness can be too compact; NB-178 shows how a larger coordinatewise class could escape; NB-179 shows that this escape architecture is nonselective on generic packing; NB-180 shows that even genuine prime-power Euler frequencies remain nonselective if their exponentially varying source amplitudes are independently normalized away; NB-181 then proves that retaining those amplitudes inside a bounded Hilbert dual imposes a quantitative nuclear ceiling.

None of these results turns a density obstruction into pointwise exclusion at a selected sparse sequence, removes the `a_T\lesssim T^(-1/2)` ultra-thin regime, constructs a source-selective arithmetic phase code at bounded acquisition cost, or by itself connects surviving source response back to global Nyman approximation. The next certificate must therefore carry enough source-resolved complexity in a source-natural **non-Hilbert or otherwise explicitly charged acquisition geometry**, together with a matched-control reason that the complexity is genuinely arithmetic.