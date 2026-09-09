---
type: partial-positive
research_line: xi_flow
finding_id: XF-152
status: canonical
---

# XF-152 — initial off-circle maximal-contact trace has an exact one-sided visibility threshold

## Statement

For the maximal-contact matched pair used in XF-145–XF-151, the initial complexified physical trace admits an exact magnitude law. Writing

\[
\Delta R(z,0)=R_1(z,0)-R_{\lambda_\rho}(z,0),
\]

one has, up to a unit phase/sign,

\[
\Delta R(z,0)
=
2(1-\lambda_\rho)e^{-iN\pi z/L}
\sin^{N-2}\!\left(\frac{\pi z}{L}\right).
\]

Hence for an outward complex displacement \(z=x+ih\), with

\[
H=\frac{\pi h}{L},\qquad b=\frac{\pi x}{L},
\]

\[
\frac{|\Delta R(x+ih,0)|}{2(1-\lambda_\rho)}
=
e^{NH}
\left(\sinh^2H+\sin^2b\right)^{(N-2)/2}.
\]

Near the antipodal point write \(x=L/2-d\) and \(D=\pi d/L\). Then

\[
\mathcal A_N(H,D)
:=
\frac{|\Delta R(L/2-d+ih,0)|}{2(1-\lambda_\rho)}
=
e^{NH}
\left(\cos^2D+\sinh^2H\right)^{(N-2)/2}.
\]

The exponential rate is

\[
F_+(H,D)
=
H+\frac12\log\!\left(\cos^2D+\sinh^2H\right).
\]

For every \(D>0\), \(F_+(\cdot,D)\) is strictly increasing and has a unique positive zero

\[
\boxed{
H_*(D)
=
\frac12\log\!\left(
\sqrt{3+\cos^2(2D)}-\cos(2D)
\right).
}
\]

Thus this matched pair has an exact one-sided complex visibility threshold at the initial slice. Below \(H_*(D)\), its normalized separation is exponentially small in \(N\); above \(H_*(D)\), it is exponentially large. At the real center \(D=\pi/2\),

\[
H_*\!\left(\frac\pi2\right)=\frac12\log3,
\qquad
h_* = \frac{L}{2\pi}\log3.
\]

Near the antipodal point,

\[
H_*(D)
=
\frac{D^2}{2}-\frac{D^4}{24}+O(D^6),
\]

so in physical coordinates

\[
\boxed{
h_*(d)
=
\frac{\pi}{2}\frac{d^2}{L}
-
\frac{\pi^3}{24}\frac{d^4}{L^3}
+
O\!\left(\frac{d^6}{L^5}\right).
}
\]

In particular the parabolic reach scale from XF-151 is sharp for the initial outward trace, with leading constant \(\pi/2\).

The direction is essential. For an inward displacement \(z=x-ih\), the rate is

\[
F_-(H,D)
=
-H+\frac12\log\!\left(\cos^2D+\sinh^2H\right),
\]

and there is no positive finite solution of \(F_-(H,D)=0\) for \(D>0\). At the antipodal point itself,

\[
F_-(H,0)=-H+\log\cosh H<0
\]

for every finite \(H>0\). Therefore inward complex continuation never produces order-one exponential-rate separation for this initial matched pair.

## Derivation

The exact initial-slice formula is the complex continuation of the physical identity already underlying XF-145:

\[
|\Delta R(x,0)|
=
2(1-\lambda_\rho)
\left|\sin\frac{\pi x}{L}\right|^{N-2}.
\]

For \(z=x+ih\),

\[
|e^{-iN\pi z/L}|=e^{NH}
\]

and

\[
\left|\sin(b+iH)\right|^2
=
\sin^2b+\sinh^2H.
\]

This gives the exact magnitude law above. Since

\[
\partial_HF_+(H,D)
=
1+
\frac{\sinh H\cosh H}
{\cos^2D+\sinh^2H}>0,
\]

there can be at most one threshold. Setting \(F_+=0\), squaring after exponentiation, and writing \(y=e^{2H}\) gives

\[
y^2+2\cos(2D)y-3=0.
\]

The positive root is

\[
y_*(D)=\sqrt{3+\cos^2(2D)}-\cos(2D),
\]

which proves the formula for \(H_*\).

For inward continuation the threshold equation instead becomes

\[
3y^2-2\cos(2D)y-1=0.
\]

Its positive root is

\[
y=
\frac{\cos(2D)+\sqrt{\cos^2(2D)+3}}{3}
\le1,
\]

with equality only at \(D=0\). Hence no solution with \(H>0\) exists.

Finally, if \(D\to0\) and \(H=\alpha D^2\), then

\[
F_+(H,D)
=
\left(\alpha-\frac12\right)D^2+O(D^4).
\]

Consequently, whenever \(ND^2\to\infty\), the normalized initial separation is exponentially small for every fixed \(\alpha<1/2\) and exponentially large for every fixed \(\alpha>1/2\). This is the local form of the exact threshold.

## Consequences for the frontier

XF-151 established, from a uniform analytic-jet bound, that shallow off-circle access cannot beat the real antipodal obstruction until the complex reach is of parabolic size \(h\asymp d^2/L\). The present calculation shows that this scale is not merely an artifact of that upper bound: for the exact maximal-contact pair, the initial outward trace itself undergoes a sharp transition at

\[
h_*(d)\sim \frac\pi2\frac{d^2}{L}.
\]

This narrows the target-side gate. An off-circle observable confined below this outward depth remains exponentially blind to the transition offset for this initial witness. Once the depth exceeds the threshold, this particular initial-slice witness no longer certifies blindness; however, that does not establish stable recovery of \(\Lambda_{\rm per}\), nor does it show that the full heat history has the same threshold. The all-future optimization remains open.

The outward/inward asymmetry is also structural rather than a modulus artifact: it is produced by the carrier \(e^{-iN\pi z/L}\). Therefore a future complex-observation theorem must keep track of which radial side of the unit circle is sampled; merely recording \(|w|\ne1\) loses decisive information.

## Falsification boundary

This finding concerns the canonical maximal-contact matched pair and the initial slice \(s=0\). It does not prove that outward access at or above \(h_*(d)\) is sufficient for a polynomially conditioned decoder, and it does not exclude a smaller threshold when positive heat time is optimized jointly with complex displacement. It also remains a target-side obstruction: source realizability of the matched packet by the Xi flow is a separate question.

## Prior-art audit

The derivation is self-contained. Classical complex growth bounds for trigonometric/exponential polynomials are compatible with the frequency-times-height mechanism already noted in XF-151, but no external theorem is needed for the exact threshold: it follows from the closed-form maximal-contact packet and elementary algebra. No source entry is therefore required.

## Next gate

Optimize the exact maximal-contact separation over \(s\ge0\) near the outward critical layer \(H\sim D^2/2\). The decisive question is whether positive heat time can lower the \(\pi/2\) physical reach constant, or whether the initial-slice threshold remains the sharp all-future boundary. In parallel, the source-side alternative remains to prove that Xi cannot realize the maximal-contact matched direction.