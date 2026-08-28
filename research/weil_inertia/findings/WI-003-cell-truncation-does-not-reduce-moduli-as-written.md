# WI-003 — the Yang--Yang cell truncation does not reduce moduli as written

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` for accepting the currently published Yang--Yang higher-moment arithmetic transport as a proof; `NEEDS-AUDIT` for whether the intended argument can be repaired by introducing and proving estimates for a distinct cell-dependent arithmetic parameter. This does **not** refute the intended fourth-moment theorem, the higher-moment constants, or the density-one conclusion; it isolates a load-bearing gap in the manuscripts as currently written.

## 1. Precise obstruction

The 17 August 2026 Yang--Yang manuscript and its 22 August density-one successor both define

\[
l=\log(T/2\pi),\qquad
\ell_1=l+2\log 2-1,
\]

so `ell_1` is a single global Riemann--von Mangoldt normalization depending only on `T`. In particular,

\[
\ell_1\asymp \log T.
\]

Later, the higher-moment truncation argument reuses the **same symbol** as though it were a positive cell-dependent arithmetic variable:

- a cell is said to be "at parameter `ell_1`";
- the number of prime-power tuples with "cell parameter `ell_1=ell`" is asserted to be divisor-bounded;
- the truncated ledger `F^(P)` is defined by restricting to cells with `ell_1 <= P`;
- the tail is estimated by summing a schematic weight

\[
\ell^{-k}\cdot \ell\cdot \ell^\varepsilon
\]

for `ell>P`;
- this is then used to conclude that only logarithmic-size moduli need be treated by the Siegel--Walfisz/Vaughan step.

No second definition of `ell_1` as a function of a cell, a prime-power tuple, `b_1,b_2`, `r,q`, a least common multiple, or another arithmetic modulus occurs before this use. A repository-wide code search for the phrase "cell parameter" in the public `zeta-0.7947-reproduction` source at commit `d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8` finds only the manuscript itself; the density-one successor at commit `acf2b3364f122dfcd3c8792cbab102444e67f7d0` retains the same truncation text.

Thus the ambiguity noted in WI-002 is not resolved by the successor manuscript. More strongly, interpreting the truncation with the manuscript's only explicit definition of `ell_1` makes the claimed modulus reduction fail.

## 2. Literal interpretation makes the truncation vacuous or total

The manuscripts take

\[
X=e^{\lambda l}\asymp T^\lambda
\]

for fixed `lambda>0`, and set the truncation threshold

\[
P=(\log X)^B\asymp (\log T)^B.
\]

But the explicitly defined `ell_1` is global and satisfies `ell_1 ~ log T`. Therefore the predicate

\[
\ell_1\le P
\]

is independent of the cell.

For any fixed `B>1`, eventually

\[
\ell_1<P.
\]

Hence **every cell survives** and

\[
F^{(P)}=F.
\]

The operation removes no large-modulus cell whatsoever. In particular, the stated consequence that only moduli at most a polylogarithmic threshold are consumed does not follow from this restriction.

For any fixed `0<B<1`, eventually

\[
\ell_1>P,
\]

so **no cell survives** and `F^(P)=0`. This is again not a cell-by-cell modulus truncation. At `B=1` the decision is still global, depending only on constants; it cannot separate large from small arithmetic cells.

Consequently, under the notation actually defined in the paper, there is no sum over distinct cell values `ell` and the displayed tail

\[
\sum_{\ell>P}\ell^{-k}\ell\ell^\varepsilon
\]

cannot be the decomposition of the ledger by that `ell_1`.

This is an exact syntactic/mathematical contradiction between the global definition and the later role assigned to the symbol, not a numerical concern or a request for additional exposition.

## 3. Why this is load-bearing

The fourth-moment route is advertised as avoiding large-modulus technology because this truncation first reduces the relevant arithmetic to logarithmic-size moduli, after which the lock variance is transported into a spectral frame and closed with Siegel--Walfisz and Vaughan estimates.

Without a valid cell-dependent truncation, that implication is unavailable. The public manuscript itself later notes that a direct character expansion has to be lifted to a joint modulus of size roughly `rq`; therefore controlling which `r,q` occur is not cosmetic. The argument needs a theorem that genuinely removes the large arithmetic cells before invoking estimates whose useful uniformity is restricted to the asserted range.

Accordingly, the chain

\[
\text{prime-side fourth trace expansion}
\Longrightarrow
m_4=13/4
\Longrightarrow
13/18
\]

is not established by the manuscript **as written**. The same issue propagates to the fifth/sixth moment headline and to the all-order density-one tower, because the successor reuses this truncation mechanism rather than replacing it with a separately defined modulus reduction.

This does not invalidate the exact rational model-side moment values, the Chebyshev--Markov/Christoffel consumption certificates, or the finite algebraic/Lean artifacts. Those are separate layers. The gap is specifically in the analytic transport from the prime-side trace ledger to the claimed limiting moments.

## 4. What a repair must actually prove

A repair cannot consist only of renaming the second occurrence of `ell_1`. It must introduce an explicit cell-dependent arithmetic quantity, say `M(c)`, and reconnect every displayed estimate to the original trace expansion.

At minimum, a valid repair must establish all of the following.

1. **Definition from the ledger.** Give `M(c)` explicitly in terms of the prime-power/modulus data of a cell and derive from the trace expansion the claimed decay weight in `M(c)`; if the true weight is not `M(c)^{-k}`, use the correct exponent and factors.
2. **Cell-mass estimate.** Prove the absolute cell contribution grows slowly enough in `M(c)` to make the tail summable after all lock, window, singular-series, and normalization factors are restored.
3. **Multiplicity estimate.** Prove the number of relevant prime-power tuples with fixed `M(c)=M` is divisor-bounded, or replace that claim by the correct counting estimate.
4. **Modulus implication.** Prove that `M(c)<=P` actually forces every modulus passed to the Siegel--Walfisz/Vaughan stage into the required polylogarithmic range. A bound on an unrelated product, gcd, or normalized volume is insufficient unless the needed implication is shown.
5. **Two-sided absolute tail.** Sum the discarded cells on absolute values with enough saving to survive every remaining outer sum. The power saving must be derived before using cancellation from the very arithmetic theorem the truncation is meant to enable.

Only after these steps does it make sense to audit the subsequent Parseval/product transport and recover `m_4=13/4`.

## 5. The successor manuscript strengthens, rather than removes, the audit obligation

The 22 August density-one manuscript again starts with the global definition

\[
\ell_1=\log(T/2\pi)+2\log2-1
\]

and again states a cell-mass lemma "at parameter `ell_1`", a multiplicity lemma with "cell parameter `ell_1=ell`", and a truncation `ell_1<=P` followed by the same `ell^{-k} ell ell^epsilon` tail bookkeeping.

Therefore this is not merely a typo already repaired between the finite-moment and density-one versions. At the current public revisions, the all-order arithmetic schema inherits the same unresolved base-case bridge.

This matters epistemically because the density-one capstone in WI-002 is structurally coherent **conditional on** having every fixed-order arithmetic moment theorem. The present finding does not attack that capstone. It says that the manuscript has not yet supplied a valid written proof of the arithmetic moment theorem even at the first decisive fourth-moment rung.

## 6. Adversarial checks and possible escape routes

Several weaker interpretations do not resolve the issue.

- Treating `ell_1` as the global normalization cannot yield a cell-dependent truncation, as Section 2 shows.
- Inferring that `ell_1` must secretly mean `r`, `q`, `rq`, `lcm(b_1,b_2)`, or another modulus is not legitimate: these choices have different multiplicities, weights, and implications for the joint modulus, and the manuscript must prove the corresponding ledger identity.
- The archived label "D1 truncation" and the repository's machine certification do not by themselves fill the analytic bridge. The authors explicitly grade the analytic consumption layer as unformalized and pending external review.
- Numerical agreement of finite ledgers with the CUE/sine-kernel model cannot prove an asymptotic absolute tail bound.

A genuine escape remains possible: there may be an intended arithmetic level variable in the authors' underlying ledger for which all five obligations in Section 4 are true. If such a variable and proof are supplied, this finding should be superseded by a new audited result; the current obstruction is to the published proof, not a no-go theorem for higher moments themselves.

## 7. Prior-art and novelty assessment

The underlying analytic tools -- Siegel--Walfisz, Vaughan bounds, divisor estimates, and truncation of arithmetic sums -- are classical. No novelty is claimed for them.

No independent review resolving this notation/transport issue was located, and the public repositories currently contain no issue discussion establishing the missing definition. Both preprints self-classify their analytic chains below externally reviewed theorem status.

The Mathia contribution here is the explicit falsification test obtained by reading the claimed truncation literally and carrying its scales through:

\[
\boxed{
\ell_1\asymp\log T,\quad P\asymp(\log T)^B
\quad\Longrightarrow\quad
\ell_1\le P\text{ is a global predicate, not a modulus cutoff.}
}
\]

That observation sharply localizes the burden of proof and prevents exact-rational/model-side certificates from being mistaken for certification of the missing arithmetic transport.

## 8. Consequence for `weil_inertia`

The verified unconditional baseline therefore remains the Alpöge--Furman `0.672500703679...` result. The Yang--Yang moment tower remains a high-value research lead because, if repaired, it supplies exactly the defect-to-zero mechanism sought by this line; but its claimed `13/18`, `0.7962`, finite order-14, and density-one rungs must not be used as established arithmetic evidence on the strength of the present manuscripts.

The next highest-value audit is now narrower than WI-002's original target. Before recomputing the fourth-moment constant, reconstruct the cell ledger far enough to identify the intended arithmetic level variable and prove or disprove the five repair obligations above. If that succeeds, the rest of the fourth-moment transport becomes meaningful to audit. If it fails, the proposed unconditional higher-moment escape from WI-001 is blocked at a precise prime-side truncation step rather than at the later matrix/moment certificate.