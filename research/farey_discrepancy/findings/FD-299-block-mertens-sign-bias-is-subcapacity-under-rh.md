# FD-299 — Block-Mertens sign bias is subcapacity under RH

- **Date:** 2026-09-24
- **Status:** proved conditional sign-bias suppression and one-sided near-capacity reduction
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens field / signed band bias / replication probability / sublinear moments / RH Mertens growth / one-sided repair / hard-complement rigidity
- **Depends on:** FD-234, FD-261, FD-264, FD-265, FD-298
- **Classification:** `EXACT-DERIVED + SUBLINEAR-MOMENT-BOUND + RH-CONDITIONAL + SIGN-BIAS-SUBCAPACITY + ONE-SIDED-REDUCTION + RIGID-COMPLEMENT-TRANSFER`

## Claim

FD-298 reduces the low-height zero-safe hard-complement problem, below the aggregate rigidity floor, to the original block-Mertens field

\[
G_N(d)=\sum_{q\mid d}U_N(q),
\qquad
U_N(q)=M(Nq)-M(N(q-1)).
\tag{1}
\]

FD-265 shows that the remaining physical source question is one-sided: a large `l^1` field could in principle be cheap for a positive cushion if its mass were almost completely polarized in the favorable sign. The exact signed statistic controlling that escape is

\[
L_N(x):=\sum_{x<d\le2x}|G_N(d)|,
\qquad
S_N(x):=\sum_{x<d\le2x}G_N(d).
\tag{2}
\]

The sign-polarization escape is unavailable at the current near-capacity scale under RH.

Let

\[
m_x(q)
:=
\#\{d:x<d\le2x,\ q\mid d\}
=
\left\lfloor\frac{x}{q}+\frac12\right\rfloor,
\tag{3}
\]

and, as in FD-264,

\[
w_x(q):=m_x(q)-m_x(q+1),
\qquad
\pi_x(q):=\frac{w_x(q)}x,
\qquad
1\le q\le2x,
\tag{4}
\]

with `m_x(2x+1)=0`. Then `w_x(q)>=0` and `sum_q pi_x(q)=1`. FD-264 gives the exact identity

\[
\boxed{
S_N(x)
=
\sum_{q\le2x}M(Nq)w_x(q)
=
x\,\mathcal P_x[M(N\,\cdot)].
}
\tag{5}
\]

The new input is that this probability law has uniformly bounded moments of every order strictly below one:

\[
\boxed{
\sup_{x\ge1}
\sum_{q\le2x}\pi_x(q)q^\alpha
<\infty
\qquad(0\le\alpha<1).
}
\tag{6}
\]

Consequently, if for some fixed `theta<1`

\[
M(y)\ll_\varepsilon y^{\theta+\varepsilon}
\qquad
\text{for every }\varepsilon>0,
\tag{7}
\]

then in every fixed polynomial-depth regime `x=N^{lambda+o(1)}`, `lambda>0`,

\[
\boxed{
|S_N(x)|
\le
N^{\theta}x^{1+o(1)}.
}
\tag{8}
\]

Under RH, the classical Littlewood criterion gives (7) with `theta=1/2`, hence

\[
\boxed{
|S_N(x)|
\le
N^{1/2}x^{1+o(1)}.
}
\tag{9}
\]

Now put

\[
\beta:=\log_2\frac32,
\qquad
c:=1-\beta=0.4150374992\ldots,
\tag{10}
\]

and use the FD-298 near-capacity budget

\[
B_{N,x}
:=
\frac{N^{1/2}x^{1+c}}{\ell(x)},
\qquad
\ell(x)\to\infty,
\qquad
\ell(x)=x^{o(1)}.
\tag{11}
\]

Then (9) gives

\[
\boxed{
\frac{|S_N(x)|}{B_{N,x}}
=
x^{-c+o(1)}
\longrightarrow0.
}
\tag{12}
\]

Thus the positive and negative masses of the block-Mertens field satisfy

\[
\boxed{
\sum_{x<d\le2x}(G_N(d))_+
=
\frac12L_N(x)+o(B_{N,x}),
}
\tag{13}
\]

and

\[
\boxed{
\sum_{x<d\le2x}(-G_N(d))_+
=
\frac12L_N(x)+o(B_{N,x}).
}
\tag{14}
\]

In particular, on every family for which `L_N(x)>=delta B_{N,x}` with fixed `delta>0`, both signs carry asymptotically one half of the `l^1` mass. Near-total sign polarization is impossible.

For the canonical real full-grid repair of FD-234,

\[
\widetilde c_N(d)=-\frac12G_N(d),
\tag{15}
\]

so the FD-265 one-sided negative demand becomes

\[
\boxed{
\sum_{x<d\le2x}(-\widetilde c_N(d))_+
=
\frac14L_N(x)+o(B_{N,x}).
}
\tag{16}
\]

The nearest-integer repair differs from (16) by only `O(x log x)=o(B_{N,x})`, so the same near-capacity classification holds after rounding.

Finally, in the FD-298 rigidity regime the zero-safe hard complements satisfy uniformly

\[
\|\mathcal R_{T,N}-G_N\|_{1,x}=o(B_{N,x}).
\tag{17}
\]

Since positive and negative parts are `1`-Lipschitz in `l^1`, equations (13)--(14) transfer to the entire zero-safe hard-complement path:

\[
\boxed{
\sum_{x<d\le2x}(\mathcal R_{T,N}(d))_+
=
\frac12L_N(x)+o(B_{N,x}),
}
\tag{18}
\]

\[
\boxed{
\sum_{x<d\le2x}(-\mathcal R_{T,N}(d))_+
=
\frac12L_N(x)+o(B_{N,x}),
}
\tag{19}
\]

uniformly over the FD-298 zero-safe low-height range.

Therefore the one-sided sign geometry left open by FD-265 and FD-298 is not an independent near-capacity obstruction under RH. **At the scale relevant to the current low-height route, the source and every rigid hard complement are sign-balanced up to a polynomially smaller error. The remaining source-side gate is the post-convolution magnitude `L_N(x)`, not sign polarization.**

## 1. The replication probability has bounded sublinear moments

FD-264 proves that `m_x(q)` is nonincreasing and that (4) is a probability measure. For `0<alpha<1`, summation by parts gives

\[
\begin{aligned}
\sum_{q=1}^{2x}q^\alpha w_x(q)
&=
 m_x(1)
 +
 \sum_{q=2}^{2x}
 \bigl(q^\alpha-(q-1)^\alpha\bigr)m_x(q).
\end{aligned}
\tag{20}
\]

Here `m_x(1)=x`, while

\[
m_x(q)
\le
\frac{x}{q}+\frac12
\tag{21}
\]

and

\[
q^\alpha-(q-1)^\alpha
\ll_\alpha q^{\alpha-1}.
\tag{22}
\]

Therefore

\[
\begin{aligned}
\sum_{q=1}^{2x}q^\alpha w_x(q)
&\ll_\alpha
x
+
x\sum_{q=2}^{2x}q^{\alpha-2}
+
\sum_{q=2}^{2x}q^{\alpha-1}\\
&\ll_\alpha
x+x+x^\alpha\\
&\ll_\alpha x.
\end{aligned}
\tag{23}
\]

Dividing by `x` proves (6). The case `alpha=0` is just `sum pi_x=1`.

The threshold `alpha<1` is structural for this elementary argument. At `alpha=1`, the same computation gives a logarithmic first moment rather than a uniform constant. The current RH exponent `1/2` lies safely inside the bounded-moment range.

## 2. RH Mertens growth loses no divisor-depth power after averaging

Assume (7), and fix `epsilon>0` small enough that

\[
\alpha:=\theta+\varepsilon<1.
\tag{24}
\]

Using positivity of `w_x`, (5), and (6),

\[
\begin{aligned}
|S_N(x)|
&\le
\sum_{q\le2x}w_x(q)|M(Nq)|\\
&\ll_\varepsilon
N^{\theta+\varepsilon}
\sum_{q\le2x}w_x(q)q^{\theta+\varepsilon}\\
&\ll_{\theta,\varepsilon}
N^{\theta+\varepsilon}x.
\end{aligned}
\tag{25}
\]

Because `epsilon` may be chosen arbitrarily small and `x=N^{lambda+o(1)}` with fixed `lambda>0`, (25) is exactly the exponent statement (8).

Under RH, Titchmarsh--Heath-Brown Theorem 14.25(C), already anchored in `SOURCES.md` for this research line, gives

\[
M(y)=O_\varepsilon(y^{1/2+\varepsilon})
\tag{26}
\]

for every fixed `epsilon>0`. Substituting `theta=1/2` proves (9).

This is stronger than applying the maximum bound in FD-264. The crude estimate

\[
|\mathcal P_x[M(N\,\cdot)]|
\le
\max_{q\le2x}|M(Nq)|
\]

would pay an extra factor `x^{1/2+o(1)}` under RH. Equation (6) removes that factor because the replication probability is heavily concentrated at small scale indices and has finite square-root moment.

## 3. One-sided source mass collapses to total variation at near-capacity scale

For any real field `g_d`,

\[
\sum g_d^+
=
\frac12
\left(
\sum|g_d|+
\sum g_d
\right),
\qquad
\sum(-g_d)^+
=
\frac12
\left(
\sum|g_d|-
\sum g_d
\right).
\tag{27}
\]

Applying (27) to `G_N`, equations (2) and (12) immediately give (13)--(14).

This closes the specific triangle-saturation escape isolated in FD-265 at the FD-298 scale. If `L_N(x)` is itself of order `B_{N,x}` or larger, then

\[
\frac{S_N(x)}{L_N(x)}\longrightarrow0,
\tag{28}
\]

not `-1`. The divisor-smoothed source cannot become almost entirely nonpositive, nor almost entirely nonnegative. Its two one-sided masses are asymptotically equal at the scale that matters for the current hard-complement route.

For the real repair, (15) and (27) give exactly

\[
\sum(-\widetilde c_N)_+
=
\frac14(L_N+S_N),
\tag{29}
\]

which is the FD-265 identity. Combining (12) with (29) proves (16). For the rounded repair `c_N=\widetilde c_N+r_N`, FD-234 gives `|r_N(d)|<=tau(d)`, and the negative-part map is `1`-Lipschitz. Hence

\[
\left|
\sum(-c_N)_+
-
\sum(-\widetilde c_N)_+
\right|
\ll
x\log x.
\tag{30}
\]

In the polynomial-depth regime,

\[
\frac{x\log x}{B_{N,x}}
=
o(1),
\tag{31}
\]

so rounding does not reopen the sign escape.

## 4. The same one-sided classification transfers to rigid hard complements

For real numbers `a,b`,

\[
|a_+-b_+|\le|a-b|,
\qquad
|(-a)_+-(-b)_+|\le|a-b|.
\tag{32}
\]

Summing coordinatewise over the band gives, for any fields `f,g`,

\[
\left|
\sum f_+-\sum g_+
\right|
\le
\|f-g\|_1,
\tag{33}
\]

and the same bound for negative parts.

FD-298 proves (17) throughout the low-height zero-safe rigidity regime, under its RH, simple-zero, complete-cluster background, and packet-subcriticality hypotheses. Taking `f=mathcal R_{T,N}` and `g=G_N` in (33), then using (13)--(14), proves (18)--(19).

This is stronger than norm equivalence alone. FD-298 already says that the hard complement cannot become `l^1`-small merely by moving the cutoff through the rigid low-height range. The present result says that it cannot become **one-sided-small** there either, provided the block-Mertens total variation is at near-capacity scale. Any one-sided gain of order `B_{N,x}` would contradict (17) together with the RH sign-bias estimate.

## 5. Adversarial review and boundary

The moment estimate (6) is exact and unconditional, but the subcapacity conclusion uses a power-growth hypothesis for `M`; the stated `theta=1/2` application is RH-conditional. No simple-zero hypothesis enters (6)--(16). Simplicity is inherited only when the result is transferred to the FD-298 hard-complement path in (17)--(19).

The restriction `theta<1` is essential to this proof. At the endpoint `theta=1`, the replication probability has a logarithmically growing first moment, so (25) acquires a logarithm. This finding does not claim an unconditional analogue of the RH-scale estimate.

The complete integer band `x<d<=2x` and the FD-264 endpoint convention are also essential to the exact probability law. Changing the band or smoothing its endpoints changes the replication weights and requires a fresh moment calculation.

Most importantly, the result supplies **no lower bound for `L_N(x)`**. It does not prove that the canonical repair exceeds the available physical cushion, nor that the Farey discrepancy route closes. It removes only the sign-polarization loophole: once post-convolution variation reaches the relevant budget scale, one-sided mass automatically carries the same scale up to a fixed factor.

Likewise, (18)--(19) are only as broad as FD-298's rigidity theorem. They do not control hard cutoffs above the aggregate rigidity floor, nor moving spectral packets outside the hypotheses used there.

A counterexample to the central new claim would therefore have to break the bounded-moment estimate (6), the classical RH Mertens growth (26), or the exact FD-264 signed identity (5). The first follows directly from the monotone replication count, the second is the already-anchored RH criterion, and the third was proved exactly in FD-264. No sign-independence or probabilistic model for Möbius values is used.

## Prior-art and source hygiene

No new external theorem is load-bearing. The only external analytic input is the standard RH consequence `M(y)=O_epsilon(y^(1/2+epsilon))`, already anchored in `research/farey_discrepancy/SOURCES.md` to Titchmarsh--Heath-Brown, Theorem 14.25(C). The bounded-moment estimate and its transfer through the FD-264 replication probability are elementary deductions internal to this research line. No update to `SOURCES.md` is required.

**Verdict.** Under RH, the signed bias of the divisor-smoothed block-Mertens field is smaller than the FD-298 near-capacity budget by the full depth factor `x^(1-beta)` up to subpowers. Therefore a capacity-scale block field cannot evade one-sided repair demand by sign polarization. In the low-height rigid regime, the same statement holds for every zero-safe hard complement. The live arithmetic gate is now a lower bound for the post-convolution variation `L_N(x)` (or a stronger coordinate-level obstruction), not control of the signed band mean.