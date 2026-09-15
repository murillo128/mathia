# MC-318 — Schmidt's probabilistic Möbius route fails two exact consistency tests as stated

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `PRIOR-ART-AUDITED` · `NON-RH`.

## Claim

Maxie Dion Schmidt's 2026 preprint *Picking up the partial sums of the Möbius function problem with probabilistic number theory* (`MC-S54`, arXiv:2604.23517) proposes probabilistic independence assumptions involving `\Omega(n)` and `\mu^2(n)` and derives asymptotics for auxiliary Möbius/Liouville sums. Two statements used in that route are incompatible with exact elementary identities as written.

First, Assertion 1.10 (IH-A) states, for the conditioned strata under consideration,

\[
\mathbb P\!\left(\mu^2(n)\ne0\mid \Omega(n)=k\right)
=
\mathbb P\!\left(\mu^2(n)\ne0\right).
\tag{1}
\]

The assertion explicitly allows `k=1`. But `\Omega(n)=1` means that `n` is prime, hence squarefree, so the left side of `(1)` is exactly `1`. The unconditional squarefree probability tends to `6/\pi^2<1`. Thus IH-A is false already on the exact `k=1` stratum.

Second, Theorem 2.2 defines

\[
Q_{1,n}(x):=\sum_{j\le x}\lambda(nj)\mu^2(j)
\tag{2}
\]

for `1\le n\le x`, and then gives an asymptotic whose displayed leading term is independent of `n`. Yet complete multiplicativity of `\lambda` and the pointwise identity

\[
\lambda(j)\mu^2(j)=\mu(j)
\tag{3}
\]

give the exact reduction

\[
\boxed{Q_{1,n}(x)=\lambda(n)M(x)}
\tag{4}
\]

for every `n,x`. Taking `n=1` and `n=2` therefore yields

\[
Q_{1,1}(x)=M(x),
\qquad
Q_{1,2}(x)=-M(x).
\tag{5}
\]

The same nonzero `n`-independent asymptotic cannot hold for both quantities. This contradiction is independent of whether one grants the probabilistic independence assumptions.

Consequently the preprint's stated route from those assumptions through Theorem 2.2 cannot presently be used as evidence for the later claimed Mertens asymptotics. This finding does **not** assert that every statement in the preprint is false, nor does it rule out a repaired probabilistic program.

## 1. Exact failure of IH-A on the first `\Omega` stratum

To make the probability statement unambiguous, let `N_x` be uniform on the positive integers at most `x`, and interpret the manuscript's conditioning in this finite probability space. For every `x\ge2` for which the event is nonempty,

\[
\{\Omega(N_x)=1\}
=
\{N_x\text{ is prime}\}.
\tag{6}
\]

Every prime is squarefree, so

\[
\mathbb P\!\left(\mu^2(N_x)\ne0\mid\Omega(N_x)=1\right)=1.
\tag{7}
\]

On the other hand the classical squarefree-density theorem gives

\[
\mathbb P\!\left(\mu^2(N_x)\ne0\right)
=\frac1{\lfloor x\rfloor}\sum_{m\le x}\mu^2(m)
\longrightarrow \frac6{\pi^2}.
\tag{8}
\]

Equations `(7)` and `(8)` contradict `(1)` at `k=1`. The issue is structural, not a finite-size error: the condition `\Omega(n)=1` forces squarefreeness.

A narrower hypothesis restricted to a central or growing-`k` Erdős–Kac regime could avoid this particular counterexample, but that would be a materially different assertion and would require its own proof. The manuscript's displayed IH-A is not valid with its stated quantification.

## 2. The Theorem 2.2 auxiliary sum is exactly a signed copy of `M(x)`

The second obstruction requires no probability model. The Liouville function is completely multiplicative, hence

\[
\lambda(nj)=\lambda(n)\lambda(j).
\tag{9}
\]

Also `\mu^2(j)` is the squarefree indicator. If `j` is squarefree then `\lambda(j)=(-1)^{\Omega(j)}=\mu(j)`; if it is not squarefree then `\mu^2(j)=\mu(j)=0`. Therefore `(3)` holds for every positive integer `j`.

Substituting `(9)` and `(3)` into the manuscript's definition `(2)` gives

\[
\begin{aligned}
Q_{1,n}(x)
&=\sum_{j\le x}\lambda(n)\lambda(j)\mu^2(j)\\
&=\lambda(n)\sum_{j\le x}\mu(j)\\
&=\lambda(n)M(x).
\end{aligned}
\tag{10}
\]

This is an exact identity, with no limiting regime, smoothing, zero-free hypothesis, or independence assumption.

The displayed equation (8b) in Theorem 2.2 instead assigns `Q_{1,n}(x)` the same leading asymptotic

\[
\frac{6x}{\pi^2}\,
\frac{(-1)^{\lfloor\log\log x\rfloor}}
     {2\sqrt{2\pi\log\log x}}
\tag{11}
\]

for all `1\le n\le x`. Its magnitude is nonzero for sufficiently large `x` and its sign contains no `\lambda(n)` factor. Taking the two admissible fixed choices `n=1` and `n=2` in `(10)` forces opposite values, so both cannot be asymptotic to `(11)` with ratio tending to `1`.

This contradiction is stronger than the failure of IH-A: even a repaired independence hypothesis does not change the exact factorization `(10)`. A repaired theorem would at minimum have to respect the `\lambda(n)` dependence, and any further scaling dependence would need to be rederived from the corrected object.

## 3. Why this blocks the stated downstream route

The preprint uses Theorem 2.2 as an input to subsequent probabilistic estimates involving its auxiliary functions and ultimately to claimed asymptotic information for the Mertens function. Once `(10)` is imposed, the theorem is no longer an independently estimated proxy: it is exactly `M(x)` up to the known sign `\lambda(n)`.

Thus the manuscript cannot obtain new control of `M(x)` from the stated `Q_{1,n}` asymptotic unless the argument first proves a compatible estimate for the same quantity after correcting the theorem. Treating `(11)` as an independent probabilistic consequence would otherwise insert the target cancellation into an auxiliary sum that algebraically collapses back to the target.

This is precisely the kind of deterministic-consistency gate required by the Möbius Cancellation mandate: probabilistic independence or central-limit heuristics must first descend to observables that preserve exact multiplicative identities.

## Prior-art and novelty boundary

The identities used in the audit are classical and elementary: `\lambda` is completely multiplicative, `\mu^2` is the squarefree indicator, `\lambda\mu^2=\mu`, and squarefree integers have natural density `6/\pi^2`. No novelty is claimed for any of these facts.

The durable Mathia contribution is the **manuscript-specific consistency audit**: applying those exact identities to Assertion 1.10 and Theorem 2.2 shows that two load-bearing displayed statements cannot hold as written. A bounded search around arXiv:2604.23517 found the preprint and secondary descriptions but no correction or independent published critique resolving these two points as of 15 September 2026. Absence from that bounded search is not a novelty theorem; future versions or corrections must be checked before reusing this finding as a statement about the current manuscript.

## Boundaries and falsification tests

- **Version-sensitive.** The audit targets arXiv:2604.23517 as available on 15 September 2026. A later version may narrow IH-A or alter Theorem 2.2; if so, the exact statements must be re-audited rather than assuming the objection persists.
- **IH-A could be reformulated.** Excluding fixed small `k`, especially `k=1`, could evade the first counterexample. Such a central-range independence statement would be a new hypothesis and is not validated here.
- **The `Q_{1,n}` identity is not removable by probabilistic assumptions.** Any definition retaining `(2)` necessarily satisfies `(4)`. A corrected theorem must therefore carry the exact `\lambda(n)` dependence or change the auxiliary object itself.
- **No claim about RH.** The contradiction neither proves nor disproves RH and yields no new bound for `M(x)`.
- **No blanket rejection of probabilistic number theory.** It rules out this stated chain only. A model that respects `(4)` and uses genuinely additional information could still be mathematically useful.
- **Decisive repair test.** Recheck the current manuscript for an explicit replacement of IH-A and equation (8b). If Theorem 2.2 still defines `(2)` while assigning an `n`-independent nonzero leading term, the exact sign contradiction remains.

## Consequence for the research line

This audit supplies a concrete warning for the line's probabilistic-comparator work: **conditioning claims must be tested first on arithmetic strata where support becomes deterministic, and every proposed random proxy must be simplified against exact multiplicative identities before asymptotic independence is invoked.**

For the Schmidt route specifically, further work should not build on IH-A or Theorem 2.2 in their present form. The useful research question, if the route is revisited, is whether a corrected central-range dependence statement can be paired with an auxiliary observable that does not collapse algebraically to `\lambda(n)M(x)` and still carries quantitative information beyond known Möbius cancellation.