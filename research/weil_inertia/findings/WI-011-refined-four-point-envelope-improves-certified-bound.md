# WI-011 — the trace--energy envelope upgrades the proved four-point certificate to 0.672852563956...

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED`. The finite four-point inequality is the `sorry`-free Lean theorem `four_point_cert` in `teal-sea/zeta-lab`; the full-bandwidth stability/explicit-formula bridge is the one already audited in WI-009. The trace--energy envelope and window-in-frame averaging used below are prior art from `tawanerguo-cn/zeta-simple-zeros` and were independently re-derived in `trmdy/zeta-simple-zeros-673137`. The splice and constant below are an exact deduction from those inputs. The new assembled constant is not yet itself an end-to-end Lean theorem.

## 1. Precise unconditional improvement

Let

\[
H_{\rm MT}
=
\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}
=
0.6725007036794116457\ldots
\]

and let `S=N_0^s(T,2T)`, `N=N(T,2T)`. WI-009 records the formally checked stability bridge

\[
S\ge H_{\rm MT}N+\mathcal D(M^\circ)-o(N),
\qquad
\mathcal D(G)=\operatorname{tr}\Psi(G),
\]

where

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

The same Lean development proves, for every three nonnegative normalized gaps, the four-point inequality

\[
F_4(g_1,g_2,g_3)\ge \varepsilon,
\qquad
\varepsilon=\frac{231}{100000},
\]

with uniform span-pressure coefficient

\[
p=\frac1{2500}.
\]

Using the sharper trace--energy/block assembly described below and choosing block length

\[
m=438,
\]

gives

\[
A=\varepsilon(m-3)
=\frac{20097}{20000}
=1.00485.
\]

Define

\[
\Phi_m(A)=
2\sqrt{\frac{m-1}{m}A}-1+\frac{A}{m}
\]

on the second branch `A >= m/(m-1)`. At `m=438`,

\[
\Phi_{438}(A)
=
2\sqrt{\frac{8782389}{8760000}}
-1+\frac{20097}{8760000}
=
1.0048483690271541680\ldots.
\]

Then

\[
\boxed{
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{
438H_{\rm MT}-261/500
}{
438-\Phi_{438}(20097/20000)
}
=
0.6728525639567808470\ldots
}
\tag{1}
\]

This improves the WI-009 four-point value

\[
0.6728470197666888276\ldots
\]

by

\[
5.5441900920\ldots\times10^{-6}
\]

in proportion, i.e. about `0.0005544` percentage points.

The gain is small, but its evidence level is stronger than the larger public `0.673...` candidates that still depend on external finite certificates: no new numerical gap certificate is introduced here.

## 2. Exact trace--energy envelope

Let `G` be an `m x m` positive-semidefinite unit-diagonal Gram matrix with eigenvalues `lambda_i >= 0`. Put

\[
E=\operatorname{tr}(G-I)^2
=\sum_i(\lambda_i-1)^2,
\qquad
D=\mathcal D(G)=\sum_i\Psi(\lambda_i).
\]

Write `x_i=lambda_i-1`, so `x_i>=-1` and `sum_i x_i=0`. Let

\[
L=\{i:x_i>1\},\qquad
k=|L|,\qquad
R=\sum_{i\in L}x_i,\qquad
Q=\sum_{i\in L}x_i^2.
\]

Because the linear branch of `Psi(1+x)` replaces `x^2` by `2x-1` when `x>1`,

\[
\boxed{D=E+2R-k-Q.}
\tag{2}
\]

If `k=0`, then `D=E`. If `k=1`, with the exceptional coordinate `r>1`, Cauchy on the other `m-1` coordinates gives

\[
r\le\sqrt{\frac{m-1}{m}E},
\]

and therefore

\[
D\ge E+2r-1-r^2
\ge
2\sqrt{\frac{m-1}{m}E}-1+\frac{E}{m}.
\]

For `k>=2`, the same one-large-coordinate estimate applies after an exact compression. Write each large coordinate as

\[
x_i=1+z_i,\qquad z_i>0,
\]

and let

\[
Z=\sum_{i\in L}z_i=R-k.
\]

Replace the `k` large coordinates by

\[
1+Z,\underbrace{1,\ldots,1}_{k-1},
\]

leaving every other coordinate unchanged. The total sum is preserved. The defect is also preserved exactly: the original large-coordinate contribution is

\[
\sum_{i\in L}(2x_i-1)=k+2Z,
\]

whereas after compression it is

\[
(2(1+Z)-1)+(k-1)\Psi(2)=1+2Z+k-1=k+2Z.
\]

The energy cannot decrease. Before compression the large-coordinate contribution to `E` is

\[
k+2Z+\sum_{i\in L}z_i^2,
\]

and afterwards it is

\[
k+2Z+Z^2,
\]

with

\[
Z^2\ge\sum_{i\in L}z_i^2.
\]

Thus the transformed vector has the same `D`, the same zero-sum constraint, energy `E' >= E`, and at most one coordinate strictly above the threshold. Applying the already proved `k=0,1` case to the transformed vector and using monotonicity of `Phi_m` gives the global bound

\[
\boxed{D\ge\Phi_m(E)}.
\]

Here

\[
\Phi_m(E)=
\begin{cases}
E,&0\le E\le m/(m-1),\\
2\sqrt{(m-1)E/m}-1+E/m,&E\ge m/(m-1).
\end{cases}
\]

The function `Phi_m` is nondecreasing and 1-Lipschitz. Therefore, globally rather than only in the numerical range used below,

\[
\boxed{
E+P\ge A,\quad P\ge0
\Longrightarrow
D+P\ge\Phi_m(A).
}
\tag{3}
\]

Indeed,

\[
\Phi_m(A)\le\Phi_m(E+P)\le\Phi_m(E)+P\le D+P.
\]

This is the finite-dimensional trace--energy envelope used by the recent `tawanerguo-cn` and `trmdy` refinements. For the concrete application (1), `Phi_438(A)<2`; that observation gives a shorter numerical discharge of the multi-large-eigenvalue case, but it is not needed for the global statement (3).

## 3. The four-point certificate supplies block energy

Take `m` consecutive simple critical zeros with normalized ordinates

\[
y_1<\cdots<y_m
\]

and let `G` be their limiting Montgomery--Taylor Gram block. Write

\[
w(x)=|k_{\rm MT}(x)|^2.
\]

Since `G` has unit diagonal,

\[
E=\operatorname{tr}(G-I)^2
=
2\sum_{1\le i<j\le m}w(y_j-y_i).
\tag{4}
\]

Sum the Lean-proved four-point inequality over all `m-3` consecutive four-point windows inside the block. A pair separated by `r=1,2,3` indices is contained in at most `4-r` such windows, while its coefficient in `F_4` is exactly

\[
\frac{2}{4-r}.
\]

Thus its total coefficient after summation is at most `2`, exactly the coefficient available in (4). All other pair energies in (4) are nonnegative. If `P` denotes the summed nonnegative pressure term, this gives

\[
\boxed{
E+P\ge\varepsilon(m-3)=A.
}
\tag{5}
\]

No new prime-side moment appears in (5); it uses only the actual Gram geometry already present at bandwidth one.

There is also no hidden compactness assumption. If `P>=A`, (5) is automatic. If `P<A`, every internal gap appears in at least one four-point span, so

\[
P\ge p(y_m-y_1),
\]

and hence the normalized block span is bounded by `A/p`, a constant for fixed `m`. The compact-uniform Montgomery--Taylor kernel asymptotic already used in WI-009 therefore applies on precisely the blocks for which it is needed. Finite-`T` diagonal and endpoint errors contribute only `o(N)` for fixed `m`.

## 4. Window-in-frame averaging removes the old bridge loss

Pinching the full simple-zero Gram matrix into principal `m x m` blocks cannot increase the spectral convex functional `tr Psi`; equivalently,

\[
\mathcal D(M^\circ)
\ge
\sum_{\text{blocks}}\mathcal D(G_{\text{block}}).
\]

Apply (3) to each full block and then average over the `m` possible shifts of the block partition along the ordered simple zeros.

A fixed consecutive four-point window is wholly contained in a block for exactly

\[
m-3
\]

of those `m` shifts. Its pressure is `p` times its three-gap span. Globally, away from `O(1)` endpoints, each normalized adjacent gap is counted in three such spans. Therefore the averaged pressure tax is

\[
\frac{m-3}{m}\,\frac{3}{2500}\,N+o(N).
\]

At the same time, the averaged number of full `m`-blocks is `S/m+o(N)`. Equations (3)--(5) therefore give the global inequality

\[
\boxed{
\mathcal D(M^\circ)
\ge
\frac{\Phi_m(A)}{m}S
-
\frac{m-3}{m}\frac{3}{2500}N
-o(N).
}
\tag{6}
\]

Substituting (6) into the stability bridge and solving for `S/N` yields

\[
\boxed{
\frac SN
\ge
\frac{
mH_{\rm MT}-(m-3)(3/2500)
}{
m-\Phi_m(\varepsilon(m-3))
}
-o(1).
}
\tag{7}
\]

The integer optimization of (7) over `m>=4` has its maximum at `m=438`; the neighboring values decrease on both sides, and a direct scan through `m<5000` finds no larger value. The exact value at `m=438` is (1).

## 5. Why this does not contradict WI-010

WI-010 is an exact no-go for the specific `Zeta23Ext.Bridge.n_point_bound` formula, whose block cap and pressure ledger imply an `O(1/n)` gain ceiling as the local point count grows.

Equation (7) uses a different global assembly. It keeps the same local four-point certificate but replaces the old chord/cap conversion by the nonlinear trace--energy envelope and averages only windows actually lying inside each block. Therefore it can improve the `n=4` output of the old bridge without violating any inequality in WI-010.

The lesson is structural:

\[
\boxed{
\text{local Gram rigidity is not exhausted by the old sliding-window bridge;}\quad
\text{the global assembly itself contains recoverable slack.}
}
\]

This does not imply that increasing `n` indefinitely will now give a large gain. The recent external explorations report shallow ceilings for several related finite-horizon families, but those stronger ceiling claims remain below Mathia's evidence threshold until independently reconstructed.

## 6. Prior art and novelty assessment

The trace--energy envelope (2)--(3) and the window-in-frame pressure accounting are not claimed as new. They are explicitly described in `tawanerguo-cn/zeta-simple-zeros`, and `trmdy/zeta-simple-zeros-673137` records an independent re-derivation and applies them to its own externally certified seven-point data.

The public `teal-sea/zeta-lab` artifact, by contrast, currently applies its internally proved four-point certificate through the older `n_point_bound` bridge, producing WI-009's `0.672847019766...`. A search of the public artifacts and exact decimal did not locate the particular splice (7) with `four_point_cert` or the constant (1).

Accordingly the evidence claim here is deliberately narrow: the **new Mathia deduction** is to combine an already kernel-checked local certificate with an already published exact assembly to obtain a slightly stronger unconditional bound at the strongest currently available certificate evidence tier. No priority claim is made beyond that audit.

## 7. Adversarial checks and boundaries

Several failure modes were checked explicitly.

**Pair overcounting.** The coefficient `2/(4-r)` is designed so that at most `4-r` containing windows spend at most total weight `2` on a pair. Boundary pairs occur fewer times and only add slack.

**Pressure undercounting.** A gap can occur in fewer four-point windows only near the global endpoints; there are `O(1)` such losses for each fixed shift. They are absorbed by `o(N)`. Inside the averaged block frame, the exact containment count is `m-3`.

**Unbounded blocks.** Pressure itself bounds the block span whenever the kernel approximation is needed, as explained after (5); high-pressure blocks satisfy the target without any kernel approximation.

**Envelope compression.** Multiple eigenvalues above `2` do not create an uncovered branch. Concentrating their excess above the threshold into one eigenvalue preserves the spectral defect and trace constraint and can only increase the quadratic energy. The one-large-eigenvalue bound therefore implies the global envelope by monotonicity. At `m=438`, `Phi_438(A)<2` also supplies an independent shorter check for the actual operating point.

**Finite-`T` unit diagonal.** The simple-zero vectors have diagonal `1+o(1)` uniformly on bounded spans in the same truncation/tail regime as WI-009. Since `m` is fixed, normalization changes (6) by `o(1)` per block, hence `o(N)` globally.

**No unverified larger certificate.** Neither the `tawanerguo-cn` seven-point finite certificate nor the `trmdy` nine-point certificate is used. Only their exact assembly lemma is imported; the numerical local input is the Lean theorem `four_point_cert`.

A decisive falsification test is therefore finite and clear: formalize (3), including the excess-compression step, the pair/window counting behind (5), and the `m`-shift averaging behind (6) in the existing zeta-lab bridge and instantiate it with `four_point_cert`. Any failure would have to identify a missing analytic normalization or an error in one of these exact finite steps.

## 8. Consequence for the research line

The strongest rigorously discharged bandwidth-one numerical certificate in this line can be raised, without any new prime arithmetic, from

\[
0.6728470197666888\ldots
\quad\text{to}\quad
0.6728525639567808\ldots.
\]

More importantly, this demonstrates that WI-010's negative result should be read exactly at its stated scope: the bottleneck was partly the **assembly**, not merely the quality or size of the local certificate.

The next worthwhile zero-side question is therefore not just to search for a larger local `n`, but to identify the sharp global dual/variational formulation of `tr Psi(M)` under the ordered-gap Gram constraints. A useful formulation must first beat (7) on the already proved four-point input before expensive new finite certification is justified.
