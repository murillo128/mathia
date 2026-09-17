# AF-388 — Shrinking solid PF3 tests exclude quadratic PF2-boundary contact

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `TOEPLITZ` · `MULTISCALE` · `BOUNDARY-RIGIDITY` · `NO-NOVELTY-CLAIM`

## Claim

AF-387 leaves open whether one continuous profile tested on arbitrarily fine lattices can realize the fixed-grid degeneracy that defeats nonstrict solid `PF_3` recognition. Multiscale consistency does impose an additional exact constraint.

Let

\[
f:\mathbb R\to(0,\infty)
\]

be `C^8`, let `h_m>0` with `h_m\to0`, and for every `m` and every integer `d` suppose the solid Toeplitz minors

\[
C_{2,m}(d)
:=
\det\!\left(f((d+i-j)h_m)\right)_{i,j=0}^{1}
\ge0,
\tag{1}
\]

and

\[
C_{3,m}(d)
:=
\det\!\left(f((d+i-j)h_m)\right)_{i,j=0}^{2}
\ge0.
\tag{2}
\]

Write

\[
g=\log f,
\qquad
q=-g''.
\tag{3}
\]

Then:

1. `q(x)\ge0` for every `x`;
2. for every `x`,

\[
2q(x)^3-q(x)q''(x)+q'(x)^2\ge0;
\tag{4}
\]

3. every zero of `q` is flatter than a nondegenerate quadratic contact:

\[
q(x_0)=0
\quad\Longrightarrow\quad
q''(x_0)=0.
\tag{5}
\]

Where `q>0`, `(4)` is equivalently

\[
(\log q)''\le 2q.
\tag{6}
\]

Thus the same nonstrict solid order-two/order-three data that fail on a single lattice acquire extra boundary information when required consistently along `h_m\to0`. AF-393 now shows that on the strictly positive stratum `q>0`, `(6)` already integrates to every finite order-three placement condition and hence gives continuum `TN_3`. The unresolved part is the boundary where `q=0`; `(5)` excludes the simplest smooth lower-order degeneracy that could support an AF-387-type placement alias.

## Local solid-minor expansions

For a real center `x` and mesh `h`, define

\[
D_2(x,h)
=
\det
\begin{pmatrix}
f(x)&f(x-h)\\f(x+h)&f(x)
\end{pmatrix}
\tag{7}
\]

and

\[
D_3(x,h)
=
\det\!\left(f(x+(i-j)h)\right)_{i,j=0}^{2}.
\tag{8}
\]

A direct Taylor expansion after factoring the common positive powers of `f(x)` gives

\[
\frac{D_2(x,h)}{f(x)^2}
=
-g''(x)h^2
-
\left(\frac{g^{(4)}(x)}{12}+\frac{g''(x)^2}{2}\right)h^4
+o(h^4),
\tag{9}
\]

and

\[
\frac{D_3(x,h)}{f(x)^3}
=
R(x)h^6+S(x)h^8+o(h^8),
\tag{10}
\]

where

\[
R=(g''')^2-g''g^{(4)}-2(g'')^3
=2q^3-qq''+(q')^2,
\tag{11}
\]

and

\[
S=
-4(g'')^4
-4(g'')^2g^{(4)}
+3g''(g''')^2
-\frac16 g''g^{(6)}
+\frac12 g'''g^{(5)}
-\frac13(g^{(4)})^2.
\tag{12}
\]

The absence of `g'` is the expected exponential-tilt invariance of Toeplitz minor signs.

## Dense-center passage

Fix `x\in\mathbb R`. For each `m`, choose an integer `d_m` nearest to `x/h_m` and put

\[
x_m=d_mh_m,
\qquad
|x_m-x|\le \frac{h_m}{2}.
\tag{13}
\]

Then `x_m\to x`, while `(1)` and `(2)` say exactly that

\[
D_2(x_m,h_m)\ge0,
\qquad
D_3(x_m,h_m)\ge0.
\tag{14}
\]

Divide the first inequality by the positive quantity `f(x_m)^2h_m^2` and use `(9)` uniformly on a compact neighborhood of `x`. Passing to the limit gives

\[
-g''(x)=q(x)\ge0.
\tag{15}
\]

Likewise, dividing the second inequality by `f(x_m)^3h_m^6` and using `(10)` gives

\[
R(x)=2q(x)^3-q(x)q''(x)+q'(x)^2\ge0,
\tag{16}
\]

which proves `(4)`.

The key point is that these are not inequalities at a fixed sampled set of centers. The vanishing mesh makes the sampled centers dense enough that the leading infinitesimal solid determinants become pointwise differential constraints.

## The next-order boundary obstruction

The leading order `(16)` alone does not constrain a zero of `q`: because `q\ge0`, if `q(x_0)=0` then automatically `q'(x_0)=0`, so `R(x_0)=0`.

The multiscale condition nevertheless retains one more order of information. Let

\[
a=q''(x_0)\ge0.
\tag{17}
\]

Assume for contradiction that `a>0`. With

\[
\delta_m=x_m-x_0,
\qquad
r_m=\frac{\delta_m}{h_m},
\qquad
|r_m|\le\frac12,
\tag{18}
\]

Taylor expansion of `q` around its nonnegative minimum gives

\[
q(x_m)=\frac a2\delta_m^2+o(\delta_m^2),
\qquad
q'(x_m)=a\delta_m+o(\delta_m),
\tag{19}
\]

and hence

\[
R(x_m)=\frac{a^2}{2}\delta_m^2+o(\delta_m^2).
\tag{20}
\]

At the exact zero `x_0`, `g''=g'''=0` and `g^{(4)}=-a`, so `(12)` reduces to

\[
S(x_0)=-\frac{a^2}{3}.
\tag{21}
\]

Using `(10)`, `(18)`--`(21)`, and continuity of `S`,

\[
\frac{D_3(x_m,h_m)}{f(x_m)^3h_m^8}
=
a^2\left(\frac{r_m^2}{2}-\frac13\right)+o(1).
\tag{22}
\]

But `|r_m|\le1/2`, so uniformly

\[
\frac{r_m^2}{2}-\frac13
\le
\frac18-\frac13
=-\frac5{24}<0.
\tag{23}
\]

For all sufficiently large `m`, `(22)` is therefore negative, contradicting `(14)`. Thus `a=0`, proving `(5)`.

The nearest-grid uncertainty is not a nuisance here: its worst possible displacement still leaves a strict negative margin `-5/24`. This is precisely why the conclusion survives without requiring any lattice point to hit `x_0` exactly.

## What this repairs from AF-387

AF-387 constructs a fixed discrete sequence with full `PF_2`, connected support, and all solid order-three minors nonnegative, yet with a negative non-solid order-three minor. Its lower-order degeneracy lives on an interior boundary where some order-two minors vanish.

AF-388 proves that not every smooth analogue of such a boundary can persist through a vanishing family of lattices. If the lower-order logarithmic curvature

\[
q=-(\log f)''
\tag{24}
\]

reaches zero with ordinary quadratic contact, the next term of the solid `3x3` determinant necessarily turns negative at sufficiently fine scale. Requiring the compressed solid certificate at many scales therefore recovers information that one fixed lattice loses.

This is a concrete arithmetic-fidelity mechanism: **multiscale consistency can act as a lift of a lossy local certificate**. AF-393 shows that the lift is complete on the strictly positive curvature stratum: there `(6)` is already equivalent to full continuum `TN_3`. What remains incomplete is the treatment of curvature-zero boundary strata, whose local information is measured here through the order of contact with the lower-order boundary.

## What remains open

AF-393 closes the strictly positive branch: when `q>0` everywhere, the pointwise inequality `(6)` extracted from shrinking solid tests is sufficient for continuum `TN_3`.

The unresolved regime is therefore concentrated at zeros of `q`. AF-389 excludes every finite-order zero under the same multiscale hierarchy, while AF-390 and AF-391 give separate sufficient boundary closures under quasianalyticity and curvature-shape hypotheses. The remaining sharp question is whether smooth infinitely-flat zero-curvature strata can pass the full shrinking-mesh solid hierarchy while still hiding a negative non-solid order-three minor, or whether an exact limiting form of the AF-393 mass-coordinate argument closes that boundary as well.

No claim is made here about orders `k>3`.

## Prior-art and novelty audit

The surrounding recognition theory is classical and substantial.

- H. F. Weinberger, **“A Characterization of the Polya Frequency Functions of Order 3,”** *Applicable Analysis* **15**(1--4) (1983), 53--69, DOI `10.1080/00036818308839439`. Role: direct classical `PF_3` characterization territory; this finding is not offered as a replacement characterization of `PF_3`.
- M. Gasca and J. M. Peña, **“Characterizations and Decompositions of Almost Strictly Positive Matrices,”** *SIAM Journal on Matrix Analysis and Applications* **28**(1) (2006), 1--8, DOI `10.1137/050631203`. Role: reduced recognition on structured nonstrict total-positivity strata and the natural comparison for boundary information beyond strict positivity.
- S. Launois and T. H. Lenagan, **“Efficient Recognition of Totally Nonnegative Matrix Cells,”** *Foundations of Computational Mathematics* **14** (2014), DOI `10.1007/s10208-013-9169-5`. Role: emphasizes that nonstrict total nonnegativity is stratified by cell/zero-pattern information and does not admit the naive strict-recognition shortcut globally.
- Christian Grussler and Tobias Damm, **“Efficient `k`-Sign Consistency Verification of Hankel Matrices via Schur Polynomials,”** arXiv:`2602.08122` (2026). Role: recent consecutive-row/structured-minor recognition results extending to Toeplitz settings, and the immediate modern context of AF-383--AF-387.

A targeted search of these neighboring literatures did not identify this exact shrinking-mesh differential consequence. **No broad novelty claim is made.** The durable Mathia result is the explicit implication `(5)` from its multiscale solid-certificate setup and the resulting separation between fixed-lattice and vanishing-mesh information loss.

## Riemann-facing boundary

This finding has no direct RH consequence and introduces no arithmetic source. It is upstream theory about whether a compressed determinant certificate can retain enough structure to recognize a stronger target.

If a later prime-derived kernel supplies nonnegative solid minors at a hierarchy of increasingly fine arithmetic scales, AF-388 says those signs carry more than independent fixed-grid information: they constrain how the kernel may touch the log-concavity boundary. By AF-393, if that source also yields strict positive curvature, the same multiscale signs already force the full order-three translation target. This is useful only after the arithmetic construction itself has supplied the required signs; it must not be read backward as evidence that such a prime kernel exists.

## Boundaries and falsification checks

Strict positivity of `f` is used to define `g=\log f` and divide by powers of `f`. The result does not cover kernels with zeros without additional local treatment.

`C^8` regularity is sufficient for the displayed expansion through order `h^8` with a local Peano remainder. Weaker regularity may suffice for parts of the argument, but is not claimed.

Both solid orders two and three are used. Order two supplies `q\ge0`; order three supplies `(4)` and the next-order contradiction at a zero of `q`.

The conclusion `q''(x_0)=0` is only a necessary condition. It does not show `q(x_0)>0` or by itself rule out quartic or infinitely flat contact. AF-393 independently closes the branch where `q` never vanishes; the boundary problem remains where the curvature reaches zero.

Finally, the proof depends on one fixed continuous profile being sampled on all meshes `h_m`. Unrelated discrete sequences at different resolutions need not satisfy any such compatibility and remain subject to the AF-387 obstruction.