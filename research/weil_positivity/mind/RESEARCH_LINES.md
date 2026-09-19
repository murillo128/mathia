# Weil-positivity research lines

This file holds the current mathematical questions suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-forced mixed-prime sign mechanism beyond universal positive completion

**Linked intuitions:** `MI-039-enriched-semigroups-inherit-obstructed-scalar-shadows-or-universal-lifts` through `MI-055-centered-prime-power-toeplitz-positivity-pays-a-divergent-diagonal-tax`.

WP-356--WP-370 classify the finite Hecke, finite--archimedean and componentwise Whittaker scale routes. Genuine arithmetic incidence survives in nonconstant finite modes, but canonical positive squares scalarize critical half-density; common homogeneous globalization separates variables; the unique critical power scale freezes `nY`; exact diagonal Hecke equivariance forces that same ray; and ordinary positive boundary `L^2` squares the desired amplitude.

WP-371 isolates the prime-power Toeplitz carrier. The desired nonzero Fourier coefficients are exactly those of the centered Poisson kernel, but the centered kernel is indefinite. If each prime ray is completed independently by a scalar diagonal, positivity requires at least

`2 log p/(sqrt(p)+1)`

at prime `p`, and summing these local taxes diverges.

WP-372 shows that this divergence is **not** a global scalar positivity obstruction once arbitrary mixed-prime coefficients are allowed. On the prime torus, a positive measure with the prescribed positive-sign one-prime rays exists iff its total mass satisfies

`C >= C_+^* = sup_p 2 log p/(sqrt(p)+1)`,

and the sharp supremum is finite (attained at `p=13`). An explicit product completion realizes the mixed coefficients. By contrast, requiring all mixed-prime coefficients to vanish keeps the old sum tax, and the same divergent threshold persists if the sparse carrier is first restricted to the common prime-log translation line, because that line is dense in every finite prime torus.

Thus the `WP-371` obstruction was a **sparsity/separability tax**, not the price of positivity itself. But the mixed-prime escape produced by WP-372 is also a matched control: its product interactions are universal for freely generated prime coordinates, are engineered from the target moments, and supply no Gamma/archimedean orientation or zero data. The live question is therefore more specific than “couple primes before positivity.” One needs a **source-forced mixed-prime coupling** whose coefficients are not freely selectable, whose positive completion remains finite, and whose orientation is independently tied to the Weil sign rather than inherited from a universal product measure.

## Keep arithmetic content, positivity and mixed-prime completion distinct

The current audit distinguishes finite Hecke incidence, critical half-density, diagonal Hilbert squaring, prime-power Toeplitz coupling, zero-mode completion cost, mixed-prime Fourier freedom, sparse versus dense prime support and sign coercivity.

WP-372 adds a decisive diagnostic. A local divergence may disappear completely when the global completion is allowed to create mixed coordinates, so one must solve the **global** positive-definite extension problem before declaring a local diagonal tax fundamental. Conversely, the existence of a finite global positive extension is not arithmetic leverage when the extension is universal and unconstrained by the source.

Any next proposal should state which mixed-prime coefficients are actually forced by the finite/archimedean arithmetic construction, whether those constraints still admit a finite positive completion, how the archimedean sector fixes orientation, and why the resulting sign is not reproduced by the WP-372 product control. Independent local Poisson blocks are too sparse; an arbitrary product completion is too free. The relevant theorem surface lies between those two extremes.
