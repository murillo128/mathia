# PF-068 — fixed prime tangents are spectrally essential but thermodynamically invisible

**Status:** `DECISIVE-NEGATIVE` for attempts to globalize the PF-034/PF-050 fixed-pattern signal by ordinary per-area / thermodynamic averaging. The abstract sparse-defect phenomenon is not new; the point here is the exact sieve-rate separation for the deterministic prime-flute.

## 1. Setup: a fixed recurrent prime tangent

Fix a finite exact offset pattern

\[
H=\{\eta_1<\cdots<\eta_r\},\qquad r\ge2,
\]

of the type used in PF-034: along an infinite subsequence of translations \(P\), all

\[
P+\eta_1,\ldots,P+\eta_r
\]

are prime and the block may additionally be required to be isolated by prime-free intervals on both sides. The isolation requirement only decreases the number of occurrences, so for upper bounds it can be ignored.

The associated cusp-side tangent \(Y_H\), its exact multi-gap lengths

\[
\sinh^2\frac{L_k}{4}
=
\frac{d_1+\cdots+d_{k-1}}{d_k},
\qquad d_i=\eta_{i+1}-\eta_i,
\]

and the local spectral measures of PF-050 are fixed once \(H\) is fixed. Equivalently, the relative distinguished-cuff data are fixed through

\[
\frac{d_i}{d_j}
=
\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_i(P)-\ell_j(P)}2\right].
\]

## 2. A fixed exact pattern has zero density among pants

Let

\[
A_H(x)
=
\#\{P\le x: P+\eta_i\text{ is prime for all }i\}.
\]

For a fixed admissible \(r\)-tuple, the Selberg sieve gives the standard upper bound

\[
\boxed{
A_H(x)\ll_H \frac{x}{(\log x)^r}.
}
\]

More precisely one may retain the singular series and a constant depending only on \(r\); the coarse form above is all that is needed here. Any consecutive-prime or isolation constraints inherited from Pintz only reduce \(A_H(x)\).

The number of prime-index pants up to scale \(x\) is

\[
N(x)=\pi(x)+O(1)\sim\frac{x}{\log x}.
\]

Therefore

\[
\boxed{
\frac{A_H(x)}{N(x)}
\ll_H
\frac1{(\log x)^{r-1}}
\longrightarrow0.
}
\]

Since every tight pair of pants has area exactly \(2\pi\), the same statement is a zero-area-density statement in the natural exhaustion of the flute.

The conclusion is unchanged if one attaches to each occurrence its full fixed tangent core or its separating collar. A two-sided maximal collar about a geodesic of length \(L\) has area

\[
2L\sinh w(L)
=
\frac{2L}{\sinh(L/2)}<4,
\]

so a fixed amount of tangent/collar geometry per occurrence still occupies \(o(\operatorname{Area})\).

## 3. PF-050 local spectral measures vanish under ordinary thermodynamic averaging

Let \(\psi_H\) be any fixed normalized compactly supported probe in the canonical core of \(Y_H\), and for each isolated occurrence \(P\) let \(\psi_P\) be its transplanted copy in the prime-flute, as in PF-050.

For any bounded Borel function \(F\), define the occurrence-averaged marked spectral observable in the exhaustion up to scale \(x\) by

\[
\mathcal M_{H,x}(F)
:=
\frac1{\operatorname{Area}X(x)}
\sum_{P\in\mathcal O_H(x)}
\langle\psi_P,F(\Delta_X)\psi_P\rangle,
\]

where \(\mathcal O_H(x)\) denotes the isolated occurrences and

\[
\operatorname{Area}X(x)=2\pi N(x)+O(1).
\]

Functional calculus gives

\[
|\langle\psi_P,F(\Delta_X)\psi_P\rangle|
\le \|F\|_\infty.
\]

Hence

\[
\boxed{
|\mathcal M_{H,x}(F)|
\le
\frac{\|F\|_\infty A_H(x)}{2\pi N(x)+O(1)}
=
O_H\!\left((\log x)^{1-r}\right)
\longrightarrow0.
}
\]

The same proof works for any fixed finite family of probes, residues, small modes, or other uniformly bounded local spectral observables attached to each occurrence of \(H\).

Thus the local spectral measure whose pointed limit recovers the prime-derived tangent in PF-050 becomes invisible if one first performs the most natural global operation: averaging per unit area along the flute.

## 4. Essential spectrum and spectral density are sharply different notions here

PF-034/PF-050 use the **infinitude and spatial escape** of recurrent occurrences to construct Weyl sequences. Therefore a fixed tangent eigenvalue can satisfy

\[
\lambda_H\in\sigma_{\rm ess}(\Delta_X)
\]

although the occurrences producing it have zero density.

PF-068 therefore exhibits the deterministic prime-flute version of a familiar sparse-defect phenomenon:

\[
\boxed{
\text{spectrally essential}
\quad\not\Rightarrow\quad
\text{positive thermodynamic density}.
}
\]

For the program this distinction matters. The prime-specific signals found in the tangent/local-measure branch survive in the **support/limit-point structure** of the global operator, but every fixed exact pattern contributes zero mass to an ordinary per-area average.

## 5. Consequence for IDS, normalized traces and thermodynamic determinants

This rules out the following route for a fixed tangent fingerprint:

\[
\boxed{
\text{PF-034/PF-050 fixed pattern }H
\to
\text{ordinary finite-volume / per-area averaging}
\to
\text{nonzero atom or density carrying }H.
}
\]

Any normalized spectral statistic whose contribution from each fixed occurrence is uniformly \(O(1)\) loses that pattern at rate at least

\[
(\log x)^{1-r}.
\]

In particular, simply taking larger finite truncations and dividing a low-energy counting statistic, bounded functional trace, or finite-pattern spectral response by area cannot turn the local tangent data into a macroscopic spectral density.

This statement deliberately does **not** claim that a global integrated density of states exists for the collapsing infinite flute; standard spectral-convergence theorems often require non-collapsing/bounded-geometry hypotheses that the prime-flute violates. Nor does it claim that every possible normalized heat/Selberg trace is controlled: PF-036 shows that iterates of very short orbits create additional nonlocal divergences.

The negative result is narrower and robust: **the particular prime-specific information carried by any fixed exact recurrent tangent has zero thermodynamic weight.**

## 6. Why summing over moving patterns is a different problem

One could try to compensate by summing over many patterns \(H=H(x)\) whose number grows with the exhaustion. PF-068 does not rule that out. But then the observable no longer tracks a fixed geometric/spectral fingerprint; it becomes an ensemble statistic of the distribution of prime gaps or prime constellations.

That may be mathematically interesting, but without an additional geometric principle it risks becoming precisely the kind of restatement of prime-gap statistics that the prime-flute program is trying to avoid.

The result therefore reinforces the methodological split already visible after PF-036 and PF-064:

\[
\boxed{
\text{spatial localization first}
\;\text{retains prime-pattern data},
}
\]

whereas

\[
\boxed{
\text{thermodynamic/global averaging first}
\;\text{erases every fixed pattern}. 
}
\]

## 7. Novelty check

The number-theoretic input is classical: the Selberg sieve gives \(A_H(x)\ll_H x/(\log x)^r\) for any fixed admissible \(r\)-tuple. The spectral principle that density-zero defects can affect essential spectrum while disappearing from an integrated density of states is also familiar in operator and graph theory; novelty is not claimed for that abstract phenomenon.

Likewise, modern Benjamini--Schramm / Plancherel spectral-convergence results for large hyperbolic surfaces show how geometric sets of vanishing relative volume disappear from normalized spectral measures, but those theorems generally impose hypotheses (for example systolic/non-collapsing conditions in many formulations) that are not available for this flute.

The substantive conclusion specific to the present construction is the exact combination

\[
\boxed{
\text{fixed prime tuple sieve rate}
+
\text{area }2\pi\text{ per flute pant}
+
\text{PF-034 essential-spectrum embedding}
+
\text{PF-050 local spectral recovery}.
}
\]

It closes a natural globalization branch without assuming an IDS theorem that is unavailable in the collapsing geometry.

## Research consequence

Do not try to convert the successful fixed-tangent/local-spectral-measure channel into an RH mechanism merely by averaging it over longer and longer portions of the flute. Any genuinely global prime-sensitive object must either

1. retain spatial labels/localization;
2. apply a non-uniform weighting canonically forced by geometry; or
3. discover a collective law involving a growing family of tangent types that contains information beyond ordinary prime-gap statistics.
