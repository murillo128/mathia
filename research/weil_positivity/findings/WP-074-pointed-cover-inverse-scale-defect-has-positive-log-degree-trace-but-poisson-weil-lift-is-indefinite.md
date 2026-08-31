# WP-074 — Pointed-cover inverse-scale defect is positive trace class with trace log degree, but its prime-ray lift is the classical Hardy/Poisson route

## Claim

Continue `WP-073` in its Hardy-coordinate realization. Under

\[
T_1f=\frac{f-f(1)}{z-1},
\]

the normalized pointed-cover isometry is

\[
\widetilde W_n g(z)
:=
\frac1{\sqrt n}(1+z+\cdots+z^{n-1})g(z^n),
\qquad n\ge1.
\tag{1}
\]

Let `N` be the Hardy number operator,

\[
Ne_k=ke_k,
\qquad e_k(z)=z^k,
\]

and put

\[
\boxed{L:=N+\frac12 I.}
\tag{2}
\]

Then the same cover geometry has an exact positive scale defect not visible in `WP-073`:

\[
\boxed{
Q_n
:=
n\widetilde W_n^*L^{-1}\widetilde W_n-L^{-1}
\succeq0,
\qquad
Q_n\in S_1,
\qquad
\operatorname{Tr}Q_n=\log n.
}
\tag{3}
\]

The half-integer shift in `L` is not fitted to obtain (3). It is uniquely forced by pure degree covariance:

\[
\boxed{
\widetilde W_n^*L\widetilde W_n=nL.
}
\tag{4}
\]

More precisely,

\[
\widetilde W_n^*N\widetilde W_n
=nN+\frac{n-1}{2}I,
\tag{5}
\]

so among affine shifts `N+cI`, equation (4) for any `n>1` holds if and only if `c=1/2`.

This gives a genuinely stronger finite-place synthesis than `WP-073`. For a prime `p`, let

\[
u_{p,k}:=\widetilde W_{p^k}e_0.
\]

Then

\[
\langle u_{p,k},u_{p,\ell}\rangle
=p^{-|k-\ell|/2}
\tag{6}
\]

and therefore

\[
\boxed{
G_p(k,\ell)
:=
\operatorname{Tr}(Q_p)
\langle u_{p,k},u_{p,\ell}\rangle
=
(\log p)p^{-|k-\ell|/2}
}
\tag{7}
\]

is a positive-semidefinite prime-ray Gram kernel whose first row is exactly

\[
G_p(0,k)=\frac{\log p}{p^{k/2}}.
\tag{8}
\]

Thus **both factors in the finite Weil prime-power weight are now forced by the same pointed-cover Hilbert geometry**: the half-weight is the cover-isometry matrix coefficient from `WP-073`, while `log p` is the trace of the independently positive inverse-scale defect `Q_p`. No cyclotomic boundary value `Phi_{p^k}(1)`, zeta zero, fitted conductance, or hand-inserted generator energy is needed for (8).

However this still does **not** yield global Weil positivity. Three exact obstructions remain.

1. The all-degree defect gives `Tr Q_n=log n`, not `Lambda(n)`. To keep `log p` constant along `p,p^2,...`, one must retain the decomposition into iterates of the primitive semigroup generator `p`. Applying the same defect directly to degree `p^k` gives `Tr Q_{p^k}=k log p`. Prime-power support therefore comes from the primitive-generator/Euler-ray decomposition, not from positivity itself.
2. The bilateral Toeplitz extension of (7) has the positive Poisson symbol

   \[
   (\log p)P_{p^{-1/2}}(\theta),
   \]

   while the nonconstant finite Weil multiplier is

   \[
   -2(\log p)\sum_{k\ge1}p^{-k/2}\cos(k\theta)
   =
   (\log p)\bigl(1-P_{p^{-1/2}}(\theta)\bigr),
   \tag{9}
   \]

   which changes sign. The exact finite coefficient therefore sits in a positive Gram kernel, but the map from that kernel to the Weil summand is again an indefinite subtraction, matching the obstruction already isolated by `WP-005` and the Poisson-score route of `WP-022`.
3. The same forced half-integer operator `L` does know the **nonconstant Riemann digamma profile** through the trace-class relative resolvent

   \[
   \boxed{
   \operatorname{Tr}\!\left[
   (L+\tfrac12 I)^{-1}
   -
   (L+\tfrac{s-1}{2}I)^{-1}
   \right]
   =
   \psi(s/2)+\gamma,
   }
   \tag{10}
   \]

   but this relative response is not a positive self-adjoint form on the critical line and does not force the `-\tfrac12\log\pi` normalization or the polar terms. Hence the appearance of the correct Gamma/digamma *shape* is structural evidence, not a global sign theorem.

**Evidence status:** `EXACT-DERIVED + POSITIVE-BRIDGE + PRIOR-ART-REDIRECT + DECISIVE-LIMITATION`.

## 1. The half-integer number operator is forced by cover covariance

Equation (1) acts on the Hardy basis by block replication:

\[
\widetilde W_ne_k
=
\frac1{\sqrt n}
\sum_{r=0}^{n-1}e_{nk+r}.
\tag{11}
\]

Therefore

\[
\begin{aligned}
\widetilde W_n^*N\widetilde W_ne_k
&=
\frac1n\sum_{r=0}^{n-1}(nk+r)e_k\\
&=
\left(nk+\frac{n-1}{2}\right)e_k.
\end{aligned}
\]

This proves (5). For `A_c=N+cI`,

\[
\widetilde W_n^*A_c\widetilde W_n
=nN+\left(\frac{n-1}{2}+c\right)I.
\]

Requiring this to equal

\[
nA_c=nN+ncI
\]

for one nontrivial degree `n>1` gives

\[
\frac{n-1}{2}+c=nc,
\]

hence uniquely

\[
c=\frac12.
\]

Thus `L=N+1/2` is not chosen because half-integers occur in the Riemann Gamma factor. It is the unique affine Hardy number operator with exact degree covariance under the normalized root covers.

This can also be read as a discrete conformal-weight statement: the same normalization `n^{-1/2}` that makes the cover action isometric forces the spectral origin to lie at the half-integer lattice.

## 2. A positive inverse-scale defect has exactly trace `log n`

Because `L>=1/2`, its inverse is bounded and positive. Since `\widetilde W_n` is an isometry, the map

\[
\Phi_n(X)=\widetilde W_n^*X\widetilde W_n
\]

is unital positive. The function `x -> x^{-1}` is operator convex on `(0,infinity)`, so Jensen gives

\[
\widetilde W_n^*L^{-1}\widetilde W_n
\succeq
(\widetilde W_n^*L\widetilde W_n)^{-1}
=
(nL)^{-1}.
\]

Multiplication by `n` gives the positivity in (3).

No abstract operator-convexity theorem is actually required here. Equation (11) makes `Q_n` diagonal:

\[
Q_ne_k=q_n(k)e_k,
\]

with

\[
\boxed{
q_n(k)
=
\sum_{r=0}^{n-1}
\frac1{nk+r+1/2}
-
\frac1{k+1/2}.
}
\tag{12}
\]

The arithmetic mean of the `n` positive numbers

\[
nk+r+\frac12,
\qquad 0\le r<n,
\]

is exactly `n(k+1/2)`. Convexity of `x^{-1}` therefore gives `q_n(k)>=0` term by term.

The large-`k` expansion is

\[
q_n(k)
=
\frac{n^2-1}{12n^2(k+1/2)^3}
+O_n(k^{-5}),
\tag{13}
\]

because the centered residues

\[
r-\frac{n-1}{2}
\]

have mean zero and variance `(n^2-1)/12`. Hence `Q_n` is positive trace class.

The trace is exact. For a finite cutoff `M`, the block indices in (12) enumerate `0,...,nM-1`, so

\[
\begin{aligned}
\sum_{k=0}^{M-1}q_n(k)
&=
\sum_{j=0}^{nM-1}\frac1{j+1/2}
-
\sum_{k=0}^{M-1}\frac1{k+1/2}\\
&=
\psi(nM+1/2)-\psi(M+1/2).
\end{aligned}
\tag{14}
\]

Since `psi(x)=log x+O(1/x)`, letting `M->infinity` yields

\[
\boxed{\operatorname{Tr}Q_n=\log n.}
\]

This is the main new positive fact. The logarithm of the covering degree is not being read from an externally supplied Hamiltonian; it is the total mass of a canonical positive trace-class defect measuring the failure of inverse scale to transform linearly under block refinement.

## 3. The finite prime-power coefficient becomes a positive Gram first row

For `p` prime and `k>=0`, equation (11) iterated gives

\[
u_{p,k}
=\widetilde W_{p^k}e_0
=\frac1{p^{k/2}}
\sum_{j=0}^{p^k-1}e_j.
\tag{15}
\]

If `k<=ell`, the first `p^k` coefficients overlap, so

\[
\langle u_{p,k},u_{p,\ell}\rangle
=
\frac{p^k}{p^{(k+\ell)/2}}
=p^{-(\ell-k)/2}.
\]

Multiplying this Gram kernel by the positive scalar `Tr Q_p=log p` proves (7).

In particular,

\[
\boxed{
\operatorname{Tr}(Q_p)
\langle e_0,\widetilde W_{p^k}e_0\rangle
=(\log p)p^{-k/2}.
}
\tag{16}
\]

This differs materially from `WP-073`. There the `n^{-1/2}` came from cover geometry but `Lambda(n)` was still supplied by the cyclotomic shell boundary identity. Here, after restricting to a primitive prime ray, both `log p` and `p^{-k/2}` are generated by the same Hardy-coordinate cover system.

It also differs from simply declaring `log p` to be the generator energy, as in the Prime-Lattice/Bost--Connes skeleton. The equality `Tr Q_p=log p` is a positive trace theorem inside the pointed-cover representation.

## 4. The positive local kernel is exactly Poisson, and Weil requires subtracting it

Set

\[
r=p^{-1/2}.
\]

The bilateral extension of the scalar kernel in (7) is

\[
g_p(j)=(\log p)r^{|j|},
\qquad j\in\mathbb Z.
\]

Its Fourier symbol is the standard Poisson kernel

\[
\widehat g_p(\theta)
=(\log p)
\frac{1-r^2}{1-2r\cos\theta+r^2}
=(\log p)P_r(\theta)>0.
\tag{17}
\]

Thus the positive ray kernel obtained from `Q_p` is not a new mysterious local object: it lands exactly on the Poisson/GCD boundary already encountered in `WP-022`.

But the finite prime contribution in the Weil multiplier uses only the nonconstant cosine part with the opposite sign:

\[
-2(\log p)\sum_{k\ge1}r^k\cos(k\theta)
=(\log p)(1-P_r(\theta)).
\tag{18}
\]

The right side is indefinite. At `theta=0`, `P_r(0)=(1+r)/(1-r)>1`; at `theta=pi`, `P_r(pi)=(1-r)/(1+r)<1`. Hence `1-P_r` changes sign for every `0<r<1`.

This gives an exact local-to-Weil diagnosis:

```text
positive inverse-scale defect Q_p
    -> Tr Q_p = log p
positive cover-orbit Gram
    -> p^{-|k-l|/2}
product
    -> log p * Poisson covariance
Weil finite summand
    -> identity minus that covariance
    -> indefinite
```

So the new positive trace theorem improves the origin of the finite coefficients, but it does not evade `WP-005`. It makes the obstruction sharper: even when the coefficient `log p` is itself the trace of a positive Mathia-native operator, the required autocorrelation/sign assembly is still not positivity preserving.

## 5. The same forced operator contains the digamma profile

The spectrum of `L` is

\[
\left\{k+\frac12:k\ge0\right\}.
\]

For `Re(s)>0`, the resolvent difference

\[
(L+\tfrac12 I)^{-1}
-
(L+\tfrac{s-1}{2}I)^{-1}
\]

is trace class, since its diagonal entries are

\[
\frac1{k+1}-\frac1{k+s/2}=O_s(k^{-2}).
\]

Therefore

\[
\begin{aligned}
R_\infty(s)
&:=
\operatorname{Tr}\!\left[
(L+\tfrac12 I)^{-1}
-
(L+\tfrac{s-1}{2}I)^{-1}
\right]\\
&=
\sum_{k\ge0}
\left(
\frac1{k+1}
-
\frac1{k+s/2}
\right)\\
&=
\psi(s/2)+\gamma.
\end{aligned}
\tag{19}
\]

Thus the same `L` that is forced by the cover covariance and produces the positive defects `Q_n` also carries the nonconstant digamma profile of the Riemann archimedean factor. Indeed

\[
\frac{d}{ds}
\log\left(\pi^{-s/2}\Gamma(s/2)\right)
=
\frac12\psi(s/2)-\frac12\log\pi
\tag{20}
\]

can be written as one half of (19) plus a scalar normalization.

This is stronger than a numerical resemblance to half-integer spectra: equation (19) is an exact convergent relative trace. But it is not enough for the mandate. The additive constant `-\tfrac12\log\pi` is not forced by (19), the polar `s=0,1` sector is absent, and on `s=1/2+it` the second resolvent in (19) is non-self-adjoint. The real archimedean Weil multiplier therefore does not inherit the positivity of `Q_n`.

## 6. Primitive-generator audit: positivity gives `log n`, not `Lambda(n)`

Equation (3) holds for **every** degree `n`, prime or composite:

\[
\operatorname{Tr}Q_n=\log n.
\]

If it is applied directly at degree `p^k`, then

\[
\operatorname{Tr}Q_{p^k}
=k\log p,
\tag{21}
\]

whereas

\[
\Lambda(p^k)=\log p.
\]

Therefore (16) relies on remembering that `p^k` is the `k`-fold iterate of the primitive generator `p` and attaching the scale defect once to that primitive ray. This is canonical in the free multiplicative semigroup, but it is arithmetic factorization data, not a consequence of the operator inequality `Q_n>=0`.

Equivalently, if one insists on starting from the all-degree positive scalar `log n`, then

\[
\log n=\sum_{d\mid n}\Lambda(d)
\]

and recovering `Lambda` requires Möbius inversion, hence signs. The positive defect by itself does not positively annihilate integers with more than one prime factor.

This distinction is essential for novelty. The new geometry supplies a positive **log-degree cocycle**. Turning that cocycle into the von Mangoldt prime-power selector still uses the classical Euler decomposition or a signed inversion.

## 7. Semigroup cocycle structure

Define the positive transfer map

\[
\mathcal E_n(X):=
n\widetilde W_n^*X\widetilde W_n.
\]

Since `\widetilde W_m\widetilde W_n=\widetilde W_{mn}`,

\[
\mathcal E_{mn}=\mathcal E_n\circ\mathcal E_m.
\]

The defect is the coboundary

\[
Q_n=\mathcal E_n(L^{-1})-L^{-1},
\]

and therefore

\[
\boxed{
Q_{mn}=Q_n+\mathcal E_n(Q_m).
}
\tag{22}
\]

Both summands on the right are positive. Taking traces recovers additivity of the logarithm,

\[
\operatorname{Tr}Q_{mn}
=\log(mn)
=\log m+\log n.
\]

So `log degree` appears as a positive trace cocycle of the cover semigroup. This algebraic compatibility makes (3) more than an isolated harmonic-sum identity, while also explaining why it naturally gives `log n` rather than the primitive-weight function `Lambda(n)`.

## 8. Matched all-composite control

The construction is not specific to rational primes. Choose any family of pairwise coprime composite integers, for example

\[
a_1=6,\quad a_2=35,\quad a_3=143,\ldots
\]

with disjoint ordinary-prime supports. They freely generate a commutative multiplicative monoid. For every generator `a_j`, the same operators satisfy

\[
Q_{a_j}\succeq0,
\qquad
\operatorname{Tr}Q_{a_j}=\log a_j,
\]

and the generator ray has the positive Gram kernel

\[
(\log a_j)a_j^{-|k-\ell|/2}.
\]

Thus the complete local mechanism

\[
\text{positive log-generator trace}
+
\text{critical half-density orbit}
\]

survives an all-composite generalized-prime control. It cannot by itself force the functional equation, the Riemann Gamma normalization, or RH-specific global positivity.

What is special to the rational-prime application is the external identification of the primitive multiplicative generators with the actual primes of `Q`. The Hilbert-space theorem (3) knows degree and refinement, not primality.

## 9. Prior-art and novelty audit

The most important audit result is a **direct prior-art identification that sharpens `WP-073`**.

Juan Manzur, Waleed Noor, and Charles F. Santos study on classical `H^2` exactly the unnormalized operators

\[
W_nf(z)=(1+z+\cdots+z^{n-1})f(z^n).
\]

Their 2023 JMAA paper, building on Noor's 2019 Hardy-space Báez--Duarte work, records

\[
W_n^*W_n=nI
\]

and therefore that `W_n/sqrt(n)` is a semigroup of isometries; it also emphasizes that this same weighted-composition semigroup already has several RH-equivalent cyclicity/invariant-subspace formulations. Under `T_1`, the normalized operator of `WP-073` is **exactly** `W_n/sqrt(n)`, not merely analogous to it.

Accordingly, no historical novelty is claimed for the semigroup, its isometric normalization, or an RH connection. The Mathia-specific content of the present finding is the directed synthesis with the forced covariant number operator `L`, the positive inverse-scale trace identity (3), and its interaction with the `WP-073` half-density orbit.

A targeted literature search did not locate the exact formula `Tr Q_n=log n` stated for this RH-weighted-composition semigroup, but the formula is elementary from its block action and is not promoted as a new theorem of operator theory. Its value here is evidential: it tests whether the already-classical semigroup contains a positive structure relevant to the much stronger Weil-positivity mandate.

The result also lands on known boundaries already present in this branch:

- `WP-010` and the Nyman--Beurling literature warn that Hardy-space cyclicity/totality formulations are RH-equivalent reformulations, not independent sign theorems.
- `WP-022` shows that Poisson geometry produces the exact critical finite coefficients but Fisher positivity diverges and the signed score is not Weil positivity. Equation (17) identifies the present prime-ray Gram with that same Poisson family at the critical radius.
- `PC-010` and `WP-012` place bare multiplicative/cyclotomic semigroup structure near Bost--Connes and endomotive prior art.

Therefore (3) should be retained as a strong positive local bridge, but not promoted as evidence that the classical weighted-composition semigroup already proves a global Weil criterion.

## 10. Exact falsification surface

The finding has direct exact checks:

1. verify the block formula (11) and `\widetilde W_n^*\widetilde W_n=I`;
2. verify (5), and hence uniqueness of the shift `1/2` in (4);
3. compute `Q_n` on basis vectors and verify (12) termwise;
4. verify `q_n(k)>=0` by convexity of `x^{-1}` and the centered-block arithmetic mean;
5. verify the `k^{-3}` asymptotic and trace-class property;
6. telescope the finite trace through the digamma identity (14) and verify `Tr Q_n=log n`;
7. verify the orbit Gram (6) and its Poisson symbol (17);
8. verify that the finite Weil nonconstant symbol is `log p(1-P_r)` and changes sign;
9. verify the relative-resolvent identity (19) directly from the standard convergent series for `psi`;
10. falsify any claimed von-Mangoldt interpretation that applies `Q_{p^k}` directly without accounting for the factor `k` in (21);
11. falsify any global-positivity promotion unless one coupled construction also forces the polar sector, the `pi` normalization, the finite/autocorrelation signs, and a nonnegative global quadratic form independently of RH.

## Research consequence

`WP-073` showed that pointed-cover isometry forces the critical half-density. The present calculation shows that the **same exact Hardy-coordinate cover system contains substantially more arithmetic-looking positive structure**:

\[
\boxed{
\widetilde W_n^*L\widetilde W_n=nL,
\qquad
Q_n:=n\widetilde W_n^*L^{-1}\widetilde W_n-L^{-1}\succeq0,
\qquad
\operatorname{Tr}Q_n=\log n.
}
\]

Consequently a primitive prime ray has the canonical positive Gram kernel

\[
\boxed{
G_p(k,\ell)
=(\log p)p^{-|k-\ell|/2},
}
\]

so the exact finite Weil weights occur as positive Gram matrix coefficients with `log p` itself supplied by a positive trace defect.

At the same time the novelty audit and sign calculation prevent overpromotion. The underlying weighted-composition semigroup is classical RH prior art; the local Gram kernel is exactly Poisson; selecting `Lambda` requires primitive Euler rays; and the Weil summand is `identity - Poisson`, hence indefinite. The forced half-integer operator also reproduces the digamma profile through a relative resolvent, but not the full archimedean/polar completion or its positivity.

The surviving research target is therefore narrower and more concrete: **look for a Mathia-native global coupling of the positive defects `Q_p`, the cover-orbit Gram, and the half-integer operator `L` in which the finite subtraction and the archimedean/polar response arise as one compression/quotient/intersection form with an independent sign theorem.** Direct sums of the local positive kernels, or a return to Hardy cyclicity/Poisson scores, are already prior-art or fail the sign gate.
