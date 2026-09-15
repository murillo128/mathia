# FD-144 — Min-wise prime selectors defeat sublinear-rank ancestry observation budgets

- **Date:** 2026-09-15
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** main-track no-go theorem / linear-rank observation-budget lower bound
- **Depends on:** FD-139, FD-142, FD-143

## Claim

FD-143 obtains a common hidden source against arbitrary source-independent ancestry partitions when the total prime-cell budget satisfies

\[
K_T M_T=o(\sqrt{r_T}),
\]

where every observed squarefree parent has at least `r_T` prime factors. Its `sqrt(r_T)` scale comes from the central point mass of a Rademacher sum. That scale is not intrinsic to the ancestry problem.

There is a different common-source construction whose one-edge defect probability is `Theta(1/r_T)` rather than `Theta(r_T^{-1/2})`. Consequently the arbitrary-observation no-go extends through every **sublinear-rank** budget.

Let `X_{p,T}` be finite sets of squarefree parents `n>1` with

\[
p\nmid n,
\qquad
\omega(n)\ge r_T,
\qquad
r_T\to\infty.
\tag{1}
\]

Let `P_T` be a finite source-independent family of active primes and put

\[
K_T:=|P_T|.
\tag{2}
\]

For each `p in P_T`, allow at most `M_T` arbitrary source-independent normalized nonnegative tests on `X_{p,T}`. Thus a test is any weight

\[
\lambda:X_{p,T}\to[0,1],
\qquad
\sum_{n\in X_{p,T}}\lambda(n)=1.
\tag{3}
\]

The tests may overlap and need not come from a partition, congruence, additive coordinate, or common weighting rule. Ordinary cells are included by taking `lambda` uniform on one cell.

If

\[
\boxed{
K_T M_T=o(r_T),
}
\tag{4}
\]

then there exist

- one fixed infinite assignment of a priority and a sign to every prime;
- one fixed global orientation `sigma in {+1,-1}`;
- one subsequence `T_j -> infinity`;

such that the resulting bounded coefficient source `a_n in {-1,0,+1}` has the same squarefree support as Möbius and satisfies, simultaneously for every active prime and every allowed test,

\[
\boxed{
\max_{p\in P_{T_j}}
\max_{\lambda\in\Lambda_{p,T_j}}
\sum_{n\in X_{p,T_j}}
\lambda(n)\,
\mathbf 1_{\{a_{pn}+a_n\ne0\}}
\longrightarrow0.
}
\tag{5}
\]

If one fixed prime `p_0` belongs to `P_{T_j}` eventually, then after passing to a further subsequence the same fixed source also obeys

\[
\boxed{
\frac1{|X_{p_0,T_j}|}
\#\{n\in X_{p_0,T_j}:a_n\ne\mu(n)\}
\ge\frac12.
}
\tag{6}
\]

Thus the observation can be much stronger than the partition model of FD-143 and still fail coefficient coercivity. In the central Farey ancestry regime `r_T asymp log log T`, every budget

\[
\boxed{
K_T M_T=o(\log\log T)
}
\tag{7}
\]

remains defeatable by one common source along a subsequence.

The improvement from `sqrt(r_T)` to `r_T` is not a sharper anti-concentration estimate. It comes from replacing a codimension-one sign wall by a **min-wise selector** whose value changes under insertion of a new prime only when that prime wins a random priority competition against all existing prime factors.

## 1. Decisive test after FD-143

FD-143 leaves two possible interpretations of its `sqrt(r_T)` threshold.

One is structural: perhaps a rank-`r_T` multiplicative parent intrinsically exposes every non-Möbius source once roughly `sqrt(r_T)` independent ancestry constraints are observed. The other is construction-specific: the prime-color half-space used there changes sign when a Rademacher sum lands on a central lattice level, whose mass is `Theta(r_T^{-1/2})`.

The discriminating test is therefore:

> Can one construct a single horizon-coherent squarefree sign source whose probability of changing across an insertion edge `n -> pn` is only `O(1/omega(n))`, uniformly for every prescribed source-independent parent and without using the observation cells?

A min-priority selector does exactly this. Once such a source exists, summing its expected defect over the whole observation family prices the number of constraints at order `r_T`, not `sqrt(r_T)`.

## 2. A fixed min-priority prime source

On one probability space, attach to every prime `q` two independent random labels:

\[
U_q\sim\operatorname{Unif}(0,1),
\qquad
\xi_q\in\{-1,+1\}
\quad\text{with}\quad
\Pr(\xi_q=\pm1)=\frac12.
\tag{8}
\]

All `U_q` and `xi_q` are mutually independent. Since there are only countably many primes and the priorities are continuous, with probability one all priorities are distinct.

For every integer `n>1`, let

\[
s(n):=\operatorname*{argmin}_{q\mid n}U_q
\tag{9}
\]

be the prime divisor of `n` with smallest priority, and define

\[
b(n):=\xi_{s(n)}.
\tag{10}
\]

For an orientation `sigma in {+1,-1}`, set

\[
a_n^{(\sigma)}:=\mu(n)\,\sigma b(n)
\qquad(n>1),
\tag{11}
\]

and set `a_1^{(sigma)}=1`. The special value at `1` is irrelevant to the high-rank parent domains and preserves the usual Möbius anchor.

After one realization of the labels, (11) is an ordinary deterministic infinite coefficient source. The random priorities and colors are only a probabilistic-method device for proving that a realization with the required properties exists.

Because of the factor `mu(n)`, every nonsquarefree coefficient is zero, while every squarefree coefficient has magnitude one. Thus the matched source preserves the exact squarefree support and amplitude class of Möbius.

## 3. Exact one-edge defect law

Fix a squarefree parent `n`, a prime `p` not dividing `n`, and write

\[
k:=\omega(n).
\tag{12}
\]

There are `k+1` independent continuous priorities attached to the prime factors of `pn`. By symmetry,

\[
\Pr\!\left(
U_p<\min_{q\mid n}U_q
\right)
=\frac1{k+1}.
\tag{13}
\]

If `p` does not win this minimum competition, then

\[
s(pn)=s(n),
\qquad
b(pn)=b(n),
\tag{14}
\]

so the ancestry edge is exact. If `p` does win, then `s(pn)=p` while `s(n)` is one of the old prime factors. Conditional on all priorities, the colors of those two distinct primes are independent fair signs, hence

\[
\Pr\bigl(b(pn)\ne b(n)\mid p\text{ wins}\bigr)=\frac12.
\tag{15}
\]

Therefore

\[
\boxed{
\Pr\bigl(b(pn)\ne b(n)\bigr)
=\frac1{2(k+1)}.
}
\tag{16}
\]

For squarefree `n` and `p\nmid n`, `mu(pn)=-mu(n)`. Equation (11) gives

\[
a_{pn}^{(\sigma)}+a_n^{(\sigma)}
=
\sigma\mu(n)\bigl(b(n)-b(pn)\bigr).
\tag{17}
\]

Thus the edge defect is independent of the orientation and

\[
\boxed{
\Pr\bigl(a_{pn}^{(\sigma)}+a_n^{(\sigma)}\ne0\bigr)
=\frac1{2(\omega(n)+1)}
\le\frac1{2(r_T+1)}.
}
\tag{18}
\]

When a defect occurs its magnitude is exactly `2`.

This `1/k` law is the whole gain over FD-143. There is no central-limit or local-limit step: the inserted prime can matter only by becoming the unique minimum-priority factor.

## 4. Arbitrary nonnegative normalized tests cost only their count

Fix `T`, `p in P_T`, and one source-independent test `lambda` satisfying (3). Define its normalized edge-defect observable

\[
E_{p,\lambda,T}
:=
\sum_{n\in X_{p,T}}
\lambda(n)\,
\mathbf 1_{\{a_{pn}+a_n\ne0\}}.
\tag{19}
\]

No independence between different parents is needed. By linearity of expectation and (18),

\[
\mathbb E E_{p,\lambda,T}
\le
\frac1{2(r_T+1)}.
\tag{20}
\]

This remains true if the supports of different tests overlap arbitrarily. In particular, nothing about the geometry, cardinality, or arithmetic definition of a cell enters the proof.

Let `Lambda_{p,T}` denote the test family for `p`, with

\[
|\Lambda_{p,T}|\le M_T,
\tag{21}
\]

and set

\[
W_T
:=
\sum_{p\in P_T}
\sum_{\lambda\in\Lambda_{p,T}}
E_{p,\lambda,T}.
\tag{22}
\]

All terms are nonnegative, and there are at most `K_T M_T` of them. Hence

\[
\boxed{
\mathbb E W_T
\le
\frac{K_T M_T}{2(r_T+1)}
=:\delta_T.
}
\tag{23}
\]

Under (4),

\[
\delta_T\longrightarrow0.
\tag{24}
\]

At a single horizon the probabilistic method already gives a realization with every observed defect at most `delta_T`, because some realization has `W_T<=E W_T` and every term is bounded by the nonnegative sum `W_T`.

The remaining issue is the same common-source gate isolated by FD-143: the realization must not be re-chosen independently at each horizon.

## 5. One infinite priority-and-color assignment works along a subsequence

Choose a subsequence `T_j` so sparse that

\[
\delta_{T_j}\le2^{-3j}.
\tag{25}
\]

Markov's inequality gives

\[
\Pr\bigl(W_{T_j}>2^{-j}\bigr)
\le
\frac{2^{-3j}}{2^{-j}}
=2^{-2j}.
\tag{26}
\]

The right-hand side is summable. By the first Borel--Cantelli lemma, with probability one only finitely many of the events in (26) occur. Consequently there exists one fixed infinite realization of all priorities and colors such that

\[
W_{T_j}\le2^{-j}
\tag{27}
\]

for every sufficiently large `j`.

Because every term in (22) is nonnegative,

\[
\max_{p\in P_{T_j}}
\max_{\lambda\in\Lambda_{p,T_j}}
E_{p,\lambda,T_j}
\le2^{-j}
\longrightarrow0.
\tag{28}
\]

This is (5), simultaneously for both global orientations because (17) shows that the zero/nonzero edge pattern does not depend on `sigma`.

The priorities and colors have now been frozen forever. Only the horizon subsequence was selected.

## 6. A fixed orientation stays macroscopically different from Möbius

It remains to show that the common source has not merely become Möbius on the domains being tested.

For `n>1` squarefree, the two orientations satisfy

\[
a_n^{(+)}=\mu(n)b(n),
\qquad
 a_n^{(-)}=-\mu(n)b(n).
\tag{29}
\]

Exactly one of these two coefficients equals `mu(n)` and the other equals `-mu(n)`. Hence on **every** finite squarefree domain `X`, without probability or asymptotics,

\[
\frac1{|X|}
\#\{n\in X:a_n^{(+)}\ne\mu(n)\}
+
\frac1{|X|}
\#\{n\in X:a_n^{(-)}\ne\mu(n)\}
=1.
\tag{30}
\]

Assume one fixed prime `p_0` is active eventually and apply (30) to `X_{p_0,T_j}`. For each `j`, one orientation disagrees with Möbius on at least half of that domain. Since there are only two orientations, one of them does so for infinitely many `j`. Pass to that infinite subsubsequence and fix that orientation once and for all.

Equation (28) survives because the edge-defect pattern is orientation-invariant. We therefore obtain one deterministic infinite source satisfying both (5) and the exact macroscopic lower bound (6).

This step is cleaner than the orientation argument in FD-143: no central zero level has to be shown negligible. The two orientations are pointwise complementary away from the fixed anchor at `1`.

## 7. Central Farey ancestry improves from root rank to full rank

In the central squarefree multiplicative regime used in FD-139 and FD-143,

\[
r_T\asymp\log\log T.
\tag{31}
\]

Substituting (31) into (4) yields

\[
\boxed{
K_T M_T=o(\log\log T).
}
\tag{32}
\]

Thus, for a fixed number of active primes, even `o(log log T)` arbitrary source-independent normalized ancestry tests per prime can all become asymptotically blind to one common source along a subsequence. The tests may be highly irregular, overlapping, weighted, and horizon-dependent.

This gains a factor `sqrt(log log T)` over FD-143. It still remains far below the `Theta(log T)` source-identity scale exhibited by FD-142, and the two budgets are not interchangeable units: (32) counts normalized ancestry probes, while FD-142 prices bits needed for full source reconstruction. The point is only that the elementary lower-bound frontier has moved substantially without approaching reconstruction.

## 8. Robustness: finite anchors, weights, and higher moments

The construction is unaffected by any fixed finite Möbius anchor. If desired, after the realization and orientation are fixed, redefine

\[
a_n:=\mu(n)
\qquad(n\le N_0)
\tag{33}
\]

for an arbitrary fixed `N_0`. Since every parent domain lies in dyadic shells with `T_j->infinity`, eventually none of the tested edges touches the modified coefficients. Equations (5)--(6) are unchanged.

The theorem already includes harmonic weighting and considerably more: any source-independent nonnegative normalized weights are permitted directly in (3). There is no need to compare `1/n` with a constant on a dyadic shell.

Finally, because a nonzero ancestry defect has magnitude exactly `2`, for every fixed `1<=s<infinity`,

\[
\sum_n\lambda(n)|a_{pn}+a_n|^s
=2^s E_{p,\lambda,T}.
\tag{34}
\]

Hence every fixed finite `L^s` ancestry moment obeys the same no-go theorem. As in FD-135 and FD-143, an `L^infinity` law is different: one surviving defect keeps the supremum equal to `2`.

## 9. What changed relative to FD-143

The new result is not merely the same prime-color wall with a better estimate.

FD-143 uses a source of the form `sign(sum epsilon_q)`. Inserting `p` changes that source only when the signed factor count lies on a central boundary. Anti-concentration makes that event `Theta(r_T^{-1/2})`, and a union budget then permits `o(sqrt(r_T))` simultaneous constraints.

Here the source retains only the color of one prime factor selected by a fixed random global priority order. Inserting `p` changes the selected factor with probability exactly `1/(k+1)`, and only half of those selector changes flip the retained color. The mechanism is therefore **low single-prime influence by min-wise competition**, not thin-boundary anti-concentration.

This matters for the research frontier. A proposed averaged ancestry law cannot now escape the matched-control family merely by using more than `sqrt(log log T)` source-independent cells. Any theorem based on fewer than linear-in-rank nonnegative normalized ancestry probes still admits a common hidden source.

At the same time, the theorem does not say that `Theta(r_T)` probes are sufficient. The scale `r_T` is where this particular first-moment union argument stops vanishing, not a proved phase transition.

## 10. Boundary and adversarial audit

Several restrictions are load-bearing.

First, all domains, active-prime sets, and test weights must be fixed independently of the hidden priorities and colors. If an observer may inspect the unknown source before choosing a test, it can place all mass on the defect set and the conclusion is false for the same circular reason identified around FD-142--FD-143.

Second, the theorem is subsequential. It disproves any uniform asymptotic coercivity principle under the stated observation budget, but it does not produce one orientation whose defects vanish at every sufficiently large horizon.

Third, (4) is strictly one-sided. Nothing here proves coercivity at `K_T M_T asymp r_T`, and no sharpness claim is made for the linear-rank scale.

Fourth, the tests are nonnegative normalized linear observations of the edge-defect magnitude. Signed tests can exploit cancellation and amplification differently and are outside the theorem. Nonlinear joint tests of many edges are also not covered merely by counting their output cells.

Fifth, the source is a matched control, not a proposed model of the physical Möbius coefficients. The priorities and colors need not be recoverable from Farey data. The theorem says that the tested ancestry information does not determine the physical source; it does not say the actual Farey/Möbius source possesses hidden random priorities.

Sixth, the result does not contradict FD-110. That finding concerns the **physical** coefficient law under deterministic least-prime-factor linear bookkeeping and shows a collapse to commuting rough-sieve resolvents. FD-144 instead uses a random global prime order only to construct an alternative coefficient source with small insertion sensitivity. It is a matched-control obstruction, not a new linear decomposition of the physical source.

Finally, full source reconstruction remains an escape. A test family that effectively labels every squarefree parent can rule out this control, but FD-142 explains why such an escape is circular unless its resolving capacity is genuinely derived from the Farey endpoint rather than imported as source identity.

## 11. Prior-art and novelty audit

The selector identity itself is classical. Min-wise independent permutations were developed by Andrei Z. Broder, Moses Charikar, Alan M. Frieze and Michael Mitzenmacher, *Min-Wise Independent Permutations*, Journal of Computer and System Sciences **60** (2000), 630--659, DOI `10.1006/jcss.1999.1690`. For a uniformly random order on a finite set, every element is the minimum with probability the reciprocal of the set size. Equivalently, the MinHash collision probability of two sets is their Jaccard similarity; for a `k`-element set and the same set with one new element, the selected minimum changes with probability `1/(k+1)`.

No novelty is claimed for min-wise sampling, the Jaccard/MinHash identity, Markov's inequality, or Borel--Cantelli. Equation (13) is also proved directly here and does not require an external theorem.

The durable delta is the ancestry splice: attach an independent prime color to the min-wise selected factor, multiply by Möbius support, and use the exact insertion sensitivity `1/(2(k+1))` to defeat an arbitrary family of source-independent weighted ancestry probes with total budget `o(r_T)`, while a single frozen orientation remains macroscopically different from Möbius on an observed parent domain. A targeted prior-art search did not identify this Farey coefficient-coercivity formulation or its linear-rank observation-budget consequence.

Because the proof is elementary after the construction is specified, the min-wise literature is a prior-art boundary rather than a load-bearing dependency; no new `SOURCES.md` theorem anchor is required.

## 12. Next live question

FD-144 moves the elementary coefficient-side obstruction from

\[
o(\sqrt{r_T})
\quad\text{to}\quad
o(r_T).
\tag{35}
\]

For the central Farey regime, this means `o(log log T)` arbitrary nonnegative ancestry probes remain noncoercive. The next useful distinction is now sharper.

One route is to ask whether the min-wise construction itself can survive **linear-rank or mildly superlinear-rank** test families by exploiting dependency/local structure instead of a first-moment union budget. A matched control at that scale would push the lower frontier again.

The opposite route is more source-specific: identify a Farey/Fourier-derived observable whose effective ancestry information is at least linear in the available factor rank and prove that it excludes min-wise selector sources without becoming a source label. Such a theorem would be the first positive evidence that the intermediate regime above FD-144 is qualitatively different.

A destination-side Fourier-skeleton coercivity theorem remains an independent escape because it need not recover the coefficient source through ancestry probes at all.