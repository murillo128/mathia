# WP-112 — Exact critical prime-torus completions have infinite cylindrical product-Wasserstein cost

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + OPTIMAL-TRANSPORT + CORRELATION-ROBUST + SHARP-THRESHOLD + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-111` closes the escape from critical Fisher divergence to another Chentsov-natural Riemannian statistical metric, but deliberately leaves non-Riemannian and nonsmooth positive geometries open. The most canonical such replacement on the finite prime torus is optimal transport. It does not repair the critical completion.

Let `mu_sigma` be any finite positive measure of mass `C>0` on the prime torus whose exact one-prime first moments are

\[
\widehat\mu_\sigma(e_p)=-\frac{\log p}{p^\sigma}.
\tag{1}
\]

For a finite prime set `P`, normalize its marginal to a probability measure

\[
\eta_P=C^{-1}(\pi_P)_*\mu_\sigma,
\qquad
m_P=\bigotimes_{p\in P}\frac{d\theta_p}{2\pi}.
\tag{2}
\]

Give each circle its standard geodesic distance `d_T` and `T^P` the additive squared product cost

\[
d_P(\theta,\phi)^2
=\sum_{p\in P}d_T(\theta_p,\phi_p)^2.
\tag{3}
\]

Then the quadratic Wasserstein distance satisfies the correlation-independent lower bound

\[
\boxed{
W_{2,P}(\eta_P,m_P)^2
\ge
\frac1{C^2}
\sum_{p\in P}\frac{(\log p)^2}{p^{2\sigma}}.
}
\tag{4}
\]

Consequently

\[
\boxed{
\sup_{P\Subset\mathcal P}W_{2,P}(\eta_P,m_P)=+\infty
\qquad(\sigma\le1/2).
}
\tag{5}
\]

At the Weil exponent `sigma=1/2`, every exact positive completion therefore has infinite **cylindrical product-transport cost** to Haar, including correlated completions of the type constructed in `WP-101`. This conclusion needs no density, Fisher differentiability, product factorization, spectral multiplier, or zero data.

The threshold is matched. For every `sigma>1/2`, there is an exact positive product completion whose finite-cylinder Wasserstein costs are uniformly bounded. Thus the divergence occurs exactly at the same critical exponent forced by the one-prime Weil amplitudes; it is not a generic pathology of transport geometry.

This is a branch-specific no-go, not a new theorem in optimal transport and not a proof of Weil positivity.

## 1. Coordinate transport cannot hide the exact prime moments

Write `eta_p` for the `p`-th marginal of `eta_P` and `m` for Haar probability on one circle. From (1),

\[
\int_{\mathbb T}e^{-i\theta}\,d\eta_p(\theta)
=-\frac{\log p}{C p^\sigma}.
\tag{6}
\]

The real function `cos(theta)` is 1-Lipschitz for the unit-circle geodesic distance, while its Haar mean is zero. Kantorovich--Rubinstein duality therefore gives

\[
W_1(\eta_p,m)
\ge
\left|
\int\cos\theta\,d(\eta_p-m)
\right|
=
\frac{\log p}{C p^\sigma}.
\tag{7}
\]

For probability measures, `W_2>=W_1`, hence

\[
W_2(\eta_p,m)^2
\ge
\frac{(\log p)^2}{C^2p^{2\sigma}}.
\tag{8}
\]

Now let `Pi` be any coupling of `eta_P` with `m_P`. Its projection `Pi_p` to the `p`-th pair of circle coordinates is a coupling of `eta_p` with `m`, so additivity of the cost gives

\[
\begin{aligned}
\int d_P(\theta,\phi)^2\,d\Pi
&=\sum_{p\in P}
\int d_T(\theta_p,\phi_p)^2\,d\Pi_p\\
&\ge\sum_{p\in P}W_2(\eta_p,m)^2.
\end{aligned}
\tag{9}
\]

Taking the infimum over `Pi` and using (8) proves (4). Mixed-prime correlations cannot cancel any term because every coordinate projection of every global transport plan is still a valid one-coordinate transport plan.

At criticality,

\[
\sum_p\frac{(\log p)^2}{p}=+\infty,
\tag{10}
\]

so (5) follows. More generally the prime number theorem and partial summation give convergence of the series in (4) exactly when `sigma>1/2`.

## 2. The supercritical side has finite transport cost

The lower bound alone could reflect a poor choice of reference geometry. A matched positive completion shows that it is sharp.

Fix `sigma>1/2` and put

\[
r_p=p^{-\sigma},
\qquad
c_{p,\sigma}=\frac{2\log p}{p^\sigma-1}.
\tag{11}
\]

Since `c_{p,sigma}->0`,

\[
C_\sigma^*:=\sup_p c_{p,\sigma}<\infty.
\tag{12}
\]

Choose `C>C_sigma^*` and define the one-circle probability density

\[
\rho_{p,C,\sigma}(\theta)
=1+\frac{\log p}{C}
\left(1-P_{r_p}(\theta)\right),
\tag{13}
\]

with `P_r` the Poisson kernel. Exactly as in `WP-097`,

\[
\widehat\rho_{p,C,\sigma}(k)
=-\frac{\log p}{C}p^{-\sigma|k|}
\qquad(k\ne0),
\tag{14}
\]

and

\[
\rho_{p,C,\sigma}\ge
m_0:=1-\frac{C_\sigma^*}{C}>0.
\tag{15}
\]

The product probability measure `eta_sigma=\bigotimes_p rho_{p,C,sigma}m` therefore gives an exact positive completion after multiplication by `C`.

For completeness, its transport cost can be bounded without appealing to a small-perturbation asymptotic. Put `delta_p=rho_{p,C,sigma}-1` and solve on the circle

\[
-u_p''=\delta_p,
\qquad \int u_p\,dm=0.
\tag{16}
\]

Along the linear density path `rho_t=1+t delta_p`, choose the velocity field by

\[
rho_t v_t=u_p'.
\tag{17}
\]

Then `partial_t rho_t+partial_theta(rho_t v_t)=0`, and (15) gives the Benamou--Brenier bound

\[
W_2(\rho_{p,C,\sigma}m,m)^2
\le
m_0^{-1}\int|u_p'|^2\,dm.
\tag{18}
\]

Parseval and (14) yield

\[
\begin{aligned}
\int|u_p'|^2\,dm
&=\frac{2(\log p)^2}{C^2}
\sum_{k\ge1}\frac{p^{-2\sigma k}}{k^2}\\
&\le
\frac{2(\log p)^2}{C^2}
\frac{p^{-2\sigma}}{1-p^{-2\sigma}}.
\end{aligned}
\tag{19}
\]

The right-hand side is summable over primes for `sigma>1/2`. For finite products and the additive squared cost (3), product optimal couplings give the reverse inequality to (9), so

\[
W_{2,P}\!\left(
\bigotimes_{p\in P}\rho_{p,C,\sigma}m,
 m_P
\right)^2
=
\sum_{p\in P}W_2(\rho_{p,C,\sigma}m,m)^2.
\tag{20}
\]

Equations (18)--(20) therefore imply

\[
\sup_{P\Subset\mathcal P}
W_{2,P}(\eta_{\sigma,P},m_P)<\infty
\qquad(\sigma>1/2).
\tag{21}
\]

This is the matched control for (5).

## 3. Weighted product metrics show exactly what an escape must insert

The equal-coordinate product metric is not the only diagonal transport geometry one could put on the prime torus. Let `w_p>0` and instead use

\[
d_{P,w}^2
=\sum_{p\in P}w_p d_T^2.
\tag{22}
\]

The same projection argument gives the exact necessary lower bound

\[
\boxed{
W_{2,P,w}(\eta_P,m_P)^2
\ge
\frac1{C^2}
\sum_{p\in P}
w_p\frac{(\log p)^2}{p^{2\sigma}}.
}
\tag{23}
\]

Thus at criticality every such product transport geometry still diverges whenever

\[
\sum_p w_p\frac{(\log p)^2}{p}=+\infty.
\tag{24}
\]

In particular bounded-below weights, positive powers of `log p`, and even `w_p=(log p)^{-2}` all fail. Among pure logarithmic dampings `w_p=(log p)^{-a}`, summability begins only for `a>2`.

This is also the exact boundary against overclaiming. A sufficiently fast prime-dependent damping can make (24) converge. Such a weighted metric is not ruled out; but unless Prime Circle, Prime Flute, Prime Lattice, or a finite--archimedean coupling independently forces those weights, choosing them merely to cross (24) is an inserted regularization rather than an intrinsic positivity theorem.

The weighted supercritical product construction satisfies the analogous upper bound whenever the series on the right of (23) converges, by multiplying the one-coordinate bounds in (18)--(19) by `w_p`.

## 4. Adversarial controls and relation to the previous obstructions

**Correlations do not help.** `WP-101` proves that correlations can repair Haar measure-class singularity at the critical exponent. Equation (9) is insensitive to that repair because it uses only fixed coordinate marginals. The obstruction therefore survives the strongest currently known correlated completion escape.

**No density or smoothness is assumed in the negative direction.** Unlike `WP-102` and `WP-111`, equations (6)--(9) apply to arbitrary probability marginals on each finite torus. A singular critical state cannot evade the lower bound.

**This is not merely the Chentsov theorem again.** Wasserstein distance is not a Chentsov-natural statistical Riemannian tensor on the simplex. The proof uses global optimal-transport duality and coordinate projection, so `WP-111` does not imply it.

**This is not the Kronecker spectral form of `WP-109`.** `WP-109` measures Fourier coefficients with a multiplier depending on the multiplicative flow frequency `E(alpha)`. Here the cost is the nonlinear optimal-transport distance for the ordinary product circle geometry. Its linearization near Haar is related to negative-order Sobolev geometry, as standard optimal-transport theory predicts, but the exact lower bound (4) is global and does not require linearization or absolute continuity.

**The mechanism remains universal.** Replacing primes by free generators with energies `E_j` and exact first moments `-E_j e^{-sigma E_j}` gives the identical lower bound `C^{-2} sum_j w_j E_j^2e^{-2sigma E_j}`. The divergence is therefore a useful obstruction, not Riemann-specific arithmetic evidence.

**There is still no archimedean term.** Neither the transport metric nor the product completion generates the Gamma/digamma or polar contribution of the Weil explicit formula. Renormalizing the divergent critical transport cost by subtracting an infinite counterterm would also destroy the immediate implication from ordinary metric nonnegativity unless a new theorem controls the renormalized object.

## 5. Prior-art and novelty audit

The optimal-transport ingredients are classical. Cédric Villani, *Topics in Optimal Transportation*, Graduate Studies in Mathematics 58, AMS (2003), DOI `10.1090/gsm/058`, is a standard reference for Kantorovich duality and Wasserstein metric geometry. Jean-David Benamou and Yann Brenier, *A computational fluid mechanics solution to the Monge--Kantorovich mass transfer problem*, Numerische Mathematik 84 (2000), 375--393, DOI `10.1007/s002110050002`, gives the dynamic action formulation used in (18).

No theorem-level novelty is claimed for Kantorovich--Rubinstein duality, Wasserstein monotonicity, product coupling, or the Benamou--Brenier estimate. The retained Mathia-specific content is their composition with the exact prime-torus moment constraints: every positive completion has a correlation-independent cylindrical transport lower bound with the sharp Weil threshold, while the explicit supercritical completion supplies a matched finite-cost control.

A targeted audit found no basis for identifying this transport cost with the Weil quadratic functional itself. Doing so would in any case fail the research mandate: the critical transport cost is infinite, it contains no intrinsic archimedean completion, and it is universal for free-generator controls.

## Consequence for the research line

The natural escape

\[
\text{exact critical positive prime-torus completion}
\longrightarrow
\text{replace Fisher/spectral energy by ordinary product optimal transport}
\longrightarrow
\text{finite geometric positive sign source}
\]

is closed. The critical one-prime amplitudes already force infinite cylindrical `W_2` cost before any mixed-prime correlation can help.

A surviving transport-based construction must therefore alter the geometry itself before taking the positive cost: it needs independently forced prime-dependent weights beyond the divergent regime (24), a genuinely non-product/nonlocal finite-place cost, or a nonseparable finite--archimedean state/cost whose geometry changes the marginal lower bound rather than merely subtracting it afterward. Even then it must still derive the exact finite Weil selector together with the Gamma and polar terms and prove nonnegativity independently of RH or inserted zero data.