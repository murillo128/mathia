# AF-498 — Elton–Odell separation universalizes difference-set contact failure

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIFFERENCE-SET`, `TRANSLATION-LIMIT`, `MINIMAX-RESOLUTION`, `NEGATIVE/OBSTRUCTION`, `INFINITE-DIMENSION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-496 shows that the AF-494 translation-fiber identity and the AF-495 critical-contact equivalence characterize finite dimension when required uniformly over arbitrary closed nuisance sets. AF-497 strengthens the obstruction in infinite-dimensional Hilbert space by making the bad alias set an exact closed nuisance difference set `C=K-K` and placing the failure exactly at the critical radius.

The Hilbert hypothesis is unnecessary. The same exact critical failure occurs for a genuine closed nuisance difference set in **every infinite-dimensional real normed space**.

Let `Y` be an infinite-dimensional real normed vector space, let `s in Y` be nonzero, and let `r>0`. Then there exist a closed unbounded set `K subset Y` with `0 in K`, a closed exact difference set

\[
C:=K-K,
\]

and a constant `epsilon>0` such that

\[
\boxed{
\lambda_C(s)=r,
\qquad
\Delta_C(r/2;s)=\infty,
\qquad
\mathcal B_C(s;r)=\varnothing,
}
\]

while every bounded translated cluster point lies strictly outside the critical radius:

\[
\boxed{
\operatorname{dist}(0,\mathcal A_C(s))
\ge (1+\varepsilon)r
>r
}
\]

with the convention that the left side is `+infinity` when `mathcal A_C(s)` is empty.

Thus the finite-dimensional compactness boundary from AF-496 remains sharp even after imposing the exact algebraic form `C=K-K`, and the exact-critical Hilbert example of AF-497 extends to arbitrary infinite-dimensional normed geometry.

The mechanism is classical Banach-space separation rather than orthogonality: pass to the quotient by the target ray, use the Elton–Odell theorem to obtain transverse unit directions separated by more than one, choose minimum-norm representatives, and place them at lacunary positions along the ray. The quotient gap keeps every cross-difference alias strictly outside the critical ball, while the lacunary longitudinal labels make the exact difference set closed.

## Quotient-separated construction

Let

\[
Q:=Y/\operatorname{span}\{s\},
\]

with quotient map `pi:Y->Q` and quotient norm. Since `Y` is infinite-dimensional, so is `Q`.

By the Elton–Odell theorem, there are `epsilon>0` and unit vectors `(q_n)` in `Q` such that

\[
\boxed{
\|q_n-q_m\|_Q\ge 1+\varepsilon
\qquad(n\ne m).
}
\]

For each `q_n`, choose a representative `u_n in Y` satisfying

\[
\pi(u_n)=q_n,
\qquad
\|u_n\|=1.
\]

Such a minimum-norm representative exists because `span{s}` is one-dimensional. Indeed, for any representative `x` of the coset, the continuous function

\[
a\longmapsto \|x+a s\|
\]

is coercive on `R`, so it attains its infimum; that infimum is exactly the quotient norm `\|q_n\|_Q=1`.

Set

\[
a_n:=2^n,
\qquad
k_n:=a_n s+r u_n,
\]

and define

\[
\boxed{
K:=\{0\}\cup\{k_n:n\ge1\},
\qquad
C:=K-K.
}
\]

The sequence `(a_n)` is used only as a lacunary separation device. It carries no arithmetic meaning.

## `K` and `K-K` are closed

First,

\[
\|k_n\|
\ge
2^n\|s\|-r
\longrightarrow\infty,
\]

so `K` is closed and discrete.

Every nonzero element of `C` is of one of the forms

\[
\pm k_n
\quad\text{or}\quad
k_n-k_m\quad(n\ne m).
\]

Suppose a sequence in `C` converges. It is bounded. Primary terms satisfy the preceding lower bound, so their indices must remain bounded. For cross terms,

\[
\|k_n-k_m\|
\ge
|2^n-2^m|\,\|s\|-r\|u_n-u_m\|
\ge
|2^n-2^m|\,\|s\|-2r.
\]

Hence bounded cross terms require `|2^n-2^m|` to remain bounded. If `n\ne m`, then

\[
|2^n-2^m|\ge 2^{\min(n,m)},
\]

so `\min(n,m)` is bounded; boundedness of the difference then also bounds `\max(n,m)`. Only finitely many ordered pairs can occur. Therefore every convergent sequence in `C` is eventually confined to a finite subset, and

\[
\boxed{C=K-K\text{ is closed}.}
\]

This avoids any closure completion of the nuisance difference set.

## Exact critical separation

For every `y in Y`, quotient contraction gives

\[
\operatorname{dist}(y,\operatorname{span}\{s\})
=
\|\pi(y)\|_Q.
\]

The quotient components of the nonzero aliases are

\[
\pi(\pm k_n)=\pm r q_n,
\]

and

\[
\pi(k_n-k_m)=r(q_n-q_m).
\]

Consequently

\[
\operatorname{dist}(\pm k_n,\operatorname{span}\{s\})=r,
\]

whereas every cross difference satisfies

\[
\operatorname{dist}(k_n-k_m,\operatorname{span}\{s\})
\ge (1+\varepsilon)r.
\]

Thus, apart from the origin, every point of `C` stays at least distance `r` from the target line. For sufficiently large positive `t`, the origin itself is farther than `r` from `ts`. Hence

\[
\operatorname{dist}(ts,C)\ge r
\]

for all sufficiently large `t`.

At the lacunary times `t=a_n=2^n`, however,

\[
\|a_ns-k_n\|
=r\|u_n\|
=r.
\]

The quotient lower bound shows that this is exact:

\[
\operatorname{dist}(a_ns,C)=r.
\]

Therefore

\[
\boxed{
\lambda_C(s)=r
}
\]

and the critical radius is hit at arbitrarily large times:

\[
\boxed{
\Delta_C(r/2;s)=\infty.
}
\]

So this is not merely a bounded-offset failure above the phase boundary. It occurs on the exact AF-495 equality surface.

## The critical contact fiber is empty

Assume for contradiction that

\[
b\in\mathcal B_C(s;r).
\]

Then there are `t_j->infinity` and `c_j in C` such that

\[
\|c_j-t_js\|\le r,
\qquad
c_j-t_js\to b.
\]

A cross difference `c_j=k_n-k_m`, `n\ne m`, is impossible because quotient contraction would give

\[
\|c_j-t_js\|
\ge
\|\pi(c_j)\|_Q
\ge
(1+\varepsilon)r
>r.
\]

The origin and negative primary points cannot remain within a bounded distance of `t_js` as `t_j->infinity`. Thus, after passing to a tail, every witness must be a positive primary point `c_j=k_{n_j}`.

But then

\[
\pi(c_j-t_js)=r q_{n_j}.
\]

Convergence of the offsets would force `(q_{n_j})` to converge in `Q`. Elton–Odell separation forbids this unless the indices are eventually constant. Eventual constancy is incompatible with `t_j->infinity` and bounded offsets from one fixed `k_n`. Therefore

\[
\boxed{
\mathcal B_C(s;r)=\varnothing.
}
\]

The AF-495 implication from recurrent critical hits to a norm-contact cluster therefore fails for exact nuisance difference sets in every infinite-dimensional normed space.

## The full translation fiber also misses the true threshold

Let `a in mathcal A_C(s)`, witnessed by `t_j->infinity`, `c_j in C`, and

\[
c_j-t_js\to a.
\]

As above, the origin cannot contribute. Positive primary points cannot contribute either: their quotient offsets are `r q_n`, which have no convergent subsequence. Negative primary points cannot track the positive target ray at bounded norm.

Hence any translation-fiber point must arise, after passing to a subsequence, from cross differences. Quotient contraction and Elton–Odell separation then give

\[
\|\pi(c_j)\|_Q
=r\|q_{n_j}-q_{m_j}\|_Q
\ge(1+\varepsilon)r.
\]

Passing to the limit yields

\[
\|a\|
\ge
\|\pi(a)\|_Q
\ge
(1+\varepsilon)r.
\]

Therefore

\[
\boxed{
\operatorname{dist}(0,\mathcal A_C(s))
\ge(1+\varepsilon)r
>r
=
\lambda_C(s).
}
\]

If the cross differences themselves have no norm-convergent translated subsequence, `mathcal A_C(s)` may be empty; this is not required. What matters is stronger: **any cluster point that does survive lies behind a strict quotient gap and therefore cannot encode the actual critical threshold**.

This cleanly separates two failures that were conflated in the most elementary noncompact examples. The problem is not only that a bounded returning sequence may lack a norm cluster point. Even when other translated clusters exist, the cluster fiber can be quantitatively separated from the true liminf because the critical returning directions themselves disperse in the quotient.

## Prior-art and novelty audit

No broad novelty is claimed for the Banach-space separation theorem or for the standard quotient-norm facts used in the construction.

- J. Elton and E. Odell, **“The unit ball of every infinite-dimensional normed linear space contains a `(1+epsilon)`-separated sequence,”** *Colloquium Mathematicum* 44 (1981), 105–109, DOI `10.4064/CM-44-1-105-109`. This is the decisive classical input: every infinite-dimensional normed space has a uniformly more-than-one-separated sequence on its unit sphere/ball.
- C. A. Kottman, **“Subsets of the unit ball that are separated by more than one,”** *Studia Mathematica* 53 (1975), 15–27, DOI `10.4064/SM-53-1-15-27`. This is the earlier separation theorem underlying the same noncompact geometry; Elton–Odell supplies the convenient uniform `(1+epsilon)` margin.
- R. Tyrrell Rockafellar and Roger J.-B. Wets, ***Variational Analysis***, Springer (1998), DOI `10.1007/978-3-642-02431-3`. This remains the background language for translated set limits, distance profiles, and horizon constructions used throughout AF-493–AF-497.

The separated-sequence ingredient is classical, and no claim is made that lacunary embeddings or difference-set constructions are new objects in functional analysis. The durable AF result is the task-specific consequence obtained by combining them: **the exact critical norm-fiber failure of AF-495 persists, with `C` an exact closed difference set, in every infinite-dimensional normed space; Hilbert orthogonality is not the relevant boundary.** The true universal boundary remains norm-precompactness of the returning translated family.

## Falsification and boundary audit

- No completeness assumption is used. Elton–Odell is a theorem for infinite-dimensional normed linear spaces, the quotient by the one-dimensional closed subspace remains an infinite-dimensional normed space, and minimum-norm representatives exist because the minimized direction is finite-dimensional.
- The construction is synthetic. It proves an impossibility theorem for unrestricted exact nuisance difference sets; it does not assert that a natural arithmetic control family realizes this pathology.
- Lacunarity of `2^n` is used only to make `K-K` closed by preventing distinct longitudinal pair differences from remaining in a bounded region while both indices escape. Many faster-than-uniformly-spaced label sequences would work.
- Elton–Odell separation is used twice: `\|q_n-q_m\|>1` keeps every cross difference strictly outside the critical radius, and pairwise separation prevents the primary critical offsets from acquiring a quotient cluster point.
- The finding does not say that every infinite-dimensional nuisance family breaks AF-494/AF-495. Families whose relevant translated offsets are norm-precompact still satisfy the compactness step locally.
- Weak or weak-star compactness is not a repair of this theorem as stated because the target quantity is the norm distance. AF-496 already exhibits the corresponding norm-defect loss in Hilbert space.
- Nothing here identifies a rational-prime discriminator or advances RH directly. It closes the category boundary of one abstract fidelity mechanism before arithmetic specialization.

## Relationship to AF-496 and AF-497

AF-496 proves that universal validity of either norm-fiber recovery principle is equivalent to finite dimensionality, but its general infinite-dimensional counterexample is an arbitrary closed set and need not fail at the exact critical radius. AF-497 upgrades both features in Hilbert space: exact `C=K-K` and exact critical contact failure.

AF-498 removes the remaining Hilbert restriction. Quotient separation replaces orthogonality, and lacunary longitudinal labels replace the Hilbert-coordinate closure argument. Consequently the strongest current obstruction can be stated without category caveats:

\[
\boxed{
\text{every infinite-dimensional normed space admits a closed exact difference-set nuisance family for which the norm translation/contact fibers lose the true critical fixed-noise threshold.}
}

The next constructive question is therefore no longer whether this pathology is specifically Hilbertian. It is which **family-level compactness or metric-tightness condition**, weaker than ambient finite dimensionality but strong enough for natural arithmetic nuisance families, restores the AF-494/AF-495 recovery laws.