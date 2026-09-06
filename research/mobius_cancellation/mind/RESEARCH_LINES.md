# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Treat direct radial truncation, diagonal shell norms, and first-order local filtering as classified

**Linked intuitions:** `MI-011-source-forced-prime-deformation-is-a-polynomial-information-channel` and `MI-012-hamming-regularization-is-degree-two-damping-before-the-square-root-transition`.

MC-107--MC-109 carry the exact Hamming shell profile through every fixed proportional Sathe--Selberg scale and the critical turning window near `2 log log N`. The shell coefficients remain positive; alternating prefixes through the turning regime stay comparable to their boundary shell, so the tiny Möbius endpoint is not exposed by stopping at the natural shell peak.

MC-110 closes every certificate that takes positive diagonal shell magnitudes before reconstruction: the central shell energy is `N^{2-o(1)}` and arbitrary diagonal Hölder weights cannot hide it. MC-111 closes the first non-diagonal repair as well. Any fixed finite local filter that carries parity and has at most a simple zero at the flat-shell frequency `z=1` still leaves `N^{2-o(1)}` filtered coefficients; absoluteizing afterward merely moves the cancellation problem.

The first unresolved fixed local filters therefore have at least a double zero at `z=1` while retaining `A(-1) != 0`. More generally, a survivor may use growing-order/`N`-dependent filters, a genuinely nonlocal signed recurrence, or a non-radial source relation. The relevant distinction is whether cancellation **between degrees is preserved before absoluteization**.

## Derive a signed relation that carries parity across the full critical shell profile

The exact endpoint is an alternating evaluation at the parity frequency `z=-1`, while the positive shell bulk is concentrated around the Sathe--Selberg scale `k~2 log log N`. A useful radial theorem must connect those two facts without reducing to a finite derivative of the locally smooth positive profile and then taking absolute values.

The next candidate should therefore expose a source-forced higher-order/nonlocal signed transform whose reconstruction cost stays controlled across the full critical region. A fixed higher-order filter is only useful if its residual coefficients become genuinely smaller at the required endpoint scale; a formal zero of higher order at `z=1` is not enough by itself.

## Preserve finer source coupling when radialization discards the needed signs

The accepted parity-sensitive annular direction remains a distinct escape. Product-fiber, bilinear, prime-factor, or other source-coupled information can avoid the shell quotient, but it must carry a falsifiable signed relation rather than merely enlarge the observable.

Pointwise or narrow-window witnesses remain useful only when their location, conditioning, degree reach, and signed coupling remain controlled across the full scale range. The current no-go results classify several natural radial reconstructions; they do not imply that Möbius cancellation is inaccessible to a genuinely different source quotient.
