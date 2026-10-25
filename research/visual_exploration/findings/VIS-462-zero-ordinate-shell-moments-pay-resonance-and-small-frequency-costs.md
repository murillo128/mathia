# VIS-462 — zero-ordinate shell moments pay resonance and small-frequency costs

**Evidence/status:** LITERATURE+EXACT-DERIVED + QUANTITATIVE CONTROL + CLASSICAL-SPECIALIZATION + NO-NOVELTY-CLAIM + NON-RH.

## Claim

Count all nontrivial zeta zeros with multiplicity, regardless of real
part. Put
\[
L=\log T,\quad D_T=N(2T)-N(T),\qquad
Z_T(\nu)=D_T^{-1}\sum_{T<\gamma\le2T}e^{-i\nu\gamma}.
\]
Uniformly for \(0<|\nu|\le L/8\),
\[
|Z_T(\nu)|\ll {1\over L}+{\nu^2\over L^2}
       +{e^{|\nu|/2}L\over T}+{1\over T|\nu|}.                 \tag{1}
\]
The constant is absolute for sufficiently large \(T\). This is the
Landau/zero-density argument underlying the current
[WI-461](../../weil_inertia/findings/WI-461-fixed-scale-euler-peaks-have-positive-density-at-zeta-zero-ordinates.md),
with frequency size and small-frequency separation kept as separate
resources instead of combined into its single parameter \(B\).

Let \(F_T=\sum_a b_{T,a}z^a\ne0\) be a finite prime-torus Laurent
polynomial, frozen throughout the dyadic sampling block. The polynomial,
its prime set and coefficients may depend on \(T\). Define
\[
S_T=\|F_T\|_\infty,\quad W_T={\sum_a|b_{T,a}|\over S_T},\quad
\lambda_a=\sum_p a_p\log p,\quad \max_a|\lambda_a|\le\Omega_*<\infty.
\]
For fixed integer mixed squared-amplitude degree \(R\ge1\), let \(\delta_{T,R}^*\)
be the least nonzero magnitude of
\(\sum_{j=1}^R(\lambda_{a_j}-\lambda_{c_j})\), with value infinity
when this set has no nonzero member. Every fixed collection of offsets
\(u_j\) and nonnegative integer powers \(r_j\), \(\sum r_j=R\), obeys
\[
\left|\mathbb E_{\gamma}
  \prod_j { |F_T(z(\gamma)\tau(u_j))|^{2r_j}\over S_T^{2r_j}}
 -\int\prod_j { |F_T(z\tau(u_j))|^{2r_j}\over S_T^{2r_j}}\,dm_H(z)\right|
\ll_{R,\Omega_*}W_T^{2R}
  \left({1\over L}+{L\over T}+{1\over T\delta_{T,R}^*}\right). \tag{2}
\]
Here \(z(t)=\tau(t)=(p^{-it})_p\), and \(m_H\) is product Haar
probability on the actual base-prime coordinates. If all characters
are constant, the error is exactly zero.

For the strict near-band Wang shells of
[VIS-313](VIS-313-wang-dyadic-ratio-shell-linear-horizon.md), at arithmetic
height \(Y_T\), every mode is \(\log(q/r)\) for prime powers
\(q,r\le2Y_T\) with \(0<|\log(q/r)|<\log2\). Thus (2) gives
\[
\boxed{\quad W_T^{2R}
   \left({1\over\log T}+{\log T\over T}
                    +{(2Y_T)^{2R}\over T}\right)\longrightarrow0\quad}  \tag{3}
\]
as a sufficient condition for degree \(R\) moment calibration at
**actual zero ordinates**. If (3) holds for every fixed \(R\), it also
calibrates every fixed continuous test of the normalized amplitude and
of its supremum over a fixed offset radius. Threshold frequencies
additionally require uniform vanishing Haar boundary mass.

The coefficient check is not empty: every such nonzero shell satisfies
\(W_T\le2Y_T\). Therefore **all** these shells with
\[
\log Y_T=o(\log\log T)                                      \tag{4}
\]
satisfy (3) at every fixed order, irrespective of the source coefficient
parameters. This includes dyadic \(Y_T\asymp\log\log T\). It is a
growing-shell result, not an interchange of two qualitative limits.

## Unconditional character formula, with the resonance retained

For \(\nu>0\), set \(x=e^\nu\), let \(n_x\) be a nearest prime
power to \(x\), and put \(d=\log(x/n_x)\). Define the continuous
box transform
\[
K(u)=\int_1^2e^{-ius}\,ds
     =e^{-3iu/2}{\sin(u/2)\over u/2},\qquad K(0)=1.
\]
The more informative form of (1) is
\[
Z_T(\nu)=-{T\Lambda(n_x)\over2\pi\sqrt x\,D_T}K(Td)
 +O\left({\nu^2\over L^2}+{e^{\nu/2}L\over T}
                              +{1\over T\nu}\right).         \tag{5}
\]
Negative frequencies follow by conjugation. Ties for nearest prime
power may be resolved either way; the stated error remains valid.

Ford–Zaharescu, Lemma 1, gives the uniform Landau formula for
\(\sum_{0<\gamma\le U}x^\rho\), with main term
\(-\Lambda(n_x)(e^{iUd}-1)/(2\pi i d)\) and error
\(O(x\log^2(2xU)+\log(2U)/\log x)\). Subtract at \(2T,T\),
divide by \(\sqrt x D_T\), and conjugate. Since
\(D_T\asymp T\log T\), its errors are the last two terms of (5).
This step alone does **not** replace \(x^{\rho-1/2}\) by the
unweighted phase \(x^{i\gamma}\).

For that replacement pair each zero \(\beta+i\gamma\) with
\(1-\beta+i\gamma\), preserving multiplicity. If
\(v=\beta-1/2>0\), the pair's difference has modulus at most
\(2(\cosh(\nu v)-1)\). Selberg's density estimate, as stated in
Ford–Zaharescu Lemma 2, gives, with \(N_+(v,U)\) counting zeros
\(0<\gamma\le U\), \(\beta>1/2+v\), with multiplicity,
\[
N_+(v,U)\ll U\log U\,e^{-v\log U/4}.
\]
Layer-cake integration and \(\sinh w\le we^w\) imply, for
\(\nu\le\log U/8\),
\[
\left|\sum_{0<\gamma\le U}
       (x^{i\gamma}-x^{\rho-1/2})\right|
\le2\int_0^{1/2}\nu\sinh(\nu v)N_+(v,U)\,dv
\ll {U\nu^2\over\log U}.                                  \tag{6}
\]
The same formula works arbitrarily near \(\nu=0\); no
frequency-dependent constant has been suppressed. Subtracting the
two cumulative sums and normalizing yields (5)'s first error term.
Critical-line zeros contribute zero to (6); no RH assumption is used.

Finally \(|K(u)|\le\min(1,2/|u|)\), and
\(\Lambda(n_x)/\sqrt x\) is absolutely bounded: a power of two
lies in \([x,2x]\), hence \(n_x\le2x\), and
\(\Lambda(n_x)\le\log(2x)\). Bounding the main term proves (1).
Formula (5), rather than its absolute bound, retains the sign, width
and distance-to-resonance dependence of the classical bias.

For example, on the clue's entire reduced rational bank
\(1\le A,B\le(\log T)^c\), \(A\ne B\), fixed \(c>0\),
\[
|\log(A/B)|\ge(\log T)^{-c},\qquad
|\log(A/B)|\le c\log\log T.
\]
Equation (1) gives \(\sup |Z_T(\log(A/B))|=O_c(1/\log T)\).
This allows exact prime-power resonances; it does not assume the
ratios avoid them.

## Transfer to the actual finite shell and its paths

An offset only multiplies \(b_{T,a}\) by \(e^{-iu\lambda_a}\).
The Wiener norm of the mixed monomial in (2) is at most \(W_T^{2R}\).
Its nonconstant frequencies have magnitudes between
\(\delta_{T,R}^*\) and \(2R\Omega_*\). The character expansion,
(1), and the triangle inequality prove (2). Unique factorization
identifies zero frequency with the constant torus character; distinct
base-prime modes must not be replaced by independent ratio phases.

For Wang modes, a mixed frequency is \(\log(A/B)\), where each
of \(A,B\) is a product of \(2R\) prime powers at most \(2Y_T\).
If it is nonzero,
\[
|\log(A/B)|\ge1/\max(A,B)\ge(2Y_T)^{-2R}.
\]
This is the structural divisor before any coefficient cancellation,
so it remains valid for every offset. It proves (3).

Write \(K_T\) for the number of surviving distinct characters.
Orthogonality and Cauchy–Schwarz give
\[
S_T\ge\|F_T\|_{L^2(m_H)}=\left(\sum_a|b_{T,a}|^2\right)^{1/2},
\qquad W_T\le\sqrt{K_T}\le2Y_T.                             \tag{7}
\]
The last inequality just counts ordered integer pairs \(q,r\le2Y_T\).
It holds for the actual coefficients
\[
b_{q,r}=a_q a_r\int_0^H e^{-iu\log(q/r)}du,\qquad
a_q={\Lambda(q)\over\sqrt q}\min(q/x,x/q),\quad x,H>0,
\]
including arbitrary cancellations and small nonzero shell norms.
Under (4), the three terms in (3), using (7), are respectively at most
\(L^{-1+o(1)}\), \(L^{1+o(1)}/T\), and \(L^{o(1)}/T\).

There is also a concrete larger-height example with the same coefficient
formula. Set \(H=1\), \(x=Y_T\), and choose dyadic
\(Y_T\asymp\exp(\sqrt{\log T})\). In the strict band,
\[
b_{q,r}=a_q a_r e^{-i\lambda/2}{\sin(\lambda/2)\over\lambda/2}.
\]
All sinc factors are positive. At the torus phase \(\tau(-1/2)\)
every coefficient aligns, so \(S_T=\sum|b_{q,r}|\), \(W_T=1\),
and (3) holds for every fixed \(R\). Large dyadic intervals contain
several primes, so these shells are nonzero and have growing support.
This demonstrates an admissible coefficient family; \(H=1\) is
**not** the active Wang scale \(H\asymp x\log\log x\). No transfer
to an unstated physical relation between \(x,H,Y_T,T\) is inferred.

For the path passage, Bernstein's inequality gives
\(u\mapsto |F_T(z\tau(u))|/S_T\) Lipschitz constant at most
\(\Omega_*\), uniformly in \(z,T\). For a fixed radius and fixed
accuracy choose a mesh independent of \(T\). Mixed moment convergence
at every fixed degree plus polynomial approximation on that fixed cube
gives every fixed continuous mesh test. Uniform Lipschitz approximation
then removes the mesh. This reconstructs the
[VIS-425](VIS-425-fixed-radius-wang-persistence-moment-tariff.md)
argument with the zero-ordinate estimate replacing its Gram estimate.
For a threshold \(t\), require
\(\lim_{\eta\downarrow0}\limsup_{T\to\infty}
m_H\{|Q_{T,\rho}-t|\le\eta\}=0\), where
\(Q_{T,\rho}=\sup_{|u|\le\rho}|F_T(z\tau(u))|/S_T\).

## Two distinct boundary layers

The small-frequency cost cannot simply be omitted. The classical
zero-counting asymptotic implies that the empirical law of
\(\gamma/T\), for \(T<\gamma\le2T\), tends to uniform measure
on \([1,2]\). Hence, for each fixed real \(u\),
\[
Z_T(u/T)\longrightarrow K(u).                               \tag{8}
\]
For example \(K(1)\ne0\). A frequency shrinking at order \(1/T\)
can genuinely fail to cancel, although every fixed nonzero frequency
does cancel. This control does not assert that a given shell contains
such a character.

At a fixed prime power \(n\), (5) instead gives
\[
(\log T)Z_T(\log n+u/T)
\longrightarrow-{\Lambda(n)\over\sqrt n}K(u).                \tag{9}
\]
At a fixed integer \(n>1\) that is not a prime power the corresponding limit
is zero. Equation (9) is a classical lower-order arithmetic bias of
size \(1/\log T\), whereas (8) has order-one size. Both have the
same box-transform shape for the different reason that the sampled
height block is \((T,2T]\). Their resemblance is imposed by the
window, and the amplitudes must not be confused. The paired
[visualization](../visualizations/zero-ordinate-character-boundaries.md)
displays these two layers and the sufficient moment-growth region.

## Prior art, consequences and limits

Kevin Ford and Alexandru Zaharescu, *On the distribution of imaginary
parts of zeros of the Riemann zeta function*, J. reine angew. Math.
579 (2005), 145–158,
[arXiv:math/0405459v2](https://arxiv.org/html/math/0405459v2),
§3, Lemmas 1–2, supply the two uniform analytic inputs above. Their
paper already studies lower-order prime-resonant bias. Kevin Ford,
Xianchang Meng and Alexandru Zaharescu, *Simultaneous distribution of
the fractional parts of Riemann zeta zeros*, Bull. London Math. Soc.
49 (2017), 1–9,
[DOI 10.1112/blms.12001](https://doi.org/10.1112/blms.12001),
[author manuscript](https://www.ford126.web.illinois.edu/wwwpapers/FMZ.pdf),
give fixed-dimensional joint distribution and a quantitative
weighted/unweighted comparison. Those theorems are not invoked with
uncontrolled growing dimension.

The current WI-461 already contains the uniform mirror-pair integration
(6) and a growing prime-box application. The new local content is its
explicit transfer to changing **bounded-bandwidth Wang shell moments
and fixed-radius paths**, including the actual coefficient estimate
(7) and the covered growth regimes. The resonance profile and
near-zero box profile are controls, not discoveries. No novelty is
claimed for Landau's formula, Selberg density, Fourier approximation,
or the derived general inequalities.

This resolves the quantitative sampling prerequisite in the local
zero-ordinate clue. It does not identify a non-Haar selector or settle
the broader phase-anchoring clue. For \(Y_T=T^{a+o(1)}\) and
\(W_T=(\log T)^{b+o(1)}\), the strict inequalities
\(2Ra<1\), \(2Rb<1\) suffice at a fixed degree \(R\).
A finite number of controlled moments does not prove every continuous
path test; that requires the condition at **each** fixed degree.
Failure of this sufficient estimate proves neither an anomaly nor
failure of a sharper estimate. Resonance subtraction can improve
particular coefficient banks and is not analyzed here.

All-zero counting is essential. Nothing here applies automatically to
critical-line-only, simple-only or hypothetical off-line subpopulations,
nor to consecutive-zero gaps instead of fixed time offsets. Growing
radii, growing test degree, shrinking thresholds and unknown Haar
boundary concentration remain outside the path conclusion. No finite
height numerical guarantee is provided by unspecified implied constants.

The decisive audit checks are the mirror pairing, the dyadic factor
\(T/(2\pi D_T)\), the rational divisor floor, the grouped-character
Parseval bound and the order of limits in mesh approximation. The
result uses analytic proofs, not observed zero samples, simulated
independent phases, a fitted rate or a claim about RH.
