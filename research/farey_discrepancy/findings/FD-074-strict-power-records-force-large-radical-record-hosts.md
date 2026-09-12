# FD-074 — strict power records force large radical mass at the record host

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + POWER-RECORD-HOST-ARITHMETIC + RADICAL-LOWER-BOUND + SIGN-PARITY + FALSE-RH-RECORD-SEQUENCE`.

`FD-072` and `FD-073` use strict power records of the physical quotient-shell source

\[
\mathcal H(X)=\sum_{n\le X}c(n),
\qquad
c(n)=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}{n},
\]

as causal anchors: a `sigma`-record controls the whole source prefix and therefore protects a four-adic nonsquarefree contribution at horizon `4X`, with amplitude-length propagation around the record. Until now the arithmetic factorization of the **record index itself** played no role.

The exact increment law already forces a nontrivial host restriction. Fix

\[
0<\sigma<1,
\qquad
R_\sigma(n):=\frac{|\mathcal H(n)|}{n^\sigma},
\]

and let `X>=2` be a strict `sigma`-record:

\[
R_\sigma(X)>\max_{n<X}R_\sigma(n).
\]

Put `A=|mathcal H(X)|`. Then

\[
\boxed{
\varphi(\operatorname{rad}X)
>
XA\left[1-\left(1-\frac1X\right)^\sigma\right]
\ge \sigma A.
}
\tag{1}
\]

In particular,

\[
\boxed{\operatorname{rad}X>\sigma |\mathcal H(X)|.}
\tag{2}
\]

If `A>1`, the final increment cannot cross the origin because `|c(X)|<=1`. Hence the record value, the preceding value, and the final increment have the same sign, and therefore

\[
\boxed{
\operatorname{sgn}\mathcal H(X)
=
\operatorname{sgn}c(X)
=
\mu(\operatorname{rad}X)
=(-1)^{\omega(X)}.
}
\tag{3}
\]

Thus the power-record mechanism from `FD-072`--`FD-073` is not free to choose arbitrary source indices. Large positive records occur only at indices with an even number of distinct prime factors, large negative records only at indices with an odd number, and every large record requires squarefree-kernel mass at least proportional to its amplitude.

Under a false-RH frontier this becomes asymptotically stronger. Let

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}>\frac12
\]

and fix

\[
\frac12<\sigma<\Theta.
\]

By `FD-046`, `R_sigma` is unbounded, so there are strict record indices `X_j` with `R_sigma(X_j)->infinity`. Along every such record sequence,

\[
\boxed{
\frac{\varphi(\operatorname{rad}X_j)}{X_j^\sigma}
>\sigma R_\sigma(X_j)
\longrightarrow\infty,
}
\tag{4}
\]

and consequently

\[
\boxed{
\frac{\operatorname{rad}X_j}{X_j^\sigma}\longrightarrow\infty,
\qquad
\frac{X_j}{\operatorname{rad}X_j}
=o(X_j^{1-\sigma}).
}
\tag{5}
\]

In particular, for `sigma>1/2`, all sufficiently large strict records on such an unbounded record sequence are excluded from every prime-power family `p^a` with fixed `a>=2`; indeed `rad(p^a)=p=X^(1/a)` contradicts (5).

This does **not** supply the missing density theorem for the protected record blocks. Large-radical integers, including primes and squarefree integers, can themselves be arbitrarily sparse, and the arithmetic restriction is imposed only at strict record centers, not at every point of the amplitude-length block from `FD-073`. The result instead identifies the first exact endpoint constraint on the record mechanism coming directly from the physical coefficient law. Any attempt to turn false-RH power records into recurrent causal occupation may now use the factorization and parity of the record hosts rather than treating their locations as an arbitrary sparse subsequence.

## 1. A strict normalized record forces a large final increment

Write

\[
A:=|\mathcal H(X)|,
\qquad
B:=|\mathcal H(X-1)|.
\]

Because `X` is a strict `sigma`-record, comparison with the immediately preceding point gives

\[
\frac{A}{X^\sigma}
>
\frac{B}{(X-1)^\sigma},
\]

hence

\[
\boxed{
B<A\left(1-\frac1X\right)^\sigma.
}
\tag{6}
\]

The exact source increment is

\[
c(X)=\mathcal H(X)-\mathcal H(X-1),
\]

so the reverse triangle inequality and (6) yield

\[
\begin{aligned}
|c(X)|
&\ge A-B\\
&>A\left[1-\left(1-\frac1X\right)^\sigma\right].
\end{aligned}
\tag{7}
\]

But `FD-033` gives the physical coefficient law

\[
|c(X)|
=\frac{\varphi(\operatorname{rad}X)}{X}.
\tag{8}
\]

Multiplying (7) by `X` proves the first inequality in (1).

For `0<sigma<1`, concavity of `t^sigma` on `(0,infinity)` gives the tangent-line bound

\[
\left(1-\frac1X\right)^\sigma
\le 1-\frac\sigma X.
\tag{9}
\]

Inserting (9) into (1) proves

\[
\varphi(\operatorname{rad}X)>\sigma A.
\tag{10}
\]

Finally `phi(rad X)<=rad X`, giving (2). No asymptotic estimate or external number-theoretic input enters this argument.

## 2. Large record signs are fixed by distinct-prime parity

Since

\[
\varphi(\operatorname{rad}X)\le \operatorname{rad}X\le X,
\]

(8) implies the elementary but useful bound

\[
|c(X)|\le1.
\tag{11}
\]

Equation (6) in particular gives `A>B`. Suppose `A>1`. If `mathcal H(X)` and `mathcal H(X-1)` had opposite signs, then

\[
|c(X)|
=|\mathcal H(X)-\mathcal H(X-1)|
=A+B>A>1,
\]

contradicting (11). They therefore have the same sign. Since their magnitudes increase from `B` to `A`, the increment `c(X)` has that same sign as well. The coefficient formula then gives

\[
\operatorname{sgn}c(X)
=\mu(\operatorname{rad}X)
=(-1)^{\omega(X)},
\]

which proves (3).

The threshold `A>1` is only needed to rule out a one-step sign crossing. On the false-RH record sequences used below, `A->infinity`, so it is automatic eventually.

## 3. False RH forces super-`sigma` radical growth on its record anchors

Assume `Theta>1/2` and fix `1/2<sigma<Theta`. `FD-046` proves that `mathcal H` has polynomial growth frontier exactly `Theta`. Hence

\[
\sup_X R_\sigma(X)=\infty.
\tag{12}
\]

Choose the successive strict records whose record heights tend to infinity. At such an index `X_j`, write

\[
A_j=|\mathcal H(X_j)|
=X_j^\sigma R_\sigma(X_j).
\tag{13}
\]

Substitution into (10) gives

\[
\frac{\varphi(\operatorname{rad}X_j)}{X_j^\sigma}
>
\sigma R_\sigma(X_j),
\]

which proves (4). Since `phi(rad n)<=rad n`, the first part of (5) follows. Rearranging it gives the repeated-prime-factor estimate

\[
\frac{X_j}{\operatorname{rad}X_j}
<
\frac{X_j^{1-\sigma}}
     {\sigma R_\sigma(X_j)},
\tag{14}
\]

and the right side is `o(X_j^(1-sigma))`, proving the second part of (5).

For a prime power `X=p^a`, `a>=2`, one has `rad X=p=X^(1/a)`. Because `sigma>1/2>=1/a`, with strict inequality for every such `a`, (5) excludes prime-power record hosts eventually. The same conclusion also follows directly from (10): a strict record at `p^a` would require

\[
|\mathcal H(p^a)|<\frac{p-1}{\sigma},
\]

which is incompatible with `|mathcal H(X_j)|/X_j^sigma->infinity` when `a sigma>1`.

## 4. Relation to the current record-protection route

`FD-072` obtains a constant causal nonsquarefree occupation bound at `T=4X` from a `sigma`-record, and `FD-073` propagates that protection through a source block of radius comparable with the record amplitude. Those arguments use only prefix domination plus the one-Lipschitz increment bound once the record has been selected. Equations (1)--(5) are orthogonal information: they constrain **where the physical source is allowed to create the record in the first place**.

This is not yet enough to improve the occupation constant or prove that protected blocks have positive logarithmic density. The restriction `rad X >> X^sigma R_sigma(X)` leaves many eligible integers and gives no upper bound on the gaps between them. In particular, merely replacing the sparse centers of a synthetic tent construction by large-radical centers would not obstruct lacunarity; what such a synthetic construction still fails to satisfy is the exact physical increment law, not just (2).

The useful next question is therefore narrower than the previous generic spacing problem: can the multiplicative law

\[
c(n)=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n
\]

plus the forced endpoint conditions (1)--(5) prevent successive supercritical records from being arbitrarily multiplicatively sparse, or force enough neighboring record-quality points to make the `FD-073` causal blocks recur on logarithmic scale? A positive answer would use arithmetic information absent from `FD-039`; a negative answer would require a control preserving substantially more of the coefficient law than one-Lipschitz regularity.

## 5. Prior-art and falsification boundary

The record-step inequality (6)--(7) is elementary and no general novelty is claimed for the observation that a strict normalized record of a summatory function requires a sufficiently large final increment. The source-specific content here is the substitution of the exact physical coefficient (8), which turns that generic record fact into the radical/totient and parity constraints (1)--(5) on the causal record anchors used by `FD-072`--`FD-073`.

A targeted prior-art search found numerical literature on record values of the ordinary Mertens function, including recent large-scale computations, but no result matching this quotient-shell record-host constraint. None of that literature is load-bearing for the proof, so no new external source anchor is required.

The finding must not be read as a density statement for large-radical integers, a bound on gaps between physical records, a positive lower bound for `U_(H,D)/E_(H,D)` beyond `FD-072`, or an RH implication. It also does not constrain arbitrary near-record points in the interior of the `FD-073` block. Its exact content is only that every strict physical power-record center pays an arithmetic endpoint cost quantified by (1), with the false-RH consequences (4)--(5).
