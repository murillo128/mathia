# AF-496 — Norm-contact-fiber fidelity characterizes finite dimension

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TRANSLATION-LIMIT`, `MINIMAX-RESOLUTION`, `NEGATIVE/OBSTRUCTION`, `FINITE-DIMENSION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-494 and AF-495 use finite-dimensional compactness to turn bounded translated offsets into norm-convergent subsequences. That hypothesis is not merely convenient. For the norm-topology translation and contact fibers used there, **universal fidelity is equivalent to finite dimensionality**.

Let `Y` be a real normed vector space. For nonempty `C subset Y` and `s in Y`, recall

\[
\mathcal A_C(s)
:=
\left\{
 a\in Y:
 \exists\ t_n\to\infty,\ c_n\in C,
 \ c_n-t_ns\to a
\right\},
\]

and

\[
\lambda_C(s)
:=
\liminf_{t\to\infty}\operatorname{dist}(ts,C).
\]

For `r>=0`, with `D=\overline C`, recall the task-truncated contact fiber

\[
\mathcal B_C(s;r)
:=
\left\{
 a\in Y:
 \exists\ t_n\to\infty,\ d_n\in D,
 \ \|d_n-t_ns\|\le r,
 \ d_n-t_ns\to a
\right\},
\]

and the AF-494 ambiguity profile

\[
\Delta_C(\rho;s)
:=
\sup\{t\ge0:\operatorname{dist}(ts,C)\le2\rho\}.
\]

Then the following are equivalent:

1. `Y` is finite-dimensional.
2. For every nonempty closed `C subset Y` and every `s in Y`,

\[
\boxed{
\lambda_C(s)=\operatorname{dist}(0,\mathcal A_C(s)),
}
\]

with `dist(0,emptyset)=+infinity`.
3. For every nonempty closed `C subset Y`, every `s in Y`, and every `r>=0`,

\[
\boxed{
\Delta_C(r/2;s)=\infty
\iff
\mathcal B_C(s;r)\ne\varnothing.
}
\]

Thus each of the two AF-494/AF-495 norm-fiber principles, required uniformly over closed nuisance sets, already **characterizes finite-dimensional normed spaces**.

In every infinite-dimensional normed space there is a closed discrete nuisance set whose offsets stay uniformly bounded at arbitrarily large target displacement but have no norm-convergent translated subsequence. Consequently the AF-494 translation fiber can be empty while `lambda_C(s)<infinity`, and recurrent fixed-radius contacts can occur while the AF-495 norm contact fiber is empty.

Moreover, in the Hilbert space `R direct-sum ell^2` this failure occurs exactly at the critical radius `r=lambda_C(s)`. Replacing norm convergence by weak convergence restores a cluster point in that example but destroys the norm threshold: the weak cluster point is `0` although the true asymptotic separation is positive. Hence **weak compactness alone is not a faithful repair of the fixed-noise invariant**.

## Finite dimension implies both fiber principles

If `Y` is finite-dimensional, closed bounded sets are compact.

AF-494 proves for arbitrary nonempty `C` that every bounded near-minimizing offset sequence has a norm-convergent subsequence and therefore

\[
\lambda_C(s)=\operatorname{dist}(0,\mathcal A_C(s)).
\]

AF-495 proves that, after replacing `C` by its closure without changing the distance profile, unbounded radius-`r` contacts yield offsets in the compact ball `\overline B_r(0)`, hence a convergent subsequence and a point of `\mathcal B_C(s;r)`. The converse needs no compactness. Thus

\[
\Delta_C(r/2;s)=\infty
\iff
\mathcal B_C(s;r)\ne\varnothing.
\]

So finite dimensionality implies both universal properties.

## One infinite-dimensional construction kills both universal properties

Assume now that `Y` is infinite-dimensional.

Choose any nonzero `s in Y`. By Hahn-Banach there is a continuous linear functional `phi in Y^*` with

\[
\phi(s)=1.
\]

Its kernel

\[
Z:=\ker\phi
\]

has codimension one and is therefore infinite-dimensional. By Riesz's lemma, there is a sequence `(x_n)` in the unit sphere of `Z` and a constant `delta>0` such that

\[
\|x_n-x_m\|\ge\delta
\qquad(n\ne m).
\]

In particular `(x_n)` has no norm-convergent subsequence.

Fix `r>0` and define

\[
\boxed{
C:=\{ns+r x_n:n\in\mathbb N\}.
}
\]

The set `C` is closed. Indeed, if a sequence of points from `C` converges, applying `phi` shows that its integer labels converge in `R`; hence those labels are eventually constant, and so the points themselves are eventually constant.

At every integer time,

\[
\operatorname{dist}(ns,C)
\le
\|ns-(ns+r x_n)\|
=r.
\]

Therefore

\[
\lambda_C(s)\le r<\infty
\]

and

\[
\Delta_C(r/2;s)=\infty.
\]

Nevertheless both norm fibers are empty.

Suppose first that `a in mathcal A_C(s)`. Then there are `t_k->infinity` and indices `m_k` such that

\[
(m_k-t_k)s+r x_{m_k}\to a.
\]

Applying `phi` gives

\[
m_k-t_k\to\phi(a),
\]

because `phi(x_{m_k})=0`. Subtracting the convergent scalar multiple `(m_k-t_k)s` from the convergent offset now gives

\[
r x_{m_k}
\to
 a-\phi(a)s.
\]

The separated sequence `(x_n)` has no convergent subsequence, so `m_k` would have to be eventually constant. But then `m_k-t_k->-infinity`, contradicting convergence to `phi(a)`. Hence

\[
\boxed{
\mathcal A_C(s)=\varnothing.
}
\]

Since `lambda_C(s)<infinity`, the AF-494 identity fails:

\[
\lambda_C(s)
<
\operatorname{dist}(0,\mathcal A_C(s))
=+\infty.
\]

The same argument proves

\[
\boxed{
\mathcal B_C(s;r)=\varnothing.
}
\]

because any point of the contact fiber would in particular give a norm-convergent translated-offset sequence of exactly the form just ruled out. Yet `Delta_C(r/2;s)=infinity` from the integer contacts. Thus the AF-495 contact equivalence also fails.

This proves the converses: if either universal norm-fiber principle holds for every closed nuisance set, then `Y` must be finite-dimensional.

## The obstruction is compactness, not distance attainment

The counterexample is deliberately discrete and closed. It does not exploit nonattainment of distance to a closed set, incompleteness, a pathological closure operation, or an unbounded noise radius. At the explicit times `t=n`, an actual nuisance point lies exactly at distance `r` from `ns`.

The failure is instead the precise compactness step used by AF-494 and AF-495:

\[
\text{bounded offsets}
\not\Longrightarrow
\text{norm-precompact offsets}
\]

in an infinite-dimensional normed space.

Riesz's lemma supplies a bounded separated sequence, and the Hahn-Banach functional places it transversely to one escaping target ray while preserving the integer label. The translated sets therefore keep returning to one bounded ball, but every returning point occupies a new norm-separated transverse direction.

Equivalently, the norm-topology contact fiber is not merely recording boundedness. It records **boundedness plus norm-precompact recurrence**. Finite-dimensionality makes those notions coincide; infinite dimension separates them.

## Exact critical failure in an infinite-dimensional Hilbert space

The general construction above is enough to characterize finite dimension, but its `r` need not equal the exact `lambda_C(s)` for an arbitrary norm. In Hilbert geometry the failure can be placed exactly on the AF-495 critical boundary.

Take

\[
Y=\mathbb R\oplus_2\ell^2,
\qquad
s=(1,0),
\]

let `(e_n)` be the standard orthonormal basis of `ell^2`, fix `r>0`, and define

\[
C=\{(n,r e_n):n\in\mathbb N\}.
\]

For any real `t`,

\[
\operatorname{dist}(ts,C)
=
\inf_{n\ge1}
\sqrt{(t-n)^2+r^2}
\ge r,
\]

while at every integer `n`,

\[
\operatorname{dist}(ns,C)=r.
\]

Hence

\[
\boxed{
\lambda_C(s)=r
}
\]

and the critical contact set is unbounded:

\[
\Delta_C(r/2;s)=\infty.
\]

But the critical offsets `(0,r e_n)` have no norm-convergent subsequence, and the same coordinate argument as above excludes every other norm-convergent translated witness. Therefore

\[
\boxed{
\mathcal A_C(s)=\varnothing,
\qquad
\mathcal B_C(s;r)=\varnothing,
}
\]

even though `lambda_C(s)=r<infinity` and the radius-`r` contacts recur forever.

So the critical-contact bit from AF-495 is a complete equality classifier only in a category where bounded contacts are norm-precompact; it is not a dimension-free invariant of arbitrary normed nuisance geometry.

## Weak compactness is not by itself a faithful repair

The Hilbert example also rules out the most immediate repair: simply replace norm convergence in the fibers by weak convergence.

In `ell^2`,

\[
e_n\rightharpoonup0.
\]

Thus the translated critical offsets satisfy

\[
(0,r e_n)
\rightharpoonup
(0,0).
\]

A weak translation/contact fiber would therefore be nonempty and would contain the origin. That repairs the **existence of a cluster point**, but if one then tried to reuse the AF-494 norm formula one would obtain

\[
\operatorname{dist}(0,\mathcal A_C^{\mathrm{weak}}(s))=0,
\]

whereas the true norm-separation threshold is

\[
\lambda_C(s)=r>0.
\]

This is the same fidelity issue one level deeper. Weak topology compresses away norm magnitude along weakly null directions. It can restore compactness while losing exactly the metric quantity needed by the fixed-noise task.

An infinite-dimensional repair therefore needs more than a topology with better compactness. It must retain enough additional data to recover the norm-scale defect—for example a norm-defect/energy coordinate, a compactness assumption on the actual translated family, or a task-specific concentration/tightness condition. This finding does not choose among those possibilities.

## Prior-art and novelty audit

No broad novelty is claimed for the functional-analysis ingredients or for the abstract compactness characterization.

- James C. Robinson, *An Introduction to Functional Analysis*, Cambridge University Press (2020), especially Chapter 5, “Finite-Dimensional Normed Spaces,” DOI `10.1017/9781139030267`. Role: standard source for finite-dimensional normed-space compactness and the converse characterization via Riesz's lemma.
- N. L. Carothers, *Real Analysis*, Cambridge University Press (2000), Chapter 8, “Compactness,” DOI `10.1017/CBO9780511814228.009`. Role: standard compactness background and explicit contrast between closed bounded sets in finite-dimensional Euclidean spaces and bounded noncompact sets in infinite-dimensional sequence spaces.
- R. Tyrrell Rockafellar and Roger J. B. Wets, *Variational Analysis*, Springer (1998), DOI `10.1007/978-3-642-02431-3`. Role: set-convergence and variational-analysis background for the translated outer-limit language inherited from AF-493–AF-495.

The classical core is that a normed space has compact closed unit ball, equivalently the bounded-sequence subsequence property needed here, exactly in finite dimension. The AF contribution is the exact task-relative reformulation: **the two norm-fiber recovery laws introduced in AF-494 and AF-495 are universally valid exactly in finite-dimensional normed spaces**, and the standard weak-compactness escape does not preserve the fixed-noise threshold without an additional norm-sensitive lift.

## Falsification and boundary audit

- The equivalence is a universal statement over closed nuisance sets. Particular infinite-dimensional families can still have compact or norm-precompact translated offsets, in which case the AF-494/AF-495 proofs can remain valid on that restricted family.
- The counterexample uses a synthetic closed discrete set rather than a difference set `K-K`. It proves that finite dimensionality is necessary for the unrestricted universal theorem, not that every infinite-dimensional nuisance difference set fails. A difference-set strengthening would be a separate result.
- The general infinite-dimensional construction proves `lambda_C(s)<infinity` with an empty translation fiber and gives recurrent radius-`r` contacts with an empty contact fiber. It does not claim that the chosen `r` is always the exact critical value `lambda_C(s)` for an arbitrary norm. The Hilbert example supplies the exact critical-radius failure.
- No completeness assumption is required for the negative direction. Riesz's lemma and Hahn-Banach apply at the normed-space level, and the constructed nuisance set is closed by the continuous label functional.
- Weak convergence is audited only as the naive topology replacement in the explicit Hilbert example. The result does not rule out richer weak-plus-norm, weak-star, measure-valued, concentration-compactness, or other lifted formulations.
- Nothing here identifies a rational-prime discriminator or advances RH directly. It closes the dimensionality boundary of the abstract translation-fiber mechanism before any arithmetic specialization.

## Relationship to AF-494 and AF-495

AF-494 identifies the bounded-offset translation fiber as the exact norm-scale invariant for the open fixed-noise threshold **in finite dimension**. AF-495 refines it by truncating before the outer limit and obtains an exact critical-contact bit for the equality case, again **in finite dimension**.

AF-496 shows that the shared finite-dimensional hypothesis is sharp at the level of universal normed-space statements. The hierarchy therefore acquires an explicit category boundary: the AF-494/AF-495 fibers are faithful when bounded translated offsets are norm-precompact; finite-dimensional normed spaces guarantee this automatically, while arbitrary infinite-dimensional spaces do not.

The next meaningful extension is not to drop “finite-dimensional” syntactically. It is to identify the weakest compactness-plus-metric lift under which bounded recurrence and the fixed-noise norm threshold survive simultaneously.