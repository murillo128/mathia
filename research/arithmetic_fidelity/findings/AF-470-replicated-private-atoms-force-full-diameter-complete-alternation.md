# AF-470 — Replicated private atoms force full-diameter complete alternation

- **Date:** 2026-09-21
- **Status:** proved
- **Research line:** `arithmetic_fidelity`
- **Kind:** metric transform / total variation / conditional negative type / complete alternation / Hilbert repair
- **Depends on:** AF-466, AF-467, AF-468, AF-469
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-STRUCTURE + LINE-SPECIFIC-STRENGTHENING + NO-NOVELTY-CLAIM`

## Claim

Let `A` be an infinite discrete alphabet and let `Delta(A)` be its finitely supported probability simplex with

\[
d(\mu,\nu)=\|\mu-\nu\|_1\in[0,2].
\]

Let

\[
g:[0,2]\to[0,\infty),\qquad g(0)=0,
\]

and suppose that for every finite family in `Delta(A)` the kernel

\[
K_g(\mu,\nu)=g(d(\mu,\nu))
\]

is conditionally negative definite. Equivalently, `K_g` is the squared distance of some Hilbert embedding on every finite subset.

Then for every integer `k>=1`, every `x>=0`, and every positive increments `epsilon_1,...,epsilon_k` satisfying

\[
x+\epsilon_1+\cdots+\epsilon_k\le 2,
\]

one has the full bounded-interval complete-alternation law

\[
\boxed{
(-1)^{k-1}
\Delta_{\epsilon_1}\cdots\Delta_{\epsilon_k}g(x)\ge0.
}
\]

Here `Delta_h g(x)=g(x+h)-g(x)`. Thus an exact scalar Hilbert repair of total variation on the unrestricted probability simplex must be completely alternating on the **entire TV diameter**, not merely below half the diameter as obtained in AF-469.

No continuity assumption is needed for this finite-difference conclusion. If `g` is smooth on `(0,2)`, then

\[
(-1)^{k-1}g^{(k)}(x)\ge0
\qquad(k\ge1,\ 0<x<2),
\]

so `g'` is completely monotone throughout the whole interior.

## Exact replicated-private-atom construction

Fix `x>0`, positive `epsilon_1,...,epsilon_k` with

\[
x+\sum_{i=1}^k\epsilon_i\le2,
\]

and an auxiliary replication dimension `m>=1`.

Index a finite family of probability laws by

\[
(u,b)\in\{0,1\}^m\times\{0,1\}^k.
\]

Choose mutually distinct atoms

- one common atom `star`;
- one private atom `p_{u,b}` for every full vertex `(u,b)`;
- two coordinate atoms `(i,0)` and `(i,1)` for each `1<=i<=k`.

Define

\[
\mu_{u,b}(\star)
=1-\frac{x}{2}-\frac12\sum_{i=1}^k\epsilon_i,
\]

\[
\mu_{u,b}(p_{u,b})=\frac{x}{2},
\qquad
\mu_{u,b}(i,b_i)=\frac{\epsilon_i}{2},
\]

with all other masses zero. The budget condition makes these probability measures.

For distinct vertices `(u,b) != (u',b')`, their private atoms are disjoint, contributing exactly `x` to the `l1` distance, while each changed `b_i` contributes `epsilon_i`. Hence

\[
\boxed{
\|\mu_{u,b}-\mu_{u',b'}\|_1
=x+\sum_{i:b_i\ne b_i'}\epsilon_i
}
\]

for distinct vertices, and the distance is `0` on the diagonal.

This is the missing geometry in AF-469: the positive base distance `x` is supplied by vertex-private probability mass rather than by background Hamming coordinates. Replication therefore costs alphabet size but **no additional TV diameter**.

## Walsh eigenvalue forces the sign

View the vertex set as the Boolean group

\[
G_m=\{0,1\}^{m+k}
\]

and use the Walsh character

\[
\chi(u,b)=(-1)^{b_1+\cdots+b_k},
\]

which is nontrivial and independent of the replication coordinates `u`.

Because `K_g` is conditionally negative definite, the Fourier/Walsh eigenvalue associated with this character is nonpositive. Relative to the zero vertex it equals

\[
\lambda_m
=\sum_{(u,b)\in G_m}
\chi(u,b)\,g\!\left(d(\mu_{0,0},\mu_{u,b})\right)
\le0.
\]

If the diagonal term were assigned the same positive baseline `x` as every distinct private-atom pair, the sum over the `2^m` replication coordinates would simply multiply the desired finite difference. The actual diagonal has distance zero, so using `g(0)=0` gives the exact identity

\[
\boxed{
\lambda_m
=2^m(-1)^k
\Delta_{\epsilon_1}\cdots\Delta_{\epsilon_k}g(x)-g(x).
}
\]

Therefore

\[
2^m(-1)^k
\Delta_{\epsilon_1}\cdots\Delta_{\epsilon_k}g(x)
\le g(x).
\]

The left finite difference is independent of `m`. Letting `m` grow yields

\[
(-1)^k
\Delta_{\epsilon_1}\cdots\Delta_{\epsilon_k}g(x)
\le0,
\]

which is the claimed complete-alternation inequality.

For `x=0`, no replication is needed: the ordinary weighted Hamming cube realized inside the probability simplex gives the same Walsh inequality directly whenever `sum epsilon_i<=2`.

## Why this strictly strengthens AF-469

AF-469 used many small background coordinates whose binomial Hamming distance concentrated around `x`. That realization required a total background mass asymptotic to `x` on each side of a pair, producing the restriction

\[
2x+\sum_i\epsilon_i<2
\]

and used continuity of `g` to pass through concentration.

The private-atom family above replaces concentration by an exact finite metric identity. The admissible budget becomes the sharp geometric constraint

\[
x+\sum_i\epsilon_i\le2,
\]

which is precisely the condition that every argument of the finite difference remain in the TV diameter. The continuity hypothesis disappears simultaneously.

Thus the half-diameter boundary in AF-469 was a limitation of that realization, not a genuine freedom of scalar radial Hilbert repair.

## Prior-art audit

The surrounding structure is classical and no novelty claim is made for complete alternation, Bernstein functions, Schoenberg negative type, or Walsh analysis of Hamming/Manhattan metrics.

- Berg, Christensen and Ressel, *Harmonic Analysis on Semigroups* (Springer, 1984), is standard background for negative-definite functions, complete alternation and Bernstein composition.
- Josh Alman, Timothy Chu, Gary Miller, Shyam Narayanan, Mark Sellke and Zhao Song, *Metric Transforms and Low Rank Matrices via Representation Theory of the Real Hyperrectangle*, arXiv:2011.11503, gives a modern hyperrectangle characterization of Manhattan metric transforms and Bernstein behavior.
- Chunsheng Ma, *Vector Random Fields on the Probability Simplex with Metric-Dependent Covariance Matrix Functions*, Journal of Theoretical Probability 36 (2023), 1922–1938, DOI `10.1007/s10959-022-01217-6`, is adjacent probability-simplex prior art showing conditional negative definiteness for a simplex metric.

A targeted literature search did not locate this exact bounded-simplex replicated-private-atom argument or a theorem stated as the present full-diameter necessity result. That absence is not evidence of novelty; the result should be treated as a direct line-specific consequence of classical negative-type machinery unless stronger prior art is found.

## Boundaries

1. **Unrestricted alphabet breadth is essential to this proof.** The limit `m->infinity` consumes exponentially many private atoms. The theorem therefore applies to the full/unrestricted discrete probability simplex used in AF-456–AF-469. It does not by itself impose arbitrarily high-order constraints on a fixed finite-dimensional simplex.

2. **This is an exact-CND theorem.** It does not classify bounded-distortion or approximate Hilbert embeddings. AF-468 remains the relevant square-root lower-scale obstruction there.

3. **Only scalar radial repairs are constrained.** A non-radial embedding may depend on the source state, provenance, marking, boundary data, or other relational structure and is not represented by one scalar `g(d_TV)`.

4. **Necessity is not sufficiency on the bounded interval.** Complete alternation on `[0,2]` is forced. This finding does not prove that every bounded-interval completely alternating function extends to a Bernstein function on `[0,infinity)` or that every such local profile yields a CND transform on the entire probability simplex.

5. **There is no arithmetic specificity here.** Rational primes and matched generalized-prime controls have not yet entered. The result classifies what any source with unrestricted mixture geometry forces on an exact scalar Hilbert repair.

## Consequence for Arithmetic Fidelity

The scalar-radial exact-Hilbert escape has become much narrower. AF-466 supplies the square-root repair, AF-467 gives the sharp power threshold, AF-468 forces at least square-root local sensitivity for uniformly faithful scalar repairs, and AF-470 now forces every exact squared-Hilbert transform to obey the complete Bernstein sign hierarchy at every scale allowed by the TV diameter.

The remaining useful questions are therefore sharper: determine whether the relevant arithmetic source law genuinely contains enough replicated-private-atom or comparable mixture geometry to inherit this full obstruction; determine whether bounded-interval complete alternation is also sufficient in the exact radial problem; or leave the radial class and identify a non-radial/marked destination structure whose extra coordinates preserve the arithmetic discriminator rather than merely changing the scalar metric.