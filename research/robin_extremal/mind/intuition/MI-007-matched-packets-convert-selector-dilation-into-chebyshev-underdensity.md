# MI-007 — Matched first-layer packets convert selector dilation into Chebyshev underdensity

**Evidence level:** supported by the exact matched-packet prime-set identity RE-068, the Robin timing-compression theorem RE-069, and the selector-dilation/Chebyshev calculation RE-070; no contradiction with known prime-distribution estimates is claimed.

The matched first-layer `0 -> 0` branch is exactly silent to every additive endpoint prime statistic. RE-068 shows that the physical first-layer labels crossed by the packet are precisely the ordinary primes in the selector interval, so count, Chebyshev mass, logarithmic weights, residue indicators, and other additive decorations agree identically between source and endpoint descriptions.

RE-069 then shows that direct positional transport of those primes to their delayed event coordinates is also too weak in the final Robin metric: each delay is compressed to an `O(p^{-2})` contribution and the whole future first-layer timing tax is absolutely summable.

RE-070 finds a different surviving coordinate **before** that final compression. At a tied common-amplitude breakpoint, parameterize the selector by logarithmic state `Y` and write `Z_c(Y)` for the adaptive tangent selector. On sufficiently late false-RH blocks,

\[
Z_c'(Y)-1
=
b(1-b)a_c(Y)\log Y
\left(1+O_J\!\left(\frac1{\log Y}+a_c(Y)\log Y\right)\right)>0.
\]

Thus the selector interval is longer than the logarithmic state interval. But the matched prime-set identity fixes its exact Chebyshev mass:

\[
\vartheta(Z_+)-\vartheta(Z_-)=Y_+-Y_-.
\]

Combining the two gives

\[
\boxed{
[Z-\vartheta(Z)]_{Z_-}^{Z_+}
=(Z_+-Z_-)-(Y_+-Y_-)
>0.
}
\]

More precisely the deficit is asymptotic to

\[
b(1-b)\int_{Y_-}^{Y_+}a_c(t)\log t\,dt.
\]

For sublinear packets, the induced relative underdensity is

\[
1-
\frac{\vartheta(Z_+)-\vartheta(Z_-)}{Z_+-Z_-}
\asymp
b(1-b)a_-(Y)\log Y,
\]

with a false-RH amplitude floor of order at least `Y^{-b}\log Y`.

The reusable lesson is that **exact conservation of source mass does not imply geometric neutrality**. A matched transformation can preserve the complete labeled multiset yet force that same mass to occupy a longer target interval. The informative variable is then density relative to the adaptive selector geometry, not another additive weight on the conserved atoms.

This also clarifies where the information survives. It is visible in the selector map before the Robin kernel compresses direct timing. A prime-distribution theorem capable of contradicting the matched branch must therefore control `vartheta` on these source-selected adaptive intervals at the scale of the dilation defect, not merely prove an ordinary relative `o(1)` error on generic intervals.

**Boundary.** RE-070 derives a necessary underdensity pattern under the false-RH matched first-layer hypotheses. The required relative deficit tends to zero, so current generic short-interval asymptotics need not contradict it. The result does not treat higher CA layers, prove such matched packets recur indefinitely, or prove RH.
