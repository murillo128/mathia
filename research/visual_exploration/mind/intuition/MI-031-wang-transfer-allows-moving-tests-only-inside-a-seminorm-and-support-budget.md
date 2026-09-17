# MI-031 — Wang transfer allows moving tests only inside a seminorm and support budget

**Evidence level:** literature-backed synthesis from [VIS-265](../../findings/VIS-265-wang-short-interval-support-law-blocks-bounded-window-edge-transfer.md) and [VIS-266](../../findings/VIS-266-wang-proof-admits-norm-controlled-t-dependent-tests.md).

A theorem stated for a fixed test function need not be useless for every moving packet. VIS-266 audits Wang's proof and extracts the dependence on the test seminorms. With support kept inside a fixed margin `[-lambda,lambda]`, `lambda<theta`, the short-interval pair-correlation argument controls a `T`-dependent family by an error of the form

`||g_T'||_inf/L + ||g_T||_inf[1/L + L^(-3/2) + T^(lambda-theta)L + 1/(HL)]`,

where `L=log T`.

The theorem therefore admits controlled motion and shrinkage. For a packet of width `b=L^(-q)` and amplitude `b^(-A)`, derivative growth is of order `b^(-A-1)`, so `q(A+1)<1` is a simple sufficient logarithmic condition for the derivative term to vanish. The old binary distinction “fixed test versus moving test” is too coarse.

The correct transfer ledger has three independent entries. First, the Fourier support must remain a fixed distance inside the available edge `theta`; moving the support edge toward `theta` is not covered by this uniformity. Second, amplitude and derivative seminorms must fit the theorem's growth budget. Third, the resulting remainder must still be smaller than the arithmetic signal one wants to resolve.

This matters for visual/experimental packet design: one should search within the theorem-valid moving family rather than discard all adaptive packets, but no visual concentration is evidence until its support, seminorm and signal-to-error coordinates are all audited.

**Boundary.** VIS-266 does not extend Wang's support edge, validate bounded physical source windows, produce four-level covariance, or prove that a prime-sensitive residual survives. It only replaces a false fixed-test barrier by an explicit quantitative moving-test budget.