# FD-050 — fixed nonsquarefree dilations bound global logarithmic occupation loss

**Status:** `EXACT-DERIVED + GLOBAL-LOGARITHMIC-AVERAGE + JOINT-NONSQUAREFREE-OCCUPATION + DILATION-TELESCOPING + ZERO-FRONTIER-CALIBRATED + SCHUR-PROJECTIVE-BOUND`.

`FD-047` proves that every fixed nonsquarefree dilation injects a lower-horizon copy of the full physical Jordan energy into the nonsquarefree part. Its first use followed one exact `q`-adic chain, leaving open the possibility that very small occupation might wander between different chains. `FD-049` separately rules out pointwise polynomial-rate loss but still permits arbitrary subpower exceptional horizons.

The same dilation inequality has a stronger all-horizon consequence when averaged in the natural multiplicative measure `dH/H`. The scale shift `H -> H/q` then telescopes to two boundary intervals. Combining that exact cancellation with the `FD-046` zero-frontier upper envelope gives a **global logarithmic entropy bound** for occupation loss.

Fix `D>=1` and a nonsquarefree integer `q>1`. Write

\[
w(r):=\frac{J_2(r)}{r^2},
\qquad
E_{H,D}:=\sum_{r>D}w(r)\mathcal H(\lfloor H/r\rfloor)^2,
\]

\[
U_{H,D}:=\sum_{\substack{r>D\\\mu(r)=0}}
w(r)\mathcal H(\lfloor H/r\rfloor)^2,
\qquad
\nu_{H,D}:=\frac{U_{H,D}}{E_{H,D}},
\]

and let

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

Choose an integer `H_*` large enough that the lower-horizon injection of `FD-047` is available and `U_(H,D)>0` for `H>=H_*`. Put

\[
\lambda_H:=\log\frac{H+1}{H},
\qquad
W_X:=\sum_{H=H_*}^{X-1}\lambda_H
=\log\frac{X}{H_*}
\]

for integer `X>H_*`, and define

\[
L_q:=2\Theta\log q-\log w(q),
\qquad
c_q:=e^{-L_q}=w(q)q^{-2\Theta}.
\]

Then

\[
\boxed{
\limsup_{X\to\infty}
\frac1{W_X}
\sum_{H=H_*}^{X-1}
\lambda_H\log\frac1{\nu_{H,D}}
\le L_q.
}
\tag{1}
\]

Equivalently, the global logarithmically weighted geometric occupation obeys

\[
\boxed{
\liminf_{X\to\infty}
\prod_{H=H_*}^{X-1}
\nu_{H,D}^{\lambda_H/W_X}
\ge c_q.
}
\tag{2}
\]

Weighted AM--GM also gives

\[
\boxed{
\liminf_{X\to\infty}
\frac1{W_X}
\sum_{H=H_*}^{X-1}\lambda_H\nu_{H,D}
\ge c_q.
}
\tag{3}
\]

Most importantly, for every fixed `0<eta<1`,

\[
\boxed{
\limsup_{X\to\infty}
\frac1{W_X}
\sum_{\substack{H_*\le H<X\\\nu_{H,D}\le\eta}}
\lambda_H
\le
\min\!\left\{1,\frac{L_q}{\log(1/\eta)}\right\}.
}
\tag{4}
\]

Thus horizons with extremely small nonsquarefree occupation have vanishing **global logarithmic density** as the threshold tends to zero. More generally, for any deterministic `eta_X -> 0`,

\[
\boxed{
\frac1{W_X}
\sum_{\substack{H_*\le H<X\\\nu_{H,D}\le\eta_X}}
\lambda_H
\longrightarrow0.
}
\tag{5}
\]

This is strictly stronger than controlling each fixed `q`-adic chain separately: cross-chain wandering can still create exceptional horizons, but it cannot occupy a positive amount of logarithmic scale at thresholds tending to zero.

## 1. The pointwise dilation inequality becomes a scale difference

`FD-047` gives, whenever the lower horizon exceeds `D`,

\[
\boxed{
U_{H,D}\ge w(q)E_{\lfloor H/q\rfloor,D}.
}
\tag{6}
\]

Hence

\[
\log\frac1{\nu_{H,D}}
\le
-\log w(q)
+\log E_{H,D}
-\log E_{\lfloor H/q\rfloor,D}.
\tag{7}
\]

The crucial point is to keep this as a difference across scales rather than estimate the two energies independently.

For real `x>=H_*`, define the step function

\[
F_D(x):=\log E_{\lfloor x\rfloor,D}.
\tag{8}
\]

Because `q` is an integer,

\[
\left\lfloor\frac{\lfloor x\rfloor}{q}\right\rfloor
=
\left\lfloor\frac{x}{q}\right\rfloor,
\tag{9}
\]

so (7) gives pointwise on every unit interval

\[
\log\frac1{\nu_{\lfloor x\rfloor,D}}
\le
-\log w(q)+F_D(x)-F_D(x/q).
\tag{10}
\]

Integrating against `dx/x` from `H_*` to an integer `X` yields

\[
\int_{H_*}^{X}
\log\frac1{\nu_{\lfloor x\rfloor,D}}\frac{dx}{x}
\le
-\log w(q)\log\frac{X}{H_*}
+
\int_{H_*}^{X}
\bigl(F_D(x)-F_D(x/q)\bigr)\frac{dx}{x}.
\tag{11}
\]

The scale difference telescopes exactly after `y=x/q`:

\[
\boxed{
\int_{H_*}^{X}
\bigl(F_D(x)-F_D(x/q)\bigr)\frac{dx}{x}
=
\int_{X/q}^{X}F_D(y)\frac{dy}{y}
-
\int_{H_*/q}^{H_*}F_D(y)\frac{dy}{y}.
}
\tag{12}
\]

All interior scales cancel. This is the all-horizon analogue of the discrete product telescoping in `FD-047`, but it no longer commits to one multiplicative chain.

## 2. Only the top boundary sees the zeta-zero frontier

`FD-046` proves that for every fixed `sigma>Theta`,

\[
E_{H,D}\ll_{D,\sigma}H^{2\sigma}.
\tag{13}
\]

Therefore, for large `y`,

\[
F_D(y)\le 2\sigma\log y+O_{D,\sigma}(1).
\tag{14}
\]

The lower boundary integral in (12) is a fixed constant. For the upper boundary,

\[
\begin{aligned}
\int_{X/q}^{X}F_D(y)\frac{dy}{y}
&\le
2\sigma\int_{X/q}^{X}\log y\,\frac{dy}{y}+O_{D,\sigma,q}(1)\\
&=
2\sigma(\log q)\log X+O_{D,\sigma,q}(1).
\end{aligned}
\tag{15}
\]

Insert this in (11), divide by `log(X/H_*)`, and let `X -> infinity`. Since `sigma>Theta` was arbitrary,

\[
\limsup_{X\to\infty}
\frac1{\log(X/H_*)}
\int_{H_*}^{X}
\log\frac1{\nu_{\lfloor x\rfloor,D}}\frac{dx}{x}
\le
2\Theta\log q-\log w(q)=L_q.
\tag{16}
\]

Finally, the step-function integral is exactly the discrete logarithmic average:

\[
\int_{H_*}^{X}
\log\frac1{\nu_{\lfloor x\rfloor,D}}\frac{dx}{x}
=
\sum_{H=H_*}^{X-1}
\log\frac{H+1}{H}
\log\frac1{\nu_{H,D}}.
\tag{17}
\]

Equations (16)--(17) prove (1). Exponentiating gives (2), and weighted AM--GM gives (3).

No lower regular-variation hypothesis for `E_(H,D)` is used. Large upward jumps, long plateaus, and subpower intermittency are all allowed; the integral cancels the interior scale fluctuations exactly.

## 3. Global logarithmic lower-tail sparsity

Every term in (1) is nonnegative because `0<nu_(H,D)<=1`. On a horizon with `nu_(H,D)<=eta`,

\[
\log\frac1{\nu_{H,D}}
\ge\log\frac1\eta.
\tag{18}
\]

Hence

\[
\log\frac1\eta
\sum_{\substack{H_*\le H<X\\\nu_{H,D}\le\eta}}
\lambda_H
\le
\sum_{H=H_*}^{X-1}
\lambda_H\log\frac1{\nu_{H,D}}.
\tag{19}
\]

Divide by `W_X`, use (1), and obtain (4). The same argument with `eta=eta_X` gives (5): the numerator is bounded by `(L_q+o(1))W_X`, while `log(1/eta_X)->infinity`.

For every fixed `eta<c_q`, equation (4) also gives a positive lower logarithmic density of horizons with occupation above `eta`:

\[
\boxed{
\liminf_{X\to\infty}
\frac1{W_X}
\sum_{\substack{H_*\le H<X\\\nu_{H,D}>\eta}}
\lambda_H
\ge
1-\frac{L_q}{\log(1/\eta)}
>0.
}
\tag{20}
\]

Thus a physical escape may still be pointwise arbitrarily deep on a sparse set, but it cannot make small occupation typical in logarithmic scale.

## 4. The four-adic constants are explicit

The smallest and strongest fixed nonsquarefree dilation from `FD-047` is `q=4`, with

\[
w(4)=\frac34.
\tag{21}
\]

Consequently

\[
\boxed{
c_4=\frac34\,4^{-2\Theta},
\qquad
L_4=2\Theta\log4-\log\frac34.
}
\tag{22}
\]

Since `1/2<=Theta<=1`,

\[
\boxed{
c_4\ge\frac3{64},
\qquad
L_4\le\log\frac{64}{3}.
}
\tag{23}
\]

Therefore, unconditionally,

\[
\liminf_{X\to\infty}
\frac1{W_X}
\sum_{H=H_*}^{X-1}\lambda_H\nu_{H,D}
\ge\frac3{64},
\tag{24}
\]

and

\[
\limsup_{X\to\infty}
\frac1{W_X}
\sum_{\substack{H_*\le H<X\\\nu_{H,D}\le\eta}}
\lambda_H
\le
\min\!\left\{1,
\frac{\log(64/3)}{\log(1/\eta)}
\right\}.
\tag{25}
\]

Under RH, these sharpen to

\[
\boxed{
c_4=\frac3{16},
\qquad
L_4=\log\frac{16}{3}.
}
\tag{26}
\]

The constants coincide with the corresponding chain constants of `FD-047`; the gain here is not a better local constant but the replacement of one prescribed four-adic chain by the full set of horizons under logarithmic measure.

## 5. The same bound controls Schur projective saturation

`FD-049` proves that the normalized Schur projective defect satisfies

\[
\varepsilon_{H,D}:=\frac{\rho_{H,D}^2}{E_{H,D}}
\ge\nu_{H,D}.
\tag{27}
\]

Hence

\[
\log\frac1{\varepsilon_{H,D}}
\le
\log\frac1{\nu_{H,D}}.
\tag{28}
\]

All of (1)--(5) therefore remain valid with `nu_(H,D)` replaced by `epsilon_(H,D)`. In particular, extremely sharp approaches to the Schur equality ray also have vanishing global logarithmic density as the threshold tends to zero.

For fixed `D`, `FD-032` identifies the corresponding linear-prime-prefix GCD-ceiling gap as a positive asymptotically constant multiple of `epsilon_(H,D)`. Thus the same logarithmic lower-tail restriction transfers to that relaxed dual saturation channel. This statement is deliberately fixed-`D`; allowing the Schur-head dimension to vary with `H` would destroy the single-function telescoping in (12) and needs a separate argument.

## 6. Boundary case and matched control

This theorem does **not** prove the accepted pointwise occupation clue. A set can have zero logarithmic density and still contain an unbounded sequence of arbitrarily bad horizons. It also does not imply zero ordinary upper density: logarithmic density is the natural measure generated by the multiplicative scale shift, and large additive blocks placed at rapidly separated scales can behave differently under ordinary counting.

`FD-048` is an important matched control. Its near-half-power-smooth synthetic profile has `U/E -> 0` on a supermultiplicatively separated sequence of selected horizons while retaining critical polynomial energy growth. Those selected scales have zero logarithmic density, so they are fully compatible with (1)--(5). The present result therefore removes the **positive logarithmic-density** escape without invalidating the known sparse hyperbola-sampling construction.

The surviving physical problem is sharper. Any counterexample to eventual positive occupation must concentrate its deep losses on a logarithmically negligible set of horizons, while simultaneously respecting the exact increment placement

\[
\Delta\mathcal H(n)
=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n
\]

and all earlier terminal-density, Mellin-packet, short-interval, fixed-row, and pointwise power-scale restrictions. The missing step remains a genuinely pointwise or stronger-density use of that arithmetic placement.

## 7. Prior-art and falsification boundary

The logarithmic telescoping identity (12) is elementary, and no novelty is claimed for multiplicative averaging itself. The load-bearing arithmetic inputs are exactly the already-anchored Mathia results: the nonsquarefree dilation injection of `FD-047` and the classical Mertens/zeta zero-frontier upper envelope transferred to `E_(H,D)` in `FD-046`. A targeted search over Farey/Mertens discrepancy, Jordan-totient energies, GCD matrices, nonsquarefree restrictions, and logarithmic-density formulations located the expected local-discrepancy and general Jordan/GCD-matrix literature but no theorem matching this specific occupation consequence. No new external dependency is needed, so `SOURCES.md` is unchanged and no broad literature novelty claim is made.

The main falsification checks are structural. The integer nature of `q` is essential for (9); a nonintegral scale would introduce floor errors into the exact shift. The nonsquarefree hypothesis is essential for the injection (6). The fixed-`D` hypothesis is essential for the single energy step function `F_D`. Finally, a polynomial upper envelope alone would not produce (1) without the exact scale-difference inequality (7); conversely, the dilation injection alone gives no finite global logarithmic bound without controlling the top boundary in (12).