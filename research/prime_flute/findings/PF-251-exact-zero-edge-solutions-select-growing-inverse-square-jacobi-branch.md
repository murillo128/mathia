# PF-251 — exact zero-edge solutions select the growing inverse-square Jacobi branch

**Status:** `EXACT-DERIVED + ZERO-EDGE-BOUNDARY-CLASSIFICATION + INVERSE-SQUARE-THRESHOLD + POSITIVE/ROUTE-NARROWING`.

PF-247 identifies the fixed-axis relative operator

\[
J=A^{-1/2}LA^{-1/2}
\]

as two half-line parity Jacobi chains whose coefficients differ from the constant Dirichlet chain by `O(j^{-2})`. PF-248 shows that this perturbation is trace class but misses the first weighted moment and obtains the formal zero-edge exponents `-1/2` and `3/2`. PF-250 then proves a sharp fractional smoothing window for the **free** half-line model, while leaving its transfer to the actual first-moment-critical chains open.

The exact compactification already contains a stronger threshold statement. Because `L` is unitarily equivalent to `1-\partial_\tau^2`, its elementary zero solutions can be projected onto PF-247's exact Gegenbauer basis. The resulting coefficient sequences solve the **actual** parity-Jacobi zero recurrence, including the first half-line row, and grow like `j^{3/2}`. Discrete reduction of order then gives the independent tail solution `j^{-1/2}`.

Thus PF-248's formal exponents are the exact asymptotic branches of the actual PF-247 chains, and the half-line boundary condition selects the **growing** branch. Zero is not an `ell^2` eigenvalue and there is no bounded zero-energy solution satisfying the half-line boundary condition. The fixed-axis problem is therefore a concrete inverse-square threshold problem, not merely an arbitrary trace-class perturbation of the free chain.

## Claim

Use PF-247's notation

\[
A=-\partial_\theta^2+\csc^2\theta,
\qquad
L=-\partial_\theta(\sin^2\theta\,\partial_\theta)
+\frac34(1+\sin^2\theta),
\]

\[
\alpha=\frac{1+\sqrt5}{2},
\qquad
\kappa_n=n+\alpha,
\]

and

\[
e_n(\theta)=h_n^{-1/2}\sin^\alpha\theta\,
C_n^{(\alpha)}(\cos\theta),
\qquad
Ae_n=\kappa_n^2e_n,
\]

\[
h_n=\frac{\pi 2^{1-2\alpha}\Gamma(n+2\alpha)}
{n!(n+\alpha)\Gamma(\alpha)^2}.
\]

Identify the even and odd sectors of `J=A^{-1/2}LA^{-1/2}` with the half-line Jacobi chains of PF-247. For each parity `\varepsilon\in\{0,1\}`:

1. there is a nonzero solution `\nu^(\varepsilon)` of the **full half-line zero-energy recurrence**, including the first row, with
   \[
   \nu_j^{(\varepsilon)}=C_\varepsilon j^{3/2}(1+O(j^{-1})),
   \qquad C_\varepsilon>0;
   \]
2. on every sufficiently far tail there is an independent exact zero-energy solution
   \[
   z_j^{(\varepsilon)}=-\frac{2}{C_\varepsilon}j^{-1/2}(1+O(j^{-1}));
   \]
3. hence the exact asymptotic zero-edge exponents are
   \[
   \boxed{-\frac12,\ \frac32};
   \]
4. the actual half-line boundary condition selects the `j^{3/2}` branch, so zero is not an eigenvalue and no bounded zero-energy solution satisfies that boundary condition.

This classification does not determine matrix-element decay of `J^\sigma`, the actual normalized Robin factor, or PF-243's separated source-to-bulk maps.

## 1. Two exact differential zero modes

PF-238 defines

\[
\tau=\log\tan\frac\theta2,
\qquad
(U\phi)(\theta)=\sin^{-1/2}\theta\,\phi(\tau(\theta)),
\qquad
L=U(1-\partial_\tau^2)U^*.
\]

Since `e^\tau` and `e^{-\tau}` solve `(1-\partial_\tau^2)\phi=0`, their reflection-even and reflection-odd combinations give

\[
\boxed{
v_0(\theta)=\sin^{-3/2}\theta,
\qquad
v_1(\theta)=\cos\theta\,\sin^{-3/2}\theta,
}
\tag{1}
\]

with `Lv_0=Lv_1=0` pointwise on `(0,\pi)`.

Although these functions are not in `L^2`, pairing them with every Gegenbauer basis vector is legitimate. Near either endpoint,

\[
e_n(\theta)=O(\theta^\alpha),
\qquad
v_\varepsilon(\theta)=O(\theta^{-3/2}),
\]

so the Green boundary term satisfies

\[
\sin^2\theta\,(v_\varepsilon e_n'-v_\varepsilon'e_n)
=O(\theta^{\alpha-1/2})\to0
\]

because `\alpha>1/2`. Therefore

\[
\langle Le_n,v_\varepsilon\rangle
=\langle e_n,Lv_\varepsilon\rangle=0.
\tag{2}
\]

Parity leaves only even coefficients for `v_0` and only odd coefficients for `v_1`.

## 2. Exact Gegenbauer moments

Put

\[
\beta:=\frac{\alpha-1/2}{2}=\frac{\sqrt5}{4}.
\]

For the even mode define

\[
I_j:=\int_0^\pi
\sin^{\alpha-3/2}\theta\,
C_{2j}^{(\alpha)}(\cos\theta)\,d\theta.
\tag{3}
\]

Writing `C_{2j}^{(\alpha)}` as a terminating Gauss hypergeometric series reduces (3) to a terminating well-poised `{}_3F_2(1)`. Watson's classical summation gives

\[
\boxed{
I_j=
\frac{\Gamma(\alpha+1/2)}{\beta\Gamma(2\alpha)}
\frac{\Gamma(2j+2\alpha)}{\Gamma(2j+1)}
\frac{\Gamma(j+1/2)\Gamma(j+\beta+1)}
{\Gamma(j+\alpha+1/2)\Gamma(j+\beta+1/2)}.
}
\tag{4}
\]

At `j=0` this reduces to the elementary beta integral

\[
I_0=\sqrt\pi\,\frac{\Gamma(\beta)}{\Gamma(\beta+1/2)},
\]

which checks the normalization.

For the odd mode set

\[
K_j:=\int_0^\pi
\sin^{\alpha-3/2}\theta\cos\theta\,
C_{2j+1}^{(\alpha)}(\cos\theta)\,d\theta.
\tag{5}
\]

The standard Gegenbauer recurrence gives

\[
\boxed{
K_j=
\frac{j+1}{2j+1+\alpha}I_{j+1}
+\frac{j+\alpha}{2j+1+\alpha}I_j.
}
\tag{6}
\]

All factors in (4) are positive, so both moment sequences are nonzero.

## 3. Projection solves the actual half-line recurrence

Define the boundary-selected sequences

\[
\boxed{
\nu_j^{(0)}=(2j+\alpha)\frac{I_j}{\sqrt{h_{2j}}},
\qquad
\nu_j^{(1)}=(2j+1+\alpha)\frac{K_j}{\sqrt{h_{2j+1}}}.
}
\tag{7}
\]

For either parity, the `j`-th Jacobi row is a finite sum because PF-247 proves exact parity tridiagonality. With `c_n=\langle e_n,v_\varepsilon\rangle`, equation (2) gives

\[
\frac1{\kappa_n}
\sum_{m\in\{n-2,n,n+2\}}
\langle e_n,Le_m\rangle c_m
=\frac1{\kappa_n}\langle Le_n,v_\varepsilon\rangle=0.
\tag{8}
\]

Thus (7) satisfies every Jacobi row, including the origin row. No asymptotic boundary condition has been imposed.

Gamma-ratio asymptotics in (4) give

\[
I_j=C_Ij^{\alpha-1/2}(1+O(j^{-1})),
\qquad C_I>0,
\]

and (6) gives the same power for `K_j`. PF-247's exact norm satisfies

\[
\sqrt{h_{2j+\varepsilon}}
=C_hj^{\alpha-1}(1+O(j^{-1})),
\qquad C_h>0,
\]

while

\[
\kappa_{2j+\varepsilon}=2j+O(1).
\]

Therefore

\[
\boxed{
\nu_j^{(\varepsilon)}
=C_\varepsilon j^{3/2}(1+O(j^{-1})),
\qquad C_\varepsilon>0.
}
\tag{9}
\]

Equation (9) rigorously places the actual half-line boundary solution on PF-248's growing formal branch.

## 4. Exact subordinate tail by reduction of order

Write one parity recurrence as

\[
a_j u_{j+1}+b_j u_j+a_{j-1}u_{j-1}=0,
\tag{10}
\]

where PF-248 proves `a_j=-1/4+O(j^{-2})`. Take `u=\nu^(\varepsilon)` from (9); it is nonzero for all sufficiently large `j`. On such a tail define

\[
S_j:=\sum_{k=j}^\infty\frac{1}{a_ku_ku_{k+1}},
\qquad
z_j:=u_jS_j.
\tag{11}
\]

Because

\[
u_ku_{k+1}\asymp k^3,
\]

the series converges absolutely. Direct substitution gives the nonzero constant Wronskian

\[
a_j(u_jz_{j+1}-u_{j+1}z_j)=-1,
\]

so `z` is an independent exact solution on the tail. From (9),

\[
\frac{1}{a_ku_ku_{k+1}}
=-\frac{4}{C_\varepsilon^2}k^{-3}(1+O(k^{-1})),
\]

and therefore

\[
\boxed{
z_j=-\frac{2}{C_\varepsilon}j^{-1/2}(1+O(j^{-1})).
}
\tag{12}
\]

The squared tail is harmonic, so `z\notin\ell^2`; the boundary-selected solution grows. Since the first half-line Jacobi row leaves only one normalization free, every zero-energy solution satisfying the actual boundary condition is a scalar multiple of `\nu`. The subordinate solution (12) cannot satisfy that same origin row.

## 5. Exact confirmation of the inverse-square indicial law

PF-248 gives, in parity-chain indexing,

\[
a_j=-\frac14+\frac{1}{64j^2}+O(j^{-3}),
\qquad
b_j=\frac12+\frac{5}{32j^2}+O(j^{-3}).
\tag{13}
\]

For a power-law ansatz, multiplying (10) by four and collecting the `j^{-2}` terms gives

\[
2u_j-u_{j+1}-u_{j-1}+\frac{3}{4j^2}u_j\sim0.
\tag{14}
\]

The two off-diagonal corrections contribute `1/(8j^2)` and the diagonal correction contributes `5/(8j^2)`. Substituting `u_j\sim j^\sigma` gives

\[
-\sigma(\sigma-1)+\frac34=0,
\]

with roots `-1/2` and `3/2`. PF-248 used this only as a formal diagnostic. Equations (9) and (12) now supply actual solutions with both powers, so (14) is a consistency check rather than an existence argument.

## 6. Consequence for the PF-243 smoothing gate

PF-250 proves that the free spectral Dirichlet half-line power `J_0^\sigma` has an image cancellation leading to the sharp separated window

\[
R<\frac32+2\sigma.
\]

PF-251 shows that this window cannot be transferred to the actual chain merely from

\[
J-J_0\in\mathcal S_1:
\]

the canonical zero-edge solution itself changes from the free linear law to `j^{3/2}`. The first-moment failure in PF-248 is accompanied by a concrete threshold deformation.

The next fixed-axis theorem should therefore determine the low-energy spectral density/Green kernel of the actual PF-247 parity chains, or prove a weighted functional-calculus estimate strong enough to replace that information, while exploiting the exact boundary solution above. Only after that should the route spend margin on the `T_a` replacement, the hypercycle-coordinate defect, and the actual normalized Robin factor in PF-243.

PF-251 does not decide whether some `R>1` survives. It rules out only the shortcut of importing PF-250's free image cancellation through generic trace-class perturbation theory.

## 7. Prior-art and novelty audit

The special-function ingredients are classical. Gegenbauer normalization, differential equations, and recurrences are standard and recorded in DLMF Chapter 18. Equation (4) is a specialization of Watson's classical `{}_3F_2(1)` summation; a standard reference is W. N. Bailey, *Generalised Hypergeometric Series*, Cambridge Tracts in Mathematics and Mathematical Physics 32 (1935), §3.3.

Inverse-square tails for discrete Schrödinger/Jacobi operators are also classical spectral territory. D. Damanik and G. Teschl, *Bound States of Discrete Schrödinger Operators with Super-Critical Inverse Square Potentials*, Proceedings of the AMS 135 (2007), 1123--1127, DOI `10.1090/S0002-9939-06-08550-9`, is representative prior art for the generic inverse-square regime. It is not used to prove (7)--(12).

A targeted search did not locate the specific PF-238 compactified-axis / PF-247 Gegenbauer relative-Jacobi chain or the projection identity above. No general novelty is claimed for Watson summation, Gegenbauer moments, reduction of order, inverse-square Jacobi asymptotics, subordinacy, or Bessel behavior. The project-specific result is the exact threshold classification of the concrete Jacobi chains already forced by the prime-flute seam geometry.

No new statement about zeta zeros or RH follows.

## 8. Falsification and reproducibility checks

1. Substituting the two functions in (1) into PF-247's differential expression for `L` must give zero.
2. The Green boundary factor must vanish as `O(\theta^{\alpha-1/2})`; a nonzero residue would invalidate the first-row claim.
3. Equation (4) at `j=0` must equal `\sqrt\pi\Gamma(\beta)/\Gamma(\beta+1/2)`, and the odd moments must satisfy (6).
4. Substituting (7) into PF-247's exact Jacobi coefficients must give zero in every row.
5. Gamma-ratio asymptotics must give the `j^{3/2}` boundary sequence; reduction of order must give the independent `j^{-1/2}` tail with nonzero Wronskian.
6. The tail solution is not claimed to satisfy the origin row.
7. Nothing here implies PF-250-type matrix decay for the variable chain, the actual normalized Robin factor, or PF-243's source-to-bulk maps.
8. `T_a`, hypercycle reparameterization, Hardy ends, physical `P/H` recoupling, finite-pant completion, neighboring-module extension, global weak-`S_1` reassembly, wave/scattering equivalence, and every RH-level bridge remain open.
