# MC-452 — Raw truncated Möbius is not a standard well-factorable weight

**Status:** `EXACT-DERIVED` · `CLASSICAL-DEFINITION-CONSEQUENCE` · `NEGATIVE/OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Let

\[
\lambda_Q(n):=\mu(n)\mathbf 1_{n\le Q}.
\]

Then the raw truncated Möbius sequence is **not**, in general, a well-factorable sequence of level `Q` in the standard sieve-theoretic sense.

More precisely, for every prime `p>=3`, take

\[
Q=(p-1)^2,
\qquad
Q_1=Q_2=p-1.
\]

If `lambda_Q` were well factorable of level `Q`, the factorization `Q=Q_1Q_2` would admit bounded sequences `gamma_1,gamma_2`, supported respectively on `[1,Q_1]` and `[1,Q_2]`, such that

\[
\lambda_Q=\gamma_1*\gamma_2.
\tag{1}
\]

But `p<=Q`, so

\[
\lambda_Q(p)=\mu(p)=-1.
\tag{2}
\]

On the other hand, since `p` is prime,

\[
(\gamma_1*\gamma_2)(p)
=
\gamma_1(1)\gamma_2(p)+\gamma_1(p)\gamma_2(1)=0,
\tag{3}
\]

because both factors vanish at `p>p-1`. Equations `(2)` and `(3)` contradict `(1)`.

Therefore

\[
\boxed{
\mu(n)\mathbf 1_{n\le (p-1)^2}
\text{ is not well factorable of level }(p-1)^2
}
\]

for every prime `p>=3`.

This kills the naive continuation of `MC-409` in which one tries to replace the auxiliary well-factorable upper-sieve weight by **raw truncated Möbius itself** and then import standard well-factorable dispersion estimates unchanged. If factorability is useful for the Möbius problem, it must enter through an auxiliary weight, decomposition, majorant, smoothing, or another retained source-frame representation; it is not an intrinsic standard well-factorability property of the finite Möbius prefix.

No bound for `M(x)` follows.

## 1. General support obstruction

The proof uses only the support part of the classical definition and therefore gives a reusable lemma.

Let `lambda` be any arithmetic sequence. Suppose that for some factorization `Q=Q_1Q_2` one has

\[
\lambda=\alpha*\beta,
\qquad
\operatorname{supp}\alpha\subseteq[1,Q_1],
\qquad
\operatorname{supp}\beta\subseteq[1,Q_2].
\tag{4}
\]

If `r` is prime and

\[
r>\max(Q_1,Q_2),
\]

then

\[
\lambda(r)=\alpha(1)\beta(r)+\alpha(r)\beta(1)=0.
\tag{5}
\]

Hence any sequence carrying nonzero mass at such a prime cannot possess the requested convolution factorization for that split of the level.

For a balanced factorization `Q_1=Q_2=sqrt(Q)`, standard well-factorability therefore forces the coefficient sequence to vanish at every prime in `(sqrt(Q),Q]`. Raw truncated Möbius does the opposite: it equals `-1` at every such prime. The obstruction is thus structural and dense across the upper part of the support, not a boundary artifact at one specially chosen prime.

## 2. Relation to the retained-variable branch

`MC-409` showed that a **factorable variant of an upper linear-sieve weight** can preserve coefficient variables before scalarization and thereby exposes a legitimate bilinear representation for the prime-frame branch. The present result draws an important boundary around that observation.

The useful factorability in `MC-409` belongs to a deliberately constructed auxiliary sieve coefficient sequence. It cannot be transferred to the raw Möbius prefix merely because both objects are squarefree-supported and alternate signs. Standard well-factorability is a strong all-splits convolution property, and the balanced split already conflicts with the prime support of truncated Möbius.

This is consistent with the later `MC-451` obstruction to post-hoc recovery of factorable variables after fixed-lcm scalarization: in both cases, the useful variables must genuinely exist **before** the lossy step. Here the raw coefficient sequence never possessed the required all-splits convolution variables in the first place.

The surviving research question is therefore narrower:

> Can one place Möbius inside, or compare it to, an auxiliary representation whose factorable variables remain available long enough to yield cancellation without replacing the signed Möbius target by a sieve majorant too coarse to control `M(x)`?

This finding does not answer that question.

## 3. Prior art and novelty boundary

No novelty is claimed for the definition or for the elementary support consequence.

James Maynard, *Primes in arithmetic progressions to large moduli II: Well-factorable estimates*, Memoirs of the AMS **306** (2025), no. 1543; arXiv:`2006.07088`, Definition 1, defines a sequence `lambda_q` to be well factorable of level `Q` when **for every** factorization `Q=Q_1Q_2` it admits a convolution of two 1-bounded sequences supported on `q<=Q_1` and `q<=Q_2`, respectively. The same introduction explicitly notes that standard sieve weights are not generally well-factorable and recalls Iwaniec's modified factorable upper-sieve construction. See https://arxiv.org/abs/2006.07088.

The Mathia contribution here is only the explicit boundary check against the current Möbius branch: applying that standard definition to `mu(n)1_{n<=Q}` immediately rules out a tempting but invalid identification suggested by the successful auxiliary construction in `MC-409`.

## Boundaries and falsification tests

- **This is standard well-factorability only.** The result does not rule out weaker, one-split, approximate, averaged, smooth, or multi-stage factorizations of Möbius.
- **Auxiliary sieve weights survive.** It does not weaken `MC-409`; that finding intentionally uses a modified upper linear-sieve coefficient sequence designed to be a finite combination of well-factorable sequences.
- **A majorant is not Möbius.** Replacing `mu` by an upper-sieve weight can preserve the prime-frame architecture while destroying the signed cancellation observable needed for `M(x)`. Any transfer back to Möbius must be proved separately.
- **The coefficient bounds are irrelevant to the obstruction.** The contradiction already follows from support, so relaxing `|gamma_i|<=1` while retaining the standard support condition does not help.
- **The all-splits quantifier is load-bearing.** A decomposition for one favorable factorization does not establish standard well-factorability.
- **No analytic continuation or zero information is used.** The result is finite convolution algebra and has no RH input.

## Consequence for the research line

The factorable-weight frontier should not spend further effort trying to prove that a finite Möbius prefix itself satisfies the standard sieve definition. The live versions of the idea must instead specify **where the factorable variables come from** — for example an auxiliary sieve weight, a bounded decomposition of a Möbius sum, or a transformed bilinear object — and must preserve enough signed information that the final estimate still controls Möbius rather than only a positive majorant.

That distinction supplies a sharper first-kill test for future retained-variable candidates: before invoking a well-factorable theorem, verify the exact convolution-support property of the actual coefficient sequence being estimated, not of a neighboring sieve surrogate.