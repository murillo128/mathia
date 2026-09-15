# AF-361 — Riesz exponential-band recovery splits base attenuation from bandwidth conditioning

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `STABILITY-CLARIFICATION`, `BOUNDARY-CLARIFICATION`, `MOVING-PARAMETER-OBSTRUCTION`, `ZERO-SENSITIVE-SOURCE`, `CONDITIONAL-RH`, `NO-NOVELTY-CLAIM`

## Claim

Retain AF-359--AF-360's logarithmically normalized Riesz family and assume RH. For each distinct positive zeta-zero ordinate `gamma`, with multiplicity retained in the coefficient vector, write

\[
\rho_\gamma=\frac12+i\gamma,
\qquad
M_\delta(\rho)
=
\Gamma(1+\delta)\frac{\Gamma(\rho+1)}{\Gamma(\rho+1+\delta)},
\tag{1}
\]

so that the critical zero coefficients satisfy

\[
\widehat E_\delta(\gamma)
=M_\delta(\rho_\gamma)\widehat E_0(\gamma).
\tag{2}
\]

AF-360 proves that on every fixed-ratio shell the small-order multiplier is asymptotically one common scalar. It therefore leaves one precise escape: a **single exponentially broad band** whose logarithmic width is order `1/delta`. That escape has an exact conditioning law.

Fix `v>0`. For `delta>0` and `T>0`, define the exponential zero band

\[
\mathcal B_{\delta,T}(v)
=
\left\{\gamma:
T<\gamma\le T\exp(v/\delta)
\right\}
\tag{3}
\]

and the scaled log-frequency coordinate

\[
x_{\delta,T}(\gamma)
:=
\delta\log\frac\gamma T
\in(0,v].
\tag{4}
\]

As in AF-360, factor out the lower-edge scalar

\[
c_{\delta,T}
:=
\Gamma(1+\delta)(iT)^{-\delta}.
\tag{5}
\]

Then along every sequence

\[
\delta_j\downarrow0,
\qquad
T_j\to\infty,
\tag{6}
\]

one has the **uniform exponential-band envelope**

\[
\boxed{
\sup_{\gamma\in\mathcal B_{\delta_j,T_j}(v)}
\left|
 e^{x_{\delta_j,T_j}(\gamma)}
 \frac{M_{\delta_j}(\rho_\gamma)}{c_{\delta_j,T_j}}
 -1
\right|
\longrightarrow0.
}
\tag{7}
\]

In fact the error in `(7)` is `O(delta_j/T_j)`. Thus after lower-edge normalization the Riesz multiplier is not asymptotically scalar on this exponentially wide band; it converges uniformly to the deterministic envelope

\[
\boxed{e^{-x},\qquad 0\le x\le v.}
\tag{8}
\]

Let `D_{\delta,T,v}` be the diagonal map from the endpoint zero-coefficient vector on `(3)` to the Riesz-smoothed vector, and put

\[
A_{\delta,T,v}:=c_{\delta,T}^{-1}D_{\delta,T,v}.
\tag{9}
\]

The Riemann--von Mangoldt formula supplies zero ordinates in both a lower dyadic subband and an upper dyadic subband for all sufficiently large `(T,1/delta)`. Consequently the singular values of `(9)` attain both ends of the envelope asymptotically, and

\[
\boxed{
\|A_{\delta,T,v}\|\longrightarrow1,
\qquad
\|A_{\delta,T,v}^{-1}\|\longrightarrow e^v,
\qquad
\kappa(A_{\delta,T,v})\longrightarrow e^v.
}
\tag{10}
\]

Hence an exponentially broad band of width ratio `exp(v/delta)` is **stably invertible after removing the common lower-edge amplitude**, with a finite recovery cost depending only on its scaled logarithmic width `v`.

There is a second, independent cost. Set

\[
u_{\delta,T}:=\delta\log T.
\tag{11}
\]

If `u_{\delta,T}->u in [0,infinity]`, then the absolute singular-value scale obeys

\[
\boxed{
\|D_{\delta,T,v}\|\to e^{-u},
\qquad
\|D_{\delta,T,v}^{-1}\|\to e^{u+v},
}
\tag{12}
\]

with the usual extended-real interpretation when `u=infinity`. Thus the Riesz channel has two distinct conditioning currencies:

\[
\boxed{
\text{base attenuation cost}=e^u,
\qquad
\text{bandwidth condition cost}=e^v.
}
\tag{13}
\]

The first is the radial loss already exposed by AF-359. The second is the differential cost required to preserve structure across an exponentially broad band.

More generally, if the upper/lower ratio is `R_delta` and

\[
v_\delta:=\delta\log R_\delta,
\tag{14}
\]

then the same multiplier estimate gives the phase law

\[
\boxed{
\log\kappa(A_{\delta,T,R_\delta})
=v_\delta+o(1)
}
\tag{15}
\]

whenever the band is populated, with the zero-coordinate lower bound supplied by Riemann--von Mangoldt whenever `R_delta` grows. Therefore

\[
\begin{array}{c|c}
\delta\log R_\delta & \text{normalized recovery}\
\hline
\to0 & \kappa\to1\quad\text{(projective scalarization)}\\
\to v\in(0,\infty) & \kappa\to e^v\quad\text{(finite nontrivial envelope)}\\
\to\infty & \kappa\to\infty\quad\text{(unstable inverse)}
\end{array}
\tag{16}
\]

This resolves the exponentially broad-band escape left open by AF-360. **The escape is real but tightly priced:** finite scaled width preserves endpoint coefficient information with bounded relative conditioning, while unbounded scaled width forces diverging conditioning. The surviving variation is a universal Riesz envelope; it does not manufacture a rational-prime discriminator that was absent from the incoming coefficient vector.

## Derivation

### 1. The Gamma quotient is uniformly regularly varying on arbitrarily wide upper bands

From `(1)`, exactly as in AF-360,

\[
\log M_\delta(\rho)
=
\log\Gamma(1+\delta)
-
\int_0^\delta\psi(\rho+1+t)\,dt.
\tag{17}
\]

For `0<delta<=1` and `rho=1/2+i gamma` with `gamma>=T`, the classical vertical-sector digamma expansion gives, uniformly in `0<=t<=delta`,

\[
\psi(\rho+1+t)
=
\log\rho+O(1/\gamma).
\tag{18}
\]

Integrating `(18)` yields

\[
M_\delta(\rho_\gamma)
=
\Gamma(1+\delta)\rho_\gamma^{-\delta}
\exp\!\left(O\!\left(\frac\delta\gamma\right)\right).
\tag{19}
\]

Divide by `(5)`. Since

\[
\frac{\rho_\gamma}{iT}
=
\frac\gamma T\left(1-\frac{i}{2\gamma}\right),
\tag{20}
\]

one obtains

\[
\log\frac{M_\delta(\rho_\gamma)}{c_{\delta,T}}
=
-\delta\log\frac\gamma T
+O\!\left(\frac\delta\gamma\right)
=
-x_{\delta,T}(\gamma)
+O\!\left(\frac\delta T\right).
\tag{21}
\]

The key point is that the error in `(21)` depends on the **lower** frequency bound `T`, not on the upper endpoint. Hence `(21)` remains uniform even when the upper/lower ratio is `exp(v/delta)` or larger. Exponentiating proves `(7)`.

This is stronger than applying AF-360 independently to many dyadic shells. It identifies the single common limiting coordinate across the entire exponentially broad band: `x=delta log(gamma/T)`.

### 2. Finite scaled width gives a boundedly invertible normalized transport

Let `s_\gamma(A)` denote the diagonal singular value of `(9)` at ordinate `gamma`. Equation `(7)` gives uniformly

\[
s_\gamma(A_{\delta,T,v})
=
e^{-x_{\delta,T}(\gamma)}(1+o(1)).
\tag{22}
\]

Therefore

\[
e^{-v}(1-o(1))
\le
s_\gamma(A_{\delta,T,v})
\le
1+o(1).
\tag{23}
\]

The upper and lower inequalities alone give

\[
\kappa(A_{\delta,T,v})
\le e^v(1+o(1)).
\tag{24}
\]

To see that the bound is attained on the actual zeta-zero coordinate set, use only classical zero counting. For all sufficiently large `T`, Riemann--von Mangoldt gives at least one zero ordinate in `(T,2T]`. Because `T exp(v/delta)->infinity`, it also gives an ordinate in

\[
\left(\frac12T e^{v/\delta},\,T e^{v/\delta}\right].
\tag{25}
\]

At the lower ordinate,

\[
x\le\delta\log2\to0,
\tag{26}
\]

whereas at the upper ordinate,

\[
x\ge v-\delta\log2\to v.
\tag{27}
\]

Together with `(22)`, these ordinates force the largest and smallest singular values to tend to `1` and `e^{-v}`, respectively. This proves `(10)`.

The recovery estimate is immediate. If the normalized smoothed observation is perturbed by `eta`, then reconstructing with `A^{-1}` gives

\[
\|\Delta V_0\|_2
\le
(e^v+o(1))\|\eta\|_2.
\tag{28}
\]

Thus an order-one differential attenuation across an exponential band does **not** itself imply catastrophic information loss. For fixed `v`, it is a well-conditioned diagonal reweighting.

### 3. Absolute recovery pays the independent lower-edge attenuation

The scalar `(5)` has magnitude

\[
|c_{\delta,T}|
=
\Gamma(1+\delta)T^{-\delta}
=
\exp(-u_{\delta,T}+o(1)).
\tag{29}
\]

Since

\[
D_{\delta,T,v}
=c_{\delta,T}A_{\delta,T,v},
\tag{30}
\]

combining `(10)` and `(29)` yields `(12)`. In particular, bounded relative conditioning across the band does not rescue an observation whose entire band has already been driven below an absolute noise floor by `u_{delta,T}->infinity`.

This separates two notions that can otherwise be conflated:

- `u=delta log T` measures common radial attenuation before comparing frequencies;
- `v=delta log R` measures the differential distortion across the retained bandwidth.

A normalization that quotients the common radial scale removes the `u` cost but cannot remove the `v` cost without also undoing the known Riesz envelope.

### 4. The general moving-band phase law

For a general ratio `R_delta>=1`, `(21)` gives

\[
\left|
\frac{M_\delta(\rho_\gamma)}{c_{\delta,T}}
\right|
=
\left(\frac\gamma T\right)^{-\delta}
\left(1+O\!\left(\frac\delta T\right)\right)
\tag{31}
\]

uniformly for `T<gamma<=R_delta T`. Hence the ratio between the extremal normalized multipliers is at most

\[
R_\delta^\delta(1+o(1))
=
\exp(v_\delta+o(1)).
\tag{32}
\]

When `R_delta` grows, lower and upper dyadic zero subbands give the matching lower bound exactly as in `(25)`--`(27)`. When `R_delta` stays bounded, `v_delta->0` and the upper bound already forces `kappa->1`. This proves `(15)`--`(16)` on every populated band relevant to the zero-coordinate transport.

AF-360 is therefore the `v_delta->0` face of one continuous conditioning law rather than a separate phenomenon.

## Arithmetic-fidelity interpretation

The finding changes the status of the last post-Riesz escape from AF-360. An exponentially broad band is not automatically another lossy quotient. At fixed scaled width `v`, the full complex endpoint zero vector can be recovered from its Riesz-smoothed image with finite normalized condition number `e^v`. What survives is exactly the log-frequency profile that fixed-ratio shells cannot see.

But the surviving profile is **universal**. Equation `(21)` depends only on the Riesz Gamma quotient and the frequency coordinate. It acts in the same way on any incoming coefficient family carried on the same frequency band. Therefore the envelope itself contains no rational-prime selectivity. Any arithmetic discriminator recovered after this stage must already have been present in the incoming coefficients or in source-side relations between them; the Riesz transform merely transports that information with the costs `(13)`.

This is the relevant arithmetic control. Replacing the endpoint coefficient vector by a matched non-arithmetic vector on the same frequency coordinates changes neither `(7)` nor the conditioning law. The transformation can preserve a discriminator, but cannot create one. Consequently a future RH-relevant use of the exponential band must identify a **source-native target statistic** whose dependence on the coefficients survives the universal diagonal envelope and whose source access is independently justified.

The result also sharpens what a useful next theorem would have to do. Increasing the band beyond finite `v` cannot provide unlimited new resolution at bounded cost: `kappa` then diverges exponentially in `v_delta`. Conversely, staying at finite `v` leaves a well-conditioned but universal representation. The unresolved burden is therefore no longer “can an exponentially broad band survive Riesz smoothing?” but “which arithmetic source relation, available before smoothing, is worth transporting through that band?”

## Boundaries and falsification

- RH is used only to interpret the whole nontrivial zero set as the critical-line coefficient space inherited from AF-358--AF-360. The Gamma-quotient estimate `(21)` itself is unconditional analytic mathematics.
- The result concerns the known diagonal Riesz multiplier on a retained frequency band. It does not establish that a prime-side construction can access the endpoint zero vector without already encoding equivalent zero information.
- `kappa(A)` measures **relative** recovery after factoring out the common scalar `c_{delta,T}`. Absolute perturbations in the unnormalized observation pay the additional factor `|c|^{-1}` quantified by `u`.
- The finite-`v` result does not say that every nonlinear observable is stable. It says the complete band vector itself is connected to the endpoint vector by a boundedly invertible diagonal map; any downstream instability belongs to that observable or target, not to loss of the band vector at the Riesz stage.
- The phase law is target-relative. If one quotients the deterministic envelope `e^{-x}` itself, the representation can become scalar again; that would be a new compression after the Riesz map, not evidence that the band never carried the information.
- Multiplicity does not affect the estimates. No simplicity, pair-correlation, zero-spacing, or linear-independence conjecture is used.
- The Riemann--von Mangoldt input is needed only to show that the zero-coordinate operator asymptotically realizes both ends of the continuous multiplier envelope. The upper recovery bounds do not require endpoint occupancy.

A direct falsification would be a sequence `delta_j->0`, `T_j->infinity`, fixed `v>0`, and ordinates `gamma_j` in `(3)` for which

\[
e^{x_j(\gamma_j)}
\frac{M_{\delta_j}(\rho_{\gamma_j})}{c_{\delta_j,T_j}}
\not\longrightarrow1.
\tag{33}
\]

The uniform digamma estimate `(21)` excludes such a sequence. A conditioning falsification would require the normalized diagonal map to have asymptotic condition number different from `e^v`; `(23)` together with the lower/upper dyadic zero occupancy excludes that under the stated hypotheses.

## Source / prior-art audit

The exact Riesz multiplier is inherited from AF-359--AF-360 and ultimately from the classical Riesz-mean explicit-formula machinery of G. H. Hardy and J. E. Littlewood, **“Contributions to the Theory of the Riemann Zeta-Function and the Theory of the Distribution of Primes,”** *Acta Mathematica* **41** (1916), 119--196, DOI `10.1007/BF02422942`. NIST DLMF §5.11 supplies both the vertical-sector digamma expansion and the Gamma-ratio asymptotics, especially Eqs. 5.11.2 and 5.11.12--5.11.13. The zero-occupancy step is the classical Riemann--von Mangoldt formula; see E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-function*, 2nd ed., Oxford (1986), Chapter 9.

A targeted literature search for small-order Riesz means combined with exponential multiplicative bands, `delta log R` scaling, Gamma-quotient conditioning, and zeta-zero-band recovery did not locate this exact two-parameter conditioning formulation. Search results instead returned the classical Riesz multiplier and unrelated uses of “Riesz” conditioning. That absence is not evidence of novelty. No novelty is claimed for the Gamma asymptotics, Riesz explicit formula, zero counting, diagonal-operator conditioning, or regular-variation calculation. The durable Arithmetic Fidelity contribution is the exact resource accounting: the moving Riesz channel separates common attenuation `delta log T` from differential bandwidth cost `delta log R`, and the exponentially broad-band escape left open by AF-360 is stably recoverable precisely at finite scaled width.