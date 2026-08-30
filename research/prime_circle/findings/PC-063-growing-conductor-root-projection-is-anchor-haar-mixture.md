# PC-063 — growing-conductor root projection has only an anchor/Haar crossover

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the growing-conductor additive-Fourier escape explicitly left open by PC-061.

## Claim

PC-060 identifies the normalized escaped radial spectral mass with the logarithmic-series probability law

\[
\bar\nu_x=\frac1{L(x)}\sum_{n\ge1}\frac{x^n}{n}\,\delta_n,
\qquad
L(x)=-\log(1-x),
\qquad 0<x<1.
\]

PC-061 proves that every **fixed** finite-conductor additive character tends to its Haar value as `x -> 1^-`, but leaves open the possibility that a conductor growing with the boundary scale retains nontrivial arithmetic information.

For the canonical prime-circle projection to a growing `q`-gon, this escape can be classified exactly. Push `\bar\nu_x` to the unit circle by

\[
n\longmapsto e^{2\pi i n/q(x)}
\]

and call the resulting probability measure `\eta_{x,q}`. Assume `q(x) -> infinity` and

\[
\boxed{
\frac{\log q(x)}{L(x)}\longrightarrow\beta\in[0,\infty].
}
\]

Then

\[
\boxed{
\eta_{x,q}\Longrightarrow
c_\beta\,\delta_1+(1-c_\beta)m_{S^1},
\qquad
c_\beta=\min(1,\beta),
}
\]

where `m_{S^1}` is normalized Haar measure on the circle and `1` is the common anchored vertex.

Thus allowing the Fourier conductor to grow does not expose a new spectral object. Every power-law scale coupling produces only an elementary interpolation between the two structures already intrinsic to the original picture: the common anchor and uniform circle measure. At the geometrically natural angular resolution `q \asymp (1-r)^{-1}` for the radial parameter `x=r^2`, the limit is the **pure anchor** `\delta_1`.

## 1. The exact moving-character transform

For any angle `\theta` define the additive character `n -> e^{in\theta}`. The logarithmic power series gives the exact characteristic function

\[
\boxed{
\Phi_x(\theta)
:=\int e^{in\theta}\,d\bar\nu_x(n)
=\frac{-\Log(1-xe^{i\theta})}{L(x)}.
}
\]

The branch of `Log` is the one selected by the convergent power series for `x<1`. Its modulus is controlled by the exact identity

\[
\boxed{
|1-xe^{i\theta}|^2
=(1-x)^2+4x\sin^2(\theta/2).
}
\]

Put `\varepsilon=1-x=e^{-L(x)}` and

\[
a_x(\theta):=
\frac{-\log\!\bigl(2|\sin(\theta/2)|\bigr)}{L(x)}
\]

when the sine is nonzero. If along a sequence `\theta=\theta_x` the limit `a_x(\theta_x) -> \alpha` exists in `[0,infinity]`, then the preceding two-term competition gives

\[
\boxed{
\Re\Phi_x(\theta_x)\longrightarrow\min(1,\alpha).
}
\]

The imaginary part is bounded in absolute value by `\pi/L(x)`, hence tends to zero. Therefore

\[
\boxed{
\Phi_x(\theta_x)\longrightarrow\min(1,\alpha).
}
\]

This includes PC-061 as the case of a fixed nontrivial character: then `\alpha=0` and the coefficient tends to zero. The trivial character has coefficient identically one.

The formula also shows why conductor growth by itself is not arithmetic information. Only the angular distance of the character from the trivial mode matters, and it enters through one logarithmic scale ratio.

## 2. Growing `q`-gons converge only to anchor/Haar mixtures

For the root-of-unity projection `n -> e^{2\pi i n/q}`, the `k`-th circle Fourier coefficient is

\[
\widehat\eta_{x,q}(k)
=
\frac{-\Log(1-xe^{2\pi i k/q})}{L(x)}.
\]

Fix `k != 0`. Since `q -> infinity`,

\[
2\left|\sin\frac{\pi k}{q}\right|
\sim\frac{2\pi|k|}{q},
\]

so

\[
\frac{-\log\!\left(2|\sin(\pi k/q)|\right)}{L(x)}
\longrightarrow\beta.
\]

Hence every fixed nonzero Fourier coefficient has the same limit

\[
\boxed{
\widehat\eta_{x,q}(k)\longrightarrow c_\beta:=\min(1,\beta),
\qquad k\ne0,
}
\]

while `\widehat\eta_{x,q}(0)=1`. These are exactly the Fourier coefficients of

\[
c_\beta\delta_1+(1-c_\beta)m_{S^1}.
\]

Trigonometric polynomials are dense in `C(S^1)`, so Fourier convergence identifies the weak limit uniquely and proves the claim.

The regimes are therefore completely elementary:

\[
\begin{array}{c|c}
\log q=o(L) & \eta_{x,q}\Rightarrow m_{S^1}\\
\log q\sim\beta L,\ 0<\beta<1 & \eta_{x,q}\Rightarrow\beta\delta_1+(1-\beta)m_{S^1}\\
\log q\ge (1+o(1))L & \eta_{x,q}\Rightarrow\delta_1.
\end{array}
\]

No intermediate limit contains a new arithmetic spectral measure.

## 3. The same crossover is the log-scale law of the escaped integer mass

There is a direct probabilistic interpretation. Let `N_x` have the PC-060 normalized atom law

\[
\Pr(N_x=n)=\frac{x^n}{nL(x)}.
\]

For `0<u<1`, with `M_x=\lfloor(1-x)^{-u}\rfloor`, one has uniformly on `n<=M_x`

\[
x^n=1+o(1),
\]

and therefore

\[
\Pr(N_x\le M_x)
=\frac{\sum_{n\le M_x}x^n/n}{L(x)}
\longrightarrow u.
\]

The endpoints follow from monotonicity and the exponentially cut-off tail. Thus

\[
\boxed{
\frac{\log N_x}{L(x)}\Longrightarrow\operatorname{Unif}[0,1].
}
\]

The coefficient `c_\beta` is consequently the fraction of logarithmic scales on which `N_x` is still smaller than the growing modulus `q\asymp e^{\beta L}`. The anchor/Haar mixture is a scale-resolution crossover of the classical log-series law, not an independently generated zeta phenomenon.

## 4. The geometrically matched boundary layer is also elementary

The prime-circle radial kernel uses `x=r^2`. Near the unit circle,

\[
1-x=1-r^2\sim2(1-r),
\]

so the natural comparison between angular mesh and radial boundary distance is

\[
q(1-r)=O(1),
\]

equivalently `q(1-x)=O(1)`. This has `\log q/L(x) -> 1`, and the normalized projected measure therefore collapses to the common anchor.

Even the first centered correction carries no hidden arithmetic. If

\[
q(x)(1-x)\longrightarrow c\in(0,\infty)
\]

then for every fixed integer `k`,

\[
1-xe^{2\pi i k/q}
=(1-x)\left(1-\frac{2\pi i k}{c}+o(1)\right),
\]

hence

\[
\boxed{
-\Log(1-xe^{2\pi i k/q})-L(x)
\longrightarrow
-\Log\!\left(1-\frac{2\pi i k}{c}\right).
}
\]

So retaining the `O(1)` boundary-layer profile after the leading anchor collapse yields only an elementary logarithmic function of the mesh ratio and Fourier index. There is still no free zeta spectral parameter, gamma factor, `s <-> 1-s` symmetry, or distinguished `Re(s)=1/2`.

## 5. Prior art and novelty audit

No historical novelty is claimed for the analytic ingredients.

- The atom law `x^n/[nL(x)]` is the classical logarithmic-series distribution, already identified and sourced in PC-060 to Fisher, Corbet and Williams (1943).
- Its probability/characteristic generating function is immediately the classical logarithmic series `-Log(1-xz)/L(x)`.
- Root-of-unity filtering and characterization of Haar measure by nontrivial Fourier coefficients are standard compact-abelian harmonic analysis, already used in PC-061.
- Targeted searches around logarithmic-series characteristic functions, root-of-unity evaluations, and logarithmic/arithmetic residue laws found the ambient formulas in the standard probability/harmonic-analysis setting, not an independent RH mechanism. The limit theorem above is therefore presented only as the project-specific classification of the explicit escape route left by PC-061.

The important content for Mathia is negative: once the PC-060 mass has collapsed to the classical log-series law, **letting the finite conductor track the radial boundary does not restore lost prime-circle arithmetic**. The only weak limits forced by the one-character/full-quotient projection are mixtures of the anchor and Haar background.

## 6. Boundaries of the obstruction

PC-063 does not rule out every construction involving a growing finite quotient. It rules out the canonical additive projection of the exact PC-060/061 normalized radial spectral mass and any conclusion based only on its individual moving additive Fourier modes.

Still outside the theorem are nonlinear joint statistics of a growing family of modes, operators coupling different levels before the log-series collapse, genuinely two-dimensional kernels outside the PC-058 divisor-Haar algebra, non-scalar renormalizations forced independently by geometry, and the global primitive-root uniformization/accessory branch of PC-017. Those would need their own derivation and novelty audit; merely choosing a more elaborate conductor schedule would be an external scale wrapper.

## 7. Exact audit tests

The result has several direct falsifiers:

1. verify the exact transform `Phi_x(theta)=-Log(1-xe^{i theta})/L(x)` from the atom law;
2. verify `|1-xe^{i theta}|^2=(1-x)^2+4x sin^2(theta/2)` and the bounded argument term;
3. for any integer sequence `q(x)->infinity` with `log q/L -> beta`, check that every fixed nonzero Fourier mode tends to `min(1,beta)`;
4. identify the unique probability measure with Fourier coefficients `1` at zero and `c` at every nonzero integer as `c delta_1+(1-c)m_{S^1}`;
5. for `0<u<1`, check the harmonic-sum asymptotic giving `Pr(log N_x/L <= u)->u`;
6. in the matched layer `q(1-x)->c`, expand the exact logarithm and recover the centered profile `-Log(1-2 pi i k/c)`.

Failure of any of the first four identities would invalidate the anchor/Haar classification. A different limit can evade the result only by changing the observable or introducing additional structure before this canonical projection.
