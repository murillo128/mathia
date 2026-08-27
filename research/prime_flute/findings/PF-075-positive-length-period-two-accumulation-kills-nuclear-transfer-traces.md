# PF-075 — positive-length period-two accumulation kills natural nuclear transfer traces

**Status:** `DECISIVE-NEGATIVE` for direct/countable Bowen--Series, Mayer, and Ruelle-type transfer operators built from the canonical side-pairing branches with the standard geometric derivative weight and faithful periodic coding.

This strengthens PF-069 and PF-070 in a different direction.  PF-070 ruled out a *uniformly expanding* faithful coding because the prime-flute has systole zero.  PF-075 shows that even if one abandons uniform expansion and tries to retain a countable non-uniform nuclear/trace-class transfer operator, the canonical local coding already has infinitely many primitive periodic orbits of the **same bounded symbolic period** with geometric lengths in a compact positive interval.  The flat trace of a fixed power then diverges.

## 1. A canonical two-letter periodic family

For real boundary endpoints

\[
a<b<c<d,
\]

let

\[
G(a,b)=\frac1{b-a}
\begin{pmatrix}
a+b&-2ab\\
-2&a+b
\end{pmatrix}
\]

be the exact zero-twist side-pairing generator used throughout the prime-flute construction.

PF-004 proves that the reduced two-letter word

\[
W(a,b,c,d)=G(a,b)G(c,d)^{-1}
\]

represents a primitive simple separating closed geodesic and that, with

\[
X=b-a,\qquad Y=c-b,\qquad Z=d-c,
\]

its translation length is

\[
\boxed{
L=4\operatorname{arsinh}
\sqrt{\frac{Y(X+Y+Z)}{XZ}}
}.
\]

Thus these separators are not long complicated words whose symbolic period grows with their geometry.  In the canonical side-pairing alphabet they are all represented by reduced words of **length two**.

For four consecutive prime-derived endpoints one obtains an infinite family

\[
W_n=G_nG_{n+2}^{-1}
\]

(up to the harmless indexing convention for the side pairings), each corresponding to the four-endpoint separator of PF-004/PF-069.

## 2. PF-069 supplies infinitely many such period-two orbits in one positive compact length window

PF-069 uses the Banks--Freiberg--Maynard multidimensional theorem on limit points of three consecutive normalized prime gaps together with the exact cross-ratio above.  It proves that there is a nondegenerate interval

\[
I_L\Subset(0,\infty)
\]

contained in the closure of the lengths of these primitive simple separating geodesics.

Choose any nonempty compact interval

\[
J=[A,B]\Subset I_L,
\qquad 0<A<B<\infty.
\]

Then there are infinitely many distinct primitive separators of the canonical two-letter family with

\[
\boxed{L_n\in J.}
\]

This is the key strengthening over the short-orbit obstruction: the relevant multipliers are bounded away both from \(1\) and from infinity, while the **symbolic period stays equal to two**.

## 3. Standard transfer-operator flat traces give a positive contribution per orbit

For the usual holomorphic weighted-composition transfer operator associated with a Fuchsian branch map,

\[
(\mathcal L_s f)(x)
=\sum_{F(y)=x}|F'(y)|^{-s}f(y),
\]

a hyperbolic periodic orbit corresponding to \(\gamma\) contributes to the flat trace of the appropriate iterate by the standard fixed-point expression

\[
\boxed{
\tau_s(\gamma)
=
\frac{e^{-s\ell(\gamma)}}{1-e^{-\ell(\gamma)}}
}
\]

(up to the conventional orientation/multiplicity normalization, which is irrelevant here).  Equivalently, the denominator is the one-dimensional determinant of \(I-D F^m\) at the attracting fixed point.

For real \(s>0\) and \(L\in[A,B]\),

\[
\tau_s(L)
\ge
\frac{e^{-sB}}{1-e^{-B}}
=:c_{s,J}>0.
\]

All the period-two separators therefore contribute with the same sign and a uniform positive lower bound to the flat trace of \(\mathcal L_s^2\).  Hence

\[
\boxed{
\operatorname{tr}_{\rm flat}(\mathcal L_s^2)=+\infty
\qquad(s>0)
}
\]

for the direct canonical side-pairing coding.

The conclusion does not use the geodesics with \(L\to0\), their iterates, or the positive-length accumulation of longer symbolic words.  The fixed second iterate already diverges.

## 4. Functional-analytic obstruction

The standard Mayer/Bowen--Series transfer-operator mechanism obtains a nuclear operator (often nuclear of order zero) for which the Fredholm determinant is expanded by traces

\[
\det(1-\mathcal L_s)
=
\exp\left(
-\sum_{m\ge1}\frac1m\operatorname{tr}\mathcal L_s^m
\right).
\]

If \(\mathcal L_s\) were nuclear/trace-class in a Banach/Hilbert realization compatible with the geometric flat-trace formula above, then \(\mathcal L_s^2\) would also have a finite trace.  The preceding positive divergence contradicts this.

Therefore

\[
\boxed{
\text{no direct canonical countable side-pairing transfer operator can be
nuclear/trace-class while faithfully coding these periodic words.}
}
\]

This is logically independent of PF-070's failure of uniform expansion.  Even a hypothetical non-uniform countable Markov realization cannot simply keep the canonical local branches and hope that nuclearity survives.

## 5. Bounded-block accelerations do not fix the obstruction

A standard acceleration groups only a bounded amount of local symbolic data except in specifically identified parabolic excursions.  Any such bounded-block recoding sends the canonical two-letter separator family to periodic words of symbolic period bounded by some fixed \(M\).

By the pigeonhole principle, infinitely many of the separators then have the same recoded period \(m\le M\).  Their geometric fixed-point weights remain bounded below on \(J\), so

\[
\operatorname{tr}_{\rm flat}(\widetilde{\mathcal L}_s^m)=+\infty.
\]

Thus the obstruction survives every finite-memory/bounded-block acceleration.

One could assign arbitrarily long symbolic words to later occurrences solely to dilute their trace contribution.  But that is no longer a geometry-uniform Bowen--Series/Mayer recoding: it is an index-dependent renormalization.  Moreover PF-035 and PF-069 show that the ordinary periodic-orbit Euler product remains divergent even if one changes the symbolic presentation.

## 6. Relation to the distinguished cuffs

The primitive separator length in this family is controlled by three adjacent boundary spacings, hence asymptotically by three neighboring prime gaps.  The distinguished cuffs satisfy

\[
\ell_n
=2\log\frac{4p_n}{g_n}+o(1),
\]

so after removing their common large scale the relative cuff fluctuations determine the cross-ratio

\[
\chi=\frac{Y(X+Y+Z)}{XZ}
\]

and therefore the positive separator length

\[
L=4\operatorname{arsinh}\sqrt\chi.
\]

The transfer obstruction is therefore generated by the same multi-gap/cuff relations that survive the local-universality results for individual cuffs.

## 7. Novelty / prior-art audit

Known ingredients, not claimed as new:

- fixed-point trace formulas for holomorphic weighted-composition transfer operators;
- nuclear/order-zero Mayer/Bowen--Series transfer operators and Fredholm determinants for cofinite/geometrically finite Fuchsian groups;
- countable-state thermodynamic formalism for non-uniform systems;
- the exact relation between a hyperbolic multiplier and geodesic length.

In standard geometrically finite applications, the transfer-operator trace formula is a convergent sum over periodic words in a suitable half-plane, and cuspidal acceleration is used to restore uniform expansion around parabolic branches.  The literature does not appear to treat an infinitely generated flute with the present combination:

1. infinitely many distinct primitive hyperbolic periodic orbits;
2. all represented by a uniformly bounded (indeed two-letter) canonical symbolic word length;
3. their geometric lengths accumulating densely in a compact positive interval.

The abstract divergence argument is elementary once these three facts are present.  The substantive point for the prime-flute program is that PF-069 supplies them **inside the exact side-pairing geometry**, so the failure occurs at a fixed transfer iterate rather than only in the eventual Euler product.

## 8. Research consequence

This closes the natural escape left after PF-070:

\[
\boxed{
\text{abandon uniform expansion}
\;\not\Rightarrow\;
\text{retain a canonical non-uniform nuclear Mayer/Ruelle operator}.
}
\]

For the prime-flute, the standard options now separate as follows:

\[
\begin{array}{rcl}
\text{deterministic PSL(2,R) transport} &\to& \text{telescopes (PF-042)},\\
\text{strict uniformly expanding branching} &\to& \text{impossible (PF-070)},\\
\text{canonical countable non-uniform branching} &\to& \text{fixed-power trace divergence (PF-075)}.
\end{array}
\]

Any surviving transfer-like object must therefore alter the periodic-orbit trace itself: for example by a spatial/block renormalization forced by the tangent decomposition, or by subtracting an infinite positive-length background before taking traces.  Such a construction would be genuinely outside the standard Selberg/Mayer/Ruelle architecture and must be justified geometrically rather than introduced merely to restore convergence.
