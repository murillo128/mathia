# AF-528 — A one-derivative carrier lift recovers power-separated anchor scale

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `OUTWARD-TRANSPORT` · `CARRIER-SHAPE` · `LOWER-ORDER-FIDELITY` · `RECOVERY` · `NO-NOVELTY-CLAIM`

## Claim

Keep the co-tuned anchored outward-tail controls of AF-527. Write

\[
P(s)=\sum_p p^{-s},\qquad
B_A=\lfloor A^\theta\rfloor,\qquad
L_A=\log A,\qquad H_A=\log L_A,
\]

for a fixed \(\theta\in(0,1)\), and let \(L_B=\log B_A\), \(H_B=\log L_B\). Let \(B_1\) denote the prime reciprocal Mertens constant and define

\[
c_A=\left\lfloor e^{\sqrt{H_A}}\right\rfloor,
\qquad C_A=c_A+1,
\]

while \(d_A\) is a nearest integer to

\[
c_A\frac{H_A+B_1}{H_B+B_1},
\]

and \(\widetilde C_A=d_A+1\). For

\[
B_0(X,t)=\sum_{p\le X}p^{-1-t},
\]

the exact AF-527 carrier is

\[
D_{X,C}(t)=\frac{(C^{1+t}-1)B_0(X,t)}{P(1+t)}.
\]

Compare the two carriers by

\[
R_A(t)
=
\frac{D_{B_A,\widetilde C_A}(t)}{D_{A,C_A}(t)}
=
\frac{\widetilde C_A^{1+t}-1}{C_A^{1+t}-1}
\frac{B_0(B_A,t)}{B_0(A,t)}.
\]

The common prime-zeta factor cancels exactly, so \(R_A\) extends smoothly from \(t>0\) to \(t=0\). Then

\[
\boxed{
\frac{H_A}{L_A}\,(\log R_A)'(0)\longrightarrow 1-\theta
}
\qquad(A\to\infty).
\]

Equivalently,

\[
\theta
=
1-\frac{H_A}{L_A}(\log R_A)'(0)+o(1).
\]

Thus the same controls whose scalar boundary-layer carrier amplitudes can be co-tuned to agree beyond every algebraic order in \(1/H_A\) by AF-527 become asymptotically distinguishable after adding one infinitesimal logarithmic shape observable of the **exact carrier ratio**. This is a recovery result for the power-separated anchor exponent \(\theta\), not a claim of prime-specific recovery.

## Derivation

Set

\[
S(X)=B_0(X,0)=\sum_{p\le X}\frac1p,
\qquad
M_1(X)=\sum_{p\le X}\frac{\log p}{p}.
\]

Since

\[
\partial_t B_0(X,t)\big|_{t=0}=-M_1(X),
\]

and

\[
\partial_t\log(C^{1+t}-1)\big|_{t=0}
=
\frac{C\log C}{C-1},
\]

define

\[
g(C)=\frac{C\log C}{C-1}.
\]

Exact differentiation of the finite expression for \(R_A\) gives

\[
(\log R_A)'(0)
=
 g(\widetilde C_A)-g(C_A)
-
\frac{M_1(B_A)}{S(B_A)}
+
\frac{M_1(A)}{S(A)}.
\tag{1}
\]

The two classical Mertens estimates needed below are

\[
S(X)=\log\log X+B_1+O\!\left(\frac1{\log X}\right)
\tag{2}
\]

and

\[
M_1(X)=\log X+O(1).
\tag{3}
\]

Because \(B_A=A^\theta+O(1)\),

\[
L_B=\theta L_A+o(1),
\qquad
H_B=H_A+\log\theta+o(1).
\tag{4}
\]

Equations (2)–(4) imply

\[
\frac{M_1(A)}{S(A)}
=
\frac{L_A+O(1)}{H_A+B_1+O(L_A^{-1})},
\]

while

\[
\frac{M_1(B_A)}{S(B_A)}
=
\frac{\theta L_A+o(L_A)}{H_A+\log\theta+B_1+o(1)}.
\]

Therefore

\[
\frac{H_A}{L_A}
\left(
\frac{M_1(A)}{S(A)}-
\frac{M_1(B_A)}{S(B_A)}
\right)
\longrightarrow 1-\theta.
\tag{5}
\]

It remains to show that the co-tuned multiplier contributes only a negligible amount at this scale. From the AF-527 choice of \(d_A\),

\[
\frac{\widetilde C_A}{C_A}
=
1+O(H_A^{-1}),
\tag{6}
\]

where nearest-integer rounding is exponentially smaller than \(H_A^{-1}\) because \(c_A\asymp e^{\sqrt{H_A}}\). Also

\[
g(C)=\log C+O\!\left(\frac{\log C}{C}\right),
\]

so (6) yields

\[
g(\widetilde C_A)-g(C_A)=O(H_A^{-1}).
\tag{7}
\]

After multiplication by \(H_A/L_A\), the term in (7) is \(O(L_A^{-1})\to0\). Combining (1), (5), and (7) proves the claim.

## Fidelity / representation audit

AF-527 exhibits an amplitude collision: after co-tuning the tail multiplier, the normalized scalar carrier comparison loses the distinction between anchors \(A\) and \(A^\theta\) to every fixed algebraic order in \(1/\log\log A\). The present result shows that this collision is representation-dependent rather than an exact identification of the two carrier families.

The extra observable is relational and infinitesimal: instead of retaining only the scalar value of each carrier, retain the logarithmic slope of their exact ratio at the boundary. The derivative exposes the first logarithmic prime moment \(M_1/S\), whose leading scale is \(\log X/\log\log X\). The multiplier co-tuning acts only at order \(1/H_A\), so it cannot erase the \((1-\theta)L_A/H_A\) cross-anchor shape separation.

This gives a concrete example of a general Arithmetic Fidelity mechanism: a scalar asymptotic compression may destroy provenance to arbitrarily high perturbative order while a low-dimensional relational lift restores a coarse source parameter.

## Boundaries

1. **Exact carrier ratio, not curvature-defect ratio.** The theorem concerns \(R_A\), the ratio of the exact AF-527 carriers. AF-527 controlled values of the corresponding normalized curvature defects but did not provide derivative bounds strong enough to transfer (1) to the derivative of the curvature-defect ratio. Such a transfer requires a separate theorem.

2. **Anchor exponent, not rational-prime identity.** The recovered parameter is the power-separation exponent \(\theta\). The leading asymptotic uses only classical prime-density/Mertens moments and may be reproducible by matched generalized-prime systems. This result therefore does not establish a rational-prime discriminator.

3. **No stability claim at finite resolution.** On the physical boundary layer \(0<t\le A^{-1}\), a derivative of size \(L_A/H_A\) produces only an order \(L_A/(A H_A)\) change across the window. Exact infinitesimal recoverability is therefore compatible with severe conditioning or practical invisibility under finite-resolution observation.

4. **Not a minimal-lift theorem.** AF-527 proves collision to every fixed algebraic order in one scalar amplitude hierarchy; it does not prove that the exact zero-jet contains literally no beyond-all-orders anchor information. The present theorem supplies a sufficient one-derivative lift, not an unconditional minimal one.

5. **Specific co-tuning regime.** The negligibility of the multiplier derivative uses the AF-527 scale \(C_A,\widetilde C_A\asymp e^{\sqrt{H_A}}\) and the resulting relative mismatch \(O(H_A^{-1})\). More aggressive multiplier families could alter the balance and require a separate audit.

6. **Boundary regularity comes from cancellation.** Each individual carrier contains \(P(1+t)^{-1}\), which is singularly normalized as \(t\downarrow0\). The ratio \(R_A\) is regular at \(0\) only because this common factor cancels exactly before differentiation.

7. **Relation to AF-521.** AF-521 already shows that inward transport can promote a first logarithmic moment into leading curvature. The new point here is different: an outward-control family engineered in AF-527 to defeat the scalar amplitude hierarchy is separated by the logarithmic shape derivative of a cross-control carrier ratio.

## Prior-art / source audit

The number-theoretic input is classical. Mertens' prime estimates include

\[
\sum_{p\le x}\frac{\log p}{p}=\log x+O(1),
\qquad
\sum_{p\le x}\frac1p=\log\log x+O(1),
\]

with the refined constant/error form of the second estimate used exactly as in AF-527. A convenient modern exposition is Terence Tao, *Mertens' theorems* (2013), https://terrytao.wordpress.com/2013/12/11/mertens-theorems/ .

No novelty is claimed for those asymptotics, for differentiation of finite Dirichlet sums, or for recovering a scale parameter from a logarithmic derivative. The durable contribution recorded here is the exact specialization to the AF-527 co-tuned control family: the zeroth-order amplitude hierarchy is perturbatively blind while the first logarithmic shape observable has a nonzero normalized limit \(1-\theta\). This is retained as a Mathia representation/fidelity result, not as a new theorem in prime-number theory.

## Consequence

For this control family, "indistinguishable to all algebraic orders" is not stable under a change from scalar amplitude to first-order relational shape. Any future no-go statement based on AF-527 must therefore specify the observation class: amplitude-only algebraic asymptotics are insufficient, whereas a one-derivative exact-carrier lift already recovers the coarse anchor scale. Conversely, any practical recovery claim must separately prove conditioning on a non-infinitesimal observation window.