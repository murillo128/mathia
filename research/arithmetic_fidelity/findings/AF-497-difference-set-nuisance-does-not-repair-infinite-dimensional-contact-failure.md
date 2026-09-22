# AF-497 — Difference-set nuisance does not repair infinite-dimensional norm-contact failure

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIFFERENCE-SET`, `TRANSLATION-LIMIT`, `MINIMAX-RESOLUTION`, `NEGATIVE/OBSTRUCTION`, `INFINITE-DIMENSION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-496 showed that the AF-494/AF-495 norm-translation and contact-fiber principles fail in infinite-dimensional normed spaces, but its counterexample used an arbitrary closed discrete nuisance set and explicitly left open whether the failure survives the structural restriction

\[
C=K-K
\]

that arises naturally in the bounded-nuisance minimax geometry of AF-491.

It does. Every infinite-dimensional real Hilbert space admits a **closed nuisance family `K` whose closed difference set `C=K-K` has recurrent exact critical contacts at arbitrarily large displacement, while both norm fibers remain empty**.

Let `H` be an infinite-dimensional real Hilbert space. Choose a unit vector `s`, an orthonormal sequence `(e_n)_{n>=1}` in `s^perp`, and `r>0`. Define

\[
k_n:=ns+r e_n,
\qquad
K:=\{0\}\cup\{k_n:n\ge1\},
\qquad
C:=K-K.
\]

Then `K` and `C` are closed, and

\[
\boxed{
\lambda_C(s)
:=
\liminf_{t\to\infty}\operatorname{dist}(ts,C)
=r.
}
\]

Moreover

\[
\boxed{
\Delta_C(r/2;s)=\infty,
\qquad
\mathcal A_C(s)=\varnothing,
\qquad
\mathcal B_C(s;r)=\varnothing.
}
\]

Thus the exact critical-radius failure from AF-496 persists for a genuine nuisance difference set. The obstruction is not that AF-496 allowed an arbitrary set `C`; it is the loss of norm-precompactness in the translated difference-set contacts themselves.

## Explicit geometry of the difference set

The points of `C=K-K` are

\[
0,
\qquad
\pm(ns+r e_n),
\qquad
(n-m)s+r(e_n-e_m)
\quad(n,m\ge1,\ n\ne m).
\]

Because `s` is orthogonal to every `e_n`, the scalar coordinate along `s` is always an integer. For a fixed positive integer `q`, the slice of `C` with `s`-coordinate `q` has transverse part

\[
S_q
=
\{r e_q\}
\cup
\{r(e_{m+q}-e_m):m\ge1\}.
\]

The vectors in the second family all have norm `sqrt(2) r`. For distinct `m,l`,

\[
\langle e_{m+q}-e_m,e_{l+q}-e_l\rangle
\in\{0,-1\},
\]

so distinct members of that family are separated by at least `2r`. Their distance from `r e_q` is at least `sqrt(3) r`. Hence every fixed-coordinate slice is uniformly discrete and closed.

Now let `(c_j)` be any convergent sequence in `C`. Its scalar coordinates `\langle c_j,s\rangle` are integers and must therefore be eventually constant. The corresponding transverse sequence then lies in one fixed uniformly discrete slice, so it too is eventually constant. Thus

\[
\boxed{C\text{ is closed}.}
\]

The same scalar-coordinate argument shows immediately that `K` is closed.

## Exact asymptotic distance

Take any `c in C` with positive scalar coordinate `q`. If `c=k_q`, its transverse component has norm `r`. Every other positive-coordinate point is a difference `k_{m+q}-k_m` and has transverse norm `sqrt(2) r`. Therefore

\[
\|ts-c\|\ge r
\]

for every such `c` and every real `t`.

Points of `C` with nonpositive scalar coordinate have horizontal distance tending to infinity from `ts` as `t->infinity`. Consequently

\[
\liminf_{t\to\infty}\operatorname{dist}(ts,C)\ge r.
\]

At every positive integer `n`, however, `k_n in C` because `0 in K`, and

\[
\|ns-k_n\|=r.
\]

Hence

\[
\boxed{\lambda_C(s)=r.}
\]

In fact, once `t>r`, a radius-`r` contact can occur only at an integer `t=n`, through the point `k_n`; the pair-difference branch has transverse norm `sqrt(2)r>r`. Therefore the critical contact set is unbounded and

\[
\boxed{\Delta_C(r/2;s)=\infty.}
\]

## The translated norm fibers are empty

Suppose, toward a contradiction, that `a in mathcal A_C(s)`. Then there are `t_j->infinity` and `c_j in C` such that

\[
c_j-t_js\to a.
\]

Write

\[
q_j:=\langle c_j,s\rangle\in\mathbb Z.
\]

Taking scalar coordinates gives

\[
q_j-t_j\to\langle a,s\rangle,
\]

so `q_j->+infinity`.

For positive `q_j`, the transverse component of `c_j` is either

\[
r e_{q_j}
\]

or

\[
r(e_{n_j}-e_{m_j}),
\qquad n_j>m_j,
\qquad n_j-m_j=q_j.
\]

Across the union of all such positive-coordinate transverse components, any two distinct vectors are separated by at least `r`:

- two distinct basis vectors `r e_i,r e_j` are `sqrt(2)r` apart;
- a basis vector and an oriented two-basis difference are at least `r` apart;
- two distinct oriented differences are at least `sqrt(2)r` apart.

Therefore a norm-convergent transverse sequence must be eventually constant. But a constant transverse vector uniquely fixes either its basis index or its ordered pair of basis indices, and hence fixes the scalar difference `q_j`. That contradicts `q_j->infinity`.

Thus

\[
\boxed{\mathcal A_C(s)=\varnothing.}
\]

The contact fiber is a subset of the translation fiber, so automatically

\[
\boxed{\mathcal B_C(s;r)=\varnothing.}
\]

Combining this with the exact critical recurrence gives

\[
\Delta_C(r/2;s)=\infty
\quad\text{but}\quad
\mathcal B_C(s;r)=\varnothing,
\]

and simultaneously

\[
\lambda_C(s)=r
<
\operatorname{dist}(0,\mathcal A_C(s))
=+\infty.
\]

## What the difference-set restriction preserves — and what it does not

The construction is more structured than the arbitrary closed set used in AF-496. The nuisance geometry is generated by one actual parameter set `K`; every alias vector is a genuine pairwise difference of admissible nuisance states.

Nevertheless, forming `K-K` does not create the compactness needed by the norm fibers. The points `k_n-0` already supply a critical returning branch whose translated residuals are the orthogonal sequence `r e_n`. The additional cross-differences `k_n-k_m` do not repair this; they create another uniformly separated transverse family with larger norm.

So the failure mechanism can be stated intrinsically in the nuisance language of AF-491:

\[
\text{recurrent bounded difference-set aliases}
\not\Longrightarrow
\text{norm-precompact recurrent aliases}.
\]

The distinction survives the passage from an arbitrary alias set to an exact difference set.

## Prior-art and novelty audit

No broad novelty is claimed for the Hilbert-space or compactness ingredients.

- The orthonormal-sequence obstruction to norm compactness is standard Hilbert-space theory and is the explicit Hilbert realization of the compactness boundary already audited in AF-496.
- R. Tyrrell Rockafellar and Roger J.-B. Wets, *Variational Analysis*, Springer (1998), DOI `10.1007/978-3-642-02431-3`, provides the set-convergence and variational-analysis background for the translated-set language used in AF-493–AF-496.
- Junya Nishiguchi, **“Asymptotic compactness in topological spaces,”** *Topology and its Applications* 287 (2021), 107451, DOI `10.1016/j.topol.2020.107451`, studies asymptotic compactness of nets of sets and the relation between compactness and nonempty compact limit sets. This is directly adjacent to the compactness mechanism exposed here, although the present theorem is a task-specific deterministic alias construction rather than a dynamical-systems theorem.
- Classical results on Minkowski sums/differences emphasize that closedness and compactness properties of `K-K` are not automatic for arbitrary closed sets in infinite-dimensional spaces. The present `K` is chosen so that `K-K` is explicitly closed, removing that possible escape.

The Arithmetic Fidelity contribution is the structural strengthening of AF-496: **even when the alias set is required to be an exact closed nuisance difference set, recurrent exact critical contacts need not leave any norm-convergent translated witness in infinite-dimensional Hilbert geometry**. The restriction `C=K-K` therefore does not restore the AF-494/AF-495 fiber laws by itself.

## Falsification and boundary audit

- The theorem is proved for infinite-dimensional Hilbert spaces, not for every infinite-dimensional Banach space. AF-496 already gives the unrestricted closed-set failure in every infinite-dimensional normed space; extending the present exact `K-K` construction to all Banach spaces would require additional control of pairwise differences of a separated transverse sequence.
- The nuisance family `K` is closed and discrete but unbounded. This result does not address compact `K`; compactness of `K-K` would trivially restore precompactness and belongs to the bounded-nuisance regime of AF-491.
- The construction is synthetic. It proves that difference-set structure alone is insufficient, not that naturally occurring arithmetic nuisance families exhibit the same pathology.
- The radius `r` is exactly the asymptotic threshold `lambda_C(s)`, so the failure is not caused by choosing an oversized contact ball.
- Replacing norm convergence by weak convergence again makes the orthogonal residuals converge weakly to `0`, but as in AF-496 that loses the positive metric threshold `r`; this finding does not propose a weak-topology repair.
- Nothing here identifies a rational-prime discriminator or advances RH directly. It closes a structural escape in the abstract compression/recovery theory before arithmetic specialization.

## Relationship to AF-491 and AF-494–AF-496

AF-491 made `K-K` the exact geometry controlling two-target ambiguity under bounded nuisance. AF-494 and AF-495 then encoded large-displacement aliases by norm translation/contact fibers in finite dimension. AF-496 proved that universal norm-fiber fidelity is equivalent to finite-dimensional compactness, but left open whether requiring the alias set to come from `K-K` removes its counterexample.

AF-497 closes that escape in the Hilbert category. The finite-dimensional hypothesis cannot be replaced merely by “the nuisance aliases form a closed difference set.” What is actually needed is a compactness condition on the **translated alias family itself**—for example norm precompactness/tightness at the task-relevant radius—or a richer lift that preserves both cluster information and norm defect.