# PC-429 — one-prime Hilbert orbits are uniformly Riesz, but their marked transports cannot be combined

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE for treating a bounded single-prime marked intertwiner as a source-specific or critical-line mechanism after PC-427--PC-428. At every fixed \(0<\sigma<1\), and for every prime \(p\), the \(\mathbb Z\log p\)-translation orbits of the genuine and zero-free-control Hilbert--Schmidt seeds are Riesz sequences with bounds **uniform in \(p\)**. Their one-prime cyclic subspaces admit a canonical bounded, boundedly invertible marked intertwiner; both operator norms can be bounded independently of \(p\). Nevertheless, for \(1/2<\sigma<1\), no single bounded marked intertwiner can respect two distinct prime shifts simultaneously (PC-428).

The underlying one-generator fiber/Riesz criterion is standard spectral and shift-invariant-space theory. The line-local delta is the precise contrast between **uniformly well-conditioned separate prime directions** and **incompatible simultaneous directions**, established for the actual source-generated Bose seed and its PC-424 zero-free control. No new zeta-zero constraint or RH criterion follows.

## 1. Exact cyclic objects and the sampled spectral measure

Fix \(0<\sigma<1\). In the PC-427 Fourier model
\[
\mathcal E=L^2(\mathbb R,d\mu),\qquad
d\mu(t)=\frac2\pi|t|\,dt,\qquad
U_af(t)=e^{iat}f(t),
\tag{1}
\]
the genuine and matched-control seed vectors are
\[
g_\sigma(t)=\frac{\Gamma(\sigma-it)\zeta(\sigma-it)}{\sqrt{2\pi}},
\quad
g_{0,\sigma}(t)=
-\frac{1+\sigma-it}{2(1-\sigma+it)}
\frac{\Gamma(\sigma-it)}{\sqrt{2\pi}}.
\tag{2}
\]
Both belong to \(\mathcal E\) and are nonzero almost everywhere. For \(j\in\{1,0\}\) put
\[
w_{j,\sigma}(t)=\frac2\pi|t|\,|g_{j,\sigma}(t)|^2.
\tag{3}
\]
These are continuous nonnegative integrable functions, with positive total masses
\[
M_{j,\sigma}=\int_{\mathbb R}w_{j,\sigma}(t)\,dt
=\|g_{j,\sigma}\|_{\mathcal E}^2>0.
\tag{4}
\]
The gamma factor gives exponential decay at infinity, multiplied at most by polynomial zeta growth for fixed \(\sigma\); hence periodizations converge uniformly for any period bounded away from zero.

For a prime \(p\ge2\), write \(a_p=\log p\) and \(T_p=2\pi/a_p\). Define the two **folded densities**
\[
F_{j,\sigma,p}(\theta)
=\sum_{k\in\mathbb Z}w_{j,\sigma}(\theta+kT_p),
\quad -T_p/2\le\theta\le T_p/2.
\tag{5}
\]
For any Laurent polynomial \(P(z)=\sum_{m=-N}^Nc_mz^m\), decomposition into period cells gives the exact formula
\[
\boxed{
\|P(U_{a_p})g_{j,\sigma}\|_{\mathcal E}^2
=\int_{-T_p/2}^{T_p/2}
|P(e^{ia_p\theta})|^2F_{j,\sigma,p}(\theta)\,d\theta.
}
\tag{6}
\]
This is the pushforward of the vector spectral measure by \(t\mapsto e^{ia_pt}\); it is **not** the unfurled spectral density ratio in PC-428.

## 2. Explicit uniform positivity from the first-zero gap

The first nontrivial zero of \(\zeta\) in the critical strip has ordinate \(t_1=14.134725\ldots\); the low-height zero census is complete, not merely a list of zeros found on the critical line (NIST DLMF §25.10, the LMFDB zeta-zero census). The elementary strict inequality
\[
\boxed{
\frac{3T_p}{2}\le\frac{3\pi}{\log2}
=13.597\ldots<t_1
}
\tag{7}
\]
holds for **every prime**. For \(\theta\in[-T_p/2,T_p/2]\), the term with \(k=1\) in (5) has
\[
T_p/2\le\theta+T_p\le3T_p/2.
\tag{8}
\]
Throughout this interval \(t>0\), and \(\zeta(\sigma-it)\) has no zeros for any \(0<\sigma<1\). The other factors in (2)--(3) are also nonzero. Hence
\[
\boxed{
F_{1,\sigma,p}(\theta)>0,\qquad
F_{0,\sigma,p}(\theta)>0
\quad\text{for every }\theta,\ p\ge2.
}
\tag{9}
\]
The nonvanishing is pointwise and, by continuity on a compact period cell, has a positive minimum for each fixed \(p\). A possible zero of \(\zeta\) at a much larger ordinate cannot eliminate the folded measure: the same residue class already contains the nonzero low-frequency sample (8). A zero at \(t=0\) of the weight \(|t|\) likewise does not matter.

There is a **uniform** statement across prime generators. For any fixed \(\sigma\) and \(j\), as \(T\downarrow0\),
\[
\boxed{
\sup_{|\theta|\le T/2}
\left|
T\sum_{k\in\mathbb Z}w_{j,\sigma}(\theta+kT)
-M_{j,\sigma}\right|\longrightarrow0.
}
\tag{10}
\]
This is the uniform shifted Riemann-sum theorem, proved by uniform continuity on a large compact interval and by a uniform exponentially decaying tail bound outside it. For \(T\) in any closed interval \([\delta,2\pi/\log2]\), the periodized sums and their products with \(T\) vary continuously in \(T\) and in the normalized cell coordinate \(\theta/T\), and (8)--(9) keep them strictly positive. Compactness together with (10) therefore supplies constants
\[
\boxed{
0<\alpha_{j,\sigma}\le
T_pF_{j,\sigma,p}(\theta)
\le\beta_{j,\sigma}<\infty
\quad\text{for all primes }p,\ \theta.
}
\tag{11}
\]
The constants may depend on \(\sigma\) and the seed, not on \(p\).

## 3. Each single-prime orbit is a uniformly stable Riesz sequence

The characters \(e^{ima_p\theta}\), \(m\in\mathbb Z\), are the Fourier basis of the period-\(T_p\) circle, so
\[
\int_{-T_p/2}^{T_p/2}
|P(e^{ia_p\theta})|^2\,d\theta
=T_p\sum_m|c_m|^2.
\tag{12}
\]
Equations (6), (11), and (12) yield
\[
\boxed{
\alpha_{j,\sigma}\sum_m|c_m|^2
\le
\left\|\sum_m c_mU_{m\log p}g_{j,\sigma}\right\|_{\mathcal E}^2
\le
\beta_{j,\sigma}\sum_m|c_m|^2
}
\tag{13}
\]
for every finitely supported sequence, with **bounds independent of the prime**. Thus each orbit \(\{U_{m\log p}g_{j,\sigma}:m\in\mathbb Z\}\) is a Riesz basis for its own closed cyclic subspace
\[
\mathcal H^{(p)}_{j,\sigma}
=\overline{\operatorname{span}}\{U_{m\log p}g_{j,\sigma}:m\in\mathbb Z\}.
\tag{14}
\]
This does not contradict PC-426: there the family consists of **one shell vector per varying prime** with increasingly clustered logarithmic locations, whereas (13) fixes one prime and varies the integer power of its shift.

In fact (10) shows the stronger asymptotically tight limit
\[
\boxed{
\sup_{\|c\|_{\ell^2}=1}
\left|
\left\|\sum_m c_mU_{m\log p}g_{j,\sigma}\right\|_{\mathcal E}^2
-M_{j,\sigma}\right|\longrightarrow0
\quad(p\to\infty).
}
\tag{15}
\]
The supremum is first understood for finite sequences and extends by (13). Thus the whole infinite Gram operator tends to \(M_{j,\sigma}I\) in operator norm as \(p\to\infty\), not merely entrywise on fixed finite blocks.

## 4. Bounded one-prime marked transport, including every prime-power shell

Define on Laurent-polynomial orbit vectors
\[
\mathcal W_{p,\sigma}^{(0)}:
P(U_{\log p})g_{0,\sigma}
\longmapsto P(U_{\log p})g_\sigma.
\tag{16}
\]
It is well defined by the Riesz lower bounds (13), commutes with \(U_{\log p}\), and extends uniquely to a bounded bijection
\[
\boxed{
\mathcal W_{p,\sigma}:
\mathcal H^{(p)}_{0,\sigma}
\xrightarrow[\text{bounded inverse}]{\text{bounded}}
\mathcal H^{(p)}_{1,\sigma}.
}
\tag{17}
\]
The exact squared norms are
\[
\|\mathcal W_{p,\sigma}\|^2
=\max_\theta\frac{F_{1,\sigma,p}(\theta)}
                         {F_{0,\sigma,p}(\theta)},
\qquad
\|\mathcal W_{p,\sigma}^{-1}\|^2
=\max_\theta\frac{F_{0,\sigma,p}(\theta)}
                         {F_{1,\sigma,p}(\theta)}.
\tag{18}
\]
Both are bounded **uniformly in \(p\)** by (11). As \(p\to\infty\), (10) gives
\[
\boxed{
\|\mathcal W_{p,\sigma}\|^2\to
\frac{M_{1,\sigma}}{M_{0,\sigma}},
\quad
\|\mathcal W_{p,\sigma}^{-1}\|^2\to
\frac{M_{0,\sigma}}{M_{1,\sigma}},
\quad
\|\mathcal W_{p,\sigma}\|
\|\mathcal W_{p,\sigma}^{-1}\|\to1.
}
\tag{19}
\]

The primitive-shell multipliers of PC-427 obey
\[
g_{p^k,\sigma}(t)
=q_{p^k,\sigma}(t)g_\sigma(t),\quad
g_{0,p^k,\sigma}(t)
=q_{p^k,\sigma}(t)g_{0,\sigma}(t),
\tag{20}
\]
where
\[
q_{p^k,\sigma}(t)=
-p^{k(1-\sigma)}e^{ik(\log p)t}
(1-p^{\sigma-1}e^{-i(\log p)t})
\tag{21}
\]
is bounded, bounded away from zero, and \(T_p\)-periodic **for each fixed \(p,k\)**. It follows that both prime-power shell vectors lie in their respective spaces (14), remain cyclic there, and
\[
\boxed{\mathcal W_{p,\sigma}g_{0,p^k,\sigma}
=g_{p^k,\sigma}\qquad(k\ge1).}
\tag{22}
\]
The same one-prime transport therefore respects every source-native \(p\)-power shell. No claim is made that it transports composite shells involving a second prime within these one-generator cyclic spaces.

## 5. Two-prime incompatibility and exact information boundary

For distinct primes \(p,q\), \(\log p/\log q\) is irrational. Their integer log-shift group is dense in \(\mathbb R\). By PC-427, the joint orbit of either seed then spans the **full** embedded Hilbert--Schmidt sector \(\mathcal E\), rather than the proper one-generator cyclic subspace (14). Any bounded operator carrying \(g_{0,\sigma}\) to \(g_\sigma\) and intertwining both prime shifts must intertwine every real translation by continuity. On the dense orbit its action is the multiplier
\[
R_\sigma(t)=\frac{g_\sigma(t)}{g_{0,\sigma}(t)}
=-2\frac{1-\sigma+it}{1+\sigma-it}\zeta(\sigma-it).
\tag{23}
\]
PC-428, using Bohr--Courant value density, proves that \(R_\sigma\) and \(1/R_\sigma\) are essentially unbounded for **every \(1/2<\sigma<1\)**. Hence
\[
\boxed{
\text{Every individual prime has a uniformly bounded marked transport,}
\quad
\text{but no two distinct primes have a common bounded one}
}
\tag{24}
\]
in that right-half-strip regime, where the latter means *one bounded intertwiner of both shifts taking the control marked seed to the actual seed*. The incompatible maps in (17) have different cyclic domains and are not assumed to form a coherent operator family on \(\mathcal E\).

The mechanism is **spectral aliasing**: sampling one log shift folds all Fourier frequencies into a circle, and a small zero-free frequency band forces both folded densities to be positive. Adding an incommensurable second shift restores full-frequency resolution and exposes the unbounded classical zeta ratio. The individual orbit property and its uniformly stable bounds are reproducible for other fast-decaying seed pairs having an appropriate common low-frequency nonvanishing interval, irrespective of primality or zeta zeros.

## 6. Prior art, audit, and scope

**Classical analytic inputs.** The Riesz/fiber criterion (6)--(13) is a one-generator specialization of Fourier-fiber methods in A. Ron and Z. Shen, *Frames and Stable Bases for Shift-Invariant Subspaces of \(L^2(\mathbb R^d)\)*, *Canadian Journal of Mathematics* 47 (1995), 1051--1094, DOI 10.4153/CJM-1995-056-1. The cyclic unitary spectral measure is classical; see the spectral representation references already used in PC-427. NIST DLMF §25.10 and the LMFDB complete low-height zeta-zero census anchor the verified no-zero range beneath the first ordinate \(14.134725\ldots\). PC-428 supplies the Bohr--Courant and marked-multiplier obstruction for the two-shift closure. No novelty is claimed for the abstract fiber theorem, first-zero height, Riemann-sum convergence, or Bohr--Courant.

**Project-specific implication.** A one-prime Riesz frame or bounded, even uniformly well-conditioned, marked vector transport cannot signal the critical line: the zero-free control has precisely the same one-prime orbit properties. The source remains present in the *exact* folded densities and their Fourier coefficients, but bounded equivalence after folding is too coarse to distinguish the arithmetic zeros. Any future use of simultaneous prime directions must preserve a source-forced, analytically meaningful compatibility or coupling rather than combine individually bounded transfers by fiat.

**Falsification points.** Recheck the Fourier translation sign and \(2/\pi\) weight in PC-427; the period \(T_p=2\pi/\log p\); the strict gap \(3\pi/\log2<t_1\); the \(|t|\) zero at the origin; convergence and uniformity of the shifted Riemann sums (10); the factorization/periodicity of (21); and the distinction between a bounded map of *one-generator cyclic subspaces* and a bounded equivariant map of the full two-generator closure. Statement (24) is not asserted for \(\sigma\le1/2\), where PC-428 does not furnish the requisite joint no-go. None of these results proves RH or excludes off-line zeta zeros.
