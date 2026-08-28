# Prime-flute findings

This is a research ledger, not a theorem list. Each entry records what was found, why it matters, and what remains to be checked.

## Index

| ID | Type | Short description | Lean priority |
|---|---|---|---|
| PF-001 | EXACT-DERIVED | exact cuff parameter and logarithmic coordinate | high |
| PF-002 | NEGATIVE/OBSTRUCTION | scalar cuff observables telescope at first order | high |
| PF-003 | LITERATURE+DERIVED | canonical shears are asymptotic log ratios of consecutive prime gaps and are unbounded both ways | high |
| PF-004 | EXACT-DERIVED | four-endpoint cross-ratio gives an exact separating geodesic length | highest |
| PF-005 | LITERATURE+DERIVED | three-gap theorem forces hyperbolic closed geodesics with length tending to zero | high |
| PF-006 | NEGATIVE/OBSTRUCTION | ordinary Selberg/Ruelle products and uniform expansion fail once primitive lengths accumulate at zero | medium |
| PF-007 | LITERATURE+DERIVED | isolated bounded prime clusters produce arbitrarily weak separating necks | high |
| PF-008 | NEEDS-AUDIT | repeated isolated-cluster right limits should inject sub-1/4 spectra into essential spectrum | low/late |
| PF-009 | NEGATIVE/OBSTRUCTION | the linearized Hecke correspondence is external, not intrinsic to the exact flute | medium |
| PF-010 | EXACT-DERIVED | trace-field degree obstruction rules out containment in finitely generated Fuchsian groups | medium |
| PF-011 | NEGATIVE/OBSTRUCTION | the one-dimensional spine zeta recovers prime zeta up to a holomorphic correction | medium |
| PF-012 | NEGATIVE/OBSTRUCTION | global first-kind/parabolic invariants are too universal to retain fine prime-gap data | low |
| PF-013 | CONJECTURAL | Poisson gap background gives logistic shears and a zero-free Gamma transform | low |
| PF-014 | LITERATURE+DERIVED | short separating geodesics define a canonical low-energy graph coupling | medium |
| PF-097 | DECISIVE-NEGATIVE | finite tangents are moduli-complete and primality-blind; PF-099 strengthens the surviving boundary | medium |
| PF-098 | DECISIVE-NEGATIVE | recurrent tangent mismatch blocks even compact relative perturbations against featureless controls; PF-099 corrects its arithmetic interpretation | medium |
| PF-099 | DECISIVE-NEGATIVE / EXACT-DERIVED | global integer dilation gives an all-composite clone of the entire projective flute and recurrent tangent hull; only nonprojective finite-scale data escape | medium |

---

## PF-001 — exact cuff coordinate

**Status:** EXACT-DERIVED, based on the standard zero-twist tight-flute length formula.

Let

```text
u_n = cot(pi / p_n)
h_n = log(u_n / u_{n-1}).
```

For the canonical cuff between consecutive endpoint scales,

```text
ell_n = 2 log((sqrt(u_n)+sqrt(u_{n-1}))/(sqrt(u_n)-sqrt(u_{n-1})))
```

and therefore exactly

```text
exp(-ell_n/2)
  = (sqrt(u_n)-sqrt(u_{n-1}))/(sqrt(u_n)+sqrt(u_{n-1}))
  = tanh(h_n/4).
```

Also

```text
sum_{n=m}^N h_n = log(u_N/u_{m-1}).
```

Using `u_p ~ p/pi` and the Baker-Harman-Pintz prime-gap bound, one obtains

```text
sum_n h_n^2 < infinity.
```

**Why it matters.** `h_n` is the natural logarithmic mesh size of the flute. It cleanly separates the telescoping first-order motion from higher-order gap fluctuations.

**Formalization target.** The finite algebraic identity and finite telescoping statement should be easy Lean targets. The square-summability consequence should be kept separate because it imports analytic number theory.

---

## PF-002 — local scalar cuff observables lose the fine gaps

**Status:** NEGATIVE/OBSTRUCTION.

Suppose a local observable has a uniform expansion near zero

```text
F(h,z) = A(z) h + O(h^2).
```

Then PF-001 plus `sum h_n^2 < infinity` gives

```text
sum_{n=m}^N F(h_n,z)
  = A(z) log(u_N/u_{m-1}) + C_F(z) + o(1).
```

Thus the divergent part only sees the two endpoints. The intermediate prime gaps survive only in a convergent correction.

Concrete examples include

```text
exp(-ell_n/2) = h_n/4 + O(h_n^3)
```

and the exact product identity

```text
prod_{n=m}^N coth(ell_n/4) = sqrt(u_N/u_{m-1}).
```

**Research consequence.** Any proposed zeta/determinant which factorizes independently cuff-by-cuff should be treated with suspicion: the construction has an explicit mechanism that removes the relational prime information.

---

## PF-003 — canonical shears retain consecutive-gap irregularity

**Status:** LITERATURE+DERIVED.

Define

```text
Delta_n = u_{n+1} - u_n
sigma_n = log(Delta_{n+1}/Delta_n).
```

This is the standard fan shear: a logarithm of a ratio of adjacent horocyclic intervals, hence a Möbius/cross-ratio coordinate rather than an ad hoc statistic.

Since

```text
cot(pi/x)' = 1/pi + O(x^-2),
```

we have

```text
Delta_n = (g_n/pi) (1 + O(p_n^-2))
sigma_n = log(g_{n+1}/g_n) + o(1).
```

Pintz proved

```text
liminf g_{n+1}/g_n = 0
limsup g_{n+1}/g_n = infinity.
```

Therefore

```text
liminf sigma_n = -infinity
limsup sigma_n = +infinity.
```

So the naturally marked prime-flute cannot be a bounded-shear perturbation of a regular fan.

There is also an exact obstruction:

```text
phi_n   = log Delta_n
sigma_n = phi_{n+1} - phi_n.
```

Hence a nearest-neighbour weight made only from `exp(-s sigma_n)` telescopes. The shear is informative as a **sequence/process**, but its raw one-step potential is a coboundary.

**Formalization target.** The coboundary/telescoping identity is immediate. The asymptotic link to gaps can be formalized independently of Pintz; the unboundedness then becomes a theorem-import layer.

---

## PF-004 — exact four-prime cross-ratio/geodesic identity

**Status:** EXACT-DERIVED. Highest-priority custom lemma.

For real endpoints

```text
a < b < c < d
```

use the standard zero-twist generator

```text
G(a,b) = 1/(b-a) * [[a+b, -2ab], [-2, a+b]].
```

Define

```text
chi(a,b,c,d) = ((c-b)(d-a))/((b-a)(d-c)).
```

Direct matrix algebra gives

```text
tr(G(a,b) G(c,d)^(-1)) = -2 - 4 chi.
```

If `L` is the translation length of this hyperbolic element, then

```text
cosh(L/2) = 1 + 2 chi
sinh(L/4)^2 = chi
L = 4 asinh(sqrt(chi)).
```

For prime endpoints take

```text
a = cot(pi/p_{i-1})
b = cot(pi/p_i)
c = cot(pi/p_j)
d = cot(pi/p_{j+1}).
```

The result is Möbius invariant and can equally be expressed as a sine cross-ratio on the original circle.

Writing

```text
X = b-a
Y = c-b
Z = d-c
```

gives the especially useful exact form

```text
sinh(L/4)^2 = Y(X+Y+Z)/(XZ).
```

**Why it matters.** This is the cleanest intrinsic bridge found so far from a relation among several prime gaps to an actual closed geodesic.

**Formalization target.** Prove determinant `1`, the trace identity, positivity of `chi`, and the elementary `trace -> length` algebra as separate lemmas.

---

## PF-005 — a tiny gap between two much larger gaps forces `sys = 0`

**Status:** LITERATURE+DERIVED; custom geometric consequence still deserves independent review.

Pintz's work on ratios of consecutive gaps includes the three-gap estimate

```text
limsup min(g_{n-1}, g_{n+1}) /
       (g_n (log n)^c) = infinity,

c = 1/632.
```

Use PF-004 on four consecutive endpoint blocks, so asymptotically

```text
chi_n
  ~ g_n/g_{n-1}
   + g_n/g_{n+1}
   + g_n^2/(g_{n-1}g_{n+1}).
```

Along the Pintz subsequence,

```text
chi_n -> 0
L_n = 4 asinh(sqrt(chi_n)) -> 0.
```

The quantitative consequence suggested by the theorem is

```text
L_n = o((log n)^(-1/1264)).
```
If the corresponding curves are recorded as the expected simple primitive separating classes, this yields

```text
sys(X_prime) = 0
```

and infinitely many distinct primitive geodesics below every fixed positive length threshold.

**Audit point.** Formal matrix length is settled by PF-004; the topological identification of each word with a simple primitive separating curve should be written as an explicit lemma rather than left implicit.

---

## PF-006 — short primitive lengths obstruct standard Selberg/Ruelle and uniform expansion

**Status:** NEGATIVE/OBSTRUCTION, conditional only on the primitive-short-geodesic conclusion in PF-005.

If primitive lengths `L_j -> 0`, the `k=0` Selberg factors satisfy for fixed `Re(s)>0`

```text
1 - exp(-s L_j) -> 0,
```

not `1`. Therefore the ordinary infinite Euler product over primitive geodesics cannot converge to a finite nonzero function in the usual way. The corresponding Ruelle inverse factors diverge.

The same geometry obstructs a faithful eventually uniformly expanding Bowen-Series-type coding. A hyperbolic periodic orbit with translation length `L_j` has multiplier tending to `1` as `L_j -> 0`; no fixed iterate can have a uniform expansion factor `>1` while retaining all such periodic orbits.

**Research consequence.** A useful dynamical object for this surface would have to be genuinely non-uniformly hyperbolic and would need a renormalization of the infinite family of short periodic orbits.

---

## PF-007 — isolated bounded clusters give arbitrarily weak necks

**Status:** LITERATURE+DERIVED; arithmetic input confirmed in Pintz arXiv:1406.2658.

Pintz proves that for every fixed `k0` there are infinitely many blocks containing at least `k0` consecutive primes in a bounded interval, preceded and followed by prime-free intervals whose lengths grow on the Erdős-Rankin scale.

For a block with geometric exterior gaps `X,Z` and bounded internal span `Y`, PF-004 gives exactly

```text
sinh(L/4)^2
  = Y(X+Y+Z)/(XZ)
  = Y(1/X + 1/Z + Y/(XZ)).
```

Thus

```text
X,Z -> infinity and Y = O(1)
    => L -> 0.
```

Using `u_q-u_p ~ (q-p)/pi`, if the arithmetic block has internal diameter `D` and exterior prime gaps `G_L,G_R`, then in the pinching regime

```text
L ~ 4 sqrt(D(1/G_L + 1/G_R)).
```

(up to the coordinate normalization already absorbed by the asymptotic ratios).

**Why it matters.** This is a direct multi-gap mechanism: a bounded prime cluster isolated by two large gaps becomes an almost-decoupled hyperbolic island.

---

## PF-008 — right-limit islands and sub-`1/4` essential spectrum

**Status:** NEEDS-AUDIT. Potentially strong, but do not use as established theorem yet.

For a fixed bounded offset pattern

```text
H = {h_1 < ... < h_k}
```

that recurs in the isolated-cluster construction, the isometries

```text
z -> pi z - P
```

send

```text
pi cot(pi/(P+h)) - P -> h.
```

The proposed picture is that the isolated finite pieces converge to a finite-area punctured-sphere limit `S_H`, while the two separating necks pinch off.

If geometric/spectral convergence is made precise, every `L^2` eigenvalue

```text
lambda in (0,1/4)
```

of a recurring `S_H` should produce a Weyl sequence in the full prime-flute, hence enter its essential spectrum. Combining large `k` with a Hersch-type test-function bound was proposed as a route to infinitely many essential spectral points below `1/4` accumulating at `0`.

**Missing checks before promotion:**

1. exact topology/cusp count and area of `S_H`;
2. a precise convergence theorem applicable to these noncompact pinching pieces;
3. the Hersch/test-function argument on the punctured metric with all domain issues stated;
4. construction of the escaping Weyl sequence in the full infinite surface.

This is a good later Lean-adjacent target only after the analytic theorem boundary is made explicit.

---

## PF-009 — the Hecke shadow is not intrinsic

**Status:** NEGATIVE/OBSTRUCTION.

If one replaces the exact endpoints by the linear shadow

```text
pi cot(pi/p)  ->  p,
```

then for consecutive odd primes `q-p=2m` the normalized generator has rational projective entries and determines, relative to `PSL(2,Z)`, a primitive Hecke double coset of degree `m`.

This produces genuine modular Hecke `L`-functions **on the modular surface**, but not on the prime-flute:

- the same matrix is a deck transformation in the group generated by the flute itself, so its own double coset is trivial;
- the exact endpoint `pi cot(pi/p)` is transcendental because it is `pi` times a nonzero algebraic number, so the exact projective matrix is not in `PGL(2,Q)`;
- a small real perturbation does not preserve membership in the modular commensurator.

**Research consequence.** The appealing chain `gap -> Hecke degree -> zeta factors` is an external arithmetic reinterpretation of the gaps, not spectral evidence about the original surface.

---

## PF-010 — infinite algebraic trace complexity; no finite-type cover hiding underneath

**Status:** EXACT-DERIVED modulo standard cyclotomic/field facts.

For consecutive endpoint values `a=u_p`, `b=u_q`, the generator trace is

```text
T_{p,q} = 2(a+b)/(b-a).
```

Hence

```text
b/a = (T_{p,q}+2)/(T_{p,q}-2).
```

Successively multiplying these ratios shows that the field generated by the canonical traces contains

```text
u_p/u_3 = sqrt(3) cot(pi/p)
```

for every odd prime `p`.

The cyclotomic degree satisfies

```text
[Q(cot(pi/p)) : Q] = p-1,
```

so the degrees of `sqrt(3) cot(pi/p)` are at least `(p-1)/2` and are unbounded.

Now suppose the prime-flute group were contained in a finitely generated subgroup of `PSL(2,R)`. Lift finitely many generators to `SL(2,R)` and let `F` be the field generated by their matrix entries. Then `F/Q` is finitely generated, and its elements algebraic over `Q` lie in a finite extension of `Q`; their algebraic degrees are therefore uniformly bounded. The canonical trace ratios above contradict this.

Proposed conclusion:

```text
Gamma_prime is not contained in any finitely generated Fuchsian group.
```

Consequently the surface cannot be a cover of a finite-type hyperbolic orbifold from which a standard automorphic spectral theory is inherited.

**Audit/formalization point.** State the lifting argument carefully so trace signs in `PSL(2,R)` cannot create an ambiguity. Formalization can be split into an elementary matrix/field lemma and a cyclotomic degree theorem.

---

## PF-011 — the spine zeta is essentially prime zeta

**Status:** NEGATIVE/OBSTRUCTION.

The zero-twist spine distance between consecutive cuffs simplifies to

```text
d_n = 1/2 (h_n + h_{n+1})
    = 1/2 log(u_{n+1}/u_{n-1}).
```

Hence the canonical radial position may be taken as

```text
R_n = 1/2 log(u_{n-1}u_n) + constant.
```

The corresponding point zeta is

```text
Z_spine(s) = sum_n (u_{n-1}u_n)^(-s/2).
```

Using `cot(pi/p)=(p/pi)(1+O(p^-2))` and summability of the gap-weighted error, the exploration obtains

```text
Z_spine(s) = pi^s P(s) + H(s),
```

where `P(s)=sum_p p^-s` is the classical prime zeta function and `H` is holomorphic for `Re(s)>0`.

**Research consequence.** This one-dimensional reduction reaches Riemann zeros only because it reconstructs a known prime Dirichlet series. It is not a new geometric mechanism for RH.

---

## PF-012 — global parabolic/Patterson-Sullivan data are universal

**Status:** NEGATIVE/OBSTRUCTION; some implications should be rechecked before theorem-level citation.

The endpoint increments satisfy

```text
sum Delta_n = infinity
```

by exact telescoping. Arredondo-Morales-Ramírez identify divergence of their endpoint-spacing series with first-kind/parabolic behavior for zero-twist tight flutes.

The working conclusion is that global objects such as

```text
critical exponent delta = 1
limit-set Hausdorff dimension = 1
Patterson-Sullivan density (after normalization) = visual/Lebesgue
```

are controlled by the universal first-kind/divergence geometry rather than the fine placement of the primes.

**Research consequence.** Compressing the entire surface to one global dimension/exponent/measure is unlikely to retain prime-gap information. The relational invariants in PF-003/PF-004 are more promising.

**Audit point.** Recheck the exact divergence-type and uniqueness hypotheses before using the Patterson-Sullivan equality as a formal theorem.

---

## PF-013 — Poisson/logistic shear background is zero-free

**Status:** CONJECTURAL as a prime model; exact as a probability calculation.

If normalized consecutive gaps are modeled as independent exponential variables `X_n` and

```text
sigma_n = log X_{n+1} - log X_n,
```

then one shear has the logistic density

```text
f(x) = 1/(4 cosh(x/2)^2).
```

With the natural hyperbolic spectral coordinate `nu=2s-1`, its moment transform is

```text
K(s) = E exp((2s-1)sigma)
     = Gamma(2s) Gamma(2-2s),
```

which converges exactly on

```text
0 < Re(s) < 1
```

and satisfies

```text
K(s)=K(1-s).
```

On the critical line,

```text
K(1/2+it) = 2 pi t / sinh(2 pi t).
```

Gamma has no zeros. Finite blocks of Poisson shears similarly give products of Gamma factors and remain zero-free.

**Interpretation.** A Poisson/logistic background can naturally reproduce the strip and reflection symmetry but not the Riemann zeros. If the shear process is relevant to RH, the zeros must come from non-Poisson arithmetic correlations rather than the main random-gap background.

---

## PF-014 — cross-ratio necks define low-energy graph couplings

**Status:** LITERATURE+DERIVED; exact use on the infinite prime-flute still needs a controlled degeneration setup.

Burger's small-eigenvalue degeneration theorem associates to pinched separating geodesics a weighted graph whose edge weight is the geodesic length and whose vertex mass is component area. In his normalization,

```text
lambda_j(surface) / lambda_j(graph) -> 1/pi.
```

Combining this with PF-004 suggests the canonical effective neck weight

```text
w(a,b,c,d)
  = L/pi
  = (4/pi) asinh(sqrt(chi(a,b,c,d))).
```

For an isolated prime cluster this is asymptotically controlled by several gaps, not one cuff:

```text
w ~ (4/pi) sqrt(D(1/G_L + 1/G_R)).
```

**Why it matters.** This is the first reasonably canonical candidate for a low-energy **cluster graph** driven by multi-gap cross-ratios rather than by the canonical cuff lengths alone.

**Caution.** Burger's theorem is a degeneration theorem for controlled families; it does not by itself prove that an infinite graph built from all prime clusters is spectrally equivalent to the full fixed prime-flute.