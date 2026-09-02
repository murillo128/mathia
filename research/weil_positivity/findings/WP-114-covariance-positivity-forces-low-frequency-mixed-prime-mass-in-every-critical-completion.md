# WP-114 — Covariance positivity forces infinite low-frequency mixed-prime mass in every critical completion

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + ALL-CORRELATIONS + ALL-SOBOLEV-ORDERS + SHORT-PRIME-SHELL + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-109` shows that the exact critical one-prime Weil rays force infinite Kronecker spectral cost through Sobolev order `s=-1`, but leaves stronger negative-order smoothing open. `WP-110` closes every Sobolev order for the explicit independent product completion, and `WP-113` extends that all-order obstruction to the finite-block convex correlated class underlying the Haar-equivalent construction of `WP-101`. The remaining spectral escape was a genuinely arbitrary correlated positive completion whose two-prime coefficients might be arranged to suppress near-zero Kronecker frequencies.

That escape is impossible for every nondegenerate inhomogeneous Kronecker spectral geometry. Positivity of the completion alone forces enough mixed-prime correlation.

Let `mu` be any finite positive measure of mass `C>0` on the infinite prime torus

\[
\mathbb T^{\mathcal P}=\prod_p\mathbb T
\]

whose critical first prime-coordinate moments are exact:

\[
\boxed{
\widehat\mu(e_p)=-\frac{\log p}{\sqrt p}
\qquad(p\in\mathcal P).
}
\tag{1}
\]

For a finite prime set `P`, normalize the marginal

\[
\eta_P=C^{-1}(\pi_P)_*\mu.
\tag{2}
\]

Then for every `epsilon>0`,

\[
\boxed{
\sup_{P\Subset\mathcal P}
\sum_{\substack{p,q\in P,\ p\ne q\\
|\log p-\log q|<\epsilon}}
|\widehat\eta_P(e_p-e_q)|^2
=+\infty.
}
\tag{3}
\]

Thus every exact critical positive completion has infinite squared Fourier mass in every fixed neighborhood of **zero Kronecker frequency**, independently of its mixed-prime architecture, density, measure class, or factorization.

Consequently, if `w:[0,infinity)->[0,infinity)` is continuous at zero with `w(0)>0`, the nonnegative cylindrical spectral form

\[
\mathcal Q_{w,P}(\eta_P)
=
\sum_{\alpha\in\mathbb Z^P}
 w(|E(\alpha)|)|\widehat\eta_P(\alpha)|^2,
\qquad
E(\alpha)=\sum_{p\in P}\alpha_p\log p,
\tag{4}
\]

satisfies

\[
\boxed{
\sup_{P\Subset\mathcal P}\mathcal Q_{w,P}(\eta_P)=+\infty.
}
\tag{5}
\]

In particular, for the entire inhomogeneous Kronecker Sobolev scale

\[
w_s(t)=(1+t^2)^s,
\]

one has

\[
\boxed{
\sup_{P\Subset\mathcal P}\mathcal S_{s,P}(\eta_P)=+\infty
\qquad\text{for every }s\in\mathbb R.
}
\tag{6}
\]

This closes the `s<-1` arbitrary-correlation escape left open by `WP-109`. The mechanism is different from `WP-113`: no block decomposition or formula for the mixed coefficients is assumed. The required correlations follow directly from the positive covariance matrix of the prime-coordinate unitary random variables.

## 1. A finite covariance inequality forces off-diagonal Gram mass

Fix a finite set `Q` of primes and work with its normalized marginal `eta_Q`. Put

\[
z_p(\theta)=e^{i\theta_p},
\qquad
m_p=\mathbb E_{\eta_Q}z_p.
\tag{7}
\]

By (1)--(2), up to the harmless Fourier sign convention,

\[
|m_p|=a_p:=\frac{\log p}{C\sqrt p}.
\tag{8}
\]

Define the correlation Gram matrix

\[
R_{pq}:=\mathbb E_{\eta_Q}(z_p\overline{z_q}).
\tag{9}
\]

Because the `z_p` have unit modulus,

\[
R\succeq0,
\qquad
R_{pp}=1.
\tag{10}
\]

More importantly, the centered covariance matrix is positive semidefinite:

\[
\boxed{R-mm^*\succeq0.}
\tag{11}
\]

Indeed, for every vector `c`,

\[
c^*(R-mm^*)c
=
\mathbb E\left|
\sum_p c_p(z_p-m_p)
\right|^2
\ge0.
\tag{12}
\]

Write

\[
S_Q:=\|m\|_2^2
=\sum_{p\in Q}|m_p|^2
=\frac1{C^2}\sum_{p\in Q}\frac{(\log p)^2}{p}.
\tag{13}
\]

Testing (11) against `m` gives

\[
m^*Rm\ge(m^*m)^2=S_Q^2.
\tag{14}
\]

The diagonal part of the left side is exactly

\[
\sum_{p\in Q}|m_p|^2R_{pp}=S_Q,
\tag{15}
\]

so

\[
\operatorname{Re}
\sum_{\substack{p,q\in Q\\p\ne q}}
\overline{m_p}m_qR_{pq}
\ge S_Q^2-S_Q.
\tag{16}
\]

For `S_Q>1`, Cauchy--Schwarz therefore yields

\[
S_Q^2-S_Q
\le
\left(
\sum_{p\ne q}|m_p|^2|m_q|^2
\right)^{1/2}
\left(
\sum_{p\ne q}|R_{pq}|^2
\right)^{1/2}.
\tag{17}
\]

Since

\[
\sum_{p\ne q}|m_p|^2|m_q|^2
=S_Q^2-\sum_p|m_p|^4
\le S_Q^2,
\tag{18}
\]

we obtain the architecture-free bound

\[
\boxed{
\sum_{\substack{p,q\in Q\\p\ne q}}|R_{pq}|^2
\ge(S_Q-1)^2.
}
\tag{19}
\]

With the standard torus Fourier convention, `R_{pq}` is one of the two conjugate coefficients at `e_p-e_q`; in particular

\[
|R_{pq}|=|\widehat\eta_Q(e_p-e_q)|.
\tag{20}
\]

Equation (19) is the key point. The mixed coefficients are not free once a **positive** measure carries a sufficiently large vector of prescribed first moments. The covariance inequality forces their total Frobenius mass to become quadratic in the one-prime squared-amplitude mass.

## 2. Ordinary prime density pushes the compulsory correlations to zero frequency

Fix `epsilon>0` and choose a fixed `delta>0` such that

\[
\log(1+\delta)<\epsilon.
\tag{21}
\]

For large `X`, let

\[
Q_X=\{p\text{ prime}:X<p\le(1+\delta)X\}.
\tag{22}
\]

Every distinct pair in this shell has

\[
|E(e_p-e_q)|
=|\log p-\log q|
<\epsilon.
\tag{23}
\]

The prime number theorem gives

\[
\#Q_X\asymp_\delta\frac{X}{\log X}.
\tag{24}
\]

Uniformly for `p in Q_X`,

\[
\frac{(\log p)^2}{p}\asymp_\delta\frac{(\log X)^2}{X}.
\tag{25}
\]

Hence

\[
\boxed{
S_{Q_X}
=\frac1{C^2}
\sum_{p\in Q_X}\frac{(\log p)^2}{p}
\asymp_{\delta,C}\log X
\longrightarrow+\infty.
}
\tag{26}
\]

For all sufficiently large `X`, (19) therefore applies and gives

\[
\boxed{
\sum_{\substack{p,q\in Q_X\\p\ne q}}
|\widehat\eta_{Q_X}(e_p-e_q)|^2
\ge(S_{Q_X}-1)^2
\asymp_{\delta,C}\log^2X.
}
\tag{27}
\]

All frequencies in (27) lie inside the fixed interval `(-epsilon,epsilon)` by (23). This proves (3).

No theorem about primes in genuinely short additive intervals is being used. The shell has fixed multiplicative width, so the ordinary prime number theorem is enough.

There is also no exact nontrivial zero Kronecker frequency: unique factorization implies `E(alpha)=0` only for `alpha=0`. The obstruction is instead an accumulation of distinct mixed-prime frequencies arbitrarily close to zero in the cylindrical limit.

## 3. Every spectral geometry nondegenerate at zero pays infinite cost

Let `w` be nonnegative and continuous at zero with `w(0)>0`. There exist `epsilon>0` and `c_w>0` such that

\[
w(t)\ge c_w
\qquad(0\le t<\epsilon).
\tag{28}
\]

Take the shell `Q_X` above. Since every term in (4) is nonnegative, retaining only the pair-difference modes gives

\[
\mathcal Q_{w,Q_X}(\eta_{Q_X})
\ge
c_w
\sum_{\substack{p,q\in Q_X\\p\ne q}}
|\widehat\eta_{Q_X}(e_p-e_q)|^2.
\tag{29}
\]

Equation (27) makes the right side tend to infinity, proving (5).

For every real `s`, the inhomogeneous symbol `(1+t^2)^s` is continuous and equals one at zero, so (6) follows immediately. Negative Sobolev order can suppress large `|E(alpha)|`, but it cannot suppress the positive mass forced into arbitrarily low mixed-prime frequencies.

This exactly complements `WP-109`. The one-prime axes show that any regular spectral multiplier which decays no faster than `t^{-2}` at **high** Kronecker frequency has infinite critical cost. The present result shows that even arbitrarily strong high-frequency smoothing does not help when the multiplier remains nondegenerate at **zero**.

## 4. This strictly upgrades the correlated-completion boundary

The previous chain separates three increasingly broad statements.

`WP-110` uses the independent product formula, so every two-prime coefficient factors. `WP-113` allows arbitrary finite blocks and convex weights, but still uses product factorization inside each block. Its sharper class-specific estimate is

\[
M_Q\ge S_Q^2-\frac14S_Q.
\tag{30}
\]

The present estimate

\[
M_Q\ge(S_Q-1)^2
\tag{31}
\]

is asymptotically of the same quadratic order but is deliberately weaker at finite `S_Q`; in exchange it assumes **nothing** about how the completion was built. It applies to every positive measure with the required first moments, including the Haar-equivalent correlated completion of `WP-101` and any future non-product completion on the same prime-torus state space.

This also sharpens `WP-096`. That finding proves that deleting all mixed-prime coefficients while keeping the exact critical rays requires divergent diagonal mass. Equation (19) says more: at fixed finite mass, positivity quantitatively forces a growing Hilbert--Schmidt amount of mixed-prime correlation, and ordinary prime density forces that amount into near-zero multiplicative-flow frequencies.

The result is independent of absolute continuity. Singular measures, endpoint-rough Haar-equivalent densities, and bounded-below correlated densities all obey the same finite-marginal covariance inequality.

## 5. Matched controls and falsifiers

### Supercritical attenuation removes the shell explosion

Replace (1) by the attenuated first moments

\[
\widehat\mu_\sigma(e_p)=-\frac{\log p}{p^\sigma},
\qquad\sigma>\frac12.
\tag{32}
\]

Then on the same fixed-width shell,

\[
S_{Q_X}(\sigma)
=\frac1{C^2}
\sum_{p\in Q_X}
\frac{(\log p)^2}{p^{2\sigma}}
=O_{\delta,C}\!\left(
X^{1-2\sigma}\log X
\right)
\longrightarrow0.
\tag{33}
\]

So the covariance bound becomes trivial rather than divergent. This agrees with the explicit supercritical positive product completions already used as matched controls in `WP-109` and `WP-112`. The low-frequency explosion is tied to the critical `sigma=1/2` prime-density boundary.

### Sparse generalized generators do not reproduce the obstruction

For a free multiplicative system with generator energies `E_j` and critical-looking amplitudes `E_je^{-E_j/2}/C`, the same covariance argument replaces (26) by the squared-amplitude mass inside a fixed-width energy window. If `E_j=j`, such a window contains only `O(1)` generators and its total squared amplitude tends exponentially to zero. Thus the shell step fails.

The covariance theorem is universal, but the divergence in (3) uses a real arithmetic feature: ordinary prime energies `log p` become densely packed while their critical squared amplitudes retain total mass of order `log X` on a fixed multiplicative prime shell. This is still not RH-specific evidence, but it is stronger than a generic free-monoid pathology.

### A zero-frequency-degenerate multiplier remains logically open

Equation (5) requires a positive lower bound for `w` near zero. A homogeneous or otherwise degenerate multiplier with `w(0)=0` is not ruled out by this finding. Such a symbol must simultaneously survive the high-frequency axis obstruction of `WP-109`; choosing a bespoke multiplier merely to vanish on near-resonances and decay on the prime axes would be a hand-picked kernel unless Mathia independently forces it.

### Changing the architecture before positivity remains open

The theorem starts from a fixed positive prime-torus completion carrying (1). A genuinely nonseparable finite--archimedean object may change the observable space, state, or operator **before** a positive spectral form is formed and therefore fall outside the hypotheses. Likewise a cohomological quotient, boundary response, or signed/renormalized construction is not excluded merely because its finite shadow can later be compared with prime-torus moments.

A shell-dependent total mass is not an escape for a single global completion: `C` in (1)--(2) is the fixed finite mass of one measure. Allowing `C` to grow with the finite prime set changes the object rather than constructing a finite global positive state.

## 6. Prior-art and novelty audit

The ingredients of the proof are classical and no theorem-level novelty is claimed for them.

- Positivity of `R-mm^*` is the ordinary covariance-matrix theorem for complex random variables.
- The estimate from (16) to (19) is Cauchy--Schwarz applied to a correlation Gram matrix; it lies in the same broad finite-dimensional Gram/frame-potential family as classical correlation bounds such as Welch-type estimates.
- Interpreting `R_{pq}` as torus Fourier coefficients is standard harmonic analysis/Bochner theory.
- The shell growth (24)--(26) is an elementary consequence of the prime number theorem.

A bounded literature audit of positive-definite functions on locally compact groups, correlation/Gram matrix bounds, covariance matrices, and frame-potential/Welch inequalities found these standard ingredients but no reason to identify (3) with an established Weil-positivity theorem. The result should therefore be read only as a Mathia-specific composition of classical facts forced by the already-established exact critical prime moments.

The conclusion is also not a hidden RH-equivalent criterion. It uses no zeta zeros, no functional equation, no Weil kernel, and no assumed global sign theorem. It is a **negative architecture theorem**: ordinary positivity of the finite completion itself creates low-frequency mixed-prime mass too large for a nondegenerate Kronecker spectral energy.

## Research consequence

The arbitrary-correlation spectral branch is now substantially narrower. Combining `WP-109` with the present result gives a two-ended obstruction:

\[
\boxed{
\begin{array}{c}
\text{high prime-axis frequencies require stronger-than-}t^{-2}\text{ damping,}\\[2mm]
\text{while near-zero mixed-prime frequencies require }w(t)\to0\text{ at }t=0.
\end{array}
}
\tag{34}
\]

Every inhomogeneous Sobolev/resolvent scale fails because its symbol stays positive at zero, no matter how negative the order. A surviving spectral sign mechanism would therefore need an independently forced geometry that is simultaneously high-frequency smoothing and zero-frequency degenerate, and it would still have to generate the archimedean Gamma term, polar/global counterterms, and the exact Weil test-function pairing from the same structure.

The more structural surviving route remains the one already isolated by the line: couple the finite and archimedean sectors or change the cohomological/boundary category **before** the final positivity theorem, rather than trying to repair a completed critical prime-torus state by another ordinary positive spectral norm.