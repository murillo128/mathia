# VIS-455 — Same-prime fixed-defect Farey controls have a moving Haar sine spectrum

## Claim and evidence status

Consider the *artificial directed-edge reassemblies* of FD-327, rather than genuine Farey orderings. For an integer \(m\ge3\), put
\[
\alpha_m=1-\frac1m,\qquad d_m=\frac2{m(m+2)},\qquad e_m=\frac2{(m+2)(m+4)}.
\]
Their fixed-\(m\), source-prime-limit transport profile on \((0,1)\) is
\[
g_m(x)=d_m\mathbf1_{(\alpha_m,\alpha_m+e_m)}(x)
       -e_m\mathbf1_{(\alpha_m+e_m,\alpha_m+e_m+d_m)}(x).
\tag{1}
\]
Set
\[
b_m(r)=\sqrt2\int_0^1g_m(x)\sin(\pi rx)\,dx,\qquad
\pi_m(r)=\frac{b_m(r)^2}{\|g_m\|_2^2}\quad(r\ge1).
\tag{2}
\]
By sine Parseval, \(\sum_{r\ge1}\pi_m(r)=1\). Writing \(M=m^2\), as \(m\to\infty\), the normalized spectral laws \(\sum_{r\ge1}\pi_m(r)\delta_{r/M}\) converge weakly to the probability measure
\[
\boxed{f(u)\,du,\quad f(u)=\frac{(1-\cos2\pi u)^2}{\pi^2u^2},\quad f(0)=0,\quad \int_0^\infty f(u)\,du=1.}
\tag{3}
\]
In particular, for every \(R>0\),
\[
\lim_{m\to\infty}\sum_{r\le Rm^2}\pi_m(r)=\int_0^R f(u)\,du.
\tag{4}
\]
There exists an absolute \(C\) such that, for integers \(1\le Q\le m^2\),
\[
\boxed{\sum_{r\le Q}\pi_m(r)\le C(Q/m^2)^3.}
\tag{5}
\]
Thus the *absolute* energy shrinks as \(m^{-6}\), but after normalizing by each profile's own energy, the spectral mass migrates to positive sine modes \(r\asymp m^2\). This applies to the two controls \(m=3\) and \(m=t+3\) assembled from the **same prime** in FD-327: the former retains positive fixed-mode energy, while the latter loses every fixed-band *fraction* as \(t\to\infty\), despite the identical ordered scaled local index-defect values \((-2,4,-2)\) at each admissible common prime. Their defect positions are different.

**Evidence:** EXACT-DERIVED; CLASSICAL HAAR/FOURIER-SCALING SPECIALIZATION; NEGATIVE DEFECT-ONLY/REPRESENTATION CONTROL. The statement is a nested *fixed-cut source-prime limit, then growing cut parameter*. It is not a uniform simultaneous-prime theorem or a genuine-Farey arithmetic anomaly.

## Exact coefficients and normalization

Direct integration of (1), using \(\alpha_m+d_m+e_m=\alpha_{m+4}\), gives for every \(m\ge3\), \(r\ge1\),
\[
b_m(r)=\frac{\sqrt2}{\pi r}\left[
d_m\cos(\pi r\alpha_m)
-(d_m+e_m)\cos(\pi r(\alpha_m+e_m))
+e_m\cos(\pi r\alpha_{m+4})\right].
\tag{6}
\]
The normalizing energy is exactly
\[
\|g_m\|_2^2=d_m^2e_m+e_m^2d_m
=d_me_m(d_m+e_m)
=\frac{16}{[m(m+2)(m+4)]^2}.
\tag{7}
\]
This **complete one-sided sine-mode** law is different from VIS-451/452/453's *reflected, quarter-mode-conditioned* spectrum: their formula must not be transplanted to FD-327.

## Proof of the moving Haar law

Put \(M=m^2\), \(D_m=Md_m\), \(F_m=Me_m\), and
\[
h_m(z)=\frac{D_m}{2}\mathbf1_{(0,F_m)}(z)
-\frac{F_m}{2}\mathbf1_{(F_m,F_m+D_m)}(z).
\]
Then \(g_m(\alpha_m+z/M)=2h_m(z)/M\), \(D_m,F_m\to2\), and \(h_m\to h=\mathbf1_{(0,2)}-\mathbf1_{(2,4)}\) in both \(L^1\) and \(L^2\). In particular \(\|h\|_2^2=4\), and
\(\|g_m\|_2^2=4\|h_m\|_2^2/M^3\).

Define \(H_m(u)=\int_{\mathbb R}h_m(z)e^{i\pi uz}\,dz\). The exact sine identity, with \(u=r/M\), is
\[
\boxed{\pi_m(r)=\frac{|H_m(r/M)|^2-\operatorname{Re}\big(e^{-2\pi ir/m}H_m(r/M)^2\big)}
 {M\|h_m\|_2^2}.}
\tag{8}
\]
The second term is a **sine-boundary/translation phase**, not a negligible pointwise error. Nevertheless the geometric partial sums of \(e^{-2\pi ir/m}\) have magnitude \(O(m)\). On \(r\le RM\), \(H_m(r/M)^2\), multiplied by any fixed compactly supported \(C^1\) test, has uniformly bounded variation; summation by parts and the factor \(1/M\) make the phase contribution \(O(m/M)=O(m^{-1})\). The nonoscillatory part is a Riemann sum and converges to \(\int\varphi(u)|H(u)|^2/\|h\|_2^2\,du\).

Integration of the limiting balanced step yields
\[
H(u)=-\frac{(e^{2\pi iu}-1)^2}{i\pi u},\qquad
\frac{|H(u)|^2}{\|h\|_2^2}
=\frac{(1-\cos2\pi u)^2}{\pi^2u^2}=f(u).
\tag{9}
\]
Under the convention \(e^{i\pi uz}\), Plancherel gives
\(\int_{\mathbb R}|H(u)|^2du=2\|h\|_2^2\). Since \(h\) is real, the positive half-axis carries exactly \(\|h\|_2^2\); hence \(\int_0^\infty f=1\).

Every \(h_m\) has zero mean, compact support of uniformly bounded length, and uniformly bounded variation. Thus
\(\lvert H_m(u)\rvert\le C\min(|u|,|u|^{-1})\), uniformly in \(m\). Formula (8) implies
\(\pi_m(r)\le C\min(r^2/M^3,M/r^2)\), proving (5) by summation, and
\(\sum_{r>RM}\pi_m(r)\le C/R\) for \(R\ge1\). This uniform tightness upgrades compact-test convergence to weak convergence of probabilities and yields (4). Conversely, if \(Q/m^2\to\infty\), the tail estimate shows that \(Q\) captures all normalized energy.

## Source-prime transfer and boundary of the theorem

FD-327 constructs both \(m=3\) and \(m=t+3\) from the **same** order-\(p\) Farey edge list for each fixed \(t\), on primes \(p\equiv1\pmod{\operatorname{lcm}(3,5,7,t+3,t+5,t+7)}\). At fixed \(m\), its exact sine-Parseval transport error is \(E_p=o(1)\) and its rescaled rank transport step converges in \(L^2\) to \(g_m\), with limiting transport norm \((3/\pi^2)\|g_m\|_2^2>0\). Normalizing therefore yields total-variation convergence of the finite positive sine-energy law to (2) for **fixed \(t\), as the common prime tends to infinity**. Only after this step do (3)–(5) apply with \(t\to\infty\).

No simultaneous uniform \(m=m(p)\to\infty\) estimate follows from the fixed-parameter prime number theorem. Since the limiting energy is \(C_m=(3/\pi^2)\|g_m\|_2^2\asymp m^{-6}\), a sufficient transfer must control the finite genuine-Farey perturbation relatively, for example \(E_p=o(C_m)\), *and* the finite transport-to-\(g_m\) approximation in relative \(L^2\). A diagonal sequence with separately chosen sufficiently large admissible primes exists by the fixed-\(t\) results, but is not a uniform growing-parameter rate.

## Independent checks, prior art, and failure modes

Using (6)–(7) independently of the Haar/Riemann-sum argument, the fractions of total positive sine energy below \(m^2\) are approximately \(0.8486445208\), \(0.8555866968\), and \(0.8557032796\) at \(m=20,80,250\). Independent numerical quadrature of (3) on \([0,1]\) gives \(0.8557073274\). These checks do not replace the exact proof; they expose the moving scale and the finite-\(m\) sine-phase oscillations.

The balanced two-block profile, Fourier scale/translation behavior and Plancherel are classical; compare Strang and Nguyen, *Wavelets and Filter Banks* (1996), Chapters 1–2, and Stein and Shakarchi, *Fourier Analysis: An Introduction* (2003). This finding claims **no new general wavelet theorem**. Its line-specific result is the correct full positive sine-law and \(m^2\) spectral window for FD-327's same-prime fixed-defect controls. Equality of (9) with VIS-451's rare-sector density reflects a common limiting dipole kernel after two *different* rescalings and conditionings, not a proof of an arithmetic relation.

Coefficient squaring erases sign and cannot recover signed orientation or the physical cut. In particular, the sharp modular uniformity threshold of VIS-452 belongs to another source law and does not follow for FD-327. The experiments are on artificial labeled-edge reassemblies, not alternate genuine Farey sequences. No anomaly of true Farey order, Franel–Landau improvement, or RH consequence follows. The remaining cut-location and genuinely source-natural orientation discriminator is the subject of the local fixed-defect clue.

## Research consequence

Identical ordered **values** of three local index defects do not determine even a matched same-prime control's normalized low-frequency energy: shrinking step transports move to \(r\asymp m^2\). A source-natural test must fix its frequency window, the raw versus normalized energy, orientation and rank/cut-position metadata before interpreting apparently vanishing or universal spectra.