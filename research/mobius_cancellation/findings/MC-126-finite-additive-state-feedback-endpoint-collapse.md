# MC-126 — Fixed finite additive-history feedback has only endpoint circulation and reversible occupation

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
M_n=M(n),\qquad \mu_n=M_n-M_{n-1}\in\{-1,0,1\},
\]

and fix an integer `q>=1`. Retain from the entire Mertens history only the finite additive state

\[
r_n=M_n\pmod q\in\mathbb Z/q\mathbb Z.
\tag{1}
\]

Consider an arbitrary complex one-step observable

\[
\Psi(r,a),
\qquad r\in\mathbb Z/q\mathbb Z,
\quad a\in\{-1,0,1\}.
\tag{2}
\]

Then there are a periodic potential `F:Z/qZ->C`, a constant `c in C`, and a reversal-even residual `R` such that

\[
\boxed{
\Psi(r,a)=F(r+a)-F(r)+ca+R(r,a),
}
\tag{3}
\]

where

\[
R(r,1)=R(r+1,-1)
\tag{4}
\]

for every residue `r`; the zero-step values `R(r,0)=Psi(r,0)` are separate loop occupations.

Consequently the unweighted observable along the Mertens path satisfies the exact identity

\[
\boxed{
\sum_{n=1}^{N}\Psi(r_{n-1},\mu_n)
=
F(r_N)-F(r_0)+cM_N
+
\sum_{n=1}^{N}R(r_{n-1},\mu_n).
}
\tag{5}
\]

Thus a **fixed finite accumulator of the cumulative Möbius history creates no new oriented one-step carrier**. Its reversal-odd information consists only of a bounded periodic boundary term plus a constant multiple of the ordinary Mertens endpoint. Everything else is unoriented transition/loop occupation.

The same statement covers every fixed finite additive automaton whose `+1` update is an invertible state permutation `T`, whose `-1` update is `T^{-1}`, and whose zero update is the identity. Starting from any state, the reachable orbit is a finite cycle of some length `q`, so it is exactly the residue model `(1)` after relabeling.

This closes a different escape from `MC-123` and `MC-124`. `MC-123` classified feedback using the full scalar level `M_{n-1}` and found only potential plus occupation on the integer tree. `MC-124` killed fixed **sliding-window** sign-odd memory logarithmically. The present result treats fixed **cumulative** memory such as `M_{n-1} mod q`, a finite phase `exp(2 pi i M_{n-1}/q)`, or any fixed finite invertible accumulator. The finite cycle does acquire one genuine harmonic circulation class, but lifting that class back to the integer Mertens walk gives exactly `c mu_n`, whose cumulative integral is `cM_N`.

No bound for `M_N`, `D_M(N)`, or any occupation statistic follows.

## 1. Exact cycle decomposition

For each directed nonzero transition define the reversal-odd and reversal-even parts on the undirected residue edge joining `r` and `r+1`:

\[
g_r
:=
\frac{\Psi(r,1)-\Psi(r+1,-1)}2,
\qquad
s_r
:=
\frac{\Psi(r,1)+\Psi(r+1,-1)}2.
\tag{6}
\]

Set

\[
c:=\frac1q\sum_{r\in\mathbb Z/q\mathbb Z}g_r.
\tag{7}
\]

The centered edge field has zero circulation:

\[
\sum_r(g_r-c)=0.
\tag{8}
\]

Hence there is a periodic potential `F`, unique up to an additive constant, with

\[
F(r+1)-F(r)=g_r-c.
\tag{9}
\]

Define

\[
R(r,1)=s_r,
\qquad
R(r,-1)=s_{r-1},
\qquad
R(r,0)=\Psi(r,0).
\tag{10}
\]

For a forward step, `(6)` and `(9)` give

\[
\Psi(r,1)
=g_r+s_r
=F(r+1)-F(r)+c+R(r,1).
\tag{11}
\]

For a backward step,

\[
\Psi(r,-1)
=-g_{r-1}+s_{r-1}
=F(r-1)-F(r)-c+R(r,-1).
\tag{12}
\]

The zero step is immediate. This proves `(3)`, and `(10)` gives the reversal symmetry `(4)`.

Summing `(3)` along `r_n=r_{n-1}+mu_n mod q` telescopes the potential and uses

\[
\sum_{n\le N}\mu_n=M_N-M_0=M_N,
\tag{13}
\]

which proves `(5)`.

The constant `c` is exactly the normalized circulation of the reversal-odd edge field around the residue cycle. If `c=0`, the entire oriented part is a bounded periodic coboundary. If `c!=0`, the only non-coboundary oriented component is proportional to the original signed displacement of the Mertens walk.

The formulas remain valid for `q=1` and `q=2` algebraically even though the usual simple-cycle graph picture degenerates there: `(7)` still extracts the only additive circulation coefficient and `(9)` has a periodic solution because the centered increments sum to zero.

## 2. Deterministic weights expose the old Mertens path rather than a hidden finite-state gain

Let `w_1,...,w_N` be arbitrary deterministic complex weights. Applying summation by parts to the potential part gives

\[
\begin{aligned}
\sum_{n=1}^{N}w_n\bigl(F(r_n)-F(r_{n-1})\bigr)
={}&w_NF(r_N)-w_1F(r_0)\\
&+\sum_{n=1}^{N-1}(w_n-w_{n+1})F(r_n).
\end{aligned}
\tag{14}
\]

Likewise

\[
\boxed{
\sum_{n=1}^{N}w_n\mu_n
=
w_NM_N
+\sum_{n=1}^{N-1}(w_n-w_{n+1})M_n,
}
\tag{15}
\]

because `M_0=0`. Therefore

\[
\begin{aligned}
\sum_{n=1}^{N}w_n\Psi(r_{n-1},\mu_n)
={}&w_NF(r_N)-w_1F(r_0)
+\sum_{n<N}(w_n-w_{n+1})F(r_n)\\
&+c\left(
w_NM_N+\sum_{n<N}(w_n-w_{n+1})M_n
\right)\\
&+\sum_{n=1}^{N}w_nR(r_{n-1},\mu_n).
\end{aligned}
\tag{16}
\]

Since `q` is fixed, `F` is bounded. Thus deterministic reweighting of the periodic potential costs only the total variation of the chosen weights. The harmonic circulation term, however, becomes an explicit deterministic linear functional of the **original Mertens path**. A weight can make that functional useful, but then the required information has not been produced by the finite state: it has been reintroduced through the partial sums in `(15)`.

For triangular weights, for example, `(15)` becomes an ordinary signed sum of `M_n`; it does not become the first-absolute energy `sum |M_n|` unless an additional nonlinear/sign-sensitive input is supplied. The finite residue state therefore does not secretly solve the amplitude-recovery problem left by `MC-121`--`MC-125`.

## 3. Finite families of modular phases do not enlarge the oriented class

Suppose a candidate retains finitely many fixed residues

\[
M_n\pmod{q_1},\ldots,M_n\pmod{q_k}.
\tag{17}
\]

Their joint state is determined by `M_n mod Q` with

\[
Q=\operatorname{lcm}(q_1,\ldots,q_k).
\tag{18}
\]

Hence the same decomposition `(3)` applies on the single finite cycle `Z/QZ`. In particular, adding finitely many fixed Fourier phases

\[
\exp(2\pi i j M_n/q)
\tag{19}
\]

or finitely many fixed modular counters cannot create more independent oriented one-step degrees of freedom. All such reversal-odd edge fields reduce to one scalar circulation coefficient `c` plus a periodic gradient.

This is an information statement, not a claim that modular arithmetic is useless. A reversal-even occupation profile of residues or transitions can still carry nontrivial arithmetic information, and a modulus that grows with `N` can carry increasing state. What fails is the idea that **fixed finite cumulative memory by itself** supplies a new oriented feedback channel capable of remembering macroscopic excursion order.

## 4. Relationship to the current excursion frontier

`MC-125` shows that even complete translation-invariant local factor histograms through sub-square-root memory can forget the order of large excursion-producing cycle blocks. A natural repair is to add a persistent finite state that is updated along the path, so that the statistic no longer depends only on a local window.

Equation `(5)` gives the first-kill test for the simplest such repair. If the persistent state is only an additive finite quotient of cumulative Möbius increments, its oriented cycle memory is exactly the winding number of that quotient, and the winding number lifts to the integer displacement `M_N`. The state can remember **where the path is modulo a fixed period**, but not a new macroscopic orientation invariant independent of the endpoint.

A surviving state-coupled route must therefore do at least one of the following:

- let the state capacity grow with the observation scale;
- retain genuinely non-additive history rather than a finite quotient of the cumulative sum;
- use arithmetic labels, divisor/prime-factor information, or scale data not generated solely by the increment accumulator;
- or exploit the reversal-even occupation term and prove an independent Möbius-specific estimate for it.

The result does not rank these escapes. It removes only the fixed finite additive-accumulator class.

## Prior art and novelty assessment

The graph-theoretic mechanism is classical. `MC-123` already anchors the relevant edge-flow language in combinatorial Hodge theory: an edge field decomposes into gradient and cyclic/harmonic components. On a cycle graph the harmonic one-form space is one-dimensional, represented by constant circulation around the cycle. The construction `(7)`--`(9)` is exactly that elementary specialization.

Jiang, Lim, Yao and Ye, *Statistical ranking and combinatorial Hodge theory*, Mathematical Programming 127 (2011), 203--244, DOI `10.1007/s10107-010-0419-x`, is the same graph-Hodge prior-art anchor cited in `MC-123`. No novelty is claimed for Hodge decomposition, cycle cohomology, finite-state accumulators, or telescoping of additive increments.

A targeted literature audit around finite-cycle edge flows, harmonic circulation, additive cocycles, and finite-state accumulators found the standard graph-Hodge/cycle-space mechanism rather than a reason to claim a new general theorem. The durable content here is the **Möbius-line specialization and information boundary**: the apparent non-gradient cycle created by fixed cumulative modular memory lifts to the already-existing Mertens endpoint, rather than to an independent excursion carrier.

## Boundaries and falsification tests

- The state size `q` is fixed. If `q=q(N)` grows, the potential norm and state capacity may grow as well, and this result gives no uniform information bound without additional hypotheses.
- The update must be purely additive/invertible: `+1` applies one permutation, `-1` its inverse, and `0` the identity. A finite automaton whose transitions use arithmetic labels, time, prime factors, or other data is outside the theorem.
- The reversal-even residual is not declared useless. It records unoriented transition and zero-loop occupation and may be difficult to control arithmetically.
- Equation `(5)` does not make `M_N` easy to estimate. A candidate with `c!=0` has simply retained the ordinary endpoint as its unique harmonic orientation mode.
- Equation `(16)` does not forbid a useful weighted identity. It says the signed content supplied by the finite accumulator is explicitly a weighted Mertens-path functional plus bounded periodic boundary terms; any gain must come from an independent estimate of that functional or of the occupation residual.
- The result does not cover ordered growing memory, noncommutative state, multiscale state, or prime/divisor couplings.
- No analytic continuation, zero-free region, RH hypothesis, random model, or probabilistic independence is used.

The claim can be falsified by exhibiting a periodic `Psi` whose reversal-odd edge field has a second independent circulation class, or by violating the exact algebra `(6)`--`(13)`. On a single finite additive orbit neither is possible: centered edge circulation integrates to a periodic potential and the remaining harmonic coefficient is one-dimensional.

## Consequence for the line

The mean-absolute transfer frontier after `MC-123`--`MC-125` can now distinguish three kinds of memory more sharply. Fixed state-local feedback collapses to potential plus occupation; fixed sliding-window sign-odd memory lies in the qualitative logarithmic correlation class; and **fixed cumulative additive memory collapses to endpoint winding plus occupation**.

Thus merely replacing a local window by a fixed modular accumulator such as `M mod q` does not evade the existing information barriers. A new source mechanism should expose where its extra state grows, where it becomes non-additive, or which Möbius-specific occupation/arithmetic relation it controls. Otherwise its apparent orientation is a finite-state encoding of `M_N` rather than new information capable of recovering the first-absolute excursion exponent.