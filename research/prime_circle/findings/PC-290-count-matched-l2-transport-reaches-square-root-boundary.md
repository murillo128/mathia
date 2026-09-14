# PC-290 — count-matched L2 transport reaches the square-root boundary

**Status:** `LITERATURE+DERIVED` + `CONDITIONAL-RH-COROLLARY` + `MATCHED-CONTROL-OBSTRUCTION` + `DECISIVE-BOUNDARY` for the one-profile boundary-log finite-section frontier left by PC-289.

PC-289 reduces the remaining RH-side loss for the exact selector-subtracted boundary logarithm to the pointwise normalized prime-versus-Li source discrepancy

\[
\Delta_q\ll q^{-1/2}(\log q)^2+\frac{\log q}{q}.
\]

The geometry and logarithmic clipping no longer impose that `log^2 q` factor. This finding isolates what does: **the entire remaining factor is the single endpoint count mismatch between the prime source and the normalized Li source.** If a matched control is allowed to know only the total number of prime source points, but not their locations, then an `L^2` source discrepancy and the PC-288 path-energy estimate close the polylogarithmic gap and force collapse for every

\[
\boxed{B=o(\sqrt q).}
\]

More precisely, let `P_q` be the exact prime source set used in PC-277--PC-289, let

\[
M_q:=|P_q|,
\qquad
A_q:=\operatorname{Li}(q)-\operatorname{Li}(2),
\qquad
E_q:=M_q-A_q,
\qquad
L:=\log q.
\tag{1}
\]

The harmless endpoint convention for whether the conductor prime itself belongs to `P_q` changes `M_q` by at most one and does not affect any estimate below. Under RH,

\[
E_q=O(\sqrt q\,L).
\tag{2}
\]

For sufficiently large prime `q`, put

\[
H_q:=4(|E_q|+1)L<q-2
\tag{3}
\]

and define an absolutely continuous **count-matched Li control** on `[2,q]` by

\[
w_q(x)
:=
\frac1{\log x}
+
\frac{E_q}{H_q}\,
\mathbf 1_{[q-H_q,q]}(x).
\tag{4}
\]

Because `|E_q|/H_q<=1/(4L)` while `1/log x>=1/L` on `[2,q]`, this density is positive. It has exactly the prime-source mass:

\[
\int_2^q w_q(x)\,dx=A_q+E_q=M_q.
\tag{5}
\]

After scaling `x=qt` and dividing by `M_q`, let `lambda_q^#` be the resulting probability measure on `[2/q,1]`; let `\widetilde\lambda_q^#` be its nearest denominator-`q` grid projection exactly as in PC-277. This control uses the scalar `M_q` and the classical Li profile, but **no individual prime location**.

Let `rho^{#,log}_{q,B}` be the complete normalized ordered singular-spectrum law of the exact PC-283/PC-289 boundary-log finite section under the product source `\widetilde\lambda_q^#\otimes\widetilde\lambda_q^#`. Then, under RH, for `N=2B+1<=q` and every `1/q<=epsilon<=1/4` satisfying

\[
\frac{\varepsilon q}{B}\ge q^{1/3},
\tag{6}
\]

we have

\[
\boxed{
\begin{aligned}
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{#,log}_{q,B}
\right)
\ll{}&
\sqrt{\varepsilon+\frac{L^3}{q}}\\
&+\frac{B}{\sqrt\varepsilon}
\left(
q^{-1/2}+q^{-3/4}L^3+\frac{L}{q}
\right)
+\frac{L^2}{q}.
\end{aligned}
}
\tag{7}
\]

Choosing

\[
\boxed{\varepsilon_q:=Bq^{-1/2}}
\tag{8}
\]

makes (6) automatic because `epsilon_q q/B=sqrt q`. Therefore

\[
\boxed{
\mathrm{RH}
\quad\Longrightarrow\quad
B=o(\sqrt q)
\quad\Longrightarrow\quad
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{#,log}_{q,B}
\right)\longrightarrow0.
}
\tag{9}
\]

This reaches the denominator-microscopic square-root scale **from below**, with no surviving power of `log q`, once total source cardinality is matched. It does not improve PC-289 against its original fixed normalized Li-grid control. Instead it identifies the obstruction left by PC-289 as one scalar piece of classical prime-counting data, not as extra information created by the two-dimensional finite-section geometry.

## 1. RH mean square removes the pointwise logarithmic loss after count matching

The load-bearing external theorem is Richard P. Brent, David J. Platt and Timothy S. Trudgian, **The mean square of the error term in the prime number theorem**, *Journal of Number Theory* 238 (2022), 740--762, DOI `10.1016/j.jnt.2021.09.016`, arXiv:2008.06140. They prove under RH that, with `psi` the von Mangoldt summatory function,

\[
\int_X^{2X}(\psi(x)-x)^2\,dx\ll X^2.
\tag{10}
\]

Since `psi(x)-theta(x)=O(sqrt x)`, the same dyadic mean-square order holds for `theta(x)-x`. Partial summation gives, up to a fixed endpoint convention,

\[
\pi(x)-\operatorname{Li}(x)
=
\frac{\theta(x)-x}{\log x}
+
\int_2^x
\frac{\theta(t)-t}{t\log^2 t}\,dt
+O(1).
\tag{11}
\]

On each dyadic interval `[X,2X]`, the first term has `L^2` norm `O(X/log X)` by (10). For the integral term, Cauchy--Schwarz on dyadic shells gives

\[
\int_Y^{2Y}
\frac{|\theta(t)-t|}{t\log^2t}\,dt
\ll
\frac{\sqrt Y}{\log^2Y},
\tag{12}
\]

and summing the geometric dyadic tail yields a pointwise bound `O(sqrt x/log^2 x)` for that integral contribution. Summing the resulting shell estimates therefore gives

\[
\boxed{
\int_2^q
\left|
\Pi_q(x)-\bigl(\operatorname{Li}(x)-\operatorname{Li}(2)\bigr)
\right|^2dx
\ll
\frac{q^2}{L^2},
}
\tag{13}
\]

where `Pi_q(x)` counts the source primes up to `x`; changing the endpoint convention at `q` contributes only `O(1)`.

Equation (13) is not a new prime-number theorem. It is a direct transfer of the Brent--Platt--Trudgian RH mean-square estimate from `psi` through `theta` to `pi`.

## 2. Localizing the count correction prevents it from reintroducing the endpoint error

Let

\[
C_q(x)
:=
\int_2^x
\frac{E_q}{H_q}
\mathbf 1_{[q-H_q,q]}(u)\,du.
\tag{14}
\]

Then `C_q(q)=E_q` and

\[
\|C_q\|_{L^2(2,q)}
\le |E_q|\sqrt{H_q}.
\tag{15}
\]

If

\[
D_q(t)
:=
\nu_q([0,t])-\lambda_q^#([0,t]),
\tag{16}
\]

then scaling `x=qt` and using `M_q\asymp q/L`, (2), (3), (13), and (15) gives

\[
\begin{aligned}
\|D_q\|_{L^2(0,1)}
&\le
\frac{1}{M_q\sqrt q}
\left(
O(q/L)+O(|E_q|\sqrt{H_q})
\right)\\
&\ll
q^{-1/2}+q^{-3/4}L^3.
\end{aligned}
\tag{17}
\]

The nearest-grid projection changes a CDF by at most the largest projected cell mass. The Li part contributes `O(L/q)` in the worst endpoint cells, while the terminal correction in (4), after normalization, has density `O(1/q)` per unit `x`. Hence

\[
\boxed{
\left\|
F_{\nu_q}-F_{\widetilde\lambda_q^#}
\right\|_{L^2(0,1)}
\ll
q^{-1/2}+q^{-3/4}L^3+\frac{L}{q}
\ll q^{-1/2}.
}
\tag{18}
\]

The contrast with the original normalized Li control is essential. If one normalizes Li by `A_q` rather than matching the count `M_q`, the endpoint error `E_q` is spread through the normalized CDF with size `E_q/M_q=O(q^{-1/2}L^2)`. Mean-square information about the interior counting error cannot remove that deterministic normalization component. The control (4) localizes precisely that one scalar mismatch into a short terminal interval while keeping local mass comparable with the Li profile.

## 3. L2 source discrepancy pairs with the PC-288 path energy

For the flat-clipped boundary-log matrix of PC-288/PC-289, let `Sigma_epsilon(x,y)` denote the normalized ordered singular-value vector and let `Phi` be `1`-Lipschitz for `ell^infinity`. Fixing `y`, set

\[
F_y(x):=\Phi(\Sigma_\varepsilon(x,y)).
\tag{19}
\]

PC-288 proves the one-coordinate derivative-energy estimate

\[
\boxed{
\|F_y'\|_{L^2(0,1)}
\ll
\frac{B}{\sqrt\varepsilon},
}
\tag{20}
\]

uniformly in the fixed second coordinate. The same bound holds after exchanging the two source coordinates.

Because both source measures are probabilities, their CDF difference vanishes at the endpoints. One-dimensional Stieltjes integration by parts followed by Cauchy--Schwarz therefore gives

\[
\left|
\int F_y\,d\nu_q-
\int F_y\,d\widetilde\lambda_q^#
\right|
\le
\|F_y'\|_2
\left\|
F_{\nu_q}-F_{\widetilde\lambda_q^#}
\right\|_2.
\tag{21}
\]

Using (18), then telescoping the two product-source coordinates, yields

\[
\boxed{
W_1^{(\ell^\infty)}
\left(
\widehat\rho^{prime,(\varepsilon)}_{q,B},
\widehat\rho^{#,(\varepsilon)}_{q,B}
\right)
\ll
\frac{B}{\sqrt\varepsilon}
\left(
q^{-1/2}+q^{-3/4}L^3+\frac{L}{q}
\right).
}
\tag{22}
\]

This is the step that the Kolmogorov/Koksma estimate in PC-289 cannot see. The spectral path already comes with an `L^2` derivative estimate; pairing it with an `L^2` CDF discrepancy avoids paying the worst pointwise prime-counting fluctuation at every source location.

## 4. The PC-289 short-interval clipping estimate survives the matched control

The prime side of PC-289 is unchanged. For the count-matched control, the extra term in (4) has unnormalized density at most `1/(4L)` and normalized density `O(1/q)` per unit `x`. Consequently an ordinary interval of length `H` receives correction mass `O(H/q)`, exactly the scale required in the PC-289 long-interval preimage estimate.

The Li part already satisfies that estimate. After nearest-grid projection, the same `O(L/q)` worst-cell padding used in PC-289 remains valid. Therefore the logarithmic-depth shell argument of PC-289 applies to `\widetilde\lambda_q^#` without a new logarithmic loss. Under (6), for both the prime product source and the count-matched product source,

\[
\boxed{
\mathbb E
\left\|
\frac{K_{q,B}-\widehat K^{(\varepsilon)}_{q,B}}{N}
\right\|_F^2
\ll
\varepsilon+\frac{L^3}{q}.
}
\tag{23}
\]

Thus clipping each complete normalized singular-spectrum law costs

\[
O\!\left(\sqrt{\varepsilon+L^3/q}\right).
\tag{24}
\]

Passing from independent prime product pairs to the distinct prime-pair law still costs `O(L^2/q)`, exactly as in PC-289. Combining (22)--(24) proves (7).

## 5. Optimization reaches every sub-square-root bandwidth

Take `epsilon_q=B/sqrt q`. For every `B=o(sqrt q)`, eventually `1/q<=epsilon_q<=1/4`, `2B+1<=q`, and

\[
\frac{\varepsilon_q q}{B}=\sqrt q\ge q^{1/3},
\]

so all hypotheses of (7) hold. The terms in (7) become

\[
\begin{aligned}
\sqrt{\varepsilon_q}&=B^{1/2}q^{-1/4},\\
\frac{Bq^{-1/2}}{\sqrt{\varepsilon_q}}&=B^{1/2}q^{-1/4},\\
\frac{Bq^{-3/4}L^3}{\sqrt{\varepsilon_q}}&=B^{1/2}q^{-1/2}L^3,\\
\frac{BL/q}{\sqrt{\varepsilon_q}}&=B^{1/2}q^{-3/4}L,
\end{aligned}
\tag{25}
\]

plus the collision floor `L^{3/2}/sqrt q` and the distinct-pair correction `L^2/q`. Every term tends to zero whenever `B=o(sqrt q)`, proving (9).

This is the natural limit of the present argument: at `B` comparable with `sqrt q`, the chosen clipping scale is order one and the denominator-microscopic finite section is entering the exact rational-resolution regime. No claim is made at `B asy sqrt q` itself.

## 6. Prior-art and novelty audit

No new analytic-number-theory theorem is claimed. The RH mean-square input is Brent--Platt--Trudgian (2022), whose theorem is explicitly cited above. The passage `psi -> theta -> pi` by partial summation and dyadic Cauchy--Schwarz is classical. The identity (21) is the standard one-dimensional cumulative-discrepancy/Stieltjes duality followed by Cauchy--Schwarz; it is closely related to the classical `L^2` CDF geometry behind Cramer--von Mises and one-dimensional negative-Sobolev discrepancy. PC-288 already supplies the matching spectral path-energy norm, and PC-289 supplies the short-interval clipping estimate.

Targeted searches against mean-square PNT error, `L^2`/negative-Sobolev empirical-measure discrepancy, Cramer--von Mises transport, and prime finite-section/log-sine spectral problems found the expected classical ingredients but no independent theorem that supplies a new Prime-Circle spectral mechanism here. The project-local content is the composition of those classical ingredients with the exact PC-283 boundary-log finite section and, crucially, the matched control (4).

The control should not be called arithmetic-free: it is given the scalar `M_q`. That is deliberate. It is a **falsification control for positional information**. It asks whether, after fixing the total number of source points, their exact prime locations contribute an order-one one-profile singular-spectrum law below denominator resolution. Equation (9) says that under RH they do not.

No `SOURCES.md` change is required for this finding: the new external theorem is identified here with full bibliographic data and exact logical role, while the remaining transport, clipping, and operator inputs are already anchored by PC-288/PC-289.

## 7. Boundaries, falsification, and research-line consequence

The result is conditional on RH only through two classical source estimates: the Brent--Platt--Trudgian mean square and the pointwise endpoint bound (2). Equations (4)--(5), the positivity of the control, the source-to-grid projection estimate, and the operator transport are deterministic once those estimates are supplied. This is not an RH criterion: collapse against a control already carrying `M_q` cannot recover RH, because the count scalar itself contains classical prime-number-theorem fluctuations.

The decisive checks are local. First, (13) can be falsified only by an error in the `psi -> theta -> pi` mean-square transfer. Second, the control must stay nonnegative and integrate exactly to `M_q`; both are explicit in (3)--(5). Third, its arbitrary-interval mass must remain `O(H/q)` at the PC-289 clipping scales; the correction density was chosen specifically to ensure this. Fourth, the CDF projection error must stay `O(L/q)`. Fifth, the path-energy inequality (20) is exactly the persisted PC-288 bound, so any failure of (22) would have to come from the Stieltjes/Cauchy--Schwarz pairing or the source discrepancy (18).

The main research consequence is sharper than the `log^2` frontier of PC-289. For the **single-source normalized boundary-log singular-spectrum architecture**, the remaining polylogarithmic gap is not evidence of hidden two-dimensional arithmetic. It is the classical scalar endpoint mismatch `M_q-A_q`. Once that scalar is matched, all positional prime information is asymptotically reproducible by a non-prime denominator-grid control for every `B=o(sqrt q)` under RH.

Therefore a genuinely new Prime-Circle RH mechanism should not spend further effort interpreting the PC-289 `log^2` gap as a geometric critical scale. A surviving route must either make essential use of the scalar prime-count error itself -- which is classical explicit-formula territory -- or leave this one-profile architecture for cross-level, multi-source, directional, noncommuting, or otherwise information-preserving structure allowed by the canonical mandate.