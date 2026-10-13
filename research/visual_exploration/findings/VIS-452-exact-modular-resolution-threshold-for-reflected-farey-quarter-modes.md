# VIS-452 — an exact modular-resolution threshold for the reflected Farey quarter-mode sector

## Claim and evidence status

Take the odd-parameter reflected artificial Farey transport of VIS-451, with odd integer \(a\ge5\). After first passing to its fixed-\(a\) continuum/source-prime limit, the **quarter-mode-conditioned** positive-index law is exactly
\[
p_a(\ell)=\frac1a f(\ell/a),\qquad
f(x)=\frac{(1-\cos 2\pi x)^2}{\pi^2x^2},\quad
\ell\ge1,\quad f(0)=0,\quad \sum_{\ell\ge1}p_a(\ell)=1.
\tag{1}
\]
Put mass \(p_a(\ell)/2\) at each of the **signed** indices \(+\ell\) and \(-\ell\), and push that law forward into residues \(r\in\mathbb Z/q\mathbb Z\). Call the resulting probability law \(\nu_{a,q}\). For every integer \(1\le q\le a\), it satisfies the following **exact finite-parameter transition**:
\[
\boxed{\quad
\nu_{a,q}(r)=
\begin{cases}
1/q, &2q\le a,\\[3pt]
q^{-1}\!\left[1-(2-a/q)\cos(2\pi r/q)\right],
&a<2q\le2a.
\end{cases}\quad}
\tag{2}
\]
In particular, the symmetrized projection is **perfectly uniform at every modulus at most \(a/2\)**, including growing moduli. At the moving resolution \(q=a\), it instead equals
\[
\nu_{a,a}(r)=a^{-1}[1-\cos(2\pi r/a)],\qquad
\nu_{a,a}(0)=0.
\tag{3}
\]
For \(a/2<q\le a\), the total-variation distance from the uniform law \(U_q\) is exactly
\[
\operatorname{TV}(\nu_{a,q},U_q)
=\frac{2-a/q}{2q}\sum_{r=0}^{q-1}|\cos(2\pi r/q)|.
\tag{4}
\]
If \(q=q(a)\) and \(q/a\to c\in(0,1]\), its limit is
\[
\boxed{\quad
\lim\operatorname{TV}(\nu_{a,q},U_q)
=\frac{\max(0,\,2-1/c)}{\pi}.
\quad}
\tag{5}
\]
For \(q=a\) and odd \(a\), the finite cosine sum additionally yields
\[
\operatorname{TV}(\nu_{a,a},U_a)
=\frac1{2a\sin(\pi/(2a))}\longrightarrow\frac1\pi.
\tag{6}
\]

**Evidence:** EXACT-DERIVED; CLASSICAL FOURIER/SAMPLING SPECIALIZATION; NEGATIVE REPRESENTATION/ALIASING CONTROL. The additional source-specific statement is the sharp resolution threshold in the exact conditional law (1), not a new general Fourier theorem, a genuine-Farey arithmetic statistic, or an RH implication.

## Derivation: finite Fourier support and modular inversion

Extend \(f\) evenly to \(\mathbb R\), and let \(\Lambda(t)=(1-|t|)_+\). With Fourier convention \(\widehat f(t)=\int_{\mathbb R}f(x)e^{-2\pi i tx}\,dx\), the standard squared-sinc/triangular-transform identity gives
\[
f(x)=2(1-\cos2\pi x)\left(\frac{\sin\pi x}{\pi x}\right)^2,
\qquad
\widehat f(t)=2\Lambda(t)-\Lambda(t-1)-\Lambda(t+1).
\tag{7}
\]
Thus \(\Phi=\widehat f/2\) is continuous, even, supported on \([-2,2]\), and, for \(u=|t|\), has the **piecewise linear** values
\[
\Phi(t)=
\begin{cases}
1-\frac32u,&0\le u\le1,\\
\frac12u-1,&1\le u\le2,\\
0,&u\ge2.
\end{cases}
\tag{8}
\]
Since \(f(x)=O(x^{-2})\) and \(\widehat f\) is compactly supported, Poisson summation applies absolutely in the present sampled form. The signed-index characteristic function is
\[
C_a(t)=\sum_{\ell\ge1}p_a(\ell)\cos(2\pi t\ell)
=\frac12\sum_{\ell\in\mathbb Z}\frac1a f(\ell/a)e^{-2\pi it\ell}
=\sum_{n\in\mathbb Z}\Phi\bigl(a(t+n)\bigr).
\tag{9}
\]
In particular \(C_a(0)=1\) for \(a\ge5\), agreeing with (1).

The discrete Fourier coefficients of the modular law are \(\widehat\nu_{a,q}(j)=C_a(j/q)\), \(j=0,\ldots,q-1\). For every nonzero \(j\), the distance of \(j/q\) to an integer is at least \(1/q\), so the closest argument in (9) has absolute value at least \(a/q\). If \(2q\le a\), this is at least two and (8) makes **all** nonconstant Fourier coefficients zero. Fourier inversion proves the first case of (2), without any limiting argument.

If \(a/2<q\le a\), then \(q\ge3\) since \(a\ge5\). The only potentially nonzero coefficients are \(j=1\) and \(j=q-1\); their value, by the second interval of (8), is
\[
C_a(1/q)=C_a((q-1)/q)=\frac{a}{2q}-1.
\tag{10}
\]
All other nonconstant coefficients vanish. Fourier inversion therefore gives
\[
\nu_{a,q}(r)=\frac1q\left[1+2\left(\frac a{2q}-1\right)
\cos(2\pi r/q)\right],
\]
which proves the second case of (2). Formula (4) is now the definition of total variation. For \(q/a\to c>1/2\), we have \(q\to\infty\) and \(q^{-1}\sum_r|\cos(2\pi r/q)|\to2/\pi\); for \(c\le1/2\), the modulation vanishes, proving (5). The elementary finite sum of absolute cosines for odd \(a\) proves (6).

## Controls: the folding and resolution rules matter

This is **not** uniformity of the original one-sided positive frequency indices. For an explicit control, \(a=7\), \(q=3\) gives \(\nu_{7,3}=(1/3,1/3,1/3)\) exactly, but the *unfolded* law \(\sum_{\ell\equiv r\pmod3}p_7(\ell)\) is approximately \((0.33333,0.31104,0.35563)\). These values follow by summing the first \(10^5\) terms of (1), with a total omitted mass bounded by \(4a/(\pi^2 10^5)<2.9\times10^{-5}\); the inequality is sufficient to certify that the unequal unfolded residues are not a numerical truncation artifact. Folding kills the imaginary/sine Fourier coefficients, which have no reason to share the compact-support vanishing of (9).

A separate exact verification at \(q=a\) uses the one-sided residue masses
\[
P_a^+(r)=\frac{(1-\cos(2\pi r/a))^2}{a\pi^2}\,\psi_1(r/a),
\qquad 1\le r<a,\quad P_a^+(0)=0,
\tag{11}
\]
where \(\psi_1(x)=\sum_{n\ge0}(n+x)^{-2}\). Combining \(r\) and \(a-r\) by the classical reflection identity
\(\psi_1(x)+\psi_1(1-x)=\pi^2/\sin^2(\pi x)\) recovers (3) coefficient by coefficient. Independently, summing (1) to a large finite cutoff for \(a=5,7,9,21\) and various \(q\le a\) agrees with (2) within the explicit \(O(a/M)\) positive Fourier-tail bound. The identities (7)–(10), not visual resemblance or numerical agreement, prove the theorem.

The Fourier support \([-2,2]\) is imposed by the particular squared-sinc representation. The exact threshold \(q=a/2\), the first harmonic after crossing, and the apparent nonuniformity at \(q=a\) are therefore **representation/normalization effects**, not newly detected number-theoretic correlations. Removing sign symmetrization, changing the frequency embedding, or examining \(q>a\) changes the question; (2) does not assert uniformity or this simple sinusoidal law in those settings.

## Source attribution and research consequence

The positive quarter-mode law (1) comes from the reflection-preserving **artificial** Farey transport of VIS-451, itself specialized from FD-324; VIS-449 provides a related but differently indexed unreflected conditional density. The Fourier/Bernoulli identity and Poisson/sampling mechanism are standard: NIST DLMF §24.8(i), https://dlmf.nist.gov/24.8, and Stein–Shakarchi, *Fourier Analysis: An Introduction* (Princeton, 2003), both already anchored in this line's SOURCES.md. The trigamma reflection relation used only as an independent control is classical (NIST DLMF §5.15, https://dlmf.nist.gov/5.15). Neither the band-limited-transform principle nor the modular inversion mechanism is claimed as independently novel.

The result gives the accepted reflected/unreflected Farey-control clue a further **falsification gate**: a folded, residue-projected conditional spectrum can look *exactly* uniform for every \(q\le a/2\) and yet stay a fixed positive distance from uniform at \(q=a\). To claim an arithmetic residual, one must fix signed versus one-sided indexing, sector conditioning, the scale \(q/a\), and the model's own null first. This does not supply a source-natural order restriction or a genuine-Farey residual.

All statements concern the continuum limit taken at **fixed odd \(a\)** before letting \(a\) grow. Any simultaneous source-prime/\(a\)/modulus limit requires separate finite-transport profile approximation and the projected sector-energy stability gate of VIS-450; the present exact continuum calculation grants no uniform prime-progression estimate, no Franel–Landau improvement, and no implication toward RH.
