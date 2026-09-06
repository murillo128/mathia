# PL-181 — Almost-all short-interval PNT pushes Kronecker affine flattening to the `X^(13/15)` frequency horizon

## Claim

`PL-180` leaves the super-mesoscopic regime `|t|h/X -> infinity` open for the canonical vertical/Kronecker character after fixing one prime source `r` and broadly averaging the moving prime `q`. The current almost-all prime number theorem in short intervals closes a large polynomial part of that regime.

Fix a prime `r`, put `h=r-1`, and define

\[
B_X(t)
:=
\frac1{\pi(X)}\sum_{q\le X\atop q\ \mathrm{prime}}
\exp\!\left(it\log\left(1+\frac hq\right)\right).
\]

For real `tau` let

\[
J(\tau)
:=
\int_0^1 e^{i\tau/u}\,du
=
\int_1^\infty e^{i\tau v}v^{-2}\,dv.
\]

Then for every fixed `eta>0`, with `r` fixed,

\[
\boxed{
\sup_{|\tau|\le X^{13/15-\eta}}
\left|
B_X\!\left(\frac{X\tau}{h}\right)-J(\tau)
\right|
\longrightarrow0.
}
\]

Consequently, whenever

\[
\tau_X:=\frac{h t_X}{X},
\qquad
|\tau_X|\longrightarrow\infty,
\qquad
|\tau_X|\le X^{13/15-\eta},
\]

one has

\[
\boxed{B_X(t_X)\longrightarrow0.}
\]

Thus the bare fixed-source Kronecker phase is not merely PNT-universal at bounded and first-mesoscopic time as in `PL-180`: it remains forced to the same continuum profile throughout a polynomially super-mesoscopic window, corresponding to

\[
|t|\le h^{-1}X^{28/15-\eta}.
\]

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-REDIRECT`. The deep input is Guth--Maynard's published almost-all prime number theorem in intervals of length `X^(2/15+epsilon)`. The passage from that theorem to the displayed affine-phase limit is an elementary short-interval quadrature argument. No novelty is claimed for the Guth--Maynard theorem, the continuum kernel `J`, or the general principle that local equidistribution controls slowly varying prime weights. The durable Mathia-specific consequence is the closure of most of the explicit high-frequency escape left open by `PL-180`.

## 1. Exact phase inherited from the oriented affine plaquette

For the vertical character

\[
f_t(m)=m^{it}
=\exp\!\bigl(it\langle v(m),(\log p)_p\rangle\bigr),
\]

`PL-180` derives, after fixing the source prime `r` and removing the known source phase `r^{-it}`, the exact residual

\[
\left(1+\frac hq\right)^{it},
\qquad h=r-1.
\]

Nothing below changes that arithmetic reduction. The only question is how rapidly the phase may oscillate with the moving prime `q` before the broad prime average ceases to be controlled by known local prime-density theorems.

Write

\[
\phi_{X,t}(x)
=t\log\left(1+\frac hx\right).
\]

Its derivative is exact:

\[
\phi'_{X,t}(x)
=-\frac{t h}{x(x+h)}.
\]

Hence on any dyadic block `x asymp X`, the phase variation across an interval of length `H` is

\[
O\!\left(\frac{|t|hH}{X^2}\right)
=O\!\left(|\tau|\frac HX\right),
\qquad
\tau=\frac{ht}{X}.
\]

This identifies the relevant duality: a prime-counting theorem resolving intervals of length `X^theta` controls this phase uniformly while `|tau| X^(theta-1) -> 0`.

## 2. Current short-interval input

Larry Guth and James Maynard, *New large value estimates for Dirichlet polynomials*, **Annals of Mathematics** 203(2) (2026), 623--675, DOI `10.4007/annals.2026.203.2.6`, prove in Corollary 1.4 that for every fixed `epsilon>0` and

\[
y\ge X^{2/15+\epsilon}
\]

(up to their stated upper range), the expected asymptotic prime count in `[x,x+y]` holds for all but

\[
O\!\left(X\exp(-c(\log X)^{1/4})\right)
\]

integer starting points `x in [X,2X]`, for a positive constant `c` after harmless weakening of their explicit error. Their Corollary 1.3 gives a uniform-in-`x` theorem only from the longer scale `X^(17/30+epsilon)`; the stronger `2/15` exponent is an almost-all statement.

The distinction matters. The proof below does **not** silently replace “almost all intervals” by “all intervals.” Instead it exploits the fact that a global prime sum may be partitioned with a freely chosen offset.

## 3. A good-offset partition converts almost-all local PNT into global quadrature

For `eta>=13/15`, the displayed frequency range is contained in a fixed compact `tau`-interval, and the compact-uniform version of the PNT argument in `PL-180` already gives the claim. Thus it remains only to treat `0<eta<13/15`.

Fix a lower cutoff `delta in (0,1)` and decompose `[delta X,X]` into finitely many dyadic blocks `[Y,2Y]`. It is enough to work on one such block, because `Y asymp_delta X` and the number of blocks is fixed once `delta` is fixed.

Choose

\[
\theta=\frac{2}{15}+\frac{\eta}{3}
\]

and let `H=floor(Y^theta)`. Since `eta<13/15`, this lies safely inside the upper range of the Guth--Maynard short-interval theorem, and that theorem applies with any smaller positive epsilon, say `eta/4`. Let `E_Y` be the set of exceptional integer starts in `[Y,2Y]`. Then

\[
|E_Y|
\ll
Y\exp(-c(\log Y)^{1/4}).
\]

Consider the `H` possible residue offsets `a=0,...,H-1` for partitions with starts

\[
x_{a,j}=Y+a+jH.
\]

Every integer start belongs to exactly one residue class modulo `H`, apart from irrelevant edge bookkeeping. Averaging over the offsets therefore shows that **some** offset meets at most

\[
\frac{|E_Y|}{H}
\]

exceptional cells. We choose that offset. This choice is legitimate because it changes only the partition used to evaluate the already fixed sum over primes; it does not change the sum itself.

On every good cell `I=[x,x+H]`, Guth--Maynard gives

\[
\#\{q\in I:q\ \mathrm{prime}\}
=\frac{H}{\log x}\,(1+o(1))
\]

uniformly in the cell. If

\[
|\tau|\le X^{13/15-\eta},
\]

then the phase oscillation on one cell is, uniformly on `[delta X,X]`,

\[
\sup_{u,v\in I}|\phi_{X,t}(u)-\phi_{X,t}(v)|
\ll_\delta
|\tau|\frac HX
\ll_\delta
X^{13/15-\eta+2/15+\eta/3-1}
=
X^{-2\eta/3}.
\]

Thus each good-cell prime sum may be replaced by the phase at one representative point times the prime count, with relative additive error `o(1)` after normalization.

The exceptional cells are harmless globally. Their total number of integer positions is at most

\[
\frac{|E_Y|}{H}\,H
=|E_Y|,
\]

so even the trivial bound “at most one prime per integer” gives, after division by `pi(X) asymp X/log X`, a contribution

\[
O_\delta\!\left(
(\log X)\exp(-c(\log X)^{1/4})
\right)
=o(1).
\]

The initial and final incomplete pieces of each dyadic partition have length `O(H)` and contribute `O(H log X/X)=o(1)` after the same normalization.

Finally, on a fixed dyadic block `log x/log X=1+o(1)`. Summing the good cells therefore converts the prime average into the ordinary Riemann sum for the phase. After summing the finitely many dyadic blocks one obtains, uniformly in the displayed `tau` range,

\[
\frac1{\pi(X)}
\sum_{\delta X<q\le X}
\exp\!\left(it\log\left(1+\frac hq\right)\right)
=
\int_\delta^1
\exp\!\left(it\log\left(1+\frac{h}{Xu}\right)\right)du
+o_\delta(1).
\]

The discarded small primes satisfy

\[
\frac{\pi(\delta X)}{\pi(X)}\longrightarrow\delta,
\]

so their total contribution has modulus at most `delta+o(1)`.

## 4. The continuum profile remains `J(tau)` uniformly in the polynomial window

Set `t=X tau/h`. For fixed `delta>0` and `u in [delta,1]`, Taylor expansion gives

\[
\begin{aligned}
t\log\left(1+\frac{h}{Xu}\right)
&=\frac{X\tau}{h}
\left(\frac{h}{Xu}+O\left(\frac{h^2}{X^2u^2}\right)\right)\\
&=\frac{\tau}{u}
+O_\delta\left(\frac{|\tau|}{X}\right).
\end{aligned}
\]

Uniformly for `|tau|<=X^(13/15-eta)`, the error is `O_delta(X^(-2/15-eta))`. Therefore

\[
\int_\delta^1
\exp\!\left(it\log\left(1+\frac{h}{Xu}\right)\right)du
=
\int_\delta^1 e^{i\tau/u}\,du+o_\delta(1).
\]

Both omitted intervals `[0,delta]` have length `delta`, so letting `X -> infinity` and then `delta -> 0` proves the uniform claim

\[
B_X(X\tau/h)=J(\tau)+o(1).
\]

For large `|tau|`, use `v=1/u`:

\[
J(\tau)=\int_1^\infty e^{i\tau v}v^{-2}\,dv.
\]

A single integration by parts gives

\[
J(\tau)=O(|\tau|^{-1}),
\qquad |\tau|\ge1.
\]

Hence every sequence in the polynomially super-mesoscopic range with `|tau_X| -> infinity` satisfies `B_X(t_X)->0`.

## 5. Why the exponent `13/15` appears

Guth--Maynard's zero-density work yields the uniform density exponent

\[
A_0=\frac{30}{13}.
\]

The standard zero-density-to-short-interval transfer gives almost-all PNT for

\[
\theta>1-\frac{2}{A_0}
=\frac{2}{15}.
\]

The affine phase can be regarded as locally constant on an `X^theta` cell while

\[
|\tau|X^{\theta-1}\to0,
\]

so the dual frequency exponent is

\[
1-\theta
<
\frac{13}{15}
=
\frac{2}{A_0}.
\]

This explains both the strength and the limitation of the result. The `13/15` horizon is **not** an intrinsic prime-lattice spectral exponent and has no special relationship to the critical line `Re(s)=1/2`; it is the dual resolution exponent supplied by the best currently available unconditional almost-all short-interval theorem. An improvement in that theorem automatically moves this horizon.

As a sanity check, using only Guth--Maynard's all-starts Corollary 1.3 at the scale `X^(17/30+epsilon)` would give the weaker but immediate horizon `|tau|<=X^(13/30-epsilon)`. The good-offset argument is exactly what legitimately upgrades that to the almost-all `13/15` range.

## Prior art and novelty audit

The theorem-level input is entirely established prior art:

- **Larry Guth, James Maynard**, “New large value estimates for Dirichlet polynomials,” *Annals of Mathematics* **203**(2) (2026), 623--675, DOI `10.4007/annals.2026.203.2.6`. Corollaries 1.3 and 1.4 are the uniform and almost-all short-interval prime-counting statements used above; Section 13.2 derives them from the paper's zero-density estimate.

A targeted search for the exact reciprocal phase `exp(it log(1+h/p))` did not locate a source treating this particular average as a separate invariant. That absence is **not** used as a novelty claim: once the phase derivative is written down, the quadrature argument from almost-all short-interval PNT is elementary. The only durable purpose of storing it is to close a specific branch in the Mathia `prime_lattice` investigation that `PL-180` explicitly left open.

The matched-control content is also clear. Any source sequence with the same almost-all local counting law at the required scale would obey the same quadrature limit. Rational-prime arithmetic enters through the Guth--Maynard theorem supplying that local law, but the resulting `J` profile does not recover the zeta zero divisor. In particular the short-interval theorem is unconditional and is derived from zero-density information far weaker than excluding every off-critical zero.

## Adversarial checks and limitations

- **The source prime is fixed.** The argument assumes `h=r-1` is independent of `X`. If `r` grows with the cutoff, the phase derivative and Taylor error acquire another scale and the stated horizon does not apply unchanged.
- **The moving source average is broad.** Thin prime subsets, jointly constrained pairs `(r,q)`, arithmetic conditioning, or a target-relative weight inserted before the affine cancellation can evade the short-interval quadrature.
- **`13/15` is a theorem horizon, not a natural barrier.** The argument says nothing about `|tau|` at or beyond `X^(13/15+o(1))`. Specialized exponential-sum estimates could in principle prove cancellation farther out.
- **Almost-all is used honestly.** No local claim is made for exceptional intervals. A favorable residue offset is chosen only to partition the fixed global sum, and the exceptional cells then have vanishing total mass.
- **No analytic continuation is involved.** The proof concerns finite prime sums and local prime-counting asymptotics. It does not continue an Euler product or Dirichlet series through `Re(s)=1`.
- **No RH implication is obtained.** The argument supplies cancellation in a particular affine readout from an unconditional zero-density theorem; it cannot force `Re(rho)=1/2`.

## Consequence for the research line

The accepted affine non-Haar clue should no longer treat the bare vertical/Kronecker phase with a fixed source prime and broad prime averaging as an open high-frequency escape anywhere below the current short-interval resolution horizon. `PL-180` gave the bounded/first-mesoscopic profile; the present result extends the same profile uniformly through

\[
\frac{|t|h}{X}\le X^{13/15-\eta},
\]

and forces it to zero once that normalized frequency diverges.

A surviving phase mechanism must therefore cross a load-bearing boundary: operate beyond the `X^(13/15-o(1))` normalized-frequency horizon with an independently justified exponential-sum estimate, let the frozen source grow or become jointly constrained with the moving prime, use genuinely non-product prime phases, or insert target/completion information before the affine cancellation. Merely raising the vertical zeta time through any polynomial scale covered above does not recover zero-sensitive structure.