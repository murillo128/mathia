# PL-009 — Hilbert–Schmidt regularization of the prime Euler determinant is zero-free and removes the only critical-strip-sensitive term

## Claim

There is a canonical one-particle operator directly associated with the prime-coordinate decomposition whose standard Hilbert–Schmidt Fredholm regularization exists exactly in the half-plane `Re(s)>1/2`, but this regularized determinant is **zero-free there** and therefore cannot encode the Riemann zero divisor.

Let

```text
h = ell^2(P),
H_p e_p = (log p) e_p,
T_s = exp(-s H_p),
T_s e_p = p^(-s) e_p.
```

For `s=sigma+i t`,

```text
T_s in S_m  <=>  m sigma > 1
```

for every integer `m>=1`. In particular, `T_s` is Hilbert–Schmidt exactly when `sigma>1/2`.

On that half-plane the standard second regularized Fredholm determinant is

```text
D_2(s) = det_2(I-T_s)
       = product_p [(1-p^(-s)) exp(p^(-s))]
       = exp(-sum_{k>=2} P(k s)/k),
```

where

```text
P(s)=sum_p p^(-s)
```

is the prime zeta function in its original domain. The final series converges locally uniformly for `Re(s)>1/2`, because every `k s` with `k>=2` lies in `Re(k s)>1`.

Consequently `D_2` is holomorphic and zero-free throughout `Re(s)>1/2`.

For `Re(s)>1`, where the Euler product is absolutely convergent,

```text
log zeta(s) = P(s) + sum_{k>=2} P(k s)/k,
```

so

```text
D_2(s) = zeta(s)^(-1) exp(P(s)).
```

Thus the `det_2` regularization removes exactly the `k=1` prime-zeta contribution from the Euler logarithm. In `Re(s)>1/2`, all terms with `k>=2` are already holomorphic because `Re(k s)>1`; the only term capable of inheriting logarithmic singularities from zeros or the pole of `zeta(s)` is the removed first-order term `P(s)`. Classical analytic continuation of the prime zeta function makes this explicit: locally, its singularities track those of `log zeta(s)` while the `k>=2` remainder is holomorphic.

Therefore the most direct Hilbert–Schmidt regularized determinant of the prime modes does not expose zeta zeros; it **cancels the part that can carry them**. Reconstructing `zeta` from this determinant requires putting the prime-zeta counterterm back, and continuing that counterterm across the critical strip already requires the same zeta zero/pole data one hoped the determinant would explain.

**Evidence/status:** `EXACT-DERIVED + DECISIVE-NEGATIVE`.

The determinant and prime-zeta ingredients are classical. No novelty is claimed for `det_2`, for the Euler-logarithm expansion, or for prime-zeta continuation. The durable Mathia result is the audited obstruction: the canonical standard regularization available precisely at the `1/2` Schatten threshold deletes rather than reveals the RH-sensitive first-order prime contribution.

## Exact derivation

### 1. Schatten threshold of the one-particle prime operator

The singular values of `T_s` are

```text
s_p(T_s)=p^(-sigma).
```

Hence for integer `m>=1`,

```text
||T_s||_(S_m)^m = sum_p p^(-m sigma).
```

The prime sum converges exactly when `m sigma>1`. Therefore

```text
T_s in S_2 <=> sigma>1/2.
```

This is the one-particle counterpart of the `1/2` Hilbert–Schmidt boundary found for the full integer translation semigroup in `PL-007`.

### 2. The second regularized determinant

For a Hilbert–Schmidt operator `T`, the standard regularized determinant is

```text
det_2(I-T)=det((I-T) exp(T))
          = product_j (1-lambda_j) exp(lambda_j).
```

Applying this to the diagonal eigenvalues `lambda_p=p^(-s)` gives

```text
D_2(s)=product_p (1-p^(-s)) exp(p^(-s)).
```

Since

```text
log((1-z) exp(z)) = -sum_{k>=2} z^k/k
```

for `|z|<1`,

```text
log D_2(s)
  = -sum_p sum_{k>=2} p^(-k s)/k
  = -sum_{k>=2} P(k s)/k.
```

For any compact subset of `Re(s)>1/2`, all arguments `k s`, `k>=2`, lie uniformly inside `Re(w)>1`; the series is therefore absolutely and locally uniformly convergent. This proves that `D_2` is holomorphic there.

It is also zero-free. Directly, `|p^(-s)|<1` for every prime when `sigma>0`, so `1` is not an eigenvalue of `T_s`, and the convergent regularized product has no zero. Equivalently,

```text
D_2(s)=exp(-sum_{k>=2}P(k s)/k)
```

is the exponential of a holomorphic function.

### 3. Comparison with the Euler product

For `sigma>1`,

```text
zeta(s)^(-1)=product_p (1-p^(-s))
```

and therefore

```text
D_2(s)=zeta(s)^(-1) exp(P(s)).
```

The same fact is visible logarithmically:

```text
log zeta(s)
 = sum_{k>=1} P(k s)/k
 = P(s) + sum_{k>=2}P(k s)/k.
```

The regularization subtracts the linear trace term `P(s)` and keeps precisely the `k>=2` tail with the opposite sign.

### 4. Why the removed term is exactly the dangerous one

On the entire open half-plane `sigma>1/2`, every term

```text
P(k s),  k>=2,
```

is evaluated in its absolutely convergent domain `Re(k s)>1`. Hence

```text
G_2(s)=sum_{k>=2}P(k s)/k
```

is holomorphic throughout that half-plane.

Classical Möbius inversion for the prime zeta function gives, initially for `Re(s)>1`,

```text
P(s)=sum_{n>=1} mu(n)/n * log zeta(n s).
```

For `n>=2` the terms `log zeta(n s)` are holomorphic throughout `Re(s)>1/2`, because `Re(n s)>1`. Thus, under the classical prime-zeta continuation, any logarithmic singularity in this half-plane is concentrated in the `n=1` term `log zeta(s)`; the remainder is holomorphic.

This matches the determinant identity exactly: `det_2` removes the first-order prime trace `P(s)`, and the surviving determinant is the exponential of the holomorphic higher-prime-power tail.

## Higher regularizations

The same obstruction is not special to order two. For integer `m>=2`, the standard `m`-regularized determinant exists for

```text
Re(s)>1/m
```

and satisfies

```text
D_m(s)=det_m(I-T_s)
      = exp(-sum_{k>=m} P(k s)/k).
```

It is holomorphic and zero-free in that domain. In `Re(s)>1`,

```text
zeta(s)^(-1)
 = D_m(s) * exp(-sum_{k=1}^{m-1}P(k s)/k).
```

Increasing the regularization order therefore moves more low-order prime-zeta terms into explicit counterterms; it does not create a determinant whose zeros are the zeta zeros. Order two is the RH-relevant case because its Schatten existence threshold is exactly `1/2` and all retained terms `k>=2` lie safely in the Euler-product half-plane.

## Relevance to the prime-exponent lattice

The full exponent lattice is the bosonic occupation space generated by the prime modes. The energy functional

```text
log n = sum_p v_p(n) log p
```

is the second-quantized form of the one-particle Hamiltonian

```text
H_p e_p=(log p)e_p.
```

`PL-007` studied the corresponding full integer semigroup and showed that its ordinary trace equals `zeta(s)` only for `Re(s)>1`. The present finding audits the most immediate proposed escape: pass to the one-particle prime operator, which becomes Hilbert–Schmidt at `1/2`, and use `det_2` to regularize the divergent Euler determinant.

That escape is mathematically well-defined but sterile for zero detection. Standard Hilbert–Schmidt renormalization removes the only prime-log term whose analytic continuation can see the zeta divisor in `Re(s)>1/2`.

## Prior art and novelty assessment

- Regularized Fredholm determinants `det_m` for Schatten-class operators and the formula for `det_2` are standard operator theory. Britz–Carey–Gesztesy–Nichols–Sukochev–Zanin give a modern primary reference for the regularized determinant framework and product formulae.
- Fröberg's classical study of the prime zeta function records the Möbius-inversion continuation and its logarithmic singularities inherited from zeros and the pole of `zeta`.
- Hartmann–Lesch provide modern general context relating Schatten regularized Fredholm determinants and zeta-regularized determinants.
- Recent informal/unreviewed RH manuscripts also use prime-mode `det_2` expressions. They are not used here as mathematical evidence and do not alter the classification: the component construction is not claimed to be novel.

The Mathia-specific value is the negative synthesis: once the standard `det_2` correction is written in prime coordinates, it becomes exact that the regularization discards the `k=1` term while retaining only a holomorphic, zero-free `k>=2` tail in the whole right critical half-plane.

## Boundary conditions and failure modes

- The result concerns the **diagonal one-particle prime operator** `T_s=diag(p^(-s))` and the standard Schatten regularized determinants built from it. It does not rule out non-diagonal operators, relative determinants with independently justified comparison data, scattering determinants, adelic constructions, or an operator incorporating the archimedean factor and functional equation.
- `det_2(I-T_s)` is defined by this argument only for `Re(s)>1/2`; the critical line itself is the Hilbert–Schmidt boundary, not part of the domain.
- A hypothetical zero of `zeta` with `Re(rho)>1/2` does not create a zero of `D_2`; it creates a logarithmic singularity in the analytically continued prime-zeta counterterm. Under RH, the actual critical zeros lie on the boundary where the standard `det_2` setup ceases to exist.
- Declaring analytically continued `P(s)` to be an independently supplied renormalization does not solve the problem: its continuation has logarithmic singularities determined by the zeta zero/pole divisor.
- The finding does not say that every regularized spectral construction is circular. It says that **this canonical diagonal regularization is** insufficient unless genuinely additional structure determines the counterterm without importing the zeta divisor.

## Audit / falsification criterion

The obstruction can be audited without numerical computation:

1. verify `T_s in S_2` iff `sum_p p^(-2 sigma)<infinity`, hence iff `sigma>1/2`;
2. apply the standard eigenvalue product for `det_2`;
3. expand `log((1-z)e^z)` and interchange the absolutely convergent sums to obtain `-sum_{k>=2}P(k s)/k`;
4. note that `Re(k s)>1` for every `k>=2` when `Re(s)>1/2`, proving holomorphy and zero-freeness;
5. in `Re(s)>1`, compare with the Euler logarithm and verify that the missing term is exactly `P(s)`.

A genuine escape from this negative result must change at least one substantive ingredient: use an operator whose nontrivial spectrum is not just `{p^(-s)}`, introduce a canonically determined relative/scattering term, or otherwise produce zero-sensitive data independently of analytic continuation of `P(s)` or `zeta(s)`.

## Consequence for the research line

`PL-007` left regularized determinants as a possible way to continue the canonical prime spectral picture past the trace-class boundary. The most direct version can now be closed:

```text
prime one-particle operator
    -> Hilbert-Schmidt exactly for Re(s)>1/2
    -> standard det_2 exists
    -> standard det_2 deletes P(s)
    -> retained k>=2 prime-power tail is holomorphic and zero-free
    -> zeta-zero information survives only in the removed counterterm.
```

So the coincidence of the Hilbert–Schmidt threshold with `Re(s)=1/2` remains a genuine geometric/operator boundary, but **standard diagonal Fredholm regularization does not turn that boundary into an RH zero mechanism**.