# ANF-006 — local ordered-gap certificates already escape the global pair-moment ceiling

**Status:** `FORMAL-ARTIFACT + LITERATURE+DERIVED + EXACT-STRUCTURAL-CLASSIFICATION`. A registered Lean development proves an unconditional four-point local-gap refinement of the Anthropic/Montgomery--Taylor simple-critical-zero bound. The new Mathia conclusion is not the numerical constant itself: it is that the surviving configuration-level branch left open by `ANF-004`/`ANF-005` is already known to carry strictly more unconditional information than a single global support-one pair moment.

## 1. A machine-checked unconditional gain beyond the Montgomery--Taylor baseline

Write

\[
H=\frac32-\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right)
 =0.6725007036794116\ldots
\]

for the unconditional simple-critical proportion proved in the `anthropics/zeta-23-lean` development.

The Palomar-registered `teal-sea/zeta-lab` bridge proves, for Mathlib's `riemannZeta`, a four-point theorem with no finite-certificate hypothesis. Its finite local inequality is

\[
\forall g\in\mathbb R_{\ge0}^{3},\qquad
\frac{2310}{10^6}\le F_4(2500,g),
\tag{1}
\]

where, for \(g=(x,y,z)\),

\[
\begin{aligned}
F_4(2500,g)
={}&\frac{x+y+z}{2500}
 +\frac23\bigl(w(x)+w(y)+w(z)\bigr)\\
&+w(x+y)+w(y+z)+2w(x+y+z),
\end{aligned}
\tag{2}
\]

and \(w=k^2\) is the same support-one overlap kernel used by the bridge.

The Lean theorem `four_point_cert` proves (1) for every nonnegative gap triple. Substitution into the general `n_point_bound` theorem with `m=435` yields

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\Phi_4
:=
\frac{906250H-1085}{904171}
=
0.6728470197666887\ldots .
}
\tag{3}
\]

Thus the formally checked gain over \(H\) is

\[
\Phi_4-H=0.000346316087277\ldots,
\tag{4}
\]

about \(0.03463\) percentage points.

This is not merely a numerical interval certificate attached to an informal passage to zeta zeros. In the frozen Palomar artifact, both the four-point finite inequality and the bridge to the asymptotic zeta statement are Lean theorems. The Palomar entry `PALOMAR-2026-08-25-000005` records the four-point bound/ratio among its advertised declarations, at source commit `84312e4477dfeb7e0d8a91c38897f225f5a52f19`, with high trust. The repository's pinned axiom audit reports no `sorryAx` in the proved surface and only the standard `propext`, choice, and quotient axioms.

## 2. Why this does not contradict `ANF-004`

`ANF-004` shows that if finitely many **global scalar pair moments** are first computed and a convex/affine certificate is then applied to those moments, a supporting-hyperplane argument reduces the asymptotic bound to one signed scalar pair profile. `ANF-005` then derives necessary finite-configuration constraints and the exact normalization-slack cost for that affine signed profile.

The four-point mechanism changes the order of operations. It does not first compress the zero configuration to finitely many global pair sums. Instead it:

1. orders consecutive zeros and applies the pointwise inequality (1) to each local three-gap vector;
2. converts those local inequalities into energy lower bounds inside finite consecutive blocks;
3. applies a nonlinear spectral defect \(\operatorname{tr}\Psi(G_B)\) to each block Gram matrix;
4. uses pinching and shifted block partitions to assemble the block information;
5. only after those configuration-level operations derives the global lower bound (3).

The bridge's step table makes this separation explicit: the finite gap certificate is S10, block energy/defect are S11--S13, spectral pinching is S14, shifted-block averaging is S15, and the final scalar solve is S16.

Therefore the local-gap/block argument lies outside the hypothesis of the `ANF-004` scalarization theorem. The information gain comes from retaining **adjacency, index separation, and local block spectrum before global averaging**. The matrix language is not decorative: the nonlinear defect is evaluated while the local configuration is still present.

## 3. The configuration-level escape is established, but its present ceiling is not

This changes the live frontier. It is no longer an open question whether support-one pair information can beat Montgomery--Taylor when it is used before global moment compression: the four-point theorem answers **yes**.

What remains open is how far that mechanism can be pushed under the same evidence standard. The same `zeta-lab` development exposes an eight-point theorem with constant

\[
0.67305298298962888\ldots,
\]

but there the finite inequality remains the named hypothesis `hCert`; the Lean bridge is proved while the interval-arithmetic certificate is external. Other August 2026 projects report still larger values around \(0.67331\), again with substantial computer-assisted finite certificates and/or imported trust boundaries rather than an end-to-end theorem at the same fully checked level. This watch does not promote those headline constants to established evidence.

The important distinction is therefore not “scalar versus matrix” in syntax. It is:

\[
\text{global pair-moment compression first}
\quad\text{versus}\quad
\text{local ordered configuration processing first}.
\]

The first class is constrained by `ANF-004`/`ANF-005`; the second has already produced a strict unconditional improvement.

## 4. Prior-art and novelty assessment

The local-gap strategy is prior art. Ainta introduced the seven-point refinement; `teal-sea/zeta-lab` formalized the bridge parametrically and proved the three- and four-point finite certificates inside Lean. No novelty is claimed for (1)--(3), for the Gram-defect construction, or for the block/pinching argument.

The Mathia contribution here is the **classification relative to the current obstruction chain**. `ANF-004` deliberately left configuration-level operator structure outside its dual reduction. The external four-point theorem now supplies a concrete, audited witness that this exclusion is mathematically load-bearing rather than a merely formal loophole: local order and block spectral processing retain enough information to exceed the best zero-slack global pair-moment constant.

## 5. Falsification and trust boundary

The central classification would fail if the four-point theorem ultimately depended only on a fixed finite collection of already-global BGSST moments before any nonlinear/configuration-level operation. The formal bridge shows the opposite order: the gap certificate, block defect, pinching, and shifted partitions precede the final global solve.

The numerical theorem (3) would need to be downgraded if the Palomar-frozen Lean declarations carried an unadvertised certificate hypothesis or nonstandard proof axiom. The registered statement distinguishes the unconditional three-/four-point declarations from the conditional eight-point declaration, and the pinned axiom audit records no `sorryAx` for the proved surface.

This finding does **not** establish that \(0.6728470\ldots\) is the best currently rigorous computer-assisted constant under every acceptable proof standard. It establishes the narrower fact needed by this line: a fully machine-checked local ordered-gap/block certificate already beats \(H\), so configuration-level second-order information is a demonstrated escape from the global affine pair-moment ceiling.

## 6. Consequences for `analytic_frontier`

The accepted semidefinite/pair-correlation clue should now be split conceptually. Its scalar signed support-one question remains unresolved: decide whether `ANF-005`'s constrained objective can satisfy \(M(F)+\delta<m_{\rm MT}\). But its configuration-level branch has passed the existence test.

For that branch, the next useful analytic questions are sharper:

- determine the strongest **fully verified** finite local-gap certificate as `n` grows, rather than treating interval-search candidates as already established;
- identify which part of the gain comes from ordered adjacency, from the nonlinear block spectral defect, and from shifted pinching/averaging;
- characterize the ceiling of this local support-one information class, and what genuinely new analytic input would be required to move beyond it.

A future theorem or counterexample addressing one of these questions would be new information. Merely optimizing another unverified finite certificate constant would not by itself satisfy the line's substantive-finding gate.
