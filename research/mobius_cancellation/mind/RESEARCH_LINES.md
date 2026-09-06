# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Treat low-bias Hamming amplitude regularization and degree-only reconstruction as classified

**Linked intuitions:** `MI-011-source-forced-prime-deformation-is-a-polynomial-information-channel` and `MI-012-hamming-regularization-is-degree-two-damping-before-the-square-root-transition`.

MC-097--MC-101 show that fixed and mesoscopic low-bias amplitudes are dominated by a positive degree-two shell rather than by the signed cancellation governing the hard endpoint. MC-102 closes the apparent square-root transition: the exact degree-zero shell has a positive linear asymptotic, so the low-bias profile crosses from degree-two scale to a positive `c_0 N` floor instead of entering a new cancellation regime.

MC-103 then closes the generic reconstruction escape. Endpoint evaluation from a shrinking low-bias interval has the exact Chebyshev extrapolation norm, which is superpolynomial for polynomially shrinking windows at the available Hamming degree ceiling; the obstruction survives knowledge of any fixed number of low shells. Thus neither shrinking the amplitude toward zero nor black-box signed interpolation of degree-bounded polynomials transports the low-bias gain to the Möbius endpoint.

## Derive a source-specific signed relation that is not valid on the full degree-bounded class

A survivor must exploit arithmetic constraints among the actual Hamming coefficients, a signed cross-degree recurrence, a non-point observable, or a different source coupling. It must prove a reconstruction/contraction whose conditioning is funded by those source relations rather than by polynomial degree alone, and its gain must survive the exact positive diagonal floor and the known large signed shell cancellation.

## Keep comparator turnover and scale coverage explicit

Moving interior windows or source-specific recurrences remain logically open, but per-scale witnesses do not form an iterable theorem unless their location, conditioning, and source relation stay controlled across the full scale range. Any proposed recurrence must preserve the signed coupling uniformly rather than pay back the gain through unstable extrapolation or a hidden endpoint estimate.
