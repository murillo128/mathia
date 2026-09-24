# AF-540 — Higher log-jets defeat arbitrary tail-multiplier nuisance

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `CARRIER-SHAPE` · `NUISANCE-ANNIHILATION` · `SOURCE-FORCED-TRANSVERSALITY` · `RECOVERY` · `NO-NOVELTY-CLAIM`

## Claim

Keep the exact anchored outward-tail carrier of AF-525–AF-539,

\[
D_{X,C}(t)
=
\frac{(C^{1+t}-1)B_0(X,t)}{P(1+t)},
\qquad
B_0(X,t)=\sum_{p\le X}p^{-1-t},
\]

and compare the power-separated cutoffs

\[
B_A=\lfloor A^\theta\rfloor,
\qquad 0<\theta<1,
\]

through the exact projective ratio

\[
R_A(t)
=
\frac{D_{B_A,\widetilde C_A}(t)}{D_{A,C_A}(t)}
=
\frac{\widetilde C_A^{1+t}-1}{C_A^{1+t}-1}
\frac{B_0(B_A,t)}{B_0(A,t)}.
\]

Here the integer multipliers `C_A,\widetilde C_A\ge2` are now **completely arbitrary**: no AF-525 admissibility condition, no upper growth bound, and no co-tuning assumption is imposed.

Write

\[
L_A=\log A,
\qquad
H_A=\log L_A.
\]

Then for every fixed integer `k\ge2`,

\[
\boxed{
\frac{H_A}{L_A^k}(\log R_A)^{(k)}(0)
\longrightarrow
(-1)^{k+1}\frac{1-\theta^k}{k}
}
\tag{1}
\]

**uniformly over all choices of the multiplier sequences** `C_A,\widetilde C_A\ge2`.

In particular, the second projective log-jet already gives

\[
\boxed{
\frac{H_A}{L_A^2}(\log R_A)''(0)
\longrightarrow
-\frac{1-\theta^2}{2},
}
\tag{2}
\]

so the hidden anchor exponent is recovered by

\[
\boxed{
\theta
=
\sqrt{
1+2\frac{H_A}{L_A^2}(\log R_A)''(0)
}
+o(1).
}
\tag{3}
\]

This removes the critical multiplier obstruction found in AF-539. The first log-slope can be cancelled once multiplier logarithms reach the arithmetic scale `L_A/H_A`, but every fixed log-jet of order at least two is asymptotically immune even if the multipliers grow arbitrarily fast.

The reason is structural. The dangerous part of

\[
\log(C^{1+t}-1)
\]

is exactly affine in `t`, hence disappears after two derivatives; the remaining nonlinear correction has all fixed higher derivatives uniformly bounded over every integer `C\ge2`. By contrast, the `k`-th logarithmic shape cumulant of the retained prime prefix has size `L_A^k/H_A`.

This is a recovery theorem for the coarse anchor exponent inside the exact carrier family, not a rational-prime uniqueness theorem.

## Derivation

### 1. Exact decomposition into multiplier and source shape

Put

\[
\phi_C(t)=\log(C^{1+t}-1).
\]

Then

\[
\log R_A(t)
=
\phi_{\widetilde C_A}(t)-\phi_{C_A}(t)
+
\log B_0(B_A,t)-\log B_0(A,t).
\tag{4}
\]

The common prime-zeta factor has already cancelled exactly, so every term in `(4)` is smooth at `t=0`.

Write `a=\log C` and `q=C^{-1}`. The multiplier term has the exact representation

\[
\phi_C(t)
=(1+t)a+\log(1-qe^{-at}).
\tag{5}
\]

For `k\ge2`, the affine term contributes nothing. Expanding the second term by its absolutely convergent logarithmic series at `t=0` gives

\[
\phi_C^{(k)}(0)
=
(-1)^{k+1}(\log C)^k
\sum_{m\ge1}m^{k-1}C^{-m}
=
(-1)^{k+1}(\log C)^k
\operatorname{Li}_{1-k}(C^{-1}).
\tag{6}
\]

For each fixed `k\ge2`, the right-hand side is uniformly bounded for all real `C\ge2`, hence a fortiori for all integer `C\ge2`. Indeed it is continuous on `[2,\infty)` and, as `C\to\infty`,

\[
(\log C)^k\operatorname{Li}_{1-k}(C^{-1})
\sim\frac{(\log C)^k}{C}
\longrightarrow0.
\tag{7}
\]

Therefore there is a constant `K_k<\infty`, independent of `A` and of the multiplier choices, such that

\[
\left|
\phi_{\widetilde C_A}^{(k)}(0)-\phi_{C_A}^{(k)}(0)
\right|
\le2K_k.
\tag{8}
\]

Consequently,

\[
\sup_{C_A,\widetilde C_A\ge2}
\frac{H_A}{L_A^k}
\left|
\phi_{\widetilde C_A}^{(k)}(0)-\phi_{C_A}^{(k)}(0)
\right|
\longrightarrow0.
\tag{9}
\]

This is the decisive difference from the first derivative. AF-539 has

\[
\phi_C'(0)=\frac{C\log C}{C-1}\sim\log C,
\]

which is unbounded and can compete with the arithmetic first-shape scale `L_A/H_A`. No analogous growing multiplier direction survives at any fixed derivative order `k\ge2`.

### 2. Prime-prefix log-jets are cumulants

Define

\[
S(X)=\sum_{p\le X}\frac1p,
\qquad
M_j(X)=\sum_{p\le X}\frac{(\log p)^j}{p}.
\]

Give each prime `p\le X` probability weight

\[
\pi_X(p)=\frac{1}{pS(X)},
\]

and let `Y_X=\log p` under this finite probability measure. Then

\[
\frac{B_0(X,t)}{S(X)}
=\mathbb E[e^{-tY_X}],
\]

so for every fixed `k\ge1`,

\[
(\log B_0(X,\cdot))^{(k)}(0)
=(-1)^k\kappa_k(X),
\tag{10}
\]

where `\kappa_k(X)` is the `k`-th cumulant of `Y_X`.

The classical Mertens estimates used throughout AF-525–AF-539 are

\[
S(X)=\log\log X+B_1+O((\log X)^{-1})
\tag{11}
\]

and

\[
M_1(X)=\log X+O(1).
\tag{12}
\]

For every fixed integer `j\ge2`, partial summation applied to `(12)` gives

\[
M_j(X)
=(\log X)^{j-1}M_1(X)
-(j-1)\int_2^X
\frac{(\log u)^{j-2}M_1(u)}{u}\,du,
\]

and hence

\[
\boxed{
M_j(X)=\frac{(\log X)^j}{j}+O((\log X)^{j-1}).
}
\tag{13}
\]

Thus the normalized raw moments

\[
m_j(X)=\mathbb E[Y_X^j]=\frac{M_j(X)}{S(X)}
\]

satisfy, for each fixed `j\ge1`,

\[
m_j(X)
=
\frac{(\log X)^j}{j\log\log X}(1+o(1)).
\tag{14}
\]

For fixed `k\ge2`, the cumulant polynomial has leading term `m_k` and every other monomial is a product of at least two raw moments whose total degree is `k`. By `(14)`, every such product is

\[
O\!\left(
\frac{(\log X)^k}{(\log\log X)^2}
\right)
=o\!\left(
\frac{(\log X)^k}{\log\log X}
\right).
\]

Therefore

\[
\boxed{
\kappa_k(X)
=
\frac{(\log X)^k}{k\log\log X}(1+o(1))
\qquad(k\ge2\text{ fixed}).
}
\tag{15}
\]

### 3. Power-separated anchors retain a universal higher-jet gap

For `B_A=\lfloor A^\theta\rfloor`,

\[
\log B_A=\theta L_A+o(1),
\qquad
\log\log B_A=H_A+\log\theta+o(1).
\tag{16}
\]

Applying `(15)` at `A` and `B_A` yields

\[
\frac{H_A}{L_A^k}\kappa_k(A)
\longrightarrow\frac1k,
\qquad
\frac{H_A}{L_A^k}\kappa_k(B_A)
\longrightarrow\frac{\theta^k}{k}.
\tag{17}
\]

Using `(10)`,

\[
\frac{H_A}{L_A^k}
\left[
(\log B_0(B_A,\cdot))^{(k)}(0)
-
(\log B_0(A,\cdot))^{(k)}(0)
\right]
\longrightarrow
(-1)^{k+1}\frac{1-\theta^k}{k}.
\tag{18}
\]

Finally combine `(4)`, `(9)`, and `(18)` to obtain `(1)`. The multiplier bound `(9)` is uniform over the entire choice set `C_A,\widetilde C_A\ge2`, which proves the claimed uniform nuisance immunity.

For `k=2`, `(1)` becomes `(2)`, and `(3)` follows because `0<\theta<1` fixes the positive square-root branch.

## Representation expansion and fidelity audit

Three natural representations of the AF-539 obstruction lead to different conclusions.

**First log-jet.** Retaining `(\log R_A)'(0)` exposes the first reciprocal-prime log moment and recovers `\theta` only while the multiplier log-drift stays below the `L_A/H_A` scale. AF-539 proved that this threshold is sharp for that coordinate.

**Higher log-jet.** Equation `(5)` separates the multiplier into an affine log-scale component `(1+t)\log C` and a bounded nonlinear correction. Any derivative of order at least two annihilates the entire unbounded affine nuisance direction before asymptotics are taken. The source side does not disappear: its fixed-order cumulants grow like `L_A^k/H_A`. This produces the strictly stronger recovery theorem `(1)`.

**Finite-difference / relational version.** A second finite difference of `\log R_A(t)` also annihilates an exactly affine log-multiplier component, suggesting a non-infinitesimal analogue. But the nonlinear correction and the source approximation then depend on the chosen window size, so a sharp finite-resolution theorem needs additional scale control and is not claimed here.

The higher-jet representation is therefore the strongest exact theorem currently justified by the carrier. It does not add an arbitrary marker: it retains another intrinsic local shape coordinate of the same exact projective ratio already used in AF-528 and AF-539.

The result also sharpens the meaning of the AF-539 threshold. `L_A/H_A` is a sharp nuisance threshold for **first projective shape**, not for the full local projective germ. Once second shape is retained, the same multiplier family has no asymptotic cancellation direction at all.

## Falsification and matched-control audit

The nearest falsifier is to let the nuisance family become more flexible in `t`, rather than merely enlarging the integer multiplier size. The theorem uses the exact source-forced form

\[
C^{1+t}-1.
\]

Its unbounded dependence on `C` enters `\log` affinely in `t`. A nuisance factor of the form `\exp(h_A(t))` with unrestricted second derivative of size `L_A^2/H_A` could cancel `(2)`. Thus the recovery comes from the **functional rigidity of the transport nuisance**, not from differentiation alone.

Likewise, `(1)` does not isolate rational primes. The source term is controlled only by the reciprocal-prime moment hierarchy `(11)`–`(13)`. A generalized-prime or other matched source reproducing these fixed-order weighted moment asymptotics would reproduce the same limits. Such systems remain valid controls against a primality-specific interpretation.

The result is also not a statement of practical finite-resolution stability. A high derivative at one boundary point may be difficult to estimate from a shrinking physical observation window. AF-529–AF-532 already separate exact recoverability from conditioning/noise, and the same distinction remains here.

## Boundaries

1. **Exact carrier ratio only.** As in AF-528 and AF-539, the theorem concerns the exact carrier ratio `R_A`. AF-525 supplies value-level asymptotics for the curvature defect but not the derivative bounds needed to transfer the higher-jet statement automatically to curvature-defect ratios.

2. **Fixed derivative order.** Equation `(1)` holds for each fixed `k\ge2`. No uniform statement as `k\to\infty` is claimed; the constants `K_k` from `(8)` may grow rapidly with `k`.

3. **Fixed power separation.** The theorem is stated for fixed `\theta\in(0,1)`. A uniform result over compact subsets of `(0,1)` should follow from uniform versions of the same estimates but is not asserted here.

4. **Coarse anchor recovery only.** The recovered parameter is `\theta`, not the exact cutoff, the rational-prime set, or a zero-sensitive invariant.

5. **Rigid multiplier shape.** Arbitrary growth in the scalar multiplier `C_A` is allowed, but arbitrary `t`-dependent multiplier functions are not. The exact transport law is essential.

6. **No finite-resolution conditioning theorem.** The statement is infinitesimal and asymptotic. It does not claim that second or higher derivatives can be estimated stably from noisy sampled data at the available boundary-layer scales.

## Prior-art / source audit

The number-theoretic input is classical. Terence Tao, *Mertens' theorems* (11 December 2013), https://terrytao.wordpress.com/2013/12/11/mertens-theorems/ , records

\[
\sum_{p\le x}\frac{\log p}{p}=\log x+O(1)
\]

and the reciprocal-prime Mertens estimate used in `(11)`. The higher weighted moments `(13)` follow directly by partial summation and are not claimed as new number theory.

The identification of derivatives of a log Laplace transform with cumulants is standard exponential-family/probability theory; the Encyclopedia of Mathematics entry *Natural exponential family of probability distributions*, https://encyclopediaofmath.org/wiki/Natural_exponential_family_of_probability_distributions , records the logarithm of the Laplace transform as the cumulant function.

The multiplier series in `(6)` is the standard polylogarithm series. NIST DLMF §25.12, https://dlmf.nist.gov/25.12 , defines

\[
\operatorname{Li}_s(z)=\sum_{m\ge1}\frac{z^m}{m^s}
\]

for `|z|<1`, from which `(6)` follows by termwise differentiation of the absolutely convergent logarithmic series.

No novelty is claimed for cumulants, partial summation, polylogarithms, or annihilation of affine functions by higher derivatives. The durable Mathia result is their exact combination on the AF-525 carrier: **the first-jet nuisance threshold of AF-539 disappears completely at every fixed higher projective log-jet because the exact transport law forces all unbounded multiplier motion into an affine log direction.**

## Consequence

AF-539 identified the precise scale at which multiplier freedom can erase the first projective boundary shape. That obstruction is not persistent under a minimal increase in retained local shape: the second log-jet already recovers `\theta` uniformly over arbitrary integer multiplier growth, and every higher fixed log-jet carries the compatible invariant `1-\theta^k`.

For Arithmetic Fidelity, this gives a concrete strengthening of the source-forced-transversality principle. When nuisance enters a representation through a low-complexity functional class, the right intrinsic relational lift can annihilate the entire dangerous nuisance direction while leaving a growing source cumulant. The next useful question is therefore not whether multiplier size can be bounded more tightly, but how far this **functional-class annihilation** principle survives under more general source-forced nuisance families and under finite-resolution observation.