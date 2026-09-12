# FD-065 — growing Schur heads improve tail occupation but worsen scalar leverage

**Status:** `EXACT-DERIVED + ZERO-FRONTIER-CALIBRATED + GROWING-SCHUR-HEAD + DIRECT-TRANSFER-PACKET + NORMALIZATION-TRADEOFF + TWO-THIRDS-INVARIANCE + ROUTE-OBSTRUCTION`.

`FD-064` classifies the direct short-interval transfer family with a fixed Schur head. Moving the host outward can create a polynomial nonsquarefree packet, but the larger physical horizon offsets that gain in the normalized tail occupation. A natural response is to move the Schur head outward as well: deleting the small Jordan rows removes the fixed-row source samples at arguments much larger than the transferred spike, so the tail denominator becomes genuinely more local to the host scale.

That maneuver does improve the **raw tail occupation fraction**, but it does not improve the RH-facing scalar relaxation. The exact Schur leverage available after eliminating a head of size `D` is

\[
\Delta_{T,D}=C_T-C_D,
\]

and this shrinks like `D^{-1}`. At a zero frontier `Theta<1`, the denominator saving from a growing head is only `D^{2Theta-1}` at the power scale. Their product is therefore

\[
D^{-1}D^{2\Theta-1}=D^{-2(1-\Theta)},
\]

which is a **loss**, not a gain. Quantitatively, every positive head-growth exponent adds exactly the same penalty to both the packet obstruction of `FD-064` and the deterministic terminal-row obstruction of `FD-032`. The `Theta=2/3` crossover between those two mechanisms is unchanged.

This closes one specific version of the "source-coupled same-horizon denominator" escape left open by `FD-064`: merely discarding the small rows until the denominator samples the source nearer the transferred spike cannot improve the scalar GCD-duality bound. A genuinely stronger same-horizon argument must improve the fixed-head denominator itself, couple numerator and denominator arithmetically, or use information not represented by Schur-head elimination.

## 1. Setup: let the Schur head grow inside the transferred host

Retain the zero-frontier notation of `FD-064`. Let

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\},
\qquad 0.55<\Theta<1,
\]

and choose a spike sequence

\[
A_X:=|\mathcal H(X)|=X^{\Theta+o(1)}.
\tag{1}
\]

Fix

\[
0.55<\vartheta<\Theta,
\qquad
1-\Theta<\lambda\le1-\vartheta,
\]

and a packet exponent

\[
0<\kappa<\Theta+\lambda-1.
\tag{2}
\]

As in `FD-064`, let

\[
K_X=\lfloor X^\kappa\rfloor,
\qquad
q=X^{\lambda+o(1)},
\qquad
T=qX,
\]

with `q` in the same fixed host corridor, and put

\[
x_{q,d}:=\left\lfloor\frac{T}{q+d}\right\rfloor
\qquad(1\le d\le K_X).
\tag{3}
\]

The direct all-short-interval transfer already proved there gives uniformly

\[
\boxed{
\mathcal H(x_{q,d})=\mathcal H(X)+o(A_X).
}
\tag{4}
\]

Now allow a horizon-dependent Schur head `D=D_X` satisfying

\[
1\le D\le \frac q2,
\qquad
D=X^{\delta+o(1)},
\qquad
0\le\delta\le\lambda.
\tag{5}
\]

The endpoint `delta=lambda` is represented, for example, by `D=floor(q/2)`. For `delta=0`, `D` may be fixed or subpower.

Define the physical tail energy and its nonsquarefree part by

\[
E_{T,D}
:=\sum_{r>D}\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Tr\right\rfloor\right)^2,
\]

\[
U_{T,D}
:=\sum_{\substack{r>D\\\mu(r)=0}}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Tr\right\rfloor\right)^2,
\qquad
\nu_{T,D}:=\frac{U_{T,D}}{E_{T,D}}.
\tag{6}
\]

The Schur geometry of `FD-031`--`FD-032` gives

\[
\varepsilon_{T,D}:=\frac{\rho_{T,D}^2}{E_{T,D}},
\qquad
\mathfrak D_{T,D}
:=C_T-\widehat R_{T,D}
=\Delta_{T,D}\varepsilon_{T,D},
\]

\[
\Delta_{T,D}:=C_T-C_D.
\tag{7}
\]

Because the equality ray is exactly zero on nonsquarefree Jordan rows,

\[
\boxed{
\varepsilon_{T,D}\ge\nu_{T,D}.
}
\tag{8}
\]

All identities in (6)--(8) are finite-horizon statements and remain valid when `D` grows.

## 2. A growing head saves `D^(2Theta-1)` in energy but loses `D` in scalar leverage

`FD-003` gives the exact coordinate constant

\[
C_N=\sum_{n\le N}\frac{\mu(n)^2}{J_2(n)}.
\tag{9}
\]

Hence

\[
\Delta_{T,D}
=\sum_{D<n\le T}\frac{\mu(n)^2}{J_2(n)}.
\tag{10}
\]

The elementary bound `J_2(n)>=n^2/zeta(2)` gives

\[
\Delta_{T,D}\ll \sum_{n>D}n^{-2}\ll D^{-1}.
\tag{11}
\]

For the reverse power bound, restrict (10) to squarefree `D<n<=2D` (eventually `2D<T`). The classical squarefree count

\[
\sum_{n\le x}\mu(n)^2=\frac{x}{\zeta(2)}+O(\sqrt x)
\]

and `J_2(n)<=n^2` give

\[
\Delta_{T,D}\gg
\sum_{\substack{D<n\le2D\\\mu(n)^2=1}}\frac1{n^2}
\gg D^{-1}.
\tag{12}
\]

Thus, for `delta>0`,

\[
\boxed{
\Delta_{T,D}=X^{-\delta+o(1)}.
}
\tag{13}
\]

For fixed or subpower `D`, the same exponent statement is `Delta_(T,D)=X^{o(1)}`, so (13) remains correct at `delta=0` in the power-scale sense used below.

On the denominator side, take any fixed `sigma>Theta`. The zero-frontier envelope from `FD-046` gives `|mathcal H(n)|<<_sigma n^sigma`; therefore

\[
\begin{aligned}
E_{T,D}
&\ll_\sigma
T^{2\sigma}
\sum_{r>D}r^{-2\sigma}\\
&\ll_\sigma
T^{2\sigma}D^{1-2\sigma}.
\end{aligned}
\tag{14}
\]

Since `T=X^{1+lambda+o(1)}` and `D=X^{delta+o(1)}`, allowing `sigma` to approach `Theta` from the right yields the power envelope

\[
\boxed{
E_{T,D}
\le
X^{\,2\Theta(1+\lambda)+\delta(1-2\Theta)+o_{\rm up}(1)}.
}
\tag{15}
\]

Here `o_up(1)` denotes the usual arbitrarily small fixed loss coming from taking an exponent strictly to the right of the zero frontier; no assertion at `sigma=Theta` is needed.

Relative to a fixed head, (15) gains the factor

\[
D^{-(2\Theta-1)}.
\tag{16}
\]

But (13) says the scalar Schur leverage simultaneously loses a full factor `D^{-1}`. Consequently any lower bound for the angle/occupation factor that uses only the denominator saving is weakened in the scalar defect by

\[
\boxed{
D^{-1}\,D^{2\Theta-1}
=D^{-2(1-\Theta)}.
}
\tag{17}
\]

Because `Theta<1`, this is always a genuine loss at every positive power of `D`.

## 3. The transferred packet inherits exactly the same head-growth penalty

Since `D<=q/2`, every packet row `q+d` lies in the physical tail. Among `1<=d<=K_X`, one quarter up to `O(1)` satisfy `4|(q+d)` and are therefore nonsquarefree. Using (4) and `J_2(r)/r^2>=1/zeta(2)`, exactly as in `FD-063`--`FD-064`, gives

\[
\boxed{
U_{T,D}
\ge
\left(\frac1{4\zeta(2)}-o(1)\right)
K_XA_X^2
=X^{2\Theta+\kappa+o(1)}.
}
\tag{18}
\]

Combining (15) and (18), for every `eta>0`,

\[
\boxed{
\nu_{T,D}
\gg_\eta
X^{-\{2\Theta\lambda-\kappa-\delta(2\Theta-1)\}-\eta}.
}
\tag{19}
\]

Thus the growing head really does improve raw occupation: the loss exponent is smaller by `delta(2Theta-1)`.

However, the RH-facing scalar relaxation is `mathfrak D=Delta epsilon`, not `epsilon` alone. Equations (8), (13), and (19) give

\[
\boxed{
\mathfrak D_{T,D}
\gg_\eta
X^{-\{2\Theta\lambda-\kappa+2\delta(1-\Theta)\}-\eta}.
}
\tag{20}
\]

In physical-horizon coordinates `T=X^(1+lambda+o(1))`, the packet loss exponent is therefore

\[
\boxed{
\gamma_{\rm pkt}(\Theta,\lambda,\kappa,\delta)
=
\frac{2\Theta\lambda-\kappa+2\delta(1-\Theta)}{1+\lambda}.
}
\tag{21}
\]

For fixed `Theta,lambda,kappa`, this is strictly increasing in `delta` whenever `Theta<1`. Hence **no growing Schur head can strengthen the packet-based scalar gap**. The optimal choice inside this whole family is `delta=0`, which returns exactly the fixed-head exponent of `FD-064`.

## 4. The deterministic terminal-row obstruction pays the identical penalty

The packet is not the only source of transverse mass. `FD-032` proves for every `D<T/2`

\[
\boxed{
\rho_{T,D}^2\gg T.
}
\tag{22}
\]

Our range `D<=q/2` and `T=qX` satisfies that hypothesis. Using (15),

\[
\varepsilon_{T,D}
=\frac{\rho_{T,D}^2}{E_{T,D}}
\gg_\eta
X^{-(2\Theta-1)(1+\lambda)+\delta(2\Theta-1)-\eta}.
\tag{23}
\]

Multiplication by (13) yields

\[
\boxed{
\mathfrak D_{T,D}
\gg_\eta
X^{-\{(2\Theta-1)(1+\lambda)+2\delta(1-\Theta)\}-\eta}.
}
\tag{24}
\]

Equivalently the physical-horizon loss exponent is

\[
\boxed{
\gamma_{\rm term}(\Theta,\lambda,\delta)
=
(2\Theta-1)
+
\frac{2\delta(1-\Theta)}{1+\lambda}.
}
\tag{25}
\]

The head-growth penalty is **exactly the same additive term** as in (21):

\[
\boxed{
\frac{2\delta(1-\Theta)}{1+\lambda}.
}
\tag{26}
\]

Thus the growing-head maneuver does not merely fail for the specific four-adic packet. It worsens both independent scalar obstructions presently available for this family by the same amount.

At `delta=0`, (25) is the zero-frontier terminal exponent `2Theta-1` already underlying `FD-049`. A positive `delta` can make the raw tail angle larger by shrinking its denominator, but the available coordinate leverage `C_T-C_D` shrinks even faster at the scalar level.

## 5. The two-thirds crossover survives every head-growth exponent

For fixed `lambda`, the largest direct packet allowed by `FD-064` approaches

\[
\kappa=\Theta+\lambda-1
\]

from below. Subtracting (25) from (21) and then taking that packet endpoint gives

\[
\boxed{
\gamma_{\rm pkt}-\gamma_{\rm term}
\longrightarrow
\frac{2-3\Theta}{1+\lambda}.
}
\tag{27}
\]

The common head penalty (26) cancels identically. Therefore:

- for `Theta<2/3`, the deterministic terminal-row obstruction is stronger;
- for `Theta>2/3`, the transferred packet obstruction is stronger;
- at `Theta=2/3`, they meet exactly.

The switch remains at

\[
\boxed{\Theta=\frac23}
\tag{28}
\]

for every admissible growing-head exponent `delta`. This is the same crossover exposed by the host/packet optimization of `FD-064`, now from an independent normalization direction.

More importantly, because both exponents worsen monotonically with `delta`, optimizing over the head gives

\[
\boxed{
\inf_{\delta\ge0}\gamma_{\rm pkt}
=\gamma_{\rm pkt}|_{\delta=0},
\qquad
\inf_{\delta\ge0}\gamma_{\rm term}
=\gamma_{\rm term}|_{\delta=0}.
}
\tag{29}
\]

So moving the Schur cut toward the host can improve the visual/raw occupation of nonsquarefree rows while **never improving the scalar GCD-duality obstruction obtained from that occupation**.

## 6. Prior-art boundary, controls, and what remains open

The matrix facts used here are the existing internal specialization of classical Smith/GCD-matrix algebra: `FD-003` supplies the exact coordinate constants `C_N`, while `FD-031`--`FD-032` supply the Schur relaxation and terminal-row distance. The zeta-zero envelope and direct packet are exactly `FD-046` and `FD-064`. The squarefree counting estimate used only to calibrate `Delta_(T,D)` is classical.

A targeted literature audit across GCD/meet matrices, Schur complements, Farey--Franel criteria, Mertens transforms, and recent restricted-denominator Farey results located the expected classical GCD-matrix factorization/inverse literature and modern Farey variants, but no statement matching the head-growth normalization law (17), the scalar exponents (21)/(25), or their common penalty (26). No priority claim is made, and no new external theorem is load-bearing, so `SOURCES.md` requires no change.

Several falsification boundaries matter. First, the result concerns the scalar relaxation `C_T-hat R_(T,D)=Delta epsilon`; a theorem whose target is the raw occupation fraction `nu` may genuinely benefit from growing `D`, as (19) shows. Second, `D` must stay below the host packet so that the packet remains in the physical tail; the exponent endpoint `delta=lambda` is represented by a fixed fraction of `q`, not by deleting the packet itself. Third, the zero-frontier denominator estimate uses only the generic pointwise source envelope. A new **fixed-head** estimate coupling `E_(T,D)` to the selected spike `A_X`, a host-average theorem exploiting correlations between numerator and denominator, or a different Farey-intrinsic information carrier is not ruled out.

Finally, this is a route obstruction rather than an RH theorem. It does not prove a positive occupation constant, improve the Mertens exponent, or exclude cancellation below the square-root interval scale. What it does establish is an exact accounting principle for one proposed normalization repair: **head truncation cannot make the direct-transfer packet more useful for scalar extraction, because every power saved in the tail denominator is overpaid by the shrinking Schur leverage.**