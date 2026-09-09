# WI-211 — two off-line pairs can screen the full two-harmonic reciprocal packet

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-BARRIER + LITERATURE-CONTEXT`.

WI-210 proves a genuine first coercive step: if a dense symmetrized arithmetic bow must be cancelled **locally** at every reciprocal harmonic inside support one, a complementary population made only from critical-line zeros is too small. For `r` reciprocal harmonics, Fejer positivity forces a critical-line mass cost at least `(2r-o(1))M`, so local screening must either fail or introduce additional off-line defect.

That implication does **not** by itself bootstrap off-line *density*. In the first nontrivial full-packet regime

\[
2<d<3,
\]

there are exactly two strictly interior reciprocal harmonics, `alpha_1=1/d` and `alpha_2=2/d`. For an explicit equal-depth bow of `M` selected right-half-plane off-line pairs, the coherent amplitudes at both harmonics can be cancelled **exactly by only two further off-line functional-equation pairs**. The construction respects the reciprocal phase geometry and, whenever `M=T^\vartheta` with

\[
\vartheta<\frac1{2d},
\]

the two screening pairs remain inside the critical strip for all sufficiently large `T`. Their four local zero labels are negligible compared with the Riemann--von Mangoldt excess `(d-2+o(1))m` available when `d>2` is fixed.

Thus finite two-harmonic localization plus functional-equation symmetry plus local zero counting can force the **existence** of fresh off-line defect but cannot force a positive-density amplification. In the open spacing regime `2<d<3`, the full WI-210 reciprocal packet can be screened by `O(1)` additional off-line pairs whose horizontal depth grows like `log M` in the normalized variable. Any actual defect-to-zero iteration must therefore charge horizontal depth, control a continuum/physical slab rather than only two harmonic samples, impose source-specific arithmetic restrictions on the screening pairs, or access another invariant that makes this sparse deep screen impossible.

This is a matched structural countermodel, not a claim that the constructed zeros occur for `zeta`.

## 1. Exact two-harmonic target from an equal-depth bow

Use the WI-210 unfolded normalization. Let the selected arithmetic bow have spacing `d` and let every selected right-half-plane zero have the same scaled horizontal depth

\[
b_j=d h,
\qquad h>0.
\tag{1}
\]

At the reciprocal harmonics

\[
\alpha_k=\frac{k}{d},
\qquad k=1,2,
\tag{2}
\]

the arithmetic ordinates have one common phase. After rotating that phase away, each selected zero together with its same-ordinate functional-equation mirror contributes

\[
2\cosh(kh).
\]

For `M` selected right-half-plane labels the two target amplitudes are therefore

\[
\boxed{
B_1=2M\cosh h,
\qquad
B_2=2M\cosh(2h).
}
\tag{3}
\]

This is a special case of the exact WI-210 formula

\[
B_k=2\sum_{j\in J}\cosh\!\left(\frac{k b_j}{d}\right).
\]

The equal-depth specialization is enough for a countermodel to any universal bootstrap based only on these local moment constraints.

## 2. Two further off-line pairs solve both cancellation equations exactly

Add two further right-half-plane off-line zeros, each with its same-ordinate functional-equation mirror. Give the two new pairs a common scaled depth

\[
b'=da,
\qquad a>0,
\tag{4}
\]

and reciprocal phases

\[
z_+=e^{i\phi},
\qquad
z_-=e^{-i\phi}.
\tag{5}
\]

At the `k`-th reciprocal harmonic their combined contribution is

\[
S_k
=2\cosh(ka)(z_+^k+z_-^k)
=4\cosh(ka)\cos(k\phi).
\tag{6}
\]

We now solve

\[
S_1=-B_1,
\qquad
S_2=-B_2
\tag{7}
\]

exactly.

Set

\[
A:=\frac{M\cosh h}{2},
\qquad
C:=\frac{M\cosh(2h)}{2},
\tag{8}
\]

and consider

\[
P(y)
:=2y^2-(4A^2+1+C)y+2A^2.
\tag{9}
\]

For `M>=2` one has `A>=1`, and

\[
P(0)=2A^2>0,
\qquad
P(2A^2)=-2A^2C<0.
\tag{10}
\]

Since the leading coefficient of `P` is positive, `P` has a larger positive root `y_+` satisfying

\[
\boxed{y_+>2A^2>1.}
\tag{11}
\]

Define

\[
\cosh a:=\sqrt{y_+},
\qquad
\cos\phi:=-\frac{A}{\sqrt{y_+}}.
\tag{12}
\]

Equation (11) gives

\[
-\frac1{\sqrt2}<\cos\phi<0,
\]

so a real `phi` exists, with `pi/2<phi<3pi/4`, and `a>0` is real. Then

\[
4\cosh a\cos\phi
=4\sqrt{y_+}\left(-\frac{A}{\sqrt{y_+}}\right)
=-4A
=-2M\cosh h
=-B_1.
\tag{13}
\]

For the second harmonic,

\[
\cosh(2a)=2y_+-1,
\qquad
\cos(2\phi)=\frac{2A^2}{y_+}-1.
\tag{14}
\]

Dividing `P(y_+)=0` by `y_+` gives exactly

\[
(2y_+-1)
\left(\frac{2A^2}{y_+}-1\right)
=-C.
\tag{15}
\]

Therefore

\[
4\cosh(2a)\cos(2\phi)
=-4C
=-2M\cosh(2h)
=-B_2.
\tag{16}
\]

Combining (13) and (16),

\[
\boxed{
S_1+B_1=0,
\qquad
S_2+B_2=0.
}
\tag{17}
\]

Thus two additional off-line pairs screen both reciprocal harmonics exactly. No critical-line complementary mass is needed.

## 3. The screening depth is only logarithmic in the bow population

The roots of `P` have product `A^2`. Since `y_+>2A^2`, the smaller root is `<1/2`. Their sum is

\[
\frac{4A^2+1+C}{2},
\]

so

\[
y_+
=2A^2+\frac{C}{2}+O_h(1)
\qquad(M\to\infty).
\tag{18}
\]

Because

\[
A=\frac{M\cosh h}{2},
\]

this gives

\[
\sqrt{y_+}
=\frac{M\cosh h}{\sqrt2}\left(1+O_h(M^{-1})\right).
\tag{19}
\]

Hence

\[
\boxed{
a=\operatorname{arcosh}\sqrt{y_+}
=\log M+O_h(1).}
\tag{20}
\]

The screen is therefore sparse in count but deep in the horizontal direction. This is exactly the degree of freedom that the positive Fejer moment budget in WI-210 does not charge.

## 4. The two screening pairs can remain inside the critical strip

Return to zeta height `T` and write `L=log T`. A pair with scaled depth `b'=da` has real part

\[
\beta'
=\frac12+\frac{da}{L}.
\tag{21}
\]

Suppose

\[
M=T^{\vartheta+o(1)}
\tag{22}
\]

for a fixed `vartheta>0`. From (20),

\[
\frac{a}{L}=\vartheta+o(1),
\]

and therefore

\[
\boxed{
\beta'
=\frac12+d\vartheta+o(1).
}
\tag{23}
\]

If

\[
\boxed{d\vartheta<\frac12,}
\tag{24}
\]

then for all sufficiently large `T` the added right-half zeros satisfy

\[
\frac12<\beta'<1,
\]

and their functional-equation mirrors lie in `(0,1/2)`. Thus the sparse screen is compatible with the critical strip and the compulsory symmetry. Classical zero-density bounds do not rule out `O(1)` such pairs at a sequence of heights; the construction is deliberately exploiting a zero-density exceptional reservoir.

The two phases in (5) are also locally realizable. In WI-210 unfolded coordinates choose ordinates `u_+`,`u_-` with

\[
\frac{2\pi(u_\pm-x_0)}{d}
\equiv\pm\phi\pmod{2\pi}.
\tag{25}
\]

They differ from a bow grid point by only `O_d(1)` unfolded units, hence by `O_d(1/L)` in physical ordinate. An interval containing a bow of `m\to\infty` labels has ample room for those two additional ordinates.

## 5. Riemann--von Mangoldt count does not charge this screen at positive density

WI-210 records that a bow interval with unfolded spacing tending to `d` contains

\[
(d+o(1))m
\]

zero labels counted with multiplicity, while a full selected right-half bow together with its compulsory mirrors consumes

\[
(2+o(1))m.
\]

The remaining local count budget is therefore

\[
\boxed{(d-2+o(1))m.}
\tag{26}
\]

For every fixed

\[
2<d<3,
\tag{27}
\]

this excess tends to infinity. The screening construction uses only four additional local labels: two new right-half zeros and their same-ordinate functional-equation mirrors. Hence (26) easily accommodates the exact screen.

In the same regime (27), the complete strictly interior reciprocal packet is exactly

\[
\alpha_1=1/d,
\qquad
\alpha_2=2/d,
\]

because `1,2<d<3`. Thus (17) screens **the full WI-210 harmonic packet**, not a hand-picked proper subset.

The endpoint `d=2` is different. There is then only one strictly interior reciprocal harmonic and no positive-density local count excess. The present countermodel does not claim to supply extra local labels at that count-saturating endpoint. Its role is to show that immediately above the endpoint, where WI-210 gains a second harmonic and a positive local excess, count amplification still does not become an iterative density mechanism.

## 6. Toeplitz/inertia interpretation

For one off-line functional-equation pair with reciprocal phase `z` and radial parameter `q=e^a`, the harmonic sequence is

\[
(q^k+q^{-k})z^k.
\tag{28}
\]

On a finite Toeplitz section this pair can be written as

\[
uw^*+wu^*,
\]

with

\[
u_j=(qz)^j,
\qquad
w_j=(q^{-1}z)^j.
\tag{29}
\]

For `q\ne1`, this Hermitian block has rank at most two and generically one positive and one negative direction. This is the finite-moment signature reason the positive-measure Fejer argument breaks as soon as off-line pairs are admitted.

The explicit solution (12)--(17) shows that the failure is not merely qualitative. Two such indefinite blocks can carry amplitudes of order `M` at the first two harmonics while their **count cost stays constant**, because their radial parameter grows as `q\asymp M`. Finite-harmonic Toeplitz inertia therefore cannot be converted into a count bootstrap unless the radial/horizontal size of those indefinite blocks is charged independently.

## 7. What the barrier does and does not kill

The construction kills the following proposed inference in the full-packet regime `2<d<3`:

\[
\text{dense selected bow}
+\text{local cancellation at all interior reciprocal harmonics}
+\text{local zero count}
\Longrightarrow
\text{positive-density new off-line mass}.
\]

The conclusion is false using only those inputs. The exact screen above needs just two new off-line pairs.

It does **not** kill stronger source-localization mechanisms. In particular, the screen has rapidly growing horizontal depth and was fitted at two discrete reciprocal samples. It may fail constraints that simultaneously control:

- a continuum of nearby frequencies or the full physical Gallagher slab rather than only `alpha_1,alpha_2`;
- a depth-weighted Weil/inertia quantity whose cost grows with `a`;
- source-fixed `Lambda-Lambda^sharp` correlations that restrict the allowed radial moment sequence;
- a theorem coupling the screening pair to a mesoscopic family of further zeros;
- an arithmetic or zero-free constraint stronger than ordinary local count and classical zero density.

Those are genuine escape routes because they add information absent from the countermodel.

## 8. Prior-art and novelty audit

The positive side of WI-210 is the classical truncated trigonometric moment problem: unit-circle moments are constrained by positive-semidefinite Toeplitz matrices, equivalently by Fejer/Caratheodory positivity. The broader literature on **indefinite** truncated moment problems and generalized Nevanlinna/Pontryagin-space interpolation makes clear that allowing a finite number of negative squares changes the moment geometry qualitatively; see, for example, Vladimir Derkach, Seppo Hassi and Henk de Snoo, *Truncated moment problems in the class of generalized Nevanlinna functions*, Math. Nachr. 285 (2012), 1741--1769, DOI `10.1002/mana.201100268`, and V. A. Derkach and Harry Dym, *Entire isometric operators in de Branges-Pontryagin spaces and truncated trigonometric moment problem*, Complex Anal. Oper. Theory (2025), DOI `10.1007/s11785-025-01729-z`. These sources are context for the indefinite-moment mechanism, not evidence for the zeta-specific construction above.

Maynard--Pratt's *Half-isolated zeros and zero-density estimates*, IMRN 2024, 12978--13014, DOI `10.1093/imrn/rnae191`, explicitly leaves vertically rigid/arithmetic-progression-type exceptional configurations as live adversaries to ordinary zero-density reasoning. The present screen is a local finite-harmonic countermodel inside the Mathia bow reduction; it is not asserted or implied by Maynard--Pratt.

A targeted search around truncated trigonometric moments, indefinite Toeplitz forms, generalized Nevanlinna moment problems, reciprocal/power-sum interpolation, and Maynard--Pratt vertical arithmetic configurations found the classical positive/indefinite moment frameworks but no source giving this two-pair zeta-bow screen or the resulting local-count bootstrap barrier. Absence from that search is **not** used as a priority claim, and no novelty claim is made.

## Research consequence

WI-210 remains correct and useful: multi-harmonic localization can rule out an RH-compatible critical-line-only screen and therefore force *some* fresh off-line defect. WI-211 identifies the next obstruction precisely. In the full two-harmonic regime, the fresh defect can be only `O(1)` pairs, with depth `a=log M+O(1)`, and still cancel a dense bow exactly at both reciprocal samples.

So a successful defect-to-zero bootstrap must make sparse deep screening expensive. The next source-side target should not be merely “localize one more reciprocal harmonic.” It should seek a **radial/depth coercivity or continuum-frequency localization** whose cost grows with the screening parameter `a`, or a source identity that prevents a bounded number of deep indefinite blocks from matching the required reciprocal packet. That is the missing ingredient needed to turn WI-210's defect-to-defect alternative into a genuine iterative elimination of exceptional zeros.
