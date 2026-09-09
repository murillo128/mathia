# MC-171 — Finite-time heat mean square has a sharp exponential phase-washout horizon

**Status:** `LITERATURE+EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MEAN-VALUE-METHOD`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the prime-phase heat orbit from `MC-170`,

\[
\Theta_z(\beta,t)
=\sum_{n\ge1}\mu(n)^2\chi_z(n)
 e^{-\beta(\log n)^2}n^{-it},
\qquad
z=(z_p)_p\in\mathbb T^{\mathcal P},
\]

and replace the stationary `T\to\infty` mean by the coupled finite-window statistic

\[
V_z(\beta,T)
:=\frac1{2T}\int_{-T}^{T}|\Theta_z(\beta,t)|^2\,dt.
\tag{1}
\]

For

\[
T_\beta=\exp(\tau/\beta),\qquad \tau\ge0,
\tag{2}
\]

the classical Montgomery--Vaughan mean-value theorem gives a sharp exponential washout threshold at

\[
\boxed{\tau=\frac38.}
\tag{3}
\]

More precisely, uniformly in every prime-phase vector `z`,

\[
\boxed{
\tau>\frac38
\quad\Longrightarrow\quad
V_z(\beta,T_\beta)
=D(\beta)\bigl(1+O(e^{-(\tau-3/8+o(1))/\beta})\bigr),
}
\tag{4}
\]

where

\[
D(\beta):=\sum_{n\ge1}\mu(n)^2e^{-2\beta(\log n)^2}
\]

is the phase-blind stationary diagonal from `MC-170`, and

\[
\lim_{\beta\downarrow0}\beta\log D(\beta)=\frac18.
\tag{5}
\]

Thus every exponentially longer window with `\tau>3/8` has the same mean-square exponential type `1/8` for Möbius and for **all** unimodular prime-phase deformations. At this scale the finite-time statistic has already lost the orientation information that `MC-169` needs.

The threshold is not merely an artifact of the upper bound. For the all-plus square-free control `z_p=1`,

\[
\boxed{
\lim_{\beta\downarrow0}
\beta\log V_+(\beta,e^{\tau/\beta})
=
\max\!\left(\frac18,\frac12-\tau\right)
\qquad(\tau\ge0).
}
\tag{6}
\]

Hence `3/8` is the exact crossover, for this matched control, between a finite-window coherent phase spike and the stationary square-free diagonal.

This closes one of the explicit escape hatches left by `MC-170`: a moving scalar `L^2` window is not automatically phase-blind, but once its time horizon exceeds `exp((3/8+o(1))/beta)` it becomes phase-blind at the only exponential resolution relevant to the heat saddle. Any useful moving-window mechanism must therefore live below this washout horizon or use a statistic not controlled by this mean-square reduction.

## 1. Montgomery--Vaughan gives the finite-window error

Put

\[
a_{n,z}(\beta)
:=\mu(n)^2\chi_z(n)e^{-\beta(\log n)^2}.
\]

The Montgomery--Vaughan Hilbert-inequality mean-value estimate for Dirichlet polynomials, applied first to finite truncations and then passed to the limit, gives

\[
\int_{-T}^{T}
\left|\sum_{n\ge1}a_{n,z}(\beta)n^{-it}\right|^2dt
=
2T\sum_{n\ge1}|a_{n,z}(\beta)|^2
+O\!\left(\sum_{n\ge1}n|a_{n,z}(\beta)|^2\right).
\tag{7}
\]

The passage to the infinite series is legitimate because, for every fixed `beta>0`, both weighted sums converge. Since `|chi_z(n)|=1`, the two right-hand quantities do not depend on `z`. Dividing by `2T` yields

\[
\boxed{
V_z(\beta,T)
=D(\beta)+O\!\left(\frac{E(\beta)}{T}\right),
}
\tag{8}
\]

with

\[
E(\beta)
:=\sum_{n\ge1}n\mu(n)^2e^{-2\beta(\log n)^2}.
\tag{9}
\]

Equation `(8)` is stronger than the qualitative `T\to\infty` statement in `MC-170`: it identifies the exact weighted coefficient mass that controls how quickly stationary phase blindness is reached.

## 2. The two coefficient masses have types `1/8` and `1/2`

Use the classical square-free counting law

\[
Q(x)=\sum_{n\le x}\mu(n)^2
=\frac6{\pi^2}x+O(\sqrt x).
\tag{10}
\]

Abel summation gives the leading integral for `D(beta)` as

\[
\frac6{\pi^2}\int_0^\infty e^{u-2\beta u^2}\,du.
\]

Its saddle is at `u=1/(4beta)` and has exponent `1/(8beta)`. The `O(sqrt x)` counting error has strictly smaller type, so `(5)` follows.

For `E(beta)`, the leading integral is instead

\[
\frac6{\pi^2}\int_0^\infty e^{2u-2\beta u^2}\,du,
\]

whose saddle lies at `u=1/(2beta)` and has exponent `1/(2beta)`. Again the square-free counting error is exponentially smaller. Therefore

\[
\boxed{
\lim_{\beta\downarrow0}\beta\log E(\beta)=\frac12.
}
\tag{11}
\]

With `T_beta=e^{tau/beta}`, equations `(8)`, `(5)` and `(11)` show that the relative mean-value error has exponential rate

\[
\frac{E(\beta)}{T_\beta D(\beta)}
=
\exp\!\left(
\frac{3/8-\tau+o(1)}{\beta}
\right).
\tag{12}
\]

This proves `(4)` whenever `tau>3/8`.

## 3. The all-plus control makes the threshold sharp

For `z_p=1`, write `Theta_+(beta,t)` for the unsigned square-free heat sum. The same square-free counting law gives, uniformly for `|t|<=sqrt(beta)`,

\[
\Theta_+(\beta,t)
=
\frac6{\pi^2}
\int_0^\infty e^{(1-it)u-\beta u^2}\,du
+
O\!\left(
\operatorname{poly}(\beta^{-1})e^{(1/16+o(1))/\beta}
\right).
\tag{13}
\]

The main Gaussian saddle has modulus

\[
\exp\!\left(
\frac{1-t^2}{4\beta}+o(\beta^{-1})
\right),
\]

so on that polynomial-width interval

\[
|\Theta_+(\beta,t)|^2
\ge
\exp\!\left(
\frac{1/2-o(1)}{\beta}
\right).
\tag{14}
\]

Since `T_beta>=1`, integrating only over `|t|<=sqrt(beta)` and dividing by `2T_beta` gives

\[
\liminf_{\beta\downarrow0}
\beta\log V_+(\beta,T_\beta)
\ge
\frac12-\tau.
\tag{15}
\]

On the other hand, `(8)` gives

\[
V_+(\beta,T_\beta)
\ll
D(\beta)+E(\beta)e^{-\tau/\beta},
\]

so

\[
\limsup_{\beta\downarrow0}
\beta\log V_+(\beta,T_\beta)
\le
\max\!\left(\frac18,\frac12-\tau\right).
\tag{16}
\]

For `tau<=3/8`, `(15)` and `(16)` coincide. For `tau>3/8`, `(4)` gives type `1/8`. At the endpoint `tau=3/8`, the coherent-spike lower bound already gives `1/8`. This proves `(6)` for all `tau>=0`.

## 4. What the threshold means

The constants have a concrete information meaning. The stationary diagonal lives on the square-coefficient saddle and has type `1/8`. The finite-window error is controlled by a first-moment spacing penalty `n`, whose Gaussian saddle has type `1/2`. The difference

\[
\frac12-\frac18=\frac38
\]

is exactly the exponential time needed for ordinary Dirichlet-frequency averaging to suppress the largest possible coherent off-diagonal contribution down to the phase-free diagonal scale.

The direct expansion

\[
V_z(\beta,T)
=
\sum_{m,n}\mu(m)^2\mu(n)^2
\chi_z(n)\overline{\chi_z(m)}
 e^{-\beta[(\log m)^2+(\log n)^2]}
\operatorname{sinc}\!\bigl(T\log(n/m)\bigr)
\tag{17}
\]

makes the missing information explicit: every phase-sensitive contribution is off-diagonal and survives only to the extent that the finite time window fails to resolve nearby logarithmic frequencies. Standard block mean-value refinements express precisely this residual through near-diagonal pairs with multiplicative spacing about `X/T`.

This does **not** produce a Möbius bound. It classifies when one natural finite-window completion of the heat route becomes incapable of distinguishing Möbius orientation from matched prime-phase controls. Below the `3/8` horizon, phase information may survive, but proving that the actual Möbius phase yields a useful smaller statistic remains a separate arithmetic problem.

## Prior art and novelty audit

The mean-value mechanism is classical. Montgomery and Vaughan's Hilbert-inequality method gives the weighted-frequency mean-square estimate underlying `(7)`; see H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, **Journal of the London Mathematical Society** (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`. Modern analytic-number-theory treatments routinely state the resulting Dirichlet-polynomial estimate in the form `integral |sum a_n n^{-it}|^2 = (T+O(N)) sum |a_n|^2` for length `N`, and refinements localize the error to near-diagonal pairs.

The square-free density input `(10)` is classical and already anchored as `MC-S12`. The Bohr/Kronecker infinite-time interpretation and the particular prime-phase heat family were audited in `MC-170`.

A targeted search for finite-time mean values of Gaussian-log weighted Dirichlet series and square-free Dirichlet polynomials found the general Montgomery--Vaughan machinery and modern block/near-diagonal variants, but did not locate a source singling out the coupled `T_beta=e^{tau/beta}` crossover `(3)` for this heat family. The crossover is an immediate consequence of classical tools plus the two Gaussian saddle scales, so **no novelty claim is made** for it as a theorem of analytic number theory. Its value here is as an exact boundary for the Mathia heat mechanism left open by `MC-170`.

## Boundaries and falsification tests

- Equation `(4)` requires `tau>3/8`. At `tau=3/8`, the Montgomery--Vaughan error and the diagonal have the same exponential type, so phase-independent relative asymptotics are not proved for arbitrary `z`.
- Equation `(6)` is for the all-plus square-free matched control. It does not assert the same subcritical type for the Möbius phase.
- The result classifies the scalar unweighted time mean square. Nonquadratic time functionals, anchored weights, cross-scale covariances, operator-valued observables, or windows with substantially different geometry are outside the theorem.
- The threshold is exponential-type information only. Polynomial and subexponential factors are deliberately invisible at the `beta log` scale.
- A smaller window is not automatically useful. It merely avoids this specific phase-washout theorem; a candidate still needs an independently provable Möbius-specific estimate and a cheaper transfer to Mertens excursion.
- The argument uses no analytic continuation of `1/zeta`, no RH-scale Mertens estimate, and no random-walk model.

## Consequence for the line

`MC-170` identified a genuine missing middle between fixed-time RH-equivalent control and fully stationary phase blindness. The quadratic moving-window version of that middle is now quantitatively classified: **exponential windows beyond `exp(3/(8 beta))` are already too long** to retain prime orientation at leading exponential scale.

A surviving scalar heat route must therefore either exploit `T_beta` at or below the `3/8` horizon together with a new Möbius-specific off-diagonal estimate, or change the functional so that Montgomery--Vaughan diagonalization no longer supplies the governing information loss. This is a narrower and falsifiable frontier than the unrestricted finite-window escape left by `MC-170`.