# PF-242 — hypercycle shear is exponentially local in Pöschl--Teller mode index

**Status:** `EXACT-DERIVED + JACOBI-MODE-LOCALITY + POSITIVE/ROUTE-NARROWING`. PF-239 reduces the unresolved sheared-corridor contribution to a high-high normalized Schur block, while PF-241 shows that the canonical tangential blowup is a uniformly elliptic long-strip family. A remaining concern is that the graph-straightening shear could mix widely separated tangential frequencies strongly enough that diagonal-corridor crossing decay becomes unusable.

For the **direct shear multiplier itself**, that concern is false in a much stronger sense than ordinary smoothness. In the exact Pöschl--Teller basis from PF-231, the hypercycle slope is an analytic function of the tridiagonal Jacobi operator `cos(theta)`. Its matrix is therefore exponentially localized in mode index. More precisely, if two Pöschl--Teller spectral windows are separated by `d` mode indices, the direct shear coupling between them is bounded by

\[
\boxed{
\|E_- M_b E_+\|
\le (1+\beta^2)\beta^d,
}
\]

where `beta=max(w_1,w_2)` is exactly PF-232's reciprocal-prime shear scale. On the canonical tail `beta_n=O(P_n^{-1})`, so a fixed separation in **scaled** tangential frequency corresponds to `d=Theta(s_n^{-1})` and the direct mode-jump amplitude is super-algebraically small.

This does **not** yet prove [[research/prime_flute/findings/PF-240-total-one-scaled-boundary-derivative-is-the-sharp-high-high-shear-trace-threshold|PF-240]]'s weighted high-high estimate for the full normalized Schur difference. The variable-width diagonal background, actual seam normalization, and nonlinear resolvent/Schur operations can mediate additional mode mixing. The result nevertheless removes a concrete failure mechanism: the PF-232 coefficient `b` itself cannot directly throw a high mode across a macroscopic scaled-frequency gap at merely `O(beta)` cost. Any obstruction to the smooth route must arise from near-diagonal high-frequency propagation or from failure to preserve this locality through the remaining operator operations.

## Claim

Let

\[
A=-\partial_\theta^2+\csc^2\theta
\]

be the PF-231 Friedrichs Pöschl--Teller operator on `L^2((0,pi),dtheta)`. Put

\[
\alpha=\frac{1+\sqrt5}{2},
\qquad
\alpha(\alpha-1)=1.
\]

Its normalized eigenfunctions may be chosen as

\[
\phi_m(\theta)
=c_m(\sin\theta)^\alpha C_m^{(\alpha)}(\cos\theta),
\qquad
A\phi_m=(m+\alpha)^2\phi_m,
\tag{1}
\]

where `C_m^(alpha)` is the Gegenbauer polynomial and `c_m` is the `L^2(dtheta)` normalization.

For `M>=0`, let

\[
E_{\le M}:=\operatorname{span}\{\phi_0,\ldots,\phi_M\},
\qquad
E_{\ge M+d}:=\overline{\operatorname{span}}
\{\phi_{M+d},\phi_{M+d+1},\ldots\},
\tag{2}
\]

and use the same symbols for the orthogonal projections.

For `w>=0`, define the exact hypercycle graph and its slope

\[
f_w(\theta)=\operatorname{arsinh}(w\sin\theta),
\qquad
h_w(\theta)=f_w'(\theta)
=\frac{w\cos\theta}{\sqrt{1+w^2\sin^2\theta}}.
\tag{3}
\]

Set

\[
q(w):=\frac{w}{\sqrt{1+w^2}}\in[0,1).
\tag{4}
\]

Then for every integer `d>=1` and every `M>=0`,

\[
\boxed{
\|E_{\le M}M_{h_w}E_{\ge M+d}\|
\le
\frac{q(w)^d}{1-q(w)^2}
=(1+w^2)q(w)^d.
}
\tag{5}
\]

The same bound holds with the two projections reversed.

For the exact PF-232 shear coefficient

\[
b(X,\theta)
=(1-X)h_{w_1}(\theta)-Xh_{w_2}(\theta),
\qquad 0\le X\le1,
\tag{6}
\]

put `beta=max(w_1,w_2)`. If `beta<1`, then uniformly in `X`, `M`, and `d>=1`,

\[
\boxed{
\|E_{\le M}M_{b(X,\cdot)}E_{\ge M+d}\|
\le (1+\beta^2)\beta^d
\le2\beta^d.
}
\tag{7}
\]

Again the reversed block satisfies the same estimate.

Equivalently, let

\[
K_s^{\rm rect}:=sA^{1/2},
\tag{8}
\]

whose eigenvalues are `s(m+alpha)`. For fixed `0<Z<Z+Delta`, define

\[
P_-:=\mathbf1_{[0,Z]}(K_s^{\rm rect}),
\qquad
P_+:=\mathbf1_{[Z+\Delta,\infty)}(K_s^{\rm rect}).
\tag{9}
\]

If

\[
d_s(Z,\Delta)
:=
\max\!\left(
1,
\left\lceil\frac{Z+\Delta}{s}-\alpha\right\rceil
-
\left\lfloor\frac Zs-\alpha\right\rfloor
\right),
\tag{10}
\]

then

\[
\boxed{
\|P_-M_bP_+\|
+\|P_+M_bP_-\|
\le 2(1+\beta^2)\beta^{d_s(Z,\Delta)}.
}
\tag{11}
\]

The harmless factor `2` in (11) is only the sum of the two directional norms. Since

\[
d_s(Z,\Delta)\ge \frac{\Delta}{s}-1,
\tag{12}
\]

a fixed positive scaled-frequency gap forces geometric suppression in `1/s`.

For the canonical PF-205/PF-232 prime-flute tail,

\[
\beta_n=O(P_n^{-1}),
\qquad
s_n\asymp\frac{g_n+g_{n+1}}{P_n},
\tag{13}
\]

and the positive even prime-gap floor gives `beta_n=O(s_n)`. Therefore, for every fixed `Delta>0` and every `N>0`,

\[
\boxed{
\beta_n^{d_{s_n}(Z,\Delta)}=o(s_n^N).
}
\tag{14}
\]

Thus direct hypercycle-shear coupling across any fixed gap in the PF-231 scaled tangential spectrum is super-algebraically small.

## 1. The Pöschl--Teller basis turns `cos(theta)` into a Jacobi matrix

With `x=cos(theta)`, equation (1) identifies the PF-231 eigenbasis with the orthonormal Gegenbauer basis for the weight

\[
(1-x^2)^{\alpha-1/2}dx.
\]

The standard three-term Gegenbauer recurrence implies that multiplication by `x` is tridiagonal in this basis. Denote that self-adjoint contraction by

\[
J:=M_{\cos\theta},
\qquad \|J\|\le1.
\tag{15}
\]

Consequently every polynomial in `J` of degree `r` has matrix bandwidth at most `r` in the index `m`. In particular,

\[
E_{\le M}J^rE_{\ge M+d}=0
\qquad (r<d).
\tag{16}
\]

This is the only orthogonal-polynomial input needed below.

## 2. The exact hypercycle slope is an analytic Jacobi multiplier

Writing `x=cos(theta)` in (3),

\[
\begin{aligned}
h_w
&=\frac{wx}{\sqrt{1+w^2(1-x^2)}}\\
&=\frac{w}{\sqrt{1+w^2}}\,
 x\left(1-\frac{w^2}{1+w^2}x^2\right)^{-1/2}\\
&=q\,x(1-q^2x^2)^{-1/2}.
\end{aligned}
\tag{17}
\]

For `q<1`, the binomial series converges uniformly on `[-1,1]` and hence in operator norm after substituting `J`:

\[
\boxed{
M_{h_w}
=\sum_{k=0}^{\infty}c_kq^{2k+1}J^{2k+1},
\qquad
c_k=\frac1{4^k}\binom{2k}{k}\le1.
}
\tag{18}
\]

For a fixed index separation `d`, all terms with `2k+1<d` vanish between the projections in (5) by (16). Therefore

\[
\begin{aligned}
\|E_{\le M}M_{h_w}E_{\ge M+d}\|
&\le
\sum_{2k+1\ge d}c_kq^{2k+1}\\
&\le
\frac{q^d}{1-q^2},
\end{aligned}
\tag{19}
\]

which proves (5). Self-adjointness gives the reversed estimate.

No asymptotic eigenfunction estimate is used. The localization follows from the exact PF-231 Pöschl--Teller basis and the exact PF-232 hypercycle formula.

## 3. Convex interpolation gives the uniform two-boundary shear bound

PF-232 records the exact identity

\[
b=(1-X)f_{w_1}'-Xf_{w_2}'.
\]

Applying (5) to each term and using `0<=X<=1`,

\[
\begin{aligned}
\|E_{\le M}M_bE_{\ge M+d}\|
&\le
(1-X)(1+w_1^2)q(w_1)^d
+X(1+w_2^2)q(w_2)^d\\
&\le
(1+\beta^2)\beta^d,
\end{aligned}
\tag{20}
\]

because `q(w)<=w<=beta`. This proves (7).

The estimate is stronger than the pointwise PF-232 bound `|b|<=beta`. Pointwise smallness says every mode-mixing channel costs at most `O(beta)` in norm; (7) says a jump of `d` Pöschl--Teller indices costs `O(beta^d)`.

## 4. A fixed scaled-frequency jump is super-algebraically suppressed

The eigenvalues of `K_s^rect=sA^{1/2}` are exactly `s(m+alpha)`, so the two projectors in (9) are separated by at least the integer distance (10), proving (11). The elementary floor/ceiling inequality gives (12).

On the canonical tail PF-232 gives `beta_n=O(P_n^{-1})`, while PF-228/PF-239 give `s_n asymp (g_n+g_{n+1})/P_n`. Since consecutive odd-prime gaps are positive even integers, `g_n+g_{n+1}>=4`; hence `beta_n=O(s_n)` after changing the tail constant. Also `s_n->0` because `P_{n+1}/P_n->1`.

For fixed `Delta>0`, equations (12)--(13) therefore give

\[
\beta_n^{d_{s_n}}
\le
\exp\!\left[-\left(\frac{\Delta}{s_n}-1\right)
\log\frac1{\beta_n}\right].
\tag{21}
\]

The exponent dominates `N log(1/s_n)` for every fixed `N`, proving (14).

This is a scale statement, not a prime-distribution mechanism. Apart from the already-established canonical asymptotics and the trivial positive gap floor, no delicate theorem about prime gaps enters the proof.

## 5. Consequence for the PF-239--PF-241 high-high gate

PF-239 deliberately allowed arbitrary mixing between its fixed low band and the high tail, because the low-touch correction is already trace summable at cost `O(beta/s)`. PF-242 shows that the **direct shear coefficient** is much more structured: after inserting a fixed buffer `Delta` in the exact PF-231 scaled spectrum, coupling across that buffer is super-algebraically small.

Hence a proof or counterexample for PF-240's remaining high-high block does not need to treat the shear as an arbitrary `O(beta)` bounded operator. The direct coefficient is effectively near-diagonal in Pöschl--Teller mode index. A surviving high-high obstruction must come from one of two places:

1. near-diagonal propagation among modes whose scaled frequencies differ by `O(1)` or less; or
2. failure of the variable-width background, actual seam normalization, or nonlinear DtN/Schur operations to preserve the coefficient-level locality quantified in (7)--(11).

This is useful because these are mathematically different gates. The first is an opposite-boundary elliptic propagation problem; the second is a stability-of-locality problem. Treating them as generic high-high `O(beta)` mixing discards exact structure that the prime-flute geometry supplies for free.

## 6. Prior-art and novelty audit

Exponential off-diagonal decay for analytic functions of banded or sparse Hermitian matrices is classical matrix-analysis territory. A representative source is Michele Benzi and Valeria Simoncini, *Decay Bounds for Functions of Hermitian Matrices with Banded or Kronecker Structure*, SIAM Journal on Matrix Analysis and Applications 36 (2015), 1263--1282, DOI `10.1137/151006159`. Analytic Jacobi/Gegenbauer expansions and their exponential coefficient decay are likewise standard approximation theory.

No novelty is claimed for the Gegenbauer three-term recurrence, banded functional calculus, or the general fact that analytic multipliers have localized matrices. The proof above does not need an external decay theorem: the exact series (18) and the bandwidth of powers of `J` give (5) directly.

The project-specific mathematical delta is the identification of PF-232's **actual hypercycle slope** with the special Jacobi function

\[
qJ(1-q^2J^2)^{-1/2},
\qquad
q=\frac{w}{\sqrt{1+w^2}},
\]

so that the mode-localization ratio is itself the canonical geometric shear scale `q<=w<=beta=O(P^{-1})`. A structure-directed search did not identify this prime-flute specialization or its consequence that a fixed PF-231 scaled-frequency jump costs `beta^{Theta(1/s)}`.

## 7. Falsification and boundary checks

1. **Coefficient locality is not Schur locality.** Equations (5)--(11) concern multiplication by the direct shear coefficient `b`. They do not assert the same matrix decay for `D_1-D_0`, `Lambda_1-Lambda_0`, their inverses, or the actual seam-normalized Schur factor.
2. **The basis is PF-231's untrimmed Pöschl--Teller basis.** PF-233's variable-width `K_a` is only form-comparable to the corresponding scaled Pöschl--Teller operator; PF-242 does not silently identify their spectral projectors.
3. **Width variation remains separate.** The coefficient `a(theta)=s-f_{w_1}(theta)-f_{w_2}(theta)` is not claimed to have the same exact polynomial/Jacobi expansion. PF-232 already separates this bounded width deformation from the reciprocal-prime-small shear.
4. **No high-high trace estimate yet.** PF-240 still requires more than one total scaled boundary derivative on the full high-high normalized correction. PF-242 supplies no such derivative bound by itself.
5. **No arbitrary continuum interpolation.** The analytic multiplier is derived from the exact sampled hypercycle graphs fixed by the canonical PF-205 construction. It is not an off-prime interpolation introduced as arithmetic data.
6. **Canonical tail only for the arithmetic corollary.** The operator bounds (5)--(11) are exact for any `w_i<1`; only (13)--(14) use the prime-flute tail scales.
7. Physical `P/H` recoupling, finite-pant completion, neighboring-cell coupling, PF-222 global reassembly, wave/scattering theory, determinants/resonances, zeta zeros, and RH remain outside the result.

## Consequences for the research line

The smooth route is now narrower than the generic long-strip formulation in PF-241 suggests. The growing tangential interval does not give the **direct shear coefficient** access to arbitrary distant Pöschl--Teller modes: fixed scaled-frequency jumps are suppressed by `beta^{Theta(1/s)}`. The next local theorem should therefore exploit near-diagonal high-mode propagation and test whether this exact coefficient locality survives the variable-width DtN and actual-seam normalized Schur calculus strongly enough to yield PF-240's `r_1+r_2>1` estimate.

If that propagation fails, the countermechanism must identify where locality is destroyed. A generic appeal to mode mixing or to the length `pi/s` of the scaled strip is no longer sufficient.