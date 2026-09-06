# ANF-064 — validated finite moments complete sharp Montgomery--Taylor radial coercivity

**Status:** `COMPUTER-ASSISTED + EXACT-DERIVED + ALL-ORDER-MOMENT-BOUND + SHARP-COERCIVITY + STRICT-RADIAL-MONOTONICITY + STRUCTURAL-STRENGTHENING`. `ANF-062` proves positivity of the fixed Montgomery--Taylor five-point defect by a direct interval cover. `ANF-063` then proves analytically that the sufficient moment inequality proposed in `CLUE-even-moment-radial-coercivity` holds for every order `n>=9` and every horizontal frequency. A validated Arb/FLINT certificate returned through `CLUE-montgomery-taylor-near-extremizer-rigidity` closes the seven remaining orders `n=2,...,8` on the full real frequency line. Combining those two inputs with the exact height-power expansion gives a stronger theorem than five-point zero-freeness:

\[
\boxed{
H_{\rm MT}(y_1,y_2;t_1,t_2)
\ge
2\pi^2m_5(J_{\rm MT})(y_1^2+y_2^2)
\qquad(y_1,y_2>0),
}
\tag{1}
\]

and the constant is sharp as an infimum. Moreover, along every fixed genuine shape, the normalized defect is strictly increasing under simultaneous height dilation.

The finite certificate also supplies a uniform fourth-order remainder. With

\[
S:=y_1^2+y_2^2,
\qquad
\varepsilon:=0.00082277,
\tag{2}
\]

one has

\[
\boxed{
H_{\rm MT}
\ge
2\pi^2m_5(J_{\rm MT})S
+2\pi^4\varepsilon S^2.
}
\tag{3}
\]

The value `epsilon` is certified enclosure slack for the order-two moment inequality; it is not asserted to be the optimal quartic constant.

## 1. The all-order moment inequality is now closed

For

\[
M_n(t):=\int_{-1}^{1}\alpha^{2n}J_{\rm MT}(\alpha)
\cos(2\pi\alpha t)\,d\alpha,
\qquad n\ge2,
\tag{4}
\]

put

\[
c_n:=2^{2n-1},
\qquad
a_n:=\frac{c_n}{1+c_n}.
\tag{5}
\]

The required inequality is

\[
\boxed{
P_n(t):=M_n(t)+a_nM_n(0)>0
\qquad(n\ge2,\ t\in\mathbb R).
}
\tag{6}
\]

For every `n>=9`, this is the analytic all-frequency conclusion of `ANF-063`. The only residual orders were `n=2,...,8`.

The independent finite certificate reported through the local compute-return clue evaluates the exact Montgomery--Taylor profile with Arb/FLINT interval arithmetic. For those seven orders it combines interval enclosures of the derivatives of the exact transform `G(t)^2`, the analytic Lipschitz control

\[
\left|\left(\frac{M_n}{M_n(0)}\right)'(t)\right|\le2\pi,
\tag{7}
\]

and twice-integrated analytic Fourier tails. The compact frequency cutoffs for `n=2,...,8` are respectively

\[
4,5,6,7,8,9,10.
\tag{8}
\]

The rational compact cover inspected `601` cells, produced `304` positive leaves, and left `0` unresolved cells. Successful leaves used 128-bit arithmetic; undecided parents were reevaluated at 256 and 512 bits before subdivision. Thus (6) is certified for each of the seven finite orders on its compact interval and the analytic tails complete the whole real line. No order `n>=9` is imported from that computation; those orders remain covered analytically by `ANF-063`.

For `n=2`, the same certificate gives the stronger uniform margin

\[
\boxed{P_2(t)>\varepsilon=0.00082277\qquad(t\in\mathbb R).}
\tag{9}
\]

Ordinary floating-point sampling is not evidence for (6) or (9); the durable input is the outward-rounded certificate described above.

## 2. Every higher height coefficient is positive

Scale the two heights by

\[
y_j=\lambda f_j,
\qquad f_1,f_2>0,
\tag{10}
\]

and put

\[
A_n:=f_1^{2n}+f_2^{2n},
\qquad
B_n:=(f_1+f_2)^{2n}+(f_1-f_2)^{2n},
\qquad d:=t_1-t_2.
\tag{11}
\]

Expanding the exact `ANF-045` defect in even powers of `lambda` gives, for `n>=1`, the coefficient

\[
\frac{(2\pi)^{2n}}{(2n)!}
\Bigl[
 c_nA_nM_n(0)
 +f_1^{2n}M_n(t_1)
 +f_2^{2n}M_n(t_2)
 +B_nM_n(d)
\Bigr],
\tag{12}
\]

where for `n=1` the notation `c_1=2` and `M_1=K_{\rm MT}` is used.

For `n>=2`, substitute

\[
M_n(t)=-a_nM_n(0)+P_n(t).
\tag{13}
\]

The bracket in (12) becomes exactly

\[
\boxed{
a_n\bigl(c_nA_n-B_n\bigr)M_n(0)
+f_1^{2n}P_n(t_1)
+f_2^{2n}P_n(t_2)
+B_nP_n(d).}
\tag{14}
\]

The elementary even-power inequality

\[
B_n\le c_nA_n
\tag{15}
\]

makes the first term nonnegative. Equation (6) makes all three remaining terms positive, and `f_1,f_2>0`. Hence **every coefficient of order `lambda^(2n)`, `n>=2`, is strictly positive** for a genuine two-pair geometry.

Compact support of `J_MT` makes the hyperbolic-cosine expansion entire in the finite height variables, so no formal interchange issue is hidden in this coefficient argument.

## 3. The quadratic coefficient gives the sharp floor

Write

\[
K(t):=M_1(t),
\qquad
k_*:=\inf_{t\in\mathbb R}K(t),
\qquad
m_5:=2K(0)+3k_*.
\tag{16}
\]

At `n=1`, one has `B_1=2A_1`. Bounding each horizontal curvature term below by `k_*` therefore gives

\[
\begin{aligned}
&2A_1K(0)+f_1^2K(t_1)+f_2^2K(t_2)+B_1K(d)\\
&\qquad\ge A_1\bigl(2K(0)+3k_*\bigr)
=m_5A_1.
\end{aligned}
\tag{17}
\]

After multiplication by `(2pi)^2/2!`, the quadratic coefficient is at least

\[
2\pi^2m_5(f_1^2+f_2^2).
\tag{18}
\]

All higher coefficients are positive by Section 2. Setting `lambda=1` proves (1). Equivalently, for any fixed positive shape `(f_1,f_2;t_1,t_2)`,

\[
\boxed{
\lambda\longmapsto
\frac{H_{\rm MT}(\lambda f_1,\lambda f_2;t_1,t_2)}{\lambda^2}
\text{ is strictly increasing on }(0,\infty).
}
\tag{19}
\]

The constant in (1) is sharp as an infimum. Let one pair disappear, take the surviving horizontal position and the relative separation to the same minimizer of `K`, and then send the common height scale to zero. More explicitly, take `f_2/f_1->0`, `t_2->0`, and `t_1=d->tau` along a sequence with `K(tau)->k_*`; then let `lambda->0`. The normalized defect tends

\[
2\pi^2\bigl(2K(0)+3k_*\bigr)=2\pi^2m_5.
\tag{20}
\]

Thus the sharp value lives on the degenerate zero-height, one-pair boundary; (19) rules out attainment at a genuine positive height.

## 4. The order-two margin gives a uniform quartic remainder

For `n=2`, equation (14) and (9) imply that the order-four bracket is larger than

\[
\varepsilon(A_2+B_2).
\tag{21}
\]

Writing `S_f=f_1^2+f_2^2`, direct expansion gives

\[
A_2+B_2
=3S_f^2+6f_1^2f_2^2
\ge3S_f^2.
\tag{22}
\]

Since

\[
\frac{(2\pi)^4}{4!}=\frac{2\pi^4}{3},
\tag{23}
\]

the fourth-order contribution is at least

\[
2\pi^4\varepsilon\lambda^4S_f^2.
\tag{24}
\]

Combining this with the quadratic floor and the nonnegative higher terms yields

\[
H_{\rm MT}(\lambda f_1,\lambda f_2;t_1,t_2)
\ge
2\pi^2m_5\lambda^2S_f
+2\pi^4\varepsilon\lambda^4S_f^2,
\tag{25}
\]

which is (3) after restoring `y_j=lambda f_j`.

This remainder is useful for stability questions because any sequence approaching the sharp normalized floor must force the total height scale to zero. It does not by itself classify the horizontal geometry of such near-minimizers; that requires retaining the linkage between the three curvature arguments rather than bounding them independently.

## 5. Stress tests and evidence boundary

The theorem uses two different evidence modes and keeps them separate. Orders `n>=9` are exact analytic consequences of the endpoint anti-concentration proof in `ANF-063`. Orders `n=2,...,8` are computer-assisted statements backed by outward-rounded Arb/FLINT enclosures over compact frequency intervals plus analytic tails. Replacing the latter by dense floating-point samples would lower the evidence tier and would not support (1).

The coefficient inequality (15) is sufficient rather than necessary. A failure of the moment bound for some other spectral profile would not imply a negative five-point defect, because (14) deliberately discards linkage between `t_1`, `t_2`, and `d`. For the fixed Montgomery--Taylor profile, however, the all-order bound has now been certified, so the sufficient route is complete.

A targeted prior-art check found the classical Montgomery--Taylor extremal framework and general positive-definite/bandlimited Fourier machinery but no source establishing the profile-specific all-order bound (6), the sharp five-point floor (1), or the radial monotonicity (19). No external theorem is load-bearing here and no novelty claim is made; `SOURCES.md` therefore remains unchanged.

This result concerns the fixed Montgomery--Taylor **five-point** two-pair defect. It does not prove the universal affine counting inequality for larger conjugation-invariant multisets, does not export the moment criterion to an arbitrary spectrum, and does not imply RH.

## 6. Consequence for the research line

`CLUE-even-moment-radial-coercivity` is resolved positively. The direct sign certificate of `ANF-062` now has a sharp structural explanation: finite positive height can only increase the normalized defect above the boundary curvature floor, and it does so with a certified quartic gap. The remaining local five-point question is no longer positivity or radial coercivity, but the finer rigidity of sequences approaching the sharp boundary value: which horizontal curvature minima can be simultaneously compatible as one pair and the total height scale disappear.