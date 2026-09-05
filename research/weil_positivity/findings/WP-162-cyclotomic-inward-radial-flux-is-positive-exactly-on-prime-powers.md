# WP-162 — cyclotomic inward radial flux is positive exactly on prime powers, while positive bulk energies lose Mangoldt support

**Status:** `EXACT-DERIVED + DECISIVE-NARROWING + PRIME-CIRCLE-BRIDGE + NONLOCAL-RADIAL-FLUX + PRIME-POWER-POSITIVITY-CLASSIFICATION + SIGN-CANCELLATION + POSITIVE-SCALARIZATION-OBSTRUCTION + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-161` found a source-forced real radial deformation of a primitive cyclotomic shell whose boundary value is exactly `Lambda(n)`, while every finite local differential jet loses that support and becomes Euler/Jordan-totient data. It explicitly left genuinely nonlocal radial use of the whole family open.

The most direct such nonlocal readout can be classified exactly. For `n>1`, move the real point from the boundary at `1` inward to the origin and write

\[
G_n(s):=\log \Phi_n(e^{-s}),
\qquad s\ge 0.
\tag{1}
\]

This is the same primitive-root logarithmic chord product used in `WP-161`, now parametrized on the interior radial half-line. Define its inward flux

\[
\boxed{
\rho_n(s):=-G_n'(s)
=\frac{e^{-s}\Phi_n'(e^{-s})}{\Phi_n(e^{-s})}.
}
\tag{2}
\]

Then the complete boundary-to-origin flux has exactly the Mangoldt mass

\[
\boxed{
\int_0^\infty \rho_n(s)\,ds
=\Lambda(n).
}
\tag{3}
\]

More sharply,

\[
\boxed{
\rho_n(s)>0\ \text{for every }s>0
\quad\Longleftrightarrow\quad
n\text{ is a prime power}.
}
\tag{4}
\]

Thus the cyclotomic radial geometry does contain a canonical positivity discriminator for the prime-power shells. But this does **not** produce a positive Weil form. On every non-prime-power shell the exact zero in (3) is obtained by cancellation between positive and negative radial flux. Consequently any ordinary shellwise positive bulk scalarization such as total variation, `L^q` size, squared flux, or a pointwise strictly positive energy density becomes nonzero on every shell and destroys Mangoldt support.

The obstruction is therefore more precise than the local-jet failure of `WP-161`: the whole radial path does recover `Lambda`, but the support is carried by a **signed nonlocal conservation law**, not by a positive local density. A surviving finite--archimedean mechanism must retain this signed information until a genuinely global coupling is formed and prove positivity only at that assembled level.

## 1. The interior radial potential is canonical and finite at both ends

For `0<x<1`, `Phi_n(x)>0`, so (1) is real without a branch choice. It is exactly the primitive-shell chord product

\[
G_n(s)
=\sum_{(a,n)=1}
\log|e^{-s}-e^{2\pi i a/n}|.
\tag{5}
\]

The two endpoint values are classical:

\[
\Phi_n(0)=1
\tag{6}
\]

and, for `n>1`,

\[
\log\Phi_n(1)=\Lambda(n).
\tag{7}
\]

Hence

\[
\boxed{
G_n(0)=\Lambda(n),
\qquad
\lim_{s\to\infty}G_n(s)=0.
}
\tag{8}
\]

No regularization, zeta continuation, zero data, or chosen kernel enters this interpolation. It is already present in the embedded primitive-root geometry.

The Möbius product gives the exact divisor form

\[
G_n(s)
=
\sum_{d\mid n}
\mu(n/d)\log(1-e^{-ds}),
\tag{9}
\]

and therefore

\[
\boxed{
\rho_n(s)
=-\sum_{d\mid n}
\mu(n/d)\frac{d}{e^{ds}-1}.
}
\tag{10}
\]

Equivalently, expanding the primitive roots by their power sums gives the standard Ramanujan-sum representation

\[
G_n(s)
=-\sum_{m\ge1}
\frac{c_n(m)}m e^{-ms},
\tag{11}
\]

so for every `s>0`

\[
\boxed{
\rho_n(s)
=-\sum_{m\ge1}c_n(m)e^{-ms}.
}
\tag{12}
\]

The latter series is absolutely convergent for each positive `s`. Equations (10) and (12) show that the radial flux is not a newly inserted arithmetic weight: it is the logarithmic derivative of the exact cyclotomic chord product.

## 2. The total radial flux is exactly the Mangoldt selector

Since `rho_n=-G_n'`, equation (8) immediately yields

\[
\begin{aligned}
\int_0^\infty\rho_n(s)\,ds
&=G_n(0)-G_n(\infty)\\
&=\log\Phi_n(1)\\
&=\boxed{\Lambda(n)}.
\end{aligned}
\tag{13}
\]

Thus the zero-order boundary selector of `WP-161` has a genuinely nonlocal radial interpretation: it is the net charge transported from the cyclotomic boundary to the origin.

The flux is regular at the boundary. Cyclotomic reciprocity gives

\[
\Phi_n(x)=x^{\varphi(n)}\Phi_n(x^{-1}),
\tag{14}
\]

and differentiating at `x=1` gives

\[
\frac{\Phi_n'(1)}{\Phi_n(1)}
=\frac{\varphi(n)}2.
\tag{15}
\]

Therefore

\[
\boxed{
\rho_n(0^+)=\frac{\varphi(n)}2>0
\qquad(n>1).
}
\tag{16}
\]

At the other end, `Phi_n(x)=1+O(x)` as `x\to0`, so `rho_n(s)` decays exponentially. The signed measure

\[
d\nu_n(s):=\rho_n(s)\,ds
\tag{17}
\]

is consequently finite on the radial half-line.

## 3. Prime powers are exactly the shells with positive radial flux

Let `n=p^a`. The exact prime-power cyclotomic polynomial is

\[
\Phi_{p^a}(x)
=1+x^{p^{a-1}}+\cdots+x^{(p-1)p^{a-1}}.
\tag{18}
\]

Every nonconstant coefficient is positive, hence

\[
\Phi_{p^a}'(x)>0
\qquad(0<x<1),
\tag{19}
\]

and (2) gives

\[
\boxed{
\rho_{p^a}(s)>0
\qquad(s>0).
}
\tag{20}
\]

The same fact is visible directly from (10):

\[
\boxed{
\rho_{p^a}(s)
=
\frac{p^{a-1}}{e^{p^{a-1}s}-1}
-
\frac{p^a}{e^{p^as}-1}>0,
}
\tag{21}
\]

because `u/(e^{us}-1)` is strictly decreasing in `u>0` for fixed `s>0`. Its total mass is

\[
\nu_{p^a}([0,\infty))=\log p,
\tag{22}
\]

independent of `a`, exactly as required by `Lambda(p^a)`.

Now suppose `n` is not a prime power. Then (13) gives

\[
\int_0^\infty\rho_n(s)\,ds=0,
\tag{23}
\]

while (16) gives `rho_n(s)>0` on some interval immediately to the right of zero. Therefore `rho_n` must be negative somewhere. By continuity it changes sign. Hence

\[
\boxed{
\rho_n\ge0\text{ on }(0,\infty)
\quad\Longleftrightarrow\quad
n=p^a.
}
\tag{24}
\]

This is an exact Mathia-native positivity classification of the finite shells. The prime-power selection is not imposed by factoring `n` or multiplying by an external indicator; it is equivalent to monotonic decay of the intrinsic interior cyclotomic potential.

But this positivity is a **shell classifier**, not a global Weil quadratic form. It supplies neither the autocorrelation structure of Weil's test-function pairing nor the archimedean and polar terms.

## 4. The `n=6` control exposes the cancellation exactly

The smallest mixed-prime control is

\[
\Phi_6(x)=x^2-x+1.
\tag{25}
\]

With `x=e^{-s}`,

\[
\boxed{
\rho_6(s)
=
\frac{x(2x-1)}{x^2-x+1}.
}
\tag{26}
\]

Thus

\[
\rho_6(s)>0\quad(0<s<\log2),
\qquad
\rho_6(\log2)=0,
\qquad
\rho_6(s)<0\quad(s>\log2).
\tag{27}
\]

At the turning point,

\[
G_6(\log2)=\log\Phi_6(1/2)=\log\frac34.
\tag{28}
\]

Since `G_6(0)=G_6(\infty)=0`, the positive and negative fluxes are exactly

\[
\int_0^{\log2}\rho_6(s)\,ds
=\log\frac43,
\tag{29}
\]

and

\[
\int_{\log2}^{\infty}\rho_6(s)\,ds
=-\log\frac43.
\tag{30}
\]

Hence the Mangoldt zero is a genuine cancellation, while the total variation is strictly positive:

\[
\boxed{
\|\nu_6\|_{\rm TV}=2\log\frac43>0
\qquad\text{but}\qquad
\Lambda(6)=0.
}
\tag{31}
\]

This is a matched control on the exact source geometry, not a randomized or relabelled comparison.

## 5. Pointwise positive bulk energies necessarily acquire full shell support

The signed-flux formulation gives a broad no-go that is not visible from a finite Taylor jet. Let `w(s)>0` for almost every `s>0`, and let

\[
\Psi:\mathbb R\to[0,\infty)
\tag{32}
\]

satisfy `Psi(t)>0` for every `t\ne0`. Whenever

\[
E_n[w,\Psi]
:=
\int_0^\infty
w(s)\Psi(\rho_n(s))\,ds
\tag{33}
\]

is finite, (16) implies

\[
\boxed{
E_n[w,\Psi]>0
\qquad\text{for every }n>1.
}
\tag{34}
\]

Indeed every shell has a whole boundary interval on which `rho_n>0`. Thus ordinary pointwise positivity removes exactly the signed cancellation that made (13) sparse.

Important special cases include

\[
\int_0^\infty |\rho_n(s)|^q ds>0
\qquad(q\ge1),
\tag{35}
\]

and

\[
\int_0^\infty \rho_n(s)^2 ds>0.
\tag{36}
\]

For `q=1`, prime powers satisfy

\[
\int_0^\infty|\rho_{p^a}(s)|ds=\log p,
\tag{37}
\]

but every mixed-prime shell is a false positive. In measure language,

\[
\boxed{
\|\nu_n\|_{\rm TV}=\Lambda(n)
\quad\Longleftrightarrow\quad
n\text{ is a prime power};
}
\tag{38}
\]

for non-prime-powers the right-hand side of (13) is zero while the variation is strictly positive.

Therefore replacing the signed radial flux by a local dissipation, norm, square, absolute value, Fisher-like density, or other strictly positive pointwise size cannot be the missing finite Weil geometry. A hand-picked `Psi` with additional zeros tuned to particular shell profiles would simply move the arithmetic selector into the energy and fails the canonicality gate.

## 6. Even benign radial damping destroys the exact mixed-prime zero

One might keep the signed flux but smooth its long radial cancellation with a positive decaying anchor. For `epsilon>0`, define

\[
A_n(\epsilon)
:=
\int_0^\infty e^{-\epsilon s}\rho_n(s)\,ds.
\tag{39}
\]

Integration by parts gives

\[
\boxed{
A_n(\epsilon)
=\Lambda(n)
-\epsilon\int_0^\infty e^{-\epsilon s}G_n(s)\,ds.
}
\tag{40}
\]

For `n=6`,

\[
G_6(s)
=\log(1-e^{-s}+e^{-2s})<0
\qquad(s>0),
\tag{41}
\]

because `1-x+x^2=1-x(1-x)<1` on `0<x<1`. Hence

\[
\boxed{
A_6(\epsilon)>0
\qquad\text{for every }\epsilon>0,
}
\tag{42}
\]

while

\[
A_6(0)=\Lambda(6)=0.
\tag{43}
\]

So the exact selector is not robust under even the simplest source-independent positive exponential damping of the radial path. This does not prove that every nonlocal kernel fails. It shows that the direct boundary-to-origin cancellation must be preserved with exact global normalization; a generic smoothing of the radial charge already contaminates the first mixed-prime control.

## 7. Relation to the earlier positivity obstructions

This result is not a restatement of `WP-161`. There the complete **local differential germ** was classified: zero order is Mangoldt, while positive curvature and all higher centered even derivatives are Jordan-totient data. Here the whole radial half-line is used before scalarization. The exact Mangoldt value does survive that nonlocal passage, but only as the net mass of a signed flux.

It is also distinct from `WP-051`. That finding proves that positive Schatten sizes of a canonical Hardy remainder have full shell support. The present object is the radial cyclotomic log-chord potential itself, and the stronger source-specific statement (24) identifies exactly where positivity lives before the absolute-value operation: prime powers are precisely the shells whose entire inward flux is positive.

`WP-036` remains the closest same-geometry global comparison. Its full-root radial Mellin response is positive-real and contains the Riemann digamma scale, while the exact finite Weil coefficients appear only after a boundary finite-part subtraction that loses positivity. The present result shows an analogous but sharper separation for the primitive-shell radial path: the finite selector is already an exact nonlocal flux mass, yet mixed-prime zeros depend on sign cancellation that no shellwise positive density can inherit.

The result does **not** rule out a global operator that takes the signed family `rho_n` as input, couples different shells and the real place before scalarization, and then proves positivity of the assembled quadratic form. Nor does it rule out a boundary response whose sign theorem is genuinely nonlocal in both radial and arithmetic variables. Those are exactly the mechanisms still required by the canonical research mandate.

## 8. Prior-art and novelty audit

No theorem-level novelty is claimed for the cyclotomic identities. The product formula for `Phi_n`, the value `Phi_n(1)=p` on prime powers and `1` otherwise, reciprocity, and Ramanujan sums as primitive-root power sums are classical. The derivative literature already audited in `WP-161` includes D. H. Lehmer, *Some properties of the cyclotomic polynomial* (1966), and Andrés Herrera-Poyatos and Pieter Moree, *Coefficients and higher order derivatives of cyclotomic polynomials: old and new* (Expositiones Mathematicae 39, 2021). László Tóth, *Some remarks on Ramanujan sums and cyclotomic polynomials* (Bulletin Mathématique de la Société des Sciences Mathématiques de Roumanie 53, 2010, 277–292), is neighboring literature for the Ramanujan/cyclotomic interface.

A targeted search for cyclotomic monotonicity, logarithmic derivatives, and Ramanujan-sum formulations did not justify a historical novelty claim for (24). In fact its proof is deliberately elementary: prime-power cyclotomics have positive coefficients, while every non-prime-power has equal endpoint values `Phi_n(0)=Phi_n(1)=1`; together with the positive boundary derivative and the flux identity this forces a sign change.

The durable Mathia-specific contribution is the research consequence of applying those facts to the exact radial geometry left open by `WP-161`: **the first genuinely nonlocal reconstruction does preserve Mangoldt, but only as signed radial cancellation, and every ordinary pointwise positive bulk energy destroys the support.** This materially narrows the allowed category of a future finite--archimedean positivity mechanism.

## 9. Falsification surface and research consequence

The core claim has four independent exact checks:

1. verify `G_n(s)=log Phi_n(e^{-s})` and differentiate to obtain (2) and (10);
2. evaluate the two endpoints to obtain the total mass (13);
3. for `p^a`, use the positive-coefficient form (18) to prove strict positivity;
4. for a non-prime-power, combine zero total mass with the positive boundary limit (16) to force negative flux somewhere.

The `n=6` formula (26) is a complete symbolic control of the sign change and of the positive false mass created by total variation. Failure of any of these identities would invalidate the corresponding obstruction.

The current radial boundary is therefore

\[
\boxed{
\text{exact Mangoldt support}
=
\text{net signed cyclotomic radial flux},
}
\tag{44}
\]

not a positive local radial energy. Prime-power shells are special because their signed flux happens to be a positive measure; mixed shells require cancellation. A future Weil-positive construction cannot obtain the desired finite selector by making this flux positive shell by shell. It must preserve the signed finite information through a genuinely global finite--archimedean operation and obtain nonnegativity only from a separate theorem about the assembled form.