# PL-044 — Localized Weil spectral reality is arithmetic-insensitive before prime-power activation

## Claim

The newest localized-Weil operator work sharpens the negative boundary already visible in `PL-013` and `PL-043`: **finite-stage self-adjointness and real-zero characteristic functions can appear before any prime-exponent data is active, and therefore cannot themselves be the arithmetic rigidity that would force RH.**

For the completed Weil functional, the non-archimedean terms are

```text
-sum_n Lambda(n)/sqrt(n) f(log n)
-sum_n Lambda(n)/sqrt(n) f(-log n),
```

with `Lambda(n)` supported exactly on prime powers. If

```text
v in C_c^infinity(-a,a),
f = v * v_tilde,
```

then the convolution is supported strictly inside the diameter-two window:

```text
supp(f) subset (-2a,2a).
```

Hence the arithmetic part of the localized quadratic form `Q_W^a(v)=W(v*v_tilde)` can use only prime powers satisfying

```text
log(p^m) < 2a.
```

In exponent coordinates the active scale filtration is

```text
A(a) = { m e_p : m log p < 2a }.
```

Arithmetic can therefore change only when the aperture crosses an axis-ray threshold

```text
a = (m log p)/2.
```

In particular,

```text
2a < log 2
    => A(a) is empty
    => every von-Mangoldt / prime-power term in Q_W^a vanishes identically.
```

This is an exact support statement, not a numerical observation and not an Euler-product continuation. At the equality `2a=log(p^m)`, a compactly supported test function still has zero autocorrelation at that endpoint; the corresponding prime-power term becomes available only after the threshold is crossed.

Masatoshi Suzuki's 2026 screw-function formulation supplies the decisive spectral control. For every fixed `a>0`, the localized closed Weil form has a canonical lower-bounded self-adjoint operator `A_a`. More importantly, after choosing `lambda<lambda_a` and completing the test functions in the positive form norm, the minimal differential operator

```text
D_a = i d/dx
```

has deficiency indices `(1,1)`. Suzuki proves that every self-adjoint extension `Dbar_(a,theta)` has an entire characteristic function `W(a,theta;z)` whose zeros are exactly its eigenvalues and hence are all real. The theorem is unconditional. Suzuki explicitly notes that its proof does **not** require detailed information about the arithmetic terms of the Weil form; it uses essentially only that the prime contribution is finite at fixed `a`.

Consequently, in the prime-free regime `2a<log 2`, one already has the same basic Hilbert--Polya-looking package

```text
localized completed Weil form,
self-adjoint operator,
minimal symmetric first-order operator,
deficiency indices (1,1),
self-adjoint extensions,
entire characteristic functions with only real zeros,
```

while the active exponent-lattice set `A(a)` is literally empty. These finite-stage spectral properties therefore cannot be evidence that the rational-prime lattice itself is forcing zero localization.

A July 2026 numerical realization by Kim--Hong--Kim--Choi--Jang--Kim independently makes the same boundary explicit: it names `2a<log 2` the **prime-free window**, finds an archimedean small-`a` spectral law there, and emphasizes that the small-window results are universal rather than zeta-specific. Its numerical and symbol-level claims are treated here only as corroboration; the exact support calculation and Suzuki's operator theorems are sufficient for the negative conclusion.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
finite localized Weil self-adjointness
+ real-zero finite characteristic functions
    -> prime-lattice arithmetic rigidity
    -> RH localization.
```

The finding does **not** rule out Suzuki's or Connes--Consani--Moscovici's limiting spectral programs. It identifies where the genuinely arithmetic content must enter: in the cross-scale evolution after the prime-power thresholds activate, in global Weil positivity, or in the still-unproved large-`a` convergence/localization theorem.

## Exact prime-power activation filtration

Suzuki writes the completed Weil functional in the form

```text
W(f)
 = archimedean/pole terms
   - sum_n Lambda(n)/sqrt(n) f(log n)
   - sum_n Lambda(n)/sqrt(n) f(-log n).
```

Let `v` lie in `C_c^infinity(-a,a)` and set

```text
f = v * v_tilde,
v_tilde(x)=conjugate(v(-x)).
```

Because `supp(v)` is a compact subset of `(-a,a)`, the elementary convolution support rule gives

```text
supp(f) subset (-2a,2a).
```

Therefore the term indexed by `n` can contribute only when

```text
|log n| < 2a.
```

Since `n>=1`, this is `n<exp(2a)`. Since `Lambda(n)` is nonzero exactly for `n=p^m`, the active non-archimedean support is

```text
{p^m : p^m < exp(2a)}.
```

Under the exponent map,

```text
v(p^m)=m e_p,
log(p^m)=<m e_p,(log q)_q>=m log p,
```

so the same set is

```text
A(a)={m e_p : m log p < 2a}.
```

This is the localized-Weil version of the axis-ray compression already recorded in `PL-013`, but with a useful dynamical refinement: as the aperture `a` grows, the arithmetic input becomes active immediately after the discrete energy thresholds `m log p/2`.

The first possible event is `n=2`. Thus

```text
0<a<=(log 2)/2
```

is prime-free for compactly supported test functions; the open-window formulation used in the numerical literature is the safer strict inequality `2a<log 2`. The localized form in this interval still contains the completed archimedean and pole terms; "prime-free" does not mean trivial or equal to a bare Fourier Laplacian.

## Suzuki's unconditional real-zero finite-stage family

Suzuki's arXiv:2606.09096v2 constructs the localized self-adjoint operator `A_a` from the Weil form and the continuous screw kernel. His Theorem 1.3 proves continuity of its lowest eigenvalue `lambda_a`; failure of RH is equivalent to `lambda_a<0` for some aperture, while `lambda_a>0` for sufficiently small `a`.

The stronger matched control for the present question is Theorem 1.5. Pick any

```text
lambda < lambda_a
```

and let `H(T_a)` be the completion under

```text
||v||_(T_a)^2 = Q_W^a(v) - lambda ||v||_2^2.
```

On this Hilbert space the minimal operator

```text
D_a=i d/dx,
Dom(D_a)=C_c^infinity(-a,a),
```

is symmetric with deficiency indices `(1,1)`. Its self-adjoint extensions `Dbar_(a,theta)` are parametrized by `theta`, and Suzuki constructs an entire function `W(a,theta;z)` such that

```text
zeros W(a,theta;.)
    = spectrum(Dbar_(a,theta))
    subset R.
```

This holds for every fixed aperture, without RH. Suzuki then explicitly separates this finite-stage reality from the hard limit: his Corollary 1.6 states that an appropriate compact-uniform normalized limit of the characteristic functions to a specific `xi`-derived quotient would imply RH. That convergence is conjectural, not a consequence of self-adjointness at finite `a`.

The paper itself highlights the arithmetic-insensitivity relevant here: the proof of Theorem 1.5 does not use detailed information on the prime terms, only their finiteness for fixed aperture. The exact prime-free support calculation above therefore supplies a particularly sharp matched control: for sufficiently small aperture there are no prime terms at all, yet the same real-zero spectral mechanism exists.

## Current numerical prior art confirms the separation

Kim, Hong, Kim, Choi, Jang, and Kim, arXiv:2607.24830v2, numerically instantiate Suzuki's localized Weil operator. Section 2.2 explicitly calls

```text
2a < log 2
```

the prime-free window and states that no prime term enters the quadratic form there. Their small-`a` computations produce an archimedean spectral law and their abstract describes those results as universal rather than new arithmetic.

The same preprint stresses a second distinction that is useful for auditing operator proposals: the eigenvalues of the Friedrichs operator `A_a` are not the nontrivial Riemann zeros. The zeta zeros enter through the explicit-formula error structure of the prime-dependent symbol, while Suzuki's different first-order self-adjoint extensions have real spectra given by their finite-aperture characteristic functions. Any claim that simply observes a real spectrum in one of these finite models must therefore specify **which operator**, **which characteristic function**, and **which limiting theorem** connects it to the actual Riemann divisor.

The numerical paper is a recent `math.GM` preprint and several of its detailed asymptotic/spectral conclusions are computational or symbol-level. None of those stronger claims is required for this finding. Its role is prior-art corroboration of the exact prime-free separation already forced by the support calculation and Suzuki's theorem.

## What the lattice contributes — and what it does not

The prime-exponent interpretation of the completed Weil family is now unusually concrete:

```text
aperture a
    |
    v
energy cutoff 2a
    |
    v
axis-ray lattice points m e_p with m log p < 2a
    |
    v
localized von-Mangoldt contribution.
```

This is a genuine arithmetic filtration, but it uses only the coordinate rays because the explicit formula is weighted by `Lambda`. Mixed-prime exponent vectors do not enter directly.

The finite-stage Hilbert-space architecture, however, does not wait for this filtration to become nonempty. Thus the implication

```text
self-adjoint finite model + real characteristic zeros
    => arithmetic localization mechanism
```

is falsified by the empty-`A(a)` regime.

A viable mechanism must instead use something that changes when the correct rational prime-power thresholds are switched on and whose global evolution cannot be reproduced by an archimedean or freely modified control. Plausible exact targets include:

```text
control of lambda_a for all a,
positivity/nondegeneracy of Q_W^a for all a,
large-a convergence of the finite characteristic functions,
large-a convergence of extremal vectors/determinants,
or an arithmetic trace identity for the spectral flow across
    a=(m log p)/2.
```

But the first two are already equivalent or very close to Weil/Yoshida RH criteria, and the convergence problems are precisely the unresolved steps in the recent spectral programs. The threshold filtration by itself therefore does not constitute progress on RH.

## Analytic-continuation boundary

No Euler product is used in the critical strip here.

The arithmetic terms are read from the **completed Weil explicit formula**, where the zeta function has already been analytically continued and the archimedean/pole contributions are part of the object. The support calculation only uses compact support of the test-function convolution and the exact von-Mangoldt support.

Likewise, Suzuki's screw function is obtained through the explicit-formula/entire-function framework. The conclusion is therefore about a genuine continued/completed object, not a formal substitution of the Euler product outside `Re(s)>1`.

## Prior-art and novelty audit

The main sources are recent but the structural ingredients are not Mathia discoveries.

- **Masatoshi Suzuki**, “Weil's quadratic form via the screw function,” arXiv:`2606.09096v2` [math.NT, math.FA], revised 17 August 2026. Theorem 1.1 identifies the localized self-adjoint Weil operator through the screw kernel; Theorems 1.3--1.5 establish continuity/small-aperture structure and the unconditional self-adjoint-extension characteristic functions with only real zeros; Corollary 1.6 isolates the conjectural large-aperture limit that would imply RH. Suzuki explicitly states that Theorem 1.5 uses no detailed arithmetic input beyond finiteness of the prime contribution at fixed aperture.
- **Taebong Kim, Youngsik Hong, Minsik Kim, Sunyoung Choi, Jaewon Jang, Minseo Kim**, “A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator: The Archimedean Spectral Law, its Universality, and an Operator Form of Weil's Positivity Criterion,” arXiv:`2607.24830v2` [math.GM], revised 29 July 2026. It explicitly isolates the prime-free window `2a<log 2` and numerically studies the resulting archimedean spectrum. Its numerical claims are not promoted to theorem status here.
- Weil, Bombieri, and Connes--Consani--Moscovici are already recorded in `PL-013` and `SOURCES.md` as the classical/recent lineage of the explicit-formula quadratic form and finite spectral models.

The exact set `A(a)={m e_p:m log p<2a}` is an immediate exponent-coordinate translation of the compact-support cutoff and is not claimed as a new theorem. The durable contribution is the **research-line no-go synthesis**: the newly strengthened finite-aperture self-adjoint/real-zero machinery survives in a regime where the prime lattice contributes no arithmetic term whatsoever, so those spectral properties cannot themselves be the missing prime-lattice rigidity.

## Falsification and escape tests

This finding would be falsified or materially narrowed by any of the following:

1. a compactly supported `v` in `(-a,a)` whose convolution `v*v_tilde` has support outside `(-2a,2a)`;
2. a nonzero von-Mangoldt term in `Q_W^a` when `2a<log 2`;
3. a failure of Suzuki's Theorem 1.5 to produce self-adjoint extensions with real-zero characteristic functions at such an aperture;
4. a theorem showing that some **additional** finite-aperture arithmetic identity, absent in the prime-free model, already forces the large-`a` zeta limit;
5. a proof of the conjectural compact-uniform spectral limit or of global Weil positivity by an independent arithmetic mechanism.

Items 1--3 are excluded by elementary support theory and Suzuki's stated theorem. Items 4--5 describe genuine escape routes rather than contradictions.

## Consequence for the research line

`PL-013` showed that the completed explicit-formula channel sees only the prime-power coordinate rays and that current self-adjoint finite-cutoff models still lack a convergence theorem to `Xi`. `PL-043` showed that ambient self-adjoint/de Branges spectral geometry is too flexible unless zeta-specific positivity is proved.

The present result makes those warnings sharper using the newest localized-Weil theory:

```text
small aperture, 2a<log 2
    -> no active prime-lattice point at all
    -> yet unconditional self-adjoint / real-zero finite model

larger aperture
    -> prime-power axis points activate after crossing a=(m log p)/2
    -> arithmetic information accumulates

all apertures / a->infinity
    -> global positivity or spectral convergence is the hard RH step.
```

Therefore the next useful work should not treat finite-stage spectral reality as evidence of arithmetic localization. It should attack the **cross-scale arithmetic rigidity** of the completed Weil family: what the exact sequence of rational-prime activation events forces, if anything, beyond the universal local operator theory, and whether that can control the global positivity or limiting determinant without simply restating an existing RH-equivalent criterion.