# PL-390 — Besicovitch `B^2` continuation reaches the open strip but erases exact zero data

**Evidence:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-389`.

**Related findings:** `PL-001`, `PL-003`, `PL-005`, `PL-012`, `PL-389`.

**Status:** `THE-NATIVE-BESICOVITCH-B2-ESCAPE-LEFT-OPEN-BY-PL-389-DOES-EXTEND-THE-VERTICAL-ZETA-FUNCTION-THROUGHOUT-Re(s)>1/2-AS-A-MEAN-SQUARE-ALMOST-PERIODIC-HILBERT-VECTOR-WITH-FREQUENCIES--log(n)-AND-NORM-SQUARED-zeta(2sigma). HOWEVER-B2-IS-A-MEAN-SQUARE-QUOTIENT: ISOLATED-ZEROS-ON-A-FIXED-VERTICAL-LINE-CAN-BE-REMOVED-BY-CHANGING-THE-REPRESENTATIVE-ON-A-NULL-SET-WITHOUT-CHANGING-THE-B2-ELEMENT. THUS-NO-INVARIANT-OF-THE-B2-CLASS-ALONE-CAN-DETECT-WHETHER-zeta(sigma+it)-HAS-AN-OFF-CRITICAL-ZERO. MOREOVER-B2-IS-NOT-A-POINTWISE-BANACH-ALGEBRA, SO-THE-COBURN--DOUGLAS-INVERTIBILITY/INDEX-MECHANISM-DOES-NOT-EXTEND-NATIVELY. THE-BOUNDARY-sigma=1/2-IS-THE-CLASSICAL-MEAN-SQUARE/SQUARE-SUMMABILITY-WALL, NOT-AN-RH-SENSITIVE-INDEX-TRANSITION. RESTORING-ANALYTIC-ZERO-INFORMATION-REQUIRES-EXTRA-STRUCTURE; GENERALIZED-ANALYTIC-ALMOST-PERIODIC-JENSEN/MEAN-MOTION-THEORY-FOR-zeta-IS-ALREADY-CLASSICAL-BORCHSENIUS--JESSEN-PRIOR-ART`.

## Claim

Let

\[
Z_\sigma(t)=\zeta(\sigma+it).
\tag{PL390-1}
\]

For every fixed `sigma>1/2`, the vertical zeta function defines a Besicovitch mean-square almost-periodic element. For `1/2<sigma<1`, its Bohr--Fourier coefficients are

\[
\widehat Z_\sigma(-\log n)=n^{-\sigma},\qquad n\ge1,
\tag{PL390-2}
\]

with all other coefficients zero, and Parseval gives

\[
\boxed{
\|Z_\sigma\|_{B^2}^2
=
\sum_{n\ge1}n^{-2\sigma}
=
\zeta(2\sigma).
}
\tag{PL390-3}
\]

Thus the weakening from uniform almost periodicity in `PL-389` to Besicovitch `B^2` genuinely crosses `Re(s)=1`: it retains the prime-lattice frequency spectrum throughout the open half-plane `Re(s)>1/2`.

But this does **not** provide an RH-sensitive replacement for the almost-periodic index. The decisive obstruction is structural:

\[
\boxed{
\text{pointwise zero-freeness is not an invariant of a }B^2\text{ equivalence class.}
}
\tag{PL390-4}
\]

Consequently no construction depending only on the native `B^2` Hilbert element can distinguish a vertical zeta line containing isolated zeros from the same element represented by a function in which those values have been changed. Any successful zero-sensitive extension must therefore add structure not present in `B^2` itself, such as a distinguished analytic representative, a Jensen/subharmonic object, a target-relative compression, or another operator domain carrying pointwise analytic information.

## 1. The `B^2` escape really does reach `Re(s)>1/2`

The classical mean-square theorem for zeta states that for fixed `sigma>1/2`,

\[
\lim_{T\to\infty}
\frac1T\int_1^T|\zeta(\sigma+it)|^2\,dt
=
\zeta(2\sigma).
\tag{PL390-5}
\]

A standard source is E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. revised by D. R. Heath-Brown, Theorem 7.2. An audit-friendly modern formulation directly in Besicovitch language is Kevin Smith, “An application of functional analysis to the Riemann zeta function,” arXiv:2312.01376: in Section 3 he proves that `zeta(sigma+it)` belongs to `B^2` for `1/2<sigma<1` and computes the generalized Fourier coefficients exactly as in (PL390-2). The `sigma>1` part is already uniformly almost periodic by absolute convergence.

The frequencies in (PL390-2) are precisely

\[
-\log n=-\langle v(n),(\log p)_p\rangle,
\tag{PL390-6}
\]

so this is a genuine continuation of the prime-exponent frequency representation, not a formal use of the Dirichlet series outside its half-plane of ordinary convergence. The analytically continued zeta function and its Dirichlet polynomials agree in the `B^2` mean-square completion even though the pointwise Dirichlet series no longer converges there.

Equation (PL390-3) also identifies what is special about `1/2` in this Hilbert geometry. As `sigma` decreases to `1/2`,

\[
\zeta(2\sigma)\longrightarrow\infty.
\tag{PL390-7}
\]

On the critical line itself the classical second moment grows like `T log T`, so `Z_{1/2}` does not have finite `B^2` norm. Hence the half-line is a sharp **mean-square/square-summability boundary** for this representation. Nothing in this norm transition distinguishes an RH world from a non-RH world: it is already forced by the coefficient mass `sum n^{-2sigma}`.

This is the first control against overinterpreting the appearance of `1/2`. The boundary is natural, but it is the same Hilbert threshold already visible in the standard Bohr/Hardy coefficient geometry of `PL-001`.

## 2. Native `B^2` cannot see isolated off-critical zeros

Besicovitch `B^2` is not a space of pointwise functions with distinguished values. It is the completion of trigonometric polynomials in the mean-square seminorm, modulo seminorm-zero functions. In particular, changing a representative on a Lebesgue-null set leaves the `B^2` element unchanged.

Fix `sigma>1/2`, `sigma != 1`, and suppose that the analytic function

\[
t\longmapsto Z_\sigma(t)
\]

has one or more zeros. Since zeta is not identically zero, the zeros on this fixed vertical line are isolated, hence form a discrete and therefore measure-zero subset

\[
E_\sigma=\{t\in\mathbb R:\zeta(\sigma+it)=0\}.
\tag{PL390-8}
\]

Define another representative by

\[
\widetilde Z_\sigma(t)=
\begin{cases}
Z_\sigma(t),&t\notin E_\sigma,\\
1,&t\in E_\sigma.
\end{cases}
\tag{PL390-9}
\]

Then

\[
\|\widetilde Z_\sigma-Z_\sigma\|_{B^2}=0,
\tag{PL390-10}
\]

so

\[
[\widetilde Z_\sigma]_{B^2}=[Z_\sigma]_{B^2},
\tag{PL390-11}
\]

while `widetilde Z_sigma` has no zeros at the points in `E_sigma`.

Therefore the proposition

\[
\exists t:\ Z_\sigma(t)=0
\tag{PL390-12}
\]

is **not well-defined on the native `B^2` quotient**. This is stronger than saying that a particular proposed index has not yet been found. It is an information-loss statement: no functional, spectrum, distance, norm, or other invariant depending only on the `B^2` equivalence class can recover the exact presence of an isolated zero on that line.

RH is an all-zeros statement. A single zero with `Re(rho)>1/2` falsifies it. Such a violation can therefore be invisible to a linewise `B^2` invariant even though the entire vertical zeta function has a perfectly valid `B^2` representative. To recover the lost information one must use something beyond the quotient, most naturally the fact that the representative comes from one meromorphic function of the complex variable `s`.

## 3. Prime twists and generic frequencies give the same Hilbert obstruction

The line-specific control from the research mandate makes the loss of arithmetic rigidity even clearer. In `B^2`, Parseval identifies the native Hilbert geometry with the square-summable Fourier coefficients. Replacing

\[
n^{-\sigma}
\quad\text{by}\quad
\chi(n)n^{-\sigma},
\qquad |\chi(n)|=1,
\tag{PL390-13}
\]

preserves every coefficient norm and every inner product after applying the corresponding diagonal unitary. In the prime-lattice language this includes completely multiplicative phase twists generated independently on prime coordinates.

Such twists are precisely the kind of Helson/vertical-limit control already used in `PL-003` and `PL-012`: their analytic zero and continuation behavior can differ radically while the coefficient `B^2` geometry remains unitarily equivalent. Likewise, replacing the numerical frequency set `{-log n}` by any distinct labels carrying the same square-summable coefficient sequence gives an abstractly isometric Hilbert vector. The native `B^2` norm therefore retains the additive energy labels but does not, by itself, convert the special arithmetic of the rational primes into zero localization.

This does not say that the frequency labels are mathematically irrelevant. Analytic continuation and the relation between values at different `sigma` use them. The narrower conclusion is that **the Hilbert quotient and its coefficient metric alone do not contain the target-sensitive information** demanded by RH.

## 4. `B^2` also loses the multiplicative algebra needed by the `PL-387`--`PL-389` index

The Coburn--Douglas route used a bounded almost-periodic `C*`-algebra, where multiplication, invertibility, and the connected components of the invertible group are native objects. Passing to `B^2` destroys that setting: the full `B^2` Hilbert space is not closed under pointwise multiplication.

A concrete control already appears inside the periodic subspace. Let `h` be `2pi`-periodic and near `0` satisfy

\[
h(t)=|t|^{-\alpha}
\]

with

\[
\frac14\le\alpha<\frac12.
\tag{PL390-14}
\]

Then `h` is square-integrable over a period and hence defines a periodic `B^2` element, because `2alpha<1`. But

\[
|h(t)^2|^2=|t|^{-4\alpha}
\]

is not locally integrable at `0`, because `4alpha>=1`. Thus `h^2` is not even in the same mean-square class. Therefore

\[
\boxed{B^2\cdot B^2\not\subset B^2.}
\tag{PL390-15}
\]

So there is no native analogue of the unital `AP(R)` invertible group on which the mean-motion/Fredholm index of `PL-387`--`PL-389` lived. One can of course choose a multiplier algebra, impose boundedness, use an unbounded affiliated operator, or construct a different Fredholm problem, but each such move is additional structure and must be audited independently. Merely saying “replace uniform AP by Besicovitch AP” does not continue the old index.

## 5. The analytic repair is classical prior art

The loss of pointwise zeros in the mean-square quotient was not historically the end of almost-periodic methods for zeta. The relevant repair is classical and substantially richer than linewise `B^2`.

Vibeke Borchsenius and Børge Jessen, “Mean motions and values of the Riemann zeta function,” *Acta Mathematica* **80** (1948), 97--166, DOI `10.1007/BF02393647`, develop the Jensen function, mean motions, and zeros of **generalized analytic almost-periodic functions** and then apply that machinery to the Riemann zeta function and its logarithm in their Chapter II. A modern survey by Wei-Shih Du, Marko Kostić and Manuel Pinto, “Almost Periodic Functions and Their Applications: A Survey of Results and Perspectives,” *Journal of Mathematics* (2021), Article 5536018, explicitly points to Borchsenius--Jessen for mean motions and zeros of generalized almost-periodic analytic functions and their zeta applications.

This prior art matters conceptually. Once a distinguished analytic representative and its subharmonic/Jensen data are restored, zeros become meaningful again; but the zero sensitivity then comes from the **analytic structure added on top of the mean completion**, not from the `B^2` Hilbert class itself. Reconstructing “mean motion plus zeros” in the critical strip is therefore not a new prime-lattice mechanism unless it supplies an additional arithmetic rigidity absent from the classical Jessen theory.

The Borchsenius--Jessen machinery does not prove RH and is not cited here as a zero-localization theorem. Its role is the novelty boundary: the obvious way to repair `B^2` zero-blindness by keeping analytic Jensen/mean-motion information is already classical prior art.

## 6. Prior-art and novelty audit

The following ingredients are prior art:

- Besicovitch's mean-square almost-periodic Hilbert space and Parseval theory: A. S. Besicovitch, “On Generalized Almost Periodic Functions,” *Proceedings of the London Mathematical Society* (2) **25** (1926), 495--512, DOI `10.1112/plms/s2-25.1.495`;
- the zeta second-moment theorem for fixed `sigma>1/2`: Titchmarsh, 2nd ed., Theorem 7.2;
- the explicit statement `zeta(sigma+it) in B^2` with frequencies `-log n` in the open right half of the critical strip: Smith, arXiv:2312.01376, especially Sections 2--3;
- generalized analytic almost-periodic Jensen/zero theory applied to zeta: Borchsenius--Jessen (1948).

No novelty is claimed for these theorems. The exact derived Mathia delta is the route-specific impossibility statement (PL390-4)/(PL390-11): **the native `B^2` quotient that successfully carries the analytically continued vertical zeta function into `Re(s)>1/2` is intrinsically unable to remember isolated zeros, and it also lacks the multiplicative algebra required by the previous Fredholm-index mechanism.**

A targeted literature audit found active modern use of `B^2` for zeta moments (Smith 2023) and classical generalized almost-periodic zero theory (Borchsenius--Jessen), but no theorem converting the bare `B^2` equivalence class into an RH-sensitive zero detector. Such a detector would contradict the elementary null-set argument unless it used additional representative/analytic data.

## Boundaries and falsification tests

This finding does **not** rule out every Besicovitch- or mean-almost-periodic approach. It rules out a narrower but natural escape from `PL-389`: replacing the bounded `AP(R)` symbol algebra by the native linewise `B^2` Hilbert quotient and expecting its intrinsic geometry or a direct continuation of the old invertibility index to detect RH.

The decisive falsification test for any claimed `B^2`-native RH invariant is simple: modify the proposed vertical representative at every isolated zero, as in (PL390-9). If the readout is unchanged, it cannot encode exact zero-freeness. If the readout changes, then it is not a well-defined invariant of the `B^2` element and the extra pointwise/analytic structure must be stated explicitly.

A second mandatory control is the Helson/generic-frequency test from the line mandate. If the proposed readout depends only on coefficient magnitudes, `B^2` inner products, or abstract Hilbert-space geometry, unimodular prime twists and matched generic frequency systems remain indistinguishable even though their analytic zero behavior need not agree.

## Consequence for the research line

`PL-389` left Besicovitch/Stepanov classes as a possible way to enlarge the bounded almost-periodic symbol class. The `B^2` branch can now be separated cleanly into two statements:

\[
\boxed{
\text{analytic continuation to }\Re s>1/2
\ \Longrightarrow\ 
\text{successful mean-square prime-frequency representation},
}
\]

but

\[
\boxed{
\text{native }B^2\text{ geometry}
\ \not\Longrightarrow\ 
\text{exact zero-freeness or an RH-sensitive Fredholm index}.
}
\]

The surviving almost-periodic direction must therefore add a zero-sensitive analytic or target-relative structure that is not erased by mean-square quotienting and is not already exhausted by classical Borchsenius--Jessen mean-motion theory. The useful target is no longer “find a weaker almost-periodic class containing zeta”; that part is known. The target is to identify a **new arithmetic rigidity attached to the distinguished analytic representative** that survives the line's Helson, generic-frequency, and universality controls and can distinguish the rational-prime zeta function from its flexible phase-twisted analogues.