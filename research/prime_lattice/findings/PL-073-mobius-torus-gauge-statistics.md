# PL-073 — Möbius hypercube orientation is a prime-torus gauge for unpointed statistics

## Claim

The coefficient-dependent escape left open by `PL-072` splits sharply into **support information** and **orientation information**. For the canonical Möbius orientation on the square-free exponent hypercube, the orientation part is invisible to every unpointed statistic that is invariant under prime-torus translation.

Fix a finite square-free support

```text
S_N={n<=N: mu(n)!=0}
```

and coefficients `a_n`. Under the Bohr transform write

```text
P(z)=sum_(n in S_N) a_n z^(v(n)),

P_mu(z)=sum_(n in S_N) mu(n) a_n z^(v(n)).
```

Let

```text
epsilon=(-1,-1,-1,... ) in T^infinity.
```

Because every `n in S_N` is square-free,

```text
mu(n)=(-1)^Omega(n)=product_(p|n)(-1)=epsilon^(v(n)),
```

and therefore the Möbius-oriented polynomial is exactly a translate of the unoriented one:

```text
P_mu(z)=P(epsilon z).
```

Haar measure on the prime torus is translation invariant. Hence `P_mu` and `P` have **exactly the same Haar value distribution**. In particular, for every bounded Borel function `Phi:C->C`,

```text
integral Phi(P_mu(z)) dm(z)
 = integral Phi(P(z)) dm(z).
```

Thus all unpointed Haar moments, `L^p` norms, level-set distributions, and other statistics depending only on the law of the Bohr polynomial are unchanged by the Möbius signs.

The same invisibility is exact at finite observation time for the spectral data of the character Gram matrix. If

```text
f_n(t)=T^(-1/2)n^(-it),

g_n(t)=mu(n) f_n(t),
```

for `n in S_N`, and `G_(T,N)^sf`, `G_(T,N)^mu` are the corresponding Gram matrices, then with

```text
U_mu=diag(mu(n))_(n in S_N)
```

one has

```text
G_(T,N)^mu = U_mu^* G_(T,N)^sf U_mu.
```

Therefore their eigenvalues, singular values, determinant, condition number, Schatten norms, and every other unitary-conjugacy invariant agree **for every finite `T` and `N`**, including moving cutoffs `N=N(T)`.

For a fixed cutoff, the same conclusion holds asymptotically for vertical-flow value distributions. Unique factorization makes the finitely many active frequencies `{log p}` rationally independent, so Kronecker--Weyl equidistribution turns the long vertical orbit into Haar measure on the active finite torus. Consequently `P_mu((p^(-it))_p)` and `P((p^(-it))_p)` have the same limiting value distribution as `T->infinity`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
Möbius +/- orientation on the square-free prime hypercube
+ unpointed Bohr/Haar statistics or character-Gram spectrum
    -> new arithmetic cancellation / RH rigidity.
```

The square-free **support** is not removed by this argument, and target-relative or pointed observables can still detect the orientation. The obstruction is specifically that the sign field itself is a prime-torus gauge transformation whenever the observable is allowed to move with that gauge.

## Exact torus-translation identity

The Bohr monomial associated with `n` is

```text
z^(v(n))=product_p z_p^(v_p(n)).
```

On the square-free sector every exponent is `0` or `1`. Translation by the torus element `epsilon_p=-1` therefore gives

```text
(epsilon z)^(v(n))
 = product_(p|n)(-z_p)
 = (-1)^Omega(n) z^(v(n))
 = mu(n) z^(v(n)).
```

Summing over the support gives the exact identity

```text
P_mu = P o tau_epsilon,

tau_epsilon(z)=epsilon z.
```

This is not special to finite-dimensional notation. It is the restriction to the square-free support of the completely multiplicative unimodular character

```text
lambda(n)=(-1)^Omega(n),
```

whose prime values are all `-1`. More generally, for any completely multiplicative unimodular character `chi`, if

```text
eta=(chi(p))_p in T^infinity,
```

then

```text
sum_n chi(n)a_n z^(v(n))
 = P(eta z)
```

whenever the polynomial or function is defined in the relevant Bohr space.

Thus Möbius orientation on the square-free hypercube is not an additional invariant of the ambient prime torus. It is one particular character translation of it.

## Haar statistics cannot see the orientation

Let `m` be Haar probability measure on the active finite prime torus, or the corresponding product Haar measure on `T^infinity`. Translation invariance gives

```text
(tau_epsilon)_* m = m.
```

For any bounded Borel observable `Phi` on the value space,

```text
integral Phi(P_mu(z)) dm(z)
 = integral Phi(P(epsilon z)) dm(z)
 = integral Phi(P(z)) dm(z).
```

This is stronger than equality of `H^2` norms. It identifies the complete push-forward probability measures

```text
(P_mu)_*m = P_*m.
```

Consequently no statistic extracted solely from that law can distinguish the two coefficient orientations. Examples include

```text
||P_mu||_(L^q(m)) = ||P||_(L^q(m))
```

for every finite `q>0`, the distribution of `|P|`, all moments for which the displayed integrals are meaningful, quantiles, and tail probabilities.

An equivalent moment-level explanation is that Haar integration retains only multiplicative resonances. Whenever a mixed moment contains a surviving relation

```text
product_i n_i = product_j m_j,
```

additivity of `Omega` gives

```text
sum_i Omega(n_i)=sum_j Omega(m_j),
```

so the total Möbius/Liouville phase is `1`. The torus-translation proof is stronger because it gives the entire distribution at once.

## Finite-time Gram spectrum is exactly gauge invariant

The finite-time character Gram entry is

```text
G_(T,N)^sf(m,n)
 = (1/T) integral_0^T exp(i(log m-log n)t) dt.
```

After multiplying each character by its Möbius sign,

```text
G_(T,N)^mu(m,n)
 = conjugate(mu(m)) mu(n) G_(T,N)^sf(m,n).
```

Since `mu(n)` is `+/-1` on `S_N`, this is exactly

```text
G_(T,N)^mu=U_mu^*G_(T,N)^sfU_mu.
```

This has two consequences relevant to `PL-072`.

First, the `N~T` Dirichlet-polynomial resolution transition found there is not altered spectrally by inserting Möbius signs on the same square-free support. Any claim based on Gram eigenvalues, singular values, frame/Riesz bounds, determinant, condition number, or another unitary invariant sees exactly the same matrix up to diagonal gauge.

Second, this statement is **not asymptotic**. It remains true for arbitrary moving cutoffs, arbitrary observation horizons, and arbitrary subsets of square-free integers. Therefore allowing `N=N(T)` does not rescue an unpointed Gram-spectral Möbius mechanism.

If one instead keeps every integer `n<=N` and uses the literal coefficient `mu(n)`, nonsquare-free indices become zero vectors. That changes the support and adds null directions. The resulting information is `mu(n)^2`, i.e. square-free support; it is not information carried by the alternating hypercube orientation.

## Fixed-cutoff vertical statistics inherit the same gauge blindness

Let `P_N` be the finite set of primes dividing some member of `S_N`. The vertical Bohr orbit is

```text
z(t)=(exp(-it log p))_(p in P_N).
```

If

```text
sum_(p in P_N) k_p log p=0,

k_p in Z,
```

then unique factorization gives `k_p=0` for every prime. Hence the finite frequency vector is rationally independent. Kronecker--Weyl equidistribution implies that the orbit is Haar-equidistributed on `T^(P_N)`.

For every continuous bounded `Phi`, therefore,

```text
lim_(T->infinity) (1/T) integral_0^T
  Phi(P_mu(z(t))) dt

 = integral Phi(P_mu(z)) dm(z)
 = integral Phi(P(z)) dm(z)

 = lim_(T->infinity) (1/T) integral_0^T
  Phi(P(z(t))) dt.
```

So at every fixed arithmetic cutoff, long-time vertical value-distribution statistics also forget the Möbius orientation.

No uniform statement is claimed when the cutoff grows with the observation horizon. In that regime equidistribution rates and the number of active prime coordinates can interact. The exact Gram-conjugacy statement above, however, still rules out every moving-cutoff mechanism whose only output is an unpointed Gram spectral invariant.

## Relation to the Helson-twist falsification control

`PL-003` shows that the ambient prime torus and its `{log p}` frequencies support Helson twists with radically different zero sets and continuation domains. The present calculation is the coefficient-level version of the same information obstruction.

A completely multiplicative unimodular twist is precisely a torus translation on Bohr coefficients. Therefore any proposed statistic that is invariant under torus translation cannot distinguish the Riemann point from those twists. On square-free support, the Möbius sign pattern is exactly such a translation.

This passes the strongest line-specific falsification control in the negative direction: the mechanism survives arbitrary prime-phase changes because the phase change is its gauge symmetry. It therefore cannot be the missing datum that selects the untwisted Riemann object.

## Why this does not erase genuine Möbius cancellation

The conclusion concerns **unpointed** or translation-invariant observables. Möbius cancellation in number theory is normally measured relative to a distinguished section, target, or ordering, and that extra structure breaks the gauge symmetry.

For example, although

```text
G_mu=U_mu^* G_sf U_mu,
```

a pointed quadratic form with the fixed all-ones vector satisfies

```text
<1,G_mu 1>
 = <U_mu 1,G_sf U_mu 1>
 = <mu,G_sf mu>.
```

The matrix spectrum is unchanged, but the distinguished vector has moved. A statistic that insists on keeping the target `1` fixed can therefore detect the Möbius orientation.

This is exactly why the result does not contradict `PL-008`: the Nyman/Bagchi mechanism is target-relative. Its question is whether a distinguished function lies in the closed span of a Möbius-related family after Mellin/Hardy continuation, not whether two unpointed coefficient systems have different torus-Haar laws.

Likewise the summatory Möbius function

```text
M(x)=sum_(n<=x) mu(n)
```

is evaluation against a canonical positive cutoff/order, not a Haar-translation-invariant statistic on the prime torus. The gauge calculation does not make that cancellation trivial.

## Prior-art and novelty audit

The general character-space machinery is classical. `research/prime_lattice/SOURCES.md` source 1, Hedenmalm--Lindqvist--Seip, identifies square-summable Dirichlet series with the Hardy space of the infinite polydisk/character space and multiplicative character twists with the corresponding prime-coordinate boundary functions/vertical limits. Haar translation invariance, Kronecker--Weyl equidistribution for a finite rationally independent frequency set, and unitary diagonal conjugacy of Gram matrices are standard facts.

A targeted literature audit around Möbius twists, Bohr transforms, infinite-torus characters, and Dirichlet-polynomial statistics recovered this general character-twist framework rather than a zeta-specific theorem in which the Möbius signs become an unpointed spectral invariant. No novelty is claimed for the torus translation, Haar invariance, or Gram conjugacy.

The durable line-specific content is the **information audit** forced by the current research state: `PL-072` left coefficient-dependent arithmetic as an escape from the universal unweighted positive-cone Gram geometry, but the most canonical coefficient phase — Möbius orientation on the Boolean prime hypercube — still disappears from every unpointed torus statistic and every Gram spectral invariant. Only its square-free support, or a pointed structure that refuses to transform with the gauge, can remain informative.

## Analytic-continuation and falsification audit

No Euler product is moved outside its domain of convergence and no analytic continuation is used. The identities are finite Bohr-polynomial, finite Gram-matrix, and compact-torus statements.

The scope is deliberately sharp:

1. **Square-free support is retained.** The theorem gauges away `mu(n)=+/-1` only where `mu(n)!=0`; it does not make the support indicator `mu(n)^2` disappear.
2. **Pointed observables are not covered.** A fixed target vector, fixed basepoint, evaluation functional, Nyman target, or another canonical section can break the gauge symmetry.
3. **Non-Haar statistics are not covered.** An observable tied to the identity point or another distinguished arithmetic measure need not be translation invariant.
4. **Growing-cutoff orbit distributions are not classified.** Fixed-cutoff Kronecker--Weyl gives equality of limiting laws; simultaneous `N,T->infinity` can have nonuniform pre-equidistribution effects. Unpointed Gram spectra remain exactly gauge-invariant in that regime.
5. **Analytic continuation is outside the claim.** A construction in which continuation singles out the untwisted point may escape the obstruction, but it must identify that extra structure explicitly.
6. **Magnitude or support weights can matter.** Von Mangoldt weights, square-free support, target-relative amplitudes, or other coefficients not obtainable solely by multiplying a fixed support by a unimodular character are not gauged away by this theorem.

The decisive falsification test is immediate. If a proposed mechanism changes only the signs `a_n -> mu(n)a_n` on a fixed square-free support and then reads an unpointed Haar law or unitary-conjugacy invariant of the character Gram matrix, its claimed Möbius sensitivity is false: the two objects are exactly related by prime-torus/diagonal gauge.

## Relation to the current line frontier

The finite-horizon branch now has a more precise boundary:

```text
bare positive characters
    -> classical N~T resolution geometry (`PL-072`);

Möbius +/- orientation on fixed square-free support
    -> exact diagonal/tori gauge for unpointed statistics (`PL-073`);

square-free support, non-unimodular arithmetic weights,
or a distinguished target/basepoint
    -> not removed by this gauge argument.
```

Thus the phrase “add Möbius weights” is too broad to define a surviving mechanism. If the only new ingredient is the alternating sign orientation of the Boolean prime hypercube and the output is an unpointed spectral/distributional statistic, the route is closed. A useful next construction must retain information that the gauge cannot move away — for example support geometry, a canonical target-relative pairing, a completion-sensitive functional, or a genuinely arithmetic non-unimodular weight — and must still pass the Helson/Beurling controls from the line mandate.
