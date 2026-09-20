# FD-224 — Euler-window union law separates growing-block blindness from fixed-fraction coherence

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact source-fidelity reduction / growing-horizon quantifier boundary / prefix-rigidity classification / cofinal-source collapse
- **Depends on:** FD-221, FD-223
- **Classification:** `EXACT-DERIVED + REPRESENTATION-BOUNDARY + EULER-WINDOW-UNION + PREFIX-RIGIDITY + QUANTIFIER-CLARIFICATION`

## Claim

The growing switched-block countermodels of FD-222--FD-223 keep one **absolute**
Euler cutoff below the original prefix while the observation horizon grows. They
therefore do not test the stronger model in which every later horizon carries
the same positive *fractional* Euler coverage.

This distinction is exact.

Let

\[
\xi_n\in\{-1,0,1\},\qquad \xi_n^2=\mu(n)^2,\qquad \xi_1=1,
\]

and suppose that at horizons \(H_0,\ldots,H_{J-1}\) the same source is required
to obey the global Euler relations

\[
\xi_{pn}=-\xi_n
\qquad
(p\le Y_j,\ p\nmid n)
\]

for the cutoff \(Y_j\) attached to horizon \(H_j\). Put

\[
Y_*=\max_{0\le j<J}Y_j.
\]

Then the whole Euler package is exactly equivalent to the single package

\[
\boxed{
\xi_{pn}=-\xi_n
\qquad
(p\le Y_*,\ p\nmid n).
}
\]

Consequently,

\[
\boxed{\xi_n=\mu(n)\qquad(n\le Y_*).}
\]

In particular, for an earlier prefix \(N\),

\[
Y_*\ge N
\quad\Longrightarrow\quad
X(N)=M(N),
\qquad
X(x)=\sum_{n\le x}\xi_n.
\]

This is representation rigidity; no property of the switched filter is used.

For dyadic horizons \(H_j=2^jN\) with one fixed fractional cutoff
\(Y_j=\theta H_j\), \(0<\theta\le1\),

\[
Y_*=\theta 2^{J-1}N.
\]

Hence literal prefix rigidity occurs after the finite depth

\[
\boxed{
J\ge J_\theta:=1+\left\lceil\log_2\frac1\theta\right\rceil.
}
\]

Below that threshold, when \(J\) is fixed,
FD-221 supplies a blind same-source countermodel. At and above the threshold,
the source class itself has already collapsed to the physical Möbius prefix.
Thus the fixed-fraction finite-block problem has no additional
filter-dependent transition between these two regimes.

By contrast, FD-223 fixes

\[
Y_*=\beta N,\qquad 0<\beta<1,
\]

while \(J\) grows. At horizon \(2^jN\) this is only the relative fraction

\[
\theta_j=\beta 2^{-j}.
\]

The final-horizon fraction therefore tends to zero with \(J\). The
Vinogradov--Korobov-scale blindness theorem is a strong result about long
blocks under a **base-anchored absolute cutoff**, not a counterexample to
fixed positive fractional Euler coherence at every horizon.

Finally, if one permanent source is required to satisfy such exact Euler
packages along any cofinal family with \(Y_*\to\infty\), then necessarily

\[
\boxed{\xi=\mu\ \text{pointwise}.}
\]

So exact-Euler cofinal compatibility is not an unresolved source-relaxation
countermodel: it identifies the source before the Farey observable is used.
It still gives no estimate for \(M(N)\), and therefore is not itself a route
to RH.

## 1. Global Euler windows collapse to their union

For each horizon \(H_j\), the condition is global in \(n\): once a prime
\(p\le Y_j\) is selected, the relation

\[
\xi_{pn}=-\xi_n
\]

holds for every squarefree-compatible \(n\) with \(p\nmid n\). Horizon labels
do not change the relation.

Because every selected prime set is an initial prime interval, their union is

\[
\bigcup_{j<J}\{p:p\le Y_j\}
=
\{p:p\le Y_*\}.
\]

This proves the first boxed equivalence. Nothing about the order of the
horizons, the switched schedule, or the observation values enters.

Now let \(m\le Y_*\). If \(m\) is nonsquarefree, both \(\xi_m\) and \(\mu(m)\)
are zero. If

\[
m=p_1\cdots p_r
\]

is squarefree, every \(p_i\le m\le Y_*\). Starting from \(\xi_1=1\) and
applying the selected Euler relation successively gives

\[
\xi_m=(-1)^r=\mu(m).
\]

Thus exact Euler coverage through \(Y_*\) gives literal source identity on the
entire prefix through \(Y_*\).

## 2. Near literal coverage, the remaining prefix freedom has an exact prime formula

The union law also gives a useful exact description before complete coverage.
Assume

\[
\sqrt N\le Y_*<N.
\]

Any squarefree \(n\le N\) contains at most one prime factor larger than
\(Y_*\). Therefore every term on which \(\xi\) may differ from \(\mu\) has a
unique representation

\[
n=pa,\qquad p>Y_*,\qquad a\le N/p<Y_*.
\]

All prime factors of \(a\) are constrained, so repeated Euler relations give

\[
\xi_{pa}=\xi_p\,\mu(a),
\qquad
\mu(pa)=-\mu(a).
\]

Summing the difference over the prefix yields

\[
\boxed{
X(N)-M(N)
=
\sum_{Y_*<p\le N}
(\xi_p+1)
M\!\left(\left\lfloor\frac Np\right\rfloor\right).
}
\]

Thus the pre-coverage freedom is not an unspecified high-dimensional source
defect in this regime: it is exactly the collection of still-unconstrained
prime signs above \(Y_*\).

For the last half-prefix,

\[
N/2\le Y_*<N,
\]

one has \(\lfloor N/p\rfloor=1\) throughout the free-prime range, hence

\[
\boxed{
X(N)-M(N)
=
2\,\#\{p\in(Y_*,N]:\xi_p=+1\}.
}
\]

This recovers the reservoir mechanism behind the one- and two-horizon
constructions in its simplest exact form and shows why literal coverage has a
hard endpoint: once \(Y_*\) reaches \(N\), there is no free prime coordinate
left in the prefix.

## 3. Fixed fractional coherence has a finite memory length

Take

\[
H_j=2^jN,\qquad
Y_j=\theta H_j=\theta2^jN.
\]

Since the cutoffs are nested,

\[
Y_*=\theta2^{J-1}N.
\]

If

\[
\theta2^{J-1}\ge1,
\]

Section 1 forces \(\xi_n=\mu(n)\) for every \(n\le N\). The smallest such
block length is

\[
J_\theta
=
1+\left\lceil\log_2(1/\theta)\right\rceil.
\]

If instead

\[
\theta2^{J-1}<1
\]

and \(J\) is fixed, FD-221 constructs one source satisfying all Euler
relations through the latest cutoff and simultaneously keeps every switched
observation bounded while

\[
X(N)\asymp_{J,\theta}\frac{N}{\log N}.
\]

Therefore, for every fixed \(J\), the boundary is exact:

\[
\theta<2^{-(J-1)}
\quad\Longrightarrow\quad
\text{blind comparison source exists},
\]

whereas

\[
\theta\ge2^{-(J-1)}
\quad\Longrightarrow\quad
\text{the prefix is already Möbius}.
\]

There is no room between those statements for a separate transition caused
by the switched filter.

## 4. FD-223 uses fixed absolute coverage, not fixed fractional coverage

FD-223 imposes

\[
p\le\beta N
\]

for the entire block

\[
N,2N,\ldots,2^{J-1}N.
\]

In the notation above,

\[
Y_j=\beta N
\qquad\text{for every }j,
\]

so

\[
Y_*=\beta N<N
\]

independently of \(J\). Equivalently, the same absolute package occupies only

\[
\frac{Y_j}{H_j}=\beta2^{-j}
\]

of the prime scale visible at horizon \(H_j\).

This is exactly why \(J\) can grow to the Vinogradov--Korobov scale without
triggering the elementary rigidity of Section 1. The construction keeps
opening new high-prime coordinates as the observation horizon moves out, but
does not enlarge the exact-Euler window with that horizon.

The distinction matters for the live frontier. Improving the analytic
reservoir estimates in FD-223 asks how long blindness persists while the
absolute cutoff stays below \(N\). It does **not** answer how many horizons
are compatible with one fixed positive relative fidelity \(\theta\): the
latter is already bounded by \(J_\theta=O_\theta(1)\) before any analytic
estimate enters.

## 5. A cofinal exact-Euler source is automatically Möbius

Let one fixed source \(\xi\) satisfy a sequence of exact-Euler packages whose
maximal cutoffs \(Y_k\) tend to infinity. Fix any prime \(p\). Eventually

\[
p\le Y_k,
\]

so the global relation

\[
\xi_{pn}=-\xi_n
\]

holds for that prime and every admissible \(n\). Hence the permanent source
satisfies the Euler law for every prime.

Together with squarefree support and \(\xi_1=1\), this gives

\[
\xi_n=\mu(n)
\]

for every integer \(n\). No compactness argument, limiting estimate, switched
observation, or Farey identity is required.

This closes one interpretation of the previous frontier. Requiring a
**single cofinal source with eventually exhaustive exact Euler windows** does
eliminate all relaxed countermodels, but only because it has restored the
physical Möbius source by definition. It does not show that the switched
filter is coercive, nor does it provide a bound on \(M(N)\).

## Boundary and falsification

The result concerns the exact global Euler relation used in FD-215--FD-223.
If a future fidelity model enforces relations only locally in \(n\), in
average, probabilistically, or with errors, the union collapse need not hold.

The cutoffs are assumed to select all primes up to \(Y_j\). Arbitrary sparse
prime sets collapse to their set-theoretic union, but prefix rigidity then
requires that the union contain every prime factor needed for the target
prefix; its maximum alone is not sufficient.

The exact defect formula in Section 2 uses \(Y_*\ge\sqrt N\). Below that
range, integers up to \(N\) may contain several unconstrained prime factors,
so additional free-core interactions occur.

FD-221 is used only for the converse countermodel below the fixed-\(J\)
coverage threshold. FD-222--FD-223 are not reproved here.

Falsify the exact claim by producing a squarefree ternary source with
\(\xi_1=1\) that obeys every Euler relation for all primes \(p\le Y_*\) but
differs from \(\mu\) at an integer \(n\le Y_*\), by violating the displayed
prime-defect formula when \(Y_*\ge\sqrt N\), or by exhibiting a fixed
\(\theta>0\) and a dyadic block longer than \(J_\theta\) whose prefix remains
non-Möbius while all required global Euler relations hold.

## Prior-art and novelty boundary

No external theorem is needed. The union reduction and prefix-rigidity
argument are elementary consequences of the exact source representation
already used in FD-215--FD-223.

The new content is the repository-level quantifier classification: it
separates fixed absolute cutoff, fixed fractional per-horizon cutoff, and
cofinal exact-Euler compatibility, and shows that the last two cannot support
an unbounded non-Möbius same-source block for purely representation-theoretic
reasons.

## Research consequence

The FD-223 Vinogradov--Korobov ceiling remains a meaningful question only for
the **base-anchored cutoff** model \(Y_*=\beta N<N\). There one may still ask
whether reservoir capacity fails intrinsically before analytic estimates do.

The cofinal exact-Euler branch should no longer be treated as a possible
relaxed-source countermodel: once its cutoffs are exhaustive, it is simply
the Möbius source. Likewise, fixed positive fractional fidelity at every
dyadic horizon reaches literal prefix coverage after \(O_\theta(1)\)
observations.

A genuinely new persistence question must therefore avoid this tautological
collapse: for example, use a non-exhaustive or approximate multiplicative
fidelity notion, or work directly with a Farey-native statistic of the
physical Möbius source rather than expecting an indefinitely retunable exact-
Euler comparison source.
