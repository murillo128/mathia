# VIS-457 — Endpoint localization forces exact modular folding uniformity

## Claim and evidence status

Let \(m\ge2\) and let \(0\ne g\in L^2(0,1)\) be **real-valued** and supported, up to null sets, in the right endpoint strip \([1-1/m,1]\). Set
\[
b_r=\sqrt2\int_0^1 g(x)\sin(\pi r x)\,dx,\qquad
\mu_m^{\sin}(j)=\frac1{\|g\|_2^2}
 \sum_{\substack{r\ge1\\r\equiv j\pmod m}}b_r^2,
\quad j\in\mathbb Z/m\mathbb Z .
\]
Sine Parseval makes \(\mu_m^{\sin}\) a probability law. **For every finite \(m\)**, every residue satisfies the exact identity
\[
\boxed{\mu_m^{\sin}(j)+\mu_m^{\sin}(-j)=\frac2m,\qquad
\widetilde\mu_m^{\sin}(j):=\frac{\mu_m^{\sin}(j)+\mu_m^{\sin}(-j)}2
=\frac1m.}\tag{1}
\]
Thus the one-sided deviation is *exactly odd* under residue reflection, not merely asymptotically odd. In particular, \(\mu_m^{\sin}(0)=1/m\), and for even \(m\), \(\mu_m^{\sin}(m/2)=1/m\).

If in addition \(\int_0^1g=0\), the corresponding **positive cosine-mode** probability law
\[
\mu_m^{\cos}(j)=
\frac2{\|g\|_2^2}\sum_{\substack{r\ge1\\r\equiv j\pmod m}}
\left(\int_0^1g(x)\cos(\pi r x)\,dx\right)^2
\]
obeys the same exact identities. The zero-mean condition matters: otherwise the omitted constant cosine coefficient carries nonzero spectral energy.

In the artificial same-prime Farey controls of FD-327, VIS-455's fixed-cut source-prime-limit profile is
\[
g_m=d_m\,\mathbf1_{(\alpha_m,\alpha_m+e_m)}
    -e_m\,\mathbf1_{(\alpha_m+e_m,\alpha_{m+4})},
\quad \alpha_j=1-\frac1j,\quad
d_m=\frac2{m(m+2)},\quad e_m=\frac2{(m+2)(m+4)}.
\]
For every \(m\ge3\), its support lies inside \([1-1/m,1]\), because
\(\alpha_{m+4}-\alpha_m=4/[m(m+4)]<1/m\), and its integral is \(d_me_m-e_md_m=0\). Therefore **both the sine and cosine signed-reflection-folded modular spectra are exactly uniform for each \(m\ge3\)**. This strictly strengthens VIS-456's asymptotic folded sine conclusion and supplies its exact cosine counterpart, without disturbing VIS-456's one-sided phase law.

**Evidence:** EXACT-DERIVED; CLASSICAL FOURIER AUTOCORRELATION/FINITE-DFT SPECIALIZATION; DECISIVE NEGATIVE FOLDING CONTROL. The universal boundary-strip implication is classical harmonic analysis applied to a precise source family, not a new general Fourier theorem or a genuine-Farey/RH result.

## Exact support–autocorrelation proof

Extend \(g\) to a real \(2\)-periodic function \(F_s\) by \(F_s(x)=g(x)\) on \(0<x<1\) and \(F_s(x)=-g(2-x)\) on \(1<x<2\). This odd reflection is supported inside the circular arc
\[
J=[1-1/m,\,1+1/m]\quad\text{on }\mathbb R/2\mathbb Z,
\]
whose length is exactly \(2/m\). Hence for every \(k=1,\ldots,m-1\), the supports of \(F_s(x)\) and \(F_s(x+2k/m)\) are disjoint up to null sets.

Use the period-\(2\) Fourier coefficients
\[
a_r=\frac12\int_0^2 F_s(x)e^{-i\pi rx}\,dx
=-i\int_0^1g(x)\sin(\pi r x)\,dx .
\]
In particular \(a_0=0\), \(a_{-r}=\overline{a_r}\), and period-\(2\) Parseval gives
\(\sum_{r\in\mathbb Z}|a_r|^2=\frac12\int_0^2|F_s|^2=\|g\|_2^2\).
The shifted inner products, using Plancherel, are
\[
C_k=\frac12\int_0^2F_s(x)\overline{F_s(x+2k/m)}\,dx
=\sum_{r\in\mathbb Z}|a_r|^2e^{-2\pi i r k/m}
=\begin{cases}\|g\|_2^2,&k=0,\\0,&1\le k<m.\end{cases}
\tag{2}
\]
Writing \(P_j=\sum_{r\equiv j\pmod m}|a_r|^2\), the finite inverse DFT of (2) yields
\[
\boxed{P_j=\|g\|_2^2/m\quad\text{for every }j.}\tag{3}
\]
Since \(a_0=0\) and \(|a_{-r}|^2=|a_r|^2=b_r^2/2\), the left-hand side of (3) is precisely
\(\|g\|_2^2[\mu_m^{\sin}(j)+\mu_m^{\sin}(-j)]/2\).
This proves (1), including the self-opposite residue classes.

For cosine modes, instead use \(F_c(x)=g(x)\) for \(0<x<1\) and \(F_c(x)=g(2-x)\) for \(1<x<2\). It has the same boundary-strip support and translated disjointness, while its Fourier coefficients are \(\int_0^1g(x)\cos(\pi r x)\,dx\). The additional hypothesis \(\int g=0\) removes the zero mode, allowing the identical positive-mode argument.

The reasoning uses neither the values of the two step heights nor their Haar shape: *any* nonzero real profile localized in the boundary strip satisfies the sine identity, and any such zero-mean profile satisfies the cosine identity.

## Falsification control: short support is not enough

The result is a **boundary-position** criterion, not a generic consequence of having a short support. Take \(m=3\) and
\[
g(x)=\mathbf1_{(1/3-\varepsilon,\,1/3+\varepsilon)}(x),
\qquad 0<\varepsilon<1/12.
\]
Its support is shorter than \(1/3\), but is not in the right endpoint strip. For every positive integer \(k\),
\[
\int_0^1g(x)\sin(3\pi kx)\,dx=0
\]
by oddness around the center \(1/3\). Therefore \(\mu_3^{\sin}(0)=0\), whereas a folded-uniform law would require \(1/3\). Normalization forces
\(\widetilde\mu_3^{\sin}(1)=\widetilde\mu_3^{\sin}(2)=1/2\).
The reflected supports now overlap after a nontrivial \(2/3\)-periodic shift. Thus translating a sufficiently narrow profile can destroy the exact null.

As an independent **truncated diagnostic**, direct integration of VIS-455's finite-\(m\) step coefficients and summation to \(r=600{,}000\) at \(m=20\) gives maximum folded-residue error \(7.37\times10^{-6}\). The omitted total spectral mass is about \(1.23\times10^{-4}\), larger than the observed truncation error. A separately rendered high-resolution diagnostic confirmed the expected odd one-sided modulation and flat folded view. No plot or finite cutoff is needed for (1), and the temporary PNG is not being published as canonical evidence.

## Prior art, scope, and research consequence

The proof is the standard periodic Fourier autocorrelation identity followed by an \(m\)-point inverse DFT, using disjoint translated supports. Classical Fourier-series Parseval/translation/convolution theory is anchored by Stein–Shakarchi, *Fourier Analysis: An Introduction* (2003), already in this line's SOURCES.md; see also MIT OpenCourseWare, *Lecture 9: Fourier Transform Properties* (2011), for the classical translation/convolution/Parseval framework. No novelty is claimed for this general technique.

The mathematical delta relative to VIS-456 is **finite-parameter exactness together with profile-independence**: normalizing and folding the entire positive spectrum loses *every* boundary-strip profile distinction modulo the matching \(m\), even while VIS-456 shows an \(O(1)\) nonuniform one-sided cut phase and a sine/cosine sign reversal as \(m\to\infty\). This is a sharper obstruction to using the folded modular view as a source discriminator. It does not imply that the full spectra, one-sided residue laws, other moduli, or differently positioned cuts agree.

For FD-327 this is a theorem about \(g_m\), the **fixed-\(m\), source-prime-limit continuum transport profile**, not an exact identity for the finite-prime rank-grid Fourier transform. Transferring it to finite-prime normalized spectra first requires the fixed-\(m\) relative \(L^2\)/Parseval passage used by VIS-455/456. Neither (1) nor that fixed-parameter transfer supplies a uniform diagonal estimate when \(m=m(p)\) grows, nor a genuine Farey ordering constraint or a consequence for the Riemann hypothesis. The accepted fixed-defect clue still needs a source-natural discriminator and an explicit finite-prime growing-parameter error budget.