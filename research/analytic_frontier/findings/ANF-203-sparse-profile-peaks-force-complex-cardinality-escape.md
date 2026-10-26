# ANF-203 — Sparse profile peaks force complex cardinality escape

**Status:** EXACT-DERIVED + COMPLEX-MULTISET + FIXED-PROFILE + NONATTAINMENT + ATTAINED-CAPPED-MINIMA. The single positive-Fourier profile constructed in ANF-200, belonging to every Sobolev space below order two, has no minimizing finite conjugation-invariant complex multiset at any positive amplitude below one. Every finite configuration is strictly improved by a sufficiently distant translated copy. Nevertheless, at every fixed cardinality cap the minimum exists. Hence every sequence approaching the unrestricted floor has cardinality tending to infinity. This extends the real nonattainment example; it does not classify general complex attainment, settle the triangular-notch envelope, or give a zeta-zero consequence.

## Fixed profile and precise conclusions

Use \(\widehat f(x)=\int f(u)e^{-2\pi iux}\,du\), and set
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\qquad J_0=g*g,\qquad F=\widehat J_0=K^2,
\]
\[
K(z)=\frac{\cos(\pi z)-a z\sin(\pi z)}{1-2\pi^2z^2},
\qquad a=\sqrt2\pi\cot(1/\sqrt2),
\tag{1}
\]
with the removable points continued. For a nonempty finite multiset
\(W=\overline W\), all entries counted with positive integer multiplicity,
write
\[
N=|W|,\quad L(W)=2N-\sigma(W),\quad
S_W(u)=\sum_{z\in W}e^{-2\pi iuz},\quad
E_f(W)=\int f(u)|S_W(u)|^2\,du.
\tag{2}
\]
Here \(\sigma\) counts distinct simple real sites only. Lamzouri's
inequality gives \(E_{J_0}(W)\ge L(W)>0\).

Freeze the ANF-200 profile, as follows. If \(r_1\) is the first positive
zero of \(K\), choose \(0<\eta<1/(2r_1)\) and \(b>0\) small enough that
\[
\chi=\mathbf1_{[-\eta/4,\eta/4]},\qquad
\tau=b\chi^{*4}\le J_0,\qquad
T(z)=\widehat\tau(z)=b(\eta/2)^4\operatorname{sinc}^4(\eta z/2).
\tag{3}
\]
The sinc convention is \(\operatorname{sinc}(z)=\sin(\pi z)/(\pi z)\).
For a fixed \(0<\lambda<1\), put
\[
R_n=2^{n^2},\quad Z=\sum_{n\ge1}\frac n{R_n^2},\quad
w_n=\frac n{ZR_n^2},
\]
\[
\phi_*(u)=\frac{\tau(u)}{1+\lambda}
\left[1+\lambda\sum_{n\ge1}w_n\cos(2\pi R_nu)\right].
\tag{4}
\]
All these parameters, frequencies and weights are fixed before choosing
an amplitude or a configuration. As established directly in ANF-200,
\[
0\le\phi_*\le\tau\le J_0,\qquad
\widehat\phi_*\ge0,\qquad
\phi_*\in\bigcap_{s<2}H^s(\mathbb R),\qquad \phi_*\notin H^2(\mathbb R).
\tag{5}
\]

For \(0<t<1\), define
\[
Q_t(W)=\frac{E_{J_0-t\phi_*}(W)}{L(W)},\qquad
q_m(t)=\inf_{\substack{W=\overline W\\1\le|W|\le m}}Q_t(W),\qquad
q_\infty(t)=\inf_{W=\overline W,\ 0<|W|<\infty}Q_t(W).
\tag{6}
\]
The conclusions are:

1. Every fixed \(W\) is strictly improved by \(W\cup(W+R_n)\) for
   all sufficiently large \(n\), with the precise asymptotic
   \[
   \boxed{
   \lim_{n\to\infty}\frac{R_n^2}{n}
   \bigl[Q_t(W\cup(W+R_n))-Q_t(W)\bigr]
   =-\frac{t\lambda E_\tau(W)}{2(1+\lambda)ZL(W)}<0.
   }
   \tag{7}
   \]
2. For every integer \(m\ge1\), \(q_m(t)\) is attained and
   \[
   \boxed{1-t\le q_\infty(t)<q_{2m}(t)<q_m(t).}
   \tag{8}
   \]
3. If \(Q_t(W_j)\to q_\infty(t)\) at this fixed amplitude, then
   \(|W_j|\to\infty\).

The threshold in (7) depends on \(W\) and \(t\). No uniform rate for
the gaps in (8), nor strict decrease at each single increment of \(m\),
is asserted.

## Keep the entire source before taking a Fourier sign

For a fixed complex configuration, introduce the real-axis transforms
\[
A_W(x)=\widehat{J_0|S_W|^2}(x),\qquad
G_W(x)=\widehat{\tau|S_W|^2}(x),\qquad
B_W(x)=\widehat{\phi_*|S_W|^2}(x).
\tag{9}
\]
Conjugation invariance implies \(S_W(-u)=\overline{S_W(u)}\), so these
transforms are real and even. They need not be nonnegative away from
zero. In particular, real-axis nonnegativity of \(\widehat\phi_*\)
does not justify discarding terms evaluated at complex arguments.

The finite-sum identities are instead
\[
A_W(x)=\sum_{z,w\in W}F(x+z-\bar w),\qquad
G_W(x)=\sum_{z,w\in W}T(x+z-\bar w).
\tag{10}
\]
For each fixed \(W\), the explicit formulas (1) and (3) give
\[
|A_W(x)|\le\frac{C_W}{1+x^2},\qquad
|G_W(x)|\le\frac{D_W}{(1+x^2)^2}\qquad(x\in\mathbb R)
\tag{11}
\]
for finite constants. Indeed, each imaginary shift is fixed, so sine
and cosine are bounded on that horizontal line. The numerator of
\(K\) is \(O_W(1+|x|)\), its denominator has quadratic growth, and
the fourth power in \(T\) gives fourth-order decay. Continuity absorbs
the remaining compact interval and the removable points. Neither
constant is asserted uniform in cardinality, span or height.

The crucial positive value is the energy at zero translation
\[
G_W(0)=E_\tau(W)>0.
\tag{12}
\]
The spline \(\tau\) is positive near zero and \(S_W(0)=N>0\), so
continuity proves strictness even when the individual complex terms in
(10) have different signs.

Uniform convergence of the cosine series and integrability of
\(\tau|S_W|^2\) justify the modulation identity
\[
B_W(x)=\frac1{1+\lambda}
\left[G_W(x)+\frac\lambda2\sum_{k\ge1}w_k
\{G_W(x-R_k)+G_W(x+R_k)\}\right].
\tag{13}
\]
At \(x=R_n\), isolate \(w_nG_W(0)\). For \(k<n\) and \(n\ge2\),
\(R_n-R_k\ge R_n/2\); for \(k>n\), \(R_k-R_n\ge R_k/2\).
Using (11) and \(\sum_kw_k=1\), all earlier terms together are
\(O_W(R_n^{-4})\), and all later terms together are
\(O_W(R_{n+1}^{-4})\). The unmodulated term, all plus-shifts and
the self plus-shift have the same or smaller bound. Therefore
\[
\boxed{
B_W(R_n)=\frac{\lambda E_\tau(W)}{2(1+\lambda)}w_n
          +O_W(R_n^{-4}).
}
\tag{14}
\]
This estimate bounds every other term in absolute value. It does not
import real-pair Fourier positivity into the complex configuration.
It is also stronger than merely finding a positive subsequence after
seeing \(W\): the entire frequency sequence in (4) was fixed in advance.

## The translated-copy test and the strict sign

For any real \(R\) greater than the horizontal diameter of \(W\), the
two copies have disjoint real projections. Their site multiplicities
and real/nonreal types are unchanged, whence
\[
L(W\cup(W+R))=2L(W),\qquad
S_{W\cup(W+R)}(u)=(1+e^{-2\pi iuR})S_W(u).
\]
Consequently
\[
Q_t(W\cup(W+R))-Q_t(W)
=\frac{A_W(R)-tB_W(R)}{L(W)}.
\tag{15}
\]
There is no missing factor two: both the self-energy and the affine
denominator double, while the two cross terms contribute
\(2[A_W(R)-tB_W(R)]\).

By (11), (14) and \(R_n^2w_n=n/Z\),
\[
\frac{R_n^2}{n}\{A_W(R_n)-tB_W(R_n)\}
\longrightarrow-\frac{t\lambda E_\tau(W)}{2(1+\lambda)Z}.
\tag{16}
\]
This proves (7) for arbitrary finite conjugation-invariant \(W\),
including repeated nonreal pairs, coincident orbit centers and real
multiple sites. The new configuration remains finite and
conjugation-invariant. Thus no finite configuration attains
\(q_\infty(t)\). At the same time,
\[
J_0-t\phi_*\ge(1-t)J_0
\quad\Longrightarrow\quad Q_t(W)\ge1-t>0.
\tag{17}
\]
The failure is nonattainment, not an energy unbounded below.

## Every fixed cardinality cap still has a minimizer

The following existence argument applies more generally to every
integrable real even \(0\le\phi\le J_0\) and every fixed \(0<t<1\),
with \(Q_t=E_{J_0-t\phi}/L\). Fourier nonnegativity of \(\phi\)
is not needed.

Take a minimizing sequence \(W_j\), \(|W_j|\le m\). A real singleton
gives a value at most one, and (17) gives a positive lower bound, so
\[
E_{J_0}(W_j)\le\frac{L(W_j)Q_t(W_j)}{1-t}
\le\frac{2m(1+o(1))}{1-t}.
\tag{18}
\]
ANF-201, equation (7), bounds the maximum imaginary height using only
\(|W_j|\) and this source energy, independently of horizontal span.
Its proof does not require the excess to tend to zero.

Use the finite-label cluster extraction in ANF-201, equations
(11)--(13). After a subsequence the cardinality, multiplicity/type
pattern and denominator \(L_*\) are constant. Partition into clusters
of bounded real-part differences. Each is conjugation-invariant and,
after its own real translation, converges to a nonempty multiset
\(V_a\) with \(|V_a|\le m\). Distinct clusters separate horizontally.
The transforms of \(J_0\) and \(\phi\) vanish uniformly at horizontal
infinity on the fixed vertical strip, so the energies decouple:
\[
\lim_jE_{J_0-t\phi}(W_j)=\sum_aE_{J_0-t\phi}(V_a).
\tag{19}
\]
For clarity, the uniform Fourier decay follows by approximating the
compact family \(u\mapsto f(u)e^{2\pi uy}\), \(|y|\le2H\), by a
finite net in \(L^1\), then applying Riemann--Lebesgue to that net.
This needs no rate for the transform of \(\phi\).

Let \(L_a\) be the prelimit denominator of cluster \(a\). Collisions
can remove simple real sites but cannot create one from multiple
prelimit labels: a nonreal label that becomes real brings its conjugate
with it. Therefore
\[
L(V_a)\ge L_a,\qquad\sum_aL_a=L_*.
\tag{20}
\]
The capped infimum \(q_m\ge1-t>0\) applies to every \(V_a\). Thus
\[
q_mL_*=
\sum_aE_{J_0-t\phi}(V_a)
\ge q_m\sum_aL(V_a)
\ge q_m L_*.
\tag{21}
\]
All inequalities are equalities. Each \(V_a\) attains \(q_m\), and
no denominator is lost. This proves existence without assuming that
the whole configuration stays compact modulo one translation or that
\(L\) is continuous through arbitrary collisions.

Apply this existence result to (4). A minimizing \(W\) for \(q_m(t)\)
has a strictly better doubled competitor of size at most \(2m\), by
(7); hence \(q_{2m}(t)<q_m(t)\). The attained value \(q_{2m}(t)\)
cannot equal the unattained global floor, proving (8). An infinite
subsequence with bounded cardinality could not approach
\(q_\infty(t)\), because its values would stay above one of these
strict capped floors. This proves cardinality divergence.

## Regularity, prior art and the remaining boundary

For completeness, the regularity in (5) uses only the existing
construction. The spline transform \(T\) is nonnegative and decays
as \(O((1+|x|)^{-4})\). Modulation translates it, giving
\[
\widehat\phi_*(x)=\frac1{1+\lambda}
\left[T(x)+\frac\lambda2\sum_nw_n\{T(x-R_n)+T(x+R_n)\}\right]\ge0.
\]
The weighted translation estimate for \(H^s\), followed by
\(\sum_n w_nR_n^s=Z^{-1}\sum_n n2^{-(2-s)n^2}<\infty\), proves
membership for every \(0\le s<2\); negative orders follow from
\(L^2\). On a fixed small interval about each \(R_n\), positivity
gives \(\widehat\phi_*\ge c w_n\). The \(H^2\) integral therefore
dominates a constant times \(\sum_nR_n^4w_n^2=\infty\).

The source inequality is
[Lamzouri, Proposition 2.1](https://arxiv.org/html/2609.02882v2#S2).
The source kernel and profile are already explicit in ANF-200; the
height estimate and collision-safe extraction are ANF-201. These
are the only non-elementary/source-specific inputs. The classical
stability-constant setting in
[Procacci, equation (1.3)](https://arxiv.org/pdf/2005.10362) does not
assert finite attainment. The fixed-density infinite-volume ground
states in [Sütő](https://arxiv.org/pdf/math-ph/0508004) concern a
different optimization problem. Translation, dichotomy and selection
of a surviving cluster are classical concentration-compactness ideas;
the finite argument (18)--(21) supplies the exact multiplicity and
positive-denominator bookkeeping here.

Slow Fourier decay and modulation are classical; compare
[Boche--Tampubolon, ICASSP 2016](https://mediatum.ub.tum.de/doc/1311435/1311435.pdf).
That paper supplies a prior-art boundary, not a theorem about these
multisets. The profile, its subcritical Sobolev regularity and its real
nonattainment were already established in ANF-200. The new conclusion
is the complex nonattainment and compulsory cardinality escape:
(14) replaces real-pair termwise positivity by the strictly positive
whole-source energy \(E_\tau(W)\), and (21) excludes escape at fixed
cardinality. Targeted searches in finite stability constants,
compactly supported positive Fourier profiles and Montgomery--Taylor
complex stability did not identify this specialization; no claim of a
new general Fourier or concentration-compactness theorem is made.

The sharp audit points are the conjugate \(\bar w\) in (10), the
absolute bounds on all off-peak terms in (14), preservation of \(L\)
for disjoint copies, and the direction of (20). The constants in (11)
can grow with geometry; the fixed-profile quantifier does not make the
translation threshold uniform over configurations. No numerical
optimization or Lean proof is used to establish the assertions.

This result does not extend ANF-200's necessary-and-sufficient real
Fourier-tail classification to all complex profiles. In particular,
no complex finite-attainment sufficiency is asserted for \(H^2\).
The ordinary triangular notch has an inverse-square tail and is not
the profile (4). ANF-202's exact real reduction at each fixed cap and
sufficiently small amplitude is compatible with strict descent when
that cap is enlarged. Neither (7) nor (8) compares the unrestricted
complex floor with its real restriction or evaluates its derivative
at zero. The accepted ANF-099 exposure question remains open; there
is no new critical-zero proportion, zero-density bound or RH conclusion.
