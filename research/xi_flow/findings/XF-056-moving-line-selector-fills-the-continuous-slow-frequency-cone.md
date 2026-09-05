# XF-056 — moving-line selector fills the continuous slow-frequency cone

**Status:** `EXACT-DERIVED` + `UNIFORM-CONTINUOUS-SELECTOR` + `SOURCE-SPECIFIC-TRANSPORT` + `MATCHED-CONTROL`. XF-055 shows that the moving-high-line argument excludes every **integer arithmetic harmonic** `1 <= ell <= C log log T` at the critical XF-047 gap amplitude. That still leaves a logical inverse-bridge loophole: a nonperiodic slow wave may be detuned from every center `2 pi ell/q` by more than the very narrow `1/M` index-frequency width of an individual XF-050 probe while having essentially the same Cauchy relaxation rate.

That loophole is not real. Harmonic quantization is used only by the periodic matched control, not by the Xi moving-line estimate. The same proof is uniform when the probe center moves **continuously** through the entire slow-frequency cone.

Use the XF-050/XF-055 scales

\[
\sigma_T=\frac{4\pi}{\log(T/4\pi)},
\qquad
q\asymp\log^2T,
\qquad
M=q^2,
\qquad
W=M\sigma_T\asymp\log^3T,
\tag{1}
\]

and fix `g` with `\widehat g=\chi\in C_c^\infty((-1,1))`. For fixed constants

\[
t_0>0,\qquad c>0,\qquad C>0,
\tag{2}
\]

let the **continuous index-frequency cone** be

\[
\Theta_T
:=
\left[
\frac{c}{q},
\frac{C\log\log T}{q}
\right].
\tag{3}
\]

For every `theta in Theta_T`, put

\[
\omega_{\theta,T}:=\frac{\theta}{\sigma_T}
\tag{4}
\]

and define

\[
f_{T,\theta}(x)
:=
g\!\left(\frac{x-T}{W}\right)
 e^{-i(\omega_{\theta,T}(x-T)+\varphi_{\theta,T})},
\tag{5}
\]

where the phases `varphi_{theta,T}` are arbitrary. If `mathcal Z_t` is the canonical positive-frequency Xi carrier of XF-051, set

\[
\mathcal S_{T,\theta}(t)
:=\frac1{2\pi}
\left\langle
\mathcal Z_t(\xi),
\widehat f_{T,\theta}(-\xi)
\right\rangle.
\tag{6}
\]

Then

\[
\boxed{
\sup_{0\le t\le t_0}
\sup_{\theta\in\Theta_T}
|\mathcal S_{T,\theta}(t)|
=o(1).
}
\tag{7}
\]

Thus the source selector is not a sparse collection of narrow bands centered only at the periodic harmonics. At the matched-statistic level it sweeps a **continuous** interval of slow positive frequencies. In particular, shifting a critical wave from `2 pi ell/q` by `Theta(1/M)`, `Theta(1/q^2)`, or any larger detuning that still remains in (3) cannot evade the selector merely by landing between the discrete XF-055 centers.

There is a matching nonperiodic control. For any `theta in Theta_T`, fix `kappa>0` and set

\[
a_\theta
:=
\frac{\sigma_T\kappa/q^2}
{2\sin(\theta/2)},
\tag{8}
\]

\[
z_j
=T+j\sigma_T
+a_\theta\sin(\theta j+\phi).
\tag{9}
\]

The gaps satisfy the exact identity

\[
\boxed{
\frac{z_{j+1}-z_j}{\sigma_T}
=
1+\frac\kappa{q^2}
\cos\!\left(\theta(j+\tfrac12)+\phi\right).
}
\tag{10}
\]

No periodicity or rationality of `theta/(2 pi)` is required. Choosing the probe phase to match the wave gives, uniformly throughout the cone,

\[
\boxed{
\left|
\sum_{j\in\mathbb Z} f_{T,\theta}(z_j)
\right|
=
\frac\kappa2+o(1).
}
\tag{11}
\]

Hence every pure critical slow wave in the cone — including irrational and deliberately detuned waves — has the same order-one separation from the actual Xi statistic as the periodic controls in XF-050/XF-055.

This still does **not** give the missing inverse theorem for an arbitrary nonlinear transition block. A configuration can distribute shape among frequencies, change phase across the `M`-site envelope, create sparse defects, or couple low and high gap geometry in ways not represented by one pure wave. What (7) removes is narrower and useful: **frequency detuning between the discrete periodic harmonics is no longer an admissible explanation for loss of the endpoint selector during the source-to-transition handoff.**

## 1. Every continuously moved band remains positive and prime-free

From (5),

\[
\widehat f_{T,\theta}(\xi)
=
W e^{-iT\xi-i\varphi_{\theta,T}}
\chi\!\left(W(\xi+\omega_{\theta,T})\right),
\tag{12}
\]

so `\widehat f_{T,theta}(-xi)` is supported in

\[
I_{T,\theta}
=
\left[
\omega_{\theta,T}-W^{-1},
\omega_{\theta,T}+W^{-1}
\right].
\tag{13}
\]

The two scale products that matter are exact:

\[
W\omega_{\theta,T}=M\theta,
\qquad
M=q^2.
\tag{14}
\]

At the lower edge of (3),

\[
M\theta\ge cq\to\infty,
\tag{15}
\]

so every interval (13) lies strictly in the positive half-line for large `T`. At the upper edge,

\[
\omega_{\theta,T}
=O\!\left(\frac{\log\log T}{\log T}\right)
=o(1),
\tag{16}
\]

uniformly. Therefore

\[
I_{T,\theta}\subset(0,\log2/2)
\tag{17}
\]

for all `theta in Theta_T` and sufficiently large `T`. The endpoint Guinand--Weil prime samples miss every moved band exactly, just as in XF-050. No discrete harmonic condition enters this support argument.

Notice what changes relative to XF-055. The band half-width in **index frequency** is

\[
\frac{\sigma_T}{W}=rac1M=\frac1{q^2},
\tag{18}
\]

while adjacent periodic centers are separated by `2 pi/q`. Thus the discrete family in XF-055 leaves large gaps between its individual bands. Equation (7) is precisely the statement that the center may be slid through those gaps without losing the Xi estimate.

## 2. The moving-high-line estimate is uniform in the continuous center

Fix `t_0` and use the same zero-free line as XF-054/XF-055,

\[
a_T=A\log T,
\tag{19}
\]

with fixed `A=A(t_0)>0` large enough for the reflected Euler-product comparison. Height independence of XF-051 gives

\[
\mathcal S_{T,\theta}(t)
=
\frac{i}{2\pi}
\int_{\mathbb R}
Q_{a_T}(x,t)
 f_{T,\theta}(x+i a_T)\,dx.
\tag{20}
\]

The shifted probe is

\[
f_{T,\theta}(x+i a_T)
=
e^{a_T\omega_{\theta,T}-i\varphi_{\theta,T}}
 g\!\left(
\frac{x-T}{W}+i\frac{a_T}{W}
\right)
 e^{-i\omega_{\theta,T}(x-T)}.
\tag{21}
\]

The upper edge of (3) gives

\[
a_T\omega_{\theta,T}
=O_{A,C}(\log\log T),
\tag{22}
\]

hence

\[
\boxed{
 e^{a_T\omega_{\theta,T}}
\le(\log T)^{K_{A,C}}
}
\tag{23}
\]

uniformly in the continuous center. Also

\[
\frac{a_T}{W}=O((\log T)^{-2}),
\tag{24}
\]

so all fixed derivatives of the shifted envelope remain uniformly Schwartz.

XF-054 proves, on `|x-T|<=T/2` and uniformly for `0<=t<=t_0`,

\[
Q_{a_T}(x,t)-Q^{\rm bg}_{a_T}(x,t)
=O\!\left(T^{-\kappa_A}(\log T)^B\right)
\tag{25}
\]

for some fixed `\kappa_A>0`. Multiplying by the worst height cost (23) and integrating over a width `W=Theta(log^3 T)` gives

\[
O\!\left(
W T^{-\kappa_A}
(\log T)^{B+K_{A,C}}
\right)
=o(1).
\tag{26}
\]

A fixed negative power of `T` beats every fixed polylogarithmic factor. The arithmetic part is therefore uniform over the whole continuum (3); no discretization or union bound over centers is needed.

## 3. Oscillatory cancellation is uniform down to the memory frequency

The deterministic background from XF-054 satisfies

\[
Q^{\rm bg}_{a_T}=O(\log T),
\qquad
\partial_x^kQ^{\rm bg}_{a_T}
=O_{k,t_0}\!\left(
\frac{(\log T)^{B_k}}{T^k}
\right).
\tag{27}
\]

Integrate (20) by parts `N` times against `e^{-i\omega_{theta,T}(x-T)}`. The worst term, with all derivatives on the envelope, is bounded by

\[
O_{N,A,C}\!\left(
(\log T)^{1+K_{A,C}}
W
(W\omega_{\theta,T})^{-N}
\right).
\tag{28}
\]

Equation (15) gives the uniform lower bound

\[
W\omega_{\theta,T}=M\theta\ge cq\asymp\log^2T.
\tag{29}
\]

Choosing one fixed `N` large enough after `A,C,c` makes (28) `o(1)` uniformly in `theta`. Every term with a derivative on `Q^{bg}` gains at least one factor `W/T`, up to fixed powers of `log T`, and is smaller.

Outside `|x-T|<=T/2`, the shifted envelope is uniformly Schwartz at real distance `Omega(T/W)`. The logarithmic derivative has only polynomial growth as in XF-051/XF-054, while the extra factor (23) is only polylogarithmic. A sufficiently large fixed Schwartz power therefore makes the tails `o(1)` uniformly.

Combining (26), (28), and the tails proves (7). The argument uses only the lower and upper frequency envelopes (15)--(16). It never asks that `q theta/(2 pi)` be an integer.

## 4. Arbitrarily detuned critical pure waves still give an order-one response

Take the finite-gap control (9). The exact gap identity (10) follows from

\[
\sin(\theta(j+1)+\phi)-\sin(\theta j+\phi)
=
2\sin(\theta/2)
\cos\!\left(\theta(j+\tfrac12)+\phi\right).
\tag{30}
\]

Thus the relative gap amplitude is exactly `kappa/q^2`, independent of `theta`. Since `theta=o(1)` uniformly on (3), all gaps are positive for large `q` and the position amplitude is small.

At the reference lattice points `T+j sigma_T`, Poisson summation gives

\[
\sum_j g(j/M)e^{-i\theta j}=0
\tag{31}
\]

and

\[
\sum_j g(j/M)e^{-2i\theta j}=0
\tag{32}
\]

for all sufficiently large `T`, uniformly in the cone. Indeed, `M theta>=cq->infinity`, while `theta->0`, so neither `theta` nor `2theta` lies within the `1/M` support window of a `2 pi` alias. The corresponding identities with `g'` also vanish because the Fourier transform of `g'` is `is chi(s)`.

Choose the harmless probe phase so that the constant term produced by multiplying the wave with `e^{-i theta j}` is positive. Taylor expansion around the lattice then gives the exact leading magnitude

\[
\frac12\omega_{\theta,T}a_\theta M
=
\frac\kappa2
\frac{\theta}{2\sin(\theta/2)}.
\tag{33}
\]

Since

\[
\sup_{\theta\in\Theta_T}\theta\to0,
\]

\[
\frac{\theta}{2\sin(\theta/2)}=1+o(1)
\tag{34}
\]

uniformly. The quadratic Taylor remainder is also uniform:

\[
\begin{aligned}
&M a_\theta^2
\left(
\omega_{\theta,T}^2
+\frac{\omega_{\theta,T}}W
+\frac1{W^2}
\right)\\
&\hspace{3cm}=O\!\left(\frac{\kappa^2}{q^2}\right)
=o(1).
\end{aligned}
\tag{35}
\]

Equations (33)--(35) prove (11).

A particularly direct stress test is

\[
\theta_T
=
\frac{2\pi}{q}+\frac{2\pi}{q^2}.
\tag{36}
\]

Its center is displaced from the first periodic harmonic by `2 pi/M`, already outside the index-frequency half-width `1/M` of that individual XF-055 band. Its Cauchy damping rate differs from the first harmonic only by a relative `O(1/q)`, yet (7) tests it at its own center and (11) gives the same order-one matched-control response. This is the minimal detuning loophole that the continuous theorem closes.

## 5. The continuum still covers the linearly slow Cauchy sector

XF-007 gives the infinite-lattice Cauchy symbol

\[
\rho(\theta)
=
\frac{\theta(2\pi-\theta)}{\sigma_T^2},
\qquad 0\le\theta\le2\pi,
\tag{37}
\]

for forward damping. Relative to the first periodic harmonic `2 pi/q`, define the effective harmonic number

\[
\nu:=\frac{q\theta}{2\pi}.
\tag{38}
\]

Using the XF-047 normalization `rho_{1,q}=1/4+o(1)`, one has uniformly for `theta=o(1)`,

\[
\boxed{
\rho(\theta)
=
\frac\nu4(1+o(1)).
}
\tag{39}
\]

The cone (3) is exactly

\[
\nu\in
\left[
\frac{c}{2\pi},
\frac{C}{2\pi}\log\log T
\right].
\tag{40}
\]

Hence the continuous selector covers every detuned mode with an order-one-or-polylogarithmic Cauchy damping rate in this range, not merely the modes whose effective harmonic number happens to be an integer. The spectral complement above a sufficiently large multiple of `log log T` remains on the strongly damped side of the XF-055 heat clock.

This does not settle frequencies `theta=o(1/q)`. Those have index wavelength longer than the fixed-time memory scale and interact with the translated source-counting/large-buffer regime rather than the discrete `q`-scale relaxation split. The present finding makes no claim that the same compact probe controls arbitrarily close to zero frequency.

## 6. Stress tests and evidence boundary

The theorem contains XF-055 as the discrete specialization `theta=2 pi ell/q`, up to harmless changes of the fixed constants defining the cone. The first nontrivial control is the detuned wave (36), which would fall between discrete band centers but is detected uniformly by (7). Irrational values of `theta/(2 pi)` provide a second control: no periodic cell exists, yet the matched response (11) is unchanged.

Several stronger statements remain open. Equation (7) is a uniform family of compact carrier pairings; it is **not** a pointwise support theorem for `mathcal Z_t` and it does not reconstruct an arbitrary gap field. A nonlinear nonperiodic block may carry a slowly varying phase, multiple overlapping frequencies, sparse microfolds, or window-scale cancellations. Turning the continuous source exclusion into an inequality for low transition-side gap energy is still the missing inverse step.

Likewise, nothing here proves the XF-031 mixed `L_lambda`/`L_w` product is positive, derives the borderline `M V_M=O(1)` gate, or crosses the transition using ordered gaps. XF-038 still supplies Cauchy form rigidity only after its source-side hypothesis has been obtained. The present theorem removes a spectral sampling artifact before that harder nonlinear handoff is attempted.

## 7. Prior-art and novelty boundary

The external ingredients are exactly those already anchored for XF-050--XF-055: Guinand--Weil, de Bruijn strip control, the Xi functional equation and Euler product, Stirling asymptotics, Gaussian heat propagation, and the half-plane Fourier--Laplace support principle. A targeted literature audit of de Bruijn--Newman heat-flow, logarithmic-derivative Fourier formulations, Guinand--Weil prime-free tests, and the Polymath15 high-zero framework did not locate this particular continuously swept shrinking-band statement.

No novelty is claimed for modulating a test function by a continuously varying frequency, Poisson summation, or Fourier diagonalization of the Cauchy lattice. The durable line-specific delta is the uniform scale coupling in (7): **the source-specific moving-line estimate is continuous in the matched slow frequency with enough uniformity to fill the gaps between the periodic XF-055 harmonics, while retaining order-one sensitivity to a critical pure gap wave at every such center.**

No new load-bearing external source is introduced, so `SOURCES.md` does not require modification.

## 8. Consequence for `xi_flow`

The source-to-transition bridge can no longer fail merely because the actual slow component is nonperiodic or slightly detuned from the arithmetic `q`-cell harmonics. The endpoint selector supplies a continuous low-frequency family, and the Cauchy clock assigns essentially the same damping rate to neighboring continuous frequencies.

The next constructive gate is therefore more specific than in XF-055: convert the **continuous** family (7), rather than only discrete harmonic samples, into low-frequency control of a real-simple transition-side gap or counting-displacement field on an interior memory-scale window. A positive inverse estimate may now use continuous Fourier/Plancherel localization without first paying an interpolation loss between harmonic centers. A decisive negative must exploit genuine nonlinear window-to-gap cancellation, an ultraslow `theta=o(1/q)` component, sparse geometry, or the mixed finite-gap operators; simple spectral detuning is closed.