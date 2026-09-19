# AF-428 — Second-order exceptional amplitudes are residual but null

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIOPHANTINE-GATE` · `BAIRE-CATEGORY` · `METRIC-DIOPHANTINE` · `SIGNED-RESUMMATION` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-425--AF-427 with fixed packet index `m>=1`. Write

\[
A=\log\!\left(\frac{m^2}{a}\right),
\qquad
a(A)=m^2e^{-A},
\]

and for odd `n` and integer derivative offset `d` let

\[
H_{n,m}(d;A)
=
\log n-nA+\log K_m+dL_{n,m}
+\frac{B_1(d/n;a(A))}{n}
+\frac{B_2(d/n;a(A))}{n^2},
\]

with the quantities `K_m`, `L_{n,m}`, `B_1`, and `B_2` from AF-425. Let `\mathcal E_m` be AF-427's exceptional displacement set: the set of `A\in\mathbb R` for which there exist odd `n_j\to\infty` and integers `d_j` satisfying

\[
\frac{d_j\log n_j}{n_j}\longrightarrow A,
\qquad
H_{n_j,m}(d_j;A)=o(n_j^{-2}).
\tag{1}
\]

Then

\[
\boxed{\mathcal E_m\text{ is a dense }G_\delta\text{ subset of }\mathbb R.}
\tag{2}
\]

In particular `\mathcal E_m` is residual (comeagre). Combining `(2)` with AF-427 gives the apparently opposite pair

\[
\boxed{
\mathcal E_m\text{ is residual, }
\operatorname{Leb}(\mathcal E_m)=0,
\qquad
\dim_{\mathrm H}(\mathcal E_m)\le\frac23.
}
\tag{3}
\]

Thus the complement is meagre but has full Lebesgue measure. Under the homeomorphism `A\mapsto a=m^2e^{-A}`, the corresponding exceptional positive amplitudes are likewise residual in `(0,\infty)`, Lebesgue-null, and of Hausdorff dimension at most `2/3`.

The pointwise consequence is decisive for the current source-realizability gate: AF-427's exceptional amplitudes are not merely potentially nonempty. They are topologically generic. Therefore no obstruction based only on local neighborhoods, openness, or stability under small amplitude perturbations can exclude the displaced square-transition branch. Excluding or admitting a distinguished source amplitude now requires information about that exact amplitude or another genuinely non-open arithmetic property.

## 1. Exact `G_delta` characterization

For integers `k,N>=1`, define

\[
\begin{aligned}
U_{k,N}
=
\bigcup_{\substack{n\ge N\\ n\text{ odd}}}
\ \bigcup_{d\in\mathbb Z}
\Bigl\{A\in\mathbb R:
&\ |H_{n,m}(d;A)|<\frac1{k n^2},\\
&\ \left|\frac{d\log n}{n}-A\right|<\frac1k
\Bigr\}.
\end{aligned}
\tag{4}
\]

Each `U_{k,N}` is open because `H_{n,m}(d;A)` is continuous in `A`. Moreover

\[
\boxed{
\mathcal E_m
=
\bigcap_{k=1}^\infty\bigcap_{N=1}^\infty U_{k,N}.
}
\tag{5}
\]

Indeed, every sequence satisfying `(1)` eventually satisfies both inequalities in `(4)` for each fixed `k` and arbitrarily large `N`. Conversely, if `A` belongs to the right-hand side of `(5)`, choose successively `k=j` and `N` larger than the preceding chosen odd index. This produces odd `n_j\to\infty` and integers `d_j` with

\[
\left|\frac{d_j\log n_j}{n_j}-A\right|<\frac1j,
\qquad
n_j^2|H_{n_j,m}(d_j;A)|<\frac1j,
\]

which is exactly `(1)`.

Thus it remains only to prove that every `U_{k,N}` is dense.

## 2. Exact roots become dense at large odd scales

Fix a nonempty open interval `I`, choose `A_0\in I`, and fix `k,N`. For a sufficiently large odd `n`, choose an integer

\[
d_n
=
\operatorname*{round}\!\left(
\frac{nA_0-\log n-\log K_m}{L_{n,m}}
\right),
\tag{6}
\]

where either nearest integer is allowed at a tie. Since `L_{n,m}\sim\log n`, one has

\[
d_n=O_{A_0,m}\!\left(\frac{n}{\log n}\right),
\qquad
\alpha_n:=\frac{d_n}{n}=O\!\left(\frac1{\log n}\right).
\tag{7}
\]

The leading affine detuning at `A_0` is

\[
\Omega_{n,m}(d_n;A_0)
=
\log n-nA_0+\log K_m+d_nL_{n,m}.
\]

By `(6)`,

\[
|\Omega_{n,m}(d_n;A_0)|\le\frac12L_{n,m}=O(\log n).
\tag{8}
\]

On any fixed compact neighborhood of `A_0`, `(7)` keeps `a(A)` and the explicit AF-425 coefficients uniformly bounded, so

\[
H_{n,m}(d_n;A_0)=O(\log n).
\tag{9}
\]

AF-427 computed the exact amplitude derivative

\[
\partial_A H_{n,m}(d;A)
=
-n
-\frac{a e^{2+\alpha}(2+\alpha)}{n}
+\frac{a e^{2+\alpha}P_m(\alpha)}{n^2}.
\tag{10}
\]

For `(7)` and `A` in that compact neighborhood,

\[
\partial_A H_{n,m}(d_n;A)=-n+O(n^{-1}),
\tag{11}
\]

uniformly. Hence for large `n` the function is strictly decreasing there with derivative at most `-n/2`. Combining `(9)` and `(11)` with the intermediate value theorem gives a unique nearby root `A_n` satisfying

\[
H_{n,m}(d_n;A_n)=0,
\qquad
|A_n-A_0|=O\!\left(\frac{\log n}{n}\right).
\tag{12}
\]

In particular `A_n\in I` for all sufficiently large odd `n`.

The same root automatically becomes source-compatible. From `H_{n,m}(d_n;A_n)=0`,

\[
nA_n
=
\log n+\log K_m+d_nL_{n,m}
+\frac{B_1(d_n/n;a(A_n))}{n}
+\frac{B_2(d_n/n;a(A_n))}{n^2}.
\]

Therefore

\[
\frac{d_n\log n}{n}-A_n
=
\frac{d_n(\log n-L_{n,m})-\log n-\log K_m}{n}
+O(n^{-2}).
\tag{13}
\]

Since

\[
\log n-L_{n,m}=\log m-\frac mn
\]

and `d_n=O(n/\log n)`, the right-hand side of `(13)` is

\[
O\!\left(\frac1{\log n}\right)
+O\!\left(\frac{\log n}{n}\right)
\longrightarrow0.
\tag{14}
\]

Thus, for sufficiently large odd `n>=N`, the root `A_n\in I` satisfies both inequalities in `(4)`: the cancellation inequality holds exactly because `H=0`, while `(14)` is eventually smaller than `1/k`. Hence

\[
I\cap U_{k,N}\ne\varnothing.
\]

Every `U_{k,N}` is dense.

## 3. Category and measure give opposite notions of genericity

Equation `(5)` writes `\mathcal E_m` as a countable intersection of open dense subsets of `\mathbb R`. The Baire category theorem therefore proves `(2)`.

AF-427 independently proves

\[
\operatorname{Leb}(\mathcal E_m)=0,
\qquad
\dim_{\mathrm H}(\mathcal E_m)\le\frac23.
\]

There is no contradiction: Baire category and Lebesgue measure are different notions of largeness. A set can be topologically generic while occupying no Lebesgue measure and having small Hausdorff dimension. The classical Liouville-number set is a standard model of this phenomenon.

Finally, `A\mapsto a=m^2e^{-A}` is a homeomorphism from `\mathbb R` to `(0,\infty)`, so residuality transfers exactly. On every compact `A`-interval it is bi-Lipschitz; countable compact exhaustion therefore transfers Lebesgue nullity and the Hausdorff-dimension upper bound as well.

## Prior-art and novelty audit

Baire-category largeness coexisting with Lebesgue measure zero is classical. John C. Oxtoby, *Measure and Category: A Survey of the Analogies between Topological and Measure Spaces*, 2nd ed., Graduate Texts in Mathematics 2, Springer (1980), DOI `10.1007/978-1-4684-9339-9`, develops the measure/category duality and treats Liouville numbers as an early model example: https://doi.org/10.1007/978-1-4684-9339-9 .

The metric side used here is already classicalized in AF-427 through convergence Borel--Cantelli and Hausdorff limsup-covering arguments. Modern shrinking-target and Diophantine-approximation literature studies much broader limsup systems; the present proof does not claim a new Baire-category principle.

A targeted search across residual Diophantine sets, shrinking targets, and measure/category duality did not locate this specific Euler-log derivative-Hankel source grid. **No novelty claim is made** for Baire's theorem, residual limsup constructions, or the null-but-residual phenomenon. The durable delta is the direct specialization showing that AF-427's exact second-order exceptional set is simultaneously metrically thin and topologically generic.

## Boundaries and falsification checks

- Residuality does not show that any particular distinguished amplitude belongs to `\mathcal E_m`. A fixed arithmetic constant may lie in the meagre full-measure complement.
- Density does not contradict AF-426. The exact amplitude `a=m^2`, equivalently `A=0`, is pointwise excluded even though exceptional amplitudes occur arbitrarily close to it.
- Equation `(2)` concerns AF-425's displayed second-order target. It does not control the undisplayed determinant remainder or imply actual complete-determinant cancellation.
- The Hausdorff-dimension bound `2/3` comes from AF-427 and is only an upper bound. Residuality supplies no positive Hausdorff-dimension lower bound.
- The argument fixes `m`. It does not couple different square-transition packet indices or control a growing `m`.
- For `m>=2`, a nonexceptional amplitude blocks this route to beyond-all-orders adjacent-packet cancellation because polynomial mismatch dominates lower exponential saddles. For `m=1`, the same source-set classification holds but the `\Lambda_m>1` divergence conclusion does not.
- The genuinely supercritical regime `s_n/n->sigma>2`, omitted-`1` sector, one-/zero-singular-block contributions, and lower/tall-column saddles remain separate.
- No conclusion upgrades second-order packet cancellation to rational-prime discrimination, zeta-zero recovery, or RH.

## Consequence for the research line

AF-427 changed the finite-window question from free continuous tuning to a metrically exceptional source-lattice problem. AF-428 sharpens the boundary in the opposite direction: that exceptional set is nevertheless residual and dense.

The remaining pointwise gate is therefore genuinely arithmetic. Another almost-everywhere theorem, generic spacing argument, or perturbative neighborhood obstruction cannot decide a source-forced amplitude. The next useful finite-window result must prove membership or nonmembership for a concrete distinguished amplitude using its exact structure. Beyond-all-orders packet analysis remains justified only after such a specific amplitude is shown to lie in the residual exceptional set.