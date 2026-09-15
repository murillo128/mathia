# FD-143 — Sub-root-rank observation budgets still admit a common hidden wall

- **Date:** 2026-09-15
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** main-track no-go theorem / growing information-budget lower bound
- **Depends on:** FD-132, FD-138, FD-139, FD-140, FD-142

## Claim

FD-140 shows that every fixed congruence-coordinate alphabet can miss a transverse prime-color wall. FD-142 shows the opposite extreme: a single fixed strongly additive scalar observed with `Theta(log T)` source-identity bits can reconstruct the whole squarefree prefix. The unresolved question is whether a genuinely growing but strongly sub-reconstructive observation budget already defeats the hidden-wall mechanism.

There is a quantitative negative answer in the first growing regime.

Let `X_{p,T}` be finite sets of squarefree parents `n` in a dyadic shell `T<n<=2T`, with `p` not dividing `n`, and suppose every parent in every `X_{p,T}` has

\[
\omega(n)\ge r_T,
\qquad r_T\longrightarrow\infty.
\tag{1}
\]

For each horizon let `P_T` be a finite set of active primes, with

\[
K_T:=|P_T|,
\tag{2}
\]

and for each `p in P_T` let an arbitrary source-independent observation partition `X_{p,T}` into at most `M_T` nonempty cells. No congruence, additivity, smoothness or coordinate structure is assumed for the partition.

If

\[
\boxed{
K_T M_T=o(\sqrt{r_T}),
}
\tag{3}
\]

then there exist

- one fixed infinite prime coloring `epsilon_q in {+1,-1}`;
- one fixed orientation `sigma in {+1,-1}`;
- one subsequence `T_j -> infinity`;

such that the bounded coefficient source

\[
D(n):=\sum_{q\mid n}\epsilon_q,
\qquad
b_\sigma(n):=
\begin{cases}
+1,&\sigma D(n)\ge0,\\
-1,&\sigma D(n)<0,
\end{cases}
\qquad
a_n:=\mu(n)b_\sigma(n)
\tag{4}
\]

has vanishing ancestry defect in **every observed cell for every active prime**:

\[
\boxed{
\max_{p\in P_{T_j}}
\max_{C\in\mathcal P_{p,T_j}}
\frac1{|C|}
\#\{n\in C:a_{pn}+a_n\ne0\}
\longrightarrow0.
}
\tag{5}
\]

At the same time, if one fixed prime `p_0` belongs to `P_T` eventually, then after passing to a further subsequence the same fixed source disagrees with Möbius on at least half of the corresponding parent domain up to `o(1)`:

\[
\boxed{
\frac1{|X_{p_0,T_j}|}
\#\{n\in X_{p_0,T_j}:a_n\ne\mu(n)\}
\ge \frac12-o(1).
}
\tag{6}
\]

Thus a source-independent observation scheme with total prime-cell budget below the square root of the available prime-factor rank cannot be coefficient-coercive merely by refining its conditioning cells. The obstruction is no longer restricted to a fixed congruence alphabet: it applies to **arbitrary partitions** and is realized by one common infinite source along a subsequence.

For the central Farey ancestry regime `r_T asymp log log T`, the threshold is

\[
\boxed{
K_T M_T=o(\sqrt{\log\log T}).
}
\tag{7}
\]

This is a lower-bound frontier, not a sharp transition. Nothing here shows that budgets of order `sqrt(log log T)` or larger are coercive.

## 1. Decisive test

The bounded test is deliberately stronger than another fixed-coordinate counterexample.

> Given an arbitrary finite-resolution observation partition chosen independently of the unknown coefficient source, can a single transverse prime coloring make all of its conditional ancestry defects small simultaneously when the total number of observed prime-cell constraints grows with `T`?

The answer is yes whenever (3) holds.

The mechanism is an anti-concentration budget. On a parent with `k=omega(n)` prime factors, a random prime coloring makes `D(n)` a length-`k` Rademacher sum. An ancestry sign change can occur only at one of the two central lattice levels. Each such level has probability `O(k^{-1/2})`. Summing this cost over all observed prime-cell constraints gives precisely the product `K_T M_T / sqrt(r_T)`.

The second part of the test is essential: the coloring must not be re-chosen independently at each horizon. A subsequence argument below produces one fixed infinite coloring and then one fixed orientation of it.

## 2. Exact edge law

Let `epsilon_q in {+1,-1}` be any prime coloring. For squarefree `n` and a prime `p` not dividing `n`,

\[
D(pn)=D(n)+\epsilon_p.
\tag{8}
\]

For the positive orientation define

\[
b_+(n)=
\begin{cases}
+1,&D(n)\ge0,\\
-1,&D(n)<0.
\end{cases}
\tag{9}
\]

Because `mu(pn)=-mu(n)`,

\[
a_{pn}+a_n
=
\mu(n)\bigl(b_+(n)-b_+(pn)\bigr).
\tag{10}
\]

Hence the defect has magnitude either `0` or `2`. More precisely,

\[
|a_{pn}+a_n|=2
\quad\Longleftrightarrow\quad
\begin{cases}
D(n)=-1,&\epsilon_p=+1,\\
D(n)=0,&\epsilon_p=-1.
\end{cases}
\tag{11}
\]

For the reversed coloring `-epsilon`, the corresponding two cases become

\[
|a^{(-)}_{pn}+a^{(-)}_n|=2
\quad\Longleftrightarrow\quad
\begin{cases}
D(n)=0,&\epsilon_p=+1,\\
D(n)=1,&\epsilon_p=-1.
\end{cases}
\tag{12}
\]

Thus the two orientations together expose at most three central levels `-1,0,1`; in particular they always include the zero level. This exact edge identity is the same thin-wall mechanism behind FD-138--FD-140, but no arithmetic structure is imposed on the conditioning cells here.

## 3. Rademacher anti-concentration is uniform over arbitrary cells

Now choose the prime colors independently and uniformly from `{+1,-1}`. Fix a horizon `T`, an active prime `p`, a cell `C` of its observation partition, and a parent `n in C` with

\[
k:=\omega(n)\ge r_T.
\tag{13}
\]

Since `p` does not divide `n`, the random variable `epsilon_p` is independent of

\[
D(n)=\sum_{q\mid n}\epsilon_q.
\tag{14}
\]

The latter is a sum `S_k` of `k` independent Rademacher signs. Its largest point mass is the central binomial mass, so for an absolute constant `A`,

\[
\sup_{s\in\mathbb Z}\Pr(S_k=s)
\le \frac{A}{\sqrt{k}}
\le \frac{A}{\sqrt{r_T}}.
\tag{15}
\]

Equation (11) therefore gives

\[
\Pr(a_{pn}+a_n\ne0)
\le \frac{A}{\sqrt{r_T}}.
\tag{16}
\]

Averaging over `n in C` requires no independence between different parents:

\[
\mathbb E\left[
\frac1{|C|}
\#\{n\in C:a_{pn}+a_n\ne0\}
\right]
\le
\frac{A}{\sqrt{r_T}}.
\tag{17}
\]

The same estimate holds for the reversed coloring. This is why the observation cells may be completely arbitrary. The proof never asks how the cell was defined; it uses only that the partition was fixed independently of the random hidden coloring.

## 4. The total observation budget is the number of constraints

Write `E_{sigma,p,C}(epsilon)` for the normalized defect fraction in cell `C` for orientation `sigma in {+1,-1}`. Set

\[
W_T(\epsilon)
:=
\sum_{\sigma=\pm1}
\sum_{p\in P_T}
\sum_{C\in\mathcal P_{p,T}}
E_{\sigma,p,C}(\epsilon).
\tag{18}
\]

There are at most `2 K_T M_T` terms. From (17),

\[
\mathbb E W_T
\le
\frac{2A K_T M_T}{\sqrt{r_T}}
=:\delta_T.
\tag{19}
\]

Under (3),

\[
\delta_T\longrightarrow0.
\tag{20}
\]

For a single horizon, (19) already proves by the probabilistic method that some coloring makes the **sum** of every observed conditional defect at most `delta_T`; hence each individual defect is at most `delta_T`.

That finite-horizon statement is not enough for Mathia's common-source requirement, because a different coloring at every `T` would only be a horizonwise matched control. The next step removes that weakness.

## 5. One infinite coloring works along a subsequence

Choose a subsequence, still denoted `T_j`, so sparse that

\[
\delta_{T_j}\le2^{-3j}.
\tag{21}
\]

By Markov's inequality,

\[
\Pr\bigl(W_{T_j}>2^{-j}\bigr)
\le
\frac{2^{-3j}}{2^{-j}}
=2^{-2j}.
\tag{22}
\]

The tail union bound gives

\[
\Pr\left(
\text{some }j\ge J\text{ has }W_{T_j}>2^{-j}
\right)
\le
\sum_{j\ge J}2^{-2j}
\longrightarrow0.
\tag{23}
\]

Therefore there exists one fixed infinite coloring `epsilon` for which

\[
W_{T_j}(\epsilon)\le2^{-j}
\tag{24}
\]

for all sufficiently large `j`. Since every term in (18) is nonnegative, (24) implies simultaneously for **both orientations**

\[
\max_{p\in P_{T_j}}
\max_{C\in\mathcal P_{p,T_j}}
E_{\sigma,p,C}(\epsilon)
\le2^{-j}
\qquad(\sigma=\pm1).
\tag{25}
\]

This is stronger than selecting a fresh random coloring at each horizon. The prime colors are fixed once and for all; only the subsequence is selected.

## 6. One fixed orientation remains macroscopically wrong

It remains to prevent (25) from being vacuous because the chosen source happened to converge back to Möbius.

Assume that one fixed active prime `p_0` belongs to `P_{T_j}` for all sufficiently large `j`. Let

\[
z_j
:=
\frac1{|X_{p_0,T_j}|}
\#\{n\in X_{p_0,T_j}:D(n)=0\}.
\tag{26}
\]

For every cell of the `p_0` partition, equations (11)--(12) show that the zero level is a defect level for one of the two orientations. Consequently (25) implies

\[
z_j\le W_{T_j}(\epsilon)\le2^{-j}.
\tag{27}
\]

Let `f_{+,j}` be the fraction of `X_{p_0,T_j}` where the positive-orientation source differs from Möbius, and let `f_{-,j}` be the analogous fraction for the reversed coloring. By definition,

\[
f_{+,j}
=
\Pr_{X_{p_0,T_j}}(D<0),
\qquad
f_{-,j}
=
\Pr_{X_{p_0,T_j}}(D>0).
\tag{28}
\]

Hence

\[
f_{+,j}+f_{-,j}=1-z_j
\ge1-2^{-j}.
\tag{29}
\]

For every `j`, at least one orientation therefore satisfies

\[
f_{\sigma,j}\ge\frac12-2^{-j-1}.
\tag{30}
\]

There are only two orientations. One of them satisfies (30) for infinitely many `j`. Pass to that infinite subsubsequence and fix this orientation once and for all. Equation (25) survives the restriction, while (30) becomes exactly (6).

Thus both properties belong to one fixed coefficient source: all observed ancestry defects vanish, yet the source remains macroscopically separated from Möbius on one of the parent domains being tested.

## 7. Central-rank Farey corollary

In the central multiplicative regime used in FD-139, squarefree parents have

\[
\omega(n)=\log\log T+O(\sqrt{\log\log T})
\tag{31}
\]

through the standard central window. In particular the minimum rank in any fixed central window is

\[
r_T\asymp\log\log T.
\tag{32}
\]

Therefore (3) becomes

\[
K_T M_T=o(\sqrt{\log\log T}).
\tag{33}
\]

For fixed `K_T`, any source-independent conditioning alphabet with

\[
M_T=o(\sqrt{\log\log T})
\tag{34}
\]

can still be defeated by one common prime-color source along a subsequence, even if its cells are chosen by an arbitrary nonlinear rule rather than by congruences or additive coordinates.

Conversely, if the number of tested primes grows, the theorem prices that growth explicitly: the relevant elementary budget is the product `K_T M_T`. This product appears because the proof must make every prime-cell conditional defect small simultaneously.

The standard central window has positive asymptotic mass in the squarefree dyadic shell by the same central prime-factor distribution already used and audited in FD-138--FD-139. Thus, when `X_{p_0,T}` is that central parent window with one fixed excluded prime, (6) represents a genuine positive-mass coefficient defect, not merely a sparse exceptional set.

The theorem itself does not need that distributional input: (1)--(6) are finite-set statements once the parent domains are specified.

## 8. Harmonic weights and higher defect moments

The same obstruction survives the weighted ancestry means used elsewhere in the line. On `T<n<=2T`,

\[
\frac1{2T}<\frac1n\le\frac1T.
\tag{35}
\]

Therefore weighted and unweighted cell proportions differ by at most an absolute factor. If a defect fraction tends to zero, so does its `1/n`-weighted analogue.

Likewise, because every nonzero edge defect has magnitude exactly `2`, for each fixed `1<=s<infinity`,

\[
\frac1{|C|}
\sum_{n\in C}|a_{pn}+a_n|^s
=2^s E_{\sigma,p,C}.
\tag{36}
\]

Thus (5) is not an artifact of choosing an `L^1` ancestry statistic. Every fixed finite moment of the cellwise defect vanishes under the same budget.

As in FD-135, an `L^infinity` law is different: if a cell contains even one boundary edge, its supremum defect is still exactly `2`. Nothing in FD-143 weakens that rigidity distinction.

## 9. What has changed after FD-142

FD-142 showed that `Theta(log T)` source-identity bits suffice for complete squarefree reconstruction, so finite dimension and polynomial numerical precision were not meaningful intermediate restrictions by themselves. That left a large logical gap: perhaps even a very slowly growing non-reconstructive alphabet already defeats every hidden wall.

FD-143 rules out the first part of that gap. A genuinely growing observation can remain far too weak even when its cells are arbitrary. In the central rank regime, total prime-cell complexity

\[
o(\sqrt{\log\log T})
\tag{37}
\]

still cannot force the thin prime-color boundary to occupy a visible fraction of any observed cell.

This is qualitatively stronger than FD-140 in three ways:

1. the observation cells need not come from congruence classes or from any additive coordinate;
2. their number may grow with the horizon;
3. one fixed infinite coefficient source defeats the whole scheme along a subsequence.

The proof also identifies why `sqrt(log log T)` appears: it is the reciprocal point-mass scale of a rank-`log log T` Rademacher sum, not an information-theoretic source-identity threshold.

## 10. Boundary and adversarial audit

Several limitations are essential.

First, (33) is only a **one-sided lower bound** on the observation budget. The argument says nothing when `K_T M_T` is comparable to or larger than `sqrt(log log T)`. It does not show that this scale is sufficient, natural, or sharp.

Second, the observation partitions must be fixed independently of the hidden prime coloring. A cell definition allowed to inspect the unknown coefficients can simply encode the defect set and is circular for the same reason as the source-label coordinate in FD-142.

Third, the theorem uses a subsequence. This is enough to rule out a uniform asymptotic coercivity principle under the stated budget, but it does not claim that every horizon is simultaneously bad for the same coloring.

Fourth, the simultaneous prime budget is finite at each horizon. The theorem allows `K_T` to grow, but only subject to (3). It does not handle conditioning against all primes up to `T`.

Fifth, the positive-mass statement for a standard central window uses the already-audited prime-factor distribution from FD-138--FD-139. The core arbitrary-partition theorem does not depend on that asymptotic input.

Finally, no claim is made that the random-color source is generated by the physical Farey observable. As in FD-138--FD-140, it is a matched control showing what the proposed ancestry information does **not** determine. A positive theorem can escape the obstruction by imposing a genuinely source-native restriction that excludes these colorings, or by proving coercivity directly on the destination-side Fourier skeleton.

## 11. Prior-art and novelty audit

The probabilistic ingredients are standard: central-binomial anti-concentration for a Rademacher sum, Markov's inequality, a summable tail union bound, and the probabilistic method. Classical probabilistic number theory studies additive functions and random prime signs extensively. No novelty is claimed for those ingredients.

The durable delta is Mathia-specific: combining the exact ancestry edge law of FD-138--FD-140 with a growing arbitrary observation partition yields the explicit resource inequality

\[
K_T M_T=o(\sqrt{r_T}),
\tag{38}
\]

and, crucially, one common infinite source along a subsequence. A prior-art search did not identify an existing theorem phrased as this Farey coefficient-coercivity lower bound. Since the proof above is elementary once the previous FD edge law is available, no new external result is load-bearing and no new source anchor is required.

## 12. Next live question

The information-capacity gap is now quantitative.

At one end, FD-143 proves that arbitrary source-independent observation budgets below `sqrt(log log T)` prime-cell constraints remain noncoercive in the central ancestry regime. At the other, FD-142 shows that `Theta(log T)` source-identity bits can reconstruct every squarefree parent.

The next decisive question is therefore not whether the alphabet is merely finite or growing. It is whether a **source-native** Farey/Fourier observable can cross the sub-root-rank obstruction without becoming a disguised source label. Two concrete routes remain:

- prove a stronger hidden-wall theorem for much larger effective alphabets by exploiting structure beyond the elementary union budget; or
- identify a Farey-derived coordinate/certificate with resolving capacity above (38) and prove that its extra information is genuinely noncircular and coefficient-coercive.

A destination-side Fourier coercivity theorem remains a separate escape because it need not identify the coefficient source cell by cell.