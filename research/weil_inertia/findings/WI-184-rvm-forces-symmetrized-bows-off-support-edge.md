# WI-184 — Riemann--von Mangoldt forces long symmetrized bows off the support-one edge

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`. This finding corrects one load-bearing specialization in WI-183 without weakening the Maynard--Pratt prior-art obstruction itself. Maynard--Pratt's Section 8 bow is a one-sided schematic sequence with ordinate step `c/log T`, `c>0`. WI-183 specialized that free model parameter to `c=2π` so that the right-half bow lands on the unit unfolded lattice. That specialization is algebraically legitimate for the schematic one-sided model, but it is **not compatible with a long actual-zeta realization after the compulsory same-ordinate functional-equation reflection is included**. The classical Riemann--von Mangoldt zero count forces

\[
\boxed{c\ge 4\pi-o(1)}
\]

for any such symmetrized bow containing `m\gg\log T` right-half labels. If the bow plus its mirrors accounts for all but `o(m)` of the zero count in its vertical span, including multiplicity, then necessarily

\[
\boxed{c=4\pi+o(1).}
\]

Consequently the first reciprocal frequency of a source-compatible symmetrized bow is at `alpha<=1/2`, not at the support-one endpoint `alpha=1`. At the count-saturating spacing `c=4π`, the mirror-pair contribution is exactly phase coherent at `alpha=1/2` even when the horizontal depth varies arbitrarily along the bow. Thus slow horizontal drift remains a genuine obstruction to the Maynard--Pratt local power-sum detector, but it does **not** by itself reproduce the endpoint Poisson screening geometry used in WI-115/WI-183. For the support-one Weil/form-factor route, the remaining obstruction is extraction against the rest of the zeta amplitude.

## 1. Primary-source bow and the compulsory mirror population

Maynard and Pratt, *Half-Isolated Zeros and Zero-Density Estimates*, IMRN 2024:19 (2024), 12978--13014, Section 8, define a potential bad configuration whose ordinates lie in an arithmetic progression and whose real parts rise smoothly from `1/2`, remain near `3/4`, and return. Their displayed model (8.1) has

\[
\gamma_j=T_0+\frac{cj}{\log T},
\qquad 1\le j\le m,
\qquad m=T^\varepsilon,
\qquad T_0\asymp T,
\tag{1}
\]

with fixed `c>0`. They use it to explain why their local power-sum detector can see essentially the same Poisson cancellation as on a vertical arithmetic progression, while their global cluster argument gains too little on a cluster of length `T^\varepsilon`. This is prior art and remains the correct source-level warning.

For an actual zeta zero `rho=beta+i gamma` with `beta>1/2`, however, the functional equation and conjugation force

\[
1-\overline\rho=(1-\beta)+i\gamma
\tag{2}
\]

at the **same positive ordinate**. Therefore every off-line right-half label in (1) contributes a distinct reflected zero in the same ordinate interval. In Maynard--Pratt's displayed bow all but `O(1)` labels are off the critical line, so a realization with `m` right-half bow labels contributes at least

\[
\boxed{2m-O(1)}
\tag{3}
\]

nontrivial zeros, counted with multiplicity, across the same vertical span. Any multiplicity greater than one can only increase this count.

This observation does not assert that Maynard--Pratt claimed every value of `c` gives a globally admissible zeta configuration. Their bow is explicitly a potential/schematic obstruction. The correction is to WI-183's later use of the particular value `c=2π` as though it remained source-compatible after symmetrization.

## 2. Riemann--von Mangoldt gives the sharp spacing gate

Let `L=log T` and let

\[
H:=\gamma_m-\gamma_1
=\frac{c(m-1)}{L}.
\tag{4}
\]

The Riemann--von Mangoldt formula, uniformly for endpoints `asymp T`, is

\[
N(t)=\frac{t}{2\pi}\log\frac{t}{2\pi e}+O(\log t).
\tag{5}
\]

For `H=o(T)` this gives

\[
N(T_0+H)-N(T_0)
=\frac{H}{2\pi}L
+O\!\left(H+\frac{H^2}{T}+L\right).
\tag{6}
\]

Substituting (4), and assuming only `m/L\to\infty` and `m=o(T)` (both hold for Maynard--Pratt's `m=T^\varepsilon` with fixed small `\varepsilon>0`), yields

\[
\boxed{
N(T_0+H)-N(T_0)
=\left(\frac{c}{2\pi}+o(1)\right)m.
}
\tag{7}
\]

Comparison with the compulsory mirror count (3) gives

\[
2m-O(1)
\le
\left(\frac{c}{2\pi}+o(1)\right)m,
\]

hence

\[
\boxed{c\ge4\pi-o(1).}
\tag{8}
\]

For fixed `c`, every sufficiently long source-compatible symmetrized bow therefore has `c>=4π`.

The bookkeeping can be made precise without conflating other zeros with multiplicity. Let `r_c=O(1)` be the number of selected bow labels on the critical line, so one compulsory copy of the bow together with one copy of each distinct mirror contributes the baseline

\[
B_I=2m-r_c=2m+O(1).
\]

Define the **excess zero-count budget**

\[
E_I:=N_I-B_I\ge0,
\]

where `N_I` counts all zeta zeros in the bow interval with multiplicity. Thus `E_I` includes both extra multiplicity at selected bow/mirror points and all other zero labels in the interval. Equations (7)--(8) give

\[
\boxed{
E_I
=\left(\frac{c}{2\pi}-2+o(1)\right)m.
}
\tag{9}
\]

This yields a sharp count dichotomy:

- `c<4π`: impossible for a long symmetrized actual-zeta bow;
- `c=4π+o(1)`: the compulsory bow/mirror count may asymptotically saturate the local zero count, so `E_I=o(m)`;
- fixed `c>4π`: there is a positive-density **excess zero-count budget** `(c/(2π)-2+o(1))m`.

The last case does **not** by itself force that excess to be a distinct complementary population. It may be realized by extra multiplicity at selected points, by additional critical-line zeros, by further off-line pairs, or by a mixture. If the selected bow and mirror points are simple, then (9) does become the asymptotic count of other zeros in the interval. This separation is essential for the `weil_inertia` mandate.

## 3. Count compatibility moves the reciprocal alias into the lower half of support

Use the standard unfolded ordinate

\[
x=\gamma\frac{L}{2\pi}.
\tag{10}
\]

The bow step becomes

\[
d:=x_{j+1}-x_j=\frac{c}{2\pi}.
\tag{11}
\]

A vertical arithmetic progression of spacing `d` has reciprocal frequencies `alpha=k/d`. Its first positive reciprocal frequency is therefore

\[
\alpha_*:=\frac1d=\frac{2\pi}{c}.
\tag{12}
\]

The spacing gate (8) gives immediately

\[
\boxed{0<\alpha_*\le\frac12+o(1).}
\tag{13}
\]

At the count-saturating value `c=4π`, one has exactly

\[
d=2,
\qquad
\alpha_*=\frac12.
\tag{14}
\]

This is the opposite of the endpoint-screening specialization in WI-183. The `c=2π` formal bow has `d=1` and first reciprocal alias `alpha=1`, where support-one tapers can vanish; but after source symmetry and the mean zero count are enforced, such a long bow would contain roughly twice as many zeros as Riemann--von Mangoldt permits. The source-compatible reciprocal line is instead at or below `1/2`, inside the unconditional support-one band used in WI-124.

## 4. Horizontal drift does not dephase the selected mirror-pair alias

The stronger fact is that varying horizontal depth does not destroy coherence at (12). Use the WI-124 horizontal variable

\[
b_j=(\beta_j-\tfrac12)L.
\tag{15}
\]

For an off-line pair at ordinate `x_j`, the reciprocal-amplitude contribution at frequency `alpha` is

\[
e^{b_j\alpha+2\pi i x_j\alpha}
+
e^{-b_j\alpha+2\pi i x_j\alpha}
=
2\cosh(b_j\alpha)e^{2\pi i x_j\alpha}.
\tag{16}
\]

Write `x_j=x_0+dj`. At `alpha=alpha_*=1/d`,

\[
e^{2\pi i x_j\alpha_*}
=e^{2\pi i x_0\alpha_*}e^{2\pi i j}
=e^{2\pi i x_0\alpha_*}.
\tag{17}
\]

Hence the selected symmetrized bow contributes

\[
\boxed{
A_{\rm bow}(\alpha_*)
=
e^{2\pi i x_0\alpha_*}
\sum_{j\in J_{\rm off}}2\cosh(b_j\alpha_*)
+ A_{\rm crit}(\alpha_*),
}
\tag{18}
\]

where any critical-line endpoint labels carry the same vertical phase. In particular, after fixing the harmless common phase, every mirror pair contributes a **positive real** amount. The depth sequence may ramp, plateau, or drift arbitrarily; no horizontal-depth variation can create internal phase cancellation at the reciprocal line. Extra multiplicity at one of these selected points merely repeats the same-phase contribution and therefore strengthens, rather than cancels, this selected amplitude.

For `c=4π`, (18) is a coherent selected witness exactly at `alpha=1/2`. For fixed `c>4π`, the witness lies even deeper inside support, at `alpha_*<1/2`, while (9) simultaneously requires a positive-density excess zero-count budget. Only the part of that excess represented by genuinely additional phases can act as a cancellation reservoir; multiplicity on the selected bow cannot.

This directly matches the finite-period rigidity of WI-124: a density-one period-2 cell containing one same-ordinate mirror pair has its forced first-half Bragg alias at `alpha=1/2`. Equation (18) shows that exact periodicity of the horizontal depths is unnecessary for phase coherence along the vertical AP; slow bow drift changes amplitudes through `cosh`, not phases.

## 5. What this does and does not rule out

The result rules out a specific attempted identification:

\[
\text{long source-compatible symmetrized bow}
\not\equiv
\text{unit unfolded screening lattice at }\alpha=1.
\tag{19}
\]

Accordingly, WI-183's `c=2π` endpoint-screening specialization must be read only as a formal one-sided local model before global zeta symmetry/count compatibility is imposed. The broader Maynard--Pratt conclusion survives: their short zero-detecting power sums can still be defeated by slowly drifting locally arithmetic chains, and no theorem here excludes bows from zeta.

Nor does (18) by itself give a new unconditional simple-critical proportion or RH. WI-124 already isolates the load-bearing gap: the complete Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh form factor is a square of the **full** zeta amplitude. A large coherent amplitude from a selected bow can be canceled by the rest of the zeta amplitude before the square is formed. Equation (9) sharpens the local bookkeeping but does not solve extraction. If `c>4π`, a positive-density excess count is required, yet that excess need not consist of distinct cancelling zeros; if `c=4π`, no positive-density excess is forced by count, but zeros outside the short bow interval can still enter a global form-factor amplitude unless one proves a localization/extraction theorem.

Thus slow horizontal drift is not the missing spectral detector by itself. Once symmetry and Riemann--von Mangoldt are imposed, the reciprocal witness is already present in the lower half of support. The remaining RH-facing task is to **extract** that selected witness, or to prove that any genuinely phase-opposed cancellation reservoir capable of neutralizing it incurs another independently source-controlled cost.

## 6. Prior-art audit and provenance

The bow construction, its local Poisson-cancellation motivation, and the statement that it obstructs the Maynard--Pratt zero-detection program are from James Maynard and Kyle Pratt, **Half-Isolated Zeros and Zero-Density Estimates**, *International Mathematics Research Notices* 2024:19 (2024), 12978--13014, DOI `10.1093/imrn/rnae191`, arXiv:2206.11729v2, especially Section 8 and equation (8.1). Their paper explicitly takes `c>0` as an absolute constant in the schematic bow. No claim is made here that they asserted every such `c` is globally realizable after functional-equation symmetrization.

The zero-count input is the classical Riemann--von Mangoldt formula. For a modern explicit version, see Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, **Counting zeros of the Riemann zeta function**, *Journal of Number Theory* 235 (2022), 219--241, DOI `10.1016/j.jnt.2021.06.032`, which proves an explicit `O(log T)` error bound. Functional-equation/conjugation symmetry of zeta zeros is classical.

WI-124 is prior local work for the exact lower-half reciprocal-alias consequence of same-ordinate mirror symmetry in a density-one finite-period cell. WI-121/WI-122 show why raw zero-count regularity alone is insufficient against compensated motifs, and WI-115 records endpoint alias screening on the true unit unfolded lattice. The new durable delta here is the **joint** use of classical zero count plus compulsory mirror multiplicity to fix the admissible bow spacing and hence move its reciprocal alias away from the support edge.

A targeted search around Maynard--Pratt bows, functional-equation reflection, Riemann--von Mangoldt spacing, and reciprocal/Bragg aliases located the primary bow paper and standard zero-count references but no source spelling out the implication (8)--(18). Absence from that search is not evidence of priority, and no priority claim is made.

## 7. Research implication

The source-control hierarchy should be revised as follows. Maynard--Pratt bows remain a canonical adversarial geometry for **local zero-detecting Dirichlet polynomials**, but they are not a new endpoint-screened adversary for the support-one Weil/form-factor interface once the actual zeta symmetries and mean count are enforced. A long symmetrized bow must either sit at essentially spacing `4π/log T`, where its selected mirror amplitude is coherent at `alpha=1/2`, or use a larger spacing and carry a positive-density excess zero-count budget. The latter budget must remain split into multiplicity versus genuinely additional zero labels; only the latter can supply new cancellation phases.

This shifts the next decisive question from “which local observable sees slow horizontal drift?” to

\[
\boxed{
\text{Can the lower-half reciprocal amplitude of a symmetrized bow be localized/extracted,}
\\
\text{or can every genuinely cancelling reservoir be charged by an independent zeta-source invariant?}
}
\tag{20}
\]

That question is compatible with the canonical `weil_inertia` mandate: it keeps multiplicity, distinct exceptional population, and proof slack separate, and it seeks a defect-to-zero mechanism rather than another percentage-only refinement.