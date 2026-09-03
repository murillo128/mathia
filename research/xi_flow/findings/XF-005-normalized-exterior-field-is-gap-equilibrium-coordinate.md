# XF-005 — the normalized exterior field is an exact scale-free gap-equilibrium coordinate

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-MECHANISM`. The zero-motion equation and Lehmer-pair criterion are classical. The durable line-specific result is that the scale-invariant coupling singled out in XF-004 has an exact intrinsic normalization: `qS=2` is the arithmetic-lattice equilibrium value, `qS<2` means forward squared-gap opening, `qS>2` means forward contraction, and classical Lehmer pairs lie far on the opening side.

## 1. Claim

On a real-simple slice of the de Bruijn--Newman flow, let

\[
x_j<x_{j+1},\qquad g_j=x_{j+1}-x_j,\qquad q_j=g_j^2
\]

be an adjacent pair. With the exterior field from XF-003,

\[
S_j=\sum_{k\notin\{j,j+1\}}
\frac{1}{(x_k-x_j)(x_k-x_{j+1})},
\]

define the normalized field

\[
\boxed{R_j:=q_jS_j.}
\]

Then the exact gap equation becomes

\[
\boxed{q_j'=4(2-R_j).}
\]

Thus `R_j` is not merely a dimensionless version of `S_j`: the value `2` is the exact instantaneous equilibrium threshold for the squared gap. The three regimes are

\[
R_j<2\iff q_j'>0,\qquad
R_j=2\iff q_j'=0,\qquad
R_j>2\iff q_j'<0.
\]

Under a common affine change of local coordinates `x -> a x+b`, `q_j -> a^2q_j` and `S_j -> a^{-2}S_j`, so `R_j` is translation and scale invariant.

## 2. Exact expression in normalized neighboring gaps

The field can be written entirely from the point pattern measured in units of the chosen gap. For `m>=1`, set

\[
r_m^+=\frac{x_{j+1+m}-x_{j+1}}{g_j},\qquad
r_m^-=\frac{x_j-x_{j-m}}{g_j}.
\]

Every exterior zero lies to one side of the pair, so direct substitution gives

\[
\boxed{
R_j=
\sum_{m\ge1}\frac{1}{r_m^+(r_m^++1)}
+
\sum_{m\ge1}\frac{1}{r_m^-(r_m^-+1)}.
}
\]

The sums are absolutely convergent for the Xi zero set in the real-rooted regime because the summands have inverse-square tails.

For an exact arithmetic lattice `x_k=kh` and any adjacent pair, `r_m^+=r_m^-=m`. Hence

\[
R_{\rm lat}
=2\sum_{m\ge1}\frac1{m(m+1)}
=2,
\]

and therefore `q'=0`. The equally spaced infinite configuration is exactly stationary at the level of every gap, as expected from the principal-value zero-motion law.

At the opposite endpoint, if a simple pair is born at a collision, XF-003 gives `S -> S_*<infinity` while `q ->0`; hence

\[
R\to0,\qquad q'\to8.
\]

The normalized coordinate therefore places collision birth at `R=0` and perfect local arithmetic equilibrium at `R=2`.

## 3. An exact smoothing comparison

The normalized representation makes the elementary smoothing direction precise. If every gap to both sides of the selected pair is at least `g_j`, then

\[
r_m^\pm\ge m
\]

for every `m`, so termwise comparison with the lattice gives

\[
R_j\le2,
\qquad q_j'\ge0.
\]

If every exterior gap is at most `g_j`, the inequalities reverse and

\[
R_j\ge2,
\qquad q_j'\le0.
\]

Strict inequality holds when the corresponding comparison is strict somewhere and the remaining configuration is nondegenerate. Thus a gap that is globally smaller than all of its surrounding gaps is forced to expand forward, while one globally larger than its surroundings is forced to contract.

The lattice value is also stable under genuinely uniform multiplicative near-equilibrium. If, relative to the chosen gap, every exterior gap lies between `(1-epsilon)g_j` and `(1+epsilon)g_j` with `0<epsilon<1`, then

\[
2\sum_{m\ge1}
\frac{1}{(1+\epsilon)m((1+\epsilon)m+1)}
\le R_j\le
2\sum_{m\ge1}
\frac{1}{(1-\epsilon)m((1-\epsilon)m+1)}.
\]

Both bounds tend to `2` as `epsilon ->0`. This gives a direct collision-variable formulation of the arithmetic-progression equilibrium that appears in the Rodgers--Tao contradiction mechanism. Their theorem is substantially stronger and more delicate because it obtains local equilibrium only in averaged, height-dependent forms; the display above must not be read as a replacement for their boundary and tail analysis.

## 4. Classical Lehmer pairs occupy the strongly sub-equilibrium regime

The Csordas--Smith--Varga Lehmer criterion provides a useful calibration at the other end. At `t=0`, under RH, let `gamma_-<gamma_+` be consecutive simple Xi zeros, let `Delta=gamma_+-gamma_-`, and write

\[
G=\sum_{\gamma\ne\gamma_-,\gamma_+}
\left(
\frac1{(\gamma-\gamma_-)^2}
+
\frac1{(\gamma-\gamma_+)^2}
\right).
\]

Their definition is

\[
\Delta^2G<\frac45.
\]

For each exterior zero the two denominators have the same sign, and

\[
\frac{2}{(\gamma-\gamma_-)(\gamma-\gamma_+)}
\le
\frac1{(\gamma-\gamma_-)^2}
+
\frac1{(\gamma-\gamma_+)^2}.
\]

Summing and multiplying by `Delta^2/2` yields the exact bridge

\[
\boxed{R\le\frac12\Delta^2G.}
\]

Consequently every classical Lehmer pair satisfies

\[
\boxed{R<\frac25}
\]

and therefore, instantaneously under forward heat flow,

\[
\boxed{q'>\frac{32}{5}.}
\]

This does **not** reprove the Csordas--Smith--Varga lower bound for `Lambda`: their theorem controls enough of the subsequent evolution to obtain a backward collision bound, whereas the inequality here is only an instantaneous consequence. Its value is organizational. The same normalized field places a Lehmer pair very close to the free-collision side `R=0` and very far from the arithmetic-equilibrium value `R=2`.

## 5. Collision age is an integrated equilibrium-deficit identity

For any simple pair born at time `t_*` and remaining adjacent and real-simple until `t_0`, integration of the exact equation gives

\[
\boxed{
q(t_0)=4\int_{t_*}^{t_0}(2-R(t))\,dt.
}
\]

Equivalently,

\[
\frac1{t_0-t_*}\int_{t_*}^{t_0}R(t)\,dt
=2-\frac{q(t_0)}{4(t_0-t_*)}<2.
\]

So a collision is not characterized merely by one small physical gap. It accumulates a positive **equilibrium deficit** `2-R` over its lifetime, and the final squared gap is exactly four times that accumulated deficit. This identity survives local spatial rescaling through `R`; only the physical conversion back to heat time is carried by `q`.

This sharpens the target left by XF-004. A backward-continuation argument cannot use a global absolute gap floor, but it can in principle try to control the time integral of the scale-free deficit `2-R` along candidate collision trajectories.

## 6. Prior-art and novelty boundary

The particle ODE and gap equation are classical in the de Bruijn--Newman literature; XF-003 already traces them to Csordas--Smith--Varga and Rodgers--Tao. Csordas, Smith and Varga, **Lehmer Pairs of Zeros, the de Bruijn--Newman Constant Lambda, and the Riemann Hypothesis**, *Constructive Approximation* 10 (1994), 107--129, give the exact Lehmer criterion `Delta^2 G<4/5` and the associated lower-bound mechanism for `Lambda`. Jeffrey Stopple, **Lehmer Pairs Revisited**, *Experimental Mathematics* 26 (2017), 130--138, restates that criterion and connects it to pre-Schwarzian data and zeros of `zeta'`.

No novelty is claimed for repulsive zero dynamics, arithmetic-progression local equilibrium, or the Lehmer-pair lower-bound mechanism. The Mathia-specific contribution is the exact common coordinate `R=qS`: its normalized neighboring-gap formula, its lattice threshold `R=2`, the elementary smoothing comparison, the bridge `R<=Delta^2G/2`, and the integrated deficit identity. These put the two historically opposite regimes used in de Bruijn--Newman arguments into one collision-safe scale-free observable.

## 7. Boundaries and decisive next test

`R` is not Xi-specific. Synthetic real-rooted heat flows can realize collision birth, near-lattice configurations, and intermediate values of `R`; the matched-control requirement from the line README therefore remains active. The pointwise value of `R` also does not determine its future evolution, and the zero-motion hierarchy for `R'` introduces additional information about the surrounding configuration.

The decisive next question is whether an unconditional Xi-specific input can control the **time-averaged deficit** `2-R` on a candidate backward collision trajectory more strongly than arbitrary real-entire controls. A useful theorem would either bound that deficit in terms of zero statistics available without RH, or prove that a positive-`Lambda` collision scenario forces an observable distribution of `R` incompatible with known Xi/zeta statistics. If matched controls with positive transition time can reproduce every such `R` law, then the normalized exterior field alone is only a coordinate change and the line must move to a genuinely higher-order field.

## 8. Consequence for `xi_flow`

XF-003 identified `qS` as the finite exterior correction and XF-004 showed why scale-free information is necessary. The present result fixes its exact interpretation:

\[
\boxed{R=qS\quad\text{measures instantaneous departure from equally spaced gap equilibrium}.}
\]

Collision birth has `R=0`, a classical Lehmer pair has `R<2/5`, and the perfect arithmetic lattice has `R=2`. The next upper-bound route is therefore no longer an unspecified search for a density-normalized field. It is the concrete problem of controlling the evolution or time-integrated deficit of this field strongly enough to distinguish the Xi heat flow from matched positive-transition controls.