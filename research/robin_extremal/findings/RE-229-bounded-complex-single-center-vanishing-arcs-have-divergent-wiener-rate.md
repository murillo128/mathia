# RE-229 — Bounded complex single-center vanishing arcs have divergent Wiener rate

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + COMPLEX-CENTER-DRIFT + VANISHING-ARC + DC-NORMALIZATION + WIENER-NORM-REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-220, RE-223, RE-226--RE-228.

RE-228 closes exact complex cancellation for one fixed contracting single center, but deliberately leaves open centers whose modulus or phase drift with scale. RE-226 had already shown that the positive-real vanishing-arc degeneration is actually very expensive. The same conclusion extends to **arbitrarily drifting complex phase** as long as the center modulus stays bounded and the truncation depth remains linear.

Let

\[
Q_{m,N,a}(z)
:=z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac{z}{a}\right)^k,
\qquad
F_{m,N,a}(z):=\frac{Q_{m,N,a}(z)}{Q_{m,N,a}(1)}.
\tag{1}
\]

Consider any sequence

\[
\alpha_m\to0,
\qquad
a_m=\rho_m e^{i\varphi_m},
\qquad
N_m\ge \lambda_- m
\tag{2}
\]

with fixed constants `lambda_->0` and `A<infinity`, such that

\[
0<\rho_m\le A,
\qquad
r_m:=\max_{|\theta|\le\alpha_m}
\left|1-\frac{e^{-i\theta}}{a_m}\right|<1,
\qquad
Q_{m,N_m,a_m}(1)\ne0.
\tag{3}
\]

Then there is a constant `c=c(A,lambda_-)>0`, independent of the phases `varphi_m`, for which

\[
\boxed{
\|F_{m,N_m,a_m}\|_A\ge e^{cm}
}
\tag{4}
\]

for all sufficiently large `m`. Consequently

\[
\boxed{
\frac{\log\|F_{m,N_m,a_m}\|_A}{m\alpha_m}
\longrightarrow+\infty.
}
\tag{5}
\]

The usual research scaling `m alpha_m -> infinity` is therefore more than enough; the algebraic lower bound (4) only needs `alpha_m -> 0`. No uniform-prediction assumption is needed once contraction (3), bounded modulus, and linear truncation are imposed. In particular, exact remainder cancellation and exact complex DC normalization cannot rescue a bounded complex center in the vanishing-arc limit.

## 1. Phase alignment turns the Wiener norm into a positive truncated sum

Write

\[
C_{m,k}:=\binom{m+k-1}{k},
\qquad
S_{m,N}(x):=\sum_{k=0}^{N}C_{m,k}x^k.
\tag{6}
\]

For `a=rho e^{i varphi}`, choose the phase-adapted unit-circle point

\[
z_*:=-\frac{a}{|a|}=-e^{i\varphi}.
\tag{7}
\]

Then

\[
1-\frac{z_*}{a}=1+\frac1\rho>0,
\tag{8}
\]

so every truncation level in (1) has the same phase at `z_*`. Hence

\[
|Q_{m,N,a}(z_*)|
=
\rho^{-m}S_{m,N}\!\left(1+\frac1\rho\right).
\tag{9}
\]

Conversely, expanding each `(1-z/a)^k` and using the coefficient triangle inequality gives the same quantity as an upper bound for `||Q||_A`. Therefore equality holds:

\[
\boxed{
\|Q_{m,N,a}\|_A
=
\rho^{-m}S_{m,N}(s),
\qquad
s:=1+\frac1\rho.
}
\tag{10}
\]

At DC put

\[
q:=\left|1-\frac1a\right|.
\tag{11}
\]

Because `theta=0` belongs to the contracting arc, (3) implies `q<1`; equivalently `Re(a)>1/2`, so in particular `rho>1/2`. The exact DC value only satisfies the upper bound

\[
|Q_{m,N,a}(1)|
\le
\rho^{-m}S_{m,N}(q).
\tag{12}
\]

Thus all possible complex cancellation in the normalization denominator has the expensive sign:

\[
\boxed{
\|F_{m,N,a}\|_A
\ge
\frac{S_{m,N}(s)}{S_{m,N}(q)}.
}
\tag{13}
\]

Since `rho<=A`,

\[
s\ge s_0:=1+\frac1A>1.
\tag{14}
\]

The complex geometry has now disappeared from the lower-bound problem except for the scalar `0<=q<1`.

## 2. A uniform truncated negative-binomial ratio lemma

Fix `s_0>1` and `lambda_->0`. There are constants `c>0` and `m_0` such that for every `m>=m_0`, every `N>=lambda_- m`, every `s>=s_0`, and every `0<=q<1`,

\[
\boxed{
\frac{S_{m,N}(s)}{S_{m,N}(q)}\ge e^{cm}.
}
\tag{15}
\]

A two-regime proof keeps the estimate uniform even when `q=q_m` approaches zero or one.

First set

\[
\delta:=\min\left\{\frac{\lambda_-}{2},\frac14\right\},
\qquad
K:=\lfloor\delta m\rfloor.
\tag{16}
\]

For large `m`, `K<=N`, `K>=delta m/2`, and

\[
C_{m,K}
=\binom{m+K-1}{K}
\ge\frac{m^K}{K!}
\ge\left(\frac{m}{K}\right)^K
\ge\delta^{-K}.
\tag{17}
\]

Choose once and for all `q_0 in (0,1)` so small that

\[
-\log(1-q_0)
<
\frac{\delta}{4}\log\frac{s_0}{\delta}.
\tag{18}
\]

If `0<=q<=q_0`, the full negative-binomial generating function gives

\[
S_{m,N}(q)
\le(1-q)^{-m}
\le(1-q_0)^{-m},
\tag{19}
\]

while (17) gives

\[
S_{m,N}(s)
\ge C_{m,K}s_0^K
\ge\left(\frac{s_0}{\delta}\right)^K.
\tag{20}
\]

Equations (18)--(20) imply, for all large `m`,

\[
\log\frac{S_{m,N}(s)}{S_{m,N}(q)}
\ge
\frac{\delta}{4}
\log\frac{s_0}{\delta}\;m.
\tag{21}
\]

It remains to control `q>=q_0`, including `q->1`. Put

\[
\delta_2:=\min\left\{\frac{\lambda_-}{2},\frac{q_0}{8}\right\},
\qquad
K_2:=\lfloor\delta_2m\rfloor,
\tag{22}
\]

and define weights

\[
w_k:=C_{m,k}q^k,
\qquad 0\le k\le N.
\tag{23}
\]

For `k<K_2`,

\[
\frac{w_{k+1}}{w_k}
=q\frac{m+k}{k+1}
\ge q_0\frac{m}{K_2}
\ge8.
\tag{24}
\]

After normalizing these weights to a probability law `P(J=k)=w_k/S_{m,N}(q)`, equation (24) implies

\[
P(J<K_2/2)
\le K_2\,8^{-K_2/2}=e^{-\Omega(m)}.
\tag{25}
\]

Hence `E[J]>=K_2/3` for all sufficiently large `m`. But

\[
\frac{S_{m,N}(s)}{S_{m,N}(q)}
=
E\!\left[\left(\frac{s}{q}\right)^J\right],
\tag{26}
\]

and `s/q>=s_0`. Jensen's inequality therefore yields

\[
\frac{S_{m,N}(s)}{S_{m,N}(q)}
\ge
\exp\!\left(E[J]\log\frac{s}{q}\right)
\ge
\exp\!\left(\frac{K_2}{3}\log s_0\right)
\ge e^{c_2m}
\tag{27}
\]

for some fixed `c_2=c_2(s_0,lambda_-,q_0)>0`. Taking the smaller constant from (21) and (27) proves (15). Combining (13)--(15) proves (4), and division by `m alpha_m` proves (5).

## 3. What this closes, and what it does not

The phase `varphi_m` may vary arbitrarily fast with `m`; the aligned evaluation point (7) simply follows it. Likewise no lower bound on `1-q_m` is needed. In particular, a bounded complex center may approach the DC contraction boundary `q_m->1`, and the second half of the ratio lemma still gives a uniform exponential surcharge. Exact cancellation inside `Q(1)` only decreases its modulus relative to (12), so it can only strengthen the result.

Two hypotheses are load-bearing. **Bounded modulus is essential to this argument:** if `rho_m->infinity`, then `s_m=1+1/rho_m->1` and the uniform separation `s_0>1` disappears, so the constant in (15) may collapse. **Linear truncation is also essential:** if `N_m/m->0`, there is no index `K=Theta(m)` from which to extract an exponential gap. RE-223 independently excludes truncation collapse for fixed-corridor candidates attempting to keep the normalized prediction cost near the universal floor, but (4) itself does not cover that regime.

This is also a useful falsification control on the mechanism. The proof does not use the prediction error at all. Therefore it cannot be an artifact of converting exact complex cancellation into an absolute remainder estimate: the obstruction already exists in the coefficient geometry of the normalized finite polynomial. Conversely, because the proof loses its fixed `s_0>1` when `rho_m` diverges, it gives no evidence against an unbounded complex-center boundary layer; that escape remains genuinely open.

## 4. Prior art and representation audit

The polynomial in (1) is an incomplete-beta/negative-binomial object, and uniform large-parameter asymptotics for incomplete beta functions are classical; Temme's work on incomplete Laplace integrals and later remainder estimates by Nemes--Olde Daalhuis are representative. Exponential energy or dynamic-range penalties for superoscillatory approximation are also classical, for example in Ferreira--Kempf. No novelty is claimed for those general phenomena.

None of that literature is load-bearing here. The new step used by this research line is the exact phase-adapted identity (10), followed by the elementary uniform ratio lemma (15), to handle a **scale-dependent complex phase and DC normalization simultaneously**. No external asymptotic theorem enters the proof, so no `SOURCES.md` update is required.

The obstruction is strictly representation-specific. It applies only to the exact single-center negative-binomial predictor (1). It does **not** raise the universal separated-measure lower bound `C_sep>=1`, does not prove `C_sep>=2`, and does not directly strengthen the ordinary-prime Robin realization. Complex coefficient measures remain a surrogate for the arithmetic `{0,1,2}` prime-edit source. Multi-center coefficient recombination, minimax or rational predictors, and different approximation bases are untouched.

## Research consequence

RE-226 closed the positive-real vanishing-arc degeneration; RE-228 closed every fixed complex center. The present result closes the overlap that remained between those two statements: **bounded complex centers cannot evade the single-center surcharge by letting their phase drift while the observed arc vanishes**. In the fixed-corridor regime, RE-223 supplies the required positive truncation ratio, so this eliminates a substantial part of the diagonal complex escape.

The remaining single-center boundary is now more specific rather than merely "complex parameters may drift": an unbounded complex center `rho_m->infinity` is not controlled by the phase-alignment gap because `1+1/rho_m->1`. Other non-vanishing-arc singular complex regimes must still be checked separately unless reduced to the fixed-parameter theorem. Beyond single-center, multi-center/minimax geometry remains the principal constructive direction.