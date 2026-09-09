# NB-011 — prime normal-equation ensemble amplifies early residual energy

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIME-NORMAL-EQUATION-ENSEMBLE + RESIDUAL-SPECIFIC-COERCIVITY + POLYLOGARITHMIC-DEPTH-AMPLIFICATION`. `NB-010` shows that the single `g_2` normal equation already forces truncated semigroup energy of order `d_N^4/log(1/d_N)` at the first inverse-distance scale. Its own sharpness control proves that the logarithmic denominator cannot be removed while using only that one parity functional. The remaining finite-section equations do materially strengthen the conclusion: combining the prime-indexed normal equations produces nearly orthogonal divisibility contrasts in the harmonic mismatch norm. Their target loads add like a weighted prime square-sum, while their pairwise harmonic correlations are only boundary-size errors.

For the canonical best residual

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},\qquad
r_N=e-P_{V_N}e,\qquad
d_N=\|r_N\|,\qquad a_N=d_N^2,
\]

retain

\[
c_j(r_N)=j\int_0^{1/j}r_N(x)\,dx,\qquad
\delta_j=c_j(r_N)-a_N,
\]

and

\[
\mathcal E_K(r_N)=\sum_{m=2}^{K}\|(A_m^*-m^{-1/2}I)r_N\|^2.
\]

For `2<=L<=N`, let `P(L)` denote the primes at most `L` and define

\[
S_L:=\sum_{p\le L}\frac{(\log p)^2}{p-1},
\qquad
P_L:=\sum_{p\le L}\frac{p\log p}{p-1}.
\tag{1}
\]

Then for every integer `K` with `K-1>=L^2`,

\[
\boxed{
\mathcal E_K(r_N)
\ge
\frac{
\left[
 a_NS_L-a_NP_L/K-d_NP_L/\sqrt K
\right]_+^2
}{
H_{K-1}S_L+9P_L^2/(K-1)
}.
}
\tag{2}
\]

This is an unconditional finite residual inequality. It uses all prime normal equations `\langle r_N,g_p\rangle=0` for `p<=L`, but no Gram inversion, no common period, no Mellin-bandwidth hypothesis, and no assumption about RH.

A useful asymptotic consequence is that there are absolute constants `C_1,C_2>0` such that, for all sufficiently large `N`, one can choose

\[
\boxed{K_N\le C_1(\log N)^2}
\tag{3}
\]

with

\[
\boxed{
\mathcal E_{K_N}(r_N)
\ge
C_2\frac{\log\log N}{(\log N)^2}.
}
\tag{4}
\]

Thus the parity-only denominator in `NB-010` is not a property of the full finite-section source geometry. By moving from one normal equation to a prime ensemble and allowing a still-polylogarithmic but deeper cutoff, the guaranteed energy improves from

\[
\gg \frac1{(\log N)^2\log\log N}
\]

at the first logarithmic window to

\[
\gg \frac{\log\log N}{(\log N)^2}
\]

by depth `O((log N)^2)`. This is a gain of two logarithmic factors in the certified source energy, not an improvement of the Nyman distance itself.

## 1. Every generator normal equation is a divisibility contrast on the mismatch sequence

Use Bagchi's harmonic intervals

\[
I_n=\left(\frac1{n+1},\frac1n\right],
\qquad
g_l|_{I_n}=\left\{\frac nl\right\},
\]

with shell values `r_{N,n}`. Since `g_l\in V_N` for every `2<=l<=N`,

\[
\langle r_N,g_l\rangle=0.
\tag{5}
\]

The target mass of the generator is the standard exact identity

\[
\sum_{n\ge1}\frac{\{n/l\}}{n(n+1)}
=\langle e,g_l\rangle
=\frac{\log l}{l}.
\tag{6}
\]

As in `NB-009`--`NB-010`, tail averages reconstruct shells without loss:

\[
r_{N,n}-a_N=(n+1)\delta_n-n\delta_{n+1},
\]

so

\[
\frac{r_{N,n}-a_N}{n(n+1)}
=\frac{\delta_n}{n}-\frac{\delta_{n+1}}{n+1}.
\tag{7}
\]

For a prime `p`, multiplication of the discrete difference of the fractional-part weight gives

\[
p\left(
\left\{\frac jp\right\}
-
\left\{\frac{j-1}{p}\right\}
\right)
=1-p\mathbf1_{p\mid j}.
\tag{8}
\]

Thus every prime normal equation probes the same mismatch sequence through a centered divisibility pattern rather than through an unrelated Gram coordinate.

## 2. A target-matched prime combination has square load `S_L`

Put

\[
\alpha_p:=\frac{\log p}{p-1}
\qquad(p\le L),
\tag{9}
\]

and combine the equations (5) after multiplying the `p`-th equation by `\alpha_pp`. Define

\[
F_n:=\sum_{p\le L}\alpha_pp\left\{\frac np\right\},
\qquad
Q_j:=\sum_{p\le L}\alpha_p
\left(1-p\mathbf1_{p\mid j}\right).
\tag{10}
\]

Let `M=K-1`. Splitting the combined normal equation at shell `M` gives

\[
0
=a_N\sum_{n\le M}\frac{F_n}{n(n+1)}
+\sum_{n\le M}
\frac{F_n(r_{N,n}-a_N)}{n(n+1)}
+\sum_{n>M}\frac{F_nr_{N,n}}{n(n+1)}.
\tag{11}
\]

Equation (6) and `0<=p\{n/p\}<=p` show

\[
\sum_{n\le M}\frac{F_n}{n(n+1)}
\ge
S_L-\frac{P_L}{K}.
\tag{12}
\]

The remote residual tail is controlled in the actual Hilbert norm. Since `|F_n|<=P_L`,

\[
\left|
\sum_{n>M}\frac{F_nr_{N,n}}{n(n+1)}
\right|
\le
\frac{d_NP_L}{\sqrt K}.
\tag{13}
\]

Hence the early mismatch contribution in (11) has magnitude at least

\[
\left[
 a_NS_L-a_NP_L/K-d_NP_L/\sqrt K
\right]_+.
\tag{14}
\]

Using (7) and finite summation by parts, this early contribution is exactly

\[
\sum_{j=2}^{K-1}Q_j\frac{\delta_j}{j}
-F_M\frac{\delta_K}{K}.
\tag{15}
\]

The endpoint term is retained explicitly; no assumption that `K` is divisible by the selected primes is being made.

## 3. Prime divisibility contrasts are harmonically almost orthogonal

Let

\[
q_p(j):=1-p\mathbf1_{p\mid j}.
\]

For one prime,

\[
\sum_{j=1}^{M}\frac{q_p(j)^2}{j}
=H_M+(p-2)H_{\lfloor M/p\rfloor}
\le(p-1)H_M.
\tag{16}
\]

For distinct primes `p,q`, direct expansion gives

\[
\sum_{j=1}^{M}\frac{q_p(j)q_q(j)}j
=H_M-H_{\lfloor M/p\rfloor}
-H_{\lfloor M/q\rfloor}
+H_{\lfloor M/(pq)\rfloor}.
\tag{17}
\]

When `M>=pq`, the logarithmic main terms cancel. The elementary uniform estimate

\[
\left|H_{\lfloor x\rfloor}-\log x-\gamma\right|
\le\frac2x
\qquad(x\ge1)
\tag{18}
\]

therefore yields

\[
\left|
\sum_{j=1}^{M}\frac{q_p(j)q_q(j)}j
\right|
\le\frac{8pq}{M}.
\tag{19}
\]

This is the source of the gain. Distinct prime equations have zero logarithmic-density covariance; only the finite cutoff leaves a boundary correlation.

Since `M>=L^2`, equations (16)--(19) and (9) give

\[
\sum_{j=1}^{M}\frac{|Q_j|^2}{j}
\le
H_MS_L+\frac{8P_L^2}{M}.
\tag{20}
\]

Also `|F_M|<=P_L`, so the endpoint coefficient in (15) contributes at most `P_L^2/K` to the dual harmonic norm. Consequently

\[
\boxed{
\sum_{j=2}^{K-1}\frac{|Q_j|^2}{j}
+\frac{|F_M|^2}{K}
\le
H_{K-1}S_L+rac{9P_L^2}{K-1}.
}
\tag{21}
\]

Cauchy--Schwarz applied to (15), followed by the source coordinate bound from `NB-007`,

\[
\mathcal E_K(r_N)
\ge
\sum_{j=2}^{K}\frac{|\delta_j|^2}{j},
\tag{22}
\]

proves (2).

## 4. Choosing primes up to inverse residual size changes the logarithmic law

The finite estimate already isolates the relevant tradeoff. To read its scale, use the prime number theorem and partial summation:

\[
S_L
=\left(\frac12+o(1)\right)(\log L)^2,
\qquad
P_L=(1+o(1))L.
\tag{23}
\]

Consider first a sequence with `d_N->0` and choose

\[
L_N=\lfloor d_N^{-1}\rfloor.
\tag{24}
\]

For sufficiently large `N`, `L_N<=N`; this also follows from the Burnol floor used below. Choose `K_N` above

\[
L_N^2+1,
\qquad
\frac{4P_{L_N}}{S_{L_N}},
\qquad
\frac{16P_{L_N}^2}{d_N^2S_{L_N}^2}.
\tag{25}
\]

Then both error terms in the numerator of (2) are at most one quarter of `a_NS_{L_N}`. Equations (23)--(25) imply

\[
K_N
\ll
\frac{d_N^{-4}}
{\log^4(1/d_N)},
\qquad
\log K_N\asymp\log(1/d_N).
\tag{26}
\]

The finite-correlation term `P_L^2/K` in (2) is then lower order than `H_KS_L`, so

\[
\boxed{
\mathcal E_{K_N}(r_N)
\gg d_N^4\log(1/d_N).
}
\tag{27}
\]

If `d_N` stays bounded below, a fixed finite prime set and a fixed sufficiently large cutoff already give a positive lower bound, so (27) is only needed in the small-distance regime.

The tradeoff against `NB-010` is explicit. The one-parity theorem acts already at `K\asymp d_N^{-2}` but pays `1/log(1/d_N)`. The prime ensemble uses the deeper yet still polynomial scale `K\ll d_N^{-4}` and gains `log(1/d_N)` instead. The source equations do not eliminate the cost for free; they exchange additional semigroup depth for two logarithmic factors of certified energy.

## 5. Burnol converts the prime ensemble into a quadratic-logarithmic section

The existing Burnol anchor gives a constant `c_B>0` such that for all sufficiently large `N`,

\[
d_N^2\ge\frac{c_B}{\log N}.
\tag{28}
\]

It follows that `d_N^{-1}=O(\sqrt{\log N})`, so the prime equations used in (24) are all available in `V_N`, and (26) gives the safe uniform depth bound

\[
K_N=O((\log N)^2).
\tag{29}
\]

There is no monotonicity ambiguity when inserting the Burnol floor into (27). Already at `N=2`, the exact parity model gives

\[
\|g_2\|^2=\frac{\log2}{4},
\qquad
\langle e,g_2\rangle=\frac{\log2}{2},
\]

so

\[
d_N^2\le d_2^2=1-\log2,
\qquad
d_N<e^{-1/4}.
\tag{30}
\]

On this interval the function

\[
x\longmapsto x^4\log(1/x)
\]

is increasing. Therefore (28) and (27), with the fixed-distance case absorbed into the constants, yield

\[
\mathcal E_{K_N}(r_N)
\gg
\frac{\log\log N}{(\log N)^2},
\tag{31}
\]

which proves (3)--(4).

Equation (31) again imports the known zero-sensitive lower scale only to express the source-defect theorem in section size. It does not improve Burnol's approximation bound.

## 6. Prior-art boundary and falsification controls

The load-bearing Nyman inputs remain the existing line anchors. Bagchi supplies the harmonic-interval generator values, the discrete semigroup model, and the finite projection setting; Burnol supplies only the final zero-sensitive distance floor. The prime number theorem enters (23) only through standard weighted prime partial summation.

A targeted literature check covered Bagchi's semigroup treatment, Báez-Duarte's discrete criteria and arithmetic formulations, Burnol's quantitative distance bounds, Ehm's 2024 Nyman Gram-matrix decompositions, recent Mellin-smoothed multiscale Gram work, and searches for prime-indexed Nyman residual normal equations. The located literature studies the criterion, arithmetic approximants, Gram structure, or approximation rates; it did not supply the prime-normal-equation ensemble (2), the harmonic divisibility covariance (17)--(21) in this residual role, or the resulting `d_N^4 log(1/d_N)` source-energy law. Search absence is not a novelty proof, and no new specialized theorem is imported, so `SOURCES.md` is unchanged.

Several boundaries are load-bearing. First, the theorem is **residual-specific**: arbitrary target-orthogonal or Mellin-alias vectors do not satisfy all equations (5). Second, the prime ensemble strengthens a lower bound on the semigroup defect; no residual-specific upper bound on the same quantity is proved. Third, (31) uses Burnol and is therefore not an independent approximation-rate improvement. Fourth, pairwise prime contrast covariance is only asymptotically orthogonal; the finite `9P_L^2/(K-1)` term is retained in (2). Fifth, taking `L` larger than the inverse-distance scale without paying the corresponding remote-tail cost is invalid.

## 7. Research consequence

`NB-010` correctly identified its `1/log` denominator as sharp for the single parity functional. `NB-011` shows that this is a method boundary rather than a full-source boundary. The remaining normal equations contain a structured family of centered divisibility contrasts whose target loads add coherently while their harmonic cross-correlations cancel at leading order.

The current finite-section frontier is therefore more specific. By depth `O((log N)^2)`, the actual best residual must already carry semigroup defect energy at least of order `log log N/(log N)^2`. A useful next step must either derive a source-specific **upper** bound on this same quadratic-logarithmic defect in terms of `d_N`, or use still more of the exact normal equations to convert the forced divisibility energy into a normed dual certificate. Further lower-bound amplification alone will not improve the approximation rate unless it is paired with such a return inequality.