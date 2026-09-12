# FD-061 — CRT packets sharpen global occupation loss above the two-thirds frontier

**Status:** `EXACT-DERIVED + ZERO-FRONTIER-SPIKE + CRT-PACKET + GLOBAL-OCCUPATION-EXPONENT + SOURCE-ENVELOPE + ROUTE-REFINEMENT`.

`FD-060` turns one zero-frontier shell spike into a growing packet of nonsquarefree Jordan rows. Its lower bound is local in row space: the packet energy beats the selected squarefree host row by an unbounded factor, but unrelated rows may still dominate the full denominator `E_(T,D)`. The zeta-zero upper envelope from `FD-046` gives a first global answer to that denominator problem at the **power-exponent scale**.

Let

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\},
\qquad \frac12<\Theta<1,
\]

and choose a zero-frontier spike sequence for the physical shell source such that

\[
A_X:=|\mathcal H(X)|=X^{\Theta+o(1)}.
\tag{1}
\]

Then `Q_X:=X/A_X=X^{1-\Theta+o(1)}\to\infty`, so the `FD-060` construction supplies integers `K_X\to\infty`, with `K_X=X^{o(1)}`, and squarefree hosts `q=q_X` satisfying

\[
2K_XQ_X\le q\le(2K_X+1)Q_X,
\tag{2}
\]

such that `q+1,...,q+K_X` are all nonsquarefree. Put

\[
T_X:=qX.
\tag{3}
\]

For every fixed Schur-head dimension `D`, write

\[
\nu_{T,D}:=\frac{U_{T,D}}{E_{T,D}}
\]

for the nonsquarefree Jordan occupation fraction. Define

\[
\boxed{
\beta_\Theta:=\frac{2\Theta(1-\Theta)}{2-\Theta}.
}
\tag{4}
\]

Then for every `eta>0`, along the horizons `T_X` constructed above,

\[
\boxed{
T_X^{\beta_\Theta+\eta}\,\nu_{T_X,D}\longrightarrow\infty.
}
\tag{5}
\]

The same conclusion holds for the normalized Schur projective defect `epsilon_(T,D)`, because `epsilon_(T,D)>=nu_(T,D)`.

Combining (5) with the all-horizon bound of `FD-049` gives, on these packet horizons,

\[
\boxed{
T_X^{\gamma_\Theta+\eta}\,\nu_{T_X,D}\to\infty,
\qquad
\gamma_\Theta:=
\min\!\left\{
2\Theta-1,
\frac{2\Theta(1-\Theta)}{2-\Theta}
\right\}.
}
\tag{6}
\]

The two exponents cross exactly at

\[
\Theta=\frac23.
\tag{7}
\]

Hence the CRT-packet mechanism gives a **strictly stronger global occupation-loss barrier whenever `Theta>2/3`**:

\[
\boxed{
\Theta>\frac23
\Longrightarrow
\beta_\Theta<2\Theta-1.
}
\tag{8}
\]

This does not prove `liminf U/E>0`. It shows instead that the local packet amplification of `FD-060` survives division by the entire physical energy strongly enough to improve the allowed polynomial loss on a source-selected subsequence when the zero frontier lies sufficiently far to the right.

## 1. The packet lower bound and the global energy upper envelope live at different horizons

`FD-060` gives, for fixed `D` and all sufficiently large `X` in the spike sequence,

\[
U_{T_X,D}
\ge
\frac{K_X}{\zeta(2)}
\left(\frac{A_X}{2}-1\right)^2.
\tag{9}
\]

Since `A_X\to\infty`, this implies

\[
U_{T_X,D}\gg K_XA_X^2.
\tag{10}
\]

The host relation (2) also gives

\[
T_X=qX\asymp K_X\frac{X^2}{A_X}.
\tag{11}
\]

Because `K_X=X^{o(1)}` and (1) holds,

\[
\boxed{
T_X=X^{2-\Theta+o(1)}.
}
\tag{12}
\]

The denominator is controlled by the physical zero-frontier envelope rather than by the packet itself. `FD-046` proves that for every fixed `sigma>Theta`,

\[
E_{T,D}\ll_{D,\sigma}T^{2\sigma}
\qquad(T\to\infty).
\tag{13}
\]

Applying (13) at `T=T_X` and dividing (10) by it yields

\[
\nu_{T_X,D}
\gg_{D,\sigma}
K_XA_X^2T_X^{-2\sigma}.
\tag{14}
\]

At the power scale, (1) and (12) turn (14) into

\[
\frac{\log \nu_{T_X,D}}{\log T_X}
\ge
-\frac{2\sigma(2-\Theta)-2\Theta}{2-\Theta}
+o(1).
\tag{15}
\]

Letting `sigma` approach `Theta` from the right gives precisely

\[
\frac{2\Theta(2-\Theta)-2\Theta}{2-\Theta}
=
\frac{2\Theta(1-\Theta)}{2-\Theta}
=\beta_\Theta.
\tag{16}
\]

To obtain the stronger limit form (5), fix `eta>0` first and choose `sigma>Theta` sufficiently close that the loss from `sigma-Theta` is smaller than a fixed fraction of `eta`. The `o(1)` terms in (1), (12), and (15) are then eventually smaller than the remaining margin. Multiplication by `T_X^(beta_Theta+eta)` leaves a positive power of `T_X`, so the product tends to infinity. No rate for `K_X\to\infty` is needed for this conclusion; its subpower size is enough.

## 2. The packet improves the universal exponent only beyond `Theta=2/3`

`FD-049` proves pointwise at every sufficiently large horizon that for each `eta>0`,

\[
T^{2\Theta-1+\eta}\nu_{T,D}\to\infty.
\tag{17}
\]

Therefore the packet horizons inherit both (5) and (17). The relevant exponent is their minimum. A direct subtraction gives

\[
\beta_\Theta-(2\Theta-1)
=
\frac{2-3\Theta}{2-\Theta}.
\tag{18}
\]

Thus:

- for `1/2<Theta<2/3`, the all-horizon four-adic/zero-frontier mechanism of `FD-049` is stronger;
- at `Theta=2/3`, both give exponent `1/3`;
- for `2/3<Theta<1`, the CRT-packet horizon gives the stronger exponent `beta_Theta`.

The crossover is structural rather than an artifact of constants. `FD-049` gains from comparing the full energy at `T` with a fixed lower dilation of the same horizon. `FD-060` instead begins with a spike at the earlier source scale `X` and moves to the much later horizon `T_X=X^(2-Theta+o(1))`; the packet multiplicity partly offsets that dilation, and only after `Theta>2/3` does this trade beat the universal four-adic bound.

## 3. Growing packet multiplicity does not itself buy a better power exponent

It is tempting to read the factor `K_X` in (10) as an additional global power gain. The horizon displacement in (11) prevents that. Using the explicit upper relation `T_X\ll K_XX^2/A_X` in (14) gives

\[
\nu_{T_X,D}
\gg_{D,\sigma}
K_X^{1-2\sigma}
A_X^{2+2\sigma}
X^{-4\sigma}.
\tag{19}
\]

Since `sigma>Theta>1/2`, the exponent `1-2sigma` of `K_X` is negative. A longer packet moves the evaluation horizon farther out, where the global energy envelope is correspondingly larger. Because `K_X=X^{o(1)}`, this cost is invisible in (5), but it shows that **packet multiplicity and global occupation are genuinely different currencies**: the unbounded local ratio `U/J_q` of `FD-060` does not turn into an extra polynomial factor after normalization by `E`.

This also explains why optimizing the CRT packet length inside the existing construction would not improve `beta_Theta`. To change the power exponent one needs either a denominator estimate sharper than the global `T^(2Theta+o(1))` envelope on the packet horizons, or a transfer mechanism that reaches many nonsquarefree rows without paying the proportional horizon displacement in (11).

## 4. Boundary conditions and adversarial checks

The restriction `Theta<1` is essential for this formulation. It guarantees `Q_X=X/A_X\to\infty` along a frontier spike sequence and therefore places the `FD-060` CRT host construction in its stated regime. The result makes no claim for the possible limiting case `Theta=1`.

The spike hypothesis (1) is not an extra regularity assumption. `FD-046` proves

\[
\limsup_{X\to\infty}
\frac{\log(1+|\mathcal H(X)|)}{\log X}
=\Theta,
\]

so when `Theta>0` one may select an unbounded sequence with `A_X=X^(Theta+o(1))`; for `Theta<1` this simultaneously gives `A_X\to\infty` and `Q_X\to\infty`.

The argument does not assume that the packet dominates `E_(T_X,D)`. Equation (13) is deliberately the only denominator input. Consequently (5) remains valid even if low Jordan rows dominate the energy, but it cannot yield a positive occupation constant. It also does not improve the below-critical transfer problem of `FD-055`--`FD-058`: all packet rows are still manufactured on the deterministic supercritical side `qA_X/X\asymp K_X\to\infty`.

The head dimension `D` must remain fixed. Both the packet inclusion and the energy envelope used here are stated with that quantifier. No uniform claim for `D=D(T)\to\infty` is made.

Finally, (5) is a lower-rate statement, not an asymptotic formula. It does not identify the true decay exponent of `U/E`, assert monotonicity, or exclude subpower loss. The actual ratio can be much larger than the bound.

## 5. Prior art and research consequence

The external analytic input is the classical Mertens/zeta zero-frontier growth theorem already anchored through Titchmarsh in `SOURCES.md`; `FD-046` is the local canonical bridge turning it into the all-horizon energy envelope (13). The CRT and squarefree-progression ingredients behind the packet are already derived and audited in `FD-060`. A targeted literature search across Farey discrepancy, Mertens growth, Jordan-totient energies, and squarefree/nonsquarefree occupation located the expected classical Farey--Mertens and squarefree literature but no theorem matching the packet-horizon exponent comparison (4)--(8). No new external theorem is load-bearing, so `SOURCES.md` needs no change.

The main research delta is quantitative. The global competing-denominator problem left by `FD-060` is not completely uncontrolled: the zero-frontier envelope converts the packet into a source-selected global lower bound for `U/E`. Above `Theta=2/3`, that lower bound is strictly stronger at the polynomial scale than the previous all-horizon occupation barrier.

What remains is now sharper. To turn packet amplification into a positive occupation fraction, or even improve (5) below the displayed exponent, one must beat the generic global envelope **on the same packet horizons** or transport the source spike with a better row-count/horizon tradeoff. Merely increasing the CRT packet by another subpower factor cannot change the power-scale conclusion.