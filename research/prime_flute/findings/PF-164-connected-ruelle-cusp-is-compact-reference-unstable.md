# PF-164 — connected Ruelle cusp coefficient is compact-reference unstable

**Status:** `EXACT-DERIVED + CLASSICAL-INPUT + LITERATURE-AUDITED + DECISIVE-NEGATIVE/COMPACT-REFERENCE-DEPENDENCE`.

## Statement

Let

\[
V(x)=\pi\cot\frac{\pi}{x},
\qquad
X_n=V(p_n)
\]

be the exact prime-flute endpoints, and let the standard all-composite shift reference of PF-106/PF-161 have normalized endpoints

\[
Y_n=V(p_n+1)-1,
\qquad
e_n:=Y_n-X_n.
\]

PF-161 writes the logarithmic cusp coefficient of its connected canonical bottom-Ruelle product as

\[
C_* = \sum_i A_i,
\qquad
A_i=e_i+e_{i+1},
\]

where the left exterior pair is `(p_i,p_{i+1})`.

Fix an interior index `j`. Replace only the composite label `q_j=p_j+1` by another composite label `q'_j` satisfying

\[
q_{j-1}<q'_j<q_{j+1},
\]

and leave every other reference label unchanged. After the same global translation normalization, put

\[
\widetilde Y_j=V(q'_j)-1,
\qquad
\delta_j:=\widetilde Y_j-Y_j=V(q'_j)-V(p_j+1).
\]

Then the modified exact all-composite reference agrees **exactly** with the standard shift reference at every endpoint except `j`, hence agrees exactly on the complete tail after that vertex. Nevertheless its connected bottom-Ruelle product satisfies

\[
\boxed{
\frac d{ds}\log \widetilde{\mathcal R}_0(s)
\sim
\bigl(C_*+2\delta_j\bigr)\log\frac1s
\qquad(s\downarrow0).
}
\tag{1}
\]

The product itself still has a finite strictly positive value at `s=0`. Thus a compact one-vertex change of the exact all-composite comparison surface changes the coefficient of the PF-161 `s\log(1/s)` branch by exactly `2\delta_j`.

Moreover this change is unbounded in both signs within exact ordered all-composite controls. If the following prime gap `g_j=p_{j+1}-p_j` is larger than `2`, choose

\[
q'_j=p_{j+1}-1;
\]

then `q'_j` is even composite, remains strictly between its neighboring reference labels, and

\[
\delta_j>g_j-2.
\tag{2}
\]

If the preceding gap `g_{j-1}=p_j-p_{j-1}` is larger than `2`, choose instead

\[
q'_j=p_{j-1}+3;
\]

then again `q'_j` is even composite and ordered, while

\[
\delta_j<-(g_{j-1}-2).
\tag{3}
\]

Since prime gaps are unbounded, the coefficient in (1) can be made arbitrarily large positive or negative while changing only one vertex of the comparison surface.

## Relevance

PF-162 showed that the PF-161 coefficient varies across the natural family of fixed odd shifts `p\mapsto p+m`, and PF-163 showed that a dilation reference even changes the logarithmic order of the selected boundary cusp. Those controls differ from the standard shift reference throughout the tail. The present result closes a stronger escape: **the coefficient is not even an invariant of the exact comparison tail**. Its value can be altered without changing any sufficiently far endpoint, cuff, cross-ratio, or Fuchsian tail datum of the reference.

This is the connected `s=0` analogue of PF-102's compact-defect mechanism at the earlier `Re s=1/4` boundary. It shows that the surviving PF-161 cusp coefficient is another long-channel response to local reference data rather than an intrinsic prime-gap statistic selected by the prime flute.

The conclusion concerns only the PF-159--PF-161 selected canonical-separator relative product. It does **not** say that compact perturbations are invisible to the full Laplacian, scattering matrix, resonance set, or genuine full Ruelle/Selberg dynamics. Rather, it rules out interpreting this particular connected coefficient as a tail-intrinsic RH-relevant invariant.

## Derivation

Only one endpoint displacement changes:

\[
\widetilde e_j=e_j+\delta_j,
\qquad
\widetilde e_i=e_i\quad(i\ne j).
\tag{4}
\]

Hence among the infinitely propagated left-edge coefficients only the two adjacent ones change,

\[
\widetilde A_{j-1}=A_{j-1}+\delta_j,
\qquad
\widetilde A_j=A_j+\delta_j,
\tag{5}
\]

and all other `A_i` are unchanged. Separators in which the modified vertex occurs only in the right exterior pair form a finite family of left indices and therefore contribute at most a bounded term to the `s\downarrow0` logarithmic derivative.

For a fixed left exterior pair `(a,b)`, PF-159's exact one-ended factorization does not require the standard shift formula once the left reference gap is fixed. If `c<d` is a consecutive far prime pair, the same secant expansion used in PF-159/PF-161 gives

\[
c\bigl(L_{a,c}^{\rm ref}-\widehat L_{a,c}^{\rm ref}\bigr)
\longrightarrow
-2A_{a}^{\rm ref}.
\tag{6}
\]

For the two affected left pairs the compact endpoint modification merely replaces `A_a` by `A_a+\delta_j`; every far endpoint is otherwise identical to the standard shift clone. With

\[
q_s(L)=\frac{L}{e^{sL}-1},
\qquad
\frac{\partial q_s}{\partial L}
=-\frac12h(sL),
\]

where `h(0)=1` and `h` decays exponentially at infinity, (6) yields for each affected left family

\[
\sum_{c\ \mathrm{prime}}
\left[
\widetilde T_{a,c}(s)-T_{a,c}(s)
\right]
\sim
\delta_j\log\frac1s.
\tag{7}
\]

The only arithmetic input in (7) is the classical reciprocal-prime asymptotic

\[
\sum_{p\le x}\frac1p=\log\log x+O(1),
\]

with the soft cutoff `\log c\asymp1/s` supplied by `h(sL)` and `L\asymp\log c`. Adding the two affected left families gives

\[
\frac d{ds}
\log\frac{\widetilde{\mathcal R}_0(s)}{\mathcal R_0(s)}
\sim
2\delta_j\log\frac1s.
\tag{8}
\]

Combining (8) with PF-161 proves (1).

The zero-boundary value remains finite and nonzero. For either affected fixed left pair, (6) and the logarithmic lower bound `L\gg\log c` give

\[
\left|\log\frac{\widetilde L_{a,c}}{L_{a,c}}\right|
\ll_{a,j}\frac1{c\log c},
\tag{9}
\]

whose sum over right primes converges. All remaining changes are finite. Thus the logarithm of the ratio of the modified and standard connected products converges absolutely at `s=0`.

It remains to verify the unbounded tuning. For `x>2`,

\[
V'(x)=\left(\frac{\pi/x}{\sin(\pi/x)}\right)^2>1.
\tag{10}
\]

For the positive construction, `q'_j-q_j=g_j-2>0`, so the mean-value theorem and (10) give (2). For the negative construction, `q'_j-q_j=-(g_{j-1}-2)<0`, and (10) gives (3). Both replacement labels are even and hence composite. Unbounded prime gaps are classical (already the elementary factorial construction suffices), so `2\delta_j` is unbounded in both signs.

The same argument extends to any finite-support modification away from the initial boundary: if the normalized endpoint changes are `\delta_j` on a finite set, then the connected cusp coefficient changes by

\[
2\sum_j\delta_j,
\tag{11}
\]

up to the obvious one-sided correction if the very first admissible endpoint is modified.

## Verification

The calculation has four independent checks.

First, order and all-composite status are exact: the replacements `p_{j+1}-1` and `p_{j-1}+3` are even composites and lie strictly between `p_{j-1}+1` and `p_{j+1}+1` whenever the corresponding gap exceeds `2`.

Second, the coefficient bookkeeping is local and exact. A single displacement occurs in exactly two consecutive left-edge sums `A_i=e_i+e_{i+1}`, producing `2\delta_j`; any occurrence of the same vertex as a right endpoint affects only finitely many separators and cannot produce a logarithmic divergence.

Third, the analytic summation is the already verified PF-161 mechanism applied to two fixed left families. The difference of connected products has summable zero-boundary logarithm by `\sum_p1/(p\log p)<\infty`, while its derivative has the reciprocal-prime `\log(1/s)` divergence by Mertens' theorem. No interchange of two nonsummable infinite perturbation tails is required because the reference modification has finite support.

Fourth, the control is stronger than an asymptotically matched surface: outside one vertex the two all-composite reference endpoint sequences are literally equal. Hence the effect cannot be attributed to a different right limit, a different tail asymptotic, a continuum interpolation, or a cumulative mismatch at infinity.

## Novelty Status

No novelty is claimed for unbounded prime gaps, Mertens' reciprocal-prime theorem, local Ruelle factors, or the general dependence of relative spectral constructions on a comparison object. Werner Müller's relative determinant framework treats relative quantities as data of an operator pair; see *Relative zeta functions, relative determinants and scattering theory*, Comm. Math. Phys. 192 (1998), 309--347, DOI `10.1007/s002200050301`. Borthwick--Judge--Perry treat genuine Selberg zeta/scattering relations for geometrically finite surfaces, not this zero-systole infinite-type selected separator product; see *Selberg's zeta function and the spectral geometry of geometrically finite hyperbolic surfaces*, Comment. Math. Helv. 80 (2005), 483--515, DOI `10.4171/CMH/23`.

The closest Mathia prior art is PF-102, which shows that one compact endpoint defect already reproduces the unconnected quarter-plane propagation threshold. PF-162 and PF-163 then show reference dependence of the later connected boundary using controls that differ throughout the tail. Directed searches across relative determinant, Selberg/Ruelle, compact-perturbation, and infinite-area hyperbolic literature did not locate the specific finite-support law (8), the exact coefficient shift `2\delta_j`, or its all-composite one-vertex realization.

The warranted classification is therefore a **prime-flute-specific compact-reference instability of the selected canonical connected Ruelle cusp**, not a new general theorem about Ruelle zeta functions or compact perturbations.

## Open Consequence

PF-161--PF-164 now leave no intrinsic interpretation for either the coefficient or the singularity class of the explicit connected canonical-separator Ruelle cusp: fixed shifts vary its coefficient, dilations vary its logarithmic order, and a one-vertex compact reference change can tune its coefficient without changing the comparison tail at all.

A surviving Selberg/Ruelle mechanism must therefore be a genuinely intrinsic full-surface object, or a relative object whose reference is itself selected canonically by the prime-flute geometry and whose relevant divisor or singular data are stable under compact as well as asymptotic matched-control audits. Merely subtracting a convenient comparison surface and reading a boundary coefficient from the remaining canonical-separator product is no longer a viable RH route.