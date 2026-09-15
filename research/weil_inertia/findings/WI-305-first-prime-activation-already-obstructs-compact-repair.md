# WI-305 — The compact-repair obstruction already starts at the first prime threshold

**Status:** `EXACT-DERIVED + CLASSICAL-INEQUALITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`.

WI-304 extracted from Vincent Liu's source-exact localization an atomwise obstruction criterion: if an individually isolatable active prime-power atom `q` leaves defect weight

\[
w_q=\frac{\Lambda(q)}{\sqrt q}\bigl(1-\rho_\chi(\log q)\bigr)
\]

larger than the high-frequency reserve `beta_0=1/16`, then the tail-dropped comparison cannot be made positive by any fixed compact self-adjoint correction. Liu's manuscript proves this at `q=8`, where support alone gives `rho_chi(log 8)=0`, and therefore obtains the threshold `L>log(8)/2`.

The support condition on the localizer gives substantially more information before `log 8`. A classical numerical-radius bound for nilpotent operators controls `rho_chi(log 2)` uniformly over **every** normalized real localizer `chi in C_c^infty((-1,1))`. It implies that the `q=2` atom already exceeds the reserve as soon as it becomes active. Hence the same tail-dropping architecture is compact-repair-obstructed for every

\[
\boxed{L>\frac{\log2}{2}.}
\]

This is the first arithmetically possible threshold: below it no von-Mangoldt atom is active. Thus `log 8 / 2` is not the intrinsic onset of Liu's compact-repair obstruction; it is only the first threshold at which the source proof can set the localizer autocorrelation to zero by disjoint support without using a sharper operator inequality.

This finding concerns only the specified bounded tail-dropped comparison. It does **not** give a negative test for the full Weil form, does not contradict tail-preserving positivity, and does not upgrade or downgrade Liu's unreplayed `17/16` certificate.

## 1. Source-exact atomwise criterion

Retain the notation and normalization checked in WI-302--WI-304. For a real normalized

\[
\chi\in C_c^\infty((-1,1)),\qquad \|\chi\|_2=1,
\]

put

\[
\rho_\chi(x)=\int_{\mathbb R}\chi(v+x)\chi(v)\,dv.
\]

Liu's localization defect contains, for every active prime power `q` with `log q<2L`, the discrete term

\[
c_q\bigl(1-\rho_\chi(\log q)\bigr)H_f(\log q),
\qquad
c_q=\frac{2\Lambda(q)}{\sqrt q}.
\]

The localized comparison has high-frequency reserve

\[
\frac{\mathcal M_\chi(f_k)}{\|f_k\|^2}\longrightarrow
\beta_0,
\qquad
\beta_0=\frac1{16},
\]

on the weakly-null modulations used in Liu's obstruction theorem. WI-304 shows that if the atom at `a=log q` is individually isolatable, then varying the modulation phase gives

\[
[\beta_0-w_q,\,\beta_0+w_q]
\subseteq W_e(\mathcal D_\chi),
\]

where

\[
w_q
=\frac{\Lambda(q)}{\sqrt q}
\bigl(1-\rho_\chi(\log q)\bigr).
\tag{1}
\]

Consequently

\[
w_q>\beta_0
\quad\Longrightarrow\quad
\mathcal D_\chi+K\not\succeq0
\tag{2}
\]

for every fixed compact self-adjoint `K`. The remaining question is therefore quantitative: how large can the localizer autocorrelation be at the first prime lag?

## 2. Compact support makes translation nilpotent

Let

\[
H=L^2((-1,1))
\]

and, for `0<a<2`, let `S_a` be translation by `a` followed by compression back to `(-1,1)`, with functions extended by zero outside the interval. Then `||S_a||<=1`. Moreover,

\[
S_a^m=0
\qquad\text{whenever}\qquad ma\ge2.
\tag{3}
\]

Indeed `S_a^m` is compression of translation by `ma`, and two intervals of length `2` separated by at least `2` have only null overlap. If

\[
m(a):=\left\lceil\frac2a\right\rceil,
\]

then `S_a^{m(a)}=0`.

For normalized real `chi`, up to the harmless choice of translation orientation,

\[
\rho_\chi(a)=\langle\chi,S_a\chi\rangle.
\tag{4}
\]

Haagerup and de la Harpe proved the sharp classical nilpotent numerical-radius inequality

\[
T^m=0
\quad\Longrightarrow\quad
w(T)\le \|T\|\cos\frac{\pi}{m+1},
\qquad m\ge2.
\tag{5}
\]

Applying (5) to `S_a` and using (4) gives the localizer-independent support bound

\[
\boxed{
\rho_\chi(a)
\le
\left|\rho_\chi(a)\right|
\le
\cos\frac{\pi}{m(a)+1}
\qquad(0<a<2).
}
\tag{6}
\]

For `a>=2`, disjoint support simply gives `rho_chi(a)=0`. Thus compact support supplies a quantitative autocorrelation loss at every nonzero shift, not merely the all-or-nothing vanishing used at `log 8` in Liu's proof.

Equation (6) also gives a general lower bound for every active atom with `log q<2`:

\[
\boxed{
w_q\ge
\frac{\Lambda(q)}{\sqrt q}
\left(
1-
\cos\frac{\pi}{\lceil2/\log q\rceil+1}
\right).}
\tag{7}
\]

Only the `q=2` instance is needed for the threshold theorem below.

## 3. The first prime atom already overwhelms the reserve

Take

\[
a=\log2.
\]

Since

\[
2a<2<3a
\]

(the second inequality is `log 8>2`), one has

\[
S_a^3=0.
\]

Equation (5) therefore yields

\[
\boxed{
\rho_\chi(\log2)\le\cos\frac\pi4=\frac1{\sqrt2}.}
\tag{8}
\]

For the prime `q=2`, equation (1) becomes

\[
w_2
=\frac{\log2}{\sqrt2}
\bigl(1-\rho_\chi(\log2)\bigr),
\]

and hence

\[
\boxed{
w_2\ge
\frac{\log2}{\sqrt2}
\left(1-\frac1{\sqrt2}\right).}
\tag{9}
\]

No floating-point comparison is needed. Using the elementary rational inequalities

\[
\log2>\frac23,
\qquad
\frac75<\sqrt2<\frac32,
\]

we obtain

\[
\frac1{\sqrt2}>\frac23,
\qquad
1-\frac1{\sqrt2}>\frac27,
\]

so

\[
\boxed{
w_2>\frac23\cdot\frac23\cdot\frac27
=\frac8{63}
>\frac1{16}=\beta_0.}
\tag{10}
\]

In particular the lower end of the essential numerical-range interval satisfies the explicit rational estimate

\[
\beta_0-w_2
<\frac1{16}-\frac8{63}
=-\frac{65}{1008}<0.
\tag{11}
\]

Thus the margin is not a near-equality effect.

## 4. Exact first-threshold no-go theorem

The `q=2` atom is active exactly when

\[
\log2<2L,
\qquad\text{i.e.}\qquad
L>\frac{\log2}{2}.
\tag{12}
\]

For every such `L`, the atom is individually isolatable in the sense of WI-304. Choose two equal smooth bumps around `+-log2/2` with radius smaller than `L-log2/2`, smaller than `log2/4`, and smaller than a fixed fraction of `log3-log2`. Their autocorrelation is then supported only near `0,+-log2` among the active logarithmic atoms. Hence the WI-304 phase construction applies to `q=2`.

Combining (2), (10), and (12) gives:

> **First-prime compact-repair obstruction.** For every real normalized `chi in C_c^infty((-1,1))`, every `L>log2/2`, and every fixed compact self-adjoint operator `K` on `L^2((-L,L))`, Liu's tail-dropped bounded comparison satisfies
> \[
> \boxed{\mathcal D_\chi+K\not\succeq0.}
> \tag{13}
> \]

There is no earlier arithmetic threshold to test. If `L<=log2/2`, then `log n<2L` contains no prime-power logarithm at all. Therefore, within this source-exact localization family and its fixed high-frequency reserve, compact after-the-fact repair fails **immediately when the first discrete arithmetic channel enters**.

## 5. What changes in the interpretation of the `q=8` obstruction

Liu's `q=8` choice is structurally natural because `log8>2`, so `supp rho_chi subset(-2,2)` gives

\[
\rho_\chi(\log8)=0
\]

without optimizing the localizer. But the vanishing of the autocorrelation is stronger than necessary. The atomwise criterion only asks whether the residual coefficient beats `beta_0`; equations (8)--(10) show that the unavoidable overlap loss at `log2` already does.

Accordingly, the useful architecture boundary is sharper than the one suggested by the source's explicit example:

\[
\boxed{
\text{first active prime channel}
\Longrightarrow
\text{essential negative band for the tail-dropped comparison}
\Longrightarrow
\text{no fixed compact repair}.}
\tag{14}
\]

This reinforces WI-303's distinction between **noncompact source-exact retention** and finite-rank/compact certificate design. Past `log2/2`, a successful localization of this type must retain or replace enough noncompact information to survive the same weakly-null sequence; merely changing a finite set of trial directions or adding a compact correction cannot restore positivity.

The theorem does not say that every prime channel must be retained separately, nor that the full infinite arithmetic tail is mandatory. It only proves that the tail-dropped comparison already has an essential negative obstruction at the first channel, uniformly over the permitted localizer.

## 6. Prior-art and novelty audit

The ingredients are individually established. Liu's frozen manuscript supplies the exact defect identity, the high-frequency reserve `beta_0=1/16`, the weakly-null compact-repair argument, and the explicit `q=8` obstruction. WI-304 extracted from that source the arbitrary-isolatable-atom coefficient criterion and its essential numerical-range formulation.

The numerical-radius estimate (5) is classical: Uffe Haagerup and Pierre de la Harpe, **The Numerical Radius of a Nilpotent Operator on a Hilbert Space**, *Proceedings of the American Mathematical Society* **115** (1992), no. 2, 371--379, DOI `10.1090/S0002-9939-1992-1072339-6`. No novelty is claimed for this operator inequality or for compressed translations becoming nilpotent on a bounded interval.

A targeted audit of Liu's frozen manuscript found no use of the Haagerup--de la Harpe inequality and no optimization of the obstruction threshold below `log8/2`. The local `weil_inertia` corpus already uses `log2` support packing in a different first-crossing/screening problem (WI-281), but that result concerns a hypothetical one-signed Suzuki null mode and does not bound the autocorrelation of Liu's localizer or the essential numerical range of this tail-dropped comparison. The present line-local deduction is the composition of the source-exact atomwise obstruction with the sharp nilpotent numerical-radius control. No priority claim is made.

### Primary sources

- Vincent Liu, **Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function**, frozen source commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`, especially the localization defect identity and Obstruction Theorem.
- Uffe Haagerup and Pierre de la Harpe, **The Numerical Radius of a Nilpotent Operator on a Hilbert Space**, *Proc. Amer. Math. Soc.* 115 (1992), 371--379.

### Validation boundary

The proof above is exact once the source-exact defect/high-frequency identities of Liu and the atomwise reduction of WI-304 are fixed. No numerical spectral computation enters. The conclusion is only about Liu's specified **tail-dropped bounded comparison plus a fixed compact self-adjoint correction**. The full Weil form satisfies `Q=D_chi+S_chi` with omitted nonnegative/noncompact information that can compensate the defect, so (13) is not a negative Weil test and is not evidence against RH. It also does not promote Liu's `17/16` computer-assisted theorem claim beyond the independent-replay boundary recorded in WI-302.