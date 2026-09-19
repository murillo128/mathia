# AF-436 — Exact Euler coefficients retain the shell ladder at exponentially shrinking resolution

**Status:** `EXACT-DERIVED`, `CLASSICAL-MOMENT-STRUCTURE`, `ARITHMETIC-FIDELITY`, `MULTISCALE-RECOVERY`, `STABILITY-THRESHOLD`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
h(x)=-\log\!\left(\frac{1-e^{-x}}{x}\right),
\qquad R=2\pi,
\]

and write its even Taylor coefficients as

\[
h(x)=\frac{x}{2}+\sum_{k\ge1} c_{2k}x^{2k},
\qquad
c_{2k}=\frac{(-1)^k\zeta(2k)}{kR^{2k}}.
\]

AF-434 showed that the fixed-packet full-column saddle does **not** transport the source shell index carried by

\[
\zeta(2k)=\sum_{j\ge1}j^{-2k}
\]

into its leading packet rate. The stronger fidelity statement is more precise:

> **The exact infinite coefficient sequence has not lost the shell ladder. It retains every shell recursively, but shell `m` lives at residual scale `m^{-2k}` after shells `1,\ldots,m-1` have been removed.**

Define the normalized coefficient moments

\[
s_k:=(-1)^k kR^{2k}c_{2k}=\zeta(2k)
\]

and, for fixed `m>=1`, the peeled residual

\[
r_{m,k}
:=s_k-\sum_{j=1}^{m-1}j^{-2k}
=\sum_{j=m}^{\infty}j^{-2k}.
\]

Then

\[
\boxed{
1\le m^{2k}r_{m,k}
\le 1+\frac{m}{2k-1}
}
\]

and hence

\[
\boxed{
\lim_{k\to\infty}m^{2k}r_{m,k}=1,
\qquad
\lim_{k\to\infty}r_{m,k}^{-1/(2k)}=m,
\qquad
\lim_{k\to\infty}\frac{r_{m,k+1}}{r_{m,k}}=m^{-2}.
}
\]

Thus, once the first source radius `R` is fixed, the exact coefficient sequence recursively recovers the entire radial shell ladder

\[
R,\ 2R,\ 3R,\ldots .
\]

The recovery is, however, increasingly ill-conditioned. If normalized coefficient errors are `e_k`, then a sufficient condition for stable recovery of shell `m` after exact peeling of earlier shells is

\[
|e_k|=o(m^{-2k}).
\]

Conversely, under a worst-case coordinatewise error budget satisfying

\[
\varepsilon_k\ge m^{-2k}
\]

for all sufficiently large `k`, the presence of shell `m` is not uniformly identifiable within the natural positive shell-sum control class: deleting exactly that shell changes the normalized sequence by precisely `m^{-2k}`, which lies inside the allowed tolerance.

So the shell hierarchy defines an explicit **resolution ladder**. Exact aggregation preserves provenance; subsequent asymptotic compression can destroy it because the distinguishing residuals shrink exponentially with shell depth.

## Exact derivation

The Euler product identity used in AF-434 is

\[
\frac{1-e^{-x}}{x}
=e^{-x/2}\prod_{j\ge1}\left(1+\frac{x^2}{R^2j^2}\right),
\qquad R=2\pi.
\]

Taking `-log` and expanding for `|x|<R` gives

\[
\begin{aligned}
h(x)
&=\frac{x}{2}
-\sum_{j\ge1}\log\left(1+\frac{x^2}{R^2j^2}\right)\\
&=\frac{x}{2}
+\sum_{k\ge1}\frac{(-1)^k}{kR^{2k}}
\left(\sum_{j\ge1}j^{-2k}\right)x^{2k}.
\end{aligned}
\]

Therefore

\[
c_{2k}=\sum_{j\ge1}c_{2k}^{[j]},
\qquad
c_{2k}^{[j]}=\frac{(-1)^k}{kR^{2k}}j^{-2k},
\]

and normalization removes the common analytic radius and the harmless polynomial factor `1/k`:

\[
s_k=(-1)^k kR^{2k}c_{2k}
=\sum_{j\ge1}j^{-2k}.
\]

For fixed `m`, isolate the largest remaining term:

\[
r_{m,k}=m^{-2k}+\sum_{j=m+1}^{\infty}j^{-2k}.
\]

Since `x^{-2k}` is positive and decreasing,

\[
\sum_{j=m+1}^{\infty}j^{-2k}
\le \int_m^\infty x^{-2k}\,dx
=\frac{m^{1-2k}}{2k-1}.
\]

Hence

\[
m^{-2k}
\le r_{m,k}
\le m^{-2k}\left(1+\frac{m}{2k-1}\right),
\]

which proves

\[
m^{2k}r_{m,k}\to1.
\]

Taking `2k`-th roots gives

\[
r_{m,k}^{-1/(2k)}	o m,
\]

and applying the same asymptotic at `k` and `k+1` gives

\[
\frac{r_{m,k+1}}{r_{m,k}}	o m^{-2}.
\]

No analytic continuation, zero information, prime asymptotic, or numerical input is used in this derivation.

## Recursive shell recovery

The result gives an explicit recovery procedure from the **exact** coefficient sequence.

First, AF-435 identifies the coefficient radius from root growth:

\[
\lim_{k\to\infty}|c_{2k}|^{-1/(2k)}=R.
\]

After fixing `R`, form `s_k`. The largest atom in the power-sum representation is `1`, corresponding to shell `R`. Remove it. The residual

\[
s_k-1=\sum_{j\ge2}j^{-2k}
\]

has root scale `1/2`, so it identifies shell `2R`. Remove `2^{-2k}`. The next residual has root scale `1/3`, and so on.

Equivalently, in the variable

\[
\lambda_j=j^{-2},
\]

the normalized coefficients are power moments

\[
s_k=\sum_{j\ge1}\lambda_j^k.
\]

The peeling operation repeatedly extracts the largest remaining atom. In this particular shell system the atom weights are all one, and the atoms accumulate only at zero.

This means that the phrase "aggregation loses the shell index" requires a category qualifier. The scalar coefficient `c_{2k}` at one fixed order does not carry an explicit shell label, and the packet saddle of AF-434 does not transport one. But the **entire exact sequence across `k`** contains enough relational information to reconstruct all shell locations.

## Stability and the shell-resolution threshold

Exact recoverability and stable recoverability are different fidelity questions.

Suppose the normalized moments are observed as

\[
\widetilde s_k=s_k+e_k
\]

and assume the earlier shells `1,\ldots,m-1` have already been identified and peeled exactly. The observed residual is

\[
\widetilde r_{m,k}=r_{m,k}+e_k.
\]

Because

\[
r_{m,k}=m^{-2k}(1+o(1)),
\]

the sufficient condition

\[
|e_k|=o(m^{-2k})
\]

implies

\[
\frac{\widetilde r_{m,k}}{r_{m,k}}\to1,
\]

so both the root estimator and the scaled-amplitude estimator survive:

\[
\widetilde r_{m,k}^{-1/(2k)}\to m,
\qquad
m^{2k}\widetilde r_{m,k}\to1.
\]

A convenient stronger root-scale condition is

\[
\limsup_{k\to\infty}|e_k|^{1/(2k)}<\frac1m.
\]

It forces the perturbation to decay exponentially faster than the shell-`m` signal.

There is also a direct worst-case obstruction. Compare

\[
s_k=\sum_{j\ge1}j^{-2k}
\]

with the positive shell control in which shell `m` is deleted:

\[
s_k^{(-m)}=s_k-m^{-2k}.
\]

Their coordinatewise difference is exactly

\[
|s_k-s_k^{(-m)}|=m^{-2k}.
\]

Therefore any observation model that allows arbitrary errors of at least this size cannot uniformly distinguish "shell `m` present" from "shell `m` absent" over this matched control class. This is a minimax/worst-case statement about that error model; it does **not** say that every perturbation of size `m^{-2k}` destroys recovery.

In raw Taylor-coefficient units, the `m`-th shell contribution is

\[
|c_{2k}^{[m]}|
=\frac{1}{k(mR)^{2k}}.
\]

Thus preserving shell `m` directly at coefficient level requires accuracy on an exponentially finer scale as `m` grows. The polynomial factor `1/k` is secondary to the exponential radius `(mR)^{-2k}`.

## What the fixed-packet saddle forgets

AF-434 obtained, for fixed packet depth `r`, the zeta factor

\[
Z_{n,r}
=
\frac{\prod_{u=1}^{r}\zeta(2(n+u))}
{\prod_{u=1}^{r}\zeta(2u)}
=
\frac{1+O_r(4^{-n})}
{\prod_{u=1}^{r}\zeta(2u)}.
\]

The `4^{-n}` correction is not arbitrary: it is exactly the scale of the first shell remaining after shell `1` dominates, namely shell `2`.

Passing to the packet root-rate removes it:

\[
\frac1n\log(1+O_r(4^{-n}))\to0.
\]

The same phenomenon repeats deeper in the ladder. After peeling shells `1,\ldots,m-1`, shell `m` appears at scale `m^{-2n}`. Any compression that retains only the leading `n`-th-root/exponential packet rate but discards such additive residual scales cannot transport the shell label, even though the exact pre-compression coefficient sequence contains it.

This sharpens the boundary in AF-434:

- **exact coefficient sequence:** shell-faithful, recursively;
- **finite or coarse scalar summaries:** generally not enough without a resolution theorem;
- **fixed-packet leading saddle rate:** shell-blind to the nested residual hierarchy.

So the failure is not at the coefficient aggregation map itself. It occurs when later compression quotients out the subleading exponential scales in which provenance is encoded.

## Moment-problem interpretation and prior art

The underlying recovery mechanism is classical moment mathematics, not a new inverse theorem.

Define the finite positive measure on `[0,1]`

\[
\mu=\sum_{j\ge1}j^{-2}\,\delta_{j^{-2}}.
\]

Then

\[
\int_0^1 t^n\,d\mu(t)
=\sum_{j\ge1}j^{-2(n+1)}
=\zeta(2n+2).
\]

Thus the shifted sequence `\zeta(2k)` is a Hausdorff moment sequence of a finite measure. The classical Hausdorff moment problem on a compact interval is determinate, so the full moment sequence determines the measure. The explicit peeling above is a much simpler specialization that exploits the isolated descending atoms `1,j^{-2},...` and exposes their individual conditioning scales.

Relevant prior art includes:

- F. Hausdorff, *Summationsmethoden und Momentfolgen I, II*, Math. Z. 9 (1921), the classical compact-interval moment theorem;
- J. A. Shohat and J. D. Tamarkin, *The Problem of Moments*, AMS Mathematical Surveys 1 (1943), a standard classical reference;
- A. Kazemi, H. R. Shahdoosti, and R. M. Mnatsakanov, *Hausdorff moment problem: Recovery of an unknown support for a probability density function*, J. Inverse Ill-Posed Probl. 25 (2017), 719–731, DOI `10.1515/jiip-2016-0022`, which explicitly discusses support recovery from moment roots and consecutive-moment ratios, including noisy data;
- G. Plonka, *Prony methods for recovery of structured functions*, GAMM-Mitteilungen 37 (2014), 239–258, DOI `10.1002/gamm.201410011`, for the neighboring finite-exponential-sum recovery framework.

No novelty is claimed for moment determinacy, dominant-atom extraction, moment-root endpoint recovery, or Prony-type exponential reconstruction. The Arithmetic Fidelity contribution here is the **placement of the exact resolution boundary inside the current Euler-shell compression chain**: it identifies precisely where shell provenance still exists and the exponential accuracy needed for that provenance to survive later compression.

## Relation to AF-433, AF-434, and AF-435

AF-433 ruled out a freely chosen left-tail amplitude as an intrinsic source discriminator. AF-435 then supplied a canonical first-shell selector: coefficient root-neutrality uniquely fixes `c=R=2\pi`, hence `a=1` in the current packet normalization.

The present result extends that root idea from the first singular radius to the whole shell ladder. It does **not** repair the adjacent-packet cancellation obstruction. In particular, AF-426 and AF-435 still imply that the source-selected amplitude `a=1` does not yield exact square-packet cancellation in the current determinant mechanism.

Nor does this contradict AF-434. AF-434 states that the current full-column packet saddle does not transport the shell index into its leading rate. The present finding explains why: shell identity survives only in successively smaller residuals, while the packet saddle keeps a coarser asymptotic quotient.

The productive question therefore shifts from

> "Did coefficient aggregation already destroy shell provenance?"

to

> "Which downstream observables retain the nested residual scales `m^{-2k}`, and which asymptotic quotients erase them?"

That is a directly testable Arithmetic Fidelity question.

## Boundaries and failure modes

- The exact peeling formula uses the special positive shell decomposition `\zeta(2k)=\sum_j j^{-2k}`. Signed or complex shell weights can cancel, and their recovery needs a different analysis.
- The simple residual bounds are for fixed shell index `m` as `k\to\infty`. They do not give a uniform theorem when `m=m(k)` grows with `k`.
- Stability is stated after the common radius `R` and earlier shells are known exactly. Errors in estimating `R` or in previous peeling stages propagate and require a separate conditioning analysis.
- The deletion control proves a worst-case identifiability threshold for coordinatewise additive error. It is not a probabilistic lower bound for a specific noise law.
- The full exact coefficient sequence is much richer data than any finite prefix, finite jet, root-rate limit, determinant sign, or packet saddle. This result must not be used to infer that those coarser objects are shell-faithful.
- Recovering the deterministic shell ladder `mR` does not by itself recover rational primes, prove RH, or provide a new zero criterion. It only locates source provenance inside this particular analytic coefficient representation.
- The Hausdorff moment interpretation proves uniqueness at the full-moment level but does not supply uniform numerical conditioning. The explicit `m^{-2k}` hierarchy shows why exact uniqueness and robust recovery diverge sharply here.

## Decisive audit test

For any downstream transformation of these Euler coefficients that claims to retain source provenance:

1. identify the deepest shell `m` whose identity is claimed to survive;
2. determine whether the destination retains differences at the peeled residual scale `m^{-2k}` (equivalently raw coefficient scale `1/[k(mR)^{2k}]`);
3. compare against the matched control that deletes or changes shell `m` while preserving all earlier shells;
4. if the destination quotients the two controls together, shell-`m` provenance is lost at that layer;
5. if it separates them, quantify the separation margin and its behavior with `m` and `k` rather than relying only on exact injectivity.

This turns shell provenance into a graded fidelity test rather than a binary statement about whether `\zeta(2k)` "contains" the shells.

## Consequence for the line

Treat the Euler coefficient map and the packet saddle as **different compression layers**.

The exact coefficient sequence is recursively shell-faithful, but its provenance is stratified into exponentially shrinking scales. The current fixed-packet root-rate compression discards those scales and is therefore too coarse to transport the shell index found in AF-434.

Future source-facing work should either preserve these residual scales explicitly, prove a more stable relational encoding of the same shell information, or move to a target mechanism whose success does not require shell provenance after the packet-rate quotient.