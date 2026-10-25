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

The all-dyadic premise in [MI-102](MI-102-centered-dyadic-variance-recovers-full-principal-parts.md)
belongs to its periodic-seam proof. The full-zero-set certificate here
allows an arbitrary unbounded scale set, while retaining a quantified
exceptional-start bill. Neither version supplies the arithmetic ceiling.
