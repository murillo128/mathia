# MI-017 — The first square-defect shell contains a source-forced CRT common mode

**Evidence level:** supported by the exact intersection identity and power-budget analysis of MC-228; no new Möbius cancellation estimate is claimed.

The first square-defect shell is not a family of unrelated progression tests. With `y=c log X`, primorial `P`, shell primes `d in (y,2y]`, and

\[
\mathcal R_d=\{n\le X-P:(n,P)=1,\ n\equiv-P\pmod{d^2}\},
\]

put `Q_y=prod_d d^2`. The source-selected residues have the exact simultaneous intersection

\[
\bigcap_d\mathcal R_d
=\{kQ_y-P:1\le k\le X/Q_y,\ (k,P)=1\}.
\]

Since `Q_y=X^{2c+o(1)}`, this common block has

\[
|\cap_d\mathcal R_d|=X^{1-2c+o(1)}/\log y.
\]

For `c<1/4`, almost all of these common points are square-free, so the overlap carries polynomially many actual Möbius signs rather than merely unsigned rough support.

Writing the signed common sum as

\[
C_y=\sum_{n\in\cap_d\mathcal R_d}\mu(n),
\]

every shell coordinate decomposes exactly as `A_d=C_y+B_d`. If the common component is controlled separately, its weighted shell energy is bounded only by

\[
H_y|C_y|^2\le X^{2-4c+o(1)},
\qquad H_y=\sum_d d=X^{o(1)}.
\]

Thus separate absolute control has a sharp power boundary at `c=1/4`: for `c>=1/4` the common block is target-scale harmless by support alone; for `c<1/4` the same route is super-diagonal and needs genuine signed cancellation in `C_y` or coherent interference with the residual vectors `B_d`.

The matched independent prime-sign control is important. Its expected common-mode energy is only `X^{1-2c+o(1)}`, below the target scale. The obstruction is therefore not common incidence by itself; it is the deterministic parity coherence of the Möbius source, or the way that common component interferes with the rest of the source-selected shell.

This sharpens the meaning of “source-coupled cancellation.” Generic characterwise, large-sieve, or fiberwise estimates can lose the exact integer intersection copied into every shell coordinate. The next useful theorem should act on that coupled decomposition before taking magnitudes.

**Boundary.** The `c=1/4` threshold concerns a proof that estimates the common block independently. It does not prove that `|C_y|<=X^{1/2+o(1)}` is necessary for the full shell energy, because the residual terms may anti-align with `C_y`. Nor does the identity itself improve Mertens bounds or imply anything about zeta zeros.
