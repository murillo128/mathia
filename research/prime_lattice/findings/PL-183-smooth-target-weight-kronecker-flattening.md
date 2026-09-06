# PL-183 — Smooth target weights remain one-point-density flat below short-interval PNT resolution

## Claim

The target-relative escape left open by `PL-182` does not survive if the target enters only as a bounded slowly varying one-point weight on the moving prime. The same Guth--Maynard short-interval input that flattens the bare Kronecker phase also flattens every such weighted readout.

For `X>=2`, `h>=1`, real `t`, and an absolutely continuous weight `w:[0,1]->C`, put

\[
\kappa=\frac hX,
\qquad
\nu=\frac{|t|h}{X+h}=\frac{|t|\kappa}{1+\kappa},
\]

and

\[
B_{X,h,w}(t)
:=
\frac1{\pi(X)}
\sum_{q\le X\atop q\ \mathrm{prime}}
w(q/X)
\exp\!\left(it\log\left(1+\frac hq\right)\right).
\]

Let

\[
I_{\kappa,t,w}
:=
\int_0^1
w(u)
\exp\!\left(it\log\left(1+\frac\kappa u\right)\right)\,du,
\]

where the value at `u=0` is irrelevant. Fix `0<eta<13/15`. Uniformly over arbitrary sequences `h=h_X>=1`, `t=t_X in R`, and weights `w=w_X` satisfying

\[
\|w_X\|_\infty\le1,
\qquad
\|w_X'\|_\infty\le L_X,
\qquad
L_X+\nu_X\le X^{13/15-\eta},
\]

one has

\[
\boxed{
B_{X,h_X,w_X}(t_X)
=
I_{\kappa_X,t_X,w_X}+o(1).
}
\]

The `o(1)` is uniform in this entire family. Thus a bounded target envelope whose scaled Lipschitz complexity stays below the same short-interval resolution horizon does not restore rational-prime-specific information: the readout is determined by the continuum one-point density.

There is also a useful cancellation corollary. If `nu>0`, then

\[
\boxed{
|I_{\kappa,t,w}|
\le
\frac{3+L}{\nu}
}
\]

whenever `||w||_infinity<=1` and `||w'||_infinity<=L`. Consequently, under the hypotheses above,

\[
\nu_X\to\infty,
\qquad
L_X=o(\nu_X)
\]

implies

\[
\boxed{B_{X,h_X,w_X}(t_X)\to0.}
\]

So a genuinely slower target amplitude cannot rescue the high-frequency Kronecker branch. To avoid this conclusion, the target must change a load-bearing hypothesis: become thin/singular or arithmetically conditioned, depend jointly or nonlocally on several primes, oscillate at a scale comparable with the phase itself, or leave the present short-interval resolution band.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-REDIRECT`. The deep input is Guth--Maynard's 2026 almost-all prime number theorem in intervals of length `X^(2/15+epsilon)`, already used in `PL-181`--`PL-182`. The weighted extension is an elementary good-offset quadrature consequence of that theorem. No novelty is claimed for weighted prime sums, slowly varying weights, partial summation, or short-interval PNT. The durable Mathia-specific conclusion is the removal of the simplest target-relative escape explicitly left open after `PL-182`.

## 1. The combined target/phase has the same resolution parameter

Write

\[
\psi_{\kappa,t}(u)
=t\log\left(1+\frac\kappa u\right),
\qquad 0<u\le1.
\]

Its derivative is exact:

\[
\psi'_{\kappa,t}(u)
=-\frac{t\kappa}{u(u+\kappa)}.
\]

For every fixed `delta in (0,1)` and `u in [delta,1]`,

\[
|\psi'_{\kappa,t}(u)|
\le
\frac{1+\kappa}{u(u+\kappa)}\,\nu
\le
C_\delta\nu,
\]

uniformly for every `kappa>=0`. Hence the full weighted phase

\[
F_X(u)
:=w_X(u)e^{i\psi_{\kappa_X,t_X}(u)}
\]

satisfies on `[delta,1]`

\[
\|F_X'\|_\infty
\le
L_X+C_\delta\nu_X.
\]

This is the only new ingredient beyond `PL-182`: the target complexity and the Kronecker frequency enter additively in the local variation budget.

## 2. Guth--Maynard plus a good offset gives weighted quadrature

Fix `delta>0` and decompose `[delta X,X]` into finitely many dyadic blocks `[Y,2Y]`. Choose

\[
\theta=\frac{2}{15}+\frac\eta3,
\qquad
H=\lfloor Y^\theta\rfloor.
\]

Guth--Maynard's almost-all short-interval theorem applies at this scale. As in `PL-181`--`PL-182`, partition a dyadic block into cells of length `H` using one of the `H` possible residue offsets. Averaging the exceptional starting points over those offsets supplies a partition for which the total length of exceptional cells is bounded by the theorem's exceptional-set size. Since `|w_X|<=1`, those exceptional cells contribute `o(1)` after normalization by `pi(X)` even with the trivial bound of one prime per integer.

On every good cell, the normalized `u`-length is `H/X`, and therefore

\[
\operatorname{osc}_I F_X
\ll_\delta
(L_X+\nu_X)\frac HX.
\]

Under

\[
L_X+\nu_X\le X^{13/15-\eta},
\]

this is

\[
O_\delta\!\left(
X^{13/15-\eta+2/15+\eta/3-1}
\right)
=O_\delta(X^{-2\eta/3})
=o(1).
\]

Thus the weighted phase may be replaced by its value at one point of each good cell. The local prime count is then `H/log x (1+o(1))`; after division by `pi(X)~X/log X`, summing the good cells gives the Riemann integral of `F_X` on `[delta,1]`. The ratio `log X/log x` is `1+o_delta(1)` uniformly on this fixed bulk interval.

The two incomplete edge cells have total normalized contribution `o(1)`. The discarded small-prime range is uniformly bounded by

\[
\frac{\pi(\delta X)}{\pi(X)}=\delta+o(1),
\]

while the omitted continuum interval has modulus at most `delta`. Letting first `X->infinity` and then `delta->0` proves

\[
B_{X,h_X,w_X}(t_X)
-
I_{\kappa_X,t_X,w_X}
\longrightarrow0
\]

uniformly under the displayed complexity bound.

Nothing here upgrades the almost-all short-interval theorem to an all-starts theorem. The offset is chosen only to partition an already fixed global prime sum, exactly as in `PL-181`--`PL-182`.

## 3. A slowly varying target cannot stop high-frequency cancellation

The continuum profile admits an elementary nonstationary-phase bound that cleanly separates a genuinely slow target from a phase-matched target. For `nu>0`,

\[
|\psi'(u)|
=
\frac{|t|\kappa}{u(u+\kappa)}
\ge
\frac{|t|\kappa}{1+\kappa}
=\nu
\]

for `0<u<=1`. Moreover

\[
\frac1{\psi'(u)}
=-\frac{u(u+\kappa)}{t\kappa},
\]

so

\[
\left|\frac d{du}\frac1{\psi'(u)}\right|
=
\frac{2u+\kappa}{|t|\kappa}
\le
\frac2\nu.
\]

Integration by parts gives

\[
I_{\kappa,t,w}
=
\left[\frac{w(u)e^{i\psi(u)}}{i\psi'(u)}\right]_{0}^{1}
-
\int_0^1 e^{i\psi(u)}
\frac{w'(u)}{i\psi'(u)}\,du
-
\int_0^1 w(u)e^{i\psi(u)}
\frac d{du}\left(\frac1{i\psi'(u)}\right)\,du.
\]

The boundary term at `u=0` vanishes because `1/psi'(u)->0`. The boundary at `u=1` has modulus at most `1/nu`; the two integrals are at most `L/nu` and `2/nu`. Hence

\[
|I_{\kappa,t,w}|
\le\frac{3+L}{\nu}.
\]

This also exposes the exact limitation. A deliberately demodulating weight such as `w_X(u)=exp(-i psi_X(u))` can keep the continuum integral large, but its derivative has size comparable with the Kronecker phase derivative. That is not a slowly varying target rescue; it simply writes the known phase cancellation into the target. Any claim that such a phase-matched envelope carries new arithmetic must supply independent target-side structure rather than treating programmable demodulation as a lattice invariant.

## 4. Prime-lattice interpretation

The vertical character of the exponent lattice is

\[
f_t(n)=n^{it}
=\exp\!\left(it\langle v(n),(\log p)_p\rangle\right).
\]

After the source-forced affine plaquette reduction of `PL-179` and source demodulation, the one-axis residual is exactly

\[
\left(1+\frac hq\right)^{it}.
\]

`PL-180`--`PL-182` show that broad averaging over the moving prime `q` reduces this character to a continuum density profile throughout the current polynomial short-interval resolution band, even when `h` grows arbitrarily. The present result inserts the first target-relative factor *before* that broad average and shows that a bounded slowly varying one-point target still does not retain the discarded prime-coordinate information.

The conclusion is therefore narrower than “target-relative couplings fail.” It says that **one-point target amplitudes of sub-resolution complexity are still homogenized by local prime density**. A live target-relative mechanism must preserve information not expressible as such an envelope: joint prime relations, arithmetic conditioning, nonlocal transport, singular/thin support, completed data that changes the averaging law, or frequency complexity at the unresolved scale.

## 5. Prior-art and novelty audit

The theorem-level number-theoretic input is established prior art:

- Larry Guth and James Maynard, “New large value estimates for Dirichlet polynomials,” *Annals of Mathematics* **203**(2) (2026), 623--675, DOI `10.4007/annals.2026.203.2.6`. Their Corollary 1.4 supplies the almost-all prime number theorem in intervals of length `X^(2/15+epsilon)` used by the good-offset partition. The paper was published online on 1 March 2026.
- Jan Büthe, “A Brun--Titchmarsh inequality for weighted sums over prime numbers,” *Acta Arithmetica* **166**(3) (2014), 289--299, DOI `10.4064/aa166-3-5`, is nearby structural prior art showing that prime sums with slowly varying weights are classical objects. It gives weighted Brun--Titchmarsh upper bounds, not the particular normalized short-interval quadrature statement used here.

A targeted search did not locate the exact three-parameter family `w(q/X) exp(it log(1+h/q))` as a named theorem. That absence is not used as a novelty claim. Once the Guth--Maynard local counting theorem and the derivative bound are available, the weighted quadrature argument is elementary. The stored value is that it closes a specific live Mathia escape rather than that weighted PNT is new.

## 6. Matched controls, analytic boundary, and failure modes

The argument uses only an almost-all local counting law for the moving source sequence plus a bound on the test-function derivative. Any generalized-prime or synthetic point system with the same local counting asymptotic and exceptional-set control obeys the same weighted continuum limit. Therefore this regime cannot by itself distinguish the rational-prime zeta divisor from a matched control.

No Euler product, Dirichlet series, or analytic continuation is used. The statement concerns finite prime sums and the local distribution of primes. In particular, reaching large vertical time inside the allowed band is not a continuation mechanism through `Re(s)=1`, and the appearance of `13/15` remains the dual of the current short-interval theorem rather than a critical-line constant.

The result deliberately does **not** cover:

- weights unbounded in `X`;
- weights supported on genuinely thin sets or with jumps/singularities at unresolved scales;
- weights whose scaled Lipschitz complexity is comparable to or beyond `X^(13/15-o(1))`;
- arithmetic weights depending on factorization, congruence, Möbius/Liouville data, or a joint relation among several primes rather than only `q/X`;
- nonlocal operators, pair-conditioned source/target transport, or completed couplings whose target changes the source measure before this one-point quadrature;
- frequencies beyond the current short-interval resolution horizon.

The cancellation corollary also needs `L_X=o(nu_X)`. If `L_X` is comparable with `nu_X`, a target can phase-match the continuum oscillation, so no zero limit is asserted. Such a survivor is not automatically arithmetic: the matched-control test still applies.

## Decisive audit test

To falsify the main claim it is enough to produce a fixed `eta>0` and admissible sequences `h_X,t_X,w_X` with `||w_X||_infinity<=1`, `||w_X'||_infinity+nu_X<=X^(13/15-eta)` for which

\[
B_{X,h_X,w_X}(t_X)
-
I_{\kappa_X,t_X,w_X}
\not\to0.
\]

The vulnerable step would have to be the uniform conversion of Guth--Maynard's almost-all local PNT into global weighted quadrature. The good-offset proof above explicitly tracks the exceptional cells and the full target/phase oscillation, so an objection must identify a quantifier or scale in that conversion that is not covered by the published short-interval theorem.

## Consequence for the research line

The accepted affine non-Haar clue should no longer count a macroscopic or slowly varying target factor as sufficient to evade `PL-180`--`PL-182`. Within the current short-interval resolution band, any bounded one-point target with `L_X+nu_X<=X^(13/15-eta)` is still reduced to a continuum density integral; if the target varies more slowly than a diverging Kronecker phase, the readout tends to zero.

The target-relative branch therefore starts only after a real structural change: thin/joint arithmetic conditioning, nonlocal or completed transport, a phase-matched target with independently justified arithmetic meaning, or resolution beyond the present theorem horizon. Merely multiplying the broad prime average by a smooth target envelope does not retain a new prime-lattice invariant.
