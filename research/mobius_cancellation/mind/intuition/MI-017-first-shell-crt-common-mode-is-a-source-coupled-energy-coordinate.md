# MI-017 — First-shell smooth-dilation recombination has a subgroup-annihilator gate after sign abundance and variance are exhausted

**Evidence level:** supported by the exact CRT, Boolean-transform, smooth-inversion, dense-model, variance, and subgroup-annihilator analyses MC-228--MC-238; no square-root Möbius progression bound and no small-prime generation theorem for the special shell-square moduli is claimed.

For the first square-defect shell, MC-228--MC-233 reduce the difficult diagonalized target to

\[
B_S(X)=
\sum_{\substack{d\le T\\P^+(d)\le y}}
M_\mu\!\left(T/d;Q_S,-Pd^{-1}\bmod Q_S\right),
\qquad Q_S=\prod_{r\in S}r^2,
\]

with only `X^{o(1)}` smooth dilations. If `|S|=(\alpha+o(1))\log X/\log\log X` and `d=X^{\beta+o(1)}`, then `Q_S=X^{2\alpha+o(1)}` and the componentwise sufficient target misses trivial progression occupancy by the fixed power

\[
\delta=\max(0,\tfrac12-2\alpha-\beta).
\]

MC-234--MC-235 show that parity existence and fixed-power sign scarcity are not the obstruction: both Möbius signs have essentially the full progression occupancy exponent at every fixed interior hard point. MC-236 then shows why the audited Linnik dense-model pipeline still does not provide near-balance: it preserves principal bias, later arguments are one-sided, and separate-sign transference has only subpower relative precision.

MC-237 closes the obvious signed-average replacement. The source-selected `Q_S` is smooth enough for a strong individual-modulus variance theorem, but the resulting residue-class RMS residual is still only `X^{-o(1)}` relative to trivial occupancy. It reaches the required `X^{1/2}` scale only where support already does. Thus **sign abundance, transference resolution, and variance resolution are different currencies**.

MC-238 sharpens the final surviving escape of recombining the smooth dilations before triangle inequality. Define

\[
H_y(Q_S)=\left\langle p\bmod Q_S:p\le y\text{ prime}\right\rangle
\le G_S=(\mathbb Z/Q_S\mathbb Z)^\times.
\]

Every smooth dilation `d` and `P` lie in `H_y(Q_S)`, so all residues `-Pd^{-1}` remain in the single coset `-H_y(Q_S)`. If `nu_w` is the weighted residue measure and `chi` is a character of `G_S`, then

\[
\widehat\nu_w(\chi)
=\overline{\chi(-P)}\sum_dw_d\chi(d).
\]

For every `chi` in the annihilator `H_y(Q_S)^\perp`, this becomes

\[
\boxed{\widehat\nu_w(\chi)=\overline{\chi(-1)}\sum_dw_d.}
\]

Hence a nonnegative smooth-dilation average has normalized Fourier modulus exactly one on every blind character. **The dilation variable creates no oscillation at all on those modes.** Aggregate cancellation cannot be justified merely by saying that the residue changes with `d`; the orbit must first be large enough in the character directions that matter.

The quadratic blind sector is especially concrete. Let

\[
A_{p,r}=\frac{1-(\frac pr)}2\in\mathbb F_2,
\]

with lower primes `p<=y` as rows and shell primes `r\in S` as columns. Then

\[
\dim_{\mathbb F_2}H_y(Q_S)^\perp[2]
=|S|-\operatorname{rank}_{\mathbb F_2}A.
\]

Full column rank removes quadratic blind characters; it says nothing about higher-order characters. The logarithmic cutoff `y\asymp\log Q_S` is also genuinely delicate: generic generator theorems do not supply it, and generic moduli can fail linear-logarithmic generation. None of this proves that the special Mathia shell-square moduli actually have a nontrivial annihilator.

The reusable separation is therefore: **componentwise signed balance, aggregate residue averaging, subgroup generation, Fourier decay on the generated subgroup, and arithmetic coupling between residues and Möbius values are distinct gates**. A large family of source-selected residues can remain Fourier-degenerate because all its motion lies inside one proper subgroup coset.

The remaining routes are precise: obtain fixed-power signed discrepancy directly; prove `H_y(Q_S)=G_S` for the relevant shell-square family or control the annihilator modes that survive; prove quantitative character decay for the bounded smooth-dilation measure on all nonblind modes; or exploit a coupling between `d` and the progression sum that is invisible after projecting to the residue orbit.

**Boundary.** MC-238 is an exact support/Fourier obstruction for the residue measure, not a proof that the special shell-square moduli have blind characters and not an estimate for `B_S(X)`. MC-236--MC-237 audit particular theorem surfaces rather than proving stronger signed theorems impossible. No Mertens or RH consequence follows.