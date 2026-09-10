# ANF-159 — double-resonant X-squared heights create a cubic coherence window for endpoint twist

**Status:** `EXACT-DERIVED + TWIST-RESONANCE + ENDPOINT-GATE-REFINEMENT`. `ANF-158` reduces the hard-crop completion to source-specific endpoint partial sums of the distinguished logarithmic carrier `n^{-iU}` multiplied by the residual `r_X(n)`, at heights `U asymp X^2`. A tempting next step is to argue that the carrier itself must oscillate strongly because its first derivative is of order `X`. That is not uniformly valid. There is an explicit cofinal family of heights `U=4 pi q M^2`, with fixed integer `q>=1`, for which both the linear and quadratic Taylor phases of `-U log(M+j)` are exact integer multiples of `2 pi`. The cubic remainder is then the first visible phase, producing coherent sums of length `M^{1/3}`. Thus no source argument uniform over all `U asymp X^2` can obtain square-root cancellation on every short endpoint block from smooth carrier oscillation alone. The obstruction is nevertheless below the bow endpoint threat scale by itself: its normalized completion contribution is only of order `1/K`. The useful consequence is therefore methodological, not a bow counterexample: the remaining endpoint theorem must use arithmetic structure of `r_X`, the actual distinguished height, or a norm weaker than pointwise square-root cancellation on every dyadic block.

## 1. Exact double resonance cancels the first two Taylor phases

Let `M` be a positive integer tending to infinity, fix an integer `q>=1`, and set

\[
U_M:=4\pi q M^2.
\tag{1}
\]

Then `U_M asymp M^2`, exactly in the height scale singled out by the bow formulation. Consider the bare multiplicative carrier on a rightward block starting at `M`:

\[
a_j:=(M+j)^{-iU_M},\qquad j\ge0.
\tag{2}
\]

For `0<=x<=1`, the alternating Taylor expansion gives

\[
\log(1+x)=x-\frac{x^2}{2}+R_3(x),
\qquad
0\le R_3(x)\le\frac{x^3}{3}.
\tag{3}
\]

Hence, for `0<=j<=M`,

\[
\frac{a_j}{a_0}
=\exp\!\left(-iU_M\log\left(1+\frac jM\right)\right)
\tag{4}
\]

becomes

\[
\frac{a_j}{a_0}
=\exp\!\left(
-i4\pi qMj
+i2\pi qj^2
-i4\pi qM^2R_3(j/M)
\right).
\tag{5}
\]

The first phase in (5) is `-2 pi` times the integer `2qMj`, and the second is `2 pi` times the integer `qj^2`. They therefore disappear exactly on the integer lattice. Thus

\[
\boxed{
\frac{a_j}{a_0}
=\exp\!\left(-i\rho_{M,j}\right),
\qquad
0\le\rho_{M,j}
:=4\pi qM^2R_3(j/M)
\le\frac{4\pi q}{3}\frac{j^3}{M}.
}
\tag{6}
\]

This is stronger than merely saying that the first derivative is close to an integer frequency. The discrete linear and quadratic jets are simultaneously invisible modulo `2 pi`; the cubic Taylor term is the first one capable of producing phase separation.

## 2. The resulting coherence window has cubic scale

Choose an integer `L` with

\[
1\le L\le M,
\qquad
\frac{L^3}{M}\le\frac{1}{4q}.
\tag{7}
\]

For every `0<=j<L`, equation (6) gives `0<=rho_{M,j}<=pi/3`. After rotating the sum by the unimodular constant `a_0^{-1}`, every summand has real part at least `1/2`. Therefore

\[
\boxed{
\left|
\sum_{j=0}^{L-1}(M+j)^{-iU_M}
\right|
\ge\frac L2.
}
\tag{8}
\]

In particular, with any fixed

\[
0<c<(4q)^{-1/3}
\tag{9}
\]

and `L=floor(cM^{1/3})`, the sum has size `Omega_q(M^{1/3})`. More sharply, if `L=o(M^{1/3})`, then the right side of (6) has `rho_{M,j}=o(1)` uniformly over the block, so

\[
\sum_{j=0}^{L-1}(M+j)^{-iU_M}
=a_0L(1+o(1)).
\tag{10}
\]

Thus `M^{1/3}` is the natural coherence scale of this exact double-resonance family. This statement is intentionally family-specific: it does not assert that every `U asymp M^2` has this coherence length, nor that other Diophantine resonances cannot produce different local behavior.

A useful equivalent derivative picture is obtained from the phase `f(x)=-U_M log x`. At `x=M`,

\[
f'(M)=-4\pi qM,
\qquad
\frac12f''(M)=2\pi q,
\qquad
\frac16f'''(M)=-\frac{4\pi q}{3M}.
\tag{11}
\]

The first two coefficients generate integer cycles on integer `j`; the third accumulates order-one phase precisely when `j^3/M` reaches order one. Large `|f'(M)|` by itself therefore says essentially nothing about cancellation here.

## 3. Uniform square-root cancellation from the carrier alone is false

Suppose one tried to close the endpoint gate of `ANF-158` with a generic estimate of the schematic form

\[
\left|
\sum_{j=0}^{L-1}(M+j)^{-iU}
\right|
\ll L^{1/2}(\log M)^A
\tag{12}
\]

for every `U asymp M^2` and every relevant short length `L`, with fixed `A`. Take the resonant height (1) and `L=floor(cM^{1/3})` as above. Equation (8) gives a lower bound of order `M^{1/3}`, whereas (12) would give at most

\[
M^{1/6+o(1)}.
\tag{13}
\]

This is impossible. Consequently, neither a first-derivative argument nor any carrier-only theorem implying square-root cancellation uniformly in the whole `U asymp X^2` regime can be the missing input behind the endpoint estimate in `ANF-158`.

The quantifier is important. The bow program ultimately needs the actual distinguished twist, not an arbitrary height in a comparability class. Equation (8) does **not** show that this distinguished height is resonant. It shows that a proof which throws away its arithmetic location and retains only `U asymp X^2` has lost information that can be decisive on short blocks.

The same caveat applies to the coefficient sequence. The actual endpoint source is

\[
b_n=r_X(X+n)(X+n)^{-iU},
\tag{14}
\]

not the bare carrier. The residual may destroy or reinforce the resonance. Hence (8) is a matched carrier obstruction to a proposed analytic mechanism, not a model of `vartheta-Q_R` and not evidence that the bow variance itself is large.

## 4. The resonance is visible in endpoint completion but is too small to obstruct the bow by itself

The distinction can be quantified inside the exact endpoint functional from `ANF-158`. Let

\[
L_0:=\left\lfloor cM^{1/3}\right\rfloor
\tag{15}
\]

with `c` satisfying (9), assume `K>L_0`, and use the pure carrier as a synthetic left-edge control. Its first `r` terms satisfy (8) for every `1<=r<=L_0`; therefore the left endpoint completion obeys

\[
E_L
:=\sum_{r=1}^{K-1}
\left|\sum_{j=0}^{r-1}(M+j)^{-iU_M}\right|^2
\ge
\frac14\sum_{r=1}^{L_0}r^2
=\left(\frac{c^3}{12}+o(1)\right)M.
\tag{16}
\]

For a full synthetic vector of length `N asymp M` with unit-modulus coefficients, the moving diagonal normalization is

\[
D_N=K\sum_{n=1}^{N}|b_n|^2\asymp KM.
\tag{17}
\]

Thus this coherent block contributes at least order

\[
\frac{E_L}{D_N}\gg_q\frac1K.
\tag{18}
\]

Equation (18) is deliberately **not** a lower bound of constant size. When `K->infinity` it vanishes, so the explicit resonance does not by itself defeat the desired `o(1)` normalized endpoint completion. It instead tells us that demanding square-root cancellation on every subblock is substantially stronger than what the bow target intrinsically requires.

In the bow scaling

\[
K=X^{1-2\varepsilon+o(1)},
\tag{19}
\]

the `X^{1/3}` resonant window is actually present among endpoint dyadic scales whenever `K>>X^{1/3}`, in particular for fixed `0<epsilon<1/3`. The difficult regime inherited by the active bow discussion has `epsilon<1/4`, so this family lies comfortably inside the available endpoint window. Nevertheless, `ANF-158` shows that target-scale compensation requires cumulative size about `sqrt(X log X)`, much larger than the `X^{1/3}` bare-carrier block furnished here. The finding therefore narrows proof strategy rather than supplying a target-scale obstruction.

## 5. Prior-art boundary and frontier consequence

The literature audit places the local mechanism inside the classical theory of short exponential sums and van der Corput derivative tests. In particular, work on the `k`-th derivative test explicitly treats short phases of the form `M^{k-1} log(M+m)+P(m)` with a polynomial `P` of degree at most `k-1`, and computational zeta methods likewise exploit Taylor reduction to quadratic or cubic exponential sums. That is the correct surrounding technology. No external theorem is needed here, however: equations (3)--(18) are an elementary exact lattice-resonance calculation. The finding therefore introduces no load-bearing source and does not require a `SOURCES.md` change.

The source-side gate after `ANF-158` can now be stated more carefully. A proof of the maximal endpoint condition

\[
\max_{r<K}
\left|
\sum_{n=1}^{r}r_X(X+n)(X+n)^{-iU}
\right|
=o(\sqrt{X\log X})
\tag{20}
\]

cannot be justified uniformly from the large logarithmic carrier derivative or from a generic square-root short-sum heuristic. A viable proof must exploit at least one piece of information discarded by that heuristic: the precise distinguished value of `U`, arithmetic cancellation in `r_X`, joint cancellation between `r_X` and the carrier, or an aggregate cumulative-energy estimate that reaches the bow norm without requiring square-root cancellation on every block.

A concrete next test is therefore Diophantine rather than merely oscillatory: evaluate how close the actual distinguished bow height makes the first two local phase coefficients to integer cycles across the two endpoint regions, and combine that with the arithmetic structure of `r_X`. If those coefficients are quantitatively nonresonant at all endpoint scales capable of producing the `sqrt(X log X)` threat isolated by `ANF-158`, derivative/exponent-pair machinery may become effective. If near-resonances persist, the missing theorem must obtain its saving from the residual source rather than from the carrier.