# AF-485 — Unbounded rightward samples are faithful for general Dirichlet sources

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `ARITHMETIC-FIDELITY`, `SAMPLING-RIGIDITY`, `PRIME-ZETA`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

Let

\[
F(s)=\sum_{n\ge1} a_n e^{-\lambda_n s},
\qquad
G(s)=\sum_{n\ge1} b_n e^{-\mu_n s},
\]

be two general Dirichlet series whose real exponent sequences are strictly increasing,

\[
\lambda_1<\lambda_2<\cdots\to+\infty,
\qquad
\mu_1<\mu_2<\cdots\to+\infty,
\]

and which both converge absolutely in a common right half-plane `Re(s)>sigma_0`. Zero coefficients may be omitted from either representation.

If there is any sequence of complex sample points `s_k` such that

\[
\operatorname{Re}(s_k)\to+\infty
\]

and

\[
F(s_k)=G(s_k)
\qquad(k\ge1),
\]

then the two generalized Dirichlet expansions are identical: after merging equal exponents, the exponent sets and their coefficients agree term by term.

Applied to Beurling-prime source sequences

\[
Q=\{q_1<q_2<\cdots\},
\qquad
R=\{r_1<r_2<\cdots\},
\]

with prime-zeta functions

\[
P_Q(s)=\sum_n q_n^{-s},
\qquad
P_R(s)=\sum_n r_n^{-s},
\]

absolutely convergent in a common right half-plane, equality on any sample sequence with `Re(s_k)->+infinity` forces

\[
Q=R.
\]

In particular, a Beurling control that agrees with the ordinary prime-zeta function on an unbounded rightward sample sequence cannot be a genuinely different generator system.

Combined with AF-484, this gives a sharp sample-cardinality boundary for this source category:

\[
\boxed{
\text{every finite exact sample family is non-faithful,}
\qquad
\text{while a countable right-unbounded sample family is faithful.}
}
\]

The second statement does **not** use analytic continuation or an interior accumulation point. The rigidity comes from the ordered exponential scales of a Dirichlet source as `Re(s)->+infinity`.

## Exact derivation

### 1. Merge the two sources into one difference series

Form

\[
H(s):=F(s)-G(s).
\]

Merge the two exponent sets `\{\lambda_n\}` and `\{\mu_n\}` into one increasing sequence

\[
\nu_1<\nu_2<\cdots\to+\infty
\]

and combine coefficients at equal exponents. After deleting any zero combined coefficients, either `H` is the zero series or

\[
H(s)=\sum_{j\ge1} c_j e^{-\nu_j s}
\]

with every `c_j\ne0` and with absolute convergence in the same common right half-plane.

Suppose for contradiction that `H` is not the zero series. Then it has a least surviving exponent `\nu_1`.

### 2. The least surviving exponent dominates uniformly to the right

Fix a real number `c>sigma_0`. If there is only one surviving term, then

\[
H(s)=c_1e^{-\nu_1s}
\]

never vanishes and the claim is immediate. Otherwise let `\nu_2>\nu_1` be the next surviving exponent.

For `sigma=Re(s)>=c`, absolute convergence gives

\[
\begin{aligned}
\left|
 e^{\nu_1s}H(s)-c_1
\right|
&\le
\sum_{j\ge2}|c_j|e^{-(\nu_j-\nu_1)\sigma}\\
&\le
 e^{-(\nu_2-\nu_1)(\sigma-c)}
 \sum_{j\ge2}|c_j|e^{-(\nu_j-\nu_1)c}.
\end{aligned}
\]

The final sum is finite because

\[
\sum_{j\ge2}|c_j|e^{-(\nu_j-\nu_1)c}
=
 e^{\nu_1c}\sum_{j\ge2}|c_j|e^{-\nu_jc}<\infty.
\]

Therefore

\[
 e^{\nu_1s}H(s)=c_1+o(1)
\]

uniformly in `Im(s)` as `Re(s)->+infinity`.

### 3. A right-unbounded zero sequence is impossible

At the assumed sample points,

\[
H(s_k)=0.
\]

Multiplying by `e^{\nu_1s_k}` and using the previous estimate gives

\[
0=e^{\nu_1s_k}H(s_k)=c_1+o(1)
\qquad(k\to\infty).
\]

Hence `c_1=0`, contradicting the construction of the merged series.

So no surviving exponent exists. The merged coefficient at every exponent is zero, and therefore `F` and `G` have exactly the same exponent-coefficient data.

This argument is stronger than a positivity argument: the coefficients may be complex and the sample points may be complex. What matters is absolute convergence, a discrete ordered exponent set, and escape of the sample real parts to `+infinity`.

## Explicit peeling for positive prime-zeta sources

For a positive discrete source

\[
P_Q(t)=\sum_{n\ge1} m_n q_n^{-t},
\qquad
1<q_1<q_2<\cdots,
\]

with finite positive multiplicities `m_n`, the same mechanism is constructive along any real sequence `t_k->+infinity`.

Indeed,

\[
P_Q(t)
=
q_1^{-t}
\left(
 m_1+
 \sum_{n\ge2}m_n(q_1/q_n)^t
\right),
\]

and the parenthesized tail converges exponentially to `m_1`. Consequently

\[
q_1
=
\lim_{k\to\infty}P_Q(t_k)^{-1/t_k},
\qquad
m_1
=
\lim_{k\to\infty}q_1^{t_k}P_Q(t_k).
\]

Subtract `m_1q_1^{-t_k}` from every sample and repeat. Every generator and multiplicity is recovered after finitely many peeling steps for each fixed index.

Thus the faithful observation is not merely an abstract analytic uniqueness set. High-exponent samples asymptotically expose the source atoms one scale at a time.

## What this changes after AF-484

AF-484 proved that **any prescribed finite family** of real prime-zeta samples can be matched exactly by a genuinely non-rational, density-matched, freely multiplicative Beurling-prime system arbitrarily close to the ordinary primes coordinatewise.

That finding left a deliberately coarse dichotomy between finite sampling and complete analytic source data. AF-485 sharpens it substantially. Full knowledge of the analytic function is unnecessary: an arbitrary sample sequence escaping to the right already kills every such source ambiguity.

Within the absolutely convergent discrete Dirichlet-source category, the observation hierarchy is therefore:

\[
\text{finite exact samples}
\;<\;
\text{right-unbounded countable samples}
\;\le\;
\text{complete analytic data},
\]

where the first level is non-faithful by AF-484 and the middle level is already faithful by the theorem above.

There are also two mathematically different infinite-sampling rigidity mechanisms:

- a sample set with an accumulation point inside the analytic domain can invoke the holomorphic identity theorem;
- a sequence with `Re(s_k)->+infinity` has no finite interior accumulation point, yet is faithful because the smallest surviving Dirichlet exponent dominates asymptotically.

The second mechanism is the one relevant here.

## Exact fidelity is not robust fidelity

The theorem is zero-error. It should not be interpreted as saying that generator recovery from large exponents is numerically well conditioned.

After the first `j-1` source atoms have been removed, the signal carrying the `j`th atom is of size approximately

\[
m_j q_j^{-t}.
\]

Therefore an additive sample error `epsilon(t)` that is not `o(q_j^{-t})` can swamp the scale needed to identify the `j`th generator by the peeling argument. Recovering progressively later atoms from progressively larger exponents demands exponentially finer absolute accuracy unless additional structure is available.

So AF-485 separates two questions that must not be conflated:

\[
\boxed{
\text{exact injectivity: yes on any right-unbounded sample sequence;}
\qquad
\text{stable/quantitative recovery: a separate problem.}
}
\]

This makes stability of arithmetic fidelity under approximate compression a concrete next theorem surface rather than a reason to weaken the exact statement.

## Prior art and novelty assessment

The uniqueness mechanism is classical.

- Tom M. Apostol, *Introduction to Analytic Number Theory*, Springer (1976), Theorem 11.3, proves for ordinary absolutely convergent Dirichlet series that equality on an infinite sequence `s_k` with `Re(s_k)->+infinity` already forces equality of every Dirichlet coefficient. The proof uses exactly the least-surviving-term domination argument specialized to exponents `log n`.
- G. H. Hardy and Marcel Riesz, *The General Theory of Dirichlet's Series*, Cambridge Tracts in Mathematics and Mathematical Physics 18 (1915), is the classical source for general Dirichlet series `sum a_n exp(-lambda_n s)` and their convergence/uniqueness theory.
- Ingo Schoolmann, **“On Bohr's theorem for general Dirichlet series,”** *Mathematische Nachrichten* 293(8) (2020), 1591–1612, DOI `10.1002/mana.201800542`, uses the modern frequency language for general Dirichlet series and explicitly treats coefficient uniqueness as necessary for identifying a Dirichlet series with its limit function.

The generalized proof above is elementary and is included to make the exact hypotheses and the escape-to-infinity mechanism explicit. No novelty is claimed for Dirichlet-series uniqueness itself.

The Arithmetic Fidelity contribution is the **boundary identification produced by combining this classical rigidity with AF-484**: in the same prime-zeta observation model, every finite exact sample family admits strong non-prime matched controls, whereas any countable sample sequence escaping to the right is source-faithful. This converts the previous vague finite-versus-complete distinction into an exact compression boundary and isolates robust recovery as the next unresolved layer.

## Boundaries and failure modes

- Absolute convergence in a common right half-plane is used essentially in the uniform tail estimate.
- The exponent supports must be discrete, strictly orderable, and tend to `+infinity`. If there is no least surviving exponent or exponents accumulate at a finite point, the proof does not apply.
- The condition is `Re(s_k)->+infinity`, not merely `|s_k|->infinity`.
- Equality of samples is exact. Approximate equality needs a quantitative stability theorem and is not covered here.
- The theorem concerns the generalized Dirichlet / prime-zeta source representation. It does not say that an arbitrary downstream zeta, determinant, spectrum, trace, or positive compression inherits the same fidelity.
- The theorem does not require prime density, free multiplicativity, integer support, a functional equation, or any specifically rational-prime axiom. Its strength comes precisely from source representation plus unbounded sampling.
- Countably many samples are sufficient, but AF-485 does not classify every infinite sample geometry. In particular, infinite sets that neither accumulate inside the analytic domain nor escape rightward remain a separate uniqueness-set question.
- Exact injectivity can coexist with extreme ill-conditioning. The existence of a mathematical inverse does not imply a useful finite-precision discriminator.

## Research consequence

Further attempts to defeat AF-484 by adding one finite batch after another are now structurally misplaced. No finite batch can work in the free Beurling control class, while an actually right-unbounded family already recovers the whole discrete source.

The sharper question is therefore quantitative: **what sampling growth and accuracy are sufficient to retain a chosen finite depth of arithmetic source information stably, and how does the required precision scale with that depth?** That is a genuine fidelity problem lying between AF-484's finite exact collapse and AF-485's infinite exact rigidity.