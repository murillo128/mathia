# WI-003 — the Yang--Yang cell truncation does not reduce moduli as written

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` for the Yang--Yang higher-moment arithmetic transport in the pinned manuscripts below. The external unconditional claims have since been **retracted**, as documented in [WI-456](WI-456-retracted-moment-transport-leaves-only-a-conditional-density-capstone.md). The literal cutoff obstruction remains valid; it is not a proof that every possible fourth-moment or density-one theorem is false, nor an independent proof of the retraction notice's reported Proposition R.

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

The successor manuscript retains this ambiguity. Interpreting the truncation with the manuscript's only explicit definition of `ell_1` makes the claimed modulus reduction fail.

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

Therefore this is not merely a typo already repaired between the finite-moment and density-one versions. At the pinned pre-retraction revisions, the all-order arithmetic schema inherits the same unresolved base-case bridge.

The conditional density-one capstone is separate from this defect; WI-456 states sufficient moment, model, and counting hypotheses explicitly. The present finding does not attack that conditional implication. It identifies a failure of the pinned manuscript's proof even at the first decisive fourth-moment rung.

## 6. Adversarial checks and possible escape routes

Several weaker interpretations do not resolve the issue.

- Treating `ell_1` as the global normalization cannot yield a cell-dependent truncation, as Section 2 shows.
- Inferring that `ell_1` must secretly mean `r`, `q`, `rq`, `lcm(b_1,b_2)`, or another modulus is not legitimate: these choices have different multiplicities, weights, and implications for the joint modulus, and the manuscript must prove the corresponding ledger identity.
- The archived label "D1 truncation" and the repository's machine certification do not by themselves fill the analytic bridge. The pre-retraction authors' grading of that layer as unformalized and pending review has been superseded by the withdrawal of the unconditional claims.
- Numerical agreement of finite ledgers with the CUE/sine-kernel model cannot prove an asymptotic absolute tail bound.

A different proof could in principle introduce an arithmetic level variable satisfying all five obligations in Section 4. Such a proof would be new evidence requiring its own audit; it would not erase the literal failure of the pinned manuscripts. The present obstruction is not a no-go theorem for higher moments themselves.

## 7. Prior-art and novelty assessment

The underlying analytic tools -- Siegel--Walfisz, Vaughan bounds, divisor estimates, and truncation of arithmetic sums -- are classical. No novelty is claimed for them.

The official [retraction notice](https://github.com/JoshuaHKU/zeta-density-one-reproduction/blob/ac851520f1d135a56d2911ff512011feab2a32dd/RETRACTION.md) withdraws the unconditional moment tier from the fourth moment upward. It reports an essential analytic gap but does not identify that gap with the literal cutoff failure proved here. These are distinct evidence claims: the notice establishes withdrawal, while the displayed definitions establish this particular obstruction.

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

The Yang--Yang exact-moment manuscripts supply no unconditional improvement to the independent baseline in [[research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier|WI-001]]. Their retraction leaves the literal cutoff obstruction intact and preserves the distinction between an algebraic certificate and its missing arithmetic input. The claimed `13/18`, `0.7962`, order-14, and density-one rungs cannot be used as established arithmetic evidence through this source.

The five obligations in Section 4 are necessary checks on any future proof that actually uses such a cellwise truncation, not a standing instruction to repair the withdrawn submission. A different higher-moment argument must be judged on its own exact source identities and estimates. WI-456 preserves the conditional moment-to-density implication and the remaining gap between density one and individual-zero exclusion.
