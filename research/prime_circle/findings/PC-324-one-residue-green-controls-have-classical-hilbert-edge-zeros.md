# PC-324 — one-residue Green controls already have classical generalized-Hilbert edge zeros

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the relative-determinant/discrete-spectrum escape left open by PC-323.

PC-323 proves that every periodic cross-level Green operator

\[
X_{a,b}(k,l)=\frac{a(k)b(l)}{k+l}
\]

is a trace-class perturbation of one universal Hilbert channel, and leaves the discrete spectrum and the relative perturbation determinant as the first operator data that can still depend on the detailed periodic sources. The strongest immediate falsification test is therefore not another Prime-Circle source, but a matched periodic control with no arithmetic content.

A one-residue periodic control already produces genuine eigenvalues outside the universal Hilbert band, hence genuine zeros of the PC-323 relative perturbation determinant. They are exactly the classical edge eigenvalues of a generalized Hilbert matrix. Their location is determined only by the residue offset `alpha`, and finite-section determinant exponents in the same regime are likewise classical generalized-Hilbert edge asymptotics. Thus **the existence of off-band relative-determinant zeros is not by itself a Prime-Circle or RH discriminator**. Any surviving use of the PC-323 relative invariant must detect source-specific multi-residue interference beyond this one-channel control.

## 1. One-residue controls isolate a single generalized Hilbert matrix

Fix an integer `L>=5`, residues `1<=rho,sigma<=L`, and nonzero amplitudes `A,B`. Let

\[
a(k)=A\,\mathbf 1_{k\equiv\rho\pmod L},
\qquad
b(l)=B\,\mathbf 1_{l\equiv\sigma\pmod L}.
\tag{1}
\]

These are bounded periodic controls; no cyclotomic, prime, Ramanujan, or root-of-unity arithmetic has been inserted. Under the residue decomposition of PC-323, every block vanishes except `(rho,sigma)`, and that block is

\[
\boxed{
X_{\rho\sigma}
=\frac{AB}{L}H_\alpha,
\qquad
\alpha=\frac{\rho+\sigma}{L},
\qquad
(H_\alpha)_{mn}=\frac1{m+n+\alpha}.
}
\tag{2}
\]

The two RMS means are

\[
\mu_a=\frac{|A|^2}{L},
\qquad
\mu_b=\frac{|B|^2}{L},
\tag{3}
\]

so the universal PC-323 Hilbert-core scale is

\[
\boxed{c=\sqrt{\mu_a\mu_b}=\frac{|AB|}{L}.}
\tag{4}
\]

Consequently the comparison dilation `G_0` of PC-323 has essential spectrum

\[
\sigma(G_0)=[-\pi c,\pi c].
\tag{5}
\]

The only remaining question is what the offset `alpha` in the exact generalized-Hilbert block (2) does to the relative spectrum.

## 2. For `0<alpha<1/2`, the generalized Hilbert block has an exact edge eigenvalue

Assume

\[
0<\alpha<\frac12.
\tag{6}
\]

This regime is available intrinsically inside the residue decomposition; for example `rho=sigma=1` and any `L>=5` give `alpha=2/L<1/2`.

Define

\[
u_n=\frac{(\alpha)_n}{n!},
\qquad n\ge0.
\tag{7}
\]

Its generating function is `(1-z)^{-alpha}`. For every `j>=0`, Tonelli/Beta integration gives

\[
\begin{aligned}
(H_\alpha u)_j
&=\sum_{k\ge0}\frac{(\alpha)_k/k!}{j+k+\alpha}\\
&=\int_0^1 t^{j+\alpha-1}
\sum_{k\ge0}\frac{(\alpha)_k}{k!}t^k\,dt\\
&=\int_0^1 t^{j+\alpha-1}(1-t)^{-\alpha}\,dt\\
&=B(j+\alpha,1-\alpha)\\
&=\Gamma(\alpha)\Gamma(1-\alpha)u_j.
\end{aligned}
\tag{8}
\]

Euler reflection therefore yields the exact eigenvalue equation

\[
\boxed{
H_\alpha u
=\frac{\pi}{\sin(\pi\alpha)}u.
}
\tag{9}
\]

Moreover

\[
u_n\sim\frac{n^{\alpha-1}}{\Gamma(\alpha)},
\tag{10}
\]

so

\[
u\in\ell^2
\quad\Longleftrightarrow\quad
\alpha<\frac12.
\tag{11}
\]

Thus (9) is a genuine `ell^2` eigenvector precisely in the regime (6), and

\[
\frac{\pi}{\sin(\pi\alpha)}>\pi.
\tag{12}
\]

This already proves the needed control result directly. The complete spectral classification is classical generalized-Hilbert theory: Rosenblum's diagonalization gives the absolutely-continuous Hilbert channel, and the recent edge-eigenvalue formulation of Gebert and Küttler identifies the same `alpha<1/2` regime after their normalization.

## 3. The self-adjoint dilation has relative-determinant zeros outside the universal band

The singular spectrum of the one nonzero block (2) contains

\[
s_\alpha
=c\,\frac{\pi}{\sin(\pi\alpha)}.
\tag{13}
\]

Hence the self-adjoint dilation `G_{a,b}` has the discrete eigenvalue pair

\[
\boxed{
\lambda_\pm
=\pm\frac{\pi c}{\sin(\pi\alpha)}.
}
\tag{14}
\]

By (6),

\[
|\lambda_\pm|>\pi c,
\tag{15}
\]

so both lie strictly outside the comparison spectrum (5). PC-323 proves `G_{a,b}-G_0` is trace class and defines, for `z` outside `sigma(G_0)`,

\[
\Delta_{a,b}(z)
=\det\!\left(
I+(G_{a,b}-G_0)(G_0-z)^{-1}
\right).
\tag{16}
\]

Since

\[
G_{a,b}-z
=\left[I+(G_{a,b}-G_0)(G_0-z)^{-1}\right](G_0-z),
\tag{17}
\]

noninvertibility of `G_{a,b}-z` outside `sigma(G_0)` is equivalent to a zero of the relative determinant. Therefore

\[
\boxed{
\Delta_{a,b}(\lambda_+)
=\Delta_{a,b}(\lambda_-)=0
}
\tag{18}
\]

for these completely non-arithmetic one-residue controls.

The scale-free outlier location is

\[
\boxed{
\frac{|\lambda_\pm|}{\pi c}
=\frac1{\sin(\pi\alpha)},
}
\tag{19}
\]

which depends only on the elementary residue offset `alpha=(rho+sigma)/L`. No prime, cyclotomic, or zeta datum appears.

The control can even be matched to the canonical `(5,7)` continuous band of PC-323. Choose amplitudes with

\[
\frac{|A|^2}{L}=\frac45,
\qquad
\frac{|B|^2}{L}=\frac5{14}.
\tag{20}
\]

Then `c=sqrt(2/7)`, exactly as in PC-323, while (14) still supplies classical offset-controlled discrete outliers. Thus fixing the full essential/ac band does not make the mere appearance of relative zeros arithmetic.

## 4. Finite-section determinant growth is classical in the same edge regime

Martin Gebert and Heinrich Kuettler, *Szego-type determinant asymptotics for generalized Hilbert matrices with edge eigenvalues*, arXiv:2609.00255 [math-ph], submitted 31 August 2026, study

\[
H_N^\delta
=\left(
\frac{\sin((1+\delta)\pi)}{\pi(j+k+1+\delta)}
\right)_{j,k=0}^{N-1}.
\tag{21}
\]

Set

\[
\delta=\alpha-1,
\qquad
A_{\alpha,N}
:=\frac{\sin(\pi\alpha)}{\pi}H_{\alpha,N}.
\tag{22}
\]

Then `A_{alpha,N}=H_N^delta`. For `0<alpha<1/2`, one has `delta<-1/2`, exactly their edge-eigenvalue regime. Their Szego-type asymptotic gives

\[
\boxed{
\log\det\!\left(I_N-A_{\alpha,N}^2\right)
=-(1-\alpha)^2\log N+O(1).
}
\tag{23}
\]

Their paper emphasizes that the changed exponent in this regime is caused by the edge eigenvalues of the limiting generalized Hilbert operator. Thus both the infinite-volume outlier (14) and a natural finite-section determinant signature are already part of generalized-Hilbert spectral theory controlled by `alpha`.

The abstract Hilbert result is therefore prior art, not a new Prime-Circle theorem. The line-local mathematical delta is the exact embedding (1)--(2): the relative-determinant frontier left by PC-323 contains these classical edge zeros even for matched periodic controls with no arithmetic content.

## 5. Consequence for the PC-323 frontier

This rules out the implication

\[
\text{PC-323 relative determinant has off-band zeros}
\Longrightarrow
\text{Prime-Circle arithmetic spectral signal}
\Longrightarrow
\text{RH mechanism}.
\tag{24}
\]

The first arrow already fails. One-residue controls produce the same qualitative phenomenon, with exact zero locations prescribed by the generalized-Hilbert offset. Likewise a power-law finite-section determinant anomaly near the band edge is not sufficient evidence: (23) is already offset-driven classical behavior.

This does **not** show that the canonical multi-residue Prime-Circle relative determinant is trivial, nor that its discrete spectrum equals a one-residue control, nor that the full scattering matrix or spectral-shift function contains no arithmetic information. It sharpens the admissibility test. A surviving mechanism must identify a feature that depends on **interference among several residue blocks/source phases**, survives comparison with matched periodic controls, and then prove a non-arbitrary bridge from that feature to zeta zeros, the functional equation, or the critical line.

The result is complementary to PC-107. PC-107 rules out a fixed trace-class Hardy Fredholm determinant as a direct Riemann-zero divisor by zero-density. Here the operator itself is noncompact and only the **relative** defect is trace class; the obstruction is instead that its most immediate discrete zeros occur already in non-arithmetic generalized-Hilbert controls.

## 6. Audit and failure modes

The claim is exact at the level used here and is falsified if any of the following fails: the one-residue masks must reduce PC-323's residue matrix to the single block (2); the Beta integral must give (9); `(alpha)_n/n!` must lie in `ell^2` exactly for `alpha<1/2`; the comparison band must have edge `pi c`; and the perturbation-determinant factorization (17) must identify off-band eigenvalues with zeros of (16). These are independent checks and require no numerical fitting.

The literature-dependent finite-section statement (23) uses Gebert--Kuettler's normalization exactly: `delta=alpha-1`, so the normalized matrix in their theorem is `A_alpha`, and `delta<-1/2` is equivalent to `alpha<1/2`. Their theorem is not used to prove the explicit eigenvector (9); it supplies the prior-art classification and determinant asymptotic around the same edge regime.

No claim is made about zeros embedded inside the essential band, resonances on a continuation sheet, uniqueness of the canonical `(5,7)` discrete spectrum, or a complete classification of multi-residue relative scattering. Those remain distinct questions.