# PF-104 — continuous cotangent interpolation is not an intrinsic flute datum

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for any prime-flute spectral/dynamical mechanism that uses the off-prime differential or analytic structure of the continuous map `x -> cot(pi/x)` rather than a quantity descending to the sampled prime endpoints themselves.

## 1. Precise obstruction

Write

\[
U(x)=\cot\frac{\pi}{x},
\qquad
u_n=U(p_n).
\]

The zero-twist prime-flute is constructed from the increasing discrete endpoint sequence

\[
(\nu_n)_{n\ge 2}.
\]

Its side-pairing generators, orthogonal circles, distinguished cuffs, multi-gap separating geodesics, Fuchsian group, quotient surface, Laplacian and every intrinsic spectral/dynamical invariant depend on these sampled endpoints, not on values of `U(x)` at non-prime real `x`.

There are nevertheless infinitely many smooth/real-analytic tail interpolants that agree with `U` at every prime while having different differential data between the samples. An explicit one-parameter family is

\[
\boxed{
U_\varepsilon(x)
=
U(x)+\varepsilon e^{-x}\sin(\pi x).
}
\tag{1}
\]

For every prime `p`,

\[
\sin(\pi p)=0,
\]

hence

\[
\boxed{U_\varepsilon(p_n)=U(p_n)=\nu_n\quad\text{for every }n.}
\tag{2}
\]

Therefore `U` and `U_epsilon` produce **literally the same endpoint sequence and the same zero-twist hyperbolic flute**. In particular all intrinsic Laplace spectrum, essential spectrum, length data, scattering data (when defined), resonances, and intrinsic transfer/holonomy data are identical.

The continuous cotangent interpolation is thus extra structure sitting above the surface.

## 2. The control remains a legitimate increasing tail interpolation

For `x>=3`,

\[
U'(x)
=
\frac{\pi}{x^2}\csc^2\frac{\pi}{x}
>
\frac1\pi,
\tag{3}
\]

because `0<pi/x<=pi/3` and `sin y<y`.

For

\[
h(x)=e^{-x}\sin(\pi x),
\]

we have

\[
h'(x)=e^{-x}\bigl(\pi\cos(\pi x)-\sin(\pi x)\bigr),
\]

so

\[
|h'(x)|\le(\pi+1)e^{-x}.
\]

At `x>=3`,

\[
(\pi+1)e^{-3}<\frac1\pi.
\]

Consequently, for every `|epsilon|<=1`,

\[
\boxed{U_\varepsilon'(x)>0\qquad(x\ge3).}
\tag{4}
\]

Thus (1) is not a pathological reordering of the vertices: it is a real-analytic strictly increasing interpolation on the whole prime tail.

## 3. It agrees to every algebraic asymptotic order but changes differential data

For every integer `N>=1`,

\[
e^{-x}\sin(\pi x)=o(x^{-N})
\qquad(x\to+\infty).
\]

Therefore `U_epsilon` and `U` have the **same complete inverse-power asymptotic expansion along the positive real tail**. This is strictly stronger than the finite-jet matched controls of PF-101: no fixed algebraic order can distinguish (1) from the cotangent map.

Nevertheless their differential data already differ at the sampled primes. Since

\[
h'(p)=\pi(-1)^p e^{-p},
\]

for every odd prime `p`,

\[
\boxed{
U_\varepsilon'(p)-U'(p)
=-\varepsilon\pi e^{-p}\ne0
\qquad(\varepsilon\ne0).
}
\tag{5}
\]

Thus even the derivative of the chosen continuum endpoint map *at a prime label* is not determined by the hyperbolic surface, despite the vertex itself being fixed exactly.

The same applies to higher differential invariants. In particular the real Schwarzian profiles cannot agree identically on a tail interval. The standard Schwarzian rigidity theorem says that two locally univalent functions with equal Schwarzian differ by postcomposition with a Möbius transformation. If `S(U_epsilon)=S(U)` on a tail, then

\[
U_\varepsilon=M\circ U.
\]

But the two maps agree at infinitely many primes, hence at three distinct values of `U`; a Möbius transformation fixing those three values is the identity. That would force `U_epsilon=U`, contradicting (1) for `epsilon!=0`. Therefore

\[
\boxed{S(U_\varepsilon)\not\equiv S(U).}
\tag{6}
\]

The exact identity used in PF-082,

\[
S(U)(x)=\frac{2\pi^2}{x^4},
\]

is therefore a property of the chosen cotangent interpolation, not an additional intrinsic scalar field carried by the prime-flute.

## 4. What survives from PF-082 and PF-085

This does **not** invalidate the endpoint consequences derived using `U`.

PF-082 uses the Schwarzian as an efficient way to calculate the first finite-scale distortion of cross-ratios of the actual sampled endpoints. Once the four prime vertices are fixed, their exact cross-ratio and the corresponding separating geodesic are intrinsic. Equation (6) only says that the continuum Schwarzian used to derive an asymptotic coefficient is not itself extra spectral data of the surface.

Likewise PF-085's rectangle identity remains exact when the rectangle boundaries are the actual sampled endpoints: after integration, the mixed Grunsky/Schiffer kernel reduces to endpoint divided differences/cross-ratios. What is not intrinsic is the **pointwise continuum kernel between those boundaries**. Different interpolants can have different kernels while producing the same prime-endpoint rectangle values whenever the final expression descends completely to the endpoints.

This gives a clean criterion:

\[
\boxed{
\text{a continuum-map construction is admissible as prime-flute data only if it descends to the discrete endpoint/Fuchsian data.}
}
\tag{7}
\]

## 5. Why analyticity at infinity does not create a spectral escape

There is an important counterpoint. If one *imposes* a much stronger interpolation class — for example that the difference of two normalized interpolants is holomorphic at infinity — then the prime samples do force uniqueness by the identity theorem.

Indeed, if `F-U` is holomorphic at infinity and

\[
F(p_n)=U(p_n)
\]

for all large `n`, set

\[
g(w)=F(1/w)-U(1/w).
\]

Then `g` is holomorphic near `w=0` and has zeros

\[
w_n=1/p_n\to0.
\]

Hence `g` vanishes identically near zero. So within that imposed exterior-analytic germ class the interpolation is unique.

But this does not turn the germ into an intrinsic Laplace invariant. The zero-twist surface construction supplies the endpoint sequence; it does not supply the auxiliary requirement “extend meromorphically/holomorphically at infinity in the prime label”. That regularity comes from the upstream cotangent formula. A spectral mechanism that needs it must therefore explain why the Laplacian or Fuchsian group canonically selects that extra extension, rather than simply importing it.

The explicit control (1) makes the logical boundary sharp:

\[
\boxed{
\text{same exact surface + same complete algebraic tail jet}
\not\Rightarrow
\text{same off-prime analytic/differential interpolation}.}
\tag{8}
\]

## 6. Interior/exterior duality and exact orthogonal circles are untouched

The obstruction does not approximate or deform the actual prime circles. Equation (2) fixes every prime endpoint exactly. Hence every Euclidean circle orthogonal to the unit boundary that is used by the construction is the same, and so are both ambient interior/exterior realizations discussed in PF-017.

The gauge occurs only in the fictitious continuum of label values between prime vertices. The exact orthogonal-circle geometry at the vertices is preserved completely.

## 7. Prior art / novelty audit

The ingredients are standard:

- Arredondo--Morales--Ramirez Maluendas construct zero-twist tight flutes from a discrete positive sequence and explicit Fuchsian side pairings; no continuum interpolation of the sequence is part of the intrinsic surface data (`arXiv:2108.12487`).
- Equality of Schwarzians implying Möbius postcomposition is classical complex/projective analysis.
- The identity theorem at the accumulation point `w=0` is elementary complex analysis.
- Real-analytic interpolation freedom by adding a function vanishing on a prescribed discrete set is not new.

Directed searches for combinations of zero-twist/tight flutes, endpoint sequences, Schwarzian interpolation and Fuchsian spectral data did not locate this exact obstruction. No novelty is claimed for the analytic ingredients. The project-specific result is the impossibility principle obtained by composing them with the prime-flute construction:

\[
\boxed{
\text{off-prime analytic structure of }x\mapsto\cot(\pi/x)
\text{ cannot be an intrinsic spectral datum of }X_{\rm prime}.
}
\]

## 8. Consequence for the RH search

PF-101 ruled out extracting RH significance from any **fixed finite asymptotic jet** of the endpoint map. PF-104 closes the next natural escape if it is formulated through the continuous cotangent interpolation itself: even a beyond-all-algebraic-orders deformation can preserve every prime vertex and hence the entire hyperbolic surface while changing the continuum differential profile.

Therefore do not pursue a chain of the form

\[
\boxed{
\text{special differential/analytic identity of }\cot(\pi/x)
\to
\text{surface spectral object}
\to
\text{Riemann zeros}
}
\]

unless the proposed object is first shown to descend to the discrete sampled endpoint/Fuchsian data.

The surviving exact-geometry frontier is narrower but nonempty: a genuinely global mechanism may still use the **entire discrete sequence** `\{cot(pi/p_n)\}`, its infinite family of exact cross-ratios/holonomies, or an intrinsic operator of the resulting Fuchsian group. What PF-104 removes is the off-prime continuum interpolation as an independent source of spectral structure.
