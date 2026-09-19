# PL-371 — Reciprocal-prime-sparse Liouville defects can force a chosen real continuation obstruction arbitrarily close to 1

## Claim

The local rigidity isolated in `PL-370` does not force any uniform analytic-continuation gain to the left of `Re(s)=1`.

More precisely, fix any `sigma_0<1`. Choose a real number

`max(sigma_0,1/2) < alpha < 1`.

There is a `{+1,-1}`-valued completely multiplicative function `a_alpha` such that:

1. `a_alpha(p)=-1` at every prime outside a set `E_alpha` with

   `sum_(p in E_alpha) 1/p < infinity`;

2. its Dirichlet series

   `L(a_alpha,s)=sum_(n>=1) a_alpha(n)n^(-s)`

   is holomorphic in a neighborhood of `s=1`, has a simple zero there, and therefore satisfies the full local pole-neutral conclusion of `PL-370`;

3. nevertheless `L(a_alpha,s)` cannot admit a holomorphic continuation to the half-plane `Re(s)>sigma_0`: an explicit Euler correction forced by `E_alpha` diverges at the real point `s=alpha`, where the Liouville factor is finite and nonzero.

Thus finite pretentious distance to Liouville, even together with an actual simple zero at `s=1`, leaves enough freedom to place a real continuation obstruction at any prescribed `alpha in (1/2,1)`. A Venturini witness reaching the critical strip therefore needs genuinely global continuation input stronger than the reciprocal-prime summability forced by `PL-370`.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CONTROL + DECISIVE-NEGATIVE/OBSTRUCTION`.

No theorem-priority claim is made. The construction is elementary once `PL-370` suggests stress-testing its Liouville-like class. General Helson-zeta theory already exhibits much broader continuation programmability; the durable point here is the narrower control: the obstruction persists inside the `{+1,-1}` class at finite reciprocal-prime distance from Liouville and while preserving the required local zero at `1`.

## A sparse prime set with prescribed Dirichlet abscissa

Let `p_n` be the `n`th ordinary prime. Fix `alpha in (1/2,1)` and, after discarding finitely many initial terms if necessary, set

`q_k = p_(ceil(k^(1/alpha)))`,

and let `E_alpha={q_k:k>=k_0}`.

Because `1/alpha>1`, the indices `ceil(k^(1/alpha))` are strictly increasing for all sufficiently large `k`; deleting finitely many repeats does not affect any convergence statement below. The prime number theorem in the equivalent form

`p_n ~ n log n`

gives

`q_k ~ (1/alpha) k^(1/alpha) log k`.

Hence, for real `beta>0`,

`q_k^(-beta) asymp k^(-beta/alpha) (log k)^(-beta)`

up to an irrelevant positive constant. Consequently,

`sum_(p in E_alpha) p^(-beta) < infinity` for every `beta>alpha`,

whereas at the boundary

`sum_(p in E_alpha) p^(-alpha) = infinity`,

because it is comparable to `sum_k 1/(k (log k)^alpha)` and `alpha<1`.

In particular `1>alpha`, so

`sum_(p in E_alpha) 1/p < infinity`.

This separates two scales that `PL-370` does not identify: reciprocal-prime mass can be finite while the same selected prime set has any chosen Dirichlet convergence boundary `alpha<1`.

## A Liouville-like completely multiplicative phase

Define the prime values

`a_alpha(p)=+1` if `p in E_alpha`,

`a_alpha(p)=-1` if `p notin E_alpha`,

and extend completely multiplicatively. In exponent-lattice coordinates this is a Boolean prime-phase vector obtained from the Liouville phase `theta_p=pi` by flipping only the coordinates in `E_alpha` to phase `0`.

Since `lambda(p)=-1`, the pretentious distance appearing in `PL-370` is finite:

`D(a_alpha,lambda;infinity)^2 = sum_p (1+Re a_alpha(p))/p = 2 sum_(p in E_alpha) 1/p < infinity`.

For `Re(s)>1`, absolute convergence permits the Euler-product comparison with Liouville:

`L(lambda,s)=zeta(2s)/zeta(s)`

and

`L(a_alpha,s) = [zeta(2s)/zeta(s)] H_alpha(s)`,

where

`H_alpha(s)=product_(p in E_alpha) (1+p^(-s))/(1-p^(-s))`.

For every compact subset of `Re(s)>alpha`, the prime sum `sum_(p in E_alpha) p^(-Re(s))` converges uniformly. Therefore the Euler correction `H_alpha` converges normally there and is holomorphic and zero-free in `Re(s)>alpha`.

This factorization is initially an identity only in `Re(s)>1`; its use to the left is justified by the independently convergent product defining `H_alpha` together with the classical meromorphic continuation of `zeta(2s)/zeta(s)`. No Euler product for ordinary zeta is being continued formally across `Re(s)=1`.

## The local zero at 1 survives exactly

At `s=1`, `H_alpha(1)` is finite and strictly positive because `sum_(p in E_alpha)1/p<infinity`. Since

`zeta(2s)/zeta(s) = zeta(2)(s-1)+O((s-1)^2)`

near `s=1`, it follows that

`L(a_alpha,s) = zeta(2) H_alpha(1)(s-1)+O((s-1)^2)`.

Thus `L(a_alpha,s)` is holomorphic near `1`, has a simple zero there, and

`L'(a_alpha,1)=zeta(2)H_alpha(1) != 0`.

The exact boundary-energy identity of `PL-370` is therefore satisfied, not merely its first-order pretentious consequence. In the `{+1,-1}` case the exceptional prime set is precisely the set where `a_alpha` differs from Liouville, and its reciprocal mass is finite as required there.

So every local diagnostic supplied by `PL-370` accepts this construction as a legitimate pole-neutral Liouville-like phase.

## The chosen real obstruction at alpha

For real `sigma>alpha`, every Euler factor of `H_alpha(sigma)` is greater than `1`, and

`log H_alpha(sigma)
 = 2 sum_(p in E_alpha) [p^(-sigma) + p^(-3sigma)/3 + p^(-5sigma)/5 + ...]
 >= 2 sum_(p in E_alpha) p^(-sigma)`.

As `sigma` decreases to `alpha`, monotone convergence and the boundary divergence of the selected-prime Dirichlet series imply

`H_alpha(sigma) -> +infinity`.

The Liouville factor does not cancel this blow-up. For real `alpha in (1/2,1)`, both `zeta(2alpha)` and `zeta(alpha)` are finite and nonzero, hence

`Q(alpha):=zeta(2alpha)/zeta(alpha) != 0`.

Therefore the meromorphic continuation

`Q(s)H_alpha(s)`

has a nonremovable singularity at the real point `s=alpha` as far as holomorphy is concerned.

Suppose instead that the original Dirichlet series had a holomorphic continuation `F` to `Re(s)>sigma_0`. On `Re(s)>1`, `F=QH_alpha`. Analytic uniqueness continues this identity along a thin neighborhood of the positive real segment from `1` down to `alpha`, avoiding the isolated nonreal singularities of `Q` if necessary. Since `F` is holomorphic at `alpha` and `Q(alpha) != 0`, the quotient `F/Q` would be locally bounded and holomorphic there. But for real `sigma downarrow alpha`, that quotient equals `H_alpha(sigma)` and tends to `+infinity`, a contradiction.

Hence `L(a_alpha,s)` has no holomorphic continuation to `Re(s)>sigma_0`.

The conclusion is deliberately only about holomorphic continuation. The argument does **not** prove that `Re(s)=alpha` is a natural boundary, nor does it exclude a meromorphic continuation through `alpha`; a pole or another meromorphic singularity already suffices to defeat the Venturini-type holomorphic half-plane hypothesis being stress-tested.

## Adversarial controls

### The obstruction is source-programmed, not RH information

The real singularity comes from the deliberately chosen sparse set `E_alpha`. Its prime Dirichlet series has abscissa `alpha`, and the first term of `log H_alpha` remembers that boundary. This is exactly why the construction is a negative control rather than a candidate RH mechanism: reciprocal-prime sparsity does not prevent one from programming much finer analytic behavior at exponents below `1`.

### Existing zeta zeros do not create the argument

The contradiction uses only the positive real segment and the fact that `Q(alpha)` is finite and nonzero for `alpha in (1/2,1)`. Hypothetical nonreal zeros of zeta to the right of `alpha` could create additional poles of `Q`; they would only make holomorphic continuation harder. No zero-free hypothesis in the critical strip is used.

### Finite perturbations would not work

If `E_alpha` were finite, `H_alpha` would be a finite Euler correction and could not create the chosen boundary singularity. The construction needs infinitely many prime-axis flips, but makes them sparse enough that their total reciprocal-prime mass remains finite. This is the exact gap between the local condition in `PL-370` and global continuation.

### The half-line alpha>1/2 is intentional

Choosing `alpha>1/2` ensures the obstruction lies in the RH-relevant strip and keeps the real Liouville factor `zeta(2alpha)/zeta(alpha)` regular and nonzero. The construction can be varied outside this range, but no stronger statement is needed for the research mandate.

## Prior-art and novelty audit

The prime number theorem input `p_n~n log n`, Euler-product algebra in the absolute-convergence region, and the Liouville identity `sum lambda(n)n^(-s)=zeta(2s)/zeta(s)` are classical.

The closest broad prior-art control remains Helson-zeta flexibility. Johan Andersson's 2024 Mittag-Leffler theorem shows that completely multiplicative unimodular Euler products can realize prescribed zeros/poles and even arbitrary maximal continuation domains containing `Re(s)>1`. Bochkov's finite-value Helson constructions also show substantial flexibility with `{+1,-1}` coefficients under appropriate symmetry hypotheses. Those results are much stronger in global programmability but do not, in the audited statements, impose the specific `PL-370` condition of finite reciprocal-prime distance from Liouville together with a pole-neutral simple zero at `1`.

Accordingly, no novelty claim is made for Euler-product continuation flexibility itself. The value of the present explicit construction is as a tailored falsification test for the new `PL-370` frontier: it proves directly that its necessary local rigidity is quantitatively insufficient for every fixed continuation half-plane `Re(s)>sigma_0` with `sigma_0<1`.

Relevant stored anchors:

- `PL-003` / `SOURCES.md` Helson-zeta continuation flexibility.
- `PL-137` for pretentious prime-torus geometry and the limits of distance-only control.
- `PL-369` for Venturini's completely multiplicative zero-free witness criterion.
- `PL-370` for the pole-neutral finite-distance-to-Liouville rigidity being stress-tested here.

Fresh literature audit for this pass additionally checked Andersson's 2024 Helson-zeta continuation theorem and Bochkov's 2023 finite-value Helson-zeta construction. Neither changes the status of this finding from a derived negative control to a literature novelty claim.

## Consequence for the research line

`PL-370` sharply localizes any pole-neutral witness near the Liouville prime phase in the `1/p` geometry, but that geometry does not control where analytic continuation stops. Even within the discrete `{+1,-1}` phase cube, an exceptional prime set can have finite reciprocal mass while carrying a prescribed Dirichlet boundary `alpha` anywhere in `(1/2,1)`.

Therefore future work on the `PL-369` witness route should not try to bootstrap critical-strip continuation from

`sum_p (1+Re a(p))/p < infinity`

or from the exact local derivative identity at `s=1` alone. A surviving mechanism must control the exceptional-prime tail on every exponent scale needed to cross the strip, or supply an independent global continuation principle such as a functional equation, a trace/positivity identity, or another source-driven structure that cannot be reproduced by sparse prime-axis flips.