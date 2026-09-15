---
id: CLUE-prime-lattice-pascal-block-gcd-arithmetic-gain
type: research-clue
status: proposed
origin: research-watch
target_line: prime_lattice
based_on:
  - research/prime_lattice/README.md
---

# Can compatibility between Pascal blocks yield an independent prime-power interval estimate?

## Observation

Pascal's additive construction gives a concrete object in the line's prime-exponent lattice: the gcd of several entries is their coordinatewise minimum in every prime valuation. For integers $n\ge2$ and $0\le b<n/3$, put $H=b+1$ and

$$
B_{n,k}=\binom nk,\qquad
D_n(b)=\gcd_{H\le k\le n-H}B_{n,k},\qquad
v_p(D_n(b))=\min_{H\le k\le n-H}v_p(B_{n,k}).
$$

Theorem 9 and equations (6)--(7) of Gil Kaplan and Dan Levy, [*GCD of truncated rows in Pascal's triangle*, Integers 4 (2004), A14](https://emis.dsd.sztaki.hu/journals/INTEGERS/papers/e14/e14.pdf), specialize to

$$
D_n(b)=\prod_{\substack{p\ \mathrm{prime},\ a\ge1\\n-b\le p^a\le n}}p.
$$

Their notation is $g(n,H)=D_n(b)$. The restriction $b<n/3$ eliminates their positive-type factors; it must not be extended silently. In particular, with natural logarithms and $\psi(x)=\sum_{p^a\le x}\log p$,

$$
\log D_n(b)=\psi(n)-\psi(n-H).
$$

The full-interior identity $\log D_n(0)=\Lambda(n)$ is classical; see also Carl McTague, [*On the Greatest Common Divisor of Binomial Coefficients*, arXiv:1510.06696](https://arxiv.org/abs/1510.06696). Thus [DLMF 27.4.12](https://dlmf.nist.gov/27.4.E12) gives $\sum_{n\ge2}\log D_n(0)n^{-s}=-\zeta'(s)/\zeta(s)$ for $\Re s>1$. These are prior-art bridges, not discoveries or a continuation argument.

## Research question

Can an explicitly identified compatibility constraint among coefficients or neighboring blocks, derived from actual Pascal addition, produce a uniform interval estimate beyond the single-coefficient bound

$$
0\le\log D_n(b)\le\log\binom nH\le H\log(en/H),
$$

without importing a prime-counting, prime-gap, or cancellation estimate of comparable strength?

The first target is a proved inequality $\log D_n(H-1)\le U(n,H)$ with explicit constants, hypotheses, and a growing parameter range, together with a quantified improvement over the displayed baseline. A lower bound forcing $D_n(b)>1$ is a distinct possible outcome and must state exactly which range it covers. Start with the joint valuation constraints of several coefficients; when valuations alone lose essential information, identify the specific residue or additive-compatibility data required. Do not assume independent carries across different primes.

## Why it may matter

An independently bounded block gcd immediately bounds the weighted prime-power mass in a specified integer interval. This would turn the additive construction into a source of an arithmetic estimate, rather than merely an alternative encoding of the same prime data. The candidate therefore belongs to the mandate's mixed additive/multiplicative question, even though no transfer to the line's completed-Weil endpoint or sign problem has been established.

Exact recovery of $\psi$ only identifies the target. The missing ingredient is a constraint on the actual Pascal array that can be estimated without first evaluating the corresponding prime-power interval. Any compressed or averaged representation must retain the information used by the proposed inequality.

## Decisive test

1. **Remove already-classified local structure from the novelty claim.** Kaplan--Levy's Theorems 5 and 7 already classify a neighboring-block lcm recurrence and its defect. In the present range, for $1\le b<n/3$, they imply

   $$
   D_n(b)=\operatorname{lcm}\bigl(D_{n-1}(b-1),D_n(b-1)\bigr).
   $$

   Reconstructing this recurrence or its prime-power boundary values is calibration, not a new mechanism. Elementary adjacent-coefficient gcd identities, classical binomial proofs of prime estimates, and applicable sieve bounds are additional comparison baselines.

2. **Produce one auditable gain.** Specify the coefficients, rows, and retained arithmetic data used by the argument; derive the proposed $U(n,H)$ or positive lower bound before translating it into $\psi$. Give the exact quantifiers and scale dependence. Compare both with the single-coefficient bound and with prior-art estimates on the same range. A finite improvement obtained just by computing the gcd, or a known two-coefficient simplification, does not establish a new uniform arithmetic estimate. Explicitly identify any stronger prime-distribution input used in the derivation so the conclusion cannot be recycled as a premise.

3. **Test the information source.** For an argument using only the lcm recurrence, replace its boundary by arbitrary positive integers $F(n,0)=a_n$ and propagate $F(n,b)=\operatorname{lcm}(F(n-1,b-1),F(n,b-1))$ on the same triangular domain. Determine which proposed inference survives this substitution and which step genuinely uses Pascal coefficients. This is a control for recurrence-only reasoning, not a counterfeit Pascal triangle. Any obstruction must specify all retained hypotheses and exhibit a model satisfying them; failure of this weakened model is not a no-go theorem for the full additive array.

4. **Preserve the precise outcome.** A useful result is a proved, literature-audited inequality with its arithmetic consequence, or a proved insufficiency statement for a named family of retained constraints. If the candidate reduces to known identities with no residual mechanism, record that exact reduction rather than escalating it into a new zeta reformulation. An unfinished proof or unsuccessful search leaves the question unresolved; it is not a refutation.

## Evidence boundary

This is an untriaged research clue. The identities and the lcm recurrence above are classical; the requested independent estimate is not established here. Prime powers are not interchangeable with primes, and the interval endpoints are $n-H<m\le n$. No cancellation bound, short-interval existence result, RH implication beyond the classical arithmetic dictionary, or analytic continuation from $\Re s>1$ is claimed. Numerical checks from the originating conversation are not used as proof or as repository evidence.
