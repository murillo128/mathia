# NB-198 — Brun–Titchmarsh phase occupancy excludes accurate positive Euler returns at every sublinear Mellin power

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-ACQUISITION + POSITIVE-EULER + POINTWISE-DEPHASING + BRUN-TITCHMARSH + NB-197-EXTENSION`.

`NB-196` and `NB-197` obtain pointwise positive-shell dephasing by approximating the actual von-Mangoldt source by continuum mass on short spatial cells. Their reach is therefore tied to a prime-number-theorem input: uniform cells give the `13/30` Mellin corridor, while discarding the sparse bad cells from an almost-all theorem gives `13/15`.

For excluding a **sufficiently accurate positive return**, however, an asymptotic prime count on each phase cell is stronger than necessary. A return already requires most of the positive Euler mass to lie in the short multiplicative windows where `t log n` is close to `2 pi Z`. The classical Brun--Titchmarsh upper bound controls how much prime mass those windows can carry even when their spatial length is only a fixed power `x^beta`. This removes the current `13/15` exponent as a pointwise barrier, at the price that the excluded return tolerance deteriorates as the Mellin exponent approaches `1`.

Fix `r_0>0`, `Delta>0`, and put

\[
x_a=e^{r_0/a},\qquad y_a=e^\Delta x_a,
\]

with the same normalized full positive von-Mangoldt shell as in `NB-197`,

\[
D_a:=\sum_{x_a\le n<y_a}\Lambda(n)n^{-1-a},
\qquad
w_{n,a}:=
\frac{\Lambda(n)n^{-1-a}}{D_a}\mathbf 1_{[x_a,y_a)}(n),
\]

and

\[
\mathcal A_a(t):=
\sum_n w_{n,a}|e^{-it\log n}-1|.
\]

Then for every fixed `0<beta<1` there are constants `eta_beta>0`, `T_beta>=1`, and `a_0>0` such that

\[
\boxed{
0<a<a_0,
\qquad
T_\beta\le |t|\le x_a^{1-\beta}
\quad\Longrightarrow\quad
\mathcal A_a(t)>\eta_\beta.
}
\tag{1}
\]

One may take, after harmlessly enlarging `T_beta` and shrinking `a_0`,

\[
\boxed{
\eta_\beta=\sin\!\left(\frac{\pi\beta}{32}\right).
}
\tag{2}
\]

Consequently, for any coupled scale `a_T->0` satisfying

\[
\boxed{
\limsup_{T\to\infty}
\frac{a_T\log(2T)}{r_0}<1,
}
\tag{3}
\]

there exists a fixed `eta>0` such that the whole physical block `[T,2T]` is eventually free of positive `eta`-returns.

The conclusion is intentionally weaker than `NB-197` in tolerance and stronger in frequency range. `NB-197` excludes **every prescribed fixed** `eta<1` through exponent `13/15-epsilon`; (1) excludes **some fixed accuracy depending on the remaining exponent margin** through every exponent `1-beta<1`. In particular, (1) does not control the near-endpoint regime `|t|=x_a^{1-o(1)}` with one fixed tolerance.

## Derivation

### 1. A small positive return forces most source mass into phase windows

By symmetry it is enough to take `t>0`. Fix `0<delta<pi` and define the favorable phase set

\[
W_{t,\delta}
:=
\left\{
 u\in[x_a,y_a):
 \operatorname{dist}(t\log u,2\pi\mathbb Z)\le\delta
\right\}.
\tag{4}
\]

Outside this set,

\[
|e^{-it\log u}-1|
\ge
q_\delta,
\qquad
q_\delta:=2\sin(\delta/2).
\tag{5}
\]

Therefore, if

\[
M_a(t,\delta)
:=
\sum_{n\in W_{t,\delta}}w_{n,a},
\tag{6}
\]

then positivity gives the exact Markov-type implication

\[
\mathcal A_a(t)\le\eta
\quad\Longrightarrow\quad
\boxed{
M_a(t,\delta)
\ge
1-\frac{\eta}{q_\delta}.
}
\tag{7}
\]

Thus it suffices to show that, throughout a prescribed sublinear Mellin-power range, the actual prime source can place at most a fixed fraction of its normalized mass in `W_(t,delta)`.

### 2. Brun--Titchmarsh bounds every favorable phase window

The connected components of (4), before truncation by the shell endpoints, are

\[
I_k
=
\left[
\exp\!\left(\frac{2\pi k-\delta}{t}\right),
\exp\!\left(\frac{2\pi k+\delta}{t}\right)
\right].
\tag{8}
\]

For a component centered at `u_k=exp(2 pi k/t)` with `u_k asy x_a`, its length is

\[
H_k
=2u_k\sinh(\delta/t)
\asymp_\delta \frac{u_k}{t}.
\tag{9}
\]

Assume

\[
t\le x_a^{1-\beta}.
\tag{10}
\]

Then uniformly over the shell,

\[
H_k\gg_\delta x_a^\beta,
\qquad
\log H_k
\ge
\beta\log x_a+O_{\beta,\delta}(1).
\tag{11}
\]

The Montgomery--Vaughan Brun--Titchmarsh interval inequality

\[
\pi(u+H)-\pi(u)
\le
\frac{2H}{\log H}
\qquad(H\ge2)
\tag{12}
\]

therefore gives, uniformly for `t>=T_beta` and for all components meeting the shell,

\[
\sum_{p\in I_k}
\frac{\log p}{p^{1+a}}
\le
\left(
\frac{2}{\beta}
+O_{\beta,\delta}\!\left(\frac1{T_\beta}\right)
+o_{a\to0}(1)
\right)
H_k u_k^{-1-a}.
\tag{13}
\]

The two shell-boundary pieces may simply be enlarged to their full components before applying (13).

It remains to sum their geometric occupation. In logarithmic coordinates `u=x_a e^v`, `0<=v<=Delta`, the favorable set is periodic with period `2 pi/t` and occupies the fraction `delta/pi` of each complete period. Since the weight is `u^{-1-a}du=x_a^{-a}e^{-av}dv`, elementary periodic averaging gives

\[
\frac{
\int_{W_{t,\delta}}u^{-1-a}\,du
}{
\int_{x_a}^{y_a}u^{-1-a}\,du
}
=
\frac{\delta}{\pi}
+O_{\Delta}\!\left(\frac1t\right)
+o_{a\to0}(1),
\tag{14}
\]

uniformly for `t>=1`. The same estimate holds if the two boundary components are completed, at the cost of the displayed `O(1/t)` term.

Combining (13)--(14), first choosing `T_beta` large and then taking `a` small, yields

\[
\sum_{\substack{x_a\le p<y_a\\p\in W_{t,\delta}}}
\frac{\log p}{p^{1+a}}
\le
\left(
\frac{2\delta}{\pi\beta}
+O_{\beta,\Delta,\delta}\!\left(\frac1{T_\beta}\right)
+o(1)
\right)
\int_{x_a}^{y_a}u^{-1-a}\,du.
\tag{15}
\]

The exact full von-Mangoldt shell causes no difficulty. As already used in `NB-197`, proper prime powers contribute

\[
\sum_{\substack{x_a\le p^m<y_a\\m\ge2}}
\frac{\log p}{p^{m(1+a)}}
\ll_{r_0,\Delta}
\frac{\log x_a}{\sqrt{x_a}}
=o(1),
\tag{16}
\]

while the prime number theorem gives

\[
D_a
=
\int_{x_a}^{y_a}u^{-1-a}\,du+o(1)
=
e^{-r_0}\Delta+o(1).
\tag{17}
\]

Hence the normalized favorable source mass satisfies

\[
\boxed{
M_a(t,\delta)
\le
\frac{2\delta}{\pi\beta}
+O_{\beta,\Delta,\delta}\!\left(\frac1{T_\beta}\right)
+o(1)
}
\tag{18}
\]

uniformly throughout (10).

### 3. A fixed exponent margin gives a fixed return gap

Take

\[
\delta_\beta:=\frac{\pi\beta}{16}.
\tag{19}
\]

Choose `T_beta` so that the `O(1/T_beta)` contribution in (18) is at most `1/16`, and then choose `a_0` so that all remaining `o(1)` terms are at most `1/16`. Since the main term is `1/8`, after enlarging constants if necessary we have the convenient uniform bound

\[
\boxed{
M_a(t,\delta_\beta)<\frac14.
}
\tag{20}
\]

Now set

\[
\eta_\beta
:=
\frac12q_{\delta_\beta}
=
\sin\!\left(\frac{\pi\beta}{32}\right).
\tag{21}
\]

If `A_a(t)<=eta_beta`, equation (7) would force

\[
M_a(t,\delta_\beta)\ge\frac12,
\]

contradicting (20). This proves (1)--(2).

The constants are not optimized. The structural point is the scaling

\[
\eta_\beta\gg\beta
\qquad(\beta\downarrow0),
\tag{22}
\]

which records exactly the loss in Brun--Titchmarsh when a phase window has spatial length only `x_a^beta`:

\[
\frac{\log x_a}{\log H_k}
\lesssim\frac1\beta.
\]

### 4. Coupled physical blocks are obstructed below exponent one

Assume (3). Choose a fixed `beta>0` such that eventually

\[
\frac{a_T\log(2T)}{r_0}
\le
1-\beta.
\tag{23}
\]

Because `log x_(a_T)=r_0/a_T`, (23) is equivalent to

\[
2T\le x_{a_T}^{1-\beta}.
\tag{24}
\]

Also `T>=T_beta` and `a_T<a_0` eventually. Equation (1) then applies to every `t in [T,2T]`, proving the block consequence.

This strictly strengthens the **range** of the current positive-return obstruction: no fixed-power corridor below the full Mellin scale can support arbitrarily accurate positive Euler recurrence. The remaining positive-return frontier is compressed to the endpoint layer

\[
\frac{a_T\log T}{r_0}\to1
\]

(or beyond), where the phase windows become `x_a^{o(1)}`-short and the Brun--Titchmarsh logarithmic denominator no longer yields a fixed occupancy gap.

## Stress tests and limits

The result does **not** improve the `NB-197` statement for a prescribed large tolerance. If `beta` is small, the certified `eta_beta` is small. Thus `NB-197` remains stronger throughout its `13/15` corridor when the application requires excluding an arbitrary fixed `eta<1`.

Positivity is load-bearing twice: first in (7), which converts small average chord length into concentration of source mass, and second in bounding the omitted proper-prime-power contribution by absolute mass. A signed or complex coefficient aggregate can cancel across phase windows and is not constrained by this occupancy argument. The source-faithful signed-synthesis frontier after `NB-187`--`NB-193` therefore remains open.

The endpoint `beta=0` is also genuinely outside the proof. At `t asy x_a`, a favorable phase component has bounded spatial length, and Brun--Titchmarsh gives no fixed fractional upper bound relative to the full Euler shell. The theorem does not exclude isolated positive returns in the `x_a^{1-o(1)}` layer, nor does it assert that any such returns exist.

Finally, (1) is a source-acquisition obstruction, not an approximation theorem for the complete Nyman span. No conclusion about the optimal Nyman distance or RH follows without a separate theorem forcing a successful approximation architecture to realize one of these positive shell returns.

## Prior-art and representation boundary

The load-bearing external input is classical Brun--Titchmarsh in arbitrary intervals. Montgomery and Vaughan's large-sieve proof gives (12); later explicit refinements improve constants but do not change the fixed-power mechanism used here. The idea of slicing primes according to the phase of `p^{it}` and controlling the slices with Brun--Titchmarsh also appears in pretentious multiplicative-number-theory arguments, so **no novelty is claimed for that phase-window device itself**.

The line-specific derived statement is the transfer of that device to the normalized positive Euler-Wiener shell used in `NB-189`--`NB-197`, including the explicit tradeoff between a Mellin exponent margin `beta` and a certified source-return gap `eta_beta`, and the coupled-block consequence (3). Searches for Nyman--Beurling/Euler-shell recurrence combined with Brun--Titchmarsh did not locate this exact formulation.

The representation audit is correspondingly narrow. The inequality behind (18) is a generic upper-density fact about a positive prime-supported measure; replacing the primes by any support enjoying the same short-interval sieve upper bound would give the same geometry. What is source-specific here is that the actual Nyman acquisition channel carries von-Mangoldt mass on prime powers, proper powers are negligible on the chosen exponential shell, and the Mellin phase is exactly `t log n`. This finding should therefore be used as a **source-fidelity obstruction**, not as a new intrinsic Hilbert-space theorem.

## Consequence for the research frontier

`NB-194`--`NB-197` asked how far increasingly strong prime-density inputs could push pointwise dephasing. `NB-198` shows that for the narrower but operationally important question of **arbitrarily accurate positive recurrence**, a prime-number-theorem asymptotic is unnecessary: a sieve upper bound already reaches every fixed exponent below one.

The positive recurrence escape is therefore no longer “improve `13/15` by importing a shorter almost-all PNT.” It is specifically an **endpoint problem**: can the true source admit useful returns when `t=x_a^{1-o(1)}`, where the favorable spatial windows have subpower length and the certified tolerance from Brun--Titchmarsh collapses? Independently, the signed/complex aggregation route remains outside all positive-occupancy arguments and continues to require its own source-faithful obstruction or construction.
