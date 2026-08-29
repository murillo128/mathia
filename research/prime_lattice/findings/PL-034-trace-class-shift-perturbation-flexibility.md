# PL-034 — Trace-class shift perturbations do not supply arithmetic rigidity; the canonical Bost–Connes residual cocycle is zero

## Claim

The `S_1` gap left open by `PL-028` is real as an operator-ideal boundary, but **trace-class regularity by itself is not a prime-lattice mechanism**.

There are two complementary exact controls.

First, for the canonical one-sided prime action already present in the Bost–Connes representation,

```text
mu_p e_n = e_(pn),
H e_n = (log n)e_n,
R_H(z) = (H-z)^(-1),
```

one has the exact resolvent covariance

```text
mu_p^* R_H(z) mu_p = R_(H+log p)(z).
```

Hence the action-dependent relative resolvent remaining after subtracting the scalar `+log p` translation is **identically zero**:

```text
C_p(z)
 := mu_p^* R_H(z) mu_p - R_(H+log p)(z)
 = 0.
```

So the most canonical positive exponent-lattice action does not populate the nonautomatic `S_1` slot identified in `PL-028`.

Second, if one leaves the bare action and allows cocyclic/model-space perturbations of the unilateral shift semigroup, trace-class perturbation is far too flexible to select the Riemann divisor. Amosov–Baranov–Kapustin prove that prescribed singular unitary spectral components can be inserted into a cocyclic perturbation `V_t` of the shift semigroup while

```text
V_t - S_t in S_1
```

for every `t>=0`. Their construction is explicitly based on Hardy model spaces and inner functions. Conversely, in the same model, requiring the *unitary cocycle itself* to satisfy

```text
W_t - I in S_1
```

for all `t>=0` forces the model inner function to be constant, hence gives only the trivial case.

Thus, around the one-sided shift geometry relevant to Nyman/Mellin and prime-exponent actions, the ordinary trace-class condition has a two-sided failure mode:

```text
semigroup-level S_1 difference
    -> can carry prescribed spectral data; too flexible

cocycle-level S_1 difference in the ABK model
    -> trivial; too rigid

canonical Bost–Connes relative resolvent after +log p
    -> exactly zero.
```

Classical Kreĭn/boundary-triplet theory further shows that once two operators are resolvent-comparable in trace class, perturbation determinants and spectral-shift functions are standard consequences. Therefore **existence of an `S_1` relative resolvent and a Fredholm/perturbation determinant is not by itself evidence of an RH mechanism**. A viable construction must impose an additional arithmetic compatibility across the prime actions — something not forgeable by choosing an arbitrary inner/model-space spectral datum.

**Evidence/status:** `EXACT-DERIVED + LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`.

The exact Bost–Connes resolvent identity is an elementary consequence of the already-audited covariance in `PL-024`. The shift-perturbation flexibility/triviality dichotomy is literature. Perturbation determinants for trace-class resolvent-comparable extensions are classical operator theory. No novelty is claimed for any of these ingredients.

The negative is deliberately restricted to the route

```text
one-sided prime/shift action
    + trace-class relative regularity
    + generic perturbation determinant
    -> arithmetic zero localization.
```

It does **not** rule out a canonically specified prime family whose determinants satisfy new multiplicative compatibility laws, nor a noncompact adelic/scattering reference carrying additional global arithmetic structure.

## Exact test of the Bost–Connes prime action

On `ell^2(N)`, let

```text
mu_p e_n = e_(pn),
H e_n = (log n)e_n.
```

For nonreal `z`,

```text
R_H(z)e_n = 1/(log n-z) e_n.
```

Then

```text
mu_p^* R_H(z) mu_p e_n
 = mu_p^* [1/(log(pn)-z) e_(pn)]
 = 1/(log n+log p-z) e_n
 = R_(H+log p)(z)e_n.
```

Since the basis is total,

```text
boxed:
mu_p^* R_H(z) mu_p = R_(H+log p)(z).
```

This is stronger than saying that the difference belongs to `S_1`: it vanishes before any trace or determinant is taken.

Consequently the action-dependent part proposed in
`CLUE-trace-class-prime-resolvent-cocycle` is absent in the canonical positive-lattice Hamiltonian. The scalar shift part is already known from `PL-028` to have trace-class resolvent difference,

```text
R_(H+log p)(z)-R_H(z)
 = -(log p) R_(H+log p)(z)R_H(z),
```

in the Riemann-zero-density thought experiment. In the actual Bost–Connes `H=log N` model the same identity is elementary. Either way, the prime is entering only through the scalar energy translation; there is no residual cocycle to carry new arithmetic information.

This also clarifies why merely replacing the isometry by an unspecified unitary action would not be a harmless modification: exact unitary `+log p` covariance is the full-spectrum obstruction of `PL-025`.

## The natural half-line shift model is already flexible at `S_1`

The Nyman dilation semigroup of `PL-017` becomes the ordinary unilateral translation geometry after logarithmic coordinates. On the ambient half-line,

```text
(S_t f)(x)
 = f(x-t),  x>t,
 = 0,       0<=x<=t.
```

This is precisely the operator-theoretic background studied by Amosov, Baranov and Kapustin.

They consider unitary cocycles `W_t` and the perturbed isometric semigroup

```text
V_t = W_t S_t.
```

Every such cocyclic perturbation has a Wold–Kolmogorov decomposition of the form

```text
(V_t) ~= (U_t direct_sum S_t),
```

where `U_t` is a unitary semigroup. Their Theorem 1 states that for any unitary semigroup with spectral measure singular to Lebesgue measure they can choose the cocycle so that

```text
V_t-S_t in S_1,           for every t>=0,
W_t-I in S_p,             for every p>1,
```

while the prescribed `U_t` appears as the unitary component. They explicitly note the corresponding extension to arbitrary spectral measures, and their Theorem 2 gives arbitrary unitary semigroups at every `S_p`, `p>1`.

This is a strong control against treating trace-class shift perturbation as intrinsically spectral-selective. One may choose a large class of spectral data first and then realize it inside a perturbation that is trace class at the semigroup level.

In particular, if a zeta-zero spectral type can be encoded through a chosen inner/model-space function, the fact that the resulting shift perturbation lies in `S_1` does not explain the arithmetic spectrum. The information was supplied by the chosen model data.

This is conceptually parallel to `PL-033`: automorphic Lax–Phillips scattering gives a serious operator whose spectrum is the zeta zero divisor, but the divisor enters through the completed scattering function. Spectral realization and spectral localization remain distinct problems.

## At the cocycle level, `S_1` goes in the opposite direction

The same Amosov–Baranov–Kapustin paper contains an important opposite statement.

For their model-space class of cocyclic perturbations, Proposition 10 shows that if

```text
W_t-I in S_1
```

for all `t>=0`, then the inner function determining the model space is a unimodular constant. Equivalently, the nontrivial model-space contribution disappears.

The authors phrase the broader statement beyond their model as a hypothesis rather than a theorem, so it must not be promoted to a universal no-go. What *is* proved is enough for the present audit:

```text
S_1 on V_t-S_t
    -> compatible with prescribed singular spectral components;

S_1 on W_t-I for all t
    -> trivial inside their explicit model.
```

Hence there is no generic “trace-class sweet spot” in which the one-sided shift action itself suddenly becomes arithmetically rigid. The exact location of the `S_1` condition matters, and neither of these standard placements gives the desired mechanism.

## Perturbation determinants are standard once resolvent comparability is supplied

The remaining temptation is to move from semigroup differences to generators/resolvents and argue that an `S_1` relative resolvent has a determinant whose zeros might carry the desired divisor.

That operator-theory layer is classical. Malamud and Neidhardt study ordered pairs of proper extensions whose resolvent difference is trace class and construct perturbation determinants in the boundary-triplet framework. Under finite deficiency they obtain determinants expressed through the Weyl function and boundary operators; their broader trace-formula work relates these determinants to spectral-shift and characteristic functions.

The consequence for `prime_lattice` is not that such determinants are useless. It is that

```text
trace-class resolvent difference
    -> perturbation determinant / spectral shift
```

is generic extension/scattering machinery. The arithmetic burden lies in proving that the **specified prime action** forces a special determinant or special compatibility law, not in obtaining the determinant after choosing a trace-class pair.

This distinguishes a potentially meaningful future construction from a tautological one. For example, a genuinely new candidate would need something like a forced relation across primes,

```text
Delta_(mn)(z)
    determined compatibly by
Delta_m(z), Delta_n(z), v(m), v(n),
```

or an explicit prime-axis trace law that survives Beurling matched controls. Merely choosing an inner function whose zeros are the desired zeros and then invoking model-space/perturbation-determinant theory would re-encode the divisor rather than explain it.

## Relation to the local trace-class clue

`CLUE-trace-class-prime-resolvent-cocycle` survives this audit, but only in a narrower form.

The clue's simplest candidate is eliminated exactly:

```text
Bost–Connes prime isometry + log Hamiltonian
    -> residual relative resolvent cocycle = 0.
```

The model-space alternative is constrained by strong prior art:

```text
trace-class shift perturbation
    -> can be engineered with prescribed spectral components,

trace-class unitary cocycle in the explicit ABK model
    -> trivial.
```

And generic trace-class resolvent comparability already brings standard perturbation determinants.

The remaining research question is therefore not

```text
can one make the prime action trace class relative to a reference?
```

but rather

```text
can a canonically specified family of prime actions force
nonzero S_1 relative data with arithmetic compatibility
that is not freely selectable through an inner/scattering function?
```

That question is precise, falsifiable, and not settled by the cited results. It is also narrow enough to test against Beurling controls and against the completed Connes/Lax–Phillips prior art.

## Prior-art and novelty audit

Primary anchors:

- **G. G. Amosov, A. D. Baranov, V. V. Kapustin**, “On applications of the model spaces to the construction of cocyclic perturbations of the semigroup of shifts on the semiaxis,” *Ufa Mathematical Journal* **4**(1) (2012), 17–28; arXiv:1209.3435. Theorem 1 gives `V_t-S_t in S_1` while inserting prescribed singular unitary spectral data; Proposition 10 proves that `W_t-I in S_1` for all `t` forces the model inner function to be constant.

- **M. M. Malamud, H. Neidhardt**, “Perturbation determinants for singular perturbations,” *Russian Journal of Mathematical Physics* **21**(1) (2014), 55–98, DOI `10.1134/S1061920814010051`. Develops perturbation determinants for pairs of extensions with trace-class resolvent difference and expresses them through Weyl/boundary data.

The Bost–Connes covariance source is already recorded for `PL-024`, and `PL-033` already supplies the automorphic-scattering comparison.

A literature search did not find a theorem saying that the discrete rational-prime times `log p` by themselves force a nontrivial trace-class determinant law of the kind required by the narrowed clue. That absence is not evidence of novelty; it only leaves the narrowed question open.

## Boundary conditions and adversarial checks

### `S_1` flexibility does not mean every `S_1` perturbation is arbitrary

The Amosov–Baranov–Kapustin theorem is an existence/flexibility result. A particular canonically specified arithmetic perturbation could be highly rigid. The negative is against inferring arithmetic significance from the ideal membership alone.

### Proposition 10 is model-specific

The paper itself presents the corresponding universal statement as a hypothesis. Therefore `PL-034` does not claim that every trace-class unitary cocycle of every shift model is trivial. Only the explicit model-space class is used as a rigorous obstruction.

### The clue asks about relative resolvents, not merely `V_t-S_t`

That distinction is preserved. The semigroup theorem is used as a flexibility control, while Malamud–Neidhardt supply the separate resolvent-comparable determinant prior art. No implication between the two settings is asserted without proof.

### A noncompact adelic reference remains outside the negative

Connes-type adele-class/scattering systems can possess canonical global trace data unavailable to the bare half-line shift. Such a construction would have to be judged on its arithmetic content and novelty, not excluded by this result.

### A prime-family compatibility theorem would be new information

If a specified action produced trace-class relative resolvents whose spectral-shift functions or determinants obeyed a nontrivial law forced by unique factorization and whose failure were equivalent to off-line zeros, that would lie outside this negative. It is exactly the surviving target.

## Falsification tests

This finding would be falsified or materially narrowed if:

1. in the standard Bost–Connes representation,
   `mu_p^*R_H(z)mu_p != R_(H+log p)(z)`;
2. Amosov–Baranov–Kapustin do not obtain `V_t-S_t in S_1` while realizing the stated unitary spectral component;
3. their Proposition 10 allows a nonconstant model inner function with `W_t-I in S_1` for every `t>=0`;
4. trace-class resolvent-comparable extensions do not admit the perturbation-determinant framework stated above;
5. a canonical prime-lattice construction is found whose nonzero action-dependent `S_1` invariant is forced by the arithmetic prime family rather than chosen through free model/scattering data.

The first four checks are excluded by exact calculation or the cited literature. The fifth is the intended escape route, not a contradiction.

## Consequence for the research line

The `S_1` boundary from `PL-028` should no longer be treated as a promising mechanism merely because it is the first nonautomatic Schatten class.

The useful hierarchy is now:

```text
compact / S_p, p>1, resolvent covariance
    -> automatic at Riemann-zero density                 [PL-028]

canonical one-sided Bost–Connes prime action at S_1
    -> residual cocycle exactly zero                     [PL-034]

generic/model-space shift perturbation at S_1
    -> can carry prescribed spectral information         [PL-034]

generic trace-class resolvent pair
    -> determinant and spectral shift are classical      [PL-034]
```

What remains potentially meaningful is **arithmetic compatibility**, not trace-classness: a family indexed by prime directions whose relative invariants are jointly forced by multiplication, completion, and the global zeta structure. Any future work on the accepted local clue should test that joint structure directly.
