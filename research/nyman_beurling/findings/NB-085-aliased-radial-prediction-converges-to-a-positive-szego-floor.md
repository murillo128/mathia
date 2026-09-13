# NB-085 — aliased radial prediction converges to a positive Szegő floor

**Status:** `LITERATURE+DERIVED + ACTUAL-NYMAN-SOURCE + SZEGO-KOLMOGOROV + ALIASED-PREDICTION-FLOOR + RADIAL-METHOD-CLASSIFICATION + METHOD-REDIRECT`.

`NB-084` identifies an exact source-specific radial prediction problem for every Nyman innovation. Fix `j>=1`, an integer `q>=2`, put `h=log q`, and recall

\[
\mathcal E_{j,q,L}
:=
\inf_{a_1,\ldots,a_L}
\left\|
D_j+\sum_{r=1}^L a_rU_{rh}D_j
\right\|^2
\tag{1}
\]

with periodized spectral density

\[
W_{j,q}(\theta)
=
\frac1h\sum_{k\in\mathbb Z}
\left|
D_j\!\left(\frac12+i\frac{\theta+2\pi k}{h}\right)
\right|^2,
\qquad -\pi\le\theta<\pi.
\tag{2}
\]

`NB-084` proves `W_(j,q)>0` almost everywhere and rewrites (1) as the anchored Toeplitz problem

\[
\mathcal E_{j,q,L}
=
\inf_{\substack{p(0)=1\\\deg p\le L}}
\frac1{2\pi}
\int_{-\pi}^{\pi}
W_{j,q}(\theta)|p(e^{-i\theta})|^2\,d\theta.
\tag{3}
\]

Positivity almost everywhere alone is not enough to determine the infinite-depth prediction error: a positive density can still have non-integrable negative logarithm and zero Szegő geometric mean. The actual Nyman density is more rigid. Its single central alias already forces

\[
\boxed{
\log W_{j,q}\in L^1(\mathbb T).
}
\tag{4}
\]

Consequently the Szegő--Kolmogorov prediction formula applies and gives the exact positive radial floor

\[
\boxed{
G_{j,q}
:=
\exp\!\left(
\frac1{2\pi}\int_{-\pi}^{\pi}
\log W_{j,q}(\theta)\,d\theta
\right)
>0,
}
\tag{5}
\]

\[
\boxed{
\mathcal E_{j,q,L}\downarrow G_{j,q}
\qquad(L\to\infty).
}
\tag{6}
\]

This changes the qualitative screening question left by `NB-084`. The radial error does **not** keep falling toward zero as descendant depth grows. For every current cutoff `R>j`, the visible causal prediction error satisfies

\[
\boxed{
G_{j,q}\ge \widehat\Pi_{j,R}^2.
}
\tag{7}
\]

Therefore define the **radial floor charge**

\[
\boxed{
\mathfrak S_{R,q}
:=
\sum_{j=1}^{R-1}
\log\frac{G_{j,q}}{\widehat\Pi_{j,R}^2}
\ge0.
}
\tag{8}
\]

and the finite-depth radial upper certificate from `NB-084`,

\[
\mathfrak C_{R,q,L}
:=
\sum_{j=1}^{R-1}
\log\frac{\mathcal E_{j,q,L}}{\widehat\Pi_{j,R}^2}.
\tag{9}
\]

For every fixed `R,q`,

\[
\boxed{
\mathfrak C_{R,q,L}\downarrow\mathfrak S_{R,q}.
}
\tag{10}
\]

Hence the single-`q` radial strategy has an exact qualitative classification:

\[
\boxed{
\begin{aligned}
&\text{there exist unbounded }R_k\text{ and finite }L_k
\text{ with }\sup_k\mathfrak C_{R_k,q,L_k}<\infty\\
&\qquad\Longleftrightarrow\qquad
\text{there exist unbounded }R_k
\text{ with }\sup_k\mathfrak S_{R_k,q}<\infty.
\end{aligned}
}
\tag{11}
\]

Whenever (11) holds, `NB-084` and the stable-tail criterion of `NB-074` imply

\[
\boxed{\mathcal T_\infty=\{0\}.}
\tag{12}
\]

Thus, for **qualitative** exclusion of the stable tail, the first radial obstruction is not the convergence rate of `E_(j,q,L)` or whether depth is affordable. `NB-074` allows an arbitrary finite horizon schedule, so after the floor charge is bounded one may choose each finite `L_k` as large as needed. The rate becomes essential only for stronger quantitative statements such as polynomial or prescribed future horizons.

Conversely, if

\[
\mathfrak S_{R,q}\to\infty,
\tag{13}
\]

then increasing depth on that one integer-dilation ray can never produce a bounded radial certificate. This does **not** imply a stable tail: the complete nonstationary future can predict better than a single radial ray. It says that any successful proof must then use cross-ray or otherwise nonradial cancellation rather than more depth alone.

## 1. One alias upgrades almost-everywhere positivity to the Szegő condition

`NB-084` gives

\[
\frac1{2\pi}\int_{-\pi}^{\pi}W_{j,q}(\theta)\,d\theta
=\|D_j\|^2<\infty.
\tag{14}
\]

Therefore

\[
\int\log^+W_{j,q}<\infty,
\tag{15}
\]

because `log^+ x<=x` for `x>=0`.

For the negative logarithm, retain only the `k=0` term of the nonnegative periodization:

\[
W_{j,q}(\theta)
\ge
\frac1h
\left|
D_j\!\left(\frac12+i\frac\theta h\right)
\right|^2.
\tag{16}
\]

The exact source formula from `NB-084` is

\[
D_j(s)
=
\frac{\zeta(s)}{sB(s)}
\bigl(j^{1-s}-(j+1)^{1-s}\bigr).
\tag{17}
\]

On `Re s=1/2`, the Blaschke factor has modulus one almost everywhere. The cell factor in (17) never vanishes there: its two summands have moduli `sqrt(j)` and `sqrt(j+1)`. The denominator `s` is also nonzero. Hence on the compact frequency interval

\[
|t|\le \frac\pi h
\tag{18}
\]

the only possible zeros in the modulus of (17) are zeros of `zeta(1/2+it)`.

The zeta function is analytic and nonzero identically on this compact segment, so its zeros there are finite in number and have finite order. Near a zero `t_0` of order `m`,

\[
\log|\zeta(1/2+it)|
=m\log|t-t_0|+O(1),
\tag{19}
\]

which is locally integrable. Away from those zeros all factors in (17) have logarithm bounded on compact subsets. Thus

\[
\log\left|
D_j\!\left(\frac12+it\right)
\right|
\in L^1\!\left([-\pi/h,\pi/h]\right).
\tag{20}
\]

Equation (16) then bounds the negative part of `log W_(j,q)` by an integrable function. Together with (15), this proves (4).

The point is stronger than `W>0` almost everywhere. Almost-everywhere positivity excludes a positive-measure zero set; (4) also excludes zeros or valleys flat enough to make the geometric mean vanish.

## 2. Spectral factorization gives the exact infinite-depth radial floor

By (4), the classical Szegő spectral factorization supplies an outer `Phi_(j,q) in H^2(D)` with

\[
|\Phi_{j,q}(e^{i\theta})|^2
=W_{j,q}(\theta)
\quad\text{a.e.},
\tag{21}
\]

and

\[
|\Phi_{j,q}(0)|^2
=
\exp\!\left(
\frac1{2\pi}\int_{-\pi}^{\pi}\log W_{j,q}
\right)
=G_{j,q}.
\tag{22}
\]

Under (21), the objective in (3) is the `H^2` norm of `Phi_(j,q)p` (up to the harmless orientation convention on the circle). Every admissible polynomial has `p(0)=1`, so evaluation at zero gives

\[
\|\Phi_{j,q}p\|_{H^2}^2
\ge
|\Phi_{j,q}(0)|^2
=G_{j,q}.
\tag{23}
\]

Because `Phi_(j,q)` is outer, polynomial multiples of it are dense in `H^2`. Approximate the constant `Phi_(j,q)(0)` by `Phi_(j,q)p_n`. Evaluation at zero then gives `p_n(0)->1`; rescaling by `p_n(0)` produces admissible polynomials with the same limit. Hence the unrestricted finite-polynomial infimum is exactly `G_(j,q)`. The degree-`L` feasible sets increase with `L`, so their minima decrease to that infimum, proving (6).

This is the standard Szegő--Kolmogorov prediction formula in the exact normalization of `NB-084`; no novelty is claimed for the scalar prediction theorem itself.

## 3. The geometric floor must dominate every visible causal prediction error

Fix `R>j`. Exact branching in `NB-084` embeds the first `L` radial descendants into the actual finite future up to

\[
N_{R,L}^{(q)}=q^LR-1,
\tag{24}
\]

so

\[
\Pi_{j,N_{R,L}^{(q)}}^2
\le
\mathcal E_{j,q,L}.
\tag{25}
\]

On the other hand, `NB-074` proves for every finite future horizon

\[
\Pi_{j,N}^2\ge\widehat\Pi_{j,R}^2.
\tag{26}
\]

Combining (25)--(26) and taking `L->infinity` through (6) yields (7). In particular, the logarithms in (8) are genuinely nonnegative; no determinant cancellation is hidden in the floor charge.

There is also a purely causal lower bound on the floor. Every positive radial shift `U_(r log q)D_j` starts no earlier than `log(qj)`. Therefore no radial predictor can alter `D_j` on

\[
[\log j,\log(qj)),
\]

and

\[
\boxed{
\mathcal E_{j,q,L}
\ge
\|(J_{qj}-J_j)D_j\|^2
\qquad(L\ge1).
}
\tag{27}
\]

Taking the limit gives

\[
\boxed{
G_{j,q}
\ge
\|(J_{qj}-J_j)D_j\|^2.
}
\tag{28}
\]

This is a useful warning about the radial restriction. The ray skips all nonradial innovations between `j` and `qj`; their visible cancellation power is absent before spectral conditioning even enters.

## 4. Bounded floor charge is exactly what qualitative radial screening needs

From `NB-084`,

\[
\mathfrak J_{R,q^LR-1}
\le
\mathfrak C_{R,q,L},
\tag{29}
\]

where `mathfrak J` is the full finite-future prediction-volume charge of `NB-074`. Equation (6) and the finiteness of the sum over `j<R` give (10).

Suppose first that `mathfrak S_(R_k,q)<=M` on an unbounded sequence. For each `k`, monotone convergence in the finite sum lets us choose a finite `L_k` with

\[
\mathfrak C_{R_k,q,L_k}
\le M+1.
\tag{30}
\]

Then (29) gives a bounded full prediction-volume charge along the finite horizons `q^(L_k)R_k-1`. By `NB-074`, a nonzero stable tail would force the full charge to diverge along **every** finite horizon schedule. Hence the stable tail must vanish, proving (12).

The reverse implication in (11) is immediate from

\[
\mathfrak S_{R,q}\le\mathfrak C_{R,q,L}.
\tag{31}
\]

Therefore the radial method has two logically separate gates:

1. the **floor gate**, whether the aggregate mismatch `mathfrak S_(R,q)` stays bounded on some unbounded sequence;
2. only after that, a **rate/horizon gate**, how large `L(R)` must be to approach the floor closely enough for a desired quantitative horizon.

The second gate mattered in the fixed-schedule calibrations of `NB-081`--`NB-083`. It is not necessary for the bare qualitative contradiction with a stable tail because `NB-074` quantifies over arbitrary finite horizon schedules.

## 5. Controls, failure modes, and what is not proved

For the flat control `O=1`, `NB-084` gives

\[
W_{j,q}^{(0)}=1,
\qquad
\mathcal E_{j,q,L}^{(0)}=1,
\qquad
\widehat\Pi_{j,R}^{(0)}=1.
\tag{32}
\]

Hence

\[
G_{j,q}^{(0)}=1,
\qquad
\mathfrak S_{R,q}^{(0)}=0,
\tag{33}
\]

so the floor criterion reproduces the exact memory-free control.

The result does not give a useful uniform upper bound on `G_(j,q)/widehatPi_(j,R)^2`. Log-integrability prevents the radial infinite-depth error from vanishing, but it does not say that its positive floor matches the much richer visible prediction error generated by all intermediate innovations. That alignment is now the source-specific arithmetic question.

Nor does (13) imply a stable tail or failure of RH. The full future contains cross-ray and nonradial combinations that can beat the radial predictor. A divergent floor charge therefore falsifies only the **single-`q` radial certificate**, not the Nyman closure criterion.

Finally, no cheap depth follows from (4)--(6). The density can have deep narrow valleys while retaining an integrable logarithm, and convergence of finite Toeplitz prediction to the geometric mean can be arbitrarily slow without stronger regularity. Any polynomial-horizon theorem still needs quantitative control beyond the present result.

## 6. Prior-art boundary and consequence for the live frontier

The Szegő--Kolmogorov formula identifying the infinite one-sided linear prediction error with the geometric mean of a log-integrable spectral density is classical. A stable modern statement is given, for example, by Tryphon T. Georgiou, *The error variance of the optimal linear smoother and maximum-variance fractional pole models*, Proceedings of the 45th IEEE Conference on Decision and Control (2006), 1685--1691, DOI `10.1109/CDC.2006.377324`. The same prediction/spectral-factorization boundary underlies the stationary calibration already used in `NB-082`.

A targeted search also finds modern Nyman--Beurling work on polynomial approximation and Gram structure, including Alouges--Darses--Hillion (2022) and Carvill's 2025 Mellin-smoothed Gram analysis, but not the present source-specific combination: the exact integer-descendant periodization of `NB-084`, the proof that its aliased density satisfies the Szegő condition, and the resulting aggregate floor classification (11). No priority claim is made.

The immediate research redirect is precise. `NB-084` left the live target phrased as controlling finite Toeplitz errors at roughly a `1/R` aggregate scale. For qualitative stable-tail exclusion, `NB-085` shows that the first question is instead static:

\[
\boxed{
\text{Can }
\sum_{j<R}
\log\frac{G_{j,q}}{\widehat\Pi_{j,R}^2}
\text{ stay bounded on an unbounded sequence?}
}
\tag{34}
\]

If yes, arbitrarily large but finite radial depth is enough to kill the stable tail. If no for every fixed `q`, more depth cannot repair the route and the next source theorem must exploit cross-ray/nonradial future information. This separates a genuine arithmetic alignment problem from the secondary question of how quickly finite Toeplitz sections approach their limit.