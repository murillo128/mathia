# ANF-047 — phase-blind amplitude variation gives an explicit five-point coherence certificate

**Status:** `EXACT-DERIVED + CLASSICAL-AFFINITY + AMPLITUDE-COHERENCE-BOUND + COMPUTABLE-SAFETY-CERTIFICATE + STRICT-VARIANCE-GAP + STRUCTURAL-REDUCTION`. `ANF-045` reduces the last irreducible cardinality-five geometry to the Fourier-character coherence

\[
\kappa_*(y_1,y_2,d)
=
\frac{\sup_t(-\operatorname{Re}Z_{y_1,y_2,d}(t))}
{\sqrt{F_0Q}},
\]

and proves abstractly that `kappa_*<1` for every genuine two-pair shape, uniformly on compact shape boxes. The remaining burden there still contains a one-dimensional Fourier supremum. The present finding removes that supremum from a rigorous **sufficient** safety test. The triangle inequality gives a phase-blind envelope depending only on the amplitude distribution of the fixed shape, and its gap from one is exactly the coefficient-of-variation/Hellinger gap of that amplitude. Thus a two-pair shape is certified safe whenever one static three-variable integral inequality holds; no common-translation search is needed.

Retain the notation of `ANF-045`. Let

\[
F_0=\int J(\alpha)\,d\alpha>0,
\qquad
J\ge0,
\]

with `J` continuous, even, nonzero and compactly supported. For a genuine shape `y_1,y_2>0`, put

\[
a(\alpha)=\cosh(2\pi\alpha y_1)-1,
\qquad
b(\alpha)=\cosh(2\pi\alpha y_2)-1,
\]

\[
u_d(\alpha)=a(\alpha)e^{2\pi i\alpha d}+b(\alpha),
\]

and

\[
Q=\int J|u_d|^2,
\qquad
P=2\int J(a+b)(1+\cos(2\pi\alpha d))\ge0,
\]

\[
Z(t)=\int J(\alpha)e^{2\pi i\alpha t}u_d(\alpha)\,d\alpha.
\]

Then `ANF-045` gives

\[
H_J(y_1,y_2;t+d,t)=Q+P+\operatorname{Re}Z(t),
\tag{1}
\]

with `Q>0`. The physical five-point energy difference from the real-part collapse is `4H_J`.

## 1. A phase-blind envelope removes the translation supremum

Define the amplitude integral

\[
\boxed{
L(y_1,y_2,d)
:=\int J(\alpha)|u_d(\alpha)|\,d\alpha.
}
\tag{2}
\]

For every common translation `t`,

\[
-\operatorname{Re}Z(t)
\le |Z(t)|
\le \int J|u_d|
=L.
\tag{3}
\]

Therefore the exact coherence of `ANF-045` satisfies the explicit bound

\[
\boxed{
\kappa_*(y_1,y_2,d)
\le
\lambda(y_1,y_2,d)
:=\frac{L}{\sqrt{F_0Q}}.
}
\tag{4}
\]

Cauchy--Schwarz gives `lambda<=1`, but unlike the bare bound `kappa_*<=1`, the quantity `lambda` is a static shape functional: it contains no translation parameter and no Fourier supremum.

Combining (1) and (3) gives the phase-blind lower envelope

\[
\boxed{
\inf_t H_J(y_1,y_2;t+d,t)
\ge Q+P-L.
}
\tag{5}
\]

Equivalently, with the dimensionless variables of `ANF-045`,

\[
x=\sqrt{Q/F_0},
\qquad
p=P/F_0,
\qquad
\ell=L/F_0,
\]

one has

\[
\boxed{
\inf_t H_J
\ge F_0(x^2+p-\ell)
=F_0(x^2-\lambda x+p).
}
\tag{6}
\]

Hence a fixed two-pair shape is safe for **every** common translation as soon as

\[
\boxed{L\le Q+P.}
\tag{7}
\]

This is equivalently

\[
\lambda\le x+\frac{p}{x},
\tag{8}
\]

which has exactly the same right-hand threshold as the necessary-and-sufficient coherence gate in `ANF-045`, but replaces the unknown `kappa_*` by an explicit amplitude-only upper bound.

The logical direction matters: failure of (7) does **not** produce a five-point counterexample. It only means that phase-blind control is insufficient for that shape; the true Fourier-character coherence may still be much smaller than `lambda`.

## 2. The amplitude gap is exactly a variance/Hellinger gap

Normalize the spectral measure by

\[
d\mu(\alpha)=\frac{J(\alpha)}{F_0}\,d\alpha,
\]

and set

\[
R(\alpha)=|u_d(\alpha)|.
\]

Then

\[
x^2=\mathbb E_\mu R^2,
\qquad
\ell=\mathbb E_\mu R,
\qquad
\lambda=\frac{\mathbb E_\mu R}{\sqrt{\mathbb E_\mu R^2}}.
\tag{9}
\]

Thus the loss from perfect Cauchy coherence has the exact identity

\[
\boxed{
1-\lambda^2
=
\frac{\operatorname{Var}_\mu(R)}{\mathbb E_\mu R^2}.
}
\tag{10}
\]

Equivalently,

\[
\boxed{
1-\lambda
=
\frac{\operatorname{Var}_\mu(R)}
{\mathbb E_\mu R^2\,(1+\lambda)}.
}
\tag{11}
\]

There is also a classical affinity interpretation. Define the amplitude-weighted probability measure

\[
d\nu(\alpha)
=
\frac{R(\alpha)^2}{\mathbb E_\mu R^2}\,d\mu(\alpha).
\tag{12}
\]

Then

\[
\boxed{
\lambda
=\int\sqrt{\frac{d\nu}{d\mu}}\,d\mu,
}
\tag{13}
\]

so `lambda` is precisely the Bhattacharyya/Hellinger affinity between the base spectral measure and the shape's quadratic-amplitude reweighting. The general affinity formalism is classical; the new point here is that the `ANF-045` coherence problem lands on this exact pair of measures.

For every genuine shape,

\[
\boxed{\lambda<1.}
\tag{14}
\]

Indeed, equality in (10) would force `R` to be constant `mu`-almost everywhere. Since `J` is continuous, nonnegative and nonzero, it is positive on some open interval. On the real axis,

\[
R(\alpha)^2
=a(\alpha)^2+b(\alpha)^2
+2a(\alpha)b(\alpha)\cos(2\pi\alpha d)
\tag{15}
\]

is real analytic. Constancy on an interval would therefore force it to be constant everywhere. But `R(0)=0`, while

\[
u_d(\alpha)
=2\pi^2(y_1^2+y_2^2)\alpha^2+O(\alpha^3)
\tag{16}
\]

is nonzero for sufficiently small nonzero `alpha`. This contradiction proves (14).

So the strict Hilbert gap of `ANF-045` has a concrete source visible before any phase analysis: the hyperbolic two-pair amplitude cannot have constant magnitude across the spectral measure.

## 3. Compact shape boxes have a computable amplitude gap

Fix a compact genuine-shape box

\[
\mathcal S_{\varepsilon,Y,D}
=[\varepsilon,Y]^2\times[-D,D],
\qquad
0<\varepsilon\le Y<\infty.
\tag{17}
\]

The functions `Q` and `L` are continuous in `(y_1,y_2,d)`. By `ANF-045`, `Q>0` for every genuine shape, hence it has a positive minimum on the box. Therefore `lambda=L/sqrt(F_0Q)` is continuous there. Since (14) holds pointwise, compactness gives

\[
\boxed{
\sup_{\mathcal S_{\varepsilon,Y,D}}\lambda
\le1-\delta_{\rm amp}
}
\tag{18}
\]

for some `delta_amp>0`.

This is stronger as a certification interface than the abstract compact coherence gap alone: `delta_amp` can be bounded directly from nonnegative amplitude integrals, and automatically gives

\[
\kappa_*\le\lambda\le1-\delta_{\rm amp}.
\tag{19}
\]

No Riemann--Lebesgue tail cutoff in the translation variable is required for this bound. In particular, after the compactification of `ANF-044`, the remaining five-point safety problem admits the purely three-dimensional sufficient gate (7) on the compact obstruction box.

A useful coarse version avoids even the absolute-value integral. For any measurable partition `{B_k}` of the spectral support, define

\[
r_k=\mu(B_k),
\qquad
s_k=\frac{\int_{B_k}J|u_d|^2}{Q}.
\tag{20}
\]

Applying Cauchy--Schwarz separately on every bin gives

\[
\boxed{
\kappa_*
\le\lambda
\le
\sum_k\sqrt{r_ks_k}.
}
\tag{21}
\]

The last expression is the finite-bin Bhattacharyya coefficient between the base spectral mass and the quadratic-amplitude mass. Refining the partition decreases this coarse envelope toward the full affinity `lambda`. For two bins `B,B^c`, if `r=mu(B)` and `s=nu(B)`, then

\[
\boxed{
\kappa_*
\le
\sqrt{rs}+\sqrt{(1-r)(1-s)},
}
\tag{22}
\]

with the exact deficit identity

\[
\boxed{
1-\sqrt{rs}-\sqrt{(1-r)(1-s)}
=
\frac12\left[(\sqrt r-\sqrt s)^2
+(\sqrt{1-r}-\sqrt{1-s})^2\right].
}
\tag{23}
\]

Thus **any certified mismatch of normalized spectral mass in one frequency band produces an explicit coherence gap**.

## 4. The forced central zero gives a linear small-band coherence loss

When additionally `J(0)>0`, choose the central band

\[
B_h=[-h,h].
\]

For a fixed genuine shape, (16) gives, with

\[
A=2\pi^2(y_1^2+y_2^2)>0,
\]

\[
|u_d(\alpha)|^2=A^2\alpha^4+O(|\alpha|^5).
\tag{24}
\]

Continuity of `J` at zero then yields

\[
r_h
=\frac{2J(0)}{F_0}h+o(h),
\tag{25}
\]

while

\[
s_h
=\frac{2J(0)A^2}{5Q}h^5+o(h^5).
\tag{26}
\]

Substitution into (22) gives

\[
\boxed{
\kappa_*
\le
1-\frac{J(0)}{F_0}h+o(h)
\qquad(h\downarrow0).
}
\tag{27}
\]

On every compact genuine-shape box the remainder is uniform, because `A` is uniformly bounded and `Q` is uniformly bounded away from zero. Thus the central spectral region alone witnesses a first-order coherence loss: the base measure places order-`h` mass near zero, while the quadratic-amplitude measure places only order-`h^5` mass there because `u_d` has a forced double zero.

For the narrow central-notch spectra `J_s` of `ANF-034` and `ANF-046`, one may choose the admissible perturbation with `J_s(0)>0`, so this central-band certificate applies directly. It is robust under making the notch narrow: the perturbation changes the spectral density, but it does not remove the double zero of the two-pair amplitude.

## 5. Prior art, falsification, and evidence boundary

The inequalities used here are elementary triangle/Cauchy--Schwarz inequalities. The normalized overlap in (13) and its finite-bin form in (21)--(23) are the classical Bhattacharyya/Hellinger affinity and its coarse-graining bound. A targeted search of the neighboring statistical-affinity, Hilbert-coherence, bandlimited-extremal, and pair-correlation literature found the expected classical affinity formalism but no external theorem is load-bearing for the specialization (4)--(7), the variance identity (10), or the forced-zero asymptotic (27). No publication-level novelty claim is made, and no new `SOURCES.md` entry is required.

The main falsification checks are direct. Equation (3) keeps the correct inequality direction: it bounds the *largest possible negative* Fourier correlation from above. Equation (10) is an identity, not an estimate. Strictness in (14) does not assume `J(0)>0`; it uses only positivity of `J` on some open interval plus real analyticity of `|u_d|^2`. The stronger small-band asymptotic (27) does require `J(0)>0`. Finally, the amplitude envelope is intentionally phase-blind. It can certify safety but cannot certify danger: if `Q+P-L<0`, one must return to `kappa_*` or a phase-aware refinement before claiming a negative five-point defect.

No claim is made here about multisets of cardinality greater than five, nor about sufficiency of the full universal affine counting inequality from `ANF-005`. The result only strengthens the last cardinality-five complex gate isolated by `ANF-036`--`ANF-045`.

## 6. Consequence for the next gate

For a central-notch survivor with positive curvature margin, `ANF-044` confines every possible two-pair negative defect to a compact shape box. `ANF-045` says the exact remaining question is whether `kappa_*` crosses `x+p/x`. The present finding inserts a cheaper rigorous gate before that optimization:

\[
\boxed{
Q(y_1,y_2;d)+P(y_1,y_2;d)
\ge
L(y_1,y_2;d)
\quad\text{throughout the compact box}.
}
\tag{28}
\]

If (28) is certified, the entire remaining two-pair cardinality-five geometry is nonnegative for every common translation, and no Fourier-supremum computation is needed. If (28) fails somewhere, nothing has yet been falsified; only those shapes need the sharper phase-aware `kappa_*` test. The search domain is therefore reduced from a four-variable oscillatory problem to a three-variable nonnegative-integral certificate plus, at worst, a smaller residual set requiring phase analysis.