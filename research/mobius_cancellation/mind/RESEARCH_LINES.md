# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove fixed-power signed near-balance or defeat the smooth-dilation character blind sector

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`.

MC-188--MC-233 reduce the first-shell obstruction to a sparse source-coupled family of ordinary reduced-residue Möbius progression sums

\[
B_S(X)=
\sum_{\substack{d\le T\\P^+(d)\le y}}
M_\mu(T/d;Q_S,-Pd^{-1}\bmod Q_S),
\]

with `Q_S=X^{2\alpha+o(1)}` and component scale `Z=X^{1-\beta+o(1)}`. Support closes `2\alpha+\beta\ge1/2`. In the strict hard region `2\alpha+\beta<1/2`, the componentwise sufficient target needs fixed-power relative cancellation `X^{-\delta+o(1)}` with `\delta=1/2-2\alpha-\beta>0`.

MC-234--MC-235 remove qualitative parity and polynomial sign scarcity: the Linnik machinery already gives both signs essentially full occupancy exponent in every fixed interior hard progression. MC-236 identifies where the published dense-model route loses the missing information. The sign-specific dense model preserves each principal-character mean exactly, while the subsequent threshold/product-set argument is one-sided and the published separate-sign transference precision is only `q^{-o(1)}` relative to its one-sided main scale.

MC-237 closes a different tempting repair. The exact deep CRT modulus `Q_S` is exceptionally smooth, so the Klurman--Mangerel--Teräväinen individual-smooth-modulus variance theorem applies directly to the source-selected modulus. Even after granting that the distinguished-character main term is harmless, its residue-class RMS residual is only

\[
X^{1-\beta-2\alpha+o(1)}=\frac Zq X^{o(1)},
\]

namely a subpower relative improvement over trivial occupancy. It reaches the `X^{1/2}` target only when `2\alpha+\beta\ge1/2`, exactly where support already closes the component.

MC-238 now puts an exact algebraic gate on the remaining suggestion to recombine the smooth dilations before triangle inequality. Let

\[
H_y(Q_S)=\langle p\bmod Q_S:p\le y\text{ prime}\rangle
\le(\mathbb Z/Q_S\mathbb Z)^\times.
\]

Every `y`-smooth dilation `d` and the primorial factor `P` lie in this subgroup, so every source-selected residue `-Pd^{-1}` lies in the single coset `-H_y(Q_S)`. If `chi` is trivial on `H_y(Q_S)`, then for any dilation weights `w_d`,

\[
\widehat\nu_w(\chi)
=\overline{\chi(-1)}\sum_dw_d.
\]

For nonnegative weights this mode has normalized Fourier modulus one: **smooth-dilation averaging produces no cancellation at all on the annihilator `H_y(Q_S)^\perp`**. Thus residue-space spreading can help only after proving that the relevant annihilator is trivial or controlling its contribution by another source-coupled mechanism.

The quadratic blind sector has an exact finite diagnostic. With rows indexed by primes `p<=y`, columns by shell primes `r\in S`, and

\[
A_{p,r}=\frac{1-(\frac pr)}2\in\mathbb F_2,
\]

its dimension is `|S|-rank_F2(A)`. Full column rank eliminates quadratic blind characters but does not eliminate higher-order characters. Generic small-generator theorems do not settle the special shell-square family at the required logarithmic cutoff.

The surviving alternatives are therefore sharper: prove source-selected fixed-power signed discrepancy directly; prove that small primes generate the relevant shell-square unit groups, or otherwise control every annihilator mode; prove quantitative Fourier decay of the bounded smooth-dilation measure on the remaining characters; or exploit arithmetic coupling between the dilation and the Möbius progression values that is not captured by the residue orbit itself.

## Treat gauge, support, Boolean conditioning, smooth inversion, sign abundance, transference resolution, variance resolution, subgroup support, and signed amplitude as separate gates

High incidence is cheap by support. Exact-cell membership and the Boolean transform cost only `X^{o(1)}`. At logarithmic smoothness, the primorial coprimality mask unfolds into only `X^{o(1)}` ordinary progression sums. Each Möbius sign already has essentially full-exponent abundance in every fixed strict hard component, and the exact deep CRT modulus already lies inside a strong unconditional smooth-modulus variance theorem.

None of these reductions supplies near-balance. MC-236 shows that a nonnegative dense model can preserve principal bias exactly while proving excellent one-sided coverage. MC-237 shows that genuine signed second-moment dispersion on each smooth modulus can still have only subpower relative resolution where the target needs a fixed negative power. MC-238 adds that even aggregate recombination across dilations has an exact **support geometry**: all residues remain in one small-prime-generated coset, and annihilator characters are completely blind to the dilation average.

Future progress should therefore be credited only when it controls the source-selected signed amplitude at the required power scale, proves enough generation/Fourier decay to make aggregate recombination effective, or uses a coupling not visible in the residue measure. More representative-existence theorems, unsigned density, smooth-modulus applicability, subpower variance/transference improvements, or the mere number of smooth dilations do not cross the live gate.