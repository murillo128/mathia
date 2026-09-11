# NB-044 — the logarithmic tail dual decay index equals the zeta zero frontier

**Status:** `CLASSICAL-BRIDGE+EXACT-DERIVED + TWO-SIDED-POWER-DECAY-INDEX + ZERO-FRONTIER-IDENTITY + DUAL-NORM-ORACLE-BOUNDARY + NEGATIVE/METHOD-BOUNDARY`. `NB-043` proves one half of a quantitative boundary for the explicit logarithmic tail dual `Omega_M`: any power decay of its Hilbert norm forces a matching fixed zero-free strip for `zeta`. The converse also holds at the level of epsilon-loss exponents. If
\[
\Theta_\zeta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}
\tag{1}
\]
and
\[
\alpha_\Omega
:=
\sup\left\{
\alpha\in[0,1/2]:
\forall\varepsilon>0,
\ \|\Omega_M\|_2=O_\varepsilon(M^{-\alpha+\varepsilon})
\right\},
\tag{2}
\]
then
\[
\boxed{
\alpha_\Omega=1-\Theta_\zeta.
}
\tag{3}
\]

Equivalently, for every `epsilon>0`,
\[
\boxed{
\|\Omega_M\|_2
=O_\varepsilon\!\left(
M^{-(1-\Theta_\zeta)+\varepsilon}
\right).
}
\tag{4}
\]
Together with `NB-043`, this makes the power-decay exponent of the explicit source-defined selector an exact encoding of the rightmost-zero frontier. Under RH, `Theta_zeta=1/2` and (3) reduces to `NB-042`. If RH is false with `Theta_zeta>1/2`, the optimal epsilon-loss exponent drops continuously to `1-Theta_zeta<1/2`. If `Theta_zeta=1`, there is no positive power decay at all.

This is not a new zero-free theorem and does not improve the finite Nyman distance. The arithmetic input is the classical generalized Littlewood principle that a fixed zero-free half-plane `Re s>theta` implies `M(x)=O_epsilon(x^(theta+epsilon))`; the line-local result is that the exact shell formula of `NB-041` transports that classical zero frontier back to the full Hilbert norm of this particular dual with no further exponent loss.

Use the notation of `NB-041`--`NB-043`,
\[
\mathcal M(x):=\sum_{n\le x}\mu(n),
\qquad
m(x):=\sum_{n\le x}\frac{\mu(n)}n,
\tag{5}
\]
\[
\Theta(x)
:=1-\sum_{n\le x}\frac{\mu(n)}n\log\frac xn,
\tag{6}
\]
and
\[
\Omega_M
=e-\sum_{L=1}^{M-1}\log\frac{L+1}{L}\,\Psi_L.
\tag{7}
\]
On the harmonic shell `I_t=(1/(t+1),1/t]`, `NB-041` gives
\[
\Omega_M|_{I_t}
=
\begin{cases}
(t+1)\Theta(M/t)-t\Theta(M/(t+1)),&1\le t<M,\\
1,&t\ge M,
\end{cases}
\tag{8}
\]
and
\[
\Theta(x)-\Theta(y)
=-\int_y^x m(u)\,\frac{du}{u}.
\tag{9}
\]

## 1. A zero-free half-plane gives the matching reciprocal-Mobius exponent

Assume first that `Theta_zeta<1`. Fix any real
\[
q>\Theta_\zeta.
\tag{10}
\]
The half-plane `Re s>q` is zero-free. The classical Littlewood--Perron argument, in the same form used by Titchmarsh at the RH endpoint, gives
\[
\boxed{
\mathcal M(x)=O_{q,\eta}(x^{q+\eta})
}
\tag{11}
\]
for every `eta>0`. This is the standard generalized version of the familiar criterion
\[
\mathrm{RH}
\Longleftrightarrow
\mathcal M(x)=O_\eta(x^{1/2+\eta}).
\tag{12}
\]
No novelty is claimed for (11): one shifts the Perron contour for `1/zeta(s)` to any fixed line lying strictly to the right of the zero frontier instead of to `1/2+delta`; the usual bounds for `1/zeta` on a fixed zero-free strip absorb the vertical growth into an arbitrary power `x^eta`.

For the exponent transfer below it is convenient to absorb `eta` into `q`. Thus for every
\[
r>\Theta_\zeta
\tag{13}
\]
one may write simply
\[
\mathcal M(x)=O_r(x^r).
\tag{14}
\]

Since `r<1` may be chosen whenever `Theta_zeta<1`, partial summation and the classical limit `m(x)->0` give
\[
\boxed{
m(x)=O_r(x^{r-1}).}
\tag{15}
\]
Indeed,
\[
m(x)
=\frac{\mathcal M(x)}x
-\int_x^\infty\frac{\mathcal M(u)}{u^2}\,du,
\tag{16}
\]
and the integral converges because `r<1`. Integrating (9) from `x` to infinity then yields
\[
\boxed{
\Theta(x)=O_r(x^{r-1}).
}
\tag{17}
\]

Put
\[
\alpha:=1-r.
\tag{18}
\]
Because nontrivial zeta zeros occur on the critical line, `Theta_zeta>=1/2`; after choosing `r>Theta_zeta`, one has
\[
0<\alpha<1/2.
\tag{19}
\]
Equations (15)--(17) therefore give both reciprocal-Mobius quantities needed by the shell identity at the same exponent `alpha`.

## 2. The exact shell resummation loses no power

Rewrite the first line of (8) as
\[
\Omega_M|_{I_t}
=
\Theta(M/t)
+t\left[
\Theta(M/t)-\Theta(M/(t+1))
\right].
\tag{20}
\]
Using (9), (15), (17), and
\[
t\log\frac{t+1}{t}\le1,
\tag{21}
\]
one obtains uniformly for `1<=t<M`,
\[
\begin{aligned}
|\Omega_M|_{I_t}|
&\le
|\Theta(M/t)|
+t\int_{M/(t+1)}^{M/t}|m(u)|\,\frac{du}{u}\\
&\ll_r
\left(\frac Mt\right)^{-\alpha}.
\end{aligned}
\tag{22}
\]

The shell lengths are `|I_t|=1/(t(t+1))`, while `Omega_M=1` on `(0,1/M]`. Hence
\[
\begin{aligned}
\|\Omega_M\|_2^2
&=
\sum_{t=1}^{M-1}
\frac{|\Omega_M|_{I_t}|^2}{t(t+1)}
+\frac1M\\
&\ll_r
M^{-2\alpha}
\sum_{t<M}t^{2\alpha-2}
+\frac1M.
\end{aligned}
\tag{23}
\]
Because `alpha<1/2`, the series is bounded independently of `M`; also `M^{-1}=O(M^{-2alpha})`. Therefore
\[
\boxed{
\|\Omega_M\|_2
=O_r(M^{-(1-r)})
\qquad(r>\Theta_\zeta,\ r<1).
}
\tag{24}
\]

Now fix `epsilon>0` small enough that `Theta_zeta+epsilon<1` and choose
\[
r=\Theta_\zeta+\varepsilon.
\tag{25}
\]
Then (24) gives
\[
\|\Omega_M\|_2
=O_\varepsilon
\left(
M^{-(1-\Theta_\zeta)+\varepsilon}
\right).
\tag{26}
\]
For larger epsilon the same statement follows from any smaller admissible epsilon. Thus (4) holds for every positive epsilon whenever `Theta_zeta<1`.

If `Theta_zeta=1`, no positive exponent is required for the reverse inequality: by definition `alpha_Omega>=0`, while `NB-043` already gives `alpha_Omega<=1-Theta_zeta=0`. Hence (3) also holds at this boundary.

## 3. The selector exponent is exactly the zero frontier

`NB-043` proves the opposite inequality
\[
\alpha_\Omega\le1-\Theta_\zeta.
\tag{27}
\]
Indeed any epsilon-loss power bound with exponent `alpha` excludes zeros with real part greater than `1-alpha`.

Equation (26) proves that every exponent strictly below `1-Theta_zeta` belongs to the admissible set in (2), and in fact supplies the endpoint in the epsilon-loss sense. Therefore
\[
\alpha_\Omega\ge1-\Theta_\zeta.
\tag{28}
\]
Combining (27) and (28) proves (3).

The identity has three immediate regimes:

- `Theta_zeta=1/2` if and only if `alpha_Omega=1/2`, recovering the RH equivalence of `NB-042`.
- `1/2<Theta_zeta<1` if and only if `0<alpha_Omega<1/2`; the selector has polynomial decay, but at a subcritical exponent determined exactly by the rightmost zeros.
- `Theta_zeta=1` if and only if `alpha_Omega=0`; the unconditional logarithmic decay of `NB-041` may still hold, but no positive power can hold with arbitrary epsilon loss.

Thus `NB-043`'s one-way inequality is sharp at the exponent level. The ambient dual does not merely become expensive near the RH endpoint: its entire polynomial scale is spectrally calibrated by the zeta zero frontier.

## 4. Adversarial checks and endpoint discipline

The proof must not replace the epsilon-loss generalized Littlewood theorem by the false statement that zero-freeness of `Re s>theta` gives an epsilon-free bound `M(x)=O(x^theta)`. The margin `r>Theta_zeta` is essential and is exactly what is absorbed by the epsilon in (4). Likewise no claim is made that the supremum in (1) is attained by a zero.

The passage from `mathcal M` to `m` uses `r<1`. This is why the case `Theta_zeta=1` is split off before (16); there the desired exponent is zero and `NB-043` already settles the equality without a tail integral at a positive power.

The shell sum also needs `alpha<1/2`, not `alpha=1/2`. When RH holds, choosing any `r>1/2` gives `alpha<1/2`, and then letting `r` approach `1/2` through the epsilon-loss family recovers the `M^{-1/2+epsilon}` result. No convergent-series assertion is made at the literal endpoint `alpha=1/2`, where the sum in (23) becomes logarithmic if one insists on an epsilon-free estimate.

The geometric support floor remains consistent with the theorem:
\[
\|\Omega_M\|_2\ge M^{-1/2}.
\tag{29}
\]
Since `Theta_zeta>=1/2`, equation (3) never predicts an exponent larger than `1/2`. Conversely the target pairing
\[
|\Theta(M)|=|\langle e,\Omega_M\rangle|
\le\|\Omega_M\|_2
\tag{30}
\]
is exactly the lower-information channel used by `NB-043`; there is no hidden appeal to the finite Nyman residual `d_N` in either direction of (3).

## 5. Prior art and research consequence

The generalized Mertens/zero-free-half-plane correspondence is classical analytic number theory. Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., section 14.25, gives the Littlewood--Perron contour argument at the RH endpoint; the same proof with the contour placed to the right of a fixed zero frontier yields (11). Modern expositions commonly state the parameterized form directly. No novelty is claimed for that theorem, for the definition of the rightmost-zero abscissa, or for converting a Mertens bound to reciprocal-Mobius estimates by partial summation.

A targeted search across Nyman--Beurling criteria, mollified Mobius sums, selector norms, and zero-free-region formulations did not locate the specific identity (3) for the explicit `NB-041` vector. The line-local contribution is therefore stated narrowly: the exact harmonic-shell resummation already built into `Omega_M` loses no exponent when the classical zero-frontier bound is pushed through it, so the one-sided obstruction of `NB-043` is actually an equality of decay indices.

For the accepted weighted-skeleton target-data clue, this is a stronger negative boundary on the ambient-norm route. There is no intermediate polynomial selector estimate that is arithmetically cheap but weaker than zero information: **every** power exponent of `||Omega_M||` is exactly equivalent, at the exponent-frontier level, to pushing the rightmost zeta zeros the complementary distance away from `1`. The live route should therefore remain target-conditioned: estimate the actual pairing `<r_N,Omega_M>`, the projected repair line, or the explicit source-aligned defect without first obtaining a global norm exponent. Those directional quantities can in principle contain less arithmetic information than the ambient selector norm, whereas any polynomial improvement of that norm has now been fully priced.