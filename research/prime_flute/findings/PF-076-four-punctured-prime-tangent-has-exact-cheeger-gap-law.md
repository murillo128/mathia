# PF-076 — the four-punctured prime tangent has an exact Cheeger gap law

**Status:** `EXACT-DERIVED + CANDIDATE-NEW-SPECIALIZATION`.

PF-074 gives an exact unmarked geometric invariant for the first nontrivial prime tangent.  If

\[
Y_r\cong S_{0,4},\qquad r=\frac{d_1}{d_2},\qquad q:=\min(r,r^{-1}),
\]

then its systole is

\[
\boxed{\operatorname{sys}(Y_r)=4a,\qquad a:=\operatorname{arsinh}\sqrt q.}
\]

This note shows that, for this family, the same prime-gap contrast determines the **Cheeger constant exactly** and therefore gives a non-asymptotic lower bound for the positive Laplace spectrum.  Combining that with the exact collar-capacity Ritz bound of PF-056 yields an explicit two-sided spectral enclosure depending only on the adjacent-gap contrast.

## 1. Cheeger minimizers on a cusped four-punctured sphere

The total area of every complete finite-area hyperbolic four-punctured sphere is

\[
\operatorname{Area}(S_{0,4})=4\pi.
\]

Benson, using the Adams--Morgan classification of isoperimetric minimizers, proves that a geometrically finite finite-area hyperbolic surface has a Cheeger minimizer among the standard isoperimetric candidates.  In the presence of cusps, metric disks and annuli do not occur; a horocusp has isoperimetric ratio exactly `1`; the remaining candidates are regions bounded by simple geodesics or by curves at a common constant distance from such geodesics.

Every essential simple closed geodesic on `S_{0,4}` separates the punctures as `2+2`.  Each side is therefore a pair of pants with two cusps and one geodesic boundary, hence Gauss--Bonnet gives

\[
\boxed{\operatorname{Area}(A)=\operatorname{Area}(A^c)=2\pi.}
\]

Thus a separating geodesic of length `L` has Cheeger ratio

\[
\frac{L}{2\pi}.
\]

Because `S_{0,4}` has complexity one, two distinct non-isotopic essential simple closed curves cannot be disjoint.  Hence a non-annular Cheeger candidate cannot gain anything by using several distinct essential geodesics: the relevant candidate is a single isotopy class.

## 2. Equidistant displacement can only increase the ratio

Let an essential geodesic have length `L`.  Moving its boundary a distance `s>=0` into one side gives an equidistant curve with

\[
\ell_s=L\cosh s.
\]

The smaller enclosed area is

\[
A_s=2\pi-L\sinh s
\]

for as long as this is the smaller-side representative.  Its isoperimetric ratio is

\[
R_L(s)=\frac{L\cosh s}{2\pi-L\sinh s}.
\]

Differentiating,

\[
\boxed{
R_L'(s)=
\frac{L\left(2\pi\sinh s+L\right)}
     {(2\pi-L\sinh s)^2}>0.
}
\]

Therefore the best candidate in every essential isotopy class is the geodesic itself, `s=0`.

The remaining competitor is a horocusp, with ratio `1`.  For the prime tangent, PF-074 gives

\[
\operatorname{sys}(Y_r)
=4\operatorname{arsinh}\sqrt q
\le4\operatorname{arsinh}1
<2\pi,
\]

so the systolic separator always beats the cusp candidate.

Consequently

\[
\boxed{
h(Y_r)=\frac{\operatorname{sys}(Y_r)}{2\pi}
      =\frac{2}{\pi}\operatorname{arsinh}\sqrt q.
}
\]

This identity is exact for every `r>0`.

## 3. Exact relation to the distinguished prime cuffs

For an occurrence of the same bounded three-prime pattern near scale `P`, the distinguished cuffs satisfy

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1).
\]

Hence

\[
\boxed{
q
=\min\left(\frac{d_1}{d_2},\frac{d_2}{d_1}\right)
=\lim_{P\to\infty}
 e^{-\frac12|\ell_1(P)-\ell_2(P)|}.
}
\]

Therefore the exact Cheeger law can be written directly as a law of relative cuff fluctuations:

\[
\boxed{
h(Y_r)=
\frac{2}{\pi}
\operatorname{arsinh}
\sqrt{
\lim_{P\to\infty}
 e^{-\frac12|\ell_1(P)-\ell_2(P)|}
}.
}
\]

It is better conceptually to regard `q` as the primary invariant: the common divergent `2 log P` part of the two cuffs cancels, and the remaining contrast becomes a global isoperimetric invariant of the tangent.

## 4. Non-asymptotic lower spectral bound

Cheeger's inequality applies to the first positive spectral value of the finite-area tangent:

\[
\lambda_1(Y_r)\ge\frac{h(Y_r)^2}{4}.
\]

Substituting the exact formula above gives

\[
\boxed{
\lambda_1(Y_r)
\ge
\frac{1}{\pi^2}
\operatorname{arsinh}^2\sqrt q.
}
\]

Thus a relative prime-gap/cuff contrast controls the positive Laplace spectrum **without taking a further pinching limit**.

This lower bound is not expected to be sharp in the strongly pinched regime: Burger's graph asymptotics give a first eigenvalue of order `sqrt(q)`, whereas the Cheeger lower bound is of order `q`.  Its value is that it is exact as an isoperimetric input and non-asymptotic.

## 5. Combine with PF-056 for a fully explicit two-sided spectral enclosure

Let

\[
L=\operatorname{sys}(Y_r)=4a,
\qquad a=\operatorname{arsinh}\sqrt q.
\]

The exact capacity of the full standard collar around a geodesic of length `L` is, by PF-056,

\[
\kappa(L)=\frac{L}{4\arctan(e^{-L/2})}
         =\frac{a}{\arctan(e^{-2a})}.
\]

The area of either half-collar is

\[
\frac{L}{\sinh(L/2)}
=\frac{4a}{\sinh(2a)}.
\]

Removing the half-collar from each of the two pants leaves equal core masses

\[
m(a)=2\pi-\frac{4a}{\sinh(2a)}.
\]

The two-core harmonic Ritz trial space therefore gives

\[
\lambda_1(Y_r)
\le\frac{2\kappa(L)}{m(a)}.
\]

Together with Cheeger,

\[
\boxed{
\frac{a^2}{\pi^2}
\le
\lambda_1(Y_r)
\le
\frac{2a}
{\arctan(e^{-2a})\left(2\pi-\frac{4a}{\sinh(2a)}\right)},
\qquad
a=\operatorname{arsinh}\sqrt q.
}
\]

Whenever the explicit upper bound is below `1/4`, it certifies an actual discrete `L^2` small eigenvalue of the tangent.  PF-034 then implants that eigenvalue into the essential spectrum of the infinite prime-flute for every recurrent isolated realization of the pattern.

The point of this enclosure is not numerical optimality.  Both sides are forced by canonical geometry:

- the lower bound uses the **exact Cheeger minimizer**;
- the upper bound uses the **exact harmonic capacity of the systolic collar**.

No generating function or graph weight is chosen from the prime gaps by hand.

## 6. Interior/exterior and orthogonal-circle geometry

The quantity `q` is the Möbius-invariant adjacent-gap contrast already arising from the exact orthogonal-circle construction.  Reversing the orientation of the tangent exchanges `r` and `1/r`, hence leaves `q` and the Cheeger law unchanged.  This is exactly the amount of information an unmarked geometric invariant can retain.

The ambient prime-circle interior/exterior duality likewise preserves the corresponding cross-ratio and therefore preserves `h(Y_r)` and the spectral enclosure.  No new asymmetric choice is introduced.

## 7. Novelty / prior-art audit

Known ingredients, not claimed as new:

- Adams--Morgan's classification of isoperimetric minimizers on geometrically finite hyperbolic surfaces;
- Benson's existence/classification/algorithm for Cheeger minimizers on finite-area geometrically finite hyperbolic surfaces;
- the fact that a horocusp has Cheeger ratio `1`;
- Cheeger's inequality;
- systole theory of the four-punctured sphere;
- exact hyperbolic collar geometry and capacity estimates.

A directed search for `four-punctured sphere + Cheeger constant + systole` and variants did not locate the explicit identity

\[
h(S_{0,4})=\operatorname{sys}(S_{0,4})/(2\pi)
\]

for this family, nor the prime-gap specialization above.  However, the Cheeger identity is an elementary corollary of the known Adams--Morgan/Benson classification once one uses the complexity-one topology of `S_{0,4}`.  Historical priority should therefore **not** be claimed without a broader literature audit.

The potentially new content is narrower: the exact composition

\[
\text{adjacent prime-gap / cuff contrast}
\to
\text{global systole}
\to
\text{exact Cheeger constant}
\to
\text{two-sided non-asymptotic Laplace enclosure},
\]

inside the genuine prime-derived tangent geometry.

## 8. Research consequence

PF-047/PF-054 describe the **asymptotic** small spectrum when several prime-derived necks pinch.  PF-076 supplies a complementary fact at the first nontrivial tangent:

\[
\boxed{
\text{one adjacent cuff contrast determines a global isoperimetric invariant exactly, for every modulus.}
}
\]

This gives a clean non-asymptotic benchmark for any future scattering/resonance or two-scale localization theory.  Any proposed effective operator for the four-punctured prime tangent should at minimum be compatible with the exact Cheeger lower bound and the exact collar-capacity upper bound above.
