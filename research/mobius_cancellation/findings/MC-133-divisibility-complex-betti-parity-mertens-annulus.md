# MC-133 — Divisibility-complex Betti parity collapses to a terminal Mertens annulus

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-TAUTOLOGY`, `NO-NOVELTY-CLAIM`.

## Claim

A natural Möbius-specific escape from the generic order-forgetting obstructions `MC-122`--`MC-132` is to retain exact divisor structure rather than a finite-state summary. The most direct topological realization of that idea is already classical and, at the level of ordinary homology, does **not** reduce the global cancellation burden.

For an integer `n>=1`, let `Delta_n` be Björner's simplicial complex whose simplices are the prime-factor sets `P(m)` of squarefree integers `m<=n`. Write

\[
\beta_k(n)=\operatorname{rank}\widetilde H_k(\Delta_n;\mathbb Z).
\]

Björner proves

\[
M(n)=\sum_{k\ge0}(-1)^{k-1}\beta_k(n),
\tag{1}
\]

and, more explicitly,

\[
\beta_k(n)
=\sigma_{k+1}^{\mathrm{odd}}(n)
 -\sigma_{k+1}^{\mathrm{odd}}(n/2),
\tag{2}
\]

where `sigma_r^odd(x)` counts odd squarefree integers at most `x` with exactly `r` prime factors. Hence

\[
\boxed{
M(n)=\sum_{\substack{n/2<m\le n\\2\nmid m}}\mu(m).
}
\tag{3}
\]

Thus the alternating Betti sum of the divisibility complex is exactly the signed Möbius mass in the terminal **odd** dyadic annulus `(n/2,n]`. The topological Euler-characteristic representation is not an independent source estimate: its sign-sensitive scalar is the Mertens target itself, written in a 2-adically localized basis.

If

\[
B_0(n)=\sum_{k\ \mathrm{even}}\beta_k(n),
\qquad
B_1(n)=\sum_{k\ \mathrm{odd}}\beta_k(n),
\tag{4}
\]

then

\[
M(n)=B_1(n)-B_0(n).
\tag{5}
\]

Björner also proves

\[
B_0(n)+B_1(n)
=\sum_k\beta_k(n)
=\frac{2n}{\pi^2}+O(n^\theta)
\qquad(\theta>17/54).
\tag{6}
\]

Together with the prime number theorem `M(n)=o(n)`, this gives

\[
B_0(n)\sim B_1(n)\sim\frac{n}{\pi^2}.
\tag{7}
\]

The available unsigned homology therefore has linear mass. Reaching RH scale from this representation still requires square-root cancellation between two quantities of order `n`; bounding total Betti mass or positive combinations of the Betti numbers cannot supply that cancellation.

Finally, Björner proves that `Delta_n` is shifted and has the homotopy type of a wedge of spheres. Consequently the ordinary homotopy type of each **single** `Delta_n` is determined by the Betti multiplicities themselves. Passing from the arithmetic set to the static homotopy type does not create an extra single-scale invariant independent of the same terminal-annulus counts.

## 1. The Betti vector is a terminal odd-squarefree shell

Björner's Theorem 3.1 gives `(2)`. Since a squarefree integer of weight `r` has Möbius value `(-1)^r`, substitute `r=k+1` into `(1)`:

\[
\begin{aligned}
M(n)
&=\sum_{k\ge0}(-1)^{k-1}
  \left(\sigma_{k+1}^{\mathrm{odd}}(n)
       -\sigma_{k+1}^{\mathrm{odd}}(n/2)\right)\\
&=\sum_{\substack{n/2<m\le n\\2\nmid m\\m\ \mathrm{squarefree}}}
  (-1)^{\Omega(m)}\\
&=\sum_{\substack{n/2<m\le n\\2\nmid m}}\mu(m),
\end{aligned}
\]

which proves `(3)` directly from the literature formula.

There is also an elementary arithmetic check. Let

\[
A(x)=\sum_{\substack{m\le x\\2\nmid m}}\mu(m).
\]

Every nonzero even Möbius term has the unique form `2m` with `m` odd and squarefree, and then `mu(2m)=-mu(m)`. Therefore

\[
M(n)=A(n)-A(n/2),
\tag{8}
\]

which is exactly `(3)`. This independent derivation makes the collapse transparent: the prime `2` separates the whole Mertens sum into an odd prefix and its rescaled copy, leaving the terminal odd annulus.

## 2. Static Betti magnitude is on the wrong scale

Equation `(6)` is Björner's asymptotic theorem for the total reduced Betti number. Equation `(5)` follows from the Euler-Poincaré sign convention in `(1)`. Hence

\[
B_1(n)=\frac12\left(\sum_k\beta_k(n)+M(n)\right),
\qquad
B_0(n)=\frac12\left(\sum_k\beta_k(n)-M(n)\right).
\tag{9}
\]

The prime number theorem is equivalent to `M(n)=o(n)`, so `(6)` and `(9)` give `(7)` without any RH input.

This sharply separates **magnitude** from **parity cancellation**. Ordinary homology sees about `2n/pi^2` spheres in total, split asymptotically equally between even and odd dimensions. The hard analytic information is not the existence or abundance of homology classes; it is the exceptionally fine imbalance `B_1-B_0`. Asking for

\[
B_1(n)-B_0(n)=O_\varepsilon(n^{1/2+\varepsilon})
\]

is exactly asking for the classical Mertens RH criterion again.

## 3. Why this closes the naive divisor-topology escape

The accepted mean-absolute frontier after `MC-132` explicitly leaves **prime/divisor-labelled long-range relations** and exact multiplicative constraints open because the generic matched words do not preserve them. `Delta_n` is a clean stress test: it uses the actual rational-prime factor sets of the actual squarefree integers and therefore cannot be dismissed as another generic finite-state control.

Nevertheless, the basic topological package does not compress the source burden in the required direction:

- the full Betti vector is a partition, by prime-factor count, of the terminal odd Möbius annulus;
- its positive `l^1` mass is linear by `(6)`;
- the signed parity projection is exactly `M(n)` by `(1)`--`(3)`;
- and the static homotopy type adds no information beyond those Betti multiplicities because `Delta_n` is a wedge of spheres.

So a proposal of the form “use the topology/homology of the squarefree divisibility complex to control Mertens” is incomplete unless it identifies **additional structure whose estimate is independently cheaper than controlling the parity imbalance itself**.

This is analogous in spirit to the representation failures elsewhere in the line, but stronger in one respect: no non-arithmetic matched control is needed. The collapse occurs inside the exact Möbius/divisor object.

## Prior art and novelty assessment

The entire simplicial-complex construction, the Euler-characteristic identity `(1)`, the wedge-of-spheres theorem, the Betti formula `(2)`, and the total-Betti asymptotic `(6)` are due to Anders Björner, *A cell complex in number theory*, Advances in Applied Mathematics 46 (2011), 71--85, DOI `10.1016/j.aam.2010.09.007`, arXiv `1101.5704`. Björner explicitly notes that the Betti-number estimates do not by themselves shed new light on the growth of `M(n)`.

No novelty is claimed for translating Mertens into Euler characteristic or for the number-theoretic simplicial complex. The line-specific derived contribution is the explicit **information audit** relevant to the current frontier: combining Björner's Betti formula with Möbius parity yields the terminal-annulus identity `(3)`, which shows precisely where the basic divisor-topology representation stores the unresolved sign information and why unsigned homology is too large.

A targeted search for persistent-homology treatments of this specific Mertens filtration did not locate an established theorem turning the filtration `Delta_1 subset Delta_2 subset ...` into a stronger Mertens bound. That absence is not a novelty claim.

## Boundaries and falsification tests

- This finding kills only the **static ordinary-homology / homotopy-type** shortcut. It does not rule out additional structure on the filtration `n -> Delta_n`, inclusion maps between scales, persistent or spectral data, chain-level structure, arithmetic labels, or another invariant that is not a function of the single-scale Betti vector alone.
- Even for a wedge of spheres, nonlinear functions of the Betti vector can be defined. The obstruction is not that such functions do not exist; it is that no independent estimate for one that forces the parity imbalance has been supplied.
- Equation `(3)` is exact for integer `n`, with the inequality `n/2<m<=n` interpreted literally for integer `m`; no floor convention changes it.
- The total-Betti asymptotic `(6)` is literature input. The parity asymptotics `(7)` additionally use only the unconditional prime number theorem, not RH.
- No contour shift, continuation of `1/zeta`, random-walk independence, or zero-free-region hypothesis enters the collapse.

The exact claim can be falsified by finding an `n` for which the alternating Betti sum from `(2)` differs from the terminal odd Möbius sum in `(3)`, or by finding a contradiction to the parity decomposition `(9)`. Both identities follow algebraically from the cited formulas and the definition of `mu`.

## Consequence for the line

One of the cleanest Möbius-specific escape surfaces left after `MC-132` is now calibrated. **Exact divisor topology does not help merely by changing language:** at static-homology level it repackages the Mertens sign burden into a parity imbalance of two linear-size Betti masses, and its Euler characteristic is exactly a terminal odd dyadic Möbius sum.

The surviving topological/arithmetic possibility must therefore retain information not already collapsed by `(1)`--`(6)`. A natural residual is genuinely **inter-scale** structure of the filtration or another prime/divisor-labelled relation whose controlled statistic is demonstrably weaker than the Mertens endpoint yet still forces first-absolute amplitude. That is a distinct proof obligation, not evidence that such a mechanism exists.