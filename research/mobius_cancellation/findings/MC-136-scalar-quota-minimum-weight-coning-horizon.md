# MC-136 — Scalar quota filtrations have a minimum-weight coning horizon

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Let `V` be a vertex set with a fixed positive scalar weight function

\[
w:V\to(0,\infty)
\]

whose minimum is attained at a vertex `v_0`, with

\[
\omega=w(v_0)>0.
\]

For `t>0`, form the closed scalar quota complex

\[
X_t=\left\{F\subset V:\ F\text{ finite and }w(F):=\sum_{v\in F}w(v)\le t\right\}.
\]

Then for every `s<=t` with

\[
t\ge s+\omega,
\]

the canonical inclusion factors through the closed star of the minimum-weight vertex:

\[
\boxed{X_s\subseteq \operatorname{st}_{X_t}(v_0)\subseteq X_t.}
\tag{1}
\]

Consequently

\[
\boxed{X_s\hookrightarrow X_t\text{ is null-homotopic whenever }t-s\ge\omega.}
\tag{2}
\]

The horizon `omega` is the best possible universal additive threshold for this class. If `v!=v_0` has weight `r=w(v)`, then for every `0<=delta<omega` the vertex `v` is isolated in `X_{r+delta}`: every edge containing it has weight at least `r+omega>r+delta`. Since `v_0` is already present, the inclusion

\[
X_r\hookrightarrow X_{r+\delta}
\]

carries a nonzero reduced `H_0` class. Thus no smaller uniform lag can force even homological triviality for all scalar quota filtrations containing a second vertex.

Equivalently, if positive multiplicative vertex costs `c(v)>1` are used and

\[
Y_N=\left\{F:\prod_{v\in F}c(v)\le N\right\},
\qquad c_0=\min_v c(v),
\]

then

\[
\boxed{B\ge c_0A\quad\Longrightarrow\quad Y_A\hookrightarrow Y_B\text{ is null-homotopic}.}
\tag{3}
\]

The factor `c_0` is uniformly sharp in the same sense.

For Björner's divisor filtration, take vertices to be primes and `c(p)=p`, or equivalently `w(p)=log p`. Then `c_0=2`, and `(3)` recovers the exact factor-two null-homotopy of `MC-135`. More importantly, the argument shows that the prime `2` is not the essential mechanism: it is the specialization of the **minimum-weight vertex of a scalar threshold/quota complex**.

Therefore a large apparent escape class left after `MC-135` is already closed. Replacing the product cutoff by any fixed scalar additive reweighting, exponentiating such a reweighting, or restricting to a fixed set of allowed prime vertices with a smallest retained prime still yields a finite coning horizon. For example, on a fixed prime subset whose smallest element is `q`, the product-threshold filtration is null-homotopic across every scale ratio at least `q`.

## 1. Minimum-weight coning is immediate

Take any simplex `F` of `X_s`.

If `v_0` already belongs to `F`, then `F` lies in the closed star of `v_0` trivially.

If `v_0` does not belong to `F`, then

\[
w(F\cup\{v_0\})=w(F)+\omega\le s+\omega\le t.
\]

Hence `F union {v_0}` is a simplex of `X_t`, so `F` is a face in `st_{X_t}(v_0)`. This proves `(1)`.

A closed simplicial star is a cone with apex `v_0`, hence contractible. The inclusion `X_s -> X_t` therefore factors through a contractible subcomplex and is null-homotopic, proving `(2)`.

No arithmetic property, cancellation estimate, zeta function, or Möbius sign is used in this argument. Only positivity, additivity of the simplex weight, and the existence of a fixed minimum-weight vertex matter.

## 2. Sharpness isolates the exact hypothesis

Fix a second vertex `v` with weight `r`. At quota `r`, the singleton `{v}` is present. For `0<=delta<omega`, every possible edge `{v,u}` has

\[
w(v)+w(u)\ge r+\omega>r+\delta.
\]

Thus `v` remains an isolated component through `X_{r+delta}`. The minimum-weight vertex `v_0` gives another component, so the reduced `H_0` class separating `v` from `v_0` survives under the inclusion.

This is the abstract version of the odd-prime sharpness argument in `MC-135`: for prime weights `log p`, the first possible coface joining a new prime vertex `p` to the minimum-weight vertex occurs when the quota increases by `log 2`, equivalently when the multiplicative scale reaches `2p`.

The result also identifies the genuine ways a new filtration can evade the obstruction. At least one load-bearing hypothesis must change: the filtration must cease to be a fixed one-dimensional additive threshold, lose a uniform positive minimum-weight vertex, use scale-dependent weights, use a nonadditive simplex score, or retain extra labelled/chain/coherent information not functorially determined by the ordinary homotopy maps.

## 3. Prior art classicalizes the mechanism

Pakianathan and Winfree's scalar quota complexes are exactly the established language for this construction. Their Definition 1.1 defines `X[w:q]` by the strict inequality `w(F)<q`. Their Proposition 2.2 proves that, for a minimum-weight vertex `v_min`, the faces outside its closed star are precisely shell faces with weight in

\[
q-w(v_{min})\le w(F)<q.
\]

Their Theorem 2.3 then collapses the closed star and derives the bouquet-of-spheres description of a scalar quota complex. With their strict-quota convention, the same one-line argument as above gives

\[
Q\ge q+\omega\quad\Longrightarrow\quad X[w:q]\subseteq\operatorname{st}_{X[w:Q]}(v_0),
\]

so `(1)`--`(2)` are a direct filtration corollary of their minimum-weight-star framework. The closed `<=` convention used here only removes endpoint bookkeeping.

The connection to the Möbius problem is also already explicit in that literature. Pakianathan and Winfree define `LogPrime(q)` by assigning the prime vertex `p` the weight `log p`; a face then corresponds to a squarefree integer `m<e^q`. Their Theorem 5.2 identifies the Euler characteristic of this complex with the Mertens-function formulation and records the RH-equivalent growth condition. Thus, up to the harmless strict/closed cutoff convention,

\[
\Delta_n=LogPrime(\log(n+1))
\]

for the Björner filtration used in `MC-133`--`MC-135`.

Primary source:

Jonathan Pakianathan and Troy Winfree, *Threshold complexes and connections to number theory*, Turkish Journal of Mathematics 37 (2013), no. 3, 511--539, DOI `10.3906/mat-1112-14`, arXiv `1104.4324`. The relevant material is Definition 1.1, Proposition 2.2, Theorem 2.3, and Section 5 on `LogPrime`.

This finding therefore makes **no novelty claim** for scalar quota complexes, minimum-weight-star topology, the `LogPrime` representation, or the resulting Mertens/RH reformulation. The durable Mathia delta is the prior-art redirect: the factor-two map collapse of `MC-135` is not an isolated prime-specific topological phenomenon but an instance of a generic scalar-threshold coning mechanism. Fixed scalar reweightings or fixed prime-subset variants cannot be treated as unexplored ways to restore long-range homotopy transport.

## Boundaries and falsification tests

- The theorem concerns a **fixed scalar** weight and one threshold parameter. Pakianathan and Winfree also study vector-valued quota complexes; the single-star factorization above does not automatically classify a genuine multiparameter/vector filtration.
- A monotone reparameterization of the same scalar quota changes the numerical appearance of the lifetime but not the underlying filtration information. It is not a structural escape.
- If the weight system changes with scale, or if no fixed positive minimum is attained, the proof can fail. Such a proposal needs its own local-finiteness and information-budget audit rather than being declared viable automatically.
- Null-homotopy of long-range inclusions kills ordinary homotopy-invariant transport. It does not erase the shell/birth data themselves. In `LogPrime`, those shell populations retain squarefree support and factor-count parity, and their alternating statistic carries the Mertens burden.
- The result does not address arithmetic labels on simplices or chains, non-homotopy-invariant operators, higher coherent data not determined by individual homotopy-category maps, or nonadditive/multiparameter filtrations.
- No source-to-amplitude estimate follows. The Pakianathan--Winfree Euler-characteristic criterion is an RH reformulation, not an independent proof of the required cancellation.

A counterexample to `(1)` would require a simplex `F` with `w(F)<=s` but `w(F union {v_0})>t` despite `t>=s+omega`, which contradicts additivity directly. A claimed scalar-threshold escape should therefore be rejected unless it changes one of the theorem's actual hypotheses rather than only the notation or scale coordinate.

## Consequence for the line

`MC-135` left a genuinely different filtration as one possible topological residual. This finding sharpens the word **different**. Any fixed one-dimensional scalar quota/threshold filtration with a positive minimum vertex has a built-in finite homotopy horizon, and product-threshold prime filtrations inherit the corresponding fixed multiplicative horizon.

The source-to-amplitude frontier should therefore stop spending effort on fixed scalar reweightings, deleting finitely many small primes, or equivalent threshold-coordinate changes as ways to create persistent long-range topology. A topological continuation must leave the scalar-quota class in a mathematically substantive way--for example through genuinely vector/multiparameter data, nonadditive or scale-dependent structure, or arithmetic-labelled chain information--and must still show that its retained statistic controls mean-absolute Mertens excursion more cheaply than reconstructing the target itself.