# VIS-460 — The five-defect rank collision has inverse-prime spectral separation

## Claim and evidence status

Consider exactly the artificial whole-excursion Farey pair
\(\sigma=BDACR\), \(\tau=DBACR\) of
[FD-329](../../farey_discrepancy/findings/FD-329-four-defect-ranks-rigid-five-admit-transport-ambiguity.md),
at the same prime \(p\ge7\). Use its **transport vectors**, not the full
reconstructed discrepancy vectors. Put \(N=\sum_{q\le p}\varphi(q)\) and
\[
\widehat v_r=\sqrt{2/N}\sum_{k=1}^{N-1}v_k\sin(\pi rk/N),\qquad
\pi^\sigma_p(r)=|\widehat v^\sigma_r|^2/T_\sigma,
\quad T_\sigma=\|v^\sigma\|_2^2,
\quad 1\le r<N,
\]
and likewise for \(\tau\). Let
\[
c=3/\pi^2,\qquad Y=\pi^2/9-1>0,\qquad Z=6-5\pi^2/9,
\quad T_0=cY^2,\qquad D=-\tfrac23Y(Y+Z)<0.
\tag{1}
\]
Then, along primes tending to infinity,
\[
\boxed{T_\sigma,T_\tau\longrightarrow T_0>0,\qquad
\operatorname{TV}(\pi^\sigma_p,\pi^\tau_p)=\Theta(p^{-1}).}
\tag{2}
\]
More precisely, for every fixed positive mode \(r\),
\[
\boxed{p\bigl(\pi^\sigma_p(r)-\pi^\tau_p(r)\bigr)
\longrightarrow -\frac{D}{T_0}\,q_r,\qquad
q_r=\begin{cases}8/(\pi^2r^2),&r\text{ odd},\\0,&r\text{ even}.
\end{cases}}
\tag{3}
\]
Both spectra, extended by zero to all positive integers, converge in total
variation to \(q\). Thus the pair is eventually distinguishable by mode one,
but **no sequence of mode windows, residue pushforwards, or sign-reflection
foldings can retain a positive limiting absolute probability separation**.
The upper bound is uniform over such windows, including windows moving with
\(p\); it does not exclude a discriminator rescaled by \(p\).

Their shared five defect ranks also do not give a joint rank-and-value
collision: the first defective index value already distinguishes these two
words for every \(p\ge7\). No injectivity claim for all five-defect words follows.

**Evidence:** EXACT-DERIVED + TOTIENT-ASYMPTOTIC + CLASSICAL BV-FOURIER
SPECIALIZATION + NEGATIVE/CONTROL-DESIGN. The source-specific result is the
sharp spectral separation rate and its normalization mechanism for this
particular equal-rank pair. It is not a new general Fourier theorem or an
assertion about genuine Farey order or RH.

## Exact vectors and the boundary difference

Write
\[
a=(p+1)/2,\quad b=\lfloor p/3\rfloor+1,\quad h=N-2-2a-2b,
\qquad x=a/N-1/p,\quad y=b/N-1/p,\quad z=h/N-(p-6)/p.
\tag{4}
\]
FD-329's excursion counts, together with the endpoint convention in
[FD-320](../../farey_discrepancy/findings/FD-320-all-prime-farey-excursion-permutations-have-an-exact-transport-spectrum.md),
give the following complete vectors on ranks \(1,\ldots,N-1\):

| Consecutive block length | 1 | \(b\) | \(b\) | \(a\) | \(h\) | \(a\) |
| --- | --- | --- | --- | --- | --- | --- |
| \(v^\sigma\) | 0 | \(x\) | \(x+z\) | \(-2y\) | \(-y\) | 0 |
| \(v^\tau\) | 0 | \(x+y+z\) | \(x-y\) | \(-2y\) | \(-y\) | 0 |

In particular, with \(d=y+z\),
\[
\delta v_k:=v^\sigma_k-v^\tau_k
=\begin{cases}-d,&2\le k\le b+1,\\
d,&b+2\le k\le2b+1,\\0,&\text{otherwise}.
\end{cases}
\tag{5}
\]
This is a boundary-localized balanced difference, supported on \(O(p)\)
of the \(N\asymp p^2\) ranks. The classical totient asymptotic gives
\[
px\to\pi^2/6-1,\quad py\to Y,\quad pz\to Z,\quad h/N\to1.
\]
The bulk block therefore contributes \(hy^2\to cY^2\), and the other
nonzero blocks contribute \(O(p^{-1})\), proving the energy limit in (2).
The exact difference, already proved in FD-329, is
\[
T_\sigma-T_\tau=-2by(y+z),\qquad p(T_\sigma-T_\tau)\to D.
\tag{6}
\]
Also \(\|\delta v\|_2^2=2bd^2\sim\frac23(Y+Z)^2/p\). An argument
using only vector norm continuity would give the weaker spectral upper
bound \(O(p^{-1/2})\). The sine basis's zero at this boundary is essential
to the sharper estimate below.

## Uniform spectral upper bound and sharp fixed-mode witness

Extend each vector by \(v_0=v_N=0\). Its number of jumps is bounded and
every jump is \(O(p^{-1})\), so its endpoint-inclusive variation is
\(V(v)=O(p^{-1})\). Discrete summation by parts, as explicitly derived in
[VIS-448](VIS-448-variation-tariff-for-farey-transport-spectrum.md), gives
\[
|\widehat v_r|\le\sqrt{2/N}\frac{V(v)}{2\sin(\pi r/(2N))}
\le\frac{\sqrt{N/2}\,V(v)}r\le C/r,
\qquad 1\le r<N.
\tag{7}
\]
All constants here and below are uniform for sufficiently large primes.
On the support (5), \(k\le2b+1=O(p)\); hence, directly from
\(|\sin t|\le |t|\),
\[
|\widehat{\delta v}_r|
\le \sqrt{2/N}|d|\sum_{k=2}^{2b+1}\frac{\pi rk}{N}
\le Cr/p^2.
\tag{8}
\]
For \(r\le p\), equations (7)–(8) bound
\[
\bigl||\widehat v^\sigma_r|^2-|\widehat v^\tau_r|^2\bigr|
\le |\widehat{\delta v}_r|
(|\widehat v^\sigma_r|+|\widehat v^\tau_r|)\le C/p^2.
\]
For \(r>p\), (7) bounds the same quantity by \(C/r^2\).
Summing both ranges yields
\[
\sum_{r=1}^{N-1}\bigl||\widehat v^\sigma_r|^2
-|\widehat v^\tau_r|^2\bigr|=O(p^{-1}).
\tag{9}
\]
Since \(T_\sigma,T_\tau\to T_0>0\), normalization changes (9) by at most
another \(|T_\sigma-T_\tau|/T_\sigma=O(p^{-1})\). This proves the
total-variation upper bound. A mode window or any common probabilistic
pushforward contracts total variation, giving the asserted uniform consequence.

For fixed \(r\), the two transport vectors equal the constant vector
\(-y\) except on \(O(p)\) ranks with \(O(p^{-1})\) deviations.
Their normalized sine coefficients consequently satisfy
\[
\widehat v^\sigma_r,\widehat v^\tau_r
\longrightarrow -\sqrt{2c}\,Y\int_0^1\sin(\pi rt)\,dt
=-\sqrt{2c}\,Y\frac{1-(-1)^r}{\pi r}.
\tag{10}
\]
The coefficient perturbation relative to the constant vector is at most
\(O(p^{-1})\); the Riemann sum in (10) then gives the limit directly.
Equation (7), the positive energy floor, and summability of \(r^{-2}\)
also imply total-variation convergence to the normalized law \(q\).

For a fixed mode put \(A_\sigma=|\widehat v^\sigma_r|^2\) and similarly
\(A_\tau\). Equation (8) strengthens their difference to
\(A_\sigma-A_\tau=O_r(p^{-2})\). Therefore
\[
p\left(\frac{A_\sigma}{T_\sigma}-\frac{A_\tau}{T_\tau}\right)
=\frac{p(A_\sigma-A_\tau)}{T_\sigma}
-\frac{A_\tau\,p(T_\sigma-T_\tau)}{T_\sigma T_\tau}
\longrightarrow -q_rD/T_0,
\]
proving (3). At mode one the limit is approximately \(11.2880598>0\).
Since total variation dominates the difference on a singleton, this proves
the matching \(\Omega(p^{-1})\) lower bound in (2). The fixed-mode witness
comes at leading order from **energy normalization**, while the unnormalized
fixed-mode power difference is only \(O_r(p^{-2})\).

## What the missing defect values recover

At the first defective junction the preceding denominator is 1. The first
denominator after \(j/p\) is \(p-[j^{-1}]_p\), with inverses in
\(\{1,\ldots,p-1\}\); this follows from the Farey neighbor determinant.
For \(\sigma\) the first excursion is \(E_2\), whereas for \(\tau\) it is
\(E_{p-3}\). Thus their first index values are exactly
\[
\nu^\sigma_1=\frac{p+1}{2p},\qquad
\nu^\tau_1=\frac{1+[3^{-1}]_p}{p}.
\tag{11}
\]
Equality would force \([3^{-1}]_p=(p-1)/2\), and reducing modulo \(p\)
would give \(-3/2=1\), hence \(p\mid5\). This cannot occur for \(p\ge7\).
So exact values separate this pair immediately; their equality of ranks
alone must not be described as equality of the full defect signature.

## Independent checks and visual consequence

Independent exact rational Farey-grid and denominator-edge reconstruction
at \(p=7,11\) verified the table, every coordinate of
\(D^\sigma-P_\sigma D=v^\sigma\), the common five ranks, and the distinct
index values. The energies were respectively
\((95/2646,46/1323)\) and \((592/17787,608/17787)\).
A direct sine-matrix calculation agreed with the orthonormal type-I DST
to less than \(2\cdot10^{-14}\) per coefficient on those cases.

The full finite spectra (all \(N-1\) modes, with no tail truncation) were
checked at \(p=7,11,31,61,101,211,401,601,1009,1601,2503\). Their masses
agreed with one to within \(3\cdot10^{-13}\); residue reduction modulo 7
and subsequent sign folding contracted total variation in every case.
At \(p=101,1009,2503\), the full spectral distances were approximately
\(0.1804130,0.0500487,0.0230680\). The corresponding values of
\(p(\pi^\sigma_p(1)-\pi^\tau_p(1))\) were
\(0.879892,7.563729,9.514215\), still approaching the proved limit.
Small-prime behavior is not monotone and even the raw energy difference
has the opposite sign at \(p=7\). No asymptotic rate is inferred by fitting
these finite data.

The paired [visualization](../visualizations/five-defect-boundary-spectral-collapse.md)
shows the boundary-scaled profiles, signed mode residual, full and folded
spectral distances, and the separate raw energy difference. It documents
the representation and its controls; equations (4)–(11), not the picture,
establish the claim.

## Prior art and boundaries

Hall and Shiu, *The index of a Farey sequence*, Michigan Math. J. 51 (2003),
209–223, [DOI 10.1307/mmj/1049832901](https://doi.org/10.1307/mmj/1049832901),
is the classical index source. The totient asymptotic is classical
(Dress, 1999, already in this line's SOURCES.md). Bounded-variation Fourier
decay is classical; see Taibleson (1967) and
[Wu (1993)](https://www.ams.org/proc/1993-117-03/S0002-9939-1993-1150658-3/).
Finite sine orthogonality, endpoint suppression, and total-variation
contraction are standard. A targeted comparison against index/neighbor,
BV-Fourier and permutation-transport formulations supplies no basis for
claiming a new general theorem in any of these areas.

FD-329 already provides the raw energy difference. VIS-448 already provides
the variation estimate. Neither gives (2)–(3) for this equal-rank pair:
the additional content is the boundary estimate (8) combined with its
nonzero energy-normalization witness. It resolves this pair's spectral
question in the [five-defect clue](../clues/CLUE-five-defect-rank-collision-spectral-control.md),
without proving general five-defect rank-and-value uniqueness.

For the **full reassembled discrepancy**, FD-320 leaves the residual
\(P_\sigma D\), of norm \(\sqrt{E_p}\). Its unconditional \(E_p=o(1)\)
can support convergence to the same limiting law when transport stays
bounded below, but does not supply a rate small enough to transfer the
\(p^{-1}\) distinction proved here. The generic norm-to-spectral bound
would require \(\sqrt{E_p}=o(p^{-1})\) for that transfer; no such estimate
is asserted. These are artificial labeled-edge controls, not two genuine
Farey sequences. There is no Franel–Landau improvement or RH consequence.
