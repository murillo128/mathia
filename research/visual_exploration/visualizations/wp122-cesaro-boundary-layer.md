# WP-122 Cesàro boundary layer

![Phase-averaged Gamma–Schoenberg Gram boundary layer](wp122-cesaro-boundary-layer.png)

## Question

`WP-122` proves that every nontrivial fixed jump-local positive matrix-valued Radon geometry sees divergent critical prime coupling. Its proof replaces pointwise Fourier decay by Cesàro averaging in the logarithmic location of prime shells. This visualization asks where that averaging mechanism becomes weak and whether the weakness isolates a mathematically precise boundary for a different, scale-sensitive local geometry.

## Construction

For the canonical two-channel increment used in `WP-122`,

\[
u_t(y)=
\begin{pmatrix}
\cos(ty)-1\\
\sin(ty)
\end{pmatrix},
\qquad y>0,
\]

define the phase-averaged Gram matrix over an averaging interval of length \(T\),

\[
M_T(y)=\frac1T\int_0^T u_t(y)u_t(y)^T\,dt.
\]

Writing \(z=Ty\), this matrix depends only on \(z\):

\[
M_T(y)=M(z),
\]

with

\[
M_{11}(z)
=
\frac32+\frac{\sin(2z)}{4z}-2\frac{\sin z}{z},
\]

\[
M_{22}(z)
=
\frac12-\frac{\sin(2z)}{4z},
\]

and

\[
M_{12}(z)
=
\frac{1-\cos(2z)}{4z}
-\frac{1-\cos z}{z}.
\]

The left panel plots \(\log_{10}\lambda_{\min}(M_T(y))\) over logarithmic \(T\) and \(y\). The white diagonals are the exact scaling contours \(Ty=0.1,1,10\). The right panel plots the two eigenvalues of the universal matrix \(M(z)\).

Taylor expansion at the boundary gives

\[
\lambda_{\max}(M(z))
=
\frac{z^2}{3}+O(z^4),
\qquad
\lambda_{\min}(M(z))
=
\frac{z^4}{320}+O(z^6).
\]

For fixed \(y>0\) and \(T\to\infty\), equivalently \(z\to\infty\), the oscillatory terms vanish and the two eigenvalues approach \(3/2\) and \(1/2\).

## Observation

The Cesàro mechanism has an exact shrinking boundary layer. Away from \(y=0\), increasing the logarithmic averaging length pushes the weakest matrix direction toward a uniform positive cost \(1/2\). The only region in which the averaged Gram matrix remains small is \(Ty=O(1)\), hence \(y=O(1/T)\).

The matrix problem is strongly anisotropic inside that layer. The strong direction costs quadratically, \(z^2/3\), while an optimally oriented weak direction costs only quartically, \(z^4/320\). Thus a hypothetical escape from the fixed-measure obstruction would have to exploit both concentration toward the jump endpoint and, potentially, the weak channel orientation; ordinary fixed mass at any positive jump scale cannot do so.

## Robustness

The diagonal boundary-layer geometry is not a rendering artifact: the collapse to \(z=Ty\) is an exact algebraic identity. The small-\(z\) slopes shown in the right panel are the Taylor asymptotics of the exact matrix, not fitted power laws. The large-\(z\) limits \(1/2\) and \(3/2\) are likewise the exact phase averages.

Changing plotting resolution or the sampled \(T,y\) ranges only changes how much of the same universal \(z\)-profile is visible. What remains unresolved is mathematical rather than graphical: `WP-122` assumes one fixed Radon geometry, whereas a scale-renormalized local form that concentrates toward \(y=0\) is outside that theorem's stated scope.

## Research consequence

This view motivates a proposed clue for `weil_positivity`: determine whether the \(y\asymp 1/T\) boundary layer can arise canonically as a renormalized derivative/Sobolev-type local geometry, or whether every such attempt either retains a positive critical-shell lower bound or becomes explicitly prime-frequency/scale dependent and therefore ceases to be a fixed geometric completion.

The visualization is diagnostic context only. It does not establish that such a renormalized geometry exists, is canonical, preserves positivity, or can evade the divergence theorem.
