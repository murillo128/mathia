# ANF-201 — Bounded-cardinality complex near-extremizers have the real notch envelope

**Status:** EXACT-DERIVED + CLASSICAL-POWER-SUM-INPUT + SPAN-INDEPENDENT-HEIGHT-BOUND + FINITE-CLUSTER-COMPACTNESS + SHARP-BOUNDED-CARDINALITY-ENVELOPE. At every fixed total-cardinality cap, complex Montgomery--Taylor near-extremizers have exactly the real two-site notch-exposure envelope. No height or horizontal-span restriction is assumed. The proof first bounds height by an averaged power-sum argument, then handles separated clusters and multiplicity collisions explicitly. Consequently any near-extremizing obstruction strictly above the real envelope must have cardinality tending to infinity. There is no uniform-in-cardinality modulus or unconditional zeta-zero improvement.

## Statement and normalization

Use the Fourier convention \(\widehat f(x)=\int f(u)e^{-2\pi iux}\,du\), and set
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\qquad J_0=g*g,\qquad
K=\widehat g,\qquad F=\widehat J_0=K^2.
\tag{1}
\]
For a nonempty finite conjugation-invariant multiset \(W\), counting
every entry with its positive integer multiplicity, write
\[
N=|W|,\quad L(W)=2N-\sigma(W),\quad
S_W(u)=\sum_{z\in W}e^{-2\pi iuz},\quad
E_f(W)=\int f(u)|S_W(u)|^2\,du,
\]
\[
e(W)=E_{J_0}(W)/L(W)-1,\qquad
H(W)=\max_{z\in W}|\Im z|.
\tag{2}
\]
Here \(\sigma\) counts distinct **simple real** sites. Lamzouri's
inequality gives \(e\ge0\). ANF-087 classifies equality: it consists of
one or two real sites, each of multiplicity one or two, with any
two-site separation a positive zero \(r_j\) of \(K\).

Freeze an integrable real even profile
\[
0\le\phi\le J_0,\qquad \Phi=\widehat\phi\ge0
\quad\hbox{on }\mathbb R,
\qquad h_\phi(W)=E_\phi(W)/L(W).
\tag{3}
\]
No inverse-square Fourier tail or Sobolev assumption is needed here.
Let
\[
M_\phi=\sup_{j\ge1}\Phi(r_j),\qquad
\beta_\phi^{\mathbb R}=\Phi(0)+M_\phi.
\tag{4}
\]
If \(M_\phi>0\), the supremum is attained because
\(\Phi(r_j)\to0\). If it is zero, every source zero attains it.
The right side is the real envelope identified in ANF-195.

For each fixed integer \(m\ge2\),
\[
\boxed{
\lim_{\varepsilon\downarrow0}
\sup_{\substack{W=\overline W,\ 1\le |W|\le m\\e(W)\le\varepsilon}}
h_\phi(W)=\beta_\phi^{\mathbb R}.
}
\tag{5}
\]
For \(m=1\) the envelope is \(\Phi(0)\). More precisely, any sequence
with bounded \(N\) and \(e(W_n)\to0\) has a subsequence partitioned
into finitely many conjugation-invariant physical clusters. After a
separate real translation of each cluster, it converges to an ANF-087
equality configuration. Distinct clusters separate horizontally,
both energies decouple, and the affine denominators converge without
loss. In particular,
\[
\boxed{\sup_n|W_n|<\infty,\quad e(W_n)\to0
\quad\Longrightarrow\quad H(W_n)\to0.}
\tag{6}
\]

## A source-energy bound on height, independent of horizontal span

Let \(\mathfrak h_N=\sum_{k=1}^N1/k\) and
\(j_*:=\tfrac14\cot^2(1/\sqrt2)>0\). As in ANF-106,
\(J_0(u)\ge j_*\) for \(|u|\le1/2\): on its support
\(g\ge\cot(1/\sqrt2)/\sqrt2\), and the convolution overlap there
has length at least \(1/2\). Put \(E=E_{J_0}(W)\). Then
\[
\boxed{
H(W)\le\frac{2N}{\pi}
\log\left[2\left(1+\sqrt{\frac{4N\mathfrak h_NE}{j_*}}\right)\right].
}
\tag{7}
\]
In particular, \(E\le2N(1+\varepsilon)\) gives
\(H(W)=O_\varepsilon(N\log(2+N))\), with no condition on horizontal
positions or minimum separation. This is a sufficient bound, not a
sharp height law.

To prove it, choose a single grid spacing from
\(I_N=[1/(4N),1/(2N)]\). Changing variables separately in each term,
\[
\int_{I_N}\sum_{k=1}^N|S_W(kd)|^2\,dd
=\sum_{k=1}^N\frac1k\int_{k/(4N)}^{k/(2N)}|S_W(u)|^2\,du
\le\frac{\mathfrak h_NE}{j_*}.
\tag{8}
\]
All intervals lie in \([0,1/2]\). Since \(|I_N|=1/(4N)\), some
\(d\in I_N\) satisfies
\[
|S_W(kd)|\le P:=\sqrt{4N\mathfrak h_NE/j_*}
\qquad(1\le k\le N).
\tag{9}
\]
The same \(d\) works for every \(k\); choosing separate good samples
would not produce the following power sums.

List all entries as \(z_1,\ldots,z_N\), including repetitions, and set
\(w_j=e^{-2\pi idz_j}\). Then
\(p_k:=\sum_jw_j^k=S_W(kd)\). Write
\[
\prod_{j=1}^N(X-w_j)=\sum_{k=0}^Na_kX^{N-k},\qquad a_0=1.
\]
Newton's identities give
\[
ka_k=-\sum_{j=1}^kp_ja_{k-j}.
\tag{10}
\]
With \(A=1+P\), induction gives \(|a_k|\le A^k\): indeed
\[
k|a_k|\le P\sum_{j=1}^k A^{k-j}
\le kP A^{k-1}\le kA^k.
\]
Every root has modulus at most \(2A\). Otherwise the monic leading
term would exceed the sum of the remaining terms, since
\(\sum_{k=1}^N(A/|X|)^k<1\). Conjugation invariance guarantees an
entry of imaginary part \(H(W)\), so
\[
e^{2\pi dH(W)}=\max_j|w_j|\le2(1+P).
\]
Using \(d\ge1/(4N)\) proves (7).

The power-sum step is classical equal-weight exponential-sum algebra.
Its useful feature here is that multiplicities are integer repetitions,
so no inverse Vandermonde matrix or separation constant is needed.
It would not apply unchanged to arbitrary signed or vanishing weights.

## Cluster extraction and the collision bookkeeping

Consider \(N_n\le m\) and \(e(W_n)\to0\). Pass to a subsequence
with fixed total cardinality \(N\), fixed equality pattern of the
labels, fixed real/nonreal types, and a fixed conjugation permutation.
There are only finitely many such patterns. Equation (7) bounds all
heights uniformly because \(E_{J_0}(W_n)\le2m(1+o(1))\).

For each pair of labels, pass to a further subsequence on which its
real-part difference either converges to a finite value or diverges in
absolute value. The relation of bounded real-part difference partitions
the labels into finitely many clusters \(W_{n,a}\). It is an
equivalence relation by the triangle inequality. Conjugate labels have
identical real parts, and hence belong to the same cluster. Real-site
multiplicities are never split between clusters.

Translate each cluster by the real part of one of its labels. Its real
parts and heights are now bounded; a further subsequence converges
label by label to a nonempty finite conjugation-invariant multiset
\(V_a\). Different clusters have diverging horizontal separation.

For \(f=J_0\) or \(f=\phi\), extend the Fourier transform to complex
arguments. Compact support and integrability give
\[
\sup_{|y|\le2H_0}|\widehat f(x+iy)|\longrightarrow0
\qquad(|x|\to\infty)
\tag{11}
\]
for every fixed \(H_0\). For completeness, the map
\(y\mapsto f(u)e^{2\pi uy}\) is continuous into \(L^1([-1,1])\).
Its image on a compact \(y\)-interval is compact. Approximate that
image by a finite \(L^1\) net and apply the ordinary Riemann--Lebesgue
lemma at the net points; the Fourier transform has operator norm at
most one from \(L^1\) to the supremum norm. This proves (11), including
profiles with no prescribed decay rate.

The identity
\(E_f(W)=\sum_{z,w\in W}\widehat f(z-\bar w)\), the fixed finite
number of pairs, and (11) give
\[
E_f(W_n)\longrightarrow\sum_a E_f(V_a).
\tag{12}
\]
Internal energies converge by dominated convergence. This is absolute
decoupling at bounded cardinality, not a uniform statement for growing
numbers of clusters.

The denominator requires a separate argument. Let
\(L_a=L(W_{n,a})\), constant along the chosen subsequence. Whole-site
partitioning gives \(L(W_n)=\sum_aL_a=:L_*\). A simple real site in
\(V_a\) must descend from exactly one prelimit label. That label must
already have been real and simple: a nonreal label has a distinct
conjugate partner in the same cluster, which collides with it if its
height tends to zero. Thus
\[
\sigma(V_a)\le\sigma(W_{n,a}),\qquad L(V_a)\ge L_a.
\tag{13}
\]
Since \(e(W_n)\to0\), (12), Lamzouri's inequality on every \(V_a\),
and (13) imply
\[
L_* =\sum_a E_{J_0}(V_a)
\ge\sum_aL(V_a)\ge\sum_aL_a=L_*.
\tag{14}
\]
Every nonnegative difference in (14) vanishes. Each \(V_a\) is an
exact equality configuration and \(L(V_a)=L_a\). ANF-087 therefore
makes every limit cluster real with at most two distinct sites, each
of multiplicity one or two. This proves the subsequential assertion.
Applying it to any subsequence with heights bounded away from zero
proves (6) for the original sequence.

This argument explicitly permits a nonreal conjugate pair to collapse
to a double real site. It excludes a collision which loses a simple
real site, because that would make (13) strict. For example
\(\{\pm i/n\}\) has \(L=4\) before and after its double-site limit
and is near-extremal; \(\{\pm1/n\}\) has \(L=2\) before the limit
and energy tending to four, so is not near-extremal. Treating \(L\)
as an automatically continuous function would miss this distinction.

## Exact exposure and the growing-cardinality obstruction

For a limit equality cluster with one site,
\(h_\phi=\Phi(0)\). For two sites of multiplicities
\(a,b\in\{1,2\}\) at separation \(r_j\),
\[
h_\phi(V)=\Phi(0)+\frac{2ab}{a^2+b^2}\Phi(r_j)
\le\Phi(0)+M_\phi.
\tag{15}
\]
Here Fourier nonnegativity and \(2ab\le a^2+b^2\) are both used.
Equations (12)--(14) show that every subsequential exposure limit is
the denominator-weighted average
\[
\lim_n h_\phi(W_n)
=\frac{\sum_a L(V_a)h_\phi(V_a)}{\sum_aL(V_a)}
\le\beta_\phi^{\mathbb R}.
\tag{16}
\]
If the upper bound in (5) failed, choose configurations with excess
tending to zero and exposure uniformly above it, and apply this
subsequence argument. For the lower bound, a simple pair at an active
root has \(e=0\) and exposure \(\Phi(0)+M_\phi\). This proves (5),
including the case \(M_\phi=0\).

In particular,
\[
e(W_n)\to0,\qquad
\liminf_n h_\phi(W_n)>\beta_\phi^{\mathbb R}
\quad\Longrightarrow\quad |W_n|\to\infty.
\tag{17}
\]
The conclusion is divergence, not merely an unbounded subsequence:
any infinite bounded-cardinality subsequence would contradict (5).

For the fixed triangular notch of ANF-099, let
\(B_\eta=C(\phi_\eta)/C(J_0)\). If
\(\beta_\eta^{\mathbb R}<B_\eta\), then for every fixed \(m\)
there is \(t_m>0\) such that
\[
\inf_{\substack{W=\overline W\\1\le |W|\le m}}
\{1+e(W)-t h_\eta(W)\}>1-tB_\eta
\qquad(0<t\le t_m).
\tag{18}
\]
Indeed (5) supplies \(\varepsilon>0\) and \(a<B_\eta\) with
\(h_\eta\le a\) whenever \(e\le\varepsilon\) in this class.
For these configurations the objective is at least \(1-ta\).
For the rest, \(h_\eta\le1+e\) gives a lower bound
\((1-t)(1+\varepsilon)\ge1\) when
\(t\le\varepsilon/(1+\varepsilon)\). Taking a smaller \(t_m<1\)
also keeps \(1-tB_\eta>0\). This is the same elementary envelope
split as ANF-099, now with its exact bounded-cardinality slope.

Thus finite complex configurations of any prescribed size cannot
defeat all sufficiently small amplitudes along a real-improving fixed
notch ray. The amplitude is allowed to shrink with the cardinality cap.
Equations (17)--(18) do not interchange those two quantifiers.

## Prior art, audit and evidence boundary

Newton's identities and polynomial root bounds are classical; see
[Brent, section 1.4](https://arxiv.org/pdf/1004.5466).
Equal-weight exponential samples as power sums, and control of their
exponents through those sums, are explicitly studied in
[Chunaev, sections 2 and 4.1](https://arxiv.org/pdf/1906.01332),
*Interpolation by generalized exponential sums with equal weights*,
*Journal of Approximation Theory* 254 (2020), 105397,
DOI `10.1016/j.jat.2020.105397`. These are close prior art for the
algebraic mechanism; no novelty is claimed for parameter control from
consecutive samples. Equations (8)--(10) give the entire elementary
bound needed here directly, without importing an interpolation
existence or numerical-stability assertion.

The source inequality was checked against
[Lamzouri, Proposition 2.1, v2](https://arxiv.org/html/2609.02882v2#S2),
and its equality specialization is reconstructed in ANF-087.
Finite cluster extraction is a classical compactness/profile-splitting
argument, related to the Lions boundary already recorded for ANF-106.
No general concentration--compactness theorem is used. The local
mathematical delta is the span-independent height confinement (7)
followed by the collision-safe equality argument (13)--(16): together
they close the **entire bounded-cardinality complex** envelope,
whereas ANF-195 closes the **entire real** envelope and ANF-106 allows
cardinality to grow as the desired localization error shrinks.
Targeted searches in power-sum, equal-weight Prony and exponential-sum
compactness literature did not identify this Montgomery--Taylor
exposure conclusion. This is a derived specialization, not a claim of
a new general compactness or power-sum theorem.

The decisive checks are the common grid in (9), the inclusion of all
integer repetitions in the degree \(N\), the use of conjugation to
bound both signs of height, uniform Fourier decay only after height
is bounded, and the direction of the simple-site inequality (13).
Horizontal aliasing of the sampled \(w_j\) is harmless: repeated
polynomial roots are allowed, and only their moduli are used. Large
horizontal translations remain free; cluster extraction removes them
without asserting global compactness modulo one translation.

No numerical optimization, Lean validation, uniform stability rate,
or finite-height verification is used as proof. The unrestricted
ANF-099 clue remains open: the height bound grows with cardinality,
and neither (7) nor (18) controls the limit \(m\to\infty\).
No all-configuration affine certificate, improved critical-line
proportion, zero-density estimate, or RH conclusion follows.
