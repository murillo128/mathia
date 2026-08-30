# PF-114 — shift-clone pant waves telescope but the seam relative mode does not

**Status:** `EXACT-DERIVED + LITERATURE + NEGATIVE/BOUNDARY`. The hyperbolic pentagon identities used below are classical. The project-specific result is that the exact all-composite shift clone `p_n -> p_n+1` has a sharp split already inside each one-cusp tight pair of pants: the two returning simple orthogeodesics (“waves”) have **summable logarithmic distortion**, while the simple seam joining the two finite cuffs has a relative logarithmic defect of order `1/p_n` and is therefore not summable. No global quasiconformal, relative-resolvent, Schatten, scattering, or RH conclusion is claimed.

## Claim

Put

\[
F(x)=\log\cot\frac{\pi}{x},
\qquad
f(x)=F'(x)=\frac{2\pi}{x^2\sin(2\pi/x)},
\qquad x>2.
\tag{1}
\]

For consecutive primes define

\[
h_n=F(p_{n+1})-F(p_n)
=\int_{p_n}^{p_{n+1}}f(t)\,dt,
\tag{2}
\]

and for the shift clone

\[
h_n^+=F(p_{n+1}+1)-F(p_n+1)
=\int_{p_n}^{p_{n+1}}f(t+1)\,dt.
\tag{3}
\]

Let

\[
R_n:=\frac{h_n^+}{h_n},
\qquad
\delta_n:=\log R_n.
\tag{4}
\]

Then, after a finite initial segment,

\[
\boxed{
0<R_n<R_{n+1}<1,
\qquad
\delta_n\nearrow0,
\qquad
\sum_{n\ge N}|\delta_{n+1}-\delta_n|=-\delta_N<\infty.
}
\tag{5}
\]

Now let `P_n` be the one-cusp tight pair of pants whose finite cuffs are `ell_n, ell_{n+1}`. By PF-032 its standard collar half-widths are

\[
A_n=\frac{h_n}{2},
\qquad
B_n=\frac{h_{n+1}}2,
\tag{6}
\]

and the simple orthogeodesic seam joining those cuffs has exact length

\[
S_n=A_n+B_n.
\tag{7}
\]

Let `Y_{A,n}` be the returning simple orthogeodesic based on the cuff with collar width `A_n`, and `Y_{B,n}` the analogous wave based on the other finite cuff. Then

\[
\boxed{
\cosh\frac{Y_{A,n}}2
=
\frac{\sinh(A_n+B_n)}{\sinh B_n},
\qquad
\cosh\frac{Y_{B,n}}2
=
\frac{\sinh(A_n+B_n)}{\sinh A_n}.
}
\tag{8}
\]

For the matched waves in the shift clone,

\[
\boxed{
\sum_n
\left|\log\frac{Y_{A,n}^+}{Y_{A,n}}\right|<\infty,
\qquad
\sum_n
\left|\log\frac{Y_{B,n}^+}{Y_{B,n}}\right|<\infty.
}
\tag{9}
\]

The seam behaves differently. PF-107 gives `delta_n=-1/p_n+o(1/p_n)`, and (7) implies

\[
\boxed{
\log\frac{S_n^+}{S_n}
=-\frac1{p_n}+o(p_n^{-1}).
}
\tag{10}
\]

Hence Euler's divergence of the reciprocal-prime sum gives

\[
\boxed{
\sum_n\left|\log\frac{S_n^+}{S_n}\right|=\infty,
}
\tag{11}
\]

although PF-108 proves the **additive** seam defect is summable:

\[
\sum_n|S_n^+-S_n|<\infty.
\tag{12}
\]

Thus the marked simple-arc geometry already separates into a summable differential mode (the two waves) and a nonsummable common-scale mode (the seam).

## 1. The shift factor has finite total variation

Write

\[
f(x)=\frac1x\frac{z}{\sin z},
\qquad z=\frac{2\pi}{x}.
\tag{13}
\]

For `x>2`, Euler's sine product gives the absolutely convergent expansion

\[
\log f(x)
=-\log x
+\sum_{k\ge1}\frac{4^k\zeta(2k)}{k}x^{-2k}.
\tag{14}
\]

Every term on the right has positive second derivative, so

\[
G(x):=\log f(x)
\]

is strictly convex. Therefore

\[
\rho(x):=\frac{f(x+1)}{f(x)}
\tag{15}
\]

is strictly increasing, because

\[
(\log\rho)'(x)=G'(x+1)-G'(x)>0.
\]

Also `rho(x)<1` and `rho(x)->1`. Equation (3) can be rewritten as the weighted average

\[
R_n
=
\frac{\int_{p_n}^{p_{n+1}}f(t)\rho(t)\,dt}
     {\int_{p_n}^{p_{n+1}}f(t)\,dt}.
\tag{16}
\]

Monotonicity of `rho` gives

\[
\rho(p_n)<R_n<\rho(p_{n+1})<R_{n+1}<1.
\tag{17}
\]

This proves the first two statements in (5), and telescoping gives the finite total variation exactly:

\[
\sum_{n\ge N}|\delta_{n+1}-\delta_n|
=
\lim_{M\to\infty}(\delta_{M+1}-\delta_N)
=-\delta_N.
\tag{18}
\]

No prime-gap theorem is used in this monotonicity step.

## 2. Exact one-cusp pant arc formulas

The classification of simple essential proper arcs in a hyperbolic pair of pants is classical. For a pair of pants with one cusp and two geodesic boundaries there is one simple seam joining the two finite boundaries and one returning simple arc based on each finite boundary.

Liu--Papadopoulos--Su--Théret record the right-angled pentagon relation

\[
\cosh a=\sinh b\,\sinh c
\tag{19}
\]

and apply it explicitly to returning arcs in one-punctured pairs of pants. For the wave based on the `A_n` cuff, the relevant other finite boundary has length `ell_{n+1}` and the cross-cuff seam has length `S_n`. Therefore

\[
\cosh\frac{Y_{A,n}}2
=
\sinh\frac{\ell_{n+1}}2\,\sinh S_n.
\tag{20}
\]

The standard collar identity from PF-032 is

\[
\sinh\frac{\ell_{n+1}}2=\frac1{\sinh B_n},
\tag{21}
\]

while `S_n=A_n+B_n`. Substitution proves the first identity in (8); exchanging `A_n,B_n` proves the second.

These formulas are exact and remain valid in the highly unbalanced regimes produced by extreme neighboring prime-gap ratios.

## 3. Returning waves cancel the common scale

For `A,B>0`, define the wave `Y_A(A,B)` by

\[
\cosh\frac{Y_A}{2}=\frac{\sinh(A+B)}{\sinh B}.
\]

Set

\[
T(A,B):=\cosh\frac{Y_A}{2}-1.
\]

An exact rearrangement gives

\[
T(A,B)
=
\frac AB\,Q(A,B),
\tag{22}
\]

where

\[
Q(A,B)
=
\frac{2\sinh(A/2)}A
\frac{B}{\sinh B}
\cosh\!\left(B+\frac A2\right).
\tag{23}
\]

The function `Q` extends analytically to `(A,B)=(0,0)`, with `Q(0,0)=1` and vanishing linear part. Hence for all sufficiently small `A+B`,

\[
|\log Q(A,B)|\le C(A+B)^2.
\tag{24}
\]

The clone variables are

\[
A^+=e^{\delta_n}A,
\qquad
B^+=e^{\delta_{n+1}}B,
\tag{25}
\]

and `delta_j<0`, so `A^+<=A`, `B^+<=B`; the same quadratic bound applies to `Q(A^+,B^+)`.

Now define

\[
H(t)=\log\bigl(2\operatorname{arcosh}(1+t)\bigr).
\]

Its derivative with respect to `log t` is

\[
\frac{dH}{d\log t}
=
\frac{t}{\operatorname{arcosh}(1+t)\sqrt{t(t+2)}}.
\tag{26}
\]

Writing `t=cosh u-1`, the right side becomes

\[
\frac{\tanh(u/2)}u\le\frac12.
\tag{27}
\]

Thus `H` is globally `1/2`-Lipschitz in `log t`. Combining (22)--(27),

\[
\boxed{
\left|\log\frac{Y_{A,n}^+}{Y_{A,n}}\right|
\le
\frac12|\delta_n-\delta_{n+1}|
+C(A_n+B_n)^2.
}
\tag{28}
\]

The same estimate holds for `Y_{B,n}`.

The first term in (28) is summable by (18). For the second, the unconditional Baker--Harman--Pintz bound `g_n << p_n^0.525`, together with `f(x)<<1/x`, gives

\[
h_n\ll\frac{g_n}{p_n},
\qquad
h_n^2\ll g_n p_n^{-1.475}.
\tag{29}
\]

Because the prime intervals `[p_n,p_{n+1}]` partition the tail and `g_n=o(p_n)`, the final series is dominated by a constant multiple of

\[
\int^\infty x^{-1.475}\,dx<\infty.
\tag{30}
\]

Therefore

\[
\sum_n(A_n+B_n)^2<\infty,
\tag{31}
\]

and (28) proves (9).

The mechanism is worth isolating: the leading shift-clone scale `delta_n ~ -1/p_n` is common to two adjacent logarithmic spacings, while each returning wave depends at leading order on their **ratio**. The common mode cancels, leaving the finite-variation difference `delta_{n+1}-delta_n`.

## 4. The seam keeps the nonsummable common mode

From (7) and (25),

\[
\frac{S_n^+}{S_n}
=
\frac{e^{\delta_n}A_n+e^{\delta_{n+1}}B_n}{A_n+B_n}.
\tag{32}
\]

This ratio lies between `e^{delta_n}` and `e^{delta_{n+1}}`, so it tends to one. PF-107 gives

\[
\delta_n=-\frac1{p_n}+o(p_n^{-1}),
\tag{33}
\]

and the Baker--Harman--Pintz bound implies `p_{n+1}/p_n->1`. Hence both endpoints in that squeeze equal `-1/p_n+o(1/p_n)` after taking logarithms, proving (10).

Since the ratio is below one on the tail, there is no cancellation in absolute value. Euler's classical theorem

\[
\sum_p\frac1p=\infty
\]

then gives (11).

This does not contradict PF-108. The seam itself shrinks, and PF-108 proves that its **additive** change is in `ell^1`. What fails to be summable is the multiplicative/logarithmic scale change.

## 5. Consequence for the relative-operator clue

PF-111 rules out amplification by arbitrarily complicated **closed** words contained in a single matched pant: the supremum of their logarithmic length distortions is summable over the pants. PF-114 gives the complementary simple-arc audit.

Two natural pant-local channels are now sharply separated:

\[
\boxed{
\begin{array}{c|c}
\text{simple arc type} & \text{shift-clone logarithmic defect}\\
\hline
\text{returning wave on either cuff} & \ell^1\\
\text{cross-cuff seam} & \sim -1/p_n\notin\ell^1
\end{array}}
\tag{34}
\]

The seam therefore identifies the first local **relative** quantity in this comparison whose tail tends to zero but does not have summable logarithmic mass. This is not yet an operator obstruction: strong-equivalence/compactness theorems may require only uniform convergence to one, and PF-108 supplies stronger additive/area-weighted control in the shrinking seam regions. Conversely, a cross-pant trajectory or energy estimate is not allowed to assume an `ell^1` multiplicative seam budget that the geometry does not possess.

The surviving question is consequently more precise. Any global map/operator proof has to show that the nonsummable seam common mode is harmless because it lives on shrinking geometry or is absorbed by the correct metric/area weighting. Any counterexample has to amplify that mode through **gluing across pants, derivatives/energy, or another genuinely nonlocal mechanism**. Returning waves and pant-local closed words cannot provide such amplification.

## 6. Prior art and novelty audit

The right-angled pentagon formula, classification of essential simple arcs on pairs of pants, and the use of orthogeodesic arc lengths in Teichmüller theory are classical. Liu, Papadopoulos, Su and Théret give the exact pentagon relation and treat the one-puncture/two-boundary seam and returning-arc cases explicitly. Their global comparison theorem is stated on relative thick parts with boundary lengths bounded above and below; it does not cover the unbounded-cuff, collapsing-seam prime-flute tail and is not invoked here.

The Baker--Harman--Pintz exponent used only for the square-summability step is already source-audited in `SOURCES.md` and used elsewhere in this line.

Directed literature searches for the cotangent endpoint flute, the exact all-composite shift `p_n -> p_n+1`, monotonicity of the integrated shift factor (16), and this wave/seam summability split located no matching result. No novelty is claimed for the classical hyperbolic trigonometry, Euler sine product, convexity method, or reciprocal-prime divergence. The durable project contribution is the exact specialization

\[
\boxed{
\text{cotangent shift-clone}
\Rightarrow
\text{finite variation of adjacent log-spacing scale}
\Rightarrow
\text{summable wave distortion but nonsummable seam log distortion}.
}
\]

This is a **boundary result for the accepted relative-operator program**, not evidence for RH and not a general theorem about infinite-type surfaces.

## 7. Audit / falsification core

The reusable checks are:

1. differentiate `F(x)=log cot(pi/x)` and verify (1);
2. verify the Euler-product expansion (14) and strict convexity of `log f` for `x>2`;
3. rewrite `R_n` as the weighted average (16), proving the interlacing (17) and exact finite total variation (18);
4. verify PF-032's exact identities `w_n=h_n/2` and `S_n=(h_n+h_{n+1})/2`;
5. derive the one-cusp wave formula (8) from the right-angled pentagon identity and `sinh(ell/2)=1/sinh w`;
6. verify the factorization (22)--(23), the quadratic remainder (24), and the global `1/2` Lipschitz constant (27);
7. use the source-audited `g_n<<p_n^0.525` only to prove `sum h_n^2<infinity`;
8. independently verify PF-107's `delta_n=-1/p_n+o(1/p_n)` and squeeze (32) to obtain the nonsummable seam logarithmic defect;
9. do not promote either local statement to a global quasiconformal, resolvent, scattering, determinant, or spectral-equivalence theorem without a separate gluing/operator argument.

A refutation would need to break one of those explicit identities/inequalities or the already-audited prime-gap input. Failure of the broader operator-comparison program would not refute PF-114; it would identify the cross-pant/nonlocal mechanism this finding deliberately leaves open.

## References

- L. Liu, A. Papadopoulos, W. Su, G. Théret, *On length spectrum metrics and weak metrics on Teichmüller spaces of surfaces with boundary*, Ann. Acad. Sci. Fenn. Math. 35 (2010), 255--274, DOI `10.5186/aasfm.2010.3515`, especially the right-angled pentagon formula and Lemma 3.4 cases (iv)--(v).
- R. C. Baker, G. Harman, J. Pintz, *The Difference Between Consecutive Primes, II*, Proc. London Math. Soc. 83 (2001), 532--562, DOI `10.1112/S0024611501012690`.
- PF-032, PF-107, PF-108 and PF-111 in this research ledger.
