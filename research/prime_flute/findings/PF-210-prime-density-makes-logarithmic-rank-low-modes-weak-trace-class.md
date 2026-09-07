# PF-210 — prime density makes logarithmic-rank low modes weak trace class

**Status:** `EXACT-DERIVED + ARITHMETIC-COUNTING + CONDITIONAL-APPLICATION + POSITIVE/BOUNDARY`. PF-209 leaves one smooth-seam obstruction in a deliberately global form: after the fixed-profile principal, cutoff-commutator, and artificial-boundary pieces have acquired prime-summable strong-trace budgets, a native global-to-buffer reduction could still lose control through a low-frequency exterior/interface map. PF-189 and PF-199 reassemble weak-trace families by exact singular-value counting, but their applications use an absolutely summable weak-endpoint mass. That absolute summability is sufficient, not necessary. On the prime-flute module scales

\[
d_n\lesssim P_n^{-1},\qquad a_n\lesssim \log P_n,
\]

an orthogonal module family with only `O(1+a_n)` low modes and operator norm `O(d_n)` is already globally weak trace class even if one cannot sum the individual rank-times-norm envelopes. At threshold `\sigma`, only modules with `P_n\lesssim\sigma^{-1}` can contribute, and their total admissible rank is

\[
O\!\left(\sum_{p\le C/\sigma}(1+\log p)\right)
=O(\sigma^{-1})
\]

by the elementary Chebyshev bound `\vartheta(x)=\sum_{p\le x}\log p=O(x)`. The conclusion survives a fixed finite coloring of two-sided module supports. Thus the unresolved PF-209 exterior gate does **not** need an `\ell^1` sum of low-mode endpoint masses if a future decomposition retains one `d_n` operator factor and compresses the globally coupled sector to `O(a_n)` modes per module. Neither property is proved here for the native resolvent; PF-210 isolates the exact weaker endpoint target.

## Claim

Let `P_n` run through the prime labels of the prime-flute tail. Suppose positive scales `a_n,d_n` satisfy

\[
a_n\le A(1+\log P_n),
\qquad
d_n\le \frac{D}{P_n}.
\tag{1}
\]

Let

\[
B_n:H_n\longrightarrow K_n
\]

be finite-rank operators between mutually orthogonal source and target summands, with

\[
\boxed{
\operatorname{rank}B_n\le R(1+a_n),
\qquad
\|B_n\|\le M d_n.
}
\tag{2}
\]

For a compact operator `T`, write

\[
N_T(\sigma)=\#\{j:s_j(T)>\sigma\},
\qquad
q(T)=\sup_{\sigma>0}\sigma N_T(\sigma).
\tag{3}
\]

Then the orthogonal direct sum

\[
B=\bigoplus_n B_n
\tag{4}
\]

is compact and

\[
\boxed{
B\in\mathcal S_{1,\infty},
\qquad
q(B)\le C(A,D,M,R).
}
\tag{5}
\]

More generally, suppose the physical family is the sum of a fixed number `K` of colors,

\[
B=\sum_{c=1}^K B^{(c)},
\tag{6}
\]

and within each color the module pieces are two-sided orthogonal blocks satisfying (2). Then

\[
\boxed{
B\in\mathcal S_{1,\infty},
\qquad
q(B)\le C_K(A,D,M,R),
}
\tag{7}
\]

with no factor depending on the prime index, Lambert depth, or the number `a_n/d_n` of natural-width seam cells.

The conclusion is a **distributional** endpoint statement. It does not assert trace class, does not require

\[
\sum_n q(B_n)<\infty,
\tag{8}
\]

and does not prove that the still-unconstructed PF-209 global exterior correction admits the rank and norm bounds (2).

## 1. Threshold counting uses the prime distribution before summing module masses

Because the blocks are orthogonal on both sides, their nonzero singular values form a literal multiset union, exactly as in PF-189/PF-199. Hence

\[
N_B(\sigma)=\sum_n N_{B_n}(\sigma).
\tag{9}
\]

A block with `\|B_n\|\le\sigma` contributes nothing. From (1)--(2), every contributing module therefore satisfies

\[
P_n<\frac{MD}{\sigma}.
\tag{10}
\]

For a contributing block, the crude rank bound is enough:

\[
N_{B_n}(\sigma)\le\operatorname{rank}B_n
\le C(1+\log P_n).
\tag{11}
\]

Put `X=MD/\sigma`. For `X\ge2`, equations (9)--(11) give

\[
N_B(\sigma)
\le C\sum_{p\le X}(1+\log p).
\tag{12}
\]

Writing

\[
\vartheta(X)=\sum_{p\le X}\log p,
\tag{13}
\]

and using `\log p\ge\log2`,

\[
\pi(X)+\vartheta(X)
\le\left(1+\frac1{\log2}\right)\vartheta(X).
\tag{14}
\]

The elementary estimate proved in the next section gives

\[
\vartheta(X)\le C_0X.
\tag{15}
\]

Therefore

\[
\boxed{
N_B(\sigma)\le \frac{C}{\sigma}
}
\tag{16}
\]

for the nontrivial small-`\sigma` regime; the bounded large-`\sigma` regime is absorbed into the same constant. Taking the supremum in (3) proves the weak-`S_1` estimate.

Compactness is separate and easier. Every block is finite rank and

\[
\sup_{n>N}\|B_n\|
\le \frac{MD}{P_{N+1}}\longrightarrow0.
\tag{17}
\]

Thus the finite partial block sums converge to `B` in operator norm, so `B` is compact.

The logical order matters. Summing a per-module weak quasi-norm first throws away the threshold information `P_n\lesssim\sigma^{-1}`. PF-210 instead fixes the singular-value level first and only then counts the modules capable of reaching that level.

## 2. The only arithmetic input is an elementary Chebyshev upper bound

No prime number theorem is needed. For every integer `m\ge1`, each prime `p` with

\[
m<p\le2m
\]

divides the central binomial coefficient `\binom{2m}{m}`. Therefore

\[
\vartheta(2m)-\vartheta(m)
\le \log\binom{2m}{m}
\le 2m\log2.
\tag{18}
\]

Apply (18) on dyadic scales. For `j\ge1`,

\[
\vartheta(2^j)
\le
\sum_{k=0}^{j-1}2^{k+1}\log2
<2^{j+1}\log2.
\tag{19}
\]

Given `X\ge2`, choose `j` so that

\[
X\le2^j<2X.
\]

Monotonicity and (19) yield

\[
\boxed{
\vartheta(X)\le4(\log2)X.
}
\tag{20}
\]

This is precisely the amount of prime sparsity needed in (12). The logarithmic rank allowance in (2) is paired with the logarithmic weight naturally counted by `\vartheta`; no asymptotic formula for `\pi(X)` enters.

This also explains why the result is genuinely tied to the prime-indexed module density even though the operator-ideal argument itself is elementary. Replacing the prime labels by all integers and retaining rank `O(\log n)` would give only the crude level count `O(X\log X)` from the same envelopes, which is not a weak-`S_1` bound.

## 3. Fixed finite coloring preserves the endpoint

PF-199 records the elementary Fan counting inequality

\[
N_{S+T}(\alpha+\beta)
\le N_S(\alpha)+N_T(\beta).
\tag{21}
\]

Within one color, two-sided module orthogonality gives the exact direct-sum argument above, hence

\[
N_{B^{(c)}}(\sigma)\le\frac{C}{\sigma}
\qquad(c=1,\ldots,K).
\tag{22}
\]

Apply (21) iteratively with threshold `\sigma/K` to the `K` colors:

\[
N_B(\sigma)
\le
\sum_{c=1}^K N_{B^{(c)}}(\sigma/K)
\le
\frac{CK^2}{\sigma}.
\tag{23}
\]

This proves (7). The fixed-color condition is the same kind of two-sided support requirement that PF-199 uses: disjoint coefficient supports alone do not make globally supported resolvent pieces orthogonal.

The new point relative to PF-199 is that one does **not** estimate

\[
q(B^{(c)})
\le\sum_n q(B_n^{(c)}).
\tag{24}
\]

Instead, the level-dependent prime cutoff (10) is retained until after the ranks are counted. This permits a weak endpoint even when absolute summation of the individual endpoint envelopes is unavailable.

## 4. `O(a_n)` module rank is a real gate, not bookkeeping

From (2) alone, the individual block has the elementary endpoint bound

\[
q(B_n)\le
\operatorname{rank}(B_n)\|B_n\|
\le C(1+a_n)d_n
\le C\frac{1+\log P_n}{P_n}.
\tag{25}
\]

The majorant on the right is not an `\ell^1` route one can use to prove the global endpoint by absolute weak-mass summation. PF-210 shows that this is not fatal: the direct-sum counting distribution is better than the sum of the individual quasi-norm envelopes.

On the other hand, the rank hypothesis cannot simply be replaced by the raw natural-width cell count

\[
N_n\asymp \frac{a_n}{d_n}.
\tag{26}
\]

Indeed a finite-rank block with `r_n` singular values all comparable to `d_n` has

\[
q(B_n)\asymp r_nd_n.
\tag{27}
\]

At the cellwise saturated scale `r_n\asymp a_n/d_n`, equation (27) becomes

\[
q(B_n)\asymp a_n,
\tag{28}
\]

which is not even uniformly bounded as the Lambert depth grows. Thus a future proof cannot claim PF-210 merely by counting one independent low mode per shrinking cell. The globally coupled low-frequency sector must be compressed to the **module spectral scale** `O(a_n)`, or else its singular values must decay substantially below the crude `O(d_n)` norm envelope.

Equations (25)--(28) are only upper-envelope and model diagnostics. They do not assert that the actual exterior correction saturates either rank or norm bound.

## 5. Consequence for the PF-209 global-to-buffer gate

PF-207--PF-209 establish three scale-sensitive facts for the optional smooth decomposition-cuff route:

- the Dirichlet principal critical block keeps its physical `d_n^2` factor;
- scale-matched cutoff commutator errors are strongly trace-summable;
- fixed-profile artificial-boundary recoupling errors inside the quadratic gradient-resolvent word are strongly trace-summable with module cost `O(d_n^3+a_nd_n^2)`.

PF-209 therefore leaves the possibility that passing from the native noncompact resolvent to those fixed buffers creates a **global low-frequency exterior/interface response** not controlled by the local boundary calculus. PF-210 sharpens what would be sufficient for that remaining sector.

Suppose a future exact global-to-buffer identity splits the unhandled low-frequency part into a fixed number of two-sided orthogonal module colors and proves

\[
\operatorname{rank}B_n\le C(1+a_n),
\qquad
\|B_n\|\le Cd_n.
\tag{29}
\]

Then that entire low-frequency family is already in `\mathcal S_{1,\infty}` by (7). One does **not** additionally need a prime-summable estimate for `\sum_n q(B_n)` or a strong trace-class estimate for those low modes.

The useful smooth-route target can therefore be stated more narrowly:

\[
\boxed{
\begin{array}{l}
\text{keep one }d_n\text{ factor in the globally coupled exterior response,}\\
\text{and compress the unresolved low-frequency sector to }O(a_n)\text{ modes per module.}
\end{array}}
\tag{30}
\]

This is compatible with the geometric expectation that a genuinely module-scale bounded tangential-frequency sector on an interface of length `O(a_n)` has only `O(a_n)` modes, while the much larger `O(a_n/d_n)` cell-scale population belongs to the high-frequency/local regime already targeted by PF-207--PF-209. PF-210 does **not** prove that the native PF exterior map admits this frequency separation or that its low modes satisfy the `O(d_n)` norm estimate. Those are now explicit falsifiable operator tasks rather than hidden demands for absolute summability.

PF-204's unsmoothed native two-Hilbert factorization remains a separate route. PF-183's true-short-collar conservative splice also remains separate.

## 6. Prior art and novelty audit

No novelty is claimed for weak Schatten ideals, direct-sum singular-value counting, Fan inequalities, finite coloring, or Chebyshev's bound `\vartheta(x)=O(x)`. PF-189 already uses exact counting functions for an orthogonal short-collar family, and PF-199 records both the two-sided support criterion and the finite-color Fan estimate. Equation (18)--(20) includes a self-contained elementary proof of the only prime-counting estimate used here, so no new analytic-number-theory theorem is imported.

A structure-directed literature audit for block-diagonal weak Schatten/Lorentz ideals and singular-value counting found the expected general operator-ideal framework: membership is determined by the distribution of the singular-value sequence, and orthogonal block sums reduce to sequence rearrangement. That general fact is classical and is not presented as new. The audit did not identify a theorem whose content is the prime-flute-specific conjunction (1)--(2) with the PF-209 low-frequency global-to-buffer gate; search absence is not used as evidence of abstract novelty.

The project-specific deduction is the endpoint budget itself: **prime density converts `O(\log P)` module multiplicity at `O(P^{-1})` amplitude into a global `O(\sigma^{-1})` singular-value count.** This is strictly weaker than the absolute endpoint-mass criterion used in PF-199 and therefore removes an unnecessary `\ell^1` requirement from one plausible form of PF-209's remaining low-frequency reassembly problem. The same counting benefit applies to the all-composite shift clone because its comparison modules retain the same prime indexing; it is an analytic assembly mechanism, not a prime/clone separator or an RH mechanism.

## 7. Falsification and boundary checks

A later adversary can audit PF-210 through the following chain:

1. verify the exact direct-sum identity (9) and that both source and target module spaces must be orthogonal;
2. check that `\|B_n\|\le Md_n` implies the threshold cutoff (10) before ranks are summed;
3. derive (18) from divisibility of the central binomial coefficient and reproduce the dyadic Chebyshev estimate (20);
4. combine (11)--(15) to obtain `N_B(\sigma)=O(\sigma^{-1})` without summing `q(B_n)` first;
5. verify compactness independently from the vanishing tail operator norm (17);
6. apply PF-199's Fan inequality only across the fixed number of colors, obtaining (23);
7. keep (29) explicitly conditional: PF-207--PF-209 do not prove the native exterior map has finite rank `O(a_n)` or norm `O(d_n)`;
8. reject a cell-count substitution `rank=O(a_n/d_n)` unless extra singular-value decay compensates for it;
9. do not infer trace class, spectral shift, determinant, wave-operator completeness, or any RH consequence from weak `S_1` alone;
10. keep the smooth seam, PF-204 piecewise-transport route, and PF-183 true-short-collar gate logically distinct.

PF-210 would need narrowing if the module labels entering the actual unresolved family are not controlled by the prime scale in (1), if low-frequency reassembly cannot be made two-sided orthogonal up to finitely many colors, if the outer map consumes the `d_n` norm factor, or if the natural global low-mode rank grows faster than `O(a_n)` without compensating singular-value decay.

## Consequences for the research line

The smooth-seam endpoint no longer needs every surviving global correction to inherit the strong `\ell^1` budgets of PF-207--PF-209. Those strong estimates remain preferable for the local principal/commutator/artificial-boundary pieces, but **a genuinely global low-frequency remainder may live only at the weak endpoint and still be admissible**.

The next discriminating step is correspondingly concrete: construct the native global-to-buffer identity and inspect its exterior low-frequency spectral multiplicity and scale. If the unresolved part retains `O(d_n)` norm and only `O(a_n)` module modes, PF-210 closes its weak-trace reassembly immediately. If it instead carries `O(a_n/d_n)` independent cell-scale modes at size `O(d_n)`, or loses the `d_n` factor through the exterior map, PF-210 fails exactly where the global geometry re-enters. This turns PF-209's qualitative warning about low-frequency loss into a quantitative endpoint test.