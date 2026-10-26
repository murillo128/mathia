# VIS-468 — Four-defect Farey reassembly preserves a genuine source spectral sector

## Exact claim and evidence boundary

For the reflected four-defect `BCA` reassembly of
[FD-319](../../farey_discrepancy/findings/FD-319-four-vanishing-farey-index-defects-carry-macroscopic-energy.md),
the full discrepancy is exactly a half-period shift of the genuine
discrepancy plus a balanced step. In particular, **every sine coefficient
with absolute index divisible by four is unchanged from the genuine
Farey source**, whereas the antisymmetric projection of the usual
right-endpoint transport is zero on that entire sector.

This identifies a remaining source contribution after VIS-466's odd
stitch removal. It gives an exact bandwise lower bound on conditional
spectral separation, without estimating the genuine discrepancy.

**Evidence:** EXACT-DERIVED + CLASSICAL SHIFT-THEOREM SPECIALIZATION +
FINITE SOURCE/COMPARATOR DISTINCTION. The finite numerical panel below
illustrates the distinction; it does not establish a high-band limit,
asymptotic nonconvergence, or an RH implication.

## Half-period representation, including the fixed endpoints

Let \(p\ge7\) be an odd prime, \(N=\sum_{q\le p}\varphi(q)=2h\), and

\[
D_k=x_k-k/N,\qquad 0\le k\le N,
\]

where \(x_k\) are the genuine Farey points including zero and one.
Thus \(D_0=D_h=D_N=0\) and \(D_{N-k}=-D_k\). Put \(b=1/(2p)\).
Extend \(D_0,\ldots,D_{N-1}\) periodically with period \(N\), and define

\[
(CD)_k=D_{(k+h)\bmod N},\qquad
w_k=\begin{cases}
b,&1\le k<h,\\
0,&k=0,h,N,\\
-b,&h<k<N.
\end{cases}
\]

If \(y_k=x_k^\dagger-k/N\) is the reassembled discrepancy, then

\[
\boxed{y=CD+w.} \tag{1}
\]

Here \(C\) is a linear circular shift of the discrepancy array, not a
new permutation of Farey gaps. It preserves the antisymmetric subspace
and its Euclidean norm.

To verify (1) directly, put \(\lambda=(p-1)/(2p)\). The exchanged
blocks have coordinate formulas

\[
x_k^\dagger=\begin{cases}
x_{k+h}-\lambda,&2\le k\le h-1,\\
x_{k-h}+\lambda,&h+2\le k\le N-1,
\end{cases} \tag{2}
\]

and retain the other coordinates. Subtracting \(k/N\) from (2) gives
\(D_{k+h}+b\) and \(D_{k-h}-b\), respectively. At the two exceptional
fixed ranks,

\[
D_1=2b-1/N,\qquad D_{h+1}=b-1/N.
\]

Consequently \(y_1=D_{h+1}+b\) and \(y_{h+1}=D_1-b\), just as (1)
requires. The midpoint and outer endpoints give zero on both sides.
Thus (1) respects the exact finite endpoint assignment; it does not
replace that assignment by a continuum approximation.

## All-mode source dictionary

Use the orthonormal DST-I convention

\[
\widehat z_m=\sqrt{2/N}\sum_{k=1}^{N-1}z_k\sin(\pi mk/N),
\qquad 1\le m<N.
\]

All three vectors in (1) are rank-antisymmetric, so their odd-indexed
coefficients vanish. For even \(m=2r\), the half-period shift acts by

\[
\widehat{CD}_{2r}=(-1)^r\widehat D_{2r}.
\]

This follows by changing the circular summation index and using
\(\sin(2\pi r(k-h)/N)=(-1)^r\sin(2\pi rk/N)\).
The finite sine sum of the balanced step gives

\[
\widehat w_{2r}
=b\sqrt{2/N}\,[1-(-1)^r]\cot(\pi r/N).
\]

Together these prove the complete finite formula

\[
\boxed{
\widehat y_m=\begin{cases}
0,&m\text{ odd},\\
\widehat D_m,&m\equiv0\pmod4,\\
-\widehat D_m+2b\sqrt{2/N}\cot(\pi m/(2N)),&m\equiv2\pmod4.
\end{cases}} \tag{3}
\]

This is a signed-coefficient identity. It does not infer the missing
signs of \(D\) from a squared-magnitude spectrum.

Let \(v\) be FD-319's right-endpoint transport: it is \(b\) on
\(2\le k<h\), \(-b\) on \(h+2\le k<N\), and zero elsewhere.
Let \(Jz_k=z_{N-k}\) and \(a=(v-Jv)/2\). With
\(\theta_m=\pi m/N\), VIS-467's finite sum gives

\[
\widehat a_m=\begin{cases}
2b\sqrt{2/N}\cos\theta_m\cot(\theta_m/2),&m\equiv2\pmod4,\\
0,&\text{otherwise}.
\end{cases} \tag{4}
\]

Equivalently, \(w-a\) has value \(b/2\) at \(1,h-1\), value
\(-b/2\) at \(h+1,N-1\), and zero elsewhere. Since
\(\cot(\theta/2)-\cos\theta\cot(\theta/2)=\sin\theta\),
(3)–(4) make the remaining projected residual explicit:

\[
\widehat{y-a}_m=\begin{cases}
\widehat D_m,&m\equiv0\pmod4,\\
-\widehat D_m+2b\sqrt{2/N}\sin\theta_m,&m\equiv2\pmod4,\\
0,&m\text{ odd}.
\end{cases} \tag{5}
\]

Thus removing symmetric stitches does not remove genuine source
coefficients or the remaining antisymmetric endpoint correction.

## Bandwise obstruction and the precise remaining estimate

For a set \(B\subset\{1,\ldots,N-1\}\) on which both \(y\) and \(a\)
have positive energy, define

\[
\pi_m^B(z)=\frac{|\widehat z_m|^2}{\sum_{\ell\in B}|\widehat z_\ell|^2},
\qquad m\in B.
\]

Take the event \(H=B\cap4\mathbb N\). Equations (3)–(4) give

\[
\boxed{
\operatorname{TV}(\pi^B(y),\pi^B(a))
\ \ge\ \pi^B(y)(H)
=\frac{\sum_{m\in H}|\widehat D_m|^2}
       {\sum_{m\in B}|\widehat y_m|^2}.} \tag{6}
\]

This lower bound is valid for arbitrary bands, not only high bands.
For conditional convergence along a sequence, its right-hand side
must tend to zero. It need not equal the full TV distance: the
\(2\bmod4\) probabilities can also differ.

The sufficient projected-energy condition of
[VIS-450](VIS-450-projected-parity-transfer-sharpens-farey-gate.md) now has
the exact source form

\[
\frac{
 \sum_{m\in B\cap4\mathbb N}|\widehat D_m|^2+
 \sum_{\substack{m\in B\\m\equiv2\ (4)}}
 |\widehat D_m-2b\sqrt{2/N}\sin\theta_m|^2}
 {\sum_{\substack{m\in B\\m\equiv2\ (4)}}
 8b^2N^{-1}\cos^2\theta_m\cot^2(\theta_m/2)}
\longrightarrow0. \tag{7}
\]

It is sufficient, not necessary for convergence of energy laws.
For fixed \(B=\{m:\alpha\le m/N<1\}\), \(0<\alpha<1\),
VIS-467 evaluates the denominator as asymptotic to

\[
b^2\int_\alpha^1 2\cos^2(\pi x)\cot^2(\pi x/2)\,dx>0.
\]

Equation (7) therefore needs band-specific source cancellation at an
energy scale of order \(p^{-2}\). Neither the unconditional global
\(\|D\|^2=o(1)\) nor parity projection proves it. No estimate for the
numerator is asserted here.

## Falsification checks and finite visual panel

An integer Farey recurrence generated the grids. Independent exact
rational summation of the reordered positive gaps verified (1), endpoint
one, and reflection at every rank for all 22 primes \(7\le p\le97\):
20,508 coordinates in the period-\(N\) arrays. For the panel
\(p=7,11,19,43,101,211,503,1009\), direct translated coordinates (2)
and all-mode orthonormal DST-I transforms verified (3) with maximum
coefficient error below \(5.2\cdot10^{-15}\). The coordinate identity
error was below \(1.4\cdot10^{-16}\). Direct sine matrices at the first
four panel orders agreed with the DST within \(10^{-13}\).

All modes were used. For each panel order, bands
\(\alpha=1/4,1/2,3/4\) verified (6) and the projected upper bound.
Scaling by \(-3\) and rank reversal preserved normalized spectra within
\(10^{-13}\). As an algebraic control, 32 random antisymmetric arrays
at each \(N=10,18,42,120,584\), with the same two anchor values, obeyed
the identical dictionary (maximum error below \(1.8\cdot10^{-15}\);
NumPy PCG64 seed 468). Those arrays are not claimed to be increasing
grids: they show that the dictionary itself is shift/anchor geometry,
not an arithmetic signature.

The upper-half band gives the following descriptive values. \(R_B\)
is the exact ratio in (7), before taking any limit.

| \(p\) | \(N\) | Inherited mass, lower bound (6) | Actual TV | \(R_B\) |
|---:|---:|---:|---:|---:|
| 7 | 18 | 0.805387 | 0.805387 | 16.0672 |
| 11 | 42 | 0.625426 | 0.915705 | 21.5377 |
| 19 | 120 | 0.804499 | 0.867442 | 26.1724 |
| 43 | 584 | 0.682274 | 0.793202 | 27.8115 |
| 101 | 3144 | 0.763414 | 0.841909 | 33.7048 |
| 211 | 13624 | 0.711952 | 0.822922 | 39.5276 |
| 503 | 77200 | 0.676970 | 0.813245 | 45.7651 |
| 1009 | 309934 | 0.638069 | 0.794060 | 50.8084 |

This reused finite panel is exploratory, not independent confirmation
data or evidence of a positive limiting mass. The proof of (1)–(7)
does not depend on these observations. The
[paired visualization](../visualizations/farey-half-shift-source-sector.md)
shows the coordinate decomposition and both band normalizations.

## Prior art, mathematical delta, and boundaries

Circular shifts changing Fourier phases are classical; see Brian
McFee, [Digital Signals Theory, §6.2, The DFT shifting theorem](https://brianmcfee.net/dstbook-site/content/ch06-dft-properties/Shifting.html).
The [SciPy DST reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.dst.html)
specifies the type-I numerical convention. Targeted searches covered
Farey excursion/gap permutations, discrepancy sine spectra, half-period
shifts, and four-defect spectra. No general Fourier novelty is claimed.
The elementary finite sine sums and event lower bound for total
variation are also standard.

FD-319 already gives the reassembly, absolute residual norm and
fixed-mode limits. [VIS-466](VIS-466-reflected-farey-transport-parity-is-a-stitch-boundary-term.md)
isolates the odd stitch energy; [VIS-467](VIS-467-vanishing-stitch-parity-dominates-farey-high-bands.md)
shows why that energy matters after high-band conditioning. The
additional content here is the exact **source-to-reassembly all-mode
dictionary**: it replaces the opaque permuted residual by a half-shift,
identifies an unchanged source sector, and translates the remaining
projected transfer question into (6)–(7). It is a specialization to this
particular `BCA` control, not a theorem for arbitrary excursion orders.

The artificial labeled-edge grid is not a second genuine Farey
sequence. The projected transport \(a\) and the step \(w\) are analysis
vectors, not independently justified null ensembles. A spectral match
on \(4\mathbb N\) is copied source information, not independent
arithmetic validation. A mismatch with \(a\) does not demonstrate a
genuine-Farey anomaly. Any asymptotic high-band separation still needs
an estimate on the actual source coefficients; the finite table does
not supply it. This closes the finite representation question while
leaving that analytic question open.
