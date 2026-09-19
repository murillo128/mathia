# AF-438 — Stieltjes generating transform transports the Euler shell ladder jointly

**Status:** `EXACT-DERIVED`, `CLASSICAL-IDENTITY`, `CLASSICAL-STIELTJES-TRANSFORM`, `ARITHMETIC-FIDELITY`, `JOINT-SHELL-CARRIER`, `NO-NOVELTY-CLAIM`

## Claim

AF-436 and AF-437 encode the normalized Euler coefficients as the power moments

\[
s_k=\zeta(2k)=\sum_{m\ge1}m^{-2k},
\qquad k\ge1,
\]

and show that recursive shell peeling exposes shell `m` only at residual scale `m^{-2k}`, with exponentially amplified sensitivity to errors in earlier shells.

That instability is not an exact information-theoretic obstruction to a **joint** shell representation. Define the ordinary generating transform

\[
F(z):=\sum_{k\ge1}s_k z^{k-1},
\qquad |z|<1.
\]

Then

\[
\boxed{
F(z)
=\sum_{m\ge1}\frac{1}{m^2-z}
=\frac{1-\pi\sqrt z\cot(\pi\sqrt z)}{2z}.
}
\]

The apparent singularity at `z=0` is removable, with `F(0)=\zeta(2)`. The right-hand side extends meromorphically to the whole complex plane and has simple poles exactly at

\[
z=m^2,\qquad m=1,2,\ldots,
\]

with

\[
\boxed{\operatorname*{Res}_{z=m^2}F(z)=-1.}
\]

Thus the complete shell ladder is represented **simultaneously** by the pole divisor of one meromorphic function. No earlier shell has to be estimated and subtracted before a later shell exists in the representation.

Equivalently, with the finite positive measure

\[
\mu=\sum_{m\ge1}m^{-2}\,\delta_{m^{-2}},
\]

one has

\[
F(z)=\int_{[0,1]}\frac{d\mu(t)}{1-zt}.
\]

So the normalized Euler coefficient sequence is the Taylor germ of a classical Stieltjes/Markov transform whose pole locations encode the reciprocal support points and whose residues encode the shell weights.

This answers one exact part of the transport question left open by AF-437:

> **The exponential cascade of recursive peeling is representation-specific. Exact shell provenance can be transported jointly by passing from the moment coordinates to their Stieltjes generating transform.**

It does **not** answer the stability question. Recovering remote poles from a finite or noisy Taylor germ requires analytic continuation/rational reconstruction and may itself be severely ill-conditioned. The result separates exact representation fidelity from stable operational recoverability rather than claiming that the latter problem has been solved.

## Exact derivation

For `|z|<1`, absolute convergence justifies exchanging the shell and moment sums:

\[
\begin{aligned}
F(z)
&=\sum_{k\ge1}\sum_{m\ge1}m^{-2k}z^{k-1}\\
&=\sum_{m\ge1}\sum_{k\ge1}m^{-2k}z^{k-1}\\
&=\sum_{m\ge1}\frac{1}{m^2-z}.
\end{aligned}
\]

Indeed, for every fixed `r<1` and `|z|\le r`,

\[
\sum_{m\ge1}\sum_{k\ge1}m^{-2k}|z|^{k-1}
=\sum_{m\ge1}\frac{1}{m^2-|z|}
<\infty.
\]

The classical cotangent partial-fraction formula is

\[
\cot w=\frac1w+2w\sum_{m\ge1}\frac{1}{w^2-m^2\pi^2}.
\]

Substituting `w=\pi\sqrt z` gives

\[
\pi\sqrt z\cot(\pi\sqrt z)
=1+2z\sum_{m\ge1}\frac{1}{z-m^2},
\]

hence

\[
\sum_{m\ge1}\frac{1}{m^2-z}
=\frac{1-\pi\sqrt z\cot(\pi\sqrt z)}{2z}.
\]

Although written with `\sqrt z`, the expression is single-valued because `w\cot(\pi w)` is even in `w`. The series `\sum_m(m^2-z)^{-1}` also converges locally uniformly away from the positive-square poles, so it supplies the meromorphic continuation directly.

At `z=m^2`, all terms except the `m`-th are holomorphic and

\[
\frac{1}{m^2-z}=-\frac{1}{z-m^2},
\]

which proves the residue formula.

For the measure representation, simply compute

\[
\int\frac{d\mu(t)}{1-zt}
=\sum_{m\ge1}\frac{m^{-2}}{1-zm^{-2}}
=\sum_{m\ge1}\frac{1}{m^2-z}.
\]

The shifted moments of `\mu` are exactly the Euler coefficients:

\[
\int t^{k-1}\,d\mu(t)
=\sum_{m\ge1}m^{-2k}
=\zeta(2k).
\]

## Why this bypasses the recursive peeling cascade exactly

AF-437 studies the triangular algorithm that recovers shell `m` only after shells `1,\ldots,m-1` have been estimated and removed. An error in shell `j<m` is therefore multiplied relative to the shell-`m` target by the factor `(m/j)^{2k}`.

The Stieltjes carrier does not perform that recursion. Every shell contributes the separate meromorphic term

\[
F_m(z)=\frac{1}{m^2-z}.
\]

Changing only the weight of shell `m` from `1` to `w_m` changes the residue at `m^2` from `-1` to `-w_m`; moving that shell changes its pole location. Neither operation requires subtracting the contributions of shells `1,\ldots,m-1` first.

The standard matched deletion control is especially transparent. If shell `m` is removed, then

\[
F(z)-F^{(-m)}(z)=\frac{1}{m^2-z}.
\]

Therefore the exact transform never collapses the source and the shell-deleted control. In the moment coordinates the same distinction appears in coordinate `k` as `m^{-2k}`; in the joint transform it becomes one persistent pole term.

This is a representation change, not creation of new source information. AF-436 already proves that the complete exact moment sequence determines the shell measure. The new point is that the Stieltjes transform gives an explicit **non-peeling carrier** in which shell identity is geometrically separated as pole location rather than hidden in a recursively shrinking residual hierarchy.

## Exact fidelity versus stable recovery

The distinction between exact and stable transport is essential.

The Taylor series defining `F` has radius `1`, set by the nearest pole at `z=1`. Shells `m\ge2` lie outside that disk. Reading their pole locations from the coefficient germ therefore requires continuation beyond the initial convergence circle. With the exact Euler sequence and the classical cotangent identity, that continuation is exact. With finitely many or noisy moments, it becomes an inverse problem.

Classical Stieltjes theory relates moment sequences to continued fractions and rational approximants of their transforms, and Padé/Prony methods provide neighboring finite-data reconstruction frameworks. None of those facts by itself supplies a uniform stability theorem for the present infinite shell ladder.

In particular, this finding does **not** prove that a finite Padé approximant can recover shell `m` under a larger noise budget than recursive peeling, nor that pole recovery has polynomial conditioning in `m`. Analytic continuation can trade the explicit triangular cascade for a different and potentially severe instability.

The correct fidelity hierarchy is therefore:

- the exact moment sequence is shell-determinate (AF-436);
- recursive dominant-shell peeling is exponentially fragile (AF-437);
- the exact Stieltjes transform carries all shells jointly as poles (this finding);
- stable recovery of those poles from truncated/noisy moments remains an independent conditioning problem.

## Prior-art and novelty audit

The mathematics of the transform is classical.

NIST DLMF §4.22.3 gives the cotangent partial-fraction expansion

\[
\cot z=\frac1z+2z\sum_{n\ge1}\frac{1}{z^2-n^2\pi^2},
\]

from which the displayed generating identity follows immediately. Source: https://dlmf.nist.gov/4.22.E3

The connection between moment sequences, Stieltjes transforms, and continued fractions goes back to Stieltjes' original moment theory. A concise modern reference is the Encyclopedia of Mathematics entry **“Moment problem”**, which records the transform/continued-fraction relation: https://encyclopediaofmath.org/wiki/Moment_problem

AF-436 already places the same Euler sequence inside the determinate Hausdorff moment problem and cites classical moment and Prony references. No novelty is claimed here for the even-zeta generating function, cotangent partial fractions, Stieltjes transforms, moment determinacy, continued fractions, Padé approximation, or recovery of atoms from poles/residues.

The Arithmetic Fidelity contribution is the **placement of this classical transform at the exact boundary exposed by AF-436 and AF-437**: it proves that the sequential exponential error cascade is not synonymous with loss of exact provenance and exhibits a concrete destination representation that transports all shell labels simultaneously before asking whether that representation can be recovered stably from imperfect data.

## Boundaries and falsification checks

- The result uses the **entire exact** coefficient sequence. A finite prefix is strictly less information and does not inherit meromorphic pole recovery automatically.
- The cotangent formula supplies exact analytic continuation for this special Euler source. A generic noisy perturbation of the Taylor coefficients need not correspond to a nearby meromorphic function with the same pole structure.
- Exact non-collapse under shell deletion does not imply a useful separation margin under a specified observation norm. Any operational claim must define the data norm and quantify conditioning.
- The pole at `z=m^2` is a representation of the already-known shell `m`; it does not by itself establish rational-prime specificity, a zeta-zero mechanism, or RH.
- The source shell ladder here is deterministic and positive. Signed, complex, repeated, coalescing, or continuous spectral components require separate analysis.
- The transform does not repair the packet-cancellation obstruction of AF-426/AF-435 and does not show that the current full-column packet saddle transports shell identity.
- Calling this a “joint carrier” is an exact structural statement only: all shell poles coexist in one meromorphic object. It is not shorthand for a proved well-conditioned joint numerical inversion.

## Decisive next test

The next question is now sharply separated from exact transport:

> Given only the first `N` perturbed moments of the Euler shell measure, how accurately can the first `M` poles and residues of `F` be recovered by a genuinely joint method such as a Stieltjes continued fraction, Padé approximant, or Hankel/Prony reconstruction?

A useful result must compare its perturbation tolerance with the recursive benchmark of AF-437. Either exhibit a regime in which joint recovery provably avoids the earlier-shell cascade, or prove that an equivalent instability reappears in the conditioning of the rational/analytic continuation map.

Without such a theorem, the Stieltjes carrier should be treated as an exact representation-fidelity success but not yet as a stable provenance channel.

## Consequence for the research line

The live shell-provenance problem should no longer ask whether a non-peeling exact carrier exists: one does, classically and explicitly.

The frontier moves to **conditioning of joint transport**. The relevant comparison is no longer “exact sequence versus recursive peeling,” but “recursive peeling versus Stieltjes/Padé/Hankel joint recovery under the same finite/noisy observation model.” This preserves the line's distinction between exact recoverability and operational fidelity and gives AF-437's exponential cascade a concrete alternative representation to benchmark.