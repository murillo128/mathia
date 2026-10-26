# MI-103 — Bounded jumps price deleted starts in a pole-isolating test

**Evidence level:** supported conditional synthesis of [MC-528](../../findings/MC-528-multiplicity-aware-annihilation-forces-mobius-variance-on-every-block.md), [MC-530](../../findings/MC-530-nonquasianalytic-tests-reach-logarithmic-mobius-windows.md), [MC-531](../../findings/MC-531-bounded-jumps-recover-trimmed-mobius-variance.md), and [MC-532](../../findings/MC-532-paired-boxes-recover-trimmed-mobius-variance-at-macroscopic-lengths.md). The interpolation and analytic ingredients are classical. No retained-energy ceiling, exceptional-set estimate, external novelty or formal verification is supplied.

For integers \(X,H\ge1\), let \(I_X=\{X,\ldots,2X-1\}\) and
\(S_H(j)=M(j+H)-M(j)\). Delete any \(E\subset I_X\),
\(B=|E|<X/2\), choose any one constant \(c\in\mathbb C\), and put
\[
V_E(c)=\sum_{j\in I_X\setminus E}|S_H(j)-c|^2.
\]
The exact jump constraint
\[
S_H(j+1)-S_H(j)=\mu(j+H+1)-\mu(j+1),\qquad |\Delta S_H|\le2
\]
controls omitted mass even when \(c\) is the retained-set mean and has no supplied bound.

For any length-\(N\) sequence with \(|u_{j+1}-u_j|\le L\), deleted
count \(B<N/2\), and retained energy \(V\),
\[
\sum_{j=1}^N|u_j|\le2\sqrt{NV}+2LB^2.
\]
Indeed every deleted index lies in a block of \(2B+1\) indices with
at least \(B+1\) retained values within distance \(2B\). Thus
\(|u_j|\le\sqrt{V/(B+1)}+2LB\); sum this over the deleted set and
apply Cauchy–Schwarz to the rest. Overlaps of these blocks do not
create an extra energy factor, since each estimate uses the same global
\(V\) as an upper bound. Consequently
\[
\sum_{j\in I_X}|S_H(j)-c|\le2\sqrt{XV_E(c)}+4B^2.
\tag{*}
\]

If zeta has a zero \(\rho_0=\beta+i\gamma\), \(\beta>1/2\),
of multiplicity \(m\), MC-528 constructs one fixed complex smooth test
\(\phi\), supported in \((1,2)\), with \(\int\phi=0\), such that
\[
\sum_n\mu(n)\phi(n/X)
=X^{\rho_0}Q_{m-1}(\log X)+O(X^{\sigma_1}),\quad
1/2<\sigma_1<\beta,
\]
where \(Q_{m-1}\) has a nonzero leading coefficient. A sparse canonical
product cancels every other zero with its full multiplicity, including
the conjugate; local division bounds the cancelled reciprocal before
the contour shift. Hence no cosine zeros erase the test on selected
scales. The construction depends on the full hypothetical zero set.

Write \(S_{X,H}(y)=M(y+H)-M(y)\). For each fixed \(r>1\),
MC-530 gives mean-zero compact tests \(f_h\)
with uniformly bounded sup norm for
\(h=H/X\le1/[\log X(\log\log X)^r]\), and
\[
\left|H^{-1}\int_X^{2X}(S_{X,H}(y)-c)f_h(y/X)\,dy\right|
\gg X^\beta(\log X)^{m-1}.
\]
The test is unchanged when starts are deleted: use (*) to bound the
**complete linear pairing**, rather than cutting the test by the good-set
indicator or trying to reconstruct its second moment. Integer windows
are constant on each unit cell, so this gives
\[
\boxed{\sqrt{XV_E(c)}+B^2\gg H X^\beta(\log X)^{m-1}.}
\]
For all sufficiently large \(X\), constants are uniform in \(X,H,E,c\)
in this range, but depend on the
selected zero, full zero set and \(r\). Subtracting a constant preserves
the jump bound and is annihilated by the test; a start-dependent fitted
center has neither property automatically.

At \(H=\lfloor X/[\log X(\log\log X)^r]\rfloor\), bounds
\[
B_X\ll_\varepsilon X^{3/4+\varepsilon},\qquad
V_{E_X}(c_X)\ll_\varepsilon X^{1+\varepsilon}H
\]
for every \(\varepsilon>0\), on any one unbounded set of integer scales,
imply RH. The set, masks and centers are fixed as families before the
epsilon quantifier. RH supplies the converse with no deletions and zero
center through MC-520's complete moment estimate. At fixed
\(H=\lfloor X^\theta\rfloor\), \(0<\theta<1\), a count
\(B_X\ll_\varepsilon X^{\delta+\varepsilon}\), \(0\le\delta<1\),
and the same energy ceiling instead exclude
\(\Re\rho>\max(1-\theta/2,2\delta-\theta)\).

The same deletion lemma also works at macroscopic lengths if two
channels reconstruct the smooth target. For integers \(1\le H\le X/20\),
put \(L_1=H\), \(L_2=K=\lfloor\sqrt2H\rfloor\), and allow separate
masks \(E_i\), counts \(B_i=|E_i|<X/2\), and constants \(c_i\). Define
\(V_i=\sum_{j\in I_X\setminus E_i}|S_{L_i}(j)-c_i|^2\).
MC-532's compact-distribution two-box inverse supplies uniformly
bounded mean-zero smooth tests, supported in one fixed compact subset
of \((1,2)\). Integer rounding gives target error \(O(X^{-1})\),
which costs only \(O(1)\) against the bounded Möbius coefficients.
Applying (*) separately to the two complete pairings gives
\[
\boxed{
\frac{\sqrt{XV_1}+B_1^2}{H}
+\frac{\sqrt{XV_2}+B_2^2}{K}
\gg X^\beta(\log X)^{m-1}.}
\]
Constants depend on the selected zero and full zero set, uniformly in
all the stated observation choices. The masks need not coincide and
the centers may be the separate retained means; neither test is cut
by its mask. This is joint recovery, not a claim that either single
variance must exceed its ceiling.

At \(H=\lfloor X/20\rfloor\), RH is equivalent to the existence of
one unbounded integer scale set and mask/center families, fixed before
epsilon, for which both estimates
\(B_i\ll_\varepsilon X^{3/4+\varepsilon}\) and
\(V_i\ll_\varepsilon X^{1+\varepsilon}L_i\) hold for every
\(\varepsilon>0\), uniformly on that scale set.
These estimates bound the displayed left side by
\(O_\varepsilon(X^{1/2+\varepsilon/2}+X^{1/2+2\varepsilon})\),
excluding every \(\beta>1/2\) by choosing sufficiently small epsilon.
Conversely, [MC-520](../../findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target.md)
supplies both complete uncentered moments under RH; use empty masks
and zero centers. This removes the single-channel length restriction
by changing the observations, and supplies no independent arithmetic
upper bound. The source-independent inverse and its different prime
and reciprocal-pole inputs are compared in
[global MI-040](../../../mind/intuition/MI-040-paired-box-inversion-transports-trimmed-mobius-pole-tests.md).

The \(B^2\) cost is sharp for absolute-mass recovery from bounded jumps:
two separated opposite triangular sliding-sum spikes can have retained
energy zero and total mass comparable to \(B^2\). They arise from a
bounded nonmultiplicative coefficient sequence. They do not establish
optimality of the Möbius \(3/4\) exponent or obstruct signed test-specific
cancellation. The improvement over an amplitude-only \(HB\) bill matters
when \(B=o(H)\). Arbitrary measurable deletions cutting unit cells and
qualitative density-one statements are outside this discrete budget.

[MC-533](../../findings/MC-533-geometric-start-coverage-recovers-sparsely-sampled-mobius-variance.md)
replaces the count-only bill by the geometry of any nonempty retained
set, with no majority requirement. For each channel map every
\(j\in I_X\) to its nearest retained point \(\pi_i(j)\), breaking ties
toward the smaller point, and define
\[
w_{i,r}=|\pi_i^{-1}(r)|,\qquad
D_i=\sum_{j\in I_X}|j-\pi_i(j)|,\qquad
\widetilde V_i(c_i)=\sum_{r\in R_i}w_{i,r}|S_{L_i}(r)-c_i|^2.
\]
Telescoping the jumps and weighted Cauchy–Schwarz give
\[
\sum_{j\in I_X}|S_{L_i}(j)-c_i|
\le\sqrt{X\widetilde V_i(c_i)}+2D_i,
\qquad
\sum_{i=1}^2\frac{\sqrt{X\widetilde V_i(c_i)}+D_i}{L_i}
\gg X^\beta(\log X)^{m-1}.
\]
The same complete tests supply the second inequality; neither the
centers nor the mean-zero tests are fitted separately at each start.
An unweighted sample energy is insufficient on an irregular set:
\(\widetilde V_i(c)\le w_{i,\max}\sum_{r\in R_i}|S_{L_i}(r)-c|^2\)
is a valid conversion only with its actual coverage weight paid.

Fix \(g_X=\lfloor\sqrt X\rfloor\) and
\(R_X=\{X+kg_X:0\le k\le\lfloor(X-1)/g_X\rfloor\}\), of size
\(q_X\asymp\sqrt X\). Then \(D_i\le Xg_X\),
\(w_{i,\max}\le2g_X\), and \(g_Xq_X\le2X\). At
\(H=\lfloor X/20\rfloor\), put
\(Q_i(X)=\min_c\sum_{r\in R_X}|S_{L_i}(r)-c|^2\).
The existence of one unbounded integer scale set, fixed before epsilon,
on which both \(Q_i(X)/q_X\ll_\varepsilon X^{1+\varepsilon}\)
hold for every \(\varepsilon>0\) is equivalent to RH. Indeed the
recovery cost is \(O_\varepsilon(X^{1/2+\varepsilon/2}+X^{1/2})\);
the converse uses RH's pointwise Mertens bound with center zero,
not an inference from a complete mean square to its sparse sample.
Thus deleting \(X-O(\sqrt X)\) well-distributed starts is compatible
with this criterion even though it exceeds the count-only allowance.

For \(q\) samples in \(N\) consecutive starts, the distance cost obeys
\[
D\ge\frac{N^2/q-q}{4}.
\]
The sequence \(u_j=A\operatorname{dist}(j,R)\) has jumps at most
\(A\), zero observed values and absolute mass exactly \(AD\).
At macroscopic lengths this yields a worst-case cost of order at least
\(N/q\) when \(q\le\sqrt N\). The square-root sample exponent is
therefore sharp for this generic absolute-mass recovery method. Compatible
signed window tests need the separate construction below; necessity for
actual Möbius remains unproved.
Nearest assignment minimizes \(D\), not necessarily the whole bound
including the weighted energy. No sample-energy ceiling is established.

[MC-534](../../findings/MC-534-common-squarefree-coefficients-retain-signed-sampling-ambiguity.md)
supplies the missing compatible **signed** control. Fix any nonzero
\(\phi\in C_c^1((1,2);\mathbb C)\). There is \(\kappa_\phi>0\) such that, for all sufficiently large
\(X\), every list of \(q\le\kappa_\phi X\) integer interval
observations \(A(v_\ell)-A(u_\ell)\) admits two common coefficient
sources with
\[
|a^\pm(n)|=\mu(n)^2,\qquad
\mathcal O_\ell(a^+)=\mathcal O_\ell(a^-)\in\{-1,0,1\},\qquad
|T_{\phi,X}(a^+)-T_{\phi,X}(a^-)|\gg_\phi\frac{X}{q+1},
\]
where \(A(t)=\sum_{n\le t}a(n)\) and
\(T_{\phi,X}(a)=\sum_na(n)\phi(n/X)\). The list can include
both window lengths, and the exact observations agree before centering.
Every channel's sample-centered energy is at most its sample count.

The construction explains why square-free support and signed testing
do not remove the ambiguity. The baseline alternates signs on the
square-free integers, so its prefix is \(Q(n)\bmod2\), with
\(Q(n)=\sum_{j\le n}\mu(j)^2\). Partition a fixed derivative-phase
interval \([sX,tX]\) at all observed endpoints. In each gap with
\(m_j\) square-free sites, opposite sign bridges of half-length
\(h_j=\lfloor m_j/2\rfloor\) return both prefixes to the baseline;
an odd final site has the same sign in both sources. Their difference
primitive \(F=A^+-A^-\) is nonnegative and vanishes at every endpoint.
With \(k\le2q+1\) gaps and total population \(S\asymp_\phi X\),
\[
\sum_nF(n)\ge2\sum_jh_j^2\ge\frac{(S-k)_+^2}{2k},\qquad
T_{\phi,X}(a^+)-T_{\phi,X}(a^-)
=-\sum_nF(n)\{\phi((n+1)/X)-\phi(n/X)\}.
\]
Choose \(|\omega|=1\) and the fixed interval so that
\(\Re(-\omega\phi')\ge\eta>0\); the signed target then sees at
least \(\eta X^{-1}\sum F\). Only total square-free density is used,
not density in each short gap. This is classical indistinguishable-input
recovery realized by one coefficient source per control.

Thus \(q\le X^{1/2-\delta}\), fixed \(0<\delta<1/2\), leaves error
\(\gg_\phi X^{1/2+\delta}\) for some admissible signs even for a
nonlinear estimator or deterministic adaptive interval queries. A fixed
pair can realize prescribed observations on separated scales
\(X_{j+1}\ge4X_j\), with starts in \([X_j,2X_j)\) and lengths
at most \(X_j\). Dense interlacing and randomized average-case claims
are not supplied. The target must be fixed before \(X\) varies.
These controls have no imposed multiplicativity or reciprocal-zeta pole
formula. They rule out saving a sample-count power from exact magnitudes,
common windows and signed recovery alone, not from additional Möbius
arithmetic. They do not prove the actual source needs this many samples.

The all-dyadic premise in [MI-102](MI-102-centered-dyadic-variance-recovers-full-principal-parts.md)
belongs to its periodic-seam proof. The full-zero-set certificate here
allows an arbitrary unbounded scale set, while retaining a quantified
exceptional-start bill. Neither version supplies the arithmetic ceiling.
