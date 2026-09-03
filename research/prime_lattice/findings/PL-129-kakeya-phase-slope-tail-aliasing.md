# PL-129 — Exact tail aliasing defeats the central Grosswald–Schnitzer phase slope

## Claim

`PL-127` identified the central reflection-phase slope for an admissible Grosswald–Schnitzer deformation `p_n <= q_n <= p_(n+1)`:

`D(q) = sum_n [g(p_n)-g(q_n)]`,

with

`g(x)=log(x)/(sqrt(x)-1)`.

It is positive, additive, and gives a useful low-prefix certificate when it is small. But under an arbitrary admissible integer tail it is not merely a lossy scalar summary: it has **exact tail aliases at every prime scale**.

Restrict to the binary endpoint subclass

`q_n in {p_n, p_(n+1)}`.

Write `epsilon_n=1` when `q_n=p_(n+1)` and `epsilon_n=0` when `q_n=p_n`, and define

`b_n = g(p_n)-g(p_(n+1)) > 0`.

Then

`D(q)=sum_n epsilon_n b_n`.

The full achievement set of these binary endpoint slopes is exactly

`{sum_n epsilon_n b_n : epsilon_n in {0,1}} = [0,g(2)]`.

More strongly, for every index `j` there are two admissible integer Grosswald–Schnitzer sequences that agree at every index `<j`, differ at index `j`, and have exactly the same value of `D`. One sequence has the single endpoint defect `q_j=p_(j+1)` and no later defects; the other leaves `q_j=p_j` but uses an infinite or finite subset of later endpoint defects whose slopes sum exactly to the missing `j`th contribution.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION` for scalar phase reconstruction. This closes the one-observable `D` branch of `CLUE-prime_lattice-grosswald-schnitzer-phase-fingerprint`: no amount of numerical precision in `D` can uniformly recover even one prescribed low generator against an arbitrary admissible tail. It does **not** settle whether a genuinely finite-dimensional family of independent critical-line phase observables can recover a fixed low prefix.

## Step 1: endpoint deformations turn the slope into a subsum problem

Grosswald–Schnitzer allow each real generator independently to satisfy

`p_n <= q_n <= p_(n+1)`.

In particular, the integer endpoint choices `q_n=p_n` and `q_n=p_(n+1)` are admissible. Their theorem gives a meromorphic continuation to `Re(s)>0` with the same zero divisor as `zeta`; the quotient

`phi_q(s)=Z_q(s)/zeta(s)`

is analytic and nonvanishing there. `PL-127` derives from that continued quotient, not from a formal Euler product in the critical strip, that

`D(q)=phi_q'(1/2)/phi_q(1/2)=sum_n [g(p_n)-g(q_n)]`.

For endpoint choices this becomes

`D(q)=sum_n epsilon_n b_n`,

`b_n=g(p_n)-g(p_(n+1))`.

Because `g` is positive, strictly decreasing, and tends to zero,

`sum_(k>n) b_k = g(p_(n+1))`

by exact telescoping, and

`sum_(n>=1) b_n=g(2)`.

Thus the tail is not a small perturbation in the coding sense: its total available slope after index `n` is exactly `g(p_(n+1))`.

## Step 2: every endpoint coefficient is no larger than the tail behind it

The key inequality is

`b_n <= sum_(k>n)b_k`,

which is equivalent to

`g(p_n) <= 2 g(p_(n+1))`.

For `p_n>=5`, Bertrand's postulate gives `p_(n+1)<2p_n`. Since `g` is decreasing,

`g(p_(n+1)) > g(2p_n)`.

For every real `x>=4`,

`g(x)/g(2x)
 = [log x/log(2x)] * [(sqrt(2x)-1)/(sqrt(x)-1)]`.

The first factor is `<1`. Writing `y=sqrt(x)>=2`, the second factor is

`(sqrt(2)y-1)/(y-1)`,

which decreases in `y` and is at most its value at `y=2`, namely `2sqrt(2)-1<2`. Hence

`g(x)<2g(2x)`

for `x>=4`, and therefore `g(p_n)<2g(p_(n+1))` for every prime `p_n>=5`.

The two initial cases are direct:

`g(2)/g(3) ~= 1.115 < 2`,

`g(3)/g(5) ~= 1.153 < 2`.

Consequently

`b_n <= r_n := sum_(k>n)b_k`

for every `n`.

## Step 3: the binary slope achievement set is an interval

The relevant subsum principle is classical Kakeya territory, but in this special case the proof is elementary and does not require monotonicity of the `b_n`.

Let `(a_n)` be any positive summable sequence with tail `r_n=sum_(k>n)a_k` and suppose `a_n<=r_n` for every `n`. For any target

`x in [0,sum_n a_n]`,

construct digits recursively. If the current residual is at most `r_n`, choose `epsilon_n=0`; otherwise choose `epsilon_n=1`. In the second case the new residual lies in `[0,r_n]` because `a_n<=r_n`. Since `r_n->0`, the residual tends to zero and

`x=sum_n epsilon_n a_n`.

Applying this to `a_n=b_n` gives

`{sum_n epsilon_n b_n}=[0,g(2)]`.

The same argument applied to the tail starting after any fixed `j` gives

`{sum_(n>j) epsilon_n b_n}=[0,g(p_(j+1))]`.

But Step 2 says `b_j<=g(p_(j+1))`. Therefore there exists a subset `A subset {j+1,j+2,...}` such that

`b_j=sum_(n in A)b_n`.

This equality is exact, not asymptotic.

## Step 4: exact low-generator collisions

Fix any `j`. Define deformation `Q^(1)` by

`q_j^(1)=p_(j+1)`

and `q_n^(1)=p_n` for every `n != j`. Its phase slope is

`D(Q^(1))=b_j`.

Choose the tail subset `A` supplied by Step 3 and define `Q^(2)` by

`q_j^(2)=p_j`,

`q_n^(2)=p_(n+1)` for `n in A`,

and `q_n^(2)=p_n` otherwise. Then

`D(Q^(2))=sum_(n in A)b_n=b_j=D(Q^(1))`.

The two sequences agree on the whole prefix before `j`, disagree at `j`, and are both admissible integer Grosswald–Schnitzer sequences. Therefore the scalar slope cannot decide whether the `j`th prime generator moved, even with exact infinite-precision knowledge of `D` and even when every earlier generator is known.

This is stronger than a conditioning objection. It is genuine non-injectivity caused by the admissible infinite tail.

## Validity boundary and adversarial checks

The collision uses the endpoint `q_n=p_(n+1)`. That endpoint is explicitly allowed by the Grosswald–Schnitzer hypothesis `p_n<=q_n<=p_(n+1)`. Their theorem does not require the selected `q_n` to form a strictly increasing or duplicate-free sequence; it is an independently chosen generator in each prime interval. If a future model imposes a stricter deformation class — for example `q_n<p_(n+1)` or an additional global distinctness condition — the present exact telescoping construction does not automatically survive and must be re-audited.

The infinite-tail deformation is analytically legitimate. Grosswald–Schnitzer's quotient converges locally uniformly and nonvanishingly in `Re(s)>0`, and the slope series used here is absolutely convergent; in the endpoint subclass its positive majorant even telescopes to `g(2)`.

The result is also deliberately only one-dimensional. It gives exact aliases for the first central phase derivative `D`; it does not imply that the same two sequences agree on a second derivative, on a nonzero-height phase sample, or on any prescribed finite vector of such observables. The accepted clue therefore remains open in its narrowed finite-fingerprint form.

Finally, this is not an RH mechanism. All Grosswald–Schnitzer members already have the same zero divisor as `zeta` in `Re(s)>0`. The point is diagnostic: a scalar prime-sensitive phase observable can distinguish the undeformed sequence from every deformation (`D=0` iff `q=p`) while still being incapable of locating which low generator changed once arbitrary tail changes are allowed.

## Prior art and novelty audit

Primary modified-zeta source:

- **Emil Grosswald, F. J. Schnitzer**, “A class of modified zeta and L-functions,” *Pacific Journal of Mathematics* **74**(2) (1978), 357–364. DOI: https://doi.org/10.2140/pjm.1978.74.357. Theorem 1 permits `p_n<=q_n<=p_(n+1)`, proves meromorphic continuation to `Re(s)>0`, and proves equality of the zero divisor there. Its proof constructs the nonvanishing quotient by locally uniform convergence of paired Euler-factor differences.

Classical subsum source:

- **S. Kakeya**, “On the Set of Partial Sums of an Infinite Series,” *Proceedings of the Tokyo Mathematico-Physical Society*, 2nd Series **7**(14) (1914), 250–251. DOI: https://doi.org/10.11429/ptmps1907.7.14_250.
- **Jacek Marchwicki, Piotr Miska**, “On Kakeya Conditions for Achievement Sets,” *Results in Mathematics* **76** (2021), Article 181. DOI: https://doi.org/10.1007/s00025-021-01479-2. Modern statement and discussion of the interval-filling condition for achievement sets.

A targeted search for Grosswald–Schnitzer phase data combined with Kakeya/achievement-set or subsum arguments found no prior treatment of this particular slope-aliasing synthesis. No novelty is claimed for Grosswald–Schnitzer continuation, Bertrand's postulate, or the general theory of achievement sets. The durable contribution is the exact matched-control observation that the specific positive slope of `PL-127` is interval-filled by admissible endpoint tail deformations, producing collisions at every prescribed prime index.

## Consequence for the research line

`PL-127` remains useful as a rigidity certificate: sufficiently small `D` proves that an initial prime prefix is exact, and `D=0` characterizes the undeformed Grosswald–Schnitzer sequence. The present result draws the complementary boundary. Once `D` is above the prefix threshold, it cannot be inverted to identify low defects uniformly over an arbitrary admissible tail.

Therefore further work on `CLUE-prime_lattice-grosswald-schnitzer-phase-fingerprint` should not spend effort trying to decode the deformation pattern from the central slope alone. A genuinely new result must either use at least one additional independent phase-sensitive observable and prove a tail-uniform separation theorem, or construct a corresponding exact vector-valued tail collision showing that every fixed finite fingerprint still aliases.