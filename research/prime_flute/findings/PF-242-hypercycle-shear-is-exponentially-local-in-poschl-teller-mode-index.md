# PF-242 — hypercycle shear is exponentially local in Pöschl--Teller mode index

**Status:** `EXACT-DERIVED + JACOBI-MODE-LOCALITY + CUT-TRACE/HILBERT-SCHMIDT-CONTROL + POSITIVE/ROUTE-NARROWING`. PF-239 reduces the unresolved sheared-corridor contribution to a high-high normalized Schur block, while PF-241 shows that the canonical tangential blowup is a uniformly elliptic long-strip family. A remaining concern is that the graph-straightening shear could mix widely separated tangential frequencies strongly enough that diagonal-corridor crossing decay becomes unusable.

For the **direct shear multiplier itself**, that concern is false in a much stronger sense than ordinary smoothness. In the exact Pöschl--Teller basis from PF-231, the hypercycle slope is an analytic function of the tridiagonal Jacobi operator `cos(theta)`. Its matrix is therefore exponentially localized in mode index. More precisely, if two Pöschl--Teller spectral windows are separated by `d` mode indices, the direct shear coupling between them is bounded by

\[
\boxed{
\|E_- M_b E_+\|
\le (1+\beta^2)\beta^d,
}
\]

where `beta=max(w_1,w_2)` is exactly PF-232's reciprocal-prime shear scale. On the canonical tail `beta_n=O(P_n^{-1})`, so a fixed separation in **scaled** tangential frequency corresponds to `d=Theta(s_n^{-1})` and the direct mode-jump amplitude is super-algebraically small.

The same exact Jacobi expansion also controls the **unbuffered aggregate crossing of a single mode cut**. If `L_M=E_{\le M}` and `H_M=E_{\ge M+1}`, then uniformly in `M`

\[
\|L_M M_b H_M\|_{\mathcal S_1}=O(\beta),
\qquad
\|L_M M_b H_M\|_{\mathcal S_2}^2=O(\beta^2).
\]

Thus on the canonical tail the raw shear coefficient already has `O(P_n^{-2})` squared Hilbert--Schmidt leakage across every contiguous Pöschl--Teller cut, stronger than the logarithmic-rank `O((1+\log P_n)P_n^{-2})` scale later isolated in PF-318. There is no hidden accumulation over the low band at the coefficient level.

This does **not** yet prove [[research/prime_flute/findings/PF-240-total-one-scaled-boundary-derivative-is-the-sharp-high-high-shear-trace-threshold|PF-240]]'s weighted high-high estimate for the full normalized Schur difference, nor PF-318's seam-normalized physical-frequency estimate. The variable-width diagonal background, actual seam normalization, basis/metric conversion, nonlinear resolvent/Schur operations, and finite-pant completion can mediate additional mode mixing or amplification. The result nevertheless removes two concrete failure mechanisms: the PF-232 coefficient `b` itself cannot directly throw a mode across a macroscopic scaled-frequency gap at merely `O(beta)` cost, and even its near-cut aggregate leakage is already reciprocal-prime-small. Any surviving obstruction must arise when this coefficient-level locality is transported through the remaining operator operations and physical normalization.

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

For the contiguous cut

\[
L_M:=E_{\le M},
\qquad
H_M:=E_{\ge M+1},
\]

the same expansion gives the cut-uniform ideal bounds

\[
\boxed{
\|L_M M_b H_M\|_{\mathcal S_1}
\le
\frac{\beta(1+\beta^2)}{(1-\beta^2)^2},
}
\tag{7a}
\]

and

\[
\boxed{
\|L_M M_b H_M\|_{\mathcal S_2}^2
\le
\frac{(1+\beta^2)^2\beta^2}{1-\beta^2}.
}
\tag{7b}
\]

Both bounds also hold with `L_M,H_M` reversed. In particular they are respectively `O(\beta)` and `O(\beta^2)` with constants independent of the cut position `M`.

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

Thus direct hypercycle-shear coupling across any fixed gap in the PF-231 scaled tangential spectrum is super-algebraically small, while (7a)--(7b) control the aggregate crossing even when no positive buffer is inserted.

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

## 3a. A contiguous mode cut has `O(beta)` trace mass and `O(beta^2)` squared Hilbert--Schmidt mass

The same banded expansion closes the near-cut aggregate that a separated-window operator norm does not display explicitly. Let `L_M=E_{\le M}` and `H_M=E_{\ge M+1}`. Since `J` is tridiagonal, for every integer `r>=1`

\[
\operatorname{rank}(L_MJ^rH_M)\le r,
\qquad
\|L_MJ^rH_M\|\le1.
\tag{20a}
\]

Indeed only the first `r` high-side basis vectors can cross the cut under an `r`-step banded operator. Hence

\[
\|L_MJ^rH_M\|_{\mathcal S_1}\le r.
\tag{20b}
\]

Applying (18) to one hypercycle slope and using `c_k<=1` gives

\[
\begin{aligned}
\|L_MM_{h_w}H_M\|_{\mathcal S_1}
&\le
\sum_{k\ge0}(2k+1)q^{2k+1}\\
&=
\frac{q(1+q^2)}{(1-q^2)^2}.
\end{aligned}
\tag{20c}
\]

The triangle inequality for the two terms in `b`, together with `q(w_i)<=w_i<=beta`, proves (7a). The estimate is uniform in `M`; the increasing number of low modes does not accumulate trace mass because an `r`-step Jacobi term can interact with only `r` modes across one cut.

For the Hilbert--Schmidt bound, let `\phi_m`, `0<=m<=M`, be the low-side basis. For each `m`, apply the reversed form of (7) with separation

\[
d=M+1-m.
\]

Then

\[
\|H_MM_b\phi_m\|
\le(1+\beta^2)\beta^{M+1-m}.
\tag{20d}
\]

Therefore

\[
\begin{aligned}
\|L_MM_bH_M\|_{\mathcal S_2}^2
&=\|H_MM_bL_M\|_{\mathcal S_2}^2\\
&=\sum_{m=0}^M\|H_MM_b\phi_m\|^2\\
&\le(1+\beta^2)^2
\sum_{d=1}^{M+1}\beta^{2d}\\
&\le
\frac{(1+\beta^2)^2\beta^2}{1-\beta^2},
\end{aligned}
\tag{20e}
\]

which is (7b).

On the canonical tail `beta_n=O(P_n^{-1})`, so the raw shear cut has

\[
\|L_MM_{b_n}H_M\|_{\mathcal S_1}=O(P_n^{-1}),
\qquad
\|L_MM_{b_n}H_M\|_{\mathcal S_2}^2=O(P_n^{-2})
\tag{20f}
\]

uniformly in the cut. The second estimate is stronger than PF-318's local sufficient envelope by a factor `1+\log P_n` **provided the relevant physical/seam block can be represented by this raw Jacobi multiplier without an uncontrolled metric or basis conversion**. PF-319 proves that this proviso is load-bearing: coefficient-level smallness in the corridor representation cannot simply be pushed through an unrelated seam normalization.

Thus the current direct-angle problem is no longer whether near-cut raw shear mixing accumulates over a growing low band. It is whether the actual corridor DtN/Schur construction, the change to the seam-energy physical basis, and the finite one-cusp pant completion preserve enough of (20f).

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

## 5. Consequence for the PF-239--PF-241 high-high gate and the PF-318 direct-angle target

PF-239 deliberately allowed arbitrary mixing between its fixed low band and the high tail, because the low-touch correction is already trace summable at cost `O(beta/s)`. PF-242 shows that the **direct shear coefficient** is much more structured. After inserting a fixed buffer `Delta` in the exact PF-231 scaled spectrum, coupling across that buffer is super-algebraically small; without any buffer at all, (7a)--(7b) show that the total cross-cut trace/Hilbert--Schmidt mass is still only `O(beta)`/`O(beta^2)`.

Hence a proof or counterexample for PF-240's remaining high-high block or PF-318's direct-angle block does not need to treat the shear as an arbitrary `O(beta)` bounded operator whose error can accumulate independently across every low mode. At the coefficient level both the distant and contiguous-cut leakage are already controlled.

A surviving obstruction must therefore arise from one of two places:

1. the variable-width background, seam-energy/basis conversion, or nonlinear DtN/Schur operations fail to preserve the coefficient-level locality and cut-ideal bounds; or
2. the finite one-cusp pant completion contributes additional low/high mixing not represented by the raw hypercycle slope.

This is useful because these are mathematically different gates. PF-319 confirms that the first cannot be dismissed by a generic Loewner sandwich: the corridor and seam energy metrics can amplify a small perturbation. Conversely, a future positive proof can aim directly at stability of the cut-ideal estimate through the actual geometric conjugations rather than re-proving raw shear decay.

## 6. Prior-art and novelty audit

Exponential off-diagonal decay for analytic functions of banded or sparse Hermitian matrices is classical matrix-analysis territory. A representative source is Michele Benzi and Valeria Simoncini, *Decay Bounds for Functions of Hermitian Matrices with Banded or Kronecker Structure*, SIAM Journal on Matrix Analysis and Applications 36 (2015), 1263--1282, DOI `10.1137/151006159`. Analytic Jacobi/Gegenbauer expansions and their exponential coefficient decay are likewise standard approximation theory.

The cut trace/Hilbert--Schmidt bounds (7a)--(7b) use no new operator-ideal theorem. They are elementary consequences of the same Jacobi series: an `r`-banded power has cross-cut rank at most `r`, and the geometric coefficient series is summable with that rank weight. Closely related trace-ideal consequences of off-diagonal decay for banded functional calculus are standard; no abstract novelty is claimed here.

The project-specific mathematical delta is the identification of PF-232's **actual hypercycle slope** with the special Jacobi function

\[
qJ(1-q^2J^2)^{-1/2},
\qquad
q=\frac{w}{\sqrt{1+w^2}},
\]

so that the mode-localization ratio is itself the canonical geometric shear scale `q<=w<=beta=O(P^{-1})`. The strengthened consequence is that the same exact structure gives cut-uniform `O(P_n^{-1})` trace mass and `O(P_n^{-2})` squared Hilbert--Schmidt mass with no logarithmic accumulation. A structure-directed search did not identify this prime-flute specialization; novelty is claimed only for this project-specific application, not for the banded-functional-calculus argument.

## 7. Falsification and boundary checks

1. **Coefficient locality/cut ideals are not Schur locality.** Equations (5)--(11) and (7a)--(7b) concern multiplication by the direct shear coefficient `b`. They do not assert the same matrix decay or ideal bounds for `D_1-D_0`, `Lambda_1-Lambda_0`, their inverses, the actual seam-normalized Schur factor, or the physical pant DtN block.
2. **The basis is PF-231's untrimmed Pöschl--Teller basis.** PF-233's variable-width `K_a` is only form-comparable to the corresponding scaled Pöschl--Teller operator; PF-242 does not silently identify their spectral projectors with the PF-212 physical cuff Fourier projections.
3. **Width variation remains separate.** The coefficient `a(theta)=s-f_{w_1}(theta)-f_{w_2}(theta)` is not claimed to have the same exact polynomial/Jacobi expansion. PF-232 already separates this bounded width deformation from the reciprocal-prime-small shear.
4. **No high-high trace or direct-angle theorem yet.** PF-240 still requires more than one total scaled boundary derivative on the full high-high normalized correction, while PF-318 requires the seam-normalized local pant `L/H` Hilbert--Schmidt estimate. The raw coefficient bounds do not supply either after the unresolved metric/basis conversion.
5. **No arbitrary continuum interpolation.** The analytic multiplier is derived from the exact sampled hypercycle graphs fixed by the canonical PF-205 construction. It is not an off-prime interpolation introduced as arithmetic data.
6. **Canonical tail only for the arithmetic corollary.** The operator bounds (5)--(11) and (7a)--(7b) are exact for any `w_i<1`; only (13)--(14) and the `P_n` form of (20f) use the prime-flute tail scales.
7. Physical `P/H` recoupling, finite-pant completion, neighboring-cell coupling, PF-222 global reassembly, wave/scattering theory, determinants/resonances, zeta zeros, and RH remain outside the result.

## Consequences for the research line

The smooth route is narrower than the generic long-strip formulation in PF-241 suggests. The growing tangential interval does not give the **direct shear coefficient** access to arbitrary distant Pöschl--Teller modes, and it does not create logarithmically growing aggregate leakage at a contiguous mode cut: fixed scaled-frequency jumps are suppressed by `beta^{Theta(1/s)}`, while the whole raw cut has `S_1=O(beta)` and squared `S_2=O(beta^2)`.

The next local theorem should therefore no longer spend effort proving raw coefficient low/high summability. It should test whether the actual variable-width DtN/Schur construction and seam-energy physical representation preserve these cut-ideal bounds at reciprocal-prime scale, and then isolate the finite-pant completion. PF-319 shows precisely why this stability step is nontrivial. If the route fails, the countermechanism must identify where the known coefficient-level `O(beta)`/`O(beta^2)` cut control is amplified or destroyed; generic appeals to mode mixing, near-cut accumulation, or the length `pi/s` of the scaled strip are no longer sufficient.