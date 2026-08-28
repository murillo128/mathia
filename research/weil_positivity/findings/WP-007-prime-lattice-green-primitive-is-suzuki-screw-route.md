# WP-007 — The canonical Green primitive of the Prime-Lattice Weil measure is Suzuki's screw-function route

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. WP-004 gives a canonical positive Prime-Lattice measure with atoms `Lambda(n)/sqrt(n)` at `log n`. A natural escape from WP-005 is to integrate this signed explicit-formula data twice and seek positivity of the resulting increment kernel, as one would for a Green kernel, resistance metric, or Hilbert-space screw arc. That continuation is canonical up to an affine gauge, but it is not a new Mathia positivity mechanism: its prime term is exactly the prime term in Masatoshi Suzuki's zeta screw function, and after the standard archimedean/pole completion the resulting increment-kernel positivity is equivalent to RH. Suzuki's 2026 operator realization further shows that the associated localized Weil form is already represented through a nonlocal/Friedrichs-extension construction. Thus the most direct Green-primitive / boundary-increment completion of the Prime-Lattice axis measure lands exactly in known Weil-equivalent prior art rather than producing positivity independently from geometry.

## 1. Claim

WP-004 produces the positive discrete measure

\[
\mu_{\rm axis}^{+}
=\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}
\quad\text{on }(0,\infty).
\tag{1}
\]

Define its even zero-Cauchy-data second primitive

\[
H_{\rm fin}(t)
:=\int_{(0,\infty)} (|t|-a)_+\,d\mu_{\rm axis}^{+}(a).
\tag{2}
\]

Because only atoms with `a<=|t|` contribute,

\[
\boxed{
H_{\rm fin}(t)
=\sum_{n\le e^{|t|}}
\frac{\Lambda(n)}{\sqrt n}\bigl(|t|-\log n\bigr).
}
\tag{3}
\]

Distributionally,

\[
H_{\rm fin}''
=\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}
\bigl(\delta_{\log n}+\delta_{-\log n}\bigr).
\tag{4}
\]

Equation (2) is not a hand-picked smoothing. It is the unique even primitive with

\[
H_{\rm fin}(0)=0,
\qquad
H_{\rm fin}'(0+)=0,
\tag{5}
\]

whose second derivative is (4). More generally, changing a second primitive by an affine function does not change the increment kernel considered below, so the integration constants are a pure gauge.

Suzuki's 2023 function `Psi(t)` is defined, for `t>=0`, by

\[
\begin{aligned}
\Psi(t)
&=4(e^{t/2}+e^{-t/2}-2)
-\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n)\\
&\quad+\frac t2\left[\psi\!\left(\frac14\right)-\log\pi\right]
+\frac14\left(C-e^{-t/2}\Phi(e^{-2t},2,1/4)\right),
\end{aligned}
\tag{6}
\]

and then extended evenly. Therefore its complete finite-prime term is **exactly**

\[
\boxed{\Psi_{\rm fin}(t)=-H_{\rm fin}(t).}
\tag{7}
\]

Let

\[
g(t):=-\Psi(t)
\tag{8}
\]

and form the canonical increment kernel

\[
G_g(t,u)
:=g(t-u)-g(t)-g(-u)+g(0).
\tag{9}
\]

Suzuki proves

\[
\boxed{
\mathrm{RH}
\iff
G_g\ \text{is positive semidefinite on all finite subsets of }\mathbb R.
}
\tag{10}
\]

Equivalently, `g` is a Krein screw function exactly under RH. He also proves the distribution identity

\[
\boxed{-g''=\Psi''=W,}
\tag{11}
\]

where `W` is the Weil distribution.

Hence the seemingly natural pipeline

```text
Prime-Lattice positive axis measure
    -> canonical second primitive / Green kernel
    -> add the forced completed non-prime terms
    -> increment-kernel positivity
```

is not an independent geometric proof architecture. It is exactly a continuous-kernel realization of the classical Weil positivity problem.

---

## 2. Why the primitive is forced by the Prime-Lattice axis measure

Write

\[
w_n=\frac{\Lambda(n)}{\sqrt n},
\qquad
a_n=\log n
\]

for prime powers. For one atom `w delta_a`, the even function

\[
h_a(t)=w(|t|-a)_+
\]

satisfies

\[
h_a''=w(\delta_a+\delta_{-a})
\]

in the sense of distributions. Summing locally finitely over the atoms meeting a compact interval gives (2)-(4).

This is exactly the Green inversion of the second derivative with the natural even zero data at the origin. In particular, there is no regularization parameter and no convergence issue at finite `t`: only prime powers `n<=e^{|t|}` occur.

The construction is therefore the most canonical way to convert the WP-004 coefficient measure into a continuous translation kernel while preserving the exact finite-place explicit-formula distribution after two derivatives.

The affine ambiguity of a second primitive cannot rescue or alter its positivity. If

\[
\ell(t)=at+b,
\]

then directly

\[
G_{g+\ell}(t,u)=G_g(t,u).
\tag{12}
\]

Thus choices of integration constants disappear from the increment geometry. Any genuinely different kernel has to change more than the primitive gauge.

---

## 3. Exact sign audit: the finite positive measure does not become a positive screw kernel

WP-004 positivity is positivity of the diagonal coefficient measure (1). Under the correct Weil sign, however, `g_fin=H_fin` by (7)-(8). Its contribution to the diagonal of the increment kernel is

\[
G_{g_{\rm fin}}(t,t)
=g_{\rm fin}(0)-2g_{\rm fin}(t)
=-2H_{\rm fin}(t).
\tag{13}
\]

For every `|t|>log 2`, at least the atom `n=2` contributes, so

\[
H_{\rm fin}(t)>0
\]

and therefore

\[
\boxed{G_{g_{\rm fin}}(t,t)<0.}
\tag{14}
\]

Thus the positive Prime-Lattice measure by itself gives the **wrong sign even on the diagonal** of the screw/increment kernel.

One could flip the primitive and take `-H_fin`; that would make the diagonal sign in (13) positive. But then

\[
-(-H_{\rm fin})''=+\mu_{\rm axis}^{\rm sym},
\]

whereas the finite-prime part of the Weil distribution has the opposite sign. The sign flip therefore ceases to represent the target functional.

This is the Green-kernel version of the obstruction already seen at two earlier levels:

```text
WP-004: coefficient measure is positive.
WP-005: exact autocorrelation lift is indefinite.
WP-007: exact second primitive has a finite screw-kernel contribution
        with negative diagonal; only the completed global kernel can recover
        positivity, and that positivity is exactly RH-equivalent.
```

---

## 4. The completed primitive is already Suzuki's zeta screw function

Equation (6) matters because it assembles exactly what the research line has been asking a global construction to supply:

- the finite prime-power term with weights `Lambda(n)/sqrt(n)`;
- the remaining completed terms coming from the gamma/pole sector of `xi`;
- a single continuous function whose second derivative is the full Weil distribution.

So the branch does not need to conjecture what the canonical twofold primitive of the completed explicit formula should look like. It is already explicit.

But its positivity is not independent. Suzuki combines the Fourier-transform identity

\[
\int_0^\infty \Psi(t)e^{izt}\,dt
=-\frac1{z^2}\frac{\xi'}{\xi}\left(\frac12-iz\right)
\tag{15}
\]

with Krein-Langer theory and Lagarias's Nevanlinna criterion to prove that `g=-Psi` belongs to the screw-function class if and only if RH holds. In particular, the Hilbert-space increment interpretation exists globally exactly when the desired theorem is true.

This is precisely the circularity boundary relevant to Mathia: the kernel is geometrically suggestive and canonical, but the missing positivity is **the RH-level statement itself**, not a theorem supplied by an independently known geometry.

---

## 5. The nonlocal/operator escape is also close prior art

A possible reaction to (10) is to keep the same continuous primitive but hope that a derivative, boundary condition, or Friedrichs extension supplies positivity from a more canonical operator theorem.

Suzuki's 2026 paper develops essentially this route for the localized Weil form. On a finite interval he represents the Weil quadratic form using the screw-function convolution kernel and a differential operator, and proves that the self-adjoint operator associated with the localized form is the Friedrichs extension of the corresponding symmetric nonlocal differential construction. The same paper then studies self-adjoint extensions of a first-order differential operator and their spectral interpretation.

This does not prove global positivity; rather, it shows that **passing from the screw kernel to a nonlocal/boundary operator is already part of current Weil-form prior art**. A Mathia proposal of the form

```text
axis measure -> twice-integrated kernel -> D* G D / boundary extension -> positivity
```

therefore needs an additional theorem that is not already equivalent to positivity of the Weil form. Merely recognizing the boundary/operator realization is not a new mechanism.

---

## 6. Relation to WP-005 and WP-006

WP-005 left open compression, boundary response, different-space geometry, and noncommutative completion as possible escapes from the commuting translation obstruction. WP-007 closes only a **specific** member of that family: the canonical translation-invariant second-primitive / screw-kernel realization and its direct nonlocal differential packaging.

It does not rule out all boundary or cohomological constructions. A successful escape must introduce genuinely additional structure before positivity is asserted, for example a quotient, compression, intersection theorem, adelic/cohomological object, or boundary law whose positivity is independently established and from which Suzuki/Weil positivity follows as a consequence.

WP-006 showed that the most naive Arakelov class completion instead kills the Prime-Lattice integer vectors because principal arithmetic divisors become class-trivial. WP-007 shows that retaining the prime-axis data and completing it analytically through the canonical Green primitive goes to the opposite extreme: it preserves the full Weil information, but its positivity is exactly the original RH-equivalent problem.

The two findings therefore bracket a useful design constraint:

```text
ordinary Arakelov class quotient:
    global completion -> loses the Prime-Lattice signal

canonical Green/screw completion:
    retains exact completed Weil signal -> positivity is RH itself

surviving target:
    a larger geometric object that retains the signal
    and has an independent positivity theorem.
```

---

## 7. Prior art and novelty assessment

No novelty is claimed for screw functions, Krein-Langer theory, the zeta screw function, the Weil distribution, or Suzuki's operator realizations.

- Suzuki (2023) explicitly defines `Psi` with the prime sum (3), proves `-g''=W`, and proves that `g=-Psi` is a screw function if and only if RH.
- Suzuki (2026) explicitly organizes the Weil quadratic form through this screw function and gives localized nonlocal/Friedrichs-extension and self-adjoint-extension realizations.
- Weil, Bombieri, Yoshida, Lagarias, Connes, and Connes--Consani supply the surrounding positivity/operator theory already audited elsewhere in this branch.

The Mathia-specific contribution is the exact identification of the **canonical Green primitive of the WP-004 Prime-Lattice axis measure** with Suzuki's finite prime term. That identification materially redirects the search: a particularly natural way of turning the lattice measure into a geometric increment kernel is not merely similar to known Weil positivity; it lands on the known screw-function formulation exactly.

---

## 8. Audit and falsification tests

The exact Mathia part can be audited without zero data:

1. start from the WP-004 measure (1);
2. compute its even Green primitive (2) and obtain (3);
3. differentiate distributionally to verify (4);
4. compare (3) with the finite prime term in Suzuki's defining formula (6);
5. verify the finite diagonal sign (13)-(14);
6. verify directly that affine changes of primitive disappear from (9).

The prior-art conclusion is falsified only if Suzuki's theorem does **not** identify positivity of (9) with RH, or if the finite term in (6) differs from (3) under the same centered normalization. Both are explicit in the cited primary source.

A future Mathia construction escapes rather than falsifies WP-007 if it uses the Prime-Lattice measure inside a genuinely different global space or operation with an independently proved positivity theorem, rather than asserting positivity of the canonical screw kernel or a direct operator repackaging of it.

## Consequence for the research line

The `WP-004 -> WP-005` escape through a continuous Green/increment geometry has now been resolved sharply. Prime Lattice supplies the correct positive finite measure; its canonical twofold primitive is also mathematically natural and retains exactly the finite Weil distribution. But the uniquely completed version is Suzuki's zeta screw function, whose global increment-kernel positivity is equivalent to RH.

The next useful search should therefore **not** invent another translation-invariant primitive, resistance kernel, or direct `D* G D` realization from the same data. It should look for an additional Mathia-native global object whose positivity is a theorem before the Weil functional is recovered — most plausibly a nontrivial quotient/compression, relative boundary/cohomology construction, or adelic/intersection structure that neither erases the Prime-Lattice axis data (WP-006) nor merely restates the completed Weil kernel (WP-007).
