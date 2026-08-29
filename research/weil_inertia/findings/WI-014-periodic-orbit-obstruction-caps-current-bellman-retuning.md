# WI-014 — a period-one orbit caps the current seven-point Bellman retuning below 67.4%

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE` for the specific `alpha=1.47` seven-point Bellman/coboundary plus trace--energy block-envelope architecture used by `tawanerguo-cn/zeta-simple-zeros`. The load-bearing obstruction is the classical fact that a coboundary has zero sum on every periodic orbit. The quantitative `0.674` ceiling below is an exact Mathia deduction from the published local coefficient ledger, the cosine-window kernel, and the already audited WI-011 trace--energy envelope. It does **not** constrain a different window, a different local potential/horizon or pressure budget, the unrestricted global Fenchel witnesses of WI-012, support `>1`, or a new off-line-pair bridge.

## 1. Precise obstruction

Fix the nonnegative cosine profile used by the public Bellman construction,

\[
v_a(s)=\cos(as),\qquad a=\frac{147}{100},\qquad |s|\le\frac12,
\]

and write

\[
H_a=2-\frac1{c_1(v_a)}.
\]

The seven-point local functional in `BELLMAN_COBBOUNDARY_PROOF.md` has six consecutive gaps. Its pressure coefficients have total

\[
P=\sum_{i=1}^6 p_i=\frac1{320},
\tag{1}
\]

and at each pair span `s=1,...,6` its pair coefficients have total `2`. The Bellman improvement replaces the base local functional `F_0` by

\[
F_B(g_1,\ldots,g_6)
=F_0(g_1,\ldots,g_6)
+U(g_2,\ldots)-U(g_1,\ldots),
\tag{2}
\]

with a finite-memory coboundary. The same conclusion below holds for any finite-memory retuning of this local potential whose correction telescopes in this way.

Evaluate on the period-one gap configuration

\[
\boxed{g_i=2\quad\text{for every }i.}
\tag{3}
\]

Every shifted state is identical, so the coboundary in (2) is exactly zero. Hence any pointwise certificate

\[
F_B(g)\ge c\qquad(g_i\ge0)
\]

must satisfy

\[
\boxed{c\le c_2:=F_0(2,\ldots,2).}
\tag{4}
\]

Thus Bellman/subaction optimization can redistribute the local reward, but it cannot raise its floor above the cycle mean of this explicit periodic orbit.

## 2. Exact value of the period-one obstruction

For the cosine profile, the normalized overlap kernel is

\[
k_a(x)=
\frac{\int_{-1/2}^{1/2}\cos(as)\cos(2\pi xs)\,ds}
{\int_{-1/2}^{1/2}\cos(as)\,ds},
\qquad w_a(x)=k_a(x)^2.
\]

At every positive integer `j`, product-to-sum gives the exact identity

\[
\boxed{
 k_a(j)=\frac{(-1)^{j+1}a^2}{4\pi^2j^2-a^2},
\qquad
 w_a(j)=\frac{a^4}{(4\pi^2j^2-a^2)^2}.
}
\tag{5}
\]

On (3), the pressure contribution is `2P=1/160`, while every span-`s` pair distance is `2s` and the total pair coefficient at that span is `2`. Therefore

\[
\boxed{
 c_2=
 \frac1{160}
 +2a^4\sum_{s=1}^{6}\frac1{(16\pi^2s^2-a^2)^2}.
}
\tag{6}
\]

Numerically, only for orientation,

\[
c_2=0.0066655305618222261496\ldots.
\]

The current directed certificate proves `c=577/100000=0.00577`, so the period-one orbit leaves some room for retuning, but only a small finite amount.

A completely elementary rational upper bound suffices for the barrier below. Using

\[
\pi>\frac{157}{50}
\]

and `a=147/100`,

\[
16\pi^2s^2-a^2
>s^2\left(16\left(\frac{157}{50}\right)^2-a^2\right)
=s^2\frac{1555927}{10000}.
\]

Hence

\[
w_a(2s)
<\frac{466948881}{1555927^2}\frac1{s^4}.
\]

Summing only `s=1,...,6` gives

\[
 c_2
 <\frac1{160}
 +2\frac{466948881}{1555927^2}
 \sum_{s=1}^{6}\frac1{s^4}
 =\frac{1291227122568661}{193672706346320000}
 <\boxed{\frac{67}{10000}}.
\tag{7}
\]

The final strict inequality has exact margin

\[
\frac{6380009951683}{193672706346320000}>0.
\]

## 3. A rational upper bound for the baseline `H_a`

The same cosine-window formulas used in the public proof are

\[
I_0=\frac{2\sin(a/2)}a,
\qquad
I_2=\frac12+\frac{\sin a}{2a},
\]

\[
J=-\frac{2I_2}{a^2}
+\left(\frac{\sin(a/2)}a+\frac{2\cos(a/2)}{a^2}\right)I_0,
\qquad
H_a=2-\frac{I_2+J}{I_0^2}.
\tag{8}
\]

For completeness, the numerical value of `H_a` is not needed as an uncertified input. Put `x=a/2=147/200` and use the alternating Taylor bounds

\[
L_x=x-\frac{x^3}{6}+\frac{x^5}{120}-\frac{x^7}{5040}
\le\sin x
\le
U_x=x-\frac{x^3}{6}+\frac{x^5}{120},
\]

\[
C_x=1-\frac{x^2}{2}+\frac{x^4}{24}-\frac{x^6}{720}
\le\cos x,
\]

and

\[
L_a=a-\frac{a^3}{6}+\frac{a^5}{120}-\frac{a^7}{5040}
\le\sin a.
\]

Since `1-2/a^2>0`, (8) gives the lower bound

\[
I_2+J\ge
\left(1-\frac2{a^2}\right)
\left(\frac12+\frac{L_a}{2a}\right)
+\left(\frac{L_x}{a}+\frac{2C_x}{a^2}\right)
\frac{2L_x}{a},
\]

while `I_0<=2U_x/a`. Direct rational simplification yields

\[
\frac{I_2+J}{I_0^2}
>\frac{6637}{5000},
\]

with exact positive margin

\[
\frac{5987298733083831133259088467}
{130935229516843608542553600000000}.
\]

Therefore

\[
\boxed{H_a<\frac{3363}{5000}=0.6726.}
\tag{9}
\]

## 4. Propagation through the trace--energy block envelope

For a block of `m>=7` simple critical zeros, the present seven-point assembly sums `m-6` local inequalities. If the local floor is `c`, then

\[
A=c(m-6),
\qquad
d=\frac{m-6}{m}\in(0,1),
\]

and the nonnegative pressure tax per zero is `Pd`. The WI-011 trace--energy envelope gives the certified-proportion expression

\[
R_m(c)=
\frac{H_a-Pd}
{1-\Phi_m(A)/m},
\tag{10}
\]

where

\[
\Phi_m(A)=
\begin{cases}
A,&A\le m/(m-1),\\
2\sqrt{(m-1)A/m}-1+A/m,&A\ge m/(m-1).
\end{cases}
\]

For every `A>=0`,

\[
\boxed{\Phi_m(A)\le A.}
\tag{11}
\]

On the second branch this is just

\[
2\sqrt{rA}-1\le rA,
\qquad r=\frac{m-1}{m},
\]

equivalent to `(sqrt(rA)-1)^2>=0`.

Combining (4), (10), and (11), whenever the numerator is positive,

\[
R_m(c)
\le
\frac{H_a-Pd}{1-cd}
\le
\frac{H_a-Pd}{1-c_2d}.
\tag{12}
\]

If the numerator were nonpositive the desired upper bound is trivial. The right side of (12) is fractional-linear in `d`, so its maximum on `0<=d<=1` occurs at an endpoint. Hence

\[
\boxed{
R_m(c)
\le
\max\left\{
H_a,
\frac{H_a-P}{1-c_2}
\right\}.
}
\tag{13}
\]

Using only the rigorous coarse bounds (7), (9), and `P=1/320`,

\[
H_a<\frac{3363}{5000}<\frac{337}{500},
\]

and

\[
\frac{H_a-P}{1-c_2}
<
\frac{3363/5000-1/320}{1-67/10000}
=
\frac{26779}{39732}
<\boxed{\frac{337}{500}=0.674}.
\tag{14}
\]

The last margin is exactly

\[
\frac{337}{500}-\frac{26779}{39732}
=\frac{23}{2483250}>0.
\]

Therefore:

\[
\boxed{
\text{no finite-memory coboundary retuning of this same seven-point}
\atop
\text{`alpha=1.47`, `P=1/320` local potential, passed through the same}
\atop
\text{trace--energy block envelope, can certify }67.4\%.
}
\tag{15}
\]

If one evaluates the exact quantities in (6) and (8), the endpoint in (13) is approximately

\[
0.6738251112732444\ldots,
\]

but the durable exact claim here is the simpler strict ceiling `R_m<0.674`.

## 5. Why this is not merely a numerical limitation

The obstruction is not that the current interval search failed to find a better `U`. Equation (4) holds for **every** coboundary because the constant-gap orbit is fixed by the shift. No amount of Bellman/subaction retuning can alter its cycle average.

This is the finite-state/ergodic-optimization periodic-orbit obstruction in its simplest form. The `trmdy/zeta-simple-zeros-673137` second campaign already uses periodic-orbit cycle means as mandatory pre-screens for transfer-operator certificates and reports related horizon ceilings. Thus no novelty is claimed for the cycle-mean principle itself. The new Mathia contribution is the explicit exact specialization (6)--(15) to the current `alpha=1.47` seven-point Bellman theorem and the propagation through the audited trace--energy envelope.

The result also explains why the public follow-up optimizations change the profile, horizon, or assembly rather than merely tuning the existing coboundary: the period-one orbit is invariant under the latter operation.

## 6. Boundaries and ways to evade the obstruction

This finding is intentionally narrow.

- **Different window/profile:** changing `a`, or using a multi-cosine profile, changes `H`, the kernel, and the periodic-orbit energy. The `trmdy` candidate does exactly this.
- **Different local potential/horizon or pressure budget:** a nine-point or otherwise redesigned certificate is not covered by (15).
- **Global Fenchel/Bellman assembly:** WI-012 allows cross-boundary connection-Laplacian witnesses and is not restricted to the present seven-point local energy. Its periodic ground states must be audited separately.
- **Off-line-pair pricing:** (15) says nothing about a new invariant that charges or virtualizes off-line hyperbolic pairs; that is a genuinely different route toward the exceptional complement.
- **Wider support/new arithmetic:** support `>1` can change the available zero-side information and is outside this barrier.

A falsification is therefore concrete: exhibit an implementation claimed to remain within the exact hypotheses above whose local certificate floor exceeds (6), or whose block conversion beats (10) while retaining the same pressure and trace--energy ledger. The former would contradict the period-one evaluation; the latter would have to identify a genuinely stronger assembly step rather than a Bellman retuning.

## 7. Consequence for the research line

The current seven-point Bellman certificate can still be sharpened numerically, but **retuning its coboundary alone cannot be the route to a qualitatively larger simple-critical-zero proportion**. Even a perfect local solver remains below `67.4%` under the same block envelope.

This reinforces two distinct live directions already isolated by WI-012 and WI-005--WI-007:

\[
\boxed{
\text{support-one improvement: change the global spectral assembly/profile}
}
\]

or

\[
\boxed{
\text{exceptional-mass attack: add a genuinely new off-line/multiplicity observable.}
}
\]

Simply optimizing the existing Bellman potential more aggressively is now a closed route for any target at or above `67.4%`.
