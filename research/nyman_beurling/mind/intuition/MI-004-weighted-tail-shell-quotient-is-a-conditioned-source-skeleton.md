# MI-004 — The collective late Nyman quotient is governed by one dyadic backward shift

**Evidence level:** proved structural identities through NB-060; whether the arithmetic generalized nullspace reaches the canonical residual remains open.

After removing the common off-critical Blaschke factor, the natural Nyman closure is `\mathcal A` and its defect space is

\[
\mathcal D=\mathcal A^\perp.
\]

NB-053--NB-057 show that raw late quotient columns shrink and that the canonical finite residual becomes invisible to every sufficiently late **individual** shifted block. NB-058 identifies the collective loophole by the finite-time defect sectors

\[
\mathcal K_R
=\mathcal D\cap\ker U_{\log R}^*.
\]

Under Paley--Wiener these are exactly the defect vectors supported in `[0,log R]`, and the collective late target mass is the distance of `h_*=Qe` from `\mathcal K_R`.

NB-060 turns the whole finite-cutoff family into a one-operator root-space problem. Define

\[
B_2:=U_{\log2}^*|_{\mathcal D}.
\]

Integer-log invariance gives

\[
\mathcal K_{2^k}=\ker B_2^k,
\]

and dyadic cofinality gives

\[
\mathcal K_{\rm fin}
:=\overline{\bigcup_{R\ge2}\mathcal K_R}
=
\overline{\bigcup_{k\ge1}\ker B_2^k}.
\]

Hence

\[
\mathcal K_2=\{0\}
\iff
\mathcal K_R=\{0\}\text{ for every finite }R.
\]

This is stronger than a convenient subsequence reduction. If any compact-time arithmetic defect exists at any scale, repeatedly applying the backward shift produces a nonzero defect already in the first window `[0,log2]`. Existence is therefore a fixed-scale question.

The canonical tail is a different question. Its limiting mass is exactly

\[
\operatorname{dist}\!\left(
 h_*,
 \overline{\bigcup_{k\ge1}\ker B_2^k}
\right)^2.
\]

A nonzero first-window kernel supplies only a seed; decay requires its generalized root tower to approximate `h_*`. Conversely, if `ker B_2=0`, every finite defect sector vanishes and the collective late quotient remains the entire defect space at every finite cutoff even though each sufficiently late individual block is weak against the canonical residual.

The unit-outer control realizes the dense generalized-kernel branch: the dyadic root spaces exhaust the flat defect space. The arithmetic problem is precisely whether the actual deflated Nyman space has comparable root-space abundance.

**Boundary.** NB-060 does not construct a nonzero element of `ker B_2`, prove density of the generalized nullspace, or transfer the flat model's cubic tail rate to zeta. It replaces a moving family of existence questions by one first-window kernel plus a separate generalized-root approximation problem.