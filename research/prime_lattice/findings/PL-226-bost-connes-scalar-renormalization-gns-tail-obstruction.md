# PL-226 — Scalar renormalization of Bost–Connes all-prime corners cannot produce a nonzero KMS-GNS tail

## Claim

The scalar-renormalization loophole left explicitly open by `PL-225` already fails at the level of the canonical KMS GNS cyclic vector. Let `phi_beta` be any `KMS_beta` state of the Bost–Connes system with `beta>0`, let `(pi_beta,H_beta,Omega_beta)` be its GNS triple, and let `F` range over finite sets of rational primes. Put

\[
L_F=\prod_{p\in F}p
\]

and consider any canonical cyclotomic corner

\[
C_F=\rho_{L_F}(e(R_F)),
\qquad R_F\in\mathbb Q/\mathbb Z,
\qquad
\rho_n(e(r))=\mu_ne(r)\mu_n^*.
\]

By `PL-224`, this includes every finite product of prime cyclotomic corners after transporting its phases to the common lcm corner. Then

\[
C_F^*C_F=P_{L_F}:=\mu_{L_F}\mu_{L_F}^*,
\qquad
\phi_\beta(P_{L_F})=L_F^{-\beta},
\]

so

\[
\boxed{\|\pi_\beta(C_F)\Omega_\beta\|=L_F^{-\beta/2}.}
\]

More strongly, **no choice of scalar counterterms can turn this tail into a nonzero GNS-norm limit**. For arbitrary scalars `a_F`, if

\[
\xi_F:=a_F\pi_\beta(C_F)\Omega_\beta
\]

converges in `H_beta` as `F` exhausts the primes, then its limit is necessarily zero.

For the natural power renormalizations `a_F=L_F^alpha`, this gives the exact trichotomy

\[
\begin{array}{lll}
\alpha<\beta/2 &\Longrightarrow& \|\xi_F\|\to0,\\
\alpha>\beta/2 &\Longrightarrow& \|\xi_F\|\to\infty,\\
\alpha=\beta/2 &\Longrightarrow& \|\xi_F\|=1\text{ but }(\xi_F)\text{ is not Cauchy.}
\end{array}
\]

At the norm-balancing scale `alpha=beta/2`, the normalized vectors are in fact weakly null. Thus the most direct attempt to rescue the strongly vanishing primorial/cyclotomic corner net of `PL-225` by scalar renormalization has no nonzero Hilbert-space tail in a Bost–Connes KMS representation.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE/CONTROL + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

The exponent `beta/2` below is only the Hilbert-space normalization forced by the `KMS_beta` norm. It has no connection to the Riemann critical line `Re(s)=1/2`. The argument is valid uniformly for every real `beta>0` for which the KMS state is considered and uses no analytic continuation of zeta.

## 1. KMS mass fixes the GNS norm of every cyclotomic corner

The Bost–Connes time evolution satisfies

\[
\sigma_t(\mu_n)=n^{it}\mu_n,
\qquad
\sigma_t(e(r))=e(r).
\]

Since `mu_n` is an isometry, the KMS identity gives

\[
\phi_\beta(\mu_n\mu_n^*)
=
\phi_\beta\!\left(\mu_n^*\sigma_{i\beta}(\mu_n)\right)
=n^{-\beta}.
\]

For `C_F=rho_(L_F)(e(R_F))`, unitarity of `e(R_F)` gives

\[
C_F^*C_F
=\mu_{L_F}e(-R_F)e(R_F)\mu_{L_F}^*
=P_{L_F}.
\]

Therefore

\[
\|\pi_\beta(C_F)\Omega_\beta\|^2
=\phi_\beta(C_F^*C_F)
=L_F^{-\beta}.
\]

This is independent of the phase `R_F`. The cyclotomic information can change matrix coefficients, but it cannot change the shrinking KMS mass of the support corner.

## 2. Nested prime tails become asymptotically orthogonal after norm balancing

Let `F subset G`. Since `L_F | L_G`, the exact lcm law from `PL-224`, applied to `C_F^* C_G`, gives

\[
C_F^*C_G
=
\rho_{L_G}\!\left(
 e\!\left(R_G-\frac{L_G}{L_F}R_F\right)
\right).
\]

The KMS relation for a corner and `|phi_beta(e(r))|<=1` therefore imply

\[
|\phi_\beta(C_F^*C_G)|\le L_G^{-\beta}.
\]

Define the norm-one vectors

\[
\eta_F:=L_F^{\beta/2}\pi_\beta(C_F)\Omega_\beta.
\]

Then

\[
\boxed{
|\langle\eta_F,\eta_G\rangle|
\le
\left(\frac{L_F}{L_G}\right)^{\beta/2}.
}
\]

In particular, if `G=F union {q}` for a prime `q notin F`,

\[
|\langle\eta_F,\eta_G\rangle|\le q^{-\beta/2}.
\]

New large prime directions therefore make the normalized tail vectors arbitrarily close to orthogonal rather than close to one another. This is the opposite of the coherence needed for a nonzero strong/GNS limit.

The same estimate proves the arbitrary-scalar statement. Write

\[
b_F:=\|a_F\pi_\beta(C_F)\Omega_\beta\|
=|a_F|L_F^{-\beta/2}.
\]

For nested `F subset G`,

\[
|\langle\xi_F,\xi_G\rangle|
\le b_Fb_G\left(\frac{L_F}{L_G}\right)^{\beta/2}.
\]

Suppose `(xi_F)` were Cauchy with a nonzero limiting norm `c>0`. Beyond a sufficiently large finite prime set all `b_F` would be bounded below, say by `3c/4`. Fix such an `F` and adjoin an arbitrarily large prime `q`, obtaining `G=F union {q}` still beyond the Cauchy threshold. Then

\[
\|\xi_F-\xi_G\|^2
\ge
b_F^2+b_G^2-2b_Fb_Gq^{-\beta/2},
\]

which stays bounded away from zero for sufficiently large `q`. This contradicts Cauchy convergence. Hence any convergent scalar-renormalized net has limiting norm zero and therefore converges only to the zero vector.

## 3. The norm-balanced tail is weakly null

The failure at `alpha=beta/2` is stronger than non-Cauchy behavior. Let

\[
\eta_F=L_F^{\beta/2}\pi_\beta(C_F)\Omega_\beta.
\]

The algebraic span of monomials

\[
X=\mu_m e(r)\mu_n^*
\]

is dense in the Bost–Connes algebra, so the vectors `pi_beta(X)Omega_beta` are dense in the GNS Hilbert space. If `m ne n`, the element `X^*C_F` has nonzero time frequency `log(n/m)`. Every KMS state is invariant under the time evolution, hence

\[
\phi_\beta(X^*C_F)=0.
\]

If `m=n`, then `X=rho_m(e(r))` and `PL-224` gives

\[
|\phi_\beta(X^*C_F)|
\le \operatorname{lcm}(m,L_F)^{-\beta}
\le L_F^{-\beta}.
\]

Consequently, in both cases,

\[
|\langle\pi_\beta(X)\Omega_\beta,\eta_F\rangle|
\le L_F^{-\beta/2}
\longrightarrow0
\]

(up to the identically zero first case). Since `||eta_F||=1` and the monomial vectors are dense,

\[
\boxed{\eta_F\rightharpoonup0.}
\]

Thus the only scalar scale that keeps the tail bounded in GNS norm produces a unit-norm net that escapes weakly to zero along ever-new prime coordinates.

## 4. Gibbs-mass and Hilbert-space renormalizations are incompatible

The phase-free support projection already exhibits the obstruction. For

\[
P_F=P_{L_F},
\]

one has

\[
\phi_\beta(P_F)=L_F^{-\beta}.
\]

Renormalizing the expectation to unit mass requires `L_F^beta P_F`:

\[
\phi_\beta(L_F^\beta P_F)=1.
\]

But its GNS norm is

\[
\|\pi_\beta(L_F^\beta P_F)\Omega_\beta\|
=L_F^{\beta/2}\to\infty.
\]

Conversely, the Hilbert-bounded normalization `L_F^(beta/2) P_F` has norm one but expectation

\[
\phi_\beta(L_F^{\beta/2}P_F)=L_F^{-\beta/2}\to0,
\]

and its GNS vector is weakly null by the previous argument. The canonical KMS mass therefore does not supply a scalar normalization that is simultaneously nonvanishing and Hilbert-compact/coherent.

## 5. Matched generic control and novelty audit

Nothing in the argument uses the arithmetic identity of the rational primes beyond choosing a countable family of independent semigroup directions and their positive energies. In a generic product Toeplitz/Nica system with isometries `S_j`, commuting range projections `Q_j=S_jS_j^*`, energies `E_j>0`, and a product KMS state satisfying

\[
\phi_\beta\!\left(\prod_{j\in F}Q_j\right)
=
\exp\!\left(-\beta\sum_{j\in F}E_j\right),
\]

assume `sum_j E_j=infinity`. For nested finite sets `F subset G`, the normalized projection vectors have overlap

\[
\exp\!\left(
-\frac\beta2\sum_{j\in G\setminus F}E_j
\right),
\]

and the same no-nonzero-scalar-limit/weak-escape mechanism follows. Taking `E_p=log p` recovers the Bost–Connes prime-shift scale. This is therefore a **matched non-arithmetic control**, not a rational-prime fingerprint.

The underlying Bost–Connes semigroup dynamics and KMS identities are classical. General Nica–Toeplitz KMS theory also treats exactly this kind of quasi-lattice/product projection structure; a relevant reference is Z. Afsar, N. S. Larsen and S. Neshveyev, *KMS states on Nica-Toeplitz C*-algebras*, Communications in Mathematical Physics **378** (2020), 1875–1929, DOI `10.1007/s00220-020-03711-6`. The original arithmetic source remains J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) **1** (1995), 411–457.

A targeted audit around Bost–Connes KMS states, Nica–Toeplitz KMS systems, product range projections, normalized shrinking cylinders, and Hilbert-space normalized tails found no basis for claiming the exact lemma above as a new theorem. The durable delta is narrower: it closes a live `prime_lattice` branch left explicitly open by `PL-225` by deriving the obstruction in the exact cyclotomic-corner hierarchy of `PL-224`.

## 6. What this closes and what remains open

This finding closes the immediate proposal “multiply the vanishing all-prime cyclotomic/primorial corner by a scalar counterterm until it has a nonzero KMS-GNS limit.” The failure is not merely that the obvious power is wrong: **every scalar choice fails to yield a nonzero norm limit on the canonical KMS cyclic vector**, and the unique power that balances the vector norm is weakly null. Because the same behavior survives a generic Toeplitz/Nica control, it supplies no RH-sensitive arithmetic invariant.

The result does **not** classify non-scalar renormalizations, logarithmic/additive counterterms, cumulants, relative determinants, spectral-shift constructions, weights rather than states, modular/target-sensitive relations, adelic or Weil couplings, distributional limits, ultraproduct limits, or analytic continuation in a complex temperature parameter. Nor does convergence to zero on the cyclic vector by itself rule out every conceivable nonzero operator limit in a representation where the cyclic vector is not separating. Those possibilities require additional source-forced structure and remain outside this claim.

In particular, the occurrence of `beta/2` is not a hidden version of `Re(s)=1/2`: it is the square-root exponent converting KMS mass into Hilbert norm. Since the entire theorem persists for arbitrary `beta>0` and for matched non-arithmetic energies, it cannot by itself distinguish the Riemann critical line.

## Falsification / audit tests

The result would require correction or narrowing if any of the following exact steps failed: the KMS identity `phi_beta(mu_n mu_n^*)=n^(-beta)`; the corner support identity `C_F^*C_F=P_(L_F)`; the `PL-224` lcm product law for `C_F^*C_G`; the estimate `|phi_beta(e(r))|<=1`; invariance of KMS states under the Bost–Connes time evolution; or density of algebraic monomial vectors in the GNS cyclic subspace. None of these uses RH or analytic continuation.

## Consequence for `prime_lattice`

`PL-225` left scalar renormalization as the first possible way to rescue the canonical all-prime corner net after its strong collapse to zero. That escape is now closed in the natural KMS-GNS topology. The surviving infinite-prime program must therefore introduce a **non-scalar or relative global operation** that is forced by the arithmetic source and fails the generic Toeplitz/Nica control. Merely compensating for the shrinking product of prime-corner masses cannot create the missing global RH rigidity.