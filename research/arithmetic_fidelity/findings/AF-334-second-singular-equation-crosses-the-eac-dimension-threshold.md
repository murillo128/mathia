# AF-334 — The second singular equation crosses the exponential-algebraic-closedness dimension threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `EXPONENTIAL-SUMS`, `ROTUNDITY`, `UNLIKELY-INTERSECTION`, `STRUCTURAL-OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

The exact eight-prime singular-incidence problem isolated in AF-328 sits **one complex dimension below** the unconditional exponential-algebraic-closedness regime proved by Gallinaro for linear spaces.

Fix eight distinct rational primes `p_1,...,p_8`, put

\[
\lambda=(-\log p_1,\ldots,-\log p_8)\in\mathbb R^8,
\qquad
L_p=\mathbb C\lambda\subset\mathbb C^8,
\tag{1}
\]

and in the algebraic torus `T=(\mathbb C^\times)^8` write

\[
W_1=V(e_1),
\qquad
W_{1,4}=V(e_1,e_4).
\tag{2}
\]

Then:

1. `L_p` is additively free in the sense used in exponential-algebraic closedness;
2. `W_1` is irreducible of dimension `7`, and `L_p\times W_1` is rotund;
3. hence Gallinaro's unconditional theorem gives
   \[
   \exp(L_p)\cap W_1\ne\varnothing,
   \tag{3}
   \]
   in fact the intersection is Zariski-dense in `W_1`;
4. `W_{1,4}` has dimension `6`, so
   \[
   \dim L_p+\dim W_{1,4}=1+6=7<8;
   \tag{4}
   \]
   therefore `L_p\times W_{1,4}` fails rotundity already at the zero quotient and Gallinaro's theorem cannot apply.

Equivalently, the single centered equation

\[
\sum_{j=1}^8p_j^{-s}=0
\tag{5}
\]

lies at the generic solvability threshold of this exponential-algebraic framework, whereas adding the middle-singular equation

\[
\sum_{|I|=4}\left(\prod_{i\in I}p_i\right)^{-s}=0
\tag{6}
\]

pushes the same one-parameter prime-log source one equation beyond that threshold.

This gives a precise prior-art boundary for the current Arithmetic Fidelity bottleneck. The unresolved common zero from AF-328 is not an ordinary exponential-algebraic-closedness problem for which generic geometry should force a solution. It is an overdetermined, pointwise incidence problem. AF-333's conditional Schanuel obstruction and the failure of unconditional EAC here are therefore complementary rather than competing descriptions of the same boundary.

No claim is made that the common zero exists or does not exist, and no RH consequence follows.

## 1. The prime-log line is additively free

Gallinaro calls a linear space `L\subset\mathbb C^n` additively free when it is not contained in a translate of a proper complex linear subspace defined over `\mathbb Q`.

Suppose the line `L_p` from `(1)` were contained in such a proper rational subspace. Some nonzero rational linear functional would then vanish on `\lambda`, so after clearing denominators there would be integers `m_j`, not all zero, with

\[
\sum_{j=1}^8m_j\log p_j=0.
\tag{7}
\]

Exponentiating gives

\[
\prod_{j=1}^8p_j^{m_j}=1,
\tag{8}
\]

and unique factorization forces every `m_j=0`, contradiction. Thus

\[
\boxed{L_p\text{ is additively free}.}
\tag{9}
\]

This is the same prime-log independence already used throughout the line, now expressed in the exact language required by exponential-algebraic closedness.

## 2. The centered hypersurface is exactly at the rotund threshold

The Laurent hypersurface

\[
W_1=\{z\in T:e_1(z)=z_1+\cdots+z_8=0\}
\tag{10}
\]

is irreducible and has dimension `7`. Indeed, after solving linearly for `z_8`, its coordinate ring is a localization of a domain in the remaining seven coordinates.

We now check rotundity directly. Let `Q\subset\mathbb C^8` be a rational linear subspace of dimension `q<8`. Additive freeness implies `L_p\not\subset Q`, hence

\[
\dim \pi_Q(L_p)=1.
\tag{11}
\]

The quotient of `T` by the `q`-dimensional algebraic subgroup `\exp(Q)` has fibres of dimension `q`. Therefore the image of the seven-dimensional variety `W_1` has dimension at least

\[
\dim \pi_{\exp(Q)}(W_1)\ge 7-q.
\tag{12}
\]

Combining `(11)` and `(12)` gives

\[
\dim \pi_Q(L_p)+\dim\pi_{\exp(Q)}(W_1)
\ge 1+(7-q)=8-q,
\tag{13}
\]

which is precisely the rotundity inequality. The full-space quotient is trivial, so all rational quotients satisfy the condition. Hence

\[
\boxed{L_p\times W_1\text{ is additively free and rotund}.}
\tag{14}
\]

Gallinaro's Theorem 8.8 therefore applies and yields `(3)`. His Corollary 8.10 gives the stronger statement that `\exp(L_p)\cap W_1` is Zariski-dense in `W_1`.

Since

\[
\exp(s\lambda)
=(p_1^{-s},\ldots,p_8^{-s}),
\tag{15}
\]

this is an unconditional structural solvability result for the **complex-time** centered equation `(5)`. It says nothing about imaginary-axis times `s=it`, but it shows that one algebraic condition is still within the generic solvability budget of the prime-log line.

## 3. The middle-singular condition consumes one dimension too many

Now impose the second equation `e_4=0`. The restriction of `e_4` to `W_1` is neither zero nor a unit.

It is not identically zero because at

\[
(1,1,1,1,-1,-1,-1,-1)
\tag{16}
\]

we have `e_1=0` while

\[
e_4=6\ne0.
\tag{17}
\]

It is not a unit because AF-317 gives an explicit point of `(S^1)^8\subset T` satisfying both `e_1=0` and `e_4=0`.

Thus `e_4` cuts the irreducible seven-dimensional hypersurface `W_1` by one further genuine algebraic condition. By the principal ideal theorem, every irreducible component of the resulting nonempty variety has dimension `6`; in particular

\[
\boxed{\dim W_{1,4}=6.}
\tag{18}
\]

For `V=L_p\times W_{1,4}`, the rotundity condition already fails for the rational subspace `Q=0`, where the quotient map is the identity. Rotundity would require

\[
\dim V\ge8,
\tag{19}
\]

but

\[
\dim V=1+6=7.
\tag{20}
\]

Therefore

\[
\boxed{L_p\times W_{1,4}\text{ is not rotund}.}
\tag{21}
\]

This failure is independent of any subtler character, tropical, factorization, or boundary issue. There is simply one complex degree of freedom too little for the generic existence theorem.

AF-328 identifies exactly the same incidence analytically: `\exp(L_p)\cap W_{1,4}` is the common-zero set of the coprime exponential sums `F` and `G`. Equation `(20)` explains why passing from one equation to two changes the mathematical category of the problem. The first equation is at the exponential-algebraic solvability threshold; the second turns it into an overdetermined incidence.

## 4. Consequence for the unconditional frontier

This separates two directions in the surrounding transcendence literature.

Exponential-algebraic closedness is an **existence** principle. Gallinaro proved unconditionally that additively free rotund products `L\times W` with `L` linear meet the graph of exponentiation. The eight-prime centered problem belongs to that class.

Schanuel-type statements are **transcendence-dimension obstruction** principles. AF-333 shows conditionally that the prime-phase tuple at nonzero real time has too much algebraic freedom to satisfy the two independent algebraic equations forced by centering on the unit torus. The singular target is therefore conditionally excluded.

The middle-singular common-zero problem lies exactly between those two currencies:

\[
\text{generic EAC existence budget}=8,
\qquad
\dim(L_p\times W_{1,4})=7.
\tag{22}
\]

So the desired unconditional theorem cannot come merely from extending a generic-solvability argument already valid for rotund systems. It must exploit **special arithmetic structure of the prime-log line** strongly enough to decide a one-dimension-deficient intersection, or else prove a source-specific lower bound on algebraic/transcendence dimension comparable to the role played conditionally by Schanuel.

This also explains why several previous broad tools stop at the same place. Density of the prime flow, character-rank control, common-factor theory, and exponential-algebraic closedness all describe behaviour at or above generic dimension. None by itself decides whether this particular one-dimensional source hits this particular codimension-two target at an isolated point.

The natural neighboring language is therefore that of **unlikely/anomalous intersections**, but this statement is only a structural analogy. Standard Zilber-Pink theorems for algebraic tori concern intersections with special algebraic subgroups/cosets; `\exp(L_p)` is a transcendental one-parameter image and `W_{1,4}` is not being asserted to fall under an existing Zilber-Pink theorem.

## Prior art and novelty assessment

The decisive external result is:

- Francesco Paolo Gallinaro, **“Exponential sums equations and tropical geometry,”** *Selecta Mathematica (N.S.)* 29, 49 (2023), DOI `10.1007/s00029-023-00853-y`. Theorem 8.8 proves that every additively free rotund variety of the form `L\times W`, with `L` linear, intersects the graph of complex exponentiation; Corollary 8.10 gives Zariski density of the intersection in `W`.

The framework originates in:

- Boris Zilber, **“Exponential sums equations and the Schanuel conjecture,”** *Journal of the London Mathematical Society* 65(1) (2002), 27–44, DOI `10.1112/S0024610701002861`.

No novelty is claimed for exponential-algebraic closedness, rotundity, dimension theory, or unlikely-intersection language. The Mathia-specific contribution is the exact placement of the AF-328 prime singular gate relative to this established theory: **the first equation is an unconditional rotund existence problem; the second genuine algebraic condition drops the source-target product from dimension eight to seven and therefore exits the theorem's admissible class.**

## Boundaries and failure modes

- Gallinaro's theorem concerns complex exponentiation and supplies complex parameters `s`. It does not place a solution on the imaginary axis and therefore does not produce a real phase time `t`.
- Failure of rotundity does **not** imply nonexistence. It means the generic exponential-algebraic-closedness theorem no longer forces an intersection. Isolated common zeros remain possible.
- Calling the remaining problem “unlikely” is dimensional language, not an invocation of a proved Zilber-Pink theorem for this exact transcendental curve.
- The result is for the fixed eight-prime singular target isolated by AF-316--AF-328. It does not assert that every extra observable in every Arithmetic Fidelity problem lowers dimension by exactly one.
- The dimension calculation does not strengthen AF-333 from conditional to unconditional. It identifies why the strongest available unconditional existence theorem is on the wrong side of the boundary.
- Zariski density of `\exp(L_p)\cap W_1` does not imply topological density on the unit torus, nor does it imply any imaginary-axis zero of `F`.

## Consequence for the research line

The unconditional frontier can now be stated more sharply than “find stronger transcendence.” The exact target asks for a theorem about a **one-dimension-deficient exponential incidence**. Generic EAC is already strong enough on the immediately preceding one-equation problem and fails for a formal dimensional reason as soon as `e_4=0` is imposed.

Accordingly, further work on the AF-328/AF-333 branch should prioritize mechanisms that can cross that single missing dimension: source-specific algebraic-independence information, arithmetic restrictions on isolated exponential intersections, or a new retained mark that removes the second independent target equation. Extending generic density or generic existence machinery without changing this dimension count cannot settle the singular gate.