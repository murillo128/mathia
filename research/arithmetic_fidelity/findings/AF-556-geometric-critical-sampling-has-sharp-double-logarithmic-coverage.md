# AF-556 — Geometric critical sampling has sharp double-logarithmic scale coverage

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · PRIME-TAIL · CRITICAL-SCALE · NONADAPTIVE-SAMPLING · MATCHED-CONTROL · INVERSE-CONDITIONING · NO-NOVELTY-CLAIM

## Claim: a sharp observation-count law when the changed prime is unknown

Use the complete critical-index limiting curves of AF-554 and the ordered single-generator generalized-prime controls of AF-555. Write, for real \(a>0\),
\[
P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\qquad
\Phi(a)=P^{-1}(E_1(a)).
\]
For each odd rational prime \(p\), replace the generator \(p\) by \(p+1\), leaving every other generator unchanged, and put
\[
Q_p(s)=P(s)-\big[p^{-s}-(p+1)^{-s}\big],\quad
\Phi_p(a)=Q_p^{-1}(E_1(a)).
\]
The replacement is order-preserving because consecutive odd primes differ by at least two. Each modified source is an admissible generalized-prime *control*, not another rational-prime sequence. Let
\[
g_p(a)=\Phi(a)-\Phi_p(a)>0,\qquad
D_p=\max_{a>0}g_p(a).
\tag{1}
\]
The supremum exists and, by AF-555,
\[
D_p\sim\frac{1}{e\,p^2\log p}.
\tag{2}
\]

The additional result is the **entire normalized moving-boundary-layer shape**, not just its maximum. Let \(B_1\) denote the Meissel--Mertens reciprocal-prime constant, and set \(c=e^{B_1}\) and
\[
f(u)=u e^{1-u},\qquad u\ge0.
\]
Then
\[
\boxed{\lim_{\substack{p\to\infty\\p\ {\rm prime}}}
\sup_{a>0}\left|\frac{g_p(a)}{D_p}
-f\big(ca\log p\big)\right|=0.}
\tag{3}
\]
Thus a remote changed prime has a normalized detection window centered at \(a\asymp1/\log p\); the universal window shape is \(f\), even though its absolute amplitude (2) decays much faster.

Fix a detection fraction \(0<\theta<1\). For \(P\ge3\) let \(N_\theta(P)\) be the smallest number of **nonadaptive, source-critical parameter locations** in a finite set \(\mathcal A\subset(0,\infty)\), chosen with knowledge of \(P,\theta,\Phi\) but **without knowing \(p\)**, such that
\[
\forall\,p\le P\ \text{odd rational prime},\qquad
\max_{a\in\mathcal A}g_p(a)\ge\theta D_p.
\tag{4}
\]
This is a fixed-fraction *signal-capture* criterion, not a claim that the samples uniquely decode which prime was changed.

Let \(u_-(\theta)\in(0,1)\) and \(u_+(\theta)\in(1,\infty)\) be the two roots of
\[
u e^{1-u}=\theta,\qquad
u_-=-W_0(-\theta/e),\quad
u_+=-W_{-1}(-\theta/e),
\tag{5}
\]
where \(W_0,W_{-1}\) are the standard two real Lambert-\(W\) branches. Set
\(R_\theta=u_+(\theta)/u_-(\theta)>1\). Then the **sharp nonadaptive sample-count asymptotic** is
\[
\boxed{\displaystyle
\lim_{P\to\infty}\frac{N_\theta(P)}{\log\log P}
=\frac1{\log R_\theta}.}
\tag{6}
\]
A geometric grid of \(a\)-samples attains the upper bound; no finite set of fewer asymptotic samples can capture a fixed fraction of the optimal signal for all admissible single-prime controls with \(p\le P\).

The leading sample-count constant depends on the chosen fraction \(\theta\) but **not** on \(B_1\). The Mertens constant sets the grid's absolute \(a\)-location through \(c\); it cancels from the multiplicative band-width ratio \(R_\theta\).

## Proof of the uniform normalized response

Put \(L=\log p\), \(x=\Phi(a)-1\), and use AF-555's exact inverse displacement \(W_p(1+x)=g_p(a)\). For
\[
h_p(s)=p^{-s}-(p+1)^{-s}
\]
the integral identity in AF-555 gives, uniformly as \(x\to0^+\),
\[
h_p(1+x)=p^{-2}e^{-Lx}\big(1+O(x)+O(p^{-1})\big).
\tag{7}
\]
The prime-zeta logarithmic normal form (AF-552 and AF-555) supplies
\[
-P'(1+x)=x^{-1}+O(1).
\tag{8}
\]
AF-555 also establishes a derivative perturbation bound
\[
\sup_{s>1}\frac{|h_p'(s)|}{-P'(s)}=O(L/p^2)=o(1),
\tag{9}
\]
and its exact mean-value formula, with \(r_p(s)=Q_p^{-1}(P(s))\) and \(\xi\in(r_p(s),s)\),
\[
W_p(s)=\frac{h_p(s)}{-Q_p'(\xi)}.
\tag{10}
\]

For \(x=u/L\) with \(u\) in any compact subset of \((0,\infty)\), the global AF-555 upper bound first gives
\[
0<W_p(1+x)=O\!\left(\frac{1}{p^2 L}\right)=o(x).
\tag{11}
\]
Hence \(\xi-1\sim x\) uniformly for such \(u\); (8)--(10) imply
\[
p^2 L\,W_p(1+u/L)\longrightarrow u e^{-u}
\quad\text{locally uniformly for }u>0.
\tag{12}
\]
Combining this with (2) makes the normalized response converge locally uniformly to \(f(u)=e u e^{-u}\).

It remains to justify that (12) controls the *whole* positive parameter line. Equations (7)--(10), together with AF-555's global inequality (14), give for \(0<x\le L^{-1/2}\)
\[
0\le\frac{W_p(1+x)}{D_p}
\le(1+o(1))\,e(Lx)e^{-Lx}
\tag{13}
\]
with an error uniform in that interval. AF-555's estimates (17)--(18) show that the left-hand side is \(o(1)\) uniformly for \(x\ge L^{-1/2}\). For any fixed \(0<\eta<M\), (12) covers \(\eta\le Lx\le M\); on \(Lx<\eta\) and \(Lx>M\), (13) and the far-tail estimate force the normalized response to be arbitrarily small after \(\eta\downarrow0\) and \(M\uparrow\infty\). Therefore
\[
\sup_{x>0}\left|
\frac{W_p(1+x)}{D_p}-f(Lx)\right|\to0.
\tag{14}
\]

Finally the boundary expansions of \(P\) and \(E_1\) give (AF-555, equation (22))
\[
a=e^{-B_1}x+O(x^2),\qquad x=\Phi(a)-1.
\tag{15}
\]
When \(Lx\) stays in a compact positive interval, \(Lx-caL\to0\) uniformly. Outside such intervals, both nonnegative profiles in (14) and \(f(caL)\) have uniformly small tails: the map \(a\mapsto x\) is increasing, and \(a\to0\) iff \(x\to0\), while \(a\to\infty\) iff \(x\to\infty\). Apply this compact/tail decomposition to (14) to obtain exactly (3). No pointwise limit is silently promoted to a global supremum limit.

## Upper bound: one geometric sample per fixed logarithmic scale band

Fix \(0<\varepsilon<1-\theta\), and write
\[
\alpha=u_-(\theta+\varepsilon),\qquad
\beta=u_+(\theta+\varepsilon).
\]
Since \(f(u)\ge\theta+\varepsilon\) throughout \([\alpha,\beta]\), the uniform response law (3) ensures that, for all sufficiently large primes \(p\), every sample satisfying
\[
\alpha\le ca\log p\le\beta
\tag{16}
\]
captures at least the fraction \(\theta\) required by (4).

Choose \(1<\rho<\beta/\alpha\) and a fixed sufficiently large \(L_0\). Use the grid
\[
a_j=\frac{\alpha}{cL_0\rho^j},\qquad j=0,1,\ldots,J(P),
\tag{17}
\]
where \(J(P)\) is the least integer such that \(L_0\rho^{J(P)+1}\ge\log P\). If
\(\log p\in[L_0\rho^j,L_0\rho^{j+1}]\), then
\(ca_j\log p\in[\alpha,\rho\alpha]\subset[\alpha,\beta]\),
so this one sample covers the entire band. Finitely many odd primes with
\(\log p<L_0\) can each be covered by one of their exact maximizers from (1); that costs a constant independent of \(P\).

It follows that
\[
N_\theta(P)\le
\frac{\log\log P}{\log\rho}+O_{\theta,\varepsilon,\rho,L_0}(1).
\tag{18}
\]
First let \(P\to\infty\), then \(\rho\uparrow\beta/\alpha\) and \(\varepsilon\downarrow0\). Continuity of the two roots of (5) yields
\[
\limsup_{P\to\infty}
\frac{N_\theta(P)}{\log\log P}
\le\frac1{\log R_\theta}.
\tag{19}
\]

## Lower bound: a single sample cannot cover separated prime-log scales

Fix \(0<\varepsilon<\theta\). By (3), for all sufficiently large odd primes \(p\), a sample that meets the threshold \(g_p(a)\ge\theta D_p\) must satisfy
\[
u_-(\theta-\varepsilon)
\le ca\log p\le
u_+(\theta-\varepsilon).
\tag{20}
\]
Set \(R^-=u_+(\theta-\varepsilon)/u_-(\theta-\varepsilon)\), and choose any \(\lambda>R^-\).

For a fixed large \(L_0\), choose odd primes \(p_j\) with
\[
e^{L_0\lambda^j}<p_j<2e^{L_0\lambda^j}.
\tag{21}
\]
Their existence for all sufficiently large \(j\) follows already from the classical Bertrand--Chebyshev prime-interval theorem; the prime-number theorem is more than sufficient. Equation (21) implies
\[
\log p_j=L_0\lambda^j+O(1),\qquad
\frac{\log p_{j+1}}{\log p_j}\longrightarrow\lambda>R^-.
\tag{22}
\]
Increase \(L_0\) so that all chosen scales satisfy the strict separation ratio \(>R^-\) from the start.

If a single \(a\) satisfied (20) for two of these primes \(p_i<p_j\), dividing the two inequalities would force
\[
\frac{\log p_j}{\log p_i}\le R^-,
\]
contradicting their separation. Thus **each sample covers at most one member of the packed prime family**. The number of members satisfying \(p_j\le P\) is
\[
\frac{\log\log P}{\log\lambda}+O(1),
\tag{23}
\]
so
\[
\liminf_{P\to\infty}\frac{N_\theta(P)}{\log\log P}
\ge\frac1{\log\lambda}.
\]
Let \(\lambda\downarrow R^-\), then \(\varepsilon\downarrow0\), to get the reverse bound in (19) and prove (6).

The lower bound uses *actual rational primes* to index the matched source controls; no continuous surrogate of \(p\) is being substituted for the prime parameter.

## Fidelity interpretation, prior art, and decisive limitations

The derivation uses the **existing** AF-554 critical-limit construction, AF-555 exact inverse-displacement estimates and Mertens boundary constant, the standard two-real-branch Lambert-\(W\) inverse (NIST DLMF §4.13), and elementary multiplicative-interval covering. Geometric sampling across unknown scales is familiar in multiscale analysis; the band-packing argument does not claim priority for this general idea. The Mathia-specific addition is the globally uniform normalized remote-prime response (3), followed by the sharp observation-resource statement (6) for the exact AF-555 source-admissible control family and its retained critical-coordinate metric. No RH novelty or zero information is claimed.

For a concrete check, at \(\theta=1/2\) the roots of \(ue^{1-u}=1/2\) are approximately \(u_-=0.231961\) and \(u_+=2.678347\). Thus \(R_\theta\approx11.5465\) and
\[
N_{1/2}(P)\sim0.40877\,\log\log P.
\tag{24}
\]
This is a large-\(P\) asymptotic; it is not a claim that fractional sample counts, or the asymptotic coefficient without finite-size corrections, predict the small-\(P\) minimum.

The exact experiment and the failure modes are essential:

1. **Fractional, not absolute, signal:** each remote-prime maximum is only \(D_p\sim(e p^2\log p)^{-1}\). The logarithmic number of sample locations does not defeat that vanishing amplitude; robustness against generic additive errors still requires a prime-dependent precision budget of order \(D_p\).
2. **Nonadaptive locations:** the set \(\mathcal A\) is fixed before learning \(p\). Adaptive queries, derivatives, integrals, or a readout with additional source markings are different observation channels and can have different complexities.
3. **Guaranteed capture, not identification:** (4) guarantees one sample with a fixed fraction of the *pair-specific best* separation. It does not claim the samples distinguish all controls from one another, identify \(p\), or supply a minimax decoder under an unspecified noise law.
4. **Fixed \(0<\theta<1\):** no estimate uniform in \(\theta\to0\) or \(\theta\to1\) is asserted. Endpoint thresholds can change the sample-count regime.
5. **Ordered limiting experiment:** for each fixed deformed source, the critical-index limit \(n\to\infty\) is formed first. The separate \(p\to\infty\) limit is taken afterward. No joint finite-\(n\)/remote-\(p\) claim follows.
6. **Coordinate and calibration contract:** source parameter \(a\), the marked generator and the common-output-calibration quotient are retained. Arbitrary independent input reparameterization, unregistered observations, and raw-calibration noise are not covered.

Decisive audit tests: rederive (12) from the **exact** AF-555 inverse mean-value identity instead of differentiating a merely pointwise limit; prove both tails needed for the supremum in (3); check the Meissel--Mertens sign \(x/a\to e^{B_1}\); verify the Lambert-\(W\) branch order and the strict \(\theta\pm\varepsilon\) margins; and check that the lower-bound packing uses genuine admissible odd-prime deformations. These tests establish the observation-count theorem without presupposing source identification or stable RH transfer.

**Arithmetic Fidelity consequence.** Keeping the full critical curve costs infinitely many observations, but retaining a fixed fraction of the **best available separation against every one-generator perturbation up to height \(P\)** needs and suffices with only \(\Theta(\log\log P)\) nonadaptive samples. This is an exact distinction between sample cardinality, placement geometry, and amplitude precision: geometric sampling repairs unknown *location of a small signal*, not the severe \(p^{-2}(\log p)^{-1}\) metric conditioning of that signal.
