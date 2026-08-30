# PF-115 — the all-composite shift clone has the same Gromov-hyperbolicity class

**Status:** `LITERATURE+DERIVED + NEGATIVE/BOUNDARY`. Portilla--Rodríguez--Tourís' stability theorem for trains/flute surfaces is classical. The project-specific consequence is that the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1` are Gromov hyperbolic simultaneously. This does **not** decide whether either surface is Gromov hyperbolic, and it does not imply quasi-isometry, quasiconformal equivalence, compact relative resolvent, scattering equivalence, or any RH statement.

## Claim

Let `X` be the exact zero-twist tight prime flute, with distinguished cuffs of lengths

\[
\ell_1,\ell_2,\ldots,
\]

and let `X^+` be the exact all-composite shift clone of PF-106, obtained from the labels `p_n+1` and normalized by the hyperbolic translation `z -> z-1`, with corresponding cuff lengths

\[
\ell_1^+,\ell_2^+,\ldots.
\]

Then

\[
\boxed{
X\text{ is Gromov hyperbolic}
\quad\Longleftrightarrow\quad
X^+\text{ is Gromov hyperbolic}.}
\tag{1}
\]

More quantitatively, if one of the two surfaces is `delta`-hyperbolic, then the other is `delta'`-hyperbolic for a constant depending only on `delta` and on

\[
\sup_n |\ell_n^+-\ell_n|.
\tag{2}
\]

The point is not the value of the hyperbolicity constant. Equation (1) says that the global binary invariant "Gromov hyperbolic or not" cannot distinguish the exact prime geometry from this all-composite control.

## 1. Bridge from tight flutes to the train coordinates

Portilla--Rodríguez--Tourís work with a train `Omega`, a Denjoy domain whose Poincaré metric is encoded by two sequences. Their `n`-th fundamental geodesic has length `2 l_n`, and their `n`-th second fundamental geodesic has length `2 r_n`. A flute surface is exactly the train in which each second fundamental geodesic degenerates to a puncture, so

\[
r_n=0\qquad\text{for every }n.
\tag{3}
\]

For a zero-twist tight flute presented as an infinite chain of one-cusp pairs of pants, the fundamental geodesics are the successive separating cuffs. Thus, up to the harmless indexing convention at the finite initial end,

\[
2l_n=\ell_n,
\qquad
2l_n^+=\ell_n^+,
\qquad
r_n=r_n^+=0.
\tag{4}
\]

This is also an intrinsic way to justify the train model here: a one-cusp hyperbolic pair of pants is determined by its two finite boundary lengths, and zero-twist gluing along the successive boundaries is determined by the same cuff sequence. Hence the train with data `(l_n=ell_n/2,r_n=0)` realizes the same marked zero-twist tight-flute metric, and likewise for the clone.

No Euclidean placement of the Denjoy intervals is imported as extra prime data in this step.

## 2. The shift clone is a bounded perturbation of the fundamental lengths

PF-107 proves the asymptotic law

\[
\ell_n^+-\ell_n
=
\frac{2}{p_{n-1}}+o(p_{n-1}^{-1}).
\tag{5}
\]

In particular,

\[
|\ell_n^+-\ell_n|\longrightarrow0.
\tag{6}
\]

After absorbing the finite initial segment,

\[
\boxed{
C:=\sup_n|\ell_n^+-\ell_n|<\infty.}
\tag{7}
\]

Equations (3)--(4) therefore give

\[
|r_n^+-r_n|=0,
\qquad
|l_n^+-l_n|\le C/2
\quad\text{for every }n.
\tag{8}
\]

Notice that this uses only the boundedness consequence of PF-107. Its sharper `ell^2 \setminus ell^1` additive cuff statement and the later collar/seam summability results are not needed.

## 3. Portilla--Rodríguez--Tourís stability applies directly

Theorem 3.8 of Portilla--Rodríguez--Tourís states that if two trains have fundamental and second-fundamental half-length data satisfying

\[
|l_n'-l_n|\le c,
\qquad
|r_n'-r_n|\le c
\tag{9}
\]

for every `n`, then one train is Gromov hyperbolic if and only if the other is. Their theorem is quantitative: a hyperbolicity constant for the second train is controlled only by the first constant and `c`.

Applying the theorem with (8) proves (1).

A useful feature of the source theorem is that it is genuinely weaker than a quasi-isometry hypothesis. The authors explicitly note that bounded perturbations of these length coordinates can preserve Gromov hyperbolicity even for pairs of trains that are not quasi-isometric. Thus (1) must **not** be upgraded to a quasi-isometry statement.

## 4. Consequence for the prime-flute program

PF-105--PF-114 progressively test whether the exact cotangent prime flute can remain operator-theoretically distinguishable from an all-composite surface despite extremely small local geometric defects. PF-115 adds the first clean global coarse invariant to that control family:

\[
\boxed{
\text{exact prime flute}
\quad\text{and}\quad
\text{exact }(p_n+1)\text{ all-composite clone}
\text{ have the same Gromov-hyperbolicity class}.}
\tag{10}
\]

Therefore a route of the form

\[
\text{prime-gap fluctuations}
\longrightarrow
\text{Gromov hyperbolicity/non-hyperbolicity of the flute}
\longrightarrow
\text{RH-specific spectral mechanism}
\]

cannot be primality-specific: the first global yes/no output is unchanged after replacing every prime label by an even composite label while keeping the exact cotangent construction.

This is stronger than merely observing that local cross-ratios or pointed tangents are close. The source theorem is a global stability statement about the entire infinite metric space. But it is still a **coarse** statement. It leaves untouched the accepted relative-operator question: compactness, essential spectral comparison, scattering, or a finer nonlocal invariant could in principle distinguish two surfaces with the same Gromov-hyperbolicity class.

## 5. What this does not decide

The finding deliberately does not determine the actual value of the common binary invariant. The prime cuff sequence

\[
\ell_n\sim2\log\frac{4p_n}{g_n}
\]

has large gap-driven fluctuations, so the simpler monotonic or quasi-increasing special cases of the train criteria cannot be imported without a separate proof. Equation (1) remains valid regardless of which side of the Gromov-hyperbolicity dichotomy the exact prime flute occupies.

Nor does Theorem 3.8 imply any of the following:

1. `X` and `X^+` are quasi-isometric;
2. they are quasiconformally or asymptotically isometrically equivalent;
3. a common-manifold metric comparison tends to the identity;
4. their relative resolvent is compact or belongs to a Schatten class;
5. their essential spectra, resonances, scattering matrices, Patterson--Sullivan data, or determinants agree.

Those are strictly finer gates. In particular, the accepted clue `CLUE-affine-composite-clone-relative-operator-class.md` still requires a genuine common-manifold metric theorem or a gauge-invariant nonlocal obstruction.

## 6. Prior art and novelty audit

The stability theorem is not new:

- A. Portilla, J. M. Rodríguez, E. Tourís, *A real variable characterization of Gromov hyperbolicity of flute surfaces*, Osaka Journal of Mathematics **48** (2011), 179--207, DOI `10.18910/9158`, arXiv:0806.0093, especially Definition 2.3 and Theorem 3.8.

Their Definition 2.3 identifies flute surfaces by `r_n=0`, and Theorem 3.8 proves stability under uniformly bounded changes in both `l_n` and `r_n`. The paper even emphasizes that this stability need not come from quasi-isometry.

No novelty is claimed for that theorem, for the pants interpretation of fundamental cuffs, or for the general fact that Gromov hyperbolicity is a coarse metric property. Directed searches did not locate the specific specialization to the exact cotangent prime flute and its all-composite shift clone. The durable project contribution is therefore only the combination

\[
\boxed{
\text{PF-107: }\sup_n|\ell_n^+-\ell_n|<\infty
+
\text{Portilla--Rodríguez--Tourís Thm. 3.8}
\Rightarrow
\text{same Gromov-hyperbolicity class}.}
\]

This is a negative/boundary result for Mathia, not a new theorem about general flute surfaces and not evidence for RH.

## 7. Audit / falsification core

The reusable checks are:

1. verify that the zero-twist tight pants chain is represented by the flute/train coordinates with fundamental half-lengths `l_n=ell_n/2` and second-fundamental data `r_n=0`;
2. verify PF-107's asymptotic (5), hence the global boundedness (7) after including the finite prefix;
3. read Theorem 3.8 with the **uniform bounded-difference** hypotheses (9), not a stronger summability or quasi-isometry hypothesis;
4. apply it symmetrically to obtain (1);
5. do not infer any operator, scattering, quasi-isometry, or RH conclusion from the common Gromov-hyperbolicity class.

A refutation would have to break the tight-flute/train identification, PF-107's bounded cuff perturbation, or the applicability of Theorem 3.8. Determining that both surfaces are hyperbolic, or both are non-hyperbolic, would strengthen the description of the common class but would not alter the no-discrimination conclusion proved here.
