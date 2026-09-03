# MC-035 — Log-radial Fourier analysis of the Huxley–Watt annulus has an RH-equivalent zero mode

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/BOUNDARY`, `RH-EQUIVALENT-BOUNDARY`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The deterministic parity-correlation frontier isolated in `MC-033` and `MC-034` admits a natural multiplicative-frequency coordinate, because both the reciprocal Huxley–Watt phase and the central-divisor threshold are functions of the product ratio `q/N^2`. However, decomposing the source-prescribed sawtooth kernel into Fourier modes of the logarithmic product coordinate does **not** remove the coarse Mertens burden: its zero log-frequency component is itself RH-equivalent at the required square-scale power.

Let

\[
S_H(x)=\sum_{h=1}^H\frac{\sin(2\pi h x)}{\pi h},
\qquad 1\le H\le N,
\tag{1}
\]

be the finite sawtooth Fourier kernel used in `MC-031`–`MC-034`, and put

\[
L=\log N,
\qquad
\Phi_{N,H}(u)=S_H(e^u),
\qquad 0\le u\le L.
\tag{2}
\]

Its zero Fourier coefficient in the log-radial coordinate is

\[
\alpha_{N,H}
:=\frac1L\int_0^L\Phi_{N,H}(u)\,du
=\frac1{\log N}\int_1^N S_H(x)\frac{dx}{x}.
\tag{3}
\]

For any integer schedule `H=H(N)` with `H(N) -> infinity`, one has

\[
\boxed{
\alpha_{N,H}
=\frac{C_\psi+O(H^{-1}+N^{-1})}{\log N},
\qquad
C_\psi=1-\frac12\log(2\pi)>0.
}
\tag{4}
\]

Numerically `C_psi = 0.0810614667...`, but (4) is an exact asymptotic consequence of the classical sawtooth Fourier series and Stirling's formula, not a numerical observation.

Now let

\[
c_N(q)=\sum_{\substack{mn=q\\m,n\le N}}\mu(m)\mu(n)
\tag{5}
\]

be the finite-cutoff product coefficient from `MC-032`, and define

\[
M_2(N):=\sum_{q\le N}(\mu*\mu)(q).
\tag{6}
\]

The total product-fiber sum is exactly

\[
\sum_{q\le N^2}c_N(q)=M(N)^2,
\tag{7}
\]

while `c_N(q)=(mu*mu)(q)` for `q<=N`. Therefore

\[
\boxed{
\sum_{N<q\le N^2}c_N(q)=M(N)^2-M_2(N).
}
\tag{8}
\]

Consequently the zero log-frequency contribution to the annular Huxley–Watt aggregate is exactly

\[
\boxed{
\mathcal Z_0(N,H)
=\alpha_{N,H}\bigl(M(N)^2-M_2(N)\bigr).
}
\tag{9}
\]

The interior coefficient has the unconditional absolute bound already used in `MC-032`,

\[
|M_2(N)|
\le \sum_{q\le N}|(\mu*\mu)(q)|
=O(N\log N).
\tag{10}
\]

Because `alpha_(N,H)` is asymptotic to the **nonzero** constant `C_psi/log N`, the square-scale target

\[
\mathcal Z_0(N,H(N))=O_\varepsilon(N^{1+\varepsilon})
\quad\text{for every }\varepsilon>0
\tag{11}
\]

is equivalent to the Riemann hypothesis whenever `H(N)->infinity`.

Thus a multiplicative/log-radial Fourier attack on the accepted `CLUE-reciprocal-phase-prime-log-slab-coupling` cannot obtain the missing power gain by centering the source kernel and then bounding its zero mode independently. Subtracting the log-radial mean is an exact transfer of the burden into the coarse statistic `M(N)^2-M_2(N)`, whose target-scale bound is already RH-equivalent. A viable log-frequency continuation must instead prove **coupled signed cancellation between this zero mode and the nonzero log modes**, or derive the coarse term from independently weaker arithmetic information.

## 1. The source sawtooth has a nonzero logarithmic mean

For finite `H`, define the convergent improper integral

\[
C_H:=\int_1^\infty S_H(x)\frac{dx}{x}.
\tag{12}
\]

Since the sum in (1) is finite,

\[
C_H
=\sum_{h=1}^H\frac1{\pi h}
\int_1^\infty\frac{\sin(2\pi h x)}x\,dx.
\tag{13}
\]

Integration by parts gives, uniformly for `X>=1`,

\[
\left|\int_X^\infty\frac{\sin(2\pi h x)}x\,dx\right|
\ll \frac1{hX}.
\tag{14}
\]

Hence the weighted `h`-series has an absolutely summable `O(h^{-2})` majorant, so

\[
C_H=C_\infty+O(H^{-1}),
\tag{15}
\]

and the tail beyond `N` satisfies uniformly in `H`

\[
\int_N^\infty S_H(x)\frac{dx}{x}=O(N^{-1}).
\tag{16}
\]

It remains to identify `C_infinity`. The classical Fourier series gives, away from integers,

\[
\lim_{H\to\infty}S_H(x)=\frac12-\{x\}.
\tag{17}
\]

The partial harmonic sine sums are uniformly bounded; on every finite interval dominated convergence applies, while (14)–(16) make the improper tails uniform. Therefore

\[
C_\infty
=\int_1^\infty\left(\frac12-\{x\}\right)\frac{dx}{x}.
\tag{18}
\]

For an integer `R>=1`, splitting into unit intervals gives exactly

\[
\begin{aligned}
\int_1^{R+1}\left(\frac12-\{x\}\right)\frac{dx}{x}
&=\sum_{n=1}^R
\left[\left(n+\frac12\right)\log\frac{n+1}{n}-1\right]\\
&=\left(R+\frac12\right)\log(R+1)-\log(R!)-R.
\end{aligned}
\tag{19}
\]

Stirling's formula now yields

\[
C_\infty=1-\frac12\log(2\pi)=C_\psi>0.
\tag{20}
\]

Combining (12), (15), and (16) with (3) proves (4). In particular, every source-compatible polynomial truncation schedule from `MC-031`, such as `H=N^{1-delta}` for fixed positive `delta`, has the same nonvanishing logarithmic zero mode asymptotically.

## 2. The annular constant-kernel coefficient is `M(N)^2-M_2(N)`

Equation (7) is a finite identity:

\[
\begin{aligned}
\sum_{q\le N^2}c_N(q)
&=\sum_{m,n\le N}\mu(m)\mu(n)\\
&=M(N)^2.
\end{aligned}
\tag{21}
\]

On `q<=N` the separate cutoffs are inactive, so `MC-032` gives

\[
c_N(q)=(\mu*\mu)(q).
\tag{22}
\]

Subtracting the interior proves (8). Moreover

\[
\begin{aligned}
\sum_{q\le N}|(\mu*\mu)(q)|
&\le \sum_{ab\le N}|\mu(a)\mu(b)|\\
&\le \sum_{a\le N}\left\lfloor\frac Na\right\rfloor
=O(N\log N),
\end{aligned}
\tag{23}
\]

which proves (10) without any Möbius cancellation.

This is precisely the constant-radial-kernel specialization of the annular weights in `MC-034`. If one writes the source kernel as

\[
\Phi_{N,H}(u)=\alpha_{N,H}+\widetilde\Phi_{N,H}(u),
\qquad
\int_0^L\widetilde\Phi_{N,H}(u)\,du=0,
\tag{24}
\]

then the annular functional splits **exactly** as

\[
\mathcal A_{N,S_H}(\mu)
=\mathcal Z_0(N,H)
+\sum_{N<q\le N^2}c_N(q)
\widetilde\Phi_{N,H}\!\left(\log\frac{N^2}{q}\right).
\tag{25}
\]

No approximation or continuum replacement is involved in this centering. Thus choosing a zero-mean log-radial basis does not discard the coarse mode; it merely displays the explicit correction (9) that must be controlled or coupled back to the remaining modes.

## 3. Separate target-scale control of the zero mode is equivalent to RH

Assume first RH. The classical Mertens criterion gives, for every positive `eta`,

\[
M(N)=O_\eta(N^{1/2+\eta}).
\tag{26}
\]

Together with (10) and `alpha_(N,H)=O(1/log N)`, this implies (11), after choosing a smaller auxiliary exponent and absorbing logarithms.

Conversely, assume (11) for every positive `epsilon` along a schedule `H(N)->infinity`. Equation (4) gives, for all sufficiently large `N`,

\[
|\alpha_{N,H}|\ge \frac{C_\psi}{2\log N}.
\tag{27}
\]

Using (9)–(10),

\[
|M(N)|^2
\le |M(N)^2-M_2(N)|+|M_2(N)|
\ll_\varepsilon N^{1+\varepsilon}\log N+N\log N.
\tag{28}
\]

For any prescribed positive `delta`, apply (28) with a sufficiently smaller `epsilon` and absorb `log N` into `N^delta`. Then

\[
M(N)=O_\delta(N^{1/2+\delta}).
\tag{29}
\]

The classical Mertens criterion is therefore recovered, hence RH. This proves the claimed equivalence.

The role of `M_2(N)` is important: no RH-scale estimate for the convolution is needed. Its crude unconditional `O(N log N)` bound is already small enough relative to the square-scale target to prevent it from masking a large `M(N)^2` in a separately controlled zero mode.

## 4. Relation to the accepted reciprocal-phase / prime-log-slab clue

The log coordinate is not arbitrary decoration. In `MC-033`, writing `q=ab^2` gives the exact central-divisor occupancy

\[
R_N(a,b)
=\#\left\{\epsilon\in\{-1,+1\}^{\omega(a)}:
\left|\sum_{p\mid a}\epsilon_p\log p\right|
\le \log\frac{N^2}{q}\right\}.
\tag{30}
\]

Thus the same variable `u=log(N^2/q)` controls the shrinking prime-log slab, while the reciprocal Huxley–Watt kernel is `S_H(e^u)`. A Fourier analysis in `u` is therefore a source-natural way to ask whether slab occupancy couples to radial phase.

The present result kills only its **decoupled zero-mode version**. It does not show that the nonzero log frequencies are useless, nor that the complete Huxley–Watt annular aggregate is RH-equivalent term by term. Equation (25) permits cancellation between `Z_0` and the centered component, and such cancellation is exactly what a viable continuation would have to preserve rather than destroy by triangle inequality.

Relative to `MC-034`, the matched random multiplicative ensemble can still place the complete bounded-kernel annular functional at `N^(1+o(1))` RMS scale. The obstruction here is deterministic and representation-specific: the source kernel's logarithmic mean is nonzero, and the all-minus Möbius point couples that mean to an RH-equivalent coarse statistic if the mode is isolated.

## 5. Prior art and novelty assessment

The Huxley–Watt scale-doubling identity, sawtooth residual matrix, and additive Fourier truncation are classical prior art from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function* (2018), recorded as `MC-S24`. The finite-cutoff coefficient `c_N`, interior convolution identity, and annular localization are the current line's audited specializations from `MC-032`; the square-free product-fiber form and random multiplicative normalization are in `MC-033` and `MC-034`.

Fourier analysis after the change of variable `u=log x` is standard multiplicative harmonic/Mellin language. The sawtooth Fourier series, integration by parts, and Stirling evaluation in (17)–(20) are classical mechanisms. A targeted literature search around the Huxley–Watt formula, Mellin/logarithmic decompositions of its sawtooth kernel, and the exact constant in (18) did not locate a source that should be treated as a novelty claim for this specialization. None is made.

The durable contribution is the **line-specific information audit**: the most natural log-radial harmonic decomposition suggested by the current prime-log slab frontier has a provably nonzero zero mode; for the exact finite-cutoff annular coefficient that mode equals (9), and controlling it separately at the power needed by the scale-doubling identity is equivalent to RH.

## 6. Boundaries and decisive continuation

This finding does **not** prove a lower bound for the full annular Huxley–Watt functional. The zero log-frequency term can cancel against the centered/nonzero-frequency component in (25). It also does not prove that `M(N)^2-M_2(N)` alone is an RH-equivalent statistic without the `O_epsilon(N^(1+epsilon) log N)` scale specified above.

The negative conclusion applies to strategies that isolate or take absolute values over the log-radial zero mode. A different weighted log basis, nonlinear decomposition, or multiplicative coupling is not ruled out if it preserves the exact cancellation with the coarse piece instead of silently discarding it.

The decisive next test for the accepted reciprocal-phase clue is therefore sharper: derive arithmetic control of the **centered** log-radial occupancy/phase component together with an exact coupling law that forces cancellation against (9), or identify a source-natural nonzero-frequency statistic whose estimate produces the coarse coefficient from independently weaker arithmetic data. A proposal that simply removes the mean from `S_H(e^u)` and bounds the remainder has not solved the coarse problem; equation (25) records exactly where it went.

## Consequence for the research line

`MC-034` showed that the matched random multiplicative ensemble already has the correct power scale for the complete annular functional and reduced the live problem to deterministic parity correlation with the Huxley–Watt weights. `MC-035` now removes one natural harmonic shortcut for that correlation: multiplicative/log-radial Fourier coordinates do not make every mode cheap, because the source kernel has a fixed positive logarithmic mean and its zero mode carries an RH-equivalent Mertens-square statistic.

The surviving opportunity is **coupling**, not further scalarization. Any use of the joint prime-log slab and reciprocal phase must retain cancellation between coarse and detailed log-frequency information, or prove the coarse term from a genuinely weaker arithmetic input. This aligns the annular frontier with the earlier `MC-019` and `MC-020` lesson while identifying the exact coarse carrier specific to the current Huxley–Watt product annulus.