# FD-270 — Bohr-mean zero packets require exceptional phase coherence

- **Date:** 2026-09-22
- **Status:** proved mean-square bridge + conditional moment calibration
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** Mertens zero packet / Bohr mean / reciprocal-square zeta-derivative moment / divisor replication / exceptional phase coherence
- **Depends on:** FD-261, FD-267, FD-268, FD-269
- **Classification:** `EXACT-DERIVED + BOHR-MEAN-SQUARE + NEGATIVE-SECOND-MOMENT-BRIDGE + EXCEPTIONAL-COHERENCE-BARRIER`

## Claim

FD-269 showed that the absolute `l^1` budget of a critical-zero packet is large enough to cross the deep-repair threshold left by FD-261/268. The remaining question was whether enough of that budget can survive the phases of the actual consecutive-difference/divisor-replicated field.

For a finite packet of simple critical-line zeros

\[
\rho=\frac12+i\gamma,
\qquad 0<\gamma\le T,
\]

define

\[
F_T(t)
:=
2\Re\sum_{0<\gamma\le T}
\frac{t^\rho}{\rho\zeta'(\rho)}
\]

and its replicated consecutive-difference field

\[
G_{T,N}(d)
:=
\sum_{q\mid d}
\bigl(F_T(Nq)-F_T(N(q-1))\bigr).
\tag{1}
\]

Write `N=e^u`, remove the critical-line amplitude, and set

\[
\widetilde G_{T,u}(d)
:=
e^{-u/2}G_{T,e^u}(d).
\tag{2}
\]

For a depth band `x<d<=2x`, let

\[
S_{T,x}(u)
:=
\sum_{x<d\le2x}|\widetilde G_{T,u}(d)|.
\tag{3}
\]

Finally define the weighted reciprocal-square derivative moment

\[
\mathcal L_{-1}(T)
:=
\sum_{0<\gamma\le T}
\frac{1}{(1+\gamma)|\zeta'(\rho)|^2}.
\tag{4}
\]

Then for every fixed `epsilon>0` and `T<=x`, the Bohr mean in log-dilation satisfies

\[
\boxed{
\left(\mathbb M_u S_{T,x}(u)^2\right)^{1/2}
\ll_\varepsilon
x^{1+\varepsilon}\,\mathcal L_{-1}(T)^{1/2}.
}
\tag{5}
\]

Here

\[
\mathbb M_u H
:=
\lim_{U\to\infty}\frac1U\int_0^U H(u)\,du.
\]

Thus the phase-sensitive mean-square scale is controlled not by the first negative moment `J_{-1/2}` used in FD-269, but by a **frequency-damped reciprocal-square moment**.

If the cumulative reciprocal-square moment obeys

\[
J_{-1}^{\le}(T)
:=
\sum_{0<\gamma\le T}|\zeta'(\rho)|^{-2}
\le T^{\sigma+o(1)},
\tag{6}
\]

then dyadic summation in (4) gives

\[
\mathcal L_{-1}(T)
\le
T^{\max\{\sigma-1,0\}+o(1)}.
\tag{7}
\]

Putting `T=x` in (5),

\[
\boxed{
\left(\mathbb M_u S_{x,x}(u)^2\right)^{1/2}
\le
x^{1+\frac12\max\{\sigma-1,0\}+o(1)}.
}
\tag{8}
\]

The natural Gonek--Hejhal scale is `sigma=1`. On that calibration the replicated packet has only

\[
\boxed{
\left(\mathbb M_u S_{x,x}(u)^2\right)^{1/2}
\le x^{1+o(1)},
}
\tag{9}
\]

whereas FD-261 requires depth exponent strictly larger than

\[
2-\beta
=1.4150374992\ldots,
\qquad
\beta=\log_2\frac32.
\tag{10}
\]

For a mean-square mechanism alone even to reach that barrier, (8) would require

\[
\boxed{
\sigma\ge 3-2\beta
=1.8300749985\ldots .
}
\tag{11}
\]

So the square-root-sized absolute packet budget of FD-269 does **not** generically survive phase averaging. If the spectral route succeeds at the natural reciprocal-square moment scale, it must do so through exceptional phase coherence in `u=log N`, not through typical log-dilation behavior.

## 1. Exact Bohr orthogonality after log normalization

Define the divisor kernel

\[
K_\rho(d)
:=
\sum_{q\mid d}
\left(q^\rho-(q-1)^\rho\right),
\qquad 0^\rho:=0.
\tag{12}
\]

Since `N=e^u` and `Re rho=1/2`, (1)--(2) become the finite trigonometric polynomial

\[
\widetilde G_{T,u}(d)
=
2\Re\sum_{0<\gamma\le T}
\frac{K_\rho(d)}{\rho\zeta'(\rho)}e^{i\gamma u}.
\tag{13}
\]

For distinct positive ordinates, ordinary exponential orthogonality gives exactly

\[
\boxed{
\mathbb M_u
|\widetilde G_{T,u}(d)|^2
=
2\sum_{0<\gamma\le T}
\frac{|K_\rho(d)|^2}
{|\rho|^2|\zeta'(\rho)|^2}.
}
\tag{14}
\]

No linear-independence conjecture for zero ordinates is needed. The only point is that the finite frequencies `+gamma` and `-gamma` are distinct; every off-diagonal exponential has nonzero frequency and has zero Cesaro mean.

This is the first place in the current spectral route where the phases are used rather than discarded by triangle inequality. FD-268/269 controlled the sum of mode magnitudes. Equation (14) replaces that `l^1` accumulation by an exact `l^2` accumulation under log-dilation averaging.

## 2. The divisor kernel costs only one damped frequency

The FD-268 consecutive-difference estimate at critical exponent gives, uniformly for `q>=1`,

\[
|q^\rho-(q-1)^\rho|
\ll
q^{1/2}
\min\left\{1,\frac{1+\gamma}{q}\right\}.
\tag{15}
\]

For `q>=2`, this follows by combining the endpoint bound with

\[
q^\rho-(q-1)^\rho
=
\rho\int_{q-1}^q t^{\rho-1}\,dt;
\]

`q=1` is absorbed by the endpoint bound.

Cauchy over the divisors of `d` gives

\[
|K_\rho(d)|^2
\le
\tau(d)
\sum_{q\mid d}
|q^\rho-(q-1)^\rho|^2.
\tag{16}
\]

Summing over `x<d<=2x`, using `tau(d)<<_epsilon x^epsilon` and that the number of multiples of `q<=2x` in the band is `O(x/q)`, yields

\[
\sum_{x<d\le2x}|K_\rho(d)|^2
\ll_\varepsilon
x^{1+\varepsilon}
\sum_{q\le2x}
\min\left\{1,\frac{1+\gamma}{q}\right\}^2.
\tag{17}
\]

The remaining sum is elementary:

\[
\sum_{q\le2x}
\min\left\{1,\frac{1+\gamma}{q}\right\}^2
\ll
1+\min\{\gamma,x\}.
\tag{18}
\]

Hence

\[
\boxed{
\sum_{x<d\le2x}|K_\rho(d)|^2
\ll_\varepsilon
x^{1+\varepsilon}
\bigl(1+\min\{\gamma,x\}\bigr).
}
\tag{19}
\]

For `gamma<=T<=x`, combining (14) and (19), and using `|rho|asymp 1+gamma`, gives

\[
\mathbb M_u
\sum_{x<d\le2x}
|\widetilde G_{T,u}(d)|^2
\ll_\varepsilon
x^{1+\varepsilon}
\mathcal L_{-1}(T).
\tag{20}
\]

Finally, at every `u`, Cauchy on the `O(x)` depth coordinates gives

\[
S_{T,x}(u)^2
\ll
x
\sum_{x<d\le2x}|\widetilde G_{T,u}(d)|^2.
\tag{21}
\]

Taking Bohr means in (21) and inserting (20) proves (5).

## 3. The natural `J_{-1}` scale leaves a polynomial coherence gap

Equation (7) follows without any zeta-specific input beyond (6). Decompose the zeros into dyadic ordinate blocks. On `X<gamma<=2X`, the weight in (4) is `O(1/X)`, while the block reciprocal-square mass is at most `T^{sigma+o(1)}` at the corresponding scale. Thus each block contributes

\[
X^{\sigma-1+o(1)}.
\]

Summing the dyadic blocks gives (7), including the `sigma=1` boundary where logarithmic factors are absorbed into `T^{o(1)}`.

The standard Gonek--Hejhal conjecture for negative discrete moments predicts

\[
J_{-k}(T)
\asymp
T(\log T)^{(k-1)^2}
\]

on a dyadic zero interval. At `k=1`, this predicts reciprocal-square mass of order `T`, i.e. `sigma=1`; Gonek's sharper conjecture is `J_{-1}(T)~3T/pi^3`. Bui--Florea--Milinovich (2024, DOI `10.1112/blms.13092`) record this conjectural scale and the modern conditional upper-bound landscape. This literature input is a calibration only; equations (5), (7), and (8) are implications proved directly here.

Under that natural scale, (9) says that generic log-dilation phase energy loses the entire `x^(1/2)` absolute-budget gain isolated in FD-269. Comparing (8) with the FD-261 threshold `x^(2-beta)` gives

\[
1+\frac{\sigma-1}{2}
\ge
2-\beta,
\]

which is exactly (11). Thus a moment growth exponent near `1` is not marginally insufficient: it is separated from the required mean-square scale by the polynomial gap

\[
x^{1-\beta}
=
x^{0.4150374992\ldots}.
\]

There is also a useful exceptional-set formulation. If `sigma=1`, Markov's inequality applied to (5) gives the upper Bohr density

\[
\boxed{
\overline d_{\rm Bohr}
\left\{
 u:
 S_{x,x}(u)\ge x^{2-\beta}
\right\}
\le
x^{-2(1-\beta)+o(1)}
=
x^{-0.8300749985\ldots+o(1)}.
}
\tag{22}
\]

So on the natural reciprocal-square scale, log-dilations capable even of reaching the FD-261 depth threshold form a polynomially sparse phase set in Bohr mean.

## 4. Boundary, prior art, and validation

The distinction between continuous log-dilation and the original integer scale is essential. Equation (22) is a statement about Lebesgue/Bohr density in `u`; it does **not** prove that the discrete sequence `u=log N`, `N in N`, avoids the exceptional coherent phases. Nor does it control the truncation remainder required to replace the finite packet by the actual Mertens function. Exceptional resonances, arithmetic sampling of `log N`, or correlations between zero phases and the divisor kernel remain possible escape routes.

Likewise, the full-family upper bound `J_{-1}^{<=}(T)<=T^{1+o(1)}` is not asserted as a theorem here. The Gonek--Hejhal/Gonek prediction supplies the natural calibration; current rigorous negative-moment upper bounds in Bui--Florea--Milinovich apply to large subfamilies under additional hypotheses rather than giving the unrestricted statement needed to substitute directly into (9). The deterministic content of this finding is the exact Bohr orthogonality (14), the divisor-kernel estimate (19), and the bridge (5)--(8).

A targeted prior-art check found the classical negative-moment framework and its `J_{-1}` scale, but no source giving the consecutive-difference/divisor-replicated Bohr estimate (5). No novelty is claimed for trigonometric-polynomial orthogonality or for the Gonek--Hejhal conjecture itself. Because no external theorem is load-bearing in the proof, `SOURCES.md` does not need a new dependency.

As a normalization audit, the first eight critical zeros were evaluated numerically at depth band `32<d<=64`. Averaging the left side of (14), summed over the band, over `0<=u<=2000` gave `17.034515`, while the exact diagonal expression on the right gave `17.034578`, a ratio `0.9999963`. This is only a factor-check for the finite trigonometric identity, not evidence for the asymptotic moment hypothesis.

## Boundary

FD-270 does **not** close the spectral route. It proves something more specific: once the absolute `l^1` budget from FD-269 is replaced by the phase-sensitive Bohr mean square of the actual replicated packet, the natural reciprocal-square derivative scale predicts only linear depth mass, far below the superlinear `x^(1.415...)` demand needed by FD-261.

Therefore a successful zero-packet obstruction cannot look generic in log-dilation. It must exhibit exceptional coherence strong enough to beat the Bohr mean-square envelope, and it must do so at the arithmetic sample points `u=log N` while retaining control of the explicit-formula remainder. The next useful test is consequently discrete: determine whether the sequence of integer log-dilations can concentrate on the exceptional phase set strongly enough to evade (22), or whether a finite-window/discrete large-sieve estimate transfers the Bohr cancellation to the actual `N`-samples.

**Verdict.** FD-269 showed that the critical-zero packet has enough absolute spectral mass. FD-270 shows that, at the natural `J_{-1}` scale, typical log-dilation phases destroy that gain: the replicated packet is only `x^(1+o(1))` in band `l^1` RMS, and barrier-crossing phases have Bohr density at most `x^(-0.830074...+o(1))`. Any surviving spectral mechanism must therefore be an exceptional arithmetic phase-coherence phenomenon, not ordinary accumulation of zero residues.