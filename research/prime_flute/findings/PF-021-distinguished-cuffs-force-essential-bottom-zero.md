# PF-021 — distinguished cuffs already force essential spectral bottom zero

**Status:** NEGATIVE/OBSTRUCTION + LITERATURE+DERIVED.

This note records a coarse spectral consequence of the distinguished prime-flute cuffs themselves. The spectral mechanism is standard Cheeger/Buser/Persson theory; the custom content is the application to the exact prime-flute cuff sequence. No claim is made that the general spectral theorem is new.

## Claim

For the complete zero-twist prime-flute `X_prime`, the distinguished cuff lengths grow sublinearly in the pants index; in fact

```text
ell_n = O(log n).
```

Consequently the tail admits compact escaping pants-block domains whose boundary/area ratio tends to zero. Hence the asymptotic Cheeger constant vanishes,

```text
h_ess(X_prime) = 0,
```

and the standard Buser/Persson argument gives

```text
inf sigma_ess(Delta_X_prime) = 0.
```

Because the Laplacian is nonnegative, `0` belongs to the essential spectrum.

The important research consequence is negative: the mere presence of arbitrarily low essential spectral energy, or the absence of a positive spectral gap at zero, cannot encode fine prime-gap fluctuations. It is already forced by the coarse pants-chain geometry plus the very weak growth bound on the distinguished cuffs.

## 1. Cuff growth from the exact prime coordinate

Recall

```text
u_n = cot(pi/p_n)
h_n = log(u_n/u_{n-1})
exp(-ell_n/2) = tanh(h_n/4).
```

The function `f(x)=cot(pi/x)` satisfies

```text
f'(x) = (pi/x^2) csc(pi/x)^2 >= 1/pi,
```

because `sin y <= y`. Therefore, with `g_{n-1}=p_n-p_{n-1}>=2`,

```text
u_n-u_{n-1} >= g_{n-1}/pi >= 2/pi.
```

Also `cot y < 1/y` for `0<y<pi/2`, so

```text
u_{n-1} < p_{n-1}/pi.
```

Hence

```text
h_n
 = log(1 + (u_n-u_{n-1})/u_{n-1})
 >= log(1 + g_{n-1}/p_{n-1})
 >= log(1 + 2/p_{n-1}).
```

Since `tanh x` is increasing and is comparable to `x` near zero,

```text
ell_n = -2 log tanh(h_n/4) <= 2 log(C p_n)
```

for an absolute constant `C` and all sufficiently large `n`.

Using the standard prime-number estimate `p_n ~ n log n`,

```text
ell_n = O(log n).
```

This upper bound uses no exceptional prime-gap theorem. In the usual asymptotic notation from the construction,

```text
ell_n ~ 2 log(4 p_n/g_{n-1}),
```

it is already implied by the trivial lower bound `g_{n-1}>=2` together with ordinary prime growth.

## 2. Escaping pants blocks are Folner domains

Far out in a tight flute, each pair of pants has one cusp and two geodesic cuffs. By Gauss-Bonnet its area is exactly `2 pi`.

Take the consecutive block

```text
P_n union P_{n+1} union ... union P_{2n-1}.
```

Before cusp truncation it has area

```text
2 pi n
```

and its only geodesic boundary components are the two end cuffs, of total length

```text
ell_n + ell_{2n} = O(log n).
```

To obtain a compact domain, truncate the `n` cusp ends high enough that the sum of all new horocycle lengths is at most `epsilon_n`, with (for example) `epsilon_n=1`. In a standard hyperbolic cusp, the removed cusp-tail area equals the horocycle boundary length, so the resulting compact domain `D_n` satisfies

```text
area(D_n) >= 2 pi n - 1,
length(boundary D_n) <= ell_n + ell_{2n} + 1.
```

Therefore

```text
length(boundary D_n)/area(D_n)
    = O(log n/n)
    -> 0.
```

The blocks start at index `n`, so they escape every fixed compact subset of the flute. Thus every sufficiently far tail has Cheeger constant zero and

```text
h_ess(X_prime)=0.
```

## 3. Spectral consequence

For complete manifolds with Ricci curvature bounded below, Buser-type converse inequalities turn arbitrarily small isoperimetric ratios into compactly supported functions with arbitrarily small Rayleigh quotients. Applying the construction to the escaping domains above gives a sequence of compactly supported test functions escaping to infinity with Rayleigh quotient tending to zero.

Persson/decomposition characterization of the bottom of essential spectrum then yields

```text
lambda_ess(X_prime)
 := inf sigma_ess(Delta_X_prime)
 = 0.
```

There is also an independent consistency check. The zero-twist prime-flute was already identified in PF-012 as parabolic/first-kind under the known tight-flute criterion. A complete parabolic manifold has `lambda_0=0`; the prime-flute has infinite area, so the constant function is not in `L^2` and zero is not an `L^2` eigenvalue. Therefore zero cannot lie below a positive essential threshold as an isolated discrete eigenvalue; it must belong to the essential spectrum.

## 4. What this rules out

The following are not prime-specific spectral signatures:

```text
inf sigma(Delta) = 0,
inf sigma_ess(Delta) = 0,
0 in sigma_ess(Delta),
absence of a positive low-energy spectral gap.
```

In particular, PF-008's isolated-prime-cluster mechanism is unnecessary for establishing the bottom of the essential spectrum. Isolated clusters may still matter for **finer** information — particular spectral points in `(0,1/4)`, multiplicities, right-limit channels, or scattering/resonance structure — but not for the onset of essential spectrum at zero.

This separates two effects cleanly:

```text
coarse distinguished-cuff growth
    -> amenable/Folner tail
    -> essential spectral bottom 0

multi-gap cross-ratio fluctuations
    -> exceptional short separating geodesics
    -> potentially finer low-energy structure
```

## 5. General tight-flute criterion suggested by the proof

Nothing prime-specific was used after the cuff estimate. For a complete tight flute with one-cusp pants in a chain, the same argument works whenever one can find escaping blocks whose two end-cuff lengths are `o(number of pants in the block)`.

A simple sufficient condition is

```text
ell_n = o(n).
```

Then the blocks `[n,2n)` have boundary/area ratio tending to zero and force `h_ess=0` and essential spectral bottom zero.

This generalization should be stated as a standard geometric consequence, not as a new prime theorem.

## 6. Novelty check

The underlying spectral mechanism is established literature:

- Cheeger constants and asymptotic Cheeger constants are standard tools for the bottom and essential bottom of the Laplacian;
- Buser/Ledoux converse inequalities on complete manifolds with Ricci curvature bounded below show that zero Cheeger constant corresponds to zero spectral bottom;
- existing work on infinite-type hyperbolic surfaces already constructs low-essential-spectrum examples by producing escaping low-Rayleigh test functions from weakly coupled pieces.

Targeted searches found work on tight-flute parabolicity and general infinite-type spectral theory, but no prior application of this exact prime-endpoint cuff formula to the essential spectral bottom. The useful content here is therefore a **project-specific negative result**, not a claim of a new general theorem.

## 7. Geometry preserved

This argument is entirely intrinsic to the interior hyperbolic prime-flute. It does not alter the exact orthogonal-circle construction or the ambient interior/exterior inversion duality from PF-017. The exterior copy plays no role in the Laplacian conclusion.

## 8. Audit boundary

Before theorem-level reuse, an independent review should check:

1. the exact pants/cuff indexing used in the block `[n,2n)`;
2. the completeness/parabolicity assumptions already recorded for the prime-flute;
3. the standard Buser/Persson passage from escaping small-isoperimetric domains to `lambda_ess=0`;
4. the elementary global inequalities used to turn the exact cuff identity into `ell_n=O(log n)`.
