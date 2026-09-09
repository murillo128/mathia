# RE-005 — regular self-tangent CA peak values are not globally monotone below the Robin barrier

**Status:** `EXACT-DERIVED + FINITE-INTERVAL-CHECKED + NEGATIVE/OBSTRUCTION + PEAK-CLASS-CONTROL + PRIOR-ART-BOUNDED`. `RE-001` gives the exact workload identity between regular self-tangent colossally abundant states, while `RE-002` proves that self-tangency alone is weaker than being a local maximum of Robin's quotient on the CA ladder. A proposed control suggested testing whether the workload might nevertheless have a universal nonpositive sign on the smaller class of regular self-tangent **local peaks**.

That strengthening is false already at finite scale. There are explicit regular self-tangent CA local peaks

\[
C_1=2021649740510400
\]

and

\[
C_2=1970992304700453905270400
\]

with `C_1<C_2`, both strictly below the Robin barrier, but

\[
\boxed{G(C_2)>G(C_1).}
\tag{1}
\]

More precisely,

\[
\boxed{
0.00377508388939487784974749692512
<\log\frac{G(C_2)}{G(C_1)}
<0.00377508388939487784974749692513.
}
\tag{2}
\]

Thus the exact workload from `RE-001` is positive between two genuine regular self-tangent local peaks. Any RH-facing sign theorem must use an additional asymptotic, barrier-conditioned, or source-selection hypothesis; it cannot assert nonpositive workload for every pair of regular self-tangent peaks.

## 1. Exact CA threshold test

Retain the prime-layer increment

\[
\lambda_{p,j}
=\log\frac{1-p^{-(j+1)}}{1-p^{-j}}
\]

and, for a candidate `n`, its intrinsic Robin tangent parameter

\[
\varepsilon(n)
=\frac1{\log n\,\log\log n}.
\tag{3}
\]

If `a_p` is the exponent of `p` in `n`, strict regular colossally abundance at this parameter is certified by

\[
\max_p\frac{\lambda_{p,a_p+1}}{\log p}
<\varepsilon(n)
<\min_{p\mid n}\frac{\lambda_{p,a_p}}{\log p},
\tag{4}
\]

where an omitted prime has exponent zero. The maximum over omitted primes is attained at the smallest omitted prime: for `j=1`,

\[
\frac{\lambda_{p,1}}{\log p}
=\frac{\log(1+1/p)}{\log p}
\]

is strictly decreasing for `p>1`. For each fixed prime, the layer increments decrease strictly with `j`, since

\[
\frac{1-p^{-(j+1)}}{1-p^{-j}}
=1+\frac{p-1}{p(p^j-1)}.
\tag{5}
\]

Consequently (4), together with finite comparison of the current and next layers of primes already present and the next omitted prime, also identifies the two adjacent CA transitions.

For

\[
C_1
=2^6 3^3 5^2 7^2\,11\,13\,17\,19\,23\,29\,31,
\tag{6}
\]

the adjacent CA states are

\[
A_1=\frac{C_1}{7}=288807105787200,
\qquad
B_1=3C_1=6064949221531200.
\tag{7}
\]

The last included layer is `(7,2)` and the next excluded layer is `(3,4)`. Direct interval evaluation gives

\[
0.00755389585597668360233907875693
<\varepsilon(C_1)
<0.00909578333202773187684676033987,
\tag{8}
\]

with

\[
\varepsilon(C_1)
=0.00796536276012844808345355307935\ldots.
\]

Thus `C_1` is a regular self-tangent CA state. Its two neighboring Robin comparisons are strictly positive:

\[
\boxed{
0.00162687690489036652339455673965
<\log\frac{G(C_1)}{G(A_1)},
}
\tag{9}
\]

and

\[
\boxed{
0.000281502086459495350334862189038
<\log\frac{G(C_1)}{G(B_1)}.
}
\tag{10}
\]

Hence `C_1` is a strict local peak on the CA ladder.

For

\[
C_2
=2^7 3^4 5^2 7^2\,11\,13\,17\,19\,23\,29\,31\,37\,41\,43\,47\,53,
\tag{11}
\]

the adjacent states are

\[
A_2=\frac{C_2}{53}=37188534050951960476800,
\qquad
B_2=59C_2=116288545977326780410953600.
\tag{12}
\]

Here the last included layer is `(53,1)` and the next excluded layer is `(59,1)`. The strict tangent enclosure is

\[
0.00412187957746436510356574467758
<\varepsilon(C_2)
<0.00470799966832392458556035035548,
\tag{13}
\]

with

\[
\varepsilon(C_2)
=0.00444205330526517753053208614457\ldots.
\]

The local Robin comparisons again have positive margins:

\[
\boxed{
0.000229355677622306885329730125966
<\log\frac{G(C_2)}{G(A_2)},
}
\tag{14}
\]

and

\[
\boxed{
0.000524752672927722482008693788789
<\log\frac{G(C_2)}{G(B_2)}.
}
\tag{15}
\]

Thus `C_2` is also a strict regular self-tangent CA local peak.

## 2. Both peaks are safely below the Robin barrier

The abundance factor

\[
\rho(n)=\frac{\sigma(n)}n
\]

is an exact rational number for each displayed factorization. Evaluating only the remaining logarithms by outward interval arithmetic gives

\[
\boxed{
\gamma-\log G(C_1)
>0.02514045525298677327550055643827,
}
\tag{16}
\]

and

\[
\boxed{
\gamma-\log G(C_2)
>0.02136537136359189542575305951314.
}
\tag{17}
\]

Therefore the positive peak-to-peak increment (2) occurs while both endpoints remain well inside the Robin-safe region. It is not a finite counterexample to Robin's inequality and supplies no evidence that the barrier itself is crossed.

Combining (2) with the exact `RE-001` packet identity, the signed workload between these two self-tangent endpoints satisfies

\[
\boxed{
\int_{\log C_1}^{\log C_2}D(x)g'(x)\,dx
=\log\frac{G(C_2)}{G(C_1)}>0.
}
\tag{18}
\]

The failure is therefore a failure of universal sign, not of the workload representation.

## 3. The original safe witnesses were self-tangent but not peaks

The proposed control that triggered this audit used

\[
720720
\quad\text{and}\quad
6983776800.
\]

Their positive endpoint-to-endpoint workload is real, and both satisfy strict regular self-tangent CA inequalities. However they do **not** establish peak-level nonmonotonicity.

Indeed the immediate predecessor of `720720` is `55440`, and interval evaluation gives

\[
\log\frac{G(720720)}{G(55440)}
<-0.01043610579894056545003218562131.
\tag{19}
\]

Likewise the immediate successor of `6983776800` is `160626866400`, and

\[
\log\frac{G(6983776800)}{G(160626866400)}
<-0.00188400140298224614531448662395.
\tag{20}
\]

So those two states refute a sign claim on **all regular self-tangent states**, but not a sign claim restricted to the local/block maxima forced by `RE-001`. The pair `(C_1,C_2)` repairs that logical gap and gives the stronger peak-class control.

## 4. Audit and reproducibility boundary

All arithmetic comparisons above were reconstructed independently from the displayed factorizations. The `sigma(n)/n` factors were formed as exact rationals; prime-layer and Robin logarithms were evaluated with 60-decimal-digit interval arithmetic. The narrowest structural margins in (8) and (13) are about `3.2e-4`, while the interval widths are many orders of magnitude smaller. No inverse event-coordinate approximation is needed for the CA test.

The public CA sequence is consistent with the four neighboring triples in (7) and (12), but an external table is not used as proof: the factorized threshold criterion (4)--(5) identifies the adjacent transitions directly.

Alaoglu--Erdos supplies the classical prime-exponent threshold structure, Robin supplies the divisor-sum criterion and CA extremal setting, and the recent Mantovanelli workload preprint supplies the closest representation-level prior art for regular self-tangent states and (18). Those dependencies are already anchored in `SOURCES.md`.

Nonmonotonic behavior of `G` along the CA ladder is not claimed as new; literature and public CA computations already study increasing and decreasing consecutive CA ratios. A targeted search did not locate this exact two-peak self-tangent control, but the present result should be regarded primarily as a **proof-strategy obstruction/regression witness**, not as a deep standalone novelty claim.

## 5. Consequence for the research line

This finite obstruction does not rule out an **eventual** monotonicity theorem after some threshold, nor a theorem restricted to peaks sufficiently close to or above the Robin barrier. It also does not rule out a sign law using the extra secant-clearance geometry of `RE-002`, the prime/higher-layer dichotomy of `RE-004`, or another source-derived condition that is automatic on the hypothetical counterexample peaks furnished by `RE-001`.

What it does rule out is a tempting simplification: replacing the unresolved source-selection problem by the statement that regular self-tangent local peaks have globally nonincreasing Robin values. Positive workload can survive even after imposing genuine local maximality.

The live theorem must therefore expose an additional asymptotic selector. A useful continuation is to prove that the counterexample-peak class forced under RH failure eventually obeys a restriction absent from `(C_1,C_2)`, and then derive a sign/exclusion theorem from the prime-layer atoms under that restriction. Merely reimposing a universal workload sign on all regular self-tangent peaks is now falsified.