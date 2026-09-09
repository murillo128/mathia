# PF-249 — positive separation preserves the free Jacobi square-root threshold in full output

**Status:** `EXACT-DERIVED + SHARP-FREE-SEPARATED-THRESHOLD + FULL-OUTPUT-CALIBRATION + POSITIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-248-parity-jacobi-tail-is-trace-class-but-first-moment-critical|PF-248]] computes the square root of the constant half-line Jacobi limit from [[research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes|PF-247]] and finds an `n^{-3}` fixed-output tail, giving the toy input-weight threshold `R<5/2`. [[research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing|PF-243]], however, does not ask for one fixed output row: its far-leg estimate is a norm into the **full bulk energy space** after a fixed positive longitudinal separation. The local clue `CLUE-critical-jacobi-square-root-decay-window.md` therefore leaves open whether summing all output modes consumes the apparent `5/2` margin.

For the constant half-line square-root proxy, it does not. Positive separation exponentially damps the output mode, and that damping absorbs the polynomial growth of the row constants. More precisely, if `S=J_0^{1/2}` is PF-248's free half-line square root, `N e_n=(n+1)e_n`, and

\[
E_d=e^{-dN},\qquad d>0,
\]

then

\[
\boxed{
E_d S N^R\in\mathcal S_2
\quad\Longleftrightarrow\quad
0\le R<\frac52.
}
\]

For `R>=5/2` the operator does not even have a bounded extension. Thus the full-output separated proxy has **exactly the same sharp exponent boundary** as PF-248's fixed-row test. In particular, the whole interval `1<R<5/2` survives in the free constant half-line model.

This is not the PF-243 theorem. The actual fixed-axis parity chains have the `O(j^{-2})` first-moment-critical coefficient tail of PF-248, and the scalar operator entering the normalized actual Robin source map has not been identified as literally `J^{1/2}`. The result removes one specific ambiguity only: **full-output accumulation plus positive separation is not itself what closes the free-model smoothing window**.

## Claim

Let `J_0` act on `\ell^2(\mathbb N_0)` by

\[
(J_0u)_j=-\frac14u_{j-1}+\frac12u_j-\frac14u_{j+1},
\qquad u_{-1}=0,
\]

and put

\[
S=J_0^{1/2},\qquad
Ne_n=(n+1)e_n,\qquad
E_d=e^{-dN}.
\]

Then for every `d>0` and `R>=0`:

1. `E_dSN^R`, initially defined on finitely supported sequences, extends to a Hilbert--Schmidt operator if `R<5/2`;
2. if `R>=5/2`, `E_dSN^R` has no bounded extension;
3. hence `R=5/2` is the sharp full-output threshold for this separated free square-root model;
4. replacing `N` by either PF-247 parity restriction of the corridor weight `A^{1/2}`, whose eigenvalues are `\kappa_{2j+\varepsilon}=2j+\varepsilon+\alpha`, changes only harmless constants and the separation rate, not the threshold.

The same statement applies to the adjoint orientation `N^RSE_d`, which is the corresponding output-weighted formulation.

## 1. The half-line kernel has an exact rational form

PF-248 gives

\[
S_{mn}:=\langle e_m,Se_n\rangle
=c_{|m-n|}-c_{m+n+2},
\]

with

\[
c_k=-\frac{2}{\pi(4k^2-1)}\qquad(k\ge0),
\]

where the same formula gives `c_0=2/\pi`. Subtracting the two rational terms gives the exact identity

\[
\boxed{
S_{mn}
=-\frac{32(m+1)(n+1)}
{\pi\,[4(m-n)^2-1]\,[4(m+n+2)^2-1]}.
}
\tag{1}
\]

For fixed `m`, equation (1) recovers PF-248's

\[
S_{mn}=-\frac{2(m+1)}{\pi n^3}+O_m(n^{-4}).
\tag{2}
\]

The important point for full output is that the constant in the `n^{-3}` tail grows only polynomially with `m`.

## 2. Positive separation makes the full-output sum Hilbert--Schmidt below `5/2`

For fixed `m`, set

\[
A_m(R)=\sum_{n\ge0}(n+1)^{2R}|S_{mn}|^2.
\tag{3}
\]

Split the sum into `n<2m+2` and `n>=2m+2`.

On the finite near part, `0<=J_0<=1`, hence `\|S\|<=1` and every matrix element satisfies `|S_{mn}|<=1`. Therefore

\[
\sum_{n<2m+2}(n+1)^{2R}|S_{mn}|^2
\le C_R(m+1)^{2R+1}.
\tag{4}
\]

On the tail `n>=2m+2`, both denominator factors in (1) are bounded below by fixed positive multiples of `(n+1)^2`. Thus

\[
|S_{mn}|\le C\,(m+1)(n+1)^{-3},
\tag{5}
\]

and

\[
\sum_{n\ge2m+2}(n+1)^{2R}|S_{mn}|^2
\le C(m+1)^2
\sum_{n\ge2m+2}(n+1)^{2R-6}.
\tag{6}
\]

The last series is finite exactly when

\[
2R-6<-1,
\qquad\text{i.e.}\qquad R<\frac52.
\tag{7}
\]

For every such `R`, equations (4)--(6) give at worst polynomial growth of `A_m(R)` in `m`. Consequently

\[
\begin{aligned}
\|E_dSN^R\|_2^2
&=\sum_{m,n\ge0}e^{-2d(m+1)}(n+1)^{2R}|S_{mn}|^2\\
&=\sum_{m\ge0}e^{-2d(m+1)}A_m(R)<\infty.
\end{aligned}
\tag{8}
\]

This proves the full-output Hilbert--Schmidt bound for every `R<5/2`. No row is discarded: the entire output space is summed in (8).

The mechanism is exactly the one PF-243's geometric partition was designed to exploit. Spectral conversion may populate arbitrarily many output modes, but any mode that remains high after conversion pays an exponential positive-separation factor. Only conversion into genuinely low output modes avoids that factor, and the Dirichlet image cancellation already gives those rows the `n^{-3}` tail from PF-248.

## 3. The threshold is sharp even after separation

The first output row cannot be helped by output damping beyond the nonzero constant `e^{-d}`. Equation (1) with `m=0` gives

\[
S_{0n}
=-\frac{32(n+1)}
{\pi(4n^2-1)[4(n+2)^2-1]}
=-\frac{2}{\pi n^3}+O(n^{-4}).
\tag{9}
\]

If `E_dSN^R` had a bounded extension, its first coordinate would be a bounded linear functional on `\ell^2`, so the row

\[
\{e^{-d}(n+1)^R S_{0n}\}_{n\ge0}
\]

would have to belong to `\ell^2`. By (9), its squared tail is comparable to

\[
\sum_n n^{2R-6},
\]

which diverges for `R>=5/2`. Hence

\[
\boxed{
R\ge\frac52
\quad\Longrightarrow\quad
E_dSN^R\text{ is unbounded.}
}
\tag{10}
\]

The endpoint `R=5/2` fails logarithmically. Combining (8) and (10) proves the sharp threshold.

Positive separation is essential here. At `d=0`, `SN^R` cannot be bounded for any positive `R` merely from boundedness of `S`; the exponential output factor is what converts fixed-row decay into a full-output smoothing statement.

## 4. Translation to the PF-247 parity scale

On parity `\varepsilon\in\{0,1\}`, the corridor transverse weight inherited from PF-247 is

\[
K_\varepsilon e_j
=\kappa_{2j+\varepsilon}e_j,
\qquad
\kappa_n=n+\alpha,
\qquad
\alpha=\frac{1+\sqrt5}{2}.
\]

There are constants depending only on parity and `\alpha` such that

\[
K_\varepsilon\asymp N,
\qquad
e^{-dK_\varepsilon}\le C_de^{-d' N}
\]

for some `d'>0`. Therefore the same proof gives

\[
e^{-dK_\varepsilon}J_0^{1/2}K_\varepsilon^R\in\mathcal S_2
\quad\Longleftrightarrow\quad R<\frac52.
\tag{11}
\]

A fixed high-frequency projector `P_Z` does not change the threshold. Thus the free parity-chain proxy has more than the `R>1` demanded by PF-243 even in the norm that sums all far-leg output modes.

## 5. Prior art and novelty audit

The half-line fractional operator itself is classical and has especially close recent prior art. Gerhat--Krejčiřík--Štampach, *Criticality transition for positive powers of the discrete Laplacian on the half line*, Rev. Mat. Iberoam. 41 (2025), 1173--1200, DOI `10.4171/RMI/1523`, studies positive spectral powers of the Dirichlet half-line discrete Laplacian. Das--de la Fuente-Fernández, *An optimal fractional Hardy inequality on the discrete half-line*, Calc. Var. PDE 65 (2026), article 46, DOI `10.1007/s00526-025-03217-w`, records the spectral representation and explicit matrix elements

\[
(-\Delta_{\mathbb N})^\sigma_{mn}
=(-1)^{m+n}
\left[
{2\sigma\choose \sigma+m-n}
-{2\sigma\choose \sigma+m+n}
\right].
\]

Our `J_0` is one quarter of the Dirichlet half-line discrete Laplacian (after shifting the index from `\mathbb N` to `\mathbb N_0`), so PF-248's image kernel at `\sigma=1/2` is a scaled special case of this known half-line fractional-power formula. This strengthens the prior-art placement of PF-248; no novelty is claimed for the half-line kernel or fractional-power construction.

The project-specific contribution of PF-249 is narrower: inserting the **PF-243 positive-separation output damping** and proving the sharp weighted full-output boundary `R=5/2` by combining the exact image kernel with the source-weight requirement. The literature audit above concerns Hardy criticality and fractional powers, not this particular separated Robin-Poisson exponent budget. No general new theorem about fractional Laplacians or Jacobi matrices is claimed.

The numerical value `5/2` here is a weighted source-to-separated-output threshold and should not be confused with the unrelated Hardy criticality exponents in the cited half-line fractional-Laplacian literature.

## 6. Consequences and remaining gate

PF-249 answers one part of the accepted critical-Jacobi clue decisively:

- **full-output summation does not consume the free half-line `R<5/2` margin once a fixed positive separation is present.**

Accordingly, the next useful test should not spend effort re-proving this accumulation bound in the constant chain. The live fixed-axis question is whether the specific PF-248 perturbation

\[
J_\varepsilon-J_0=O(j^{-2})
\]

preserves any analogous estimate

\[
e^{-dN}F(J_\varepsilon)N^R\in\mathcal B(\ell^2)
\qquad\text{for some }R>1,
\]

for the **actual scalar function `F` occurring in the normalized Robin source map**. Trace-class closeness alone is not enough, and PF-248's divergent first weighted moment remains the critical obstruction to a routine threshold-scattering transfer.

Only after that fixed-axis variable-chain test succeeds should the route spend exponent budget on PF-233's `K_a` replacement and PF-235's width-dependent hypercycle/axis coordinate defect. If the variable chain already destroys every `R>1` estimate, PF-249 makes clear that the failure comes from the first-moment-critical perturbation or the actual Robin functional factor, not from summing the separated output modes.

No zeta-zero or RH consequence follows from this calibration.

## Falsification and reproducibility checks

1. **Kernel algebra.** Substituting PF-248's `c_k` into `c_{|m-n|}-c_{m+n+2}` must give (1). A missing image term restores an `n^{-2}` fixed-row tail and invalidates the theorem.
2. **Tail power.** For fixed `m`, `n^3S_{mn}/(m+1)\to-2/\pi`. This nonzero limit both proves the `5/2` obstruction and excludes accidental faster decay in the first row.
3. **Full-output sufficiency.** The proof must sum all `m`; replacing (8) by finitely many rows would not answer the PF-243 accumulation question. Exponential `e^{-dm}` is the only input that makes arbitrary polynomial growth of the row constants harmless.
4. **Sharp endpoint.** At `R=5/2`, the first-row squared norm has a harmonic tail, so no bounded extension exists even though every `R<5/2` gives a Hilbert--Schmidt operator.
5. **Model boundary.** `S=J_0^{1/2}` is still a calibration. Do not identify it with the actual complete-lift normalized Robin source factor without an independent derivation.
6. **Variable-chain boundary.** Nothing here transfers weighted decay through PF-248's `O(j^{-2})` Jacobi perturbation, `T_a`, the hypercycle coordinate map, physical `P/H` recoupling, finite-pant completion, global weak-`S_1` reassembly, or any RH-level bridge.