# RE-230 — Unbounded complex single centers force corridor blowup

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + COMPLEX-CENTER-DRIFT + UNBOUNDED-CENTER + MICROSCOPIC-NORMAL-FORM + REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-220, RE-223, RE-228, RE-229.

RE-229 closes the vanishing-arc escape for complex single centers whose modulus stays bounded, and identifies `|a_m| -> infinity` as the remaining large-center boundary layer where its fixed Wiener-gap argument disappears. In that boundary layer the exact normalized predictor has a different and very rigid asymptotic behavior: unless the truncation depth grows proportionally to the center modulus, the predictor locally reverts to the original raw delay `z^m`.

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

Consider any sequence `m -> infinity`, `N=N_m>=0`, and complex centers `a=a_m` such that

\[
|a_m|\longrightarrow\infty,
\qquad
\eta_m:=\frac{N_m}{m|a_m-1|}\longrightarrow0.
\tag{2}
\]

Then, for every fixed `U<infinity`, `Q_{m,N_m,a_m}(1)` is nonzero for all sufficiently large `m` and

\[
\boxed{
\sup_{|u|\le U}
\left|
F_{m,N_m,a_m}\!\left(e^{-iu/m}\right)-e^{-iu}
\right|
\longrightarrow0.
}
\tag{3}
\]

Thus the microscopic profile is the **raw delay** `e^{-iu}`. The phase of `a_m` is unrestricted, no contraction assumption is needed, and `N_m/m` need not itself be bounded; the only small parameter is the scale-free ratio `eta_m` in (2).

Consequently, if an observed arc satisfies

\[
m\alpha_m\longrightarrow\infty,
\tag{4}
\]

then eventually `theta=pi/m` lies inside `[-alpha_m,alpha_m]`, and (3) gives

\[
F_{m,N_m,a_m}(e^{-i\pi/m})\longrightarrow-1.
\tag{5}
\]

Hence

\[
\boxed{
\sup_{|\theta|\le\alpha_m}
\left|F_{m,N_m,a_m}(e^{-i\theta})-1\right|
\ge 2-o(1).
}
\tag{6}
\]

Uniform prediction of the constant target is therefore impossible whenever (2) and (4) hold.

In particular, any unbounded-center sequence that *does* uniformly predict on arcs with `m alpha_m -> infinity` must satisfy the quantitative necessary condition

\[
\boxed{
\liminf_{m\to\infty}
\frac{N_m}{m|a_m-1|}>0.
}
\tag{7}
\]

For the fixed-delay-corridor regime of RE-216--RE-229, `N_m/m` is bounded above. Since `|a_m| -> infinity`, (7) is impossible. Therefore **an unbounded complex single center cannot predict in any fixed delay corridor**. To keep the large-center escape alive, the delay ratio itself must diverge at least proportionally to `|a_m|`.

## 1. Exact derivative identity

The truncated negative-binomial polynomial has a useful exact integral normalization. Put

\[
D_{m,N,a}
:=
\int_0^1 s^{m-1}
\left(1-\frac{s}{a}\right)^N ds.
\tag{8}
\]

Differentiating (1), or equivalently differentiating the truncated negative-binomial identity, gives

\[
Q'_{m,N,a}(z)
=
 m\binom{m+N}{N}
 a^{-m}z^{m-1}
\left(1-\frac za\right)^N.
\tag{9}
\]

Since `Q(0)=0`, integration along the real segment `[0,1]` yields

\[
Q_{m,N,a}(1)
=
 m\binom{m+N}{N}a^{-m}D_{m,N,a}.
\tag{10}
\]

Whenever `D!=0`, the exact angular derivative of the normalized predictor is therefore

\[
\boxed{
\frac{d}{d\theta}
F_{m,N,a}(e^{-i\theta})
=
\frac{-i e^{-im\theta}
\left(1-e^{-i\theta}/a\right)^N}
{D_{m,N,a}}.
}
\tag{11}
\]

The large-center analysis reduces to estimating `D` relative to its value at `s=1`.

## 2. The normalization becomes endpoint-local

Write

\[
p:=1-\frac1a,
\qquad
\delta:=\frac1{a-1}.
\tag{12}
\]

Then

\[
1-\frac{s}{a}
=p\left(1+\delta(1-s)\right),
\tag{13}
\]

so

\[
D_{m,N,a}=p^N I_{m,N,a},
\qquad
I_{m,N,a}
:=
\int_0^1
s^{m-1}
\left(1+\delta(1-s)\right)^N ds.
\tag{14}
\]

Expanding the last factor and evaluating the beta integrals gives the finite exact identity

\[
\begin{aligned}
mI_{m,N,a}
&=
\sum_{j=0}^{N}
\binom Nj\delta^j\,mB(m,j+1)\\
&=
1+
\sum_{j=1}^{N}
\frac{N(N-1)\cdots(N-j+1)}
{(m+1)(m+2)\cdots(m+j)}
\delta^j.
\end{aligned}
\tag{15}
\]

For every `j>=1`,

\[
\left|
\frac{N(N-1)\cdots(N-j+1)}
{(m+1)\cdots(m+j)}
\delta^j
\right|
\le
\left(\frac{N}{m|a-1|}\right)^j
=\eta_m^j.
\tag{16}
\]

Therefore, once `eta_m<1`,

\[
\boxed{
|mI_{m,N,a}-1|
\le
\frac{\eta_m}{1-\eta_m}
\longrightarrow0.
}
\tag{17}
\]

In particular `I`, hence `D` and `Q(1)`, is nonzero for all sufficiently large `m`, and

\[
\boxed{
D_{m,N,a}
=
\frac{p^N}{m}(1+o(1)).
}
\tag{18}
\]

This estimate is uniform in the phase of `a`. It also shows why the relevant large-center quantity is not `N/m` by itself, but `N/(m|a-1|)`.

## 3. Microscopic raw-delay normal form

Fix `U<infinity` and put `theta=u/m` with `|u|<=U`. From (12),

\[
\frac{1-e^{-iu/m}/a}{p}
=
1+\delta\left(1-e^{-iu/m}\right).
\tag{19}
\]

Because `|1-e^{-iu/m}|<=|u|/m`,

\[
N|\delta|\,
|1-e^{-iu/m}|
\le U\eta_m
\longrightarrow0
\tag{20}
\]

uniformly for `|u|<=U`. Hence

\[
\left(
\frac{1-e^{-iu/m}/a}{p}
\right)^N
\longrightarrow1
\tag{21}
\]

uniformly on every fixed `u`-interval. Define

\[
G_m(u):=F_{m,N_m,a_m}(e^{-iu/m}).
\tag{22}
\]

Using (11), (18), and (21),

\[
\begin{aligned}
G_m'(u)
&=
\frac1m
\frac{d}{d\theta}
F_{m,N_m,a_m}(e^{-i\theta})
\Big|_{\theta=u/m}\\
&=
-i e^{-iu}
\frac{
\left((1-e^{-iu/m}/a)/p\right)^N
}{mI_{m,N,a}}\\
&\longrightarrow -i e^{-iu}
\end{aligned}
\tag{23}
\]

uniformly for `|u|<=U`. Since normalization gives `G_m(0)=1`, integration of (23) yields

\[
G_m(u)
\longrightarrow
1+\int_0^u -i e^{-iv}\,dv
=e^{-iu},
\tag{24}
\]

uniformly on the same compact interval. This proves (3).

The mechanism is transparent: when the center is much farther away than the normalized truncation depth, the off-center correction is too weak on the microscopic `1/m` scale to alter the phase rotation already supplied by `z^m`. Exact DC normalization changes its amplitude but cannot flatten that phase.

## 4. Fixed corridors are incompatible with center escape

Suppose now that a sequence with `|a_m| -> infinity` satisfies uniform prediction

\[
\varepsilon_m
:=
\sup_{|\theta|\le\alpha_m}
|F_{m,N_m,a_m}(e^{-i\theta})-1|
\longrightarrow0,
\qquad
m\alpha_m\longrightarrow\infty.
\tag{25}
\]

If `liminf eta_m=0`, there is a subsequence on which `eta_m->0`. The microscopic theorem then applies to that subsequence, and (6) gives `epsilon_m>=2-o(1)`, a contradiction. Thus (7) follows.

Under a fixed delay-ratio bound

\[
\frac{N_m}{m}\le\Lambda<\infty,
\tag{26}
\]

we instead have

\[
\eta_m
\le
\frac{\Lambda}{|a_m-1|}
\longrightarrow0,
\tag{27}
\]

so the contradiction is automatic. In the separated-predictor normalization used by the preceding findings, the delays occupy

\[
H\le L\le (1+N/m)H+o(1),
\tag{28}
\]

and `m alpha = HT`. Therefore the research regime `T->infinity` has `m alpha->infinity`, while any fixed corridor supplies (26). The large-complex-center branch left open by RE-229 is consequently unavailable in the fixed-corridor architecture.

Conversely, (7) says exactly what an unbounded-center construction would have to pay to avoid this obstruction:

\[
\frac{N_m}{m}
\ge c|a_m-1|
\tag{29}
\]

for some `c>0` eventually. Thus the upper delay ratio must itself diverge at least linearly with the center modulus. This is a representation-level tradeoff, not a new universal lower bound for arbitrary separated measures.

## 5. Falsification boundary and numerical sanity check

The proof intentionally does **not** cover the regime

\[
\frac{N_m}{m|a_m-1|}=\Theta(1)
\quad\text{or larger}.
\tag{30}
\]

There the geometric estimate (17) no longer forces `mI->1`, and the off-center correction in (21) can survive on the microscopic scale. That is a genuine different asymptotic regime rather than a technical omission. In fixed corridors it cannot occur when `|a_m|->infinity`; in widening corridors it remains open.

The result is also specific to the exact negative-binomial single-center representation (1). It does not improve the universal `C_sep>=1` lower bound, does not establish `C_sep>=2`, and says nothing directly about multi-center/minimax, rational predictors, or another polynomial basis.

As a non-load-bearing arithmetic check, evaluating the exact finite sum (15) and integrating the exact derivative (23) at `m=80`, `N=240`, `arg(a)=0.7` gives the expected convergence as `|a|` grows. For `|a|=30,100,300`, respectively,

\[
|mI-1|
\approx 0.1092,\ 0.0305,\ 0.0100,
\tag{31}
\]

and

\[
|F(e^{-i\pi/m})+1|
\approx 0.354,\ 0.0967,\ 0.0314.
\tag{32}
\]

These values only check the algebra numerically; the proof is the exact finite-series argument above.

## 6. Prior-art audit

The closest classical asymptotic background remains Temme's work on uniform incomplete-beta / incomplete-Laplace asymptotics (1975, 1987), with later explicit remainder control by Nemes and Olde Daalhuis (2016). The superoscillation literature of Ferreira and Kempf (2006) is neighboring context for the general cost of reproducing an out-of-band local phase. A targeted search for large-center truncated negative-binomial prediction, incomplete-beta large-center limits, and single-center superoscillatory prediction did not identify the specific normal form (3) or the corridor-blowup consequence (7).

None of that literature is load-bearing here: (3) follows from the exact derivative identity, the finite beta-integral expansion (15), and the geometric bound (17). No new `SOURCES.md` dependency is therefore needed.

## 7. Consequence for the current frontier

RE-229 showed that bounded complex centers are prohibitively expensive in the vanishing-arc regime but left `|a_m|->infinity` as the point where its fixed phase-alignment gap vanishes. RE-230 shows that this apparent escape has a different obstruction: **with any fixed delay corridor, the predictor degenerates locally back to the uncorrected delay and misses the constant target by almost two**.

The informative large-center frontier is therefore no longer a fixed-corridor problem. To obtain nontrivial cancellation with `|a_m|->infinity`, one must simultaneously send `N/m` to infinity on the same scale as `|a_m|`. That leaves a widening-corridor boundary layer, but it lies outside the architecture used by the current ordinary-prime realization. Within the fixed-corridor single-center search, sending the complex center to infinity is closed.