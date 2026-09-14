# FD-124 — Cesàro Fourier-skeleton saturation forces superexponential horizon growth

**Status:** `EXACT-DERIVED + FLOOR-QUOTIENT-FOURIER-SKELETON + UNBOUNDED-RATIO-MULTIHORIZON + HORIZON-ENTROPY-OBSTRUCTION + POLYNOMIAL-SOURCE-CESARO-GAP + SUPEREXPONENTIAL-NECESSITY + ROUTE-NARROWING`.

`FD-123` proves that a polynomial-growth common source cannot Cesàro-saturate the minimal floor-quotient Fourier skeleton along an integer-ratio chain whose transition ratios are bounded. Its explicit remaining loophole is that rare very large jumps can evade every fixed ratio ceiling. The ceiling is not load-bearing.

For an arbitrary integer-ratio chain, finite average logarithmic horizon growth already forces a positive Cesàro skeleton deficit. Large jumps can be discarded at a cost measured by their logarithmic entropy; near-saturated nonsquarefree stages consume the same entropy through the long-range endpoint amplification from `FD-123`; and the bounded squarefree stages that remain pay the `FD-122` pair gap. Therefore Cesàro saturation is possible only if the retained horizons become superexponentially sparse in their index.

Retain the `FD-118`--`FD-123` notation

\[
\mathcal Q_H
:=
\left\{\left\lfloor\frac Hm\right\rfloor:1\le m\le H\right\},
\qquad
A_H(k)
:=
\sum_{d\mid k}d\,Y\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\tag{1}
\]

\[
\mathcal E_H^{\mathcal Q}(Y)
:=
\sum_{k\in\mathcal Q_H}\frac{|A_H(k)|^2}{k^2},
\qquad
\Delta_H(Y)
:=
\mathcal E_H^{\mathcal Q}(Y)-|Y(H)|^2
\ge0,
\tag{2}
\]

and

\[
S_H(Y)
:=
\begin{cases}
\dfrac{|Y(H)|^2}{\mathcal E_H^{\mathcal Q}(Y)},&
\mathcal E_H^{\mathcal Q}(Y)>0,\\[1.2ex]
0,&
\mathcal E_H^{\mathcal Q}(Y)=0.
\end{cases}
\tag{3}
\]

Thus `0<=S_H<=1`; if `Y(H)\ne0`,

\[
\frac{\Delta_H(Y)}{|Y(H)|^2}
=
\frac1{S_H(Y)}-1.
\tag{4}
\]

Let

\[
H_j=q_jH_{j-1},
\qquad q_j\in\mathbb Z_{\ge2},
\tag{5}
\]

with no upper bound on `q_j`, and suppose only that

\[
|Y(n)|\le Cn^\alpha
\qquad(C>0,\ \alpha\ge0).
\tag{6}
\]

Define the average logarithmic horizon growth

\[
\Lambda_n
:=
\frac1n\log\frac{H_n}{H_0}
=
\frac1n\sum_{j=1}^n\log q_j.
\tag{7}
\]

Then

\[
\boxed{
\frac1{n+1}\sum_{j=0}^{n}S_{H_j}(Y)\longrightarrow1
\quad\Longrightarrow\quad
\Lambda_n\longrightarrow\infty.
}
\tag{8}
\]

Equivalently, Cesàro saturation by a polynomial-growth common source forces

\[
\boxed{
\forall L<\infty,\qquad
H_n>H_0e^{Ln}
\quad\text{eventually}.
}
\tag{9}
\]

For the physical source `Y=M`, the trivial bound `|M(n)|\le n` supplies (6) with `alpha=1`. Hence (8)--(9) are unconditional for the Mertens staircase.

## 1. Quantitative contrapositive at finite logarithmic horizon density

The stronger statement is local to any subsequence on which the horizon entropy stays bounded. Fix `L<infinity` and suppose an infinite subsequence `n_k` satisfies

\[
\Lambda_{n_k}\le L.
\tag{10}
\]

Choose an integer `B>=2` and `0<theta<1`. Put

\[
Z:=\zeta(2),
\qquad
r_\theta
:=
\left(1+\frac{\theta^2}{Z}\right)^{-1},
\qquad
a_\theta:=1-r_\theta
=\frac{\theta^2}{Z+\theta^2}.
\tag{11}
\]

For every fixed squarefree `q>1`, `FD-122` supplies an explicit `c_q>0` and a finite threshold beyond which

\[
\Delta_H(Y)+\Delta_{qH}(Y)
\ge
c_q\bigl(|Y(H)|^2+|Y(qH)|^2\bigr).
\tag{12}
\]

Since only finitely many squarefree `q<=B` occur, define

\[
c_B^{\rm sf}
:=
\min_{\substack{2\le q\le B\\q\text{ squarefree}}}c_q
>0,
\qquad
\delta_B^{\rm sf}
:=
\frac{c_B^{\rm sf}}{1+c_B^{\rm sf}},
\qquad
b_B:=\frac{\delta_B^{\rm sf}}2.
\tag{13}
\]

Finally set

\[
c_{\alpha,L}(B,\theta)
:=
1-
\frac{L}{\log B}
-
\frac{\alpha L}{\log(1/\theta)}.
\tag{14}
\]

Whenever `c_(alpha,L)(B,theta)>0`, one has

\[
\boxed{
\liminf_{k\to\infty}
\frac1{n_k+1}
\sum_{j=0}^{n_k}
\bigl(1-S_{H_j}(Y)\bigr)
\ge
\Gamma_{\alpha,L}(B,\theta)>0,
}
\tag{15}
\]

where the explicit choice

\[
\boxed{
\Gamma_{\alpha,L}(B,\theta)
:=
\frac{a_\theta b_B}{a_\theta+b_B}
\,c_{\alpha,L}(B,\theta)
}
\tag{16}
\]

is valid. Such parameters always exist for finite `L`: take `B` sufficiently large and then `theta` sufficiently small. For example, `B>e^{4L}` and, when `alpha L>0`, `theta<e^{-4\alpha L}` make the two losses in (14) each smaller than `1/4`; if `alpha=0`, the second loss is absent.

Thus a return of `Lambda_n` to any bounded range forces a fixed positive average skeleton deficit along the same subsequence.

## 2. Rare large jumps cost logarithmic horizon entropy

Let

\[
L_B(n)
:=
\#\{1\le j\le n:q_j>B\}.
\tag{17}
\]

Each counted transition contributes at least `log B` to (7), so

\[
L_B(n)\log B
\le
\sum_{j=1}^n\log q_j
=n\Lambda_n.
\tag{18}
\]

Along (10),

\[
\boxed{
\limsup_{k\to\infty}
\frac{L_B(n_k)}{n_k}
\le
\frac{L}{\log B}.
}
\tag{19}
\]

This removes the fixed transition ceiling from `FD-123`: very large ratios may be ignored entirely, because finite average logarithmic growth makes their density arbitrarily small once `B` is chosen large.

## 3. Near-saturated nonsquarefree stages consume the same entropy

`FD-123`, using the coordinate-stability inequality of `FD-122`, proves the long-range relation

\[
\left|
\frac{Y(H_i)}{Y(H_j)}
\right|
\le
\sqrt{
Z\left(\frac1{S_{H_j}}-1\right)
}
\qquad
(i<j,\ q_j\text{ nonsquarefree}),
\tag{20}
\]

whenever `S_(H_j)>0`. The reason is exact: `H_j/H_i` is then a nonsquarefree floor-quotient coordinate at horizon `H_j`, it samples `Y(H_i)`, and the Möbius equality ray vanishes there.

Let

\[
G_\theta(n)
:=
\#\{1\le j\le n:
q_j\text{ nonsquarefree and }S_{H_j}\ge r_\theta\}.
\tag{21}
\]

Enumerate these indices as `g_1<g_2<...`. By (11) and (20), consecutive counted endpoints satisfy

\[
|Y(H_{g_m})|
\ge
\theta^{-1}|Y(H_{g_{m-1}})|.
\tag{22}
\]

Every counted endpoint is nonzero, so iteration followed by (6) gives

\[
G_\theta(n)\log(1/\theta)
\le
\alpha\log H_n+O_Y(1).
\tag{23}
\]

Along (10), therefore,

\[
\boxed{
\limsup_{k\to\infty}
\frac{G_\theta(n_k)}{n_k}
\le
\frac{\alpha L}{\log(1/\theta)}.
}
\tag{24}
\]

No bound on the individual ratios enters (20)--(24). Repeated nonsquarefree near-saturation spends endpoint-growth budget, and polynomial source growth converts that budget directly into logarithmic horizon entropy.

## 4. Bounded squarefree stages supply the complementary gap

Let

\[
N_B^{\rm sf}(n)
:=
\#\{1\le j\le n:q_j\le B\text{ and }q_j\text{ squarefree}\}.
\tag{25}
\]

Because `B` is fixed and `H_j\to\infty`, the finite thresholds in `FD-122` are absorbed after finitely many stages. For every sufficiently late transition counted by (25), (12) implies

\[
\boxed{
\bigl(1-S_{H_{j-1}}\bigr)
+
\bigl(1-S_{H_j}\bigr)
\ge
\delta_B^{\rm sf}.
}
\tag{26}
\]

Indeed, if both endpoint deficits were smaller than `delta_B^(sf)`, then both nonzero endpoints would satisfy

\[
\frac{\Delta_H}{|Y(H)|^2}
=
\frac1{S_H}-1
<c_B^{\rm sf},
\]

contradicting (12); if an endpoint vanishes, its deficit is already `1`. Summing (26) counts each horizon at most twice. Writing

\[
s_k:=\frac{N_B^{\rm sf}(n_k)}{n_k},
\]

we obtain

\[
\frac1{n_k+1}
\sum_{j=0}^{n_k}(1-S_{H_j})
\ge
b_Bs_k-o(1).
\tag{27}
\]

Every transition not counted by the union of

- `q_j>B`,
- `q_j<=B` squarefree,
- nonsquarefree stages with `S_(H_j)>=r_theta`,

is a bounded nonsquarefree stage with

\[
1-S_{H_j}>a_\theta.
\tag{28}
\]

The first and third sets may overlap, so subtracting their cardinalities separately is conservative. Equations (19), (24), and (28) give the simultaneous lower bound

\[
\frac1{n_k+1}
\sum_{j=0}^{n_k}(1-S_{H_j})
\ge
 a_\theta
\bigl(c_{\alpha,L}(B,\theta)-s_k\bigr)-o(1).
\tag{29}
\]

Combining (27)--(29) and minimizing over `0<=s<=1`,

\[
\min_{0\le s\le1}
\max\{b_Bs,\ a_\theta(c_{\alpha,L}-s)\}
=
\frac{a_\theta b_B}{a_\theta+b_B}
 c_{\alpha,L},
\tag{30}
\]

which is exactly (15)--(16).

If the Cesàro mean of `S_(H_j)` tended to `1` while `Lambda_n` failed to tend to infinity, some finite `L` and infinite subsequence would satisfy (10). Choosing `B,theta` with (14) positive, (15) would give a fixed positive deficit on that subsequence, a contradiction. This proves (8)--(9).

## 5. Exact boundary and prior-art audit

This theorem closes the explicit **unbounded-ratio loophole of `FD-123` at the qualitative Cesàro level**. A bounded ratio ceiling is stronger than necessary: what matters is whether the retained scales have finite logarithmic entropy per step. For the physical Mertens source, any hierarchy that Cesàro-tracks the one-horizon equality geometry must therefore become superexponentially sparse before any finer Möbius correlation is invoked.

The conclusion remains weaker than the pointwise statement needed for the Farey/RH target. It does not force a designated horizon to pay a positive relative excess, does not bound `M(H)` independently of the skeleton energy, and does not improve the Franel--Landau critical exponent. It also leaves genuinely superexponential schedules open. In the older GCD-duality geometry, `FD-024` shows that sufficiently isolated horizons can still be saturated by synthetic sources obeying every fixed power envelope above `n^(1/2)`; that is a warning about the surviving sparse regime, not a theorem about the present Fourier skeleton.

There is also a direct internal precedent for the proof architecture. `FD-023` established the same logarithmic-entropy split for the older GCD-duality relaxation. The entropy mechanism itself is therefore not claimed as new. The substantive delta is its transplant to the current minimal Fourier skeleton after `FD-117`--`FD-123`: the present proof uses the Fourier-skeleton coordinate stability and squarefree-dilation gaps of `FD-122`, together with the nonsquarefree long-range memory isolated in `FD-123`.

A targeted external audit covered Franel--Landau/Farey discrepancy, Mertens floor-quotient formulas, and harmonic/Fourier treatments of Farey fractions. The neighboring literature supplies exact Farey--Mertens identities and Fourier formulations but no theorem was located matching this common-source multihorizon saturation-versus-horizon-entropy statement. No novelty claim is inferred from search absence. The proof imports no new external theorem beyond dependencies already internalized by `FD-122`--`FD-123`, so `SOURCES.md` requires no change.

The decisive falsification test is elementary: produce an integer-ratio chain with `liminf Lambda_n<infinity` and a polynomial-growth common source whose Cesàro mean of `S_(H_j)` tends to `1`. Such an example would have to violate at least one of the exact entropy count (18), endpoint-amplification count (23), bounded squarefree pair gap (26), or the final density partition (29).