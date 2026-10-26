# VIS-466 — Reflected Farey transport parity is an exact stitch boundary term

## Exact claim and evidence

For a reflection-preserving complete excursion permutation in
[FD-320](../../farey_discrepancy/findings/FD-320-all-prime-farey-excursion-permutations-have-an-exact-transport-spectrum.md), write
\(y=D_p^\sigma=e+v\), with \(e=P_\sigma D_p\),
\(E=\|e\|_2^2=\|D_p\|_2^2\), and \(T=\|v\|_2^2\).
The **right-endpoint convention** in that decomposition is essential.
Reflection makes \(y\) antisymmetric in rank; it does **not** generally make
\(v\) or \(e\) antisymmetric separately.

Let \(p\ge7\) be an odd prime, \(N=\sum_{q\le p}\varphi(q)\),
\(n=p-2\), and let \(\ell_j\) be the positive gap count of the excursion
from \(j/p\) to \((j+1)/p\). Assume
\[
\sigma(n+1-t)=p-1-\sigma(t),\qquad 1\le t\le n.
\]
Define
\[
w_j=\ell_j/N-1/p,\quad U_j=\sum_{i<j}w_i,\quad
c_t=U_{\sigma(t)}-\sum_{u<t}w_{\sigma(u)},\qquad
r_t=1+\sum_{u\le t}\ell_{\sigma(u)}.
\]
Here \(r_0=1,r_n=N-1\), \(c_0=c_{n+1}=0\), and the transport is
\(v_1=0\), \(v_k=c_t\) for \(r_{t-1}<k\le r_t\).
For the rank reversal \((Jz)_k=z_{N-k}\), put
\[
s=(v+Jv)/2,\qquad a=(v-Jv)/2.
\]
Then the symmetric part consists **only of stitch values**:
\[
\boxed{\quad s_{r_t}=\frac{c_t-c_{t+1}}2\ (0\le t\le n),
\qquad s_k=0\quad(k\notin\{r_0,\ldots,r_n\}).\quad} \tag{1}
\]
In the orthonormal Dirichlet sine basis
\(\widehat z_m=\sqrt{2/N}\sum_{k=1}^{N-1}z_k\sin(\pi mk/N)\),
odd absolute mode indices are the symmetric sector. Consequently
\[
\boxed{\quad L:=\sum_{m\ \mathrm{odd}}|\widehat v_m|^2
 =\|s\|_2^2=\frac14\sum_{t=0}^{n}(c_{t+1}-c_t)^2.\quad} \tag{2}
\]
Moreover,
\[
\boxed{\quad (e+Je)/2=-s,\qquad
L\le E,\qquad \|a\|_2^2=T-L,\qquad \|y-a\|_2^2=E-L.\quad} \tag{3}
\]
For every nonzero transport, \(0<L<T\). Thus no nonzero reflected
right-endpoint transport has an exactly even-only sine spectrum, although
its full reconstructed discrepancy does.

For nonzero vectors write \(\pi_m(z)=|\widehat z_m|^2/\|z\|_2^2\).
If \(T>0\) and \(y\ne0\), the exact parity mixture and projected transfer are
\[
\boxed{\quad
\operatorname{TV}(\pi(v),\pi(a))=L/T,
\qquad
\operatorname{TV}(\pi(y),\pi(a))
 \le\min\{1,\sqrt{(E-L)/(T-L)}\}.
\quad} \tag{4}
\]
All distributions in (4) use the **same full set of absolute mode indices**;
\(\pi(a)\) and \(\pi(y)\) have zero odd mass. In particular
\(\operatorname{TV}(\pi(y),\pi(v))\ge L/T\).

**Evidence:** EXACT-DERIVED + CLASSICAL REFLECTION/ORTHOGONAL-PROJECTION
SPECIALIZATION + FINITE REPRESENTATION CORRECTION. These are finite
identities for artificial labeled-edge grids. No PNT, asymptotic
approximation, new general Fourier theorem, or arithmetic anomaly is used.

## Derivation from the exact endpoint convention

Farey reflection gives \(\ell_{p-1-j}=\ell_j\). Let
\(S=\sum_{j=1}^n w_j\). Then
\[
U_{p-1-j}=S-U_j-w_j.
\]
For the reversed position \(n+1-t\), the reordered prefix mismatch is
\(S-\sum_{u<t}w_{\sigma(u)}-w_{\sigma(t)}\). Subtraction proves
\[
c_{n+1-t}=-c_t,\qquad r_{n-t}=N-r_t. \tag{5}
\]
At a rank strictly inside a block, reversal lands strictly inside its
paired block. The two transport values cancel. At the stitch \(r_t\),
however, the right-endpoint convention assigns the value of the **preceding**
block, \(c_t\), while the reflected stitch has value
\(c_{n-t}=-c_{t+1}\). This also covers the outer stitches by the sentinel
values \(c_0=c_{n+1}=0\). It proves (1).

The positive lengths ensure all \(r_t\) are distinct. Squaring (1) and
summing therefore gives the last equality in (2). The sine identity
\[
\sin(\pi m(N-k)/N)=(-1)^{m+1}\sin(\pi mk/N)
\]
and orthonormality prove the spectral equality. This is reflection about
the rank midpoint, separate from the odd extension used to define DST-I.

The reassembled positive gap word is palindromic, so
\(y_{N-k}=-y_k\). Projecting \(y=e+v\) onto the symmetric sector gives
\(Q_+e=-s\), where \(Q_\pm=(I\pm J)/2\). Orthogonal Pythagoras gives
\(\|Q_-e\|^2=E-L\), \(\|Q_-v\|^2=T-L\), and
\(y-a=Q_-e\), proving (3).

If \(L=0\), every consecutive difference in (2) is zero; the zero sentinel
then forces every \(c_t=0\), hence \(v=0\). If \(T-L=0\), then \(a=0\).
At the stitches
\(a_{r_t}=(c_t+c_{t+1})/2\). Starting with \(c_0=0\) forces
\(c_1=0\), then all other \(c_t=0\). Thus \(0<L<T\) whenever \(T>0\).

The two parts \(a,s\) occupy disjoint sine parities. Therefore
\[
\pi(v)=(1-L/T)\pi(a)+(L/T)\pi(s), \tag{6}
\]
which proves the first assertion in (4). The second follows by applying
the normalized-vector angle inequality of
[VIS-447](VIS-447-uniform-normalized-farey-transport-spectrum.md)/[VIS-450](VIS-450-projected-parity-transfer-sharpens-farey-gate.md) to
\(y=a+Q_-e\). This is the earlier projected-sector principle with **both**
sector energies now evaluated exactly from the stitch correction.
When \(T\ge E\), \((E-L)/(T-L)\le E/T\); when \(T<E\), both the old
and new square-root bounds cap at one. Projection therefore never worsens
the capped sufficient bound in this reflected class. It does not remove
any even-mode discrepancy error or any null-specific denominator.

## A fully explicit four-defect witness

Use [FD-319](../../farey_discrepancy/findings/FD-319-four-vanishing-farey-index-defects-carry-macroscopic-energy.md)'s reflected order \(BCA\), where \(C\) is the central two-gap
excursion, \(A\) contains the original left excursions and \(B\) their
reflected partners. Put \(b=1/(2p)\). The right-endpoint transport is
\[
v_k=\begin{cases}
 b,&2\le k\le N/2-1,\\
 -b,&N/2+2\le k\le N-1,\\
 0,&\text{otherwise}.
\end{cases}
\]
Its four nonzero symmetric values are
\[
s_1=s_{N-1}=-\frac1{4p},\qquad
s_{N/2-1}=s_{N/2+1}=\frac1{4p}.
\]
Thus
\[
T=\frac{N-4}{4p^2},\qquad L=\frac1{4p^2},\qquad
T-L=\frac{N-5}{4p^2},\qquad \frac LT=\frac1{N-4}. \tag{7}
\]
For odd \(m\), direct summation even gives
\[
\widehat v_m=\frac1{2p}\sqrt{\frac2N}
 \left[\sin(\pi m/2)\cos(\pi m/N)-\sin(\pi m/N)\right]. \tag{8}
\]
At \(p=7\), the genuine excursion lengths are \((3,4,2,4,3)\), and
\(\sigma=(4,5,3,1,2)\). Here \(N=18\), \(E=197/7560\),
\(T=1/14\), \(L=1/196\), and
\[
\widehat v_1=\frac{\cos(\pi/18)-\sin(\pi/18)}{42}>0.
\]
The full reconstructed \(\widehat y_1\) is exactly zero. The missing
cancellation is supplied by \(\widehat e_1=-\widehat v_1\), not by
numerical accuracy, continuum symmetry, or a different sine normalization.

## Source distinction, novelty, and scope

FD-320 §3 says under reflection that every odd sine coefficient in its
all-mode identity vanishes. If read as including its right-endpoint
transport and residual, that statement conflicts with (7)–(8). Exact
vanishing applies to the **full reconstructed discrepancy**. Its vector
identity and all-mode error equality remain valid. FD-319's positive
limiting energy and fixed-mode limits likewise survive: the boundary
energy in (7) tends to zero. This finding records the finite distinction;
it does not rewrite either source finding or withdraw their principal
transport/asymptotic claims.

[VIS-461](VIS-461-one-quantum-farey-pair-retains-normalized-spectral-separation.md) already explicitly distinguishes exact full-discrepancy reflection
from transport odd mass tending to zero for its particular six-stitch
pair. VIS-450 already proves the general projected-sector transfer
inequality. The additional content here is the **all-reflected-permutation
stitch formula**, its exact cancellation and the computable energies
\(E-L,T-L\), including the strict \(L>0\) obstruction for nonzero
right-endpoint transport. It is not a new claim that symmetry and sampling
conventions affect Fourier parity.

Classical sine parity, orthogonal projection and Parseval underlie the
proof. The [FFTW documentation on real even/odd transforms](https://www.fftw.org/fftw3_doc/Real-even_002fodd-DFTs-_0028cosine_002fsine-transforms_0029.html)
distinguishes sample-centered from half-sample symmetry and the associated
transform conventions. The [SciPy DST documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.dst.html)
specifies the type-I normalization used in the checks. Targeted literature
searches covered discrete-sine reflection/endpoint conventions and Farey
excursion-permutation spectra. No external theorem is needed for (1)–(8),
and no broad novelty in Fourier analysis is claimed. FD-320 provides the
source construction; the formulas above are derived from it independently.

These are positive-gap reassemblies with copied denominator labels, not
alternative genuine Farey sequences. Projection \(v\mapsto a\) is an
analysis of the decomposition, not a new admissible reassembled grid.
The genuine Farey case has \(T=0\), so its normalized transport law is
undefined. Small \(L/T\) alone does not imply small \(E/T\), low-band
concentration, a matched-null anomaly, or an improved Franel–Landau bound.

## Falsification checks and visual consequence

An integer Farey recurrence generated the original rational grids. For
**all 8 reflected permutations at \(p=7\)** and **all 384 at \(p=11\)**,
independent exact `Fraction` summation of the reordered denominator-edge
gaps verified positivity, endpoint one, the complete directed-edge
inventory, reflection, \(y=e+v\), every coordinate of (1), and the coordinate-space energy
identities in (2)–(3). This includes identity/zero-transport degeneracies.
The enumeration chooses one label from each mirror pair for the left
half, orders those labels arbitrarily, inserts the central label, and
reflects the result. It exhausts \(2^h h!\) choices with \(h=(p-3)/2\).

A further 128 independently sampled reflected permutations at each
\(p=13,29,101,211\), using NumPy PCG64 seed 466 in that order (draw a
permutation of the \(h\) pair labels, then \(h\) binary orientation bits),
checked the direct translated-coordinate reconstruction, complete DST-I
odd energy, mixture distance and projected bound. All 512 passed. Across
these checks and the eight four-defect examples below, the maximum vector
identity error was below \(2\cdot10^{-16}\), the odd-energy error below
\(3\cdot10^{-18}\), and the error in
\(\operatorname{TV}(\pi(v),\pi(a))=L/T\) below \(4\cdot10^{-16}\).
No projected-bound violation occurred. Exact arithmetic proves the small
cases; floating-point checks are falsification controls, not the proof
of the general result.

The four-defect family was independently evaluated at
\(p=7,11,19,43,101,211,503,1009\), including every sine mode, and agreed
with \(L/T=1/(N_p-4)\). At \(p=7\), direct sine-matrix multiplication
and DST-I agreed within \(2\cdot10^{-15}\); scaling \(v\) by \(-3\) or
reversing its ranks left its normalized spectrum unchanged within the
same tolerance. Thus the leakage is a boundary-assignment effect, not an
amplitude, orientation, high-mode truncation, or colormap artifact.

The paired [stitch-parity visualization](../visualizations/farey-stitch-parity.md)
shows the exact small witness, its boundary cancellation and the finite
family decay. **Research consequence:** a reflection-matched spectral
control should use the full discrepancy or explicitly projected transport
with energies \(T-L,E-L\). Assigning exact reflection parity to the raw
right-endpoint vector creates a spurious forbidden-sector signal; merely
silently dropping those modes removes a fraction \(L/T\) of its energy.
