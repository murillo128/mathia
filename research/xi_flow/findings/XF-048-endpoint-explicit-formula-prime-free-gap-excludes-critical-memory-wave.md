# XF-048 — endpoint explicit formula has a prime-free spectral gap that excludes the critical coherent memory wave

**Status:** `CLASSICAL-IDENTITY` + `LITERATURE+DERIVED` + `EXACT-DERIVED` + `SOURCE-SPECIFIC` + `STRUCTURAL/SELECTOR`. XF-047 shows that the universal logarithmic-particle dynamics admits a `q~log^2 T` coherent gap wave at relative amplitude `kappa/q^2` whose normalized-triple BV stays at the critical order throughout every fixed heat-time interval, while the counting information currently used by the line cannot see it. The missing question was whether the actual Xi source has a phase-sensitive constraint that the periodic matched control does not.

At the endpoint `t=0` there is such a constraint. The Guinand--Weil explicit formula gives the `H_0` zero measure an arithmetic Fourier spectrum whose first nonzero prime-power frequency, in the Rodgers--Tao zero coordinate `x=2 gamma`, is

\[
\omega_2=\frac{\log 2}{2}.
\]

The XF-047 memory frequency is only `Theta(1/log T)`. A Gaussian probe with physical width `Theta(log^3 T)` can therefore isolate that memory phase while its Fourier transform is exponentially small at every prime-power frequency. For the actual endpoint zero set the probe statistic is `o(1)`. For the critical coherent XF-047 wave the same statistic tends to a nonzero constant,

\[
-\frac{\sqrt{2\pi}}2\,\kappa.
\]

Consequently an exact critical memory wave cannot be inserted into the endpoint Xi zero configuration across a full source buffer (up to a slowly growing Gaussian-tail margin) without generating compensating low-frequency structure. This is a genuine Xi-specific selector: it does not come from counting, gap envelopes, or universal Cauchy repulsion. It does **not** yet close the dynamic argument, because the explicit formula is an endpoint `t=0` identity and does not itself propagate the filtered coefficient through `t<0`.

## 1. Exact explicit formula in the `H_0` zero coordinate

Assume the real-rooted endpoint regime needed to speak about an ordered `H_0` zero configuration; in particular this is legitimate inside the usual hypothetical `Lambda<0` contradiction regime. Write the nontrivial zeta zeros as

\[
\rho=\frac12+i\gamma,
\qquad
x=2\gamma,
\]

so the corresponding `H_0` zeros have mean spacing

\[
\sigma_T:=\frac{4\pi}{\log(T/4\pi)}.
\tag{1}
\]

For an admissible test `f` define

\[
\widehat f(\xi):=\int_{\mathbb R} f(x)e^{-i\xi x}\,dx.
\tag{2}
\]

Applying the classical Guinand--Weil formula to `h(r)=f(2r)` gives

\[
\boxed{
\begin{aligned}
\sum_{\gamma} f(2\gamma)
={}&f(i)+f(-i)\\
&-\frac1{4\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\left[
\widehat f\!\left(\frac{\log n}{2}\right)
+\widehat f\!\left(-\frac{\log n}{2}\right)
\right]\\
&+\frac1{4\pi}\int_{\mathbb R}f(x)\,
\Omega(x)\,dx,
\end{aligned}
}
\tag{3}
\]

where

\[
\Omega(x)
:=\operatorname{Re}\psi\!\left(\frac14+\frac{i x}{4}\right)-\log\pi.
\tag{4}
\]

The sum over `gamma` includes both signs and multiplicity. Stirling's expansion gives, uniformly for `x` in a window `|x-T|=o(T)`,

\[
\frac{\Omega(x)}{4\pi}
=
\frac1{4\pi}\log\frac{T}{4\pi}
+O\!\left(\frac{|x-T|}{T}\right)
+O(T^{-2})
=
\frac1{\sigma_T}
+O\!\left(\frac{|x-T|}{T}\right)
+O(T^{-2}).
\tag{5}
\]

The important source-specific fact is visible directly in (3): after the zero-frequency archimedean density, the arithmetic side is sampled only at

\[
\xi=\pm\frac{\log n}{2},
\qquad n\ge2.
\tag{6}
\]

There is therefore a fixed spectral gap between frequency zero and the first prime-power line `log 2/2`.

## 2. A memory-scale Gaussian probe is asymptotically prime-free

Take an integer

\[
q=q_T\asymp\log^2T,
\qquad
M:=q^2,
\qquad
W:=M\sigma_T,
\tag{7}
\]

and define

\[
\theta:=\frac{2\pi}{q},
\qquad
\omega:=\frac{\theta}{\sigma_T}
=\frac{2\pi}{q\sigma_T}
=\Theta\!\left(\frac1{\log T}\right).
\tag{8}
\]

Thus

\[
W\asymp\log^3T,
\qquad
W\omega=2\pi q\to\infty,
\qquad
\omega\to0.
\tag{9}
\]

For an arbitrary phase `phi`, use

\[
\boxed{
f_T(x)
:=
\exp\!\left(-\frac{(x-T)^2}{2W^2}\right)
\exp\!\left[-i\left(\omega(x-T)+\phi-\frac\theta2\right)\right].
}
\tag{10}
\]

Its Fourier transform is the explicit Gaussian

\[
\widehat f_T(\xi)
=
\sqrt{2\pi}\,W\,
 e^{-iT\xi-i(\phi-\theta/2)}
\exp\!\left(-\frac{W^2(\xi+\omega)^2}{2}\right).
\tag{11}
\]

Because `omega=o(1)`, every prime-power sample in (3) is separated from the center `-omega` by a fixed positive amount for all sufficiently large `T`. Hence

\[
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\left(
\left|\widehat f_T\!\left(\frac{\log n}{2}\right)\right|
+
\left|\widehat f_T\!\left(-\frac{\log n}{2}\right)\right|
\right)
=o(1).
\tag{12}
\]

In fact the first prime already pays `exp(-cW^2)` and the rest of the absolutely convergent Gaussian-in-`log n` tail is smaller still.

The pole terms are also negligible:

\[
|f_T(i)|+|f_T(-i)|
\le
\exp\!\left[-c\left(\frac{T}{W}\right)^2\right]
=o(1).
\tag{13}
\]

For the archimedean integral, split off the constant density `1/sigma_T`. The constant term contains

\[
\int_{\mathbb R}f_T(x)\,dx
=
\sqrt{2\pi}\,W\,
 e^{-i(\phi-\theta/2)}
 e^{-(W\omega)^2/2}
=o(T^{-A})
\tag{14}
\]

for every fixed `A`. The variation of the density over the Gaussian window is bounded without using oscillation:

\[
\int |f_T(x)|\,
O\!\left(\frac{|x-T|}{T}+T^{-2}\right)dx
=
O\!\left(\frac{W^2}{T}+\frac{W}{T^2}\right)
=o(1).
\tag{15}
\]

Substituting (12)--(15) into (3) yields the endpoint selector

\[
\boxed{
\sum_{\gamma} f_T(2\gamma)=o(1).
}
\tag{16}
\]

The negative-height zeros contribute only a Gaussian tail because the probe is centered at `T`; no symmetry assumption beyond the ordinary endpoint zero pairing is being used to manufacture cancellation.

## 3. The XF-047 critical wave has an order-one response

Now apply the same probe to the exact coherent geometry behind XF-047. Set

\[
\varepsilon:=\frac{\kappa}{q^2},
\qquad \kappa>0\ \text{fixed},
\tag{17}
\]

and define the periodic position wave on the source lattice by

\[
\boxed{
 z_j
:=
 T+j\sigma_T
 +a\sin\!\left(\theta j+\phi-\frac\theta2\right),
\qquad
 a:=\frac{\sigma_T\varepsilon}{2\sin(\theta/2)}.
}
\tag{18}
\]

This is exactly the gap wave, because

\[
z_{j+1}-z_j
=
\sigma_T\left(1+\varepsilon\cos(\theta j+\phi)\right).
\tag{19}
\]

The position amplitude is

\[
a
\sim
\frac{\sigma_T\varepsilon q}{2\pi}
=\Theta(\log^{-3}T),
\tag{20}
\]

which is why ordinary counting cannot see the phase.

First compare with the unperturbed lattice `T+j sigma_T`. Poisson summation and (11) show

\[
\sum_{j\in\mathbb Z}f_T(T+j\sigma_T)=o(1):
\tag{21}
\]

the zero reciprocal-lattice mode pays `exp[-(W omega)^2/2]`, while every nonzero reciprocal-lattice frequency is of order `1/sigma_T=Theta(log T)` and is even farther from the Gaussian Fourier center.

Taylor expand at the lattice points. Writing

\[
\varphi_j:=\theta j+\phi-\frac\theta2,
\tag{22}
\]

the main derivative contribution is

\[
\begin{aligned}
\sum_j f_T'(T+j\sigma_T)\,a\sin\varphi_j
={}&
-i\omega a
\sum_j e^{-j^2/(2M^2)}e^{-i\varphi_j}\sin\varphi_j
+o(1)\\
={}&
-\frac{\omega a}{2}
\sum_j e^{-j^2/(2M^2)}
+o(1).
\end{aligned}
\tag{23}
\]

The second harmonic in `e^{-2i varphi_j}` is exponentially small because its index frequency is `2theta` while the Gaussian envelope has width `M=q^2`; the derivative of the envelope has the same cancellation. Moreover

\[
\sum_j e^{-j^2/(2M^2)}
=\sqrt{2\pi}\,M+o(M),
\tag{24}
\]

and

\[
\omega a
=
\frac{\pi\varepsilon}{q\sin(\pi/q)}
=\varepsilon\bigl(1+O(q^{-2})\bigr).
\tag{25}
\]

Since `M epsilon=kappa`, equations (23)--(25) give

\[
\sum_j f_T'(T+j\sigma_T)\,a\sin\varphi_j
=
-\frac{\sqrt{2\pi}}2\,\kappa+o(1).
\tag{26}
\]

The quadratic Taylor remainder is lower order:

\[
\sum_j
\sup_{|u-(T+j\sigma_T)|\le a}|f_T''(u)|\,a^2
=
O(M\omega^2a^2)+o(1)
=O\!\left(\frac{\kappa^2}{q^2}\right)+o(1)
=o(1).
\tag{27}
\]

Combining (21), (26), and (27),

\[
\boxed{
\sum_{j\in\mathbb Z} f_T(z_j)
=
-\frac{\sqrt{2\pi}}2\,\kappa+o(1).
}
\tag{28}
\]

Thus the explicit-formula probe distinguishes the critical memory phase by an order-one amount even though every individual displacement is only `Theta(log^-3 T)` and every relative gap perturbation is only `Theta(log^-4 T)`.

## 4. The obstruction survives localization; it is not an artifact of the infinite periodic continuation

XF-047 correctly warns that its infinite periodic continuation is not a global Xi zero set. The probe above can be localized enough to remove that loophole.

Let

\[
B_T:=\sqrt{12\log\log T}.
\tag{29}
\]

Suppose a consecutive endpoint Xi block centered near `T` agrees with (18) for

\[
|j|\le B_T M,
\tag{30}
\]

or, more generally, differs there by a uniform positional error `o(a)`. The physical half-width is

\[
B_TW
=O\!\left(\log^3T\sqrt{\log\log T}\right)
=o(T),
\tag{31}
\]

so this is still a localized high-zero insertion. It is only a slowly growing multiple of the XF-047 source buffer, and the periodic matched control can be repeated over it without changing its local critical `M V_M` scale.

Classical zero counting gives `O(log T)` zeros per unit interval at height comparable with `T`. Hence the total absolute contribution of actual zeros outside the block to the Gaussian probe is

\[
O\!\left(
W\log T
\int_{B_T}^{\infty}e^{-u^2/2}\,du
\right)
=o(1),
\tag{32}
\]

and the same is true for the periodic comparison lattice. A uniform positional error `o(a)` changes the statistic by at most

\[
o(a)\sum_j|f_T'(T+j\sigma_T)|=o(1),
\tag{33}
\]

because `a` times the derivative mass is `Theta(M epsilon)=Theta(kappa)`.

Therefore a localized block satisfying (30) would force the actual Xi statistic to have the nonzero limit (28), contradicting the source identity (16). The failure is phase-sensitive, not a response to the artificial global mean density: the unperturbed source lattice itself has statistic `o(1)` by (21).

## 5. What this does and does not rule out

The result kills the **coherent pure memory wave** as a possible endpoint Xi block at the critical XF-047 amplitude. It also shows what any surviving near-buffer mechanism must do: if an order-`R^-2` slow mode reaches `t=0`, it needs compensating low-frequency content whose tapered explicit-formula statistic cancels the order-one signal. A mere correction to global density or to the `log(4pi)/log T` spacing normalization cannot do that, because those contributions are already `o(1)` in (15).

The endpoint is essential. Formula (3) comes from the Euler product and functional equation of zeta at `t=0`; the de Bruijn--Newman functions `H_t` for `t<0` do not come with the same prime-power explicit formula. Thus (16) is not, by itself, a differential inequality along the heat flow. A positive Xi-flow argument still has to show that the relevant tapered coefficient is transported to the endpoint with enough fidelity, or that near-buffer exchange cannot create the required compensating phase before `t=0`.

The theorem also does not prove `M V_M=o(1)` for an arbitrary endpoint block. BV can be carried by broadband, incoherent, or mutually cancelling modes that the single matched probe does not isolate. What has been removed is the specific coherent first memory mode used by XF-047 to show that universal Cauchy smoothing alone is insufficient.

There is no circular use of RH beyond the legitimate real-zero regime in which the block geometry is being tested. The explicit formula itself is unconditional as an identity over nontrivial zeta zeros. The assumption `Lambda<0` is used only to identify the endpoint zeros with an ordered real `H_0` configuration, exactly as required by the surrounding Rodgers--Tao-style contradiction framework.

## 6. Prior art and novelty boundary

The Guinand--Weil explicit formula and the occurrence of prime powers at Fourier frequencies `log n` are classical. In the `H_0` coordinate `x=2 gamma`, the rescaling to frequencies `(log n)/2` is immediate. No novelty is claimed for this spectral gap, for Gaussian test functions, or for Poisson summation on the comparison lattice.

Primary anchors are A. P. Guinand, **A summation formula in the theory of prime numbers**, *Proceedings of the London Mathematical Society* (2) 50 (1948), 107--119, and Andre Weil, **Sur les "formules explicites" de la theorie des nombres premiers**, *Communications du Seminaire Mathematique de l'Universite de Lund*, Tome Supplementaire (1952), 252--265.

The Mathia-local content is the scale match with XF-047: the slow mode has physical frequency `Theta(1/log T)`, its critical amplitude produces an order-one tapered zero statistic over `W=Theta(log^3 T)`, and that whole Fourier packet sits asymptotically below the first prime-power frequency. A targeted literature search did not identify this specific coupling to the de Bruijn--Newman memory-mode obstruction; absence of a match is not used as evidence of general novelty.

## 7. Consequence for `xi_flow`

XF-046 removed the genuinely remote tail at the critical `R^-2` scale. XF-047 then showed that counting plus universal nonlinear Cauchy damping still permits a coherent memory wave at exactly that scale. XF-048 supplies the first source-specific phase selector for that obstruction: **the endpoint zeta explicit formula forbids the coherent wave from occupying the full source buffer without compensating spectral content.**

The frontier is therefore narrower than "find any Xi-specific statistic." The next useful dynamic gate is to control the evolution of a tapered memory-frequency coefficient from the real-simple `t<0` regime to `t=0`, including near-buffer exchange. If that coefficient cannot be cancelled at order one, (16) kills the XF-047 slow mode. If it can, the cancellation mechanism itself identifies the source-compatible forcing that a final coercive argument must control.