# ANF-196 — Positive-Fourier notches can have no power stability rate

**Status:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + FIXED-PROFILE + FOUR-REAL-SITE-CONTROL. The qualitative real envelope of ANF-195 survives, but its square-root rate cannot extend to the full dominated positive-Fourier profile class. A single continuous profile, supported in a fixed central interval and arbitrarily close in relative amplitude to a triangular notch, can fail every positive power rate. No nonreal configuration or growing cardinality is needed.

## Claim and normalization

Use the Montgomery--Taylor source
\[
J_0=g*g,\qquad F(t)=\widehat{J_0}(t)=K(t)^2,\qquad
K(t)=\frac{\cos(\pi t)-a t\sin(\pi t)}{1-2\pi^2t^2},
\quad a=\sqrt2\pi\cot(1/\sqrt2),
\tag{1}
\]
with removable values interpreted continuously. In particular \(F(0)=1\).
Here \(g(u)=\cos(\sqrt2u)/(\sqrt2\sin(1/\sqrt2))\) on
\([-1/2,1/2]\), and zero elsewhere, with the Fourier convention in (2).
ANF-087 gives the true positive roots \(r_j\in(j,j+1/2)\), \(j\ge1\).
For a finite nonempty real multiset \(W\), put
\[
L(W)=2|W|-\sigma(W),\quad S_W(\alpha)=\sum_{x\in W}e^{-2\pi i\alpha x},
\quad e(W)=\frac{\int J_0|S_W|^2}{L(W)}-1,
\quad h_\phi(W)=\frac{\int\phi|S_W|^2}{L(W)},
\tag{2}
\]
where \(\sigma\) counts simple real support sites. Write
\[
\beta_\phi^{\mathbb R}
=\lim_{\epsilon\downarrow0}\sup_{e(W)\le\epsilon}h_\phi(W).
\tag{3}
\]

Freeze any \(0<\eta<1/(2r_1)\) and any \(b>0\) for which
\[
\tau(\alpha)=b(1-|\alpha|/\eta)_+\le J_0(\alpha),\qquad
T(t)=\widehat\tau(t)=b\eta\operatorname{sinc}^2(\eta t).
\tag{4}
\]
Here \(\operatorname{sinc}(x)=\sin(\pi x)/(\pi x)\). Such \(b\) exists because
\(\eta<1\) and \(J_0\) is strictly positive on \([-\eta,\eta]\).

For every fixed \(0<\lambda<1\), there is a fixed real even continuous
profile \(\phi\), supported in \([-\eta,\eta]\), satisfying
\[
\frac{1-\lambda}{1+\lambda}\tau\le\phi\le\tau\le J_0,
\qquad \Phi:=\widehat\phi\ge0,
\tag{5}
\]
and a sequence of four distinct simple real sites \(W_n\) such that
\[
e(W_n)\asymp_\phi 2^{-2n^2},\qquad
h_\phi(W_n)-\beta_\phi^{\mathbb R}\ge c_\phi2^{-n}>0.
\tag{6}
\]
Consequently, for this **one fixed profile**, for every \(p>0\),
\[
\boxed{\displaystyle
\frac{h_\phi(W_n)-\beta_\phi^{\mathbb R}}{e(W_n)^p}\longrightarrow\infty.}
\tag{7}
\]
In particular there is no finite profile-dependent constant \(C_\phi\)
making \(h_\phi(W)\le\beta_\phi^{\mathbb R}+C_\phi e(W)^p\) valid for all
sufficiently small excess, even just on four-site real configurations.

## One frozen profile with sparse Fourier peaks

Set \(R_n=2^{n^2}\) and \(w_n=2^{-n}\), \(n\ge1\), so \(\sum_nw_n=1\).
Define the entire profile before selecting any configurations:
\[
\phi(\alpha)=\frac{\tau(\alpha)}{1+\lambda}
\left(1+\lambda\sum_{n\ge1}w_n\cos(2\pi R_n\alpha)\right).
\tag{8}
\]
The cosine series converges uniformly and has absolute value at most one.
Thus \(\phi\) is continuous and (5)'s pointwise bounds hold, including at
the support endpoints. The elementary Fourier modulation identity gives
\[
\Phi(t)=\frac1{1+\lambda}\left[
T(t)+\frac\lambda2\sum_{n\ge1}w_n
\{T(t-R_n)+T(t+R_n)\}\right]\ge0.
\tag{9}
\]
Termwise transformation is justified by the integrable majorant
\((1+\lambda)\tau\). The series in (9) is uniformly convergent since
\(0\le T(t)\le T(0)\). A finite-head/summable-tail argument also proves
\(\Phi(t)\to0\) as \(|t|\to\infty\). Moreover, positivity and translation
invariance give \(\|\Phi\|_1=\|T\|_1<\infty\).

At every prescribed large separation, the corresponding translated term
retains its central value:
\[
\boxed{\displaystyle
\Phi(R_n)\ge\frac{\lambda T(0)}{2(1+\lambda)}2^{-n}.}
\tag{10}
\]
There is no truncated-series or numerical positivity assumption here.

## Two exact equality pairs convert slow Fourier decay into slow stability

The profile meets all hypotheses of ANF-195, section 5. Hence its exact
all-cardinality real envelope is
\[
\beta_\phi^{\mathbb R}=\Phi(0)+M,\qquad
M=\max_{j\ge1}\Phi(r_j).
\tag{11}
\]
This maximum is positive: (9) implies
\(\Phi(r_1)\ge T(r_1)/(1+\lambda)>0\), since \(0<\eta r_1<1/2\).
It is attained because \(r_j\to\infty\) and \(\Phi\to0\). Choose one
maximizer \(r_*=r_j\); it is fixed after \(\phi\) is fixed and is independent
of \(n\).

For all sufficiently large \(n\), take
\[
W_n=\{0,r_*,R_n,R_n+r_*\}.
\tag{12}
\]
These are four distinct simple real sites and \(L(W_n)=4\). Their six
unordered separations are \(r_*\) twice, \(R_n\) twice, and \(R_n-r_*\),
\(R_n+r_*\) once each. Since \(F(r_*)=0\), exact pair counting gives
\[
e(W_n)=F(R_n)+\frac{F(R_n-r_*)+F(R_n+r_*)}{2},
\tag{13}
\]
\[
h_\phi(W_n)=\Phi(0)+\Phi(r_*)+\Phi(R_n)
+\frac{\Phi(R_n-r_*)+\Phi(R_n+r_*)}{2}.
\tag{14}
\]
All the last three terms are nonnegative. Equations (10)--(11) prove the
exposure lower bound in (6), with \(c_\phi=\lambda b\eta/[2(1+\lambda)]\).

The source excess has an exact integer-separation formula. Put
\(s_*:=\sin(\pi r_*)\ne0\) and \(D(t)=1-2\pi^2t^2\). The root equation is
\(\cos(\pi r_*)=a r_*s_*\). For an integer \(R\), the squared numerators
of \(K(R+r_*)\) and \(K(R-r_*)\) are both \(a^2R^2s_*^2\), while the
squared numerator of \(K(R)\) is one. For sufficiently large \(R=R_n\),
\[
e(W_n)=\frac1{D(R_n)^2}
+\frac{a^2R_n^2s_*^2}{2}
\left[\frac1{D(R_n-r_*)^2}+\frac1{D(R_n+r_*)^2}\right].
\tag{15}
\]
No removable denominator is encountered for large \(n\). Therefore
\[
R_n^2e(W_n)\longrightarrow
\frac{a^2\sin^2(\pi r_*)}{4\pi^4}>0.
\tag{16}
\]
This proves the excess estimate in (6). For every fixed \(p>0\), the ratio
in (7) is bounded below by a positive constant times
\(2^{2pn^2-n}\), which diverges.

## Consequence and falsification boundary

The automatic summable local Fourier envelope in ANF-195 is qualitative.
It cannot supply an algebraic tail or an algebraic finite-excess modulus.
The failure already occurs when each component is an exact maximizing
two-site equality configuration; the only changing geometry is the
separation between the two components. Thus bounding cardinality or
multiplicity does not repair the missing rate.

Taking \(\lambda\) arbitrarily small makes
\[
0\le\tau-\phi\le\frac{2\lambda}{1+\lambda}\tau.
\tag{17}
\]
So the existence of a positive power stability rate is not preserved by
arbitrarily small continuous relative-amplitude perturbations within this
positive-Fourier cone. The infinitely many fixed modulation frequencies
matter: no assertion of this kind is made for a finite modulation sum or
for a class with a prescribed Fourier-decay or differentiability bound.

There is no contradiction with the exact envelope: by (14),
\(h_\phi(W_n)\to\beta_\phi^{\mathbb R}\), because every cross term tends to
zero. There is also no contradiction with the triangular square-root
theorem: (10) implies \(R_n^2\Phi(R_n)\to\infty\), so this profile fails the
inverse-square majorant used in ANF-195's paired-source argument. That
particular decay condition is sufficient there; this counterexample does
not claim it is necessary for every profile admitting a power rate.

The decisive audit points are the global sign and domination in (5), the
positive shifted Fourier series (9), attainment of the **actual** profile's
maximizing root in (11), the six-pair normalization in (13)--(14), and the
integer/root identity in (15). Using a nonmaximizing root would leave a
fixed envelope gap and would not prove (7). The derivation is exact; a
standard-library check of the six-pair counts and a floating-point check
of (16) at the first root were sanity checks only, not certification of a
maximizer or of the infinite construction.

This result does not decide ANF-099's unrestricted complex envelope,
improve an unconditional critical-zero proportion, or imply RH. It rules out
an extension of the real stability theorem and identifies a
profile-regularity requirement for quantitative use of the broader cone.

## Prior art and mathematical delta

Fourier modulation and slow decay without regularity are classical.
The institutional record for Boche--Tampubolon,
[On the decay and smoothness behavior of the Fourier transform](https://portal.fis.tum.de/en/publications/on-the-decay-and-the-smoothness-behavior-of-the-fourier-transform/)
(ICASSP 2016, DOI `10.1109/ICASSP.2016.7472603`), explicitly describes
arbitrarily slow Fourier-decay constructions. That general phenomenon is
not claimed as new, and no theorem from that paper is imported here.

The exact source kernel is the classical extremizer in
[Carneiro--Chandee--Littmann--Milinovich, Corollary 14](https://arxiv.org/pdf/1406.5462).
[Suto's compact-Fourier ground-state theory](https://arxiv.org/pdf/math-ph/0508004)
is neighboring positive pair-energy literature, with different
infinite-volume and fixed-density objectives. Neither is used as a
theorem about the modulus (7).

The local mathematical delta is the compatibility of slow-decay modulation
with **all** of the fixed-notch constraints, followed by the exact
four-site conversion into failure of every power rate relative to the
known sharp real envelope. Targeted searches in Fourier decay,
Montgomery--Taylor extremals and positive-type pair-potential stability did
not locate this exact finite-multiset statement. This is a line-specific
derived obstruction, not a claim of global literature novelty.
