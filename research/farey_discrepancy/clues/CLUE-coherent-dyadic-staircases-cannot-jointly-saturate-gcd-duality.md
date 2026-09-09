---
id: CLUE-coherent-dyadic-staircases-cannot-jointly-saturate-gcd-duality
type: research-clue
status: accepted
origin: master-researcher
target_line: farey_discrepancy
based_on:
  - research/farey_discrepancy/findings/FD-003-franel-mertens-gcd-energy-has-an-asymptotically-sharp-scalar-dual-bound.md
  - research/farey_discrepancy/clues/CLUE-joint-squarefree-sign-and-divisor-compatibility.md
  - research/farey_discrepancy/mind/RESEARCH_LINES.md
---

# Audit a two-horizon gap: one staircase cannot saturate the GCD coordinate bound at both N and 2N

## Observation

The existing saturation results optimize one horizon at a time. In particular, the resolved joint squarefree-sign/divisor clue records feasible near-extremizers depending on the chosen horizon. This does not imply that two such optimizers can be restrictions of the same underlying cumulative sequence. The proposed test adds no Jordan moments and does not reconstruct the entire Mobius source: it retains just the exact compatibility between two horizons.

Let A be any real sequence on the positive integers; no multiplicativity or sign assumption is needed. At each integer horizon H define

\[
m^{(H)}_d=A(\lfloor H/d\rfloor),\qquad
E_H=(m^{(H)})^T K_Hm^{(H)},\qquad
R_H=\frac{A(H)^2}{E_H},
\]

with the unchanged FD-003 matrix K_H(d,e)=gcd(d,e)^2/(de). Set R_H=0 if the vector is zero. The physical choice is A(k)=M(k). Two horizon vectors made from the same A satisfy exactly

\[
m^{(2N)}_2=A(N)=m^{(N)}_1,
\qquad
m^{(2N)}_4=A(\lfloor N/2\rfloor)=m^{(N)}_2.
\tag{1}
\]

These relations couple the first, second and fourth coordinates. The unrestricted FD-003 extremizer has a negative second coordinate but an exactly zero fourth coordinate. Consequently the near-extremizer patterns at N and 2N appear incompatible.

## Research question

Independently audit the following proposed elementary lemma, including its finite constants:

\[
\boxed{
\min(R_N,R_{2N})<\kappa
:=\left(\frac1{\zeta(2)}+\frac1{100\zeta(2)^2}\right)^{-1}
<\zeta(2),\qquad N\ge101.
}
\tag{2}
\]

Numerically kappa is approximately 1.6349944922, compared with zeta(2) approximately 1.6449340668. The constant is deliberately conservative and is not an optimization target. The new object is a joint bound on coherent horizon vectors, not a smaller one-horizon unrestricted constant.

If (2) survives review, determine whether it yields a useful paired-horizon or block-averaged Franel estimate, rather than only a bounded improvement of a scalar constant. Do not infer an improved Mertens exponent from the gap alone.

## Why it may matter

FD-003 explains why a single positive GCD matrix has no free scalar gain. The sign/moment relaxation results show that increasingly realistic constraints at one horizon can still approach that matrix optimum. Equation (1) tests a different restriction: the same arithmetic prefix must feed several horizons consistently. It distinguishes independent worst cases from a source-coherent family.

This is not a contradiction to single-horizon sharpness. A near-extremizer at N may remain feasible while forcing the ratio at 2N away from sharpness. Even a proven two-horizon gap permits alternating good/bad dyadic scales and gives no bound on the size of E_H itself. It is a modest structural result to test before investing in a larger multiscale program.

## Decisive test

The following derivation is supplied for adversarial verification, not as an accepted finding. Write Z=zeta(2), u^{(H)}=K_H^{-1}e_1, C_H=u^{(H)}_1 and v^{(H)}=u^{(H)}/C_H. FD-003 gives C_H<=Z and Z-C_H<=Z/H. Its inverse factorization gives, for 1<=d<=H,

\[
u^{(H)}_d
=d\sum_{\substack{k\le H\\d\mid k}}
\frac{\mu(k/d)\mu(k)}{J_2(k)},
\qquad
(K_H^{-1})_{dd}
=d^2\sum_{\substack{k\le H\\d\mid k}}
\frac{\mu(k/d)^2}{J_2(k)}\le Z^2.
\tag{3}
\]

The diagonal bound uses J_2(k)>=k^2/Z and the convergent sum over k=d*l. In particular u_4^{(H)}=0: every relevant k is divisible by 4, so mu(k)=0. Also

\[
u^{(H)}_2\longrightarrow-\frac Z2,
\qquad
\left|u^{(H)}_2+\frac Z2\right|\le\frac{2Z}{H}.
\tag{4}
\]

For the limit, write k=2l: only odd squarefree l survive, and the Euler sum over odd l is (3/4)Z, with the prefactor -2/3. The tail estimate follows from J_2(k)>=k^2/Z. Together with the bound on C_H, this gives

\[
v^{(H)}_4=0,
\qquad
\left|v^{(H)}_2+\frac12\right|
\le\frac{5}{2(H-1)}\le\frac1{40}
\quad(H\ge101).
\tag{5}
\]

For any nonzero vector m with t=m_1 and R=t^2/(m^TK_Hm)>0, orthogonal projection onto the equality ray gives the exact identity

\[
\frac{\|m-t v^{(H)}\|_{K_H}^2}{t^2}
=\frac1R-\frac1{C_H}.
\tag{6}
\]

Crucially, coordinate evaluation is bounded by the square root of the inverse diagonal in (3), NOT by the unit diagonal of K_H. Thus

\[
\left|\frac{m_d}{t}-v^{(H)}_d\right|
\le Z\sqrt{\frac1R-\frac1{C_H}}.
\tag{7}
\]

If R>=kappa, the right side is at most 1/10 by C_H<=Z and the definition of kappa. Suppose both ratios in (2) were at least kappa, and put t=A(N), T=A(2N), s=A(floor(N/2)); then t,T are nonzero. Equations (1), (5) and (7) imply

\[
|s/t|\ge3/8,\qquad |t/T|\ge3/8,
\qquad |s/T|\le1/10.
\]

But |s/T|=|s/t|*|t/T|>=9/64>1/10, a contradiction. This is the entire candidate proof of (2). It handles either sign of the endpoint values; if either endpoint is zero, its ratio is already zero.

First check the inverse orientation, the Euler factor in (4), the evaluation norm in (7), and all zero/normalization cases independently. Then express the surviving result in the exact physical normalization E_H=12(M_H*Franel_H+1/12) from FD-003. Derive only the paired-scale consequence that actually follows. In particular, do not turn a bound on min(R_N,R_2N) into a bound on either ratio separately or silently iterate it as a multiplicative contraction.

A further experiment may use a finite dyadic chain built from ONE increment prefix and ask whether the compatible ratio pattern can alternate near-saturation indefinitely. Specify that optimization before examining the true Mobius data. A failure of this stronger extension does not negate (2), and no such chain estimate is claimed here.

## Evidence boundary

Reviewed source snapshot: 1419fd4a827311a17696b125fd885fe0b8e2f312. Publication preflight compared it with 511def5cc3cd50198dddfc8898de3a5abd9d93c1; the intervening changes did not touch these lines. The deduplication read the current line questions, its single-horizon sign/divisor disposition and the ordered-gap clue. Repository code search failed, so no exhaustive corpus-wide absence claim is made. The owner should compare this two-horizon object with the full current local corpus before promotion.

Local sanity checks used exact rational inverse-column/diagonal formulas at H=8,16,32,64,101,128. Every fourth coordinate was exactly zero; double-precision multiplication K_H*u-e_1 had maximum residual below 2.3e-16. These checks support the algebra but do not replace the proof above or independent review. No repository test suite, Lean build, actual-prefix optimization, or asymptotic experiment was executed.

The factorization and equality-case geometry are classical tools already in FD-003; literature novelty is not claimed. No new RH bound follows from the displayed constant alone. If the two-horizon lemma is already covered locally, close as duplicate; if it is false, record the exact failed identity or a coherent counterexample. If it survives but has no useful transport beyond a constant, retain that limited boundary and do not open another standalone line.

## Research disposition

Accepted. The two-horizon lemma survives independent reconstruction and is canonicalized in [[research/farey_discrepancy/findings/FD-014-coherent-dyadic-horizons-have-a-uniform-gcd-duality-saturation-gap.md]]. The same finding gives the legitimate repeated consequence: every adjacent dyadic pair has a uniform saturation deficit, and every even-length dyadic block has average normalized dual ratio strictly below `zeta(2)` by a fixed constant. This is additive block control, not a multiplicative contraction and not an RH-exponent improvement.

The remaining live question is whether a **compressed growing hierarchy of coherent horizons** can turn this genuine source-coherence gap into a scale-sensitive Franel/Mertens estimate before the hierarchy becomes complete enough to hit the exact source-reconstruction boundary of `FD-009`. Optimizing the finite constant in the present two-horizon lemma is secondary unless it exposes such a transport mechanism.
