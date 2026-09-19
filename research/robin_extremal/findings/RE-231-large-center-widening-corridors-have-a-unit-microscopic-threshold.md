# RE-231 — Large-center widening corridors have a unit microscopic threshold

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + COMPLEX-CENTER-DRIFT + WIDENING-CORRIDOR + MICROSCOPIC-NORMAL-FORM + SHARP-BOUNDARY + REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-223, RE-228--RE-230.

RE-230 showed that an unbounded complex single center reverts to the raw delay when

\[
\frac{N_m}{m|a_m-1|}\to0,
\]

and therefore cannot predict inside a fixed delay corridor. The open regime was the widening-corridor transition where `N/m` grows on the same scale as the center. That transition has a natural complex parameter

\[
\boxed{
\kappa_m:=\frac{N_m}{m(a_m-1)}.
}
\tag{1}
\]

It controls the microscopic predictor exactly.

Let

\[
Q_{m,N,a}(z)
:=z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac za\right)^k,
\qquad
F_{m,N,a}(z):=\frac{Q_{m,N,a}(z)}{Q_{m,N,a}(1)}.
\tag{2}
\]

Assume throughout this finding that `m->infinity`, `|a_m|->infinity`, and `N_m>=0`.

There are two exact microscopic regimes.

1. If

\[
\kappa_m\to\kappa,
\qquad
\Re\kappa<1,
\tag{3}
\]

then, for every fixed `U<infinity`, `Q_{m,N_m,a_m}(1)` is nonzero for all sufficiently large `m` and

\[
\boxed{
\sup_{|u|\le U}
\left|
F_{m,N_m,a_m}(e^{-iu/m})
-e^{-i(1-\kappa)u}
\right|
\to0.
}
\tag{4}
\]

Thus RE-230's raw-delay profile is only the special case `kappa=0`. A finite amount of widening does not immediately flatten the delay; it merely **renormalizes its microscopic phase rate from `1` to `1-kappa`**.

2. If the centers are eventually positive real,

\[
a_m>1,
\qquad
a_m\to+\infty,
\tag{5}
\]

and

\[
\kappa_m\to\kappa\in[1,\infty),
\tag{6}
\]

then, for every fixed `U`,

\[
\boxed{
\sup_{|u|\le U}
\left|
F_{m,N_m,a_m}(e^{-iu/m})-1
\right|
\to0.
}
\tag{7}
\]

Hence `kappa=1` is a sharp threshold for the **positive-real microscopic obstruction**. Below one, a residual delay survives. At and above one, the `1/m`-scale delay is flattened.

This does not prove global prediction on arcs with `m alpha_m->infinity`: (7) controls only fixed compact `u=m theta` windows. It shows instead that the local obstruction found in RE-230 is genuinely exhausted at the unit transition and cannot be extended past it without a new argument.

## 1. Exact normalization retained from RE-230

Put

\[
p:=1-\frac1a,
\qquad
\delta:=\frac1{a-1}.
\tag{8}
\]

The exact beta-integral normalization is

\[
D_{m,N,a}
:=
\int_0^1
s^{m-1}
\left(1-\frac sa\right)^N ds
=p^N I_{m,N,a},
\tag{9}
\]

where

\[
I_{m,N,a}
:=
\int_0^1
s^{m-1}
\left(1+\delta(1-s)\right)^N ds.
\tag{10}
\]

The normalized angular derivative is exactly

\[
\frac{d}{d\theta}
F_{m,N,a}(e^{-i\theta})
=
\frac{-i e^{-im\theta}
(1-e^{-i\theta}/a)^N}
{D_{m,N,a}}.
\tag{11}
\]

Define the microscopic profile

\[
G_m(u):=F_{m,N_m,a_m}(e^{-iu/m}).
\tag{12}
\]

Since

\[
\frac{1-e^{-iu/m}/a}{p}
=
1+\delta(1-e^{-iu/m}),
\tag{13}
\]

we obtain

\[
\boxed{
G_m'(u)
=
-i e^{-iu}
\frac{R_m(u)}{mI_m},
}
\tag{14}
\]

with

\[
R_m(u):=
\left(1+\delta_m(1-e^{-iu/m})\right)^{N_m}.
\tag{15}
\]

The transition is therefore completely controlled by `R_m` and `mI_m`.

## 2. The off-center factor remembers `kappa`

Assume `kappa_m->kappa` is finite. Because `|a_m|->infinity`, also `delta_m->0`. For fixed `U`,

\[
N_m\delta_m(1-e^{-iu/m})
=
kappa_m\,m(1-e^{-iu/m})
\to i\kappa u
\tag{16}
\]

uniformly on `|u|<=U`.

Moreover,

\[
N_m|\delta_m|^2
|1-e^{-iu/m}|^2
\le
|\kappa_m|\,|\delta_m|\,\frac{U^2}{m}
\to0.
\tag{17}
\]

The logarithm of (15) may therefore be expanded uniformly, giving

\[
\boxed{
R_m(u)\to e^{i\kappa u}
}
\tag{18}
\]

on every compact `u`-interval.

The only remaining question is the normalization `mI_m`.

## 3. Subcritical complex transition: endpoint Laplace normal form

Make the exact change of variables

\[
y=m(1-s).
\tag{19}
\]

Then

\[
mI_m
=
\int_0^m
\left(1-\frac ym\right)^{m-1}
\left(1+\delta_m\frac ym\right)^{N_m}dy.
\tag{20}
\]

Suppose `kappa_m->kappa` with `Re(kappa)<1`. For every fixed `y`,

\[
\left(1-\frac ym\right)^{m-1}
\to e^{-y},
\tag{21}
\]

and

\[
N_m\log\left(1+\delta_m\frac ym\right)
\to\kappa y.
\tag{22}
\]

Thus the integrand in (20) converges pointwise to

\[
e^{-(1-\kappa)y}.
\tag{23}
\]

The convergence is dominated. Indeed, for large `m`, `|delta_m|<1/2`; for `0<=y<=m`, the elementary estimate

\[
\log|1+z|
\le\Re z+C|z|^2
\qquad(|z|\le1/2)
\tag{24}
\]

gives

\[
\begin{aligned}
\left|
\left(1-\frac ym\right)^{m-1}
\left(1+\delta_m\frac ym\right)^{N_m}
\right|
&\le
\exp\Bigl(
-(1-1/m)y
+\Re(\kappa_m)y
+C|\kappa_m||\delta_m|y
\Bigr).
\end{aligned}
\tag{25}
\]

Because `Re(kappa)<1`, the right-hand side is bounded by `e^{-c y}` for some fixed `c>0` and all sufficiently large `m`. Dominated convergence yields

\[
\boxed{
mI_m\to
\int_0^\infty e^{-(1-\kappa)y}dy
=\frac1{1-\kappa}.
}
\tag{26}
\]

In particular the normalization is eventually nonzero. Combining (14), (18), and (26),

\[
G_m'(u)
\to
-i(1-\kappa)e^{-i(1-\kappa)u}
\tag{27}
\]

uniformly on compact `u`-intervals. Since `G_m(0)=1`, integration gives (4).

The mechanism is now explicit. The widening corridor supplies a phase correction `kappa`; while `Re(kappa)<1`, endpoint localization survives and leaves the residual microscopic delay `1-kappa`.

## 4. Uniform prediction excludes every finite subcritical accumulation point

Suppose an unbounded-center sequence predicts the constant target on arcs

\[
\varepsilon_m
:=
\sup_{|\theta|\le\alpha_m}
|F_m(e^{-i\theta})-1|
\to0,
\qquad
m\alpha_m\to\infty.
\tag{28}
\]

If `kappa_m` has a finite subsequential limit `kappa` with `Re(kappa)<1`, then every fixed microscopic interval `|u|<=U` eventually lies inside the observed arc. Equation (4) would therefore have to converge simultaneously to the constant `1` and to

\[
e^{-i(1-\kappa)u}.
\tag{29}
\]

These functions are different because `kappa!=1`. Contradiction.

Hence:

\[
\boxed{
\text{a successful large-center predictor has no finite accumulation point }
\kappa\text{ with }\Re\kappa<1.
}
\tag{30}
\]

In particular, if `kappa_m` is bounded, prediction forces

\[
\boxed{
\liminf_{m\to\infty}\Re\kappa_m\ge1.
}
\tag{31}
\]

Since

\[
\Re\kappa_m
=
\frac{N_m}{m}
\frac{\Re(a_m-1)}{|a_m-1|^2},
\tag{32}
\]

(31) is a phase-sensitive corridor requirement. Any bounded-transition successful family must eventually point into the right half-plane, and if

\[
\arg(a_m-1)\to\varphi,
\qquad
|\varphi|<\frac\pi2,
\tag{33}
\]

then necessarily

\[
\frac{N_m}{m}
\ge
(1-o(1))
\frac{|a_m-1|}{\cos\varphi}.
\tag{34}
\]

For positive-real centers this becomes the clean unit lower bound

\[
\boxed{
\frac{N_m}{m}
\ge(1-o(1))(a_m-1).
}
\tag{35}
\]

Thus RE-230's qualitative condition `N/m >= c|a|` sharpens, in the finite-transition regime, to an explicit coefficient-one boundary.

## 5. Positive-real sharpness: the unit threshold kills the local delay

Now assume `a_m>1`, so `delta_m>0`, and `kappa_m->kappa>=1`. The finite beta-integral expansion from RE-230 is

\[
mI_m
=
1+
\sum_{j=1}^{N_m}
\frac{N_m(N_m-1)\cdots(N_m-j+1)}
{(m+1)(m+2)\cdots(m+j)}
\delta_m^j.
\tag{36}
\]

Every term is nonnegative. For each fixed `j`,

\[
\frac{N_m(N_m-1)\cdots(N_m-j+1)}
{(m+1)\cdots(m+j)}
\delta_m^j
\to\kappa^j.
\tag{37}
\]

Since `kappa>=1`, for every fixed `J`,

\[
\liminf_{m\to\infty}mI_m
\ge
\sum_{j=0}^{J}\kappa^j.
\tag{38}
\]

Letting `J->infinity` proves

\[
\boxed{mI_m\to+\infty.}
\tag{39}
\]

Equation (18) still gives `R_m(u)->e^{i kappa u}` uniformly on compact intervals. Therefore (14) implies

\[
\sup_{|u|\le U}|G_m'(u)|\to0.
\tag{40}
\]

With `G_m(0)=1`, this proves (7).

So the microscopic transition for positive-real large centers is genuinely sharp:

\[
\boxed{
0\le\kappa<1
\quad\Longrightarrow\quad
G_m(u)\to e^{-i(1-\kappa)u},
}
\tag{41}
\]

whereas

\[
\boxed{
\kappa\ge1
\quad\Longrightarrow\quad
G_m(u)\to1.
}
\tag{42}
\]

At the critical value `kappa=1`, the local phase is already flattened even though the global prediction problem remains unresolved.

## 6. Falsification boundary and numerical sanity check

The theorem is deliberately microscopic. Equation (42) does **not** imply

\[
\sup_{|\theta|\le\alpha_m}|F_m(e^{-i\theta})-1|\to0
\tag{43}
\]

when `m alpha_m->infinity`, because the corresponding `u`-interval grows without bound. A different obstruction may appear on mesoscopic or macroscopic scales, and the Wiener norm may still be prohibitive.

The complex region with finite accumulation points satisfying `Re(kappa)>=1` is also not classified by this finding. For non-real `kappa`, the integral (20) becomes a genuinely complex endpoint/saddle problem; positivity used in (38) is unavailable. Nor does the argument classify `|kappa_m|->infinity`, multi-center/minimax predictors, rational predictors, or different bases.

A non-load-bearing finite-sum check illustrates the transition. With `m=200` and `a=30` real, choosing `N` so that `kappa` is approximately `0.5, 0.9, 1.0, 1.2` gives

\[
mI_m
\approx
1.9801,\ 7.7130,\ 17.7785,\ 1069.11,
\tag{44}
\]

respectively. The subcritical limits predicted by (26) are `2` and `10`; convergence slows near the critical point. At `u=1`, direct integration of the exact derivative gives, for `kappa=0.5`,

\[
G_m(1)\approx0.87627-0.48444i,
\qquad
e^{-i/2}\approx0.87758-0.47943i,
\tag{45}
\]

while for `kappa=1.2`,

\[
G_m(1)\approx1.00009-0.00093i,
\tag{46}
\]

consistent with the supercritical flattening. These numbers only check the exact formulas; they are not part of the proof.

## 7. Prior-art audit

The closest classical background is the asymptotic theory of incomplete beta and incomplete Laplace integrals: Temme's uniform asymptotic expansions (1975, 1987) and the later remainder analysis of Nemes and Olde Daalhuis (2016). The negative-binomial partial-sum / incomplete-beta correspondence is also classical. Those sources make an endpoint-to-saddle transition unsurprising at a special-function level.

A targeted search for truncated negative-binomial prediction with a drifting large complex center, the scaling `N/(m(a-1))`, and a microscopic phase normal form did not identify the predictor-specific limits (4), (7), or the phase-sensitive corridor consequence (31)--(35). The derivation here does not require an external asymptotic theorem: it uses the exact finite integral/derivative identities already established in RE-230 plus dominated convergence and positivity of the finite expansion. No new `SOURCES.md` dependency is therefore needed.

## 8. Consequence for the current frontier

RE-230 left the entire transition

\[
\frac{N}{m|a-1|}=\Theta(1)
\tag{47}
\]

as an undifferentiated widening-corridor boundary layer. RE-231 resolves its microscopic structure much more sharply.

For finite complex transition parameter, every region with `Re(kappa)<1` still carries a residual delay and is incompatible with uniform prediction. For positive-real centers, the obstruction disappears **exactly at `kappa=1`**. Therefore a widening-corridor single-center attack cannot merely make `N/m` proportional to `|a|` with an arbitrary small constant; at microscopic scale the positive-real geometry requires coefficient at least one, and complex phase can make the required corridor still wider through (34).

This does not revive the current ordinary-prime construction, whose useful realization is fixed-corridor. It instead identifies the first genuinely different single-center regime that survives the local obstruction: critical/supercritical widening with `Re(kappa)>=1`, followed by a global-arc and Wiener-cost analysis. If that regime is too expensive globally, the remaining constructive frontier is still a category change such as multi-center/minimax cancellation or another approximation basis.