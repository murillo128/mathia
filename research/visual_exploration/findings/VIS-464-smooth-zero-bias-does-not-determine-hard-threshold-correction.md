# VIS-464 — smooth zero-bias calibration does not determine the hard-threshold correction

**Evidence/status:** EXACT-DERIVED + CLASSICAL-SPECIALIZATION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM + NON-RH.

## Claim

The prime-axis correction of
[VIS-463](VIS-463-prime-only-shell-symmetry-erases-zero-resonance-bias.md)
cannot be transferred to a hard amplitude threshold merely from all
fixed smooth-test asymptotics and vanishing Haar boundary mass. This
remains false for a fixed two-prime ratio shell, a regular threshold,
uniformly bounded positive sampling densities, and a uniform linear
boundary-mass bound for the sampling laws themselves.

An explicit family below matches the classical correction for **every
fixed smooth torus test** with an `O(test-dependent constant / L^2)`
remainder. Every fixed mixed amplitude moment has zero `1/L` correction,
as required by prime-only symmetry. Nevertheless its low-tail probability
at squared amplitude `1/2` has the nonzero correction

\[
 \nu_L\{X\le\tfrac12\}-m\{X\le\tfrac12\}
 =\frac{a}{\pi}\arcsin\frac2L
 =\frac{2a}{\pi L}+O(L^{-3}),\qquad a=\tfrac14.       \tag{1}
\]

Here `m` is normalized Haar measure and `L>=16`; interpret `L=log T`
only to compare resolution with zero sampling. **These are constructed
measures, not the ordinates of zeta zeros.** The result refutes a
moment-to-threshold inference, not a number-theoretic threshold formula.
The leading `o(1)` tail-transfer statements in VIS-424/425/462 remain
valid; the distinction is the additional multiplication by `log T`.

A complementary smooth-density construction below matches an entire
growing harmonic bank **exactly**, including every mixed amplitude
moment of total degree at most `K`, yet leaves a threshold discrepancy
of order `1/K`. It retains a nonzero scaled correction when `K` is
proportional to `L`. A pointwise-bracket lower bound then shows why the
physical-frequency range of VIS-462 cannot alone implement (12) at
first-correction resolution, even if errors inside that range vanished.

## A fixed shell and its classical signed correction

On the torus of the primes `2,3`, write `z_p=exp(i theta_p)`, put
`lambda=log(2/3)`, and set

\[
 F(z)=e^{-i\lambda/2}z_2z_3^{-1}
       +e^{i\lambda/2}z_3z_2^{-1},\qquad
 X=|F|^2/4=\cos^2 v,\quad v=\theta_2-\theta_3-\lambda/2.
                                                               \tag{2}
\]

This is the prime-only `Y=x=2, H=1` strict near-band Wang shell up
to a positive scalar: its only oriented prime pairs are `(2,3)` and
`(3,2)`, and their equal sinc magnitudes cancel in normalization.
The exact supremum is `2`. The relative angle is uniform under `m`, so

\[
 X_*m(dx)=\rho(x)dx,\qquad
 \rho(x)=\frac1{\pi\sqrt{x(1-x)}},\quad 0<x<1.          \tag{3}
\]

In particular `t=1/2` is regular: `d(cos^2 v)/dv=-sin(2v)` is
nonzero on its four preimages. There is no atom or singular density at
the tested level.

For `r in (0,1)` let
`K_r(theta)=(1-r^2)/(1-2r cos(theta)+r^2)` be the Poisson kernel.
Define the bounded, mean-zero function

\[
 h(\theta_2,\theta_3)
 =-\sum_{p\in\{2,3\}}\log p\,[K_{p^{-1/2}}(\theta_p)-1]. \tag{4}
\]

Its absolutely convergent Fourier series gives, for any finite Laurent
polynomial `P=sum_m c_m z^m`,

\[
 \int Ph\,dm=-\mathcal B(P),\qquad
 \mathcal B(P)=\sum_{p=2,3}\sum_{k\ne0}
            c_{ke_p}\frac{\log p}{p^{|k|/2}}.             \tag{5}
\]

Thus `(1+h/L)m` encodes exactly the first correction in VIS-463.
It is a comparison density, not an asserted exact finite-height zero
law. Common-phase averaging shows `E_m[h | v]=0`: for fixed `v`,
both prime angles traverse complete circles. Hence

\[
 \int \phi(X)h\,dm=0                                      \tag{6}
\]

for every bounded measurable `phi`. This extends to every function
of finitely many fixed time-offset amplitudes, since those amplitudes
also depend only on `v`.

## Move a small amount of mass across the level

Set `delta=1/L` and

\[
 d_L(x)=\mathbf1_{(1/2-\delta,1/2)}(x)
        -\mathbf1_{(1/2,1/2+\delta)}(x),\qquad
 d\nu_L=[1+h/L+a d_L(X)]\,dm.                            \tag{7}
\]

The arcsine density is symmetric about `1/2`, so `int d_L(X) dm=0`
and `nu_L` has total mass one. With

\[
 C=\sum_{p=2,3}\frac{2\log p}{\sqrt p-1},
 \quad h\ge-C,\quad 1-C/16-a>0.353,
\]

the density is positive for all `L>=16`; it is also uniformly bounded
above. Consequently both `m` and `nu_L` give mass `O(epsilon)` to
`{|X-1/2|<epsilon}` uniformly in `L`, for sufficiently small
`epsilon`. Ordinary anti-concentration has not been discarded.

For a torus test `psi`, let
`A_psi(x)=E_m[psi | X=x]`. Near `1/2` this is the average of `psi`
over the common angle and the four smooth inverse branches of
`cos^2 v=x`, with equal branch weights. Thus `A_psi` is `C^1`
there whenever `psi` is `C^1`. Direct disintegration yields

\[
 \nu_L(\psi)-m(\psi)-L^{-1}m(\psi h)
 =a\int_0^\delta
    [A_\psi(1/2-s)-A_\psi(1/2+s)]\rho(1/2+s)\,ds
 =O_\psi(L^{-2}).                                      \tag{8}
\]

Every fixed character and every fixed mixed amplitude polynomial
therefore has the prescribed first correction. In fact the scaled
residual tends to zero for every fixed continuous torus test too:
replace the derivative bound in (8) by the modulus of continuity of
`A_psi` on this compact regular band. This stronger property belongs
to the constructed measures, not to an asserted zero theorem.

For powers of the amplitude there is the explicit estimate, `r>=1`,

\[
 |\nu_L(X^r)-m(X^r)|
 \le \frac{ar}{\pi\sqrt{1/4-L^{-2}}}\,L^{-2}.            \tag{9}
\]

It follows by the mean value bound
`|(1/2-s)^r-(1/2+s)^r|<=2rs` and (6). For example,

\[
 \nu_L(X)-m(X)=-\frac a\pi[1-\sqrt{1-4/L^2}].           \tag{10}
\]

For the hard event, however, the positive collar is retained and the
negative collar is discarded. Its extra mass is
`a int_0^delta rho(1/2+s) ds`, proving (1). Equation (6) says that
the classical signed-density prediction for this very event is zero.

## The missing boundary control

The signed residual measure
`eta_L=L(nu_L-m)-h m=a L d_L(X)m` tends weakly to zero, but its
total variation concentrates on the threshold boundary:

\[
 \|\eta_L\|_{\rm TV}
 =\frac{2aL}{\pi}\arcsin(2/L)\longrightarrow\frac{4a}{\pi}.
                                                               \tag{11}
\]

The norm here is total absolute mass, not half that mass. Haar assigns
zero mass to the boundary; this does not control the variation of the
**scaled signed residual** near it. In particular a probability-measure
continuity-set argument cannot simply be applied to `eta_L`.

A sufficient repair for a genuine sequence of sampling probabilities
`sigma_L` is to produce moving smooth brackets
`q_L^- <= 1_E <= q_L^+`, `0<=q_L^-<=q_L^+<=1`, such that

\[
 Lm(q_L^+-q_L^-)\to0,\qquad
 m(|h|(q_L^+-q_L^-))\to0,\qquad
 L[\sigma_L(q_L^\pm)-m(q_L^\pm)]-m(hq_L^\pm)\to0.      \tag{12}
\]

Positivity of `sigma_L` and the two bracket inequalities then squeeze
the desired corrected event probability. For an ordinary transition
collar of width `epsilon_L` at this regular level,
`epsilon_L=o(1/L)` suffices for the first condition. The last
condition is a theorem about **moving tests**; fixed-test asymptotics
do not supply it. No uniform growing-degree estimate is inferred from
the fixed-degree constants in VIS-463.

## Exact growing-bank matching still leaves threshold ambiguity

Write `theta=2v`, so `X=(1+cos(theta))/2` and the hard event is
`E={pi/2<=theta<=3pi/2}` modulo `2pi`. For an integer `K>=0`, let
`n` be the least odd integer greater than `K`, and let
`s_n=sin(n*pi/2)`, which is `+1` or `-1`. Using the same `h` and
`a=1/4`, define two comparison probabilities on the two-prime torus:

\[
 d\nu_{L,K}^{\pm}
  =[1+h/L\mp a s_n\cos(n\theta)]\,dm,\qquad L\ge16.       \tag{13}
\]

Both densities are smooth, normalized and bounded below by
`1-C/16-a>0.353`. Both satisfy the same uniform ordinary boundary-mass
bound as the collar construction. Conditional Haar averaging gives
`E_m[h | theta]=0`, so their angle marginals have densities
`1 \mp a s_n cos(n theta)` relative to uniform angle measure.

Their only Fourier differences from `(1+h/L)m` are at the torus
characters `m=+/-2n(e_2-e_3)`. Hence every angular trigonometric test
of degree at most `K` agrees **exactly** with the baseline. This includes
every product of fixed-offset squared amplitudes of total degree at
most `K`: each factor is `(1+cos(theta+omega u))/2`, with
`omega=2log(3/2)`, and a product of total degree `R` has angular
Fourier support in `[-R,R]`. The offsets can vary; support is unchanged.
Nevertheless, direct integration gives

\[
 \nu_{L,K}^{\pm}(E)-m(E)=\pm\frac{a}{\pi n}.             \tag{14}
\]

Indeed `m(E)=1/2`, `m(h 1_E)=0`, and
`int_E cos(n theta) dtheta/(2pi)=-s_n/(pi n)`.
If `K=floor(cL)` for fixed `c>0`, then

\[
 L[\nu_{L,K}^{\pm}(E)-\tfrac12]
     \longrightarrow\pm\frac{a}{\pi c}.                 \tag{15}
\]

For every fixed smooth torus test, repeated integration by parts in
`theta_2` makes the difference from `(1+h/L)m` be `O_{psi,j}(n^{-j})`
for every fixed `j`. Thus with `K` proportional to `L`, every fixed
smooth-test remainder can be smaller than any prescribed inverse power
of `L`, while (15) survives. Unlike the collar model, the scaled signed
residual here has unbounded total variation, `2aL/pi`; no convergence
against **all continuous** tests is asserted for this second model.
The controls isolate different information failures, rather than
silently strengthening every property of the first model.

## The finite-band bracket resolution floor

Let real angular trigonometric polynomials `q^-`, `q^+` of degree
at most `K` obey `q^-<=1_E<=q^+`. Allow overshoot outside `[0,1]`,
so this is more permissive than insisting that each bracket be bounded
between zero and one. Set `g=q^+-q^-`. Then `g>=0` everywhere,
and continuity from the two sides of each jump forces
`g(pi/2)>=1` and `g(3pi/2)>=1`, regardless of the event's endpoint
convention. Define the even integer `M_K=2 ceil((K+1)/2)>K`.
The equally spaced quadrature rule starting at `pi/2` is exact for
every trigonometric polynomial of degree at most `K`, and includes
both jump points. Therefore

\[
 \int g\,\frac{d\theta}{2\pi}
 =\frac1{M_K}\sum_{j=0}^{M_K-1}
        g(\pi/2+2\pi j/M_K)
 \ge\frac2{M_K}.                                        \tag{16}
\]

Consequently `L m(q^+-q^-)->0` requires `K/L->infinity`.
This is a necessary condition, not a sufficient arithmetic estimate
and not a claim that the displayed finite-`K` constant is always optimal.

Adding torus coordinates does not evade (16). For any finite Laurent
brackets of the same event, conditionally average over Haar fibers of
`theta=2(theta_2-theta_3)-lambda`. This preserves order and the Haar
gap integral. A character survives precisely when its exponent is
`2k(e_2-e_3)`; every other prime coordinate and the common angle
average away, and the twofold relative-angle fiber removes odd
multiples of `e_2-e_3`. The surviving physical frequencies have
magnitude `|k| omega`.

Thus if the original brackets use only characters with physical
frequency at most `L/8`, their conditional averages have degree
`K<=floor(L/(8 omega))`. Equation (16) then implies

\[
 \liminf_{L\to\infty} Lm(q^+-q^-)
       \ge16\omega>0.                                  \tag{17}
\]

This is precisely the frequency range of the unconditional character
estimate in VIS-462. The first condition of (12) cannot hold within
that band, even if all its character errors were zero. The construction
(13) with `K=floor(L/(8 omega))` is a compatible information control:
its only residual characters lie just outside that physical band, so
**every** character inside the band on this two-prime torus matches the
signed-density baseline,
yet its scaled threshold correction tends to `+/-8a omega/pi`.

This closes only the proposed finite-band bracketing repair using the
current input. An enlarged band still needs moving-test error control;
conditional arithmetic cancellation, direct interval estimates, or
other information about the sampling measure may bypass this argument.
It is not a theorem that genuine zero ordinates have a nonzero residual.

The [Fourier-bank visualization](../visualizations/threshold-fourier-bank.md)
shows the exact matched moments, opposite threshold shifts and bracket
floor. Rational Laurent convolution verified 78 moment-support checks;
independent event quadrature agreed with (14) within `2.4e-16`, and
the equally spaced quadrature identity within `6.7e-16` on the stated
finite control panel. The proof, not these finite checks, gives the
growing-bank and multivariate statements.

## Controls and numerical audit

The [paired visualization](../visualizations/threshold-boundary-layer.md)
renders the exact density collar, CDF correction and moment errors.
Independent integration in the relative phase and in the arcsine
amplitude coordinate agreed within `4.5e-17` for
`L=16,24,32,64,128,256` and moments `r=0,1,2,3,8`, including the
hard event. Periodic quadrature reproduced the Poisson axis coefficients
through `k=8` within `4e-16`; the common-phase mean vanished within
`4.8e-16`. These are implementation checks, not the proof.

The effect is not caused by discontinuous sampling densities. Replace
`d_L(x)` by `b(L(x-1/2))`, where
`b(y)=-y exp(-1/(1-y^2))` for `|y|<1` and zero otherwise.
This smooth odd function has absolute value below one. Normalization,
positivity and (8) survive, while the scaled hard-event excess tends to
`(2a/pi) int_{-1}^0 b(y)dy>0`. The derivatives are not uniformly
bounded as `L` grows; that is precisely the unresolved resolution cost.
The step profile was retained in the image because (1) is closed form.

Changing the sign of `a` reverses the hard-event shift without changing
the fixed-test orders. Common phase shifts and relabelling the two
prime coordinates do not remove the boundary transport. Changing
color, grid density or vertical scaling cannot decide the result,
which is an exact mass integral.

## Prior art, delta and limits

Ford–Meng–Zaharescu, *Simultaneous distribution of the fractional parts
of Riemann zeta zeros*, BLMS 49 (2017), 1–9,
[Theorem 1, Corollary 1.1 and (1.3)](https://www.ford126.web.illinois.edu/wwwpapers/FMZ.pdf),
provide the smooth-test prime-resonant correction underlying (4)–(5).
That paper imposes Fourier decay and does not supply the hard-threshold
claim by a continuity-set argument.

Ford–Soundararajan–Zaharescu, *On the distribution of imaginary parts
of zeros of the Riemann zeta function, II*, *Mathematische Annalen*
343 (2009), 487–505, DOI `10.1007/s00208-008-0280-x`,
[§1, (1.4) and Conjecture 1](https://www.ford126.web.illinois.edu/wwwpapers/fsz.pdf),
explicitly separate smooth-test correction from an interval-indicator
assertion. This describes what that source establishes, not a claim
that its conjecture remains open after all subsequent literature.
Its section 2, proof of Theorem 1(ii) and Theorem 2, also uses classical
interval majorants/minorants with an inverse-degree integral gap and
separates the controlled Fourier range from higher modes. The resolution
tradeoff itself is therefore prior art. Equations (13)--(17) specialize
it to the normalized two-prime shell, give smooth positive exact-bank
controls and show by fiber averaging that extra torus coordinates do
not repair this particular threshold. They are elementary harmonic
analysis, not a new approximation theorem.

The measure-theoretic mechanism is classical weak-versus-setwise
convergence of signed corrections. For the underlying probability and
total-variation distinctions see Amir Dembo,
[Probability Theory, §3.2, Theorem 3.2.21 and Definition 3.2.22](https://adembo.su.domains/stat-310b/lnotes.pdf).
No new general convergence theorem or analytic number theory is claimed.
The local delta is an explicit regular prime-only shell countermodel
that retains the **whole** classical smooth-test correction, even with
`O_psi(L^-2)` error, yet defeats first-correction threshold transfer.

VIS-463's axis cancellation remains exact, and VIS-462's leading Haar
tail convergence is unaffected. These models do not obey or purport to
obey every arithmetic constraint on a zero sequence, estimates outside
their specified test banks, or a fixed single orbit sampling rule. They
therefore cannot demonstrate an actual zero anomaly or disprove an
arithmetic threshold theorem. Their consequence is narrower: calibrating a hard
low-tail residual at `1/log T` resolution requires a quantitative
boundary/moving-test input beyond the existing fixed-moment and
ordinary Haar boundary-mass gates. No new selector, RH implication,
or compute/formalization enrollment follows.
