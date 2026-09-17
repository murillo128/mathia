# FD-171 — Midpoint temporal sensing has zero exact redundancy

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** sparse temporal acquisition / exact nullspace / permanent-source obstruction / information-boundary
- **Depends on:** FD-117, FD-166, FD-169, FD-170
- **Classification:** `EXACT-DERIVED + TEMPORAL-ACQUISITION + EXPLICIT-KERNEL + PERMANENT-SOURCE + NEGATIVE/ROUTE-RESTRICTION`

## Claim

`FD-170` shows that the complete consecutive midpoint history is an invertible temporal sensor for the formal source. The converse is sharp: over the unrestricted normalized arithmetic-source class, **none of those horizon samples is redundant**.

Let

\[
P_a(H):=\mathcal D_{H,a}(1/2),
\qquad a(1)=1,
\tag{1}
\]

and let `S` be any subset of the horizons `{2,3,...}`. Then the observation map

\[
a\longmapsto (P_a(H))_{H\in S}
\tag{2}
\]

is injective on normalized arithmetic functions if and only if

\[
\boxed{S=\{2,3,4,\ldots\}.}
\tag{3}
\]

More strongly, if a single horizon `k>=2` is omitted, there is an explicit **fixed, integer-valued, permanent** perturbation of the Möbius source that is invisible at every other midpoint horizon.

Write

\[
u(n)=1_{2\nmid n},
\qquad
\mu_{\rm odd}(n)=\mu(n)1_{2\nmid n},
\tag{4}
\]

so `u^{-1}=mu_odd` under Dirichlet convolution by `FD-170`. Let `e_k` denote the arithmetic pulse at `k`, and define

\[
\boxed{
\delta a_k
:=
\mu_{\rm odd}*(e_k-e_{k+1}).
}
\tag{5}
\]

Equivalently,

\[
\boxed{
\delta a_k(n)
=
1_{k\mid n}\,\mu_{\rm odd}(n/k)
-
1_{k+1\mid n}\,\mu_{\rm odd}(n/(k+1)).
}
\tag{6}
\]

Then `delta a_k(1)=0`, `delta a_k` is nonzero and integer-valued, and for

\[
a_k:=\mu+\delta a_k
\tag{7}
\]

one has

\[
\boxed{
P_{a_k}(H)=P_\mu(H)
\quad\text{for every }H\ne k,
}
\tag{8}
\]

while

\[
P_{a_k}(k)-P_\mu(k)=-\frac12.
\tag{9}
\]

Thus even observing **all horizons except one** fails to determine a permanent formal source.

There is also an exact finite-prefix rank statement. For `K>=2` and `S subset {2,...,K}`, the linear map

\[
(\delta a(2),\ldots,\delta a(K))
\longmapsto
\bigl(P_{\mu+\delta a}(H)-P_\mu(H)\bigr)_{H\in S}
\tag{10}
\]

has

\[
\boxed{
\operatorname{rank}=|S|,
\qquad
\dim\ker=K-1-|S|.
}
\tag{11}
\]

So midpoint temporal acquisition has exactly one independent scalar constraint per observed horizon and no hidden exact redundancy that sparse sampling can exploit over the unrestricted formal source class.

## 1. In the convolution coordinates, midpoint observations are cumulative sums

Let

\[
E_H:=P_a(H)-P_\mu(H),
\qquad E_0:=0,
\qquad
\delta a:=a-\mu.
\tag{12}
\]

`FD-170` gives

\[
E_H-E_{H-1}
=-\frac12(u*\delta a)(H).
\tag{13}
\]

Introduce the invertible source coordinate

\[
b:=u*\delta a.
\tag{14}
\]

Then

\[
\boxed{
E_H=-\frac12\sum_{n\le H}b(n).
}
\tag{15}
\]

The sparse temporal acquisition problem is therefore completely transparent in `b`-coordinates: observing the midpoint at horizon `H` reveals one prefix sum of `b`. Consecutive horizons recover each individual `b(H)` by first differencing, but deleting horizon `k` deletes exactly the prefix equation that separates `b(k)` from the compensating change at `k+1`.

Choose

\[
b_k=e_k-e_{k+1}.
\tag{16}
\]

Its cumulative sum is

\[
\sum_{n\le H}b_k(n)
=
\begin{cases}
0,&H<k,\\
1,&H=k,\\
0,&H\ge k+1.
\end{cases}
\tag{17}
\]

Equation (15) immediately proves that its midpoint response is supported at the single horizon `k`. Since `u` is Dirichlet-invertible,

\[
\delta a_k=u^{-1}*b_k
=\mu_{\rm odd}*(e_k-e_{k+1}),
\tag{18}
\]

which proves (5)--(9). In particular, the invisible alternative is not a cutoff-dependent control that changes when a larger horizon is requested: it is one permanent arithmetic function valid simultaneously at every observed horizon.

This gives the global classification. If every horizon `H>=2` is observed, `FD-170` recovers every coefficient under the normalization `a(1)=1`. If any `k>=2` is not observed, (18) gives a nonzero normalized source perturbation invisible on the entire observation set. Hence (3) is an if-and-only-if statement.

## 2. Every finite selected horizon contributes exactly one row of rank

For finite-prefix acquisition, expand (15) back in the original source coordinates. Since

\[
b(q)=\sum_{\substack{m\mid q\\m\text{ odd}}}\delta a(q/m),
\tag{19}
\]

we have

\[
E_H
=-\frac12
\sum_{j\le H}
\delta a(j)
\#\{m\le H/j:m\text{ odd}\}.
\tag{20}
\]

After fixing `delta a(1)=0`, the full matrix with rows `H=2,...,K` and columns `j=2,...,K` is lower triangular in the ordinary ordering. Its diagonal coefficient is exactly `-1/2`, because when `j=H` only `m=1` contributes.

Now select any rows indexed by `S={H_1<...<H_r}` and the same columns `H_1,...,H_r`. The resulting `r x r` submatrix is again lower triangular with diagonal `-1/2`. Therefore every selected row is independent and

\[
\operatorname{rank}=r=|S|.
\tag{21}
\]

Rank-nullity gives (11). This is stronger than saying that consecutive observations are sufficient: it says that, for the unrestricted `K-1` dimensional normalized source prefix, **there is no exact temporal oversampling to discard**. A density-`alpha` horizon set supplies only density-`alpha` rank unless additional source restrictions or extra spatial measurements are introduced.

## 3. Contrast with complete-field permanent-source rigidity

The result sharply separates midpoint temporal sensing from the complete-field theorem `FD-166`. A complete field at horizon `H` reveals the floor-quotient staircase and therefore a consecutive source prefix of length about `sqrt(H)`. Consequently any unbounded family of complete fields eventually exposes every fixed source coordinate, however sparse the horizons are.

The midpoint path has the opposite information geometry. At each horizon it contributes only one new triangular equation. Later midpoint samples do **not** subsume an omitted earlier equation: the pulse pair `e_k-e_{k+1}` changes one cumulative prefix and then cancels forever. Hence a single missing temporal row leaves a permanent null direction even if every larger horizon is observed.

This also clarifies the role of the apparently stationary physical midpoint. For Möbius, `P_mu(H)=1/2` for `H>=2`; `FD-170` showed that the changing operator nevertheless makes the complete consecutive history source-complete. The present theorem says exactly how fragile that completeness is: its information resides in the full set of horizon equations, not in a redundant encoding of a smaller source statistic.

## 4. Self-adversarial audit and source-faithfulness boundary

The explicit kernel survives the main obvious attacks. First, normalization is preserved: for `k>=2`, (6) gives `delta a_k(1)=0`, so `a_k(1)=1`. Second, the perturbation is genuinely nonzero because `delta a_k(k)=1`, while convolution by `u` recovers exactly `e_k-e_{k+1}`. Third, it is integer-valued because `mu_odd` is integer-valued. Direct finite-prefix matrix checks agree with the analytic triangular argument, but no computation is load-bearing.

There is, however, an important boundary. The perturbation (6) generally has infinite support and does not preserve the full Möbius architecture: `a_k` need not remain in `{-1,0,1}`, need not vanish exactly on nonsquarefree integers, and need not be multiplicative. Therefore (3) is a sharp impossibility theorem for the **formal arithmetic-source model** of `FD-117`, not yet for a source-faithful Möbius admissible class.

That distinction is precisely where a nontrivial sparse-acquisition theorem could still live. If ternary squarefree support, multiplicativity, a finite-tail condition, or another genuinely arithmetic compatibility destroys the pulse-pair null directions, then sparse horizons may recover more than their raw linear rank suggests. Conversely, producing a source-faithful analogue of (18) would show that the obstruction survives much deeper into the arithmetic architecture.

The exact kernel also means that no noise-stability theorem can rescue unrestricted sparse midpoint acquisition: along (18), the observation distance is literally zero. Stability becomes meaningful only after the admissible source class is narrowed or additional measurements are added.

## 5. Representation audit, prior art, and dependency ledger

The cumulative-sum/nullspace part is generic linear algebra. For any invertible transform from source coefficients to increments, observing only selected cumulative prefixes has one exact degree of freedom per omitted row. No novelty is claimed for that abstraction, for Dirichlet convolution, or for Möbius inversion.

The Farey-specific splice is `FD-170`: the exact midpoint horizon increment of the source-controlled Farey field is `-(1/2)(u*a)(H)` with `u` the odd indicator. That identity makes the generic one-hole cumulative kernel into the explicit arithmetic perturbation (5) and yields the permanent-source comparison with `FD-166`.

A focused prior-art search around Farey midpoint ranks, sparse horizon observation and Möbius/Dirichlet inversion recovered the standard midpoint symmetry and standard Dirichlet-convolution inversion, but no direct statement of the one-missing-horizon kernel for this source-controlled Farey observation model. The existing García 2025 rank/local-discrepancy anchor in `SOURCES.md` remains the relevant external boundary; no new external theorem is load-bearing, so `SOURCES.md` needs no update.

Dependency ledger: the exact source-controlled field comes from `FD-117`; permanent complete-field rigidity used for contrast is `FD-166`; the acquisition-model distinction from arbitrary same-horizon mixing is `FD-169`; and the only substantive algebraic input for the new proof is the midpoint increment/convolution identity and inverse established in `FD-170`. The rest of the proof is finite triangular linear algebra plus the explicit pulse-pair construction above.

Clue transition check: no accepted clue changes status. This result resolves the unrestricted sparse-midpoint branch opened by `FD-170`; it does not settle the surviving gap-order or nonsquarefree-occupation clue programs.

## Research consequence

The exact sparse/nonconsecutive temporal question is now closed over the unrestricted formal source space: **there is no compressed midpoint-only sampling pattern with exact injectivity**. To remove any horizon, one must pay for information somewhere else.

The live acquisition frontier should therefore move to one of two genuinely narrower problems: impose source-faithful arithmetic constraints and ask whether they kill the pulse-pair kernel, or augment sparse temporal samples with bounded/local spatial measurements and determine the minimum mixed space-time row set needed for a useful source prefix. Only after that kernel is fixed does it make sense to study stable inversion or information-budget lower bounds.

None of this supplies new Möbius cancellation or an RH-critical Franel--Landau estimate. It is a source-architecture restriction: it prevents the research program from treating sparse midpoint histories as if the consecutive inversion of `FD-170` survived automatically.

## Related findings

- `FD-117` — complete source-controlled Farey field is an affine transform of the quotient cumulative source.
- `FD-166` — any unbounded family of exact complete fields rigidifies a permanent source to Möbius.
- `FD-169` — unrestricted same-horizon mixed measurements reduce exact recovery to target rank.
- `FD-170` — every consecutive midpoint horizon supplies the odd-divisor convolution increment and yields exact source inversion.
