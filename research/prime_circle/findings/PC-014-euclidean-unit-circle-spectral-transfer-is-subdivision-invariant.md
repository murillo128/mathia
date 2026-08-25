# PC-014 — the canonical Euclidean/unit-circle spectral transfer is subdivision-invariant

**Status:** `DECISIVE-NEGATIVE` for a one-dimensional spectral mechanism obtained by using the exact Euclidean/unit-circle geometry to remove the projective gauge of PC-013.

## Motivation

PC-013 showed that the projective cross-ratios of the prime-vertex path do not canonically determine a Hill/Schrödinger spectrum: a unit-Wronskian lift retains a real gauge freedom. The most natural repair is to use the Euclidean structure already present in the original circle.

Take the distinguished prime vertices

\[
z_n=e^{i\theta_n},\qquad \theta_n=\frac{2\pi}{p_n},
\]

ordered toward the common vertex \(1\). Their exact angular spacings are

\[
h_n:=\theta_n-\theta_{n+1}
=2\pi\left(\frac1{p_n}-\frac1{p_{n+1}}\right)
=\frac{2\pi g_n}{p_np_{n+1}}.
\]

These \(h_n\) do contain the prime-gap fluctuations exactly. The question is whether the canonical Euclidean propagation along the circle converts them into nontrivial spectral data.

## Exact Helmholtz / Dirichlet-to-Neumann element

For the homogeneous one-dimensional equation

\[
-u''=k^2u
\]

on an arc of length \(h\), the exact endpoint Dirichlet-to-Neumann matrix is

\[
D_h(k)
=k
\begin{pmatrix}
\cot(kh)&-\csc(kh)\\
-\csc(kh)&\cot(kh)
\end{pmatrix}.
\]

Equivalently, the Cauchy data propagate through the exact transfer matrix

\[
T_h(k)=
\begin{pmatrix}
\cos(kh)&\sin(kh)/k\\
-k\sin(kh)&\cos(kh)
\end{pmatrix}.
\]

Assembling consecutive prime intervals gives the tridiagonal dynamic-stiffness equation

\[
-k\csc(kh_{n-1})u_{n-1}
+k\bigl(\cot(kh_{n-1})+\cot(kh_n)\bigr)u_n
-k\csc(kh_n)u_{n+1}=0.
\]

At \(k=1\), this is exactly the canonical \(\csc/\cot\) recurrence suggested by the unit-circle lift at the end of PC-013; the sampled coordinate functions \(e^{i\theta_n}\), hence also \(\cos\theta_n\) and \(\sin\theta_n\), satisfy it.

## Exact collapse of all prime-gap fluctuations

The transfer matrices form a one-parameter group:

\[
T_a(k)T_b(k)=T_{a+b}(k).
\]

Therefore, for any finite prime block,

\[
\boxed{
T_{h_m}(k)T_{h_{m+1}}(k)\cdots T_{h_N}(k)
=T_{h_m+\cdots+h_N}(k).
}
\]

But the angular increments telescope exactly:

\[
h_m+\cdots+h_N
=2\pi\left(\frac1{p_m}-\frac1{p_{N+1}}\right).
\]

Hence

\[
\boxed{
T_{h_m}(k)\cdots T_{h_N}(k)
=
T_{\,2\pi(1/p_m-1/p_{N+1})}(k),
}
\]

and in the infinite tail

\[
\boxed{
T_{h_m}(k)T_{h_{m+1}}(k)\cdots
=
T_{2\pi/p_m}(k)
}
\]

in the obvious finite-endpoint limiting sense.

Thus the exact transfer sees only the two endpoint angles. Every interior prime-gap fluctuation disappears.

The same statement holds in Dirichlet-to-Neumann language: if two exact elements of lengths \(a,b\) are glued and the common degree of freedom is eliminated by Schur complement, the resulting endpoint matrix is exactly \(D_{a+b}(k)\). Repeated elimination therefore removes every inserted prime vertex.

## Spectral consequence

Any boundary-value spectrum obtained from this exact one-dimensional Euclidean propagation is the spectrum of the ordinary homogeneous interval of the same total angular length. For example, on the tail from \(\theta_m\) to its accumulation point \(0\), Dirichlet conditions at both ends give

\[
k_j=\frac{j\pi}{2\pi/p_m}=\frac{jp_m}{2},\qquad j=1,2,\ldots,
\]

with the analogous universal formulas for the other standard endpoint conditions.

The locations of the intermediate prime vertices are spectrally invisible.

A fixed tridiagonal Jacobi matrix can of course be manufactured by freezing the \(k=1\) coefficients and then introducing an unrelated linear spectral parameter \(\lambda\). Such an operator may depend on the \(h_n\), but that new \(\lambda\)-dependence is no longer the exact Euclidean Helmholtz/Dirichlet-to-Neumann geometry. It is an additional modeling choice, precisely the kind of extra structure PC-013 warned against.

## Relation to chord metrics

If instead one joins the distinguished vertices by straight Euclidean chords and gives the resulting chain the standard metric-graph Laplacian, degree-two subdivision invariance gives the same qualitative obstruction: the chain is spectrally just one interval whose length is the total polyline length. That length may retain a single aggregate statistic through

\[
\sum_n 2\sin(h_n/2),
\]

but no individual gap sequence survives as a spectral potential without adding scatterers or nonstandard vertex conditions.

## Literature / novelty check

Nothing in the subdivision-invariance mechanism is new. Exact dynamic-stiffness / spectral-element methods derive precisely the frequency-dependent \(\cot/\csc\) matrix above from exact wave solutions and are explicitly independent of how a homogeneous one-dimensional member is subdivided. In quantum-graph language, inserting degree-two Kirchhoff vertices likewise leaves the spectrum unchanged.

Relevant references checked:

- exact dynamic stiffness for longitudinal rods: the standard matrix is proportional to \(k\begin{psmallmatrix}\cot(kh)&-\csc(kh)\\-\csc(kh)&\cot(kh)\end{psmallmatrix}\);
- spectral-element literature emphasizes exactness and independence from the number of elements;
- quantum-graph literature states subdivision invariance under insertion of degree-two standard/Kirchhoff vertices.

The useful result here is therefore negative and specific to the prime-circle program: **using the Euclidean/unit-circle metric to canonically fix the PC-013 lift does not create a prime-sensitive one-dimensional spectral transfer. Exact geometry makes the prime vertices mere subdivision points.**

## Research consequence

This closes the most natural one-dimensional Euclidean repair of PC-013:

\[
\boxed{
\text{prime angular gaps}
\to
\text{exact unit-circle }\csc/\cot\text{ transfer}
\to
\text{spectral data}
}
\]

is universal after endpoint reduction.

A surviving construction must therefore use structure that is not reducible to propagation along a homogeneous one-dimensional arc: genuinely two-dimensional off-circle fields, labeled cross-level interactions, nontrivial loops, or a canonically derived inhomogeneity/scatterer rather than one inserted by hand.
