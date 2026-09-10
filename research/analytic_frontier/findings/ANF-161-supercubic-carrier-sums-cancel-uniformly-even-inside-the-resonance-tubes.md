# ANF-161 — supercubic carrier sums cancel uniformly even inside the resonance tubes

**Status:** `EXACT-DERIVED + SHARP-VECTOR-SUM-CUBIC-CEILING + QUADRATIC-REPHASING-INVARIANT + ENDPOINT-GATE-REFINEMENT`. `ANF-159` and `ANF-160` identify the sharp `M^{1/3}` scale on which the bare logarithmic carrier can remain concentrated in one fixed arc, and classify the corresponding `U asymp M^2` resonance tubes. They deliberately leave open a stronger loophole: a large exponential sum need not have all phasors in one arc, so perhaps a resonant carrier could retain substantial **vector-sum** coherence on the much longer endpoint support forced by `ANF-158`. That loophole can be closed at the carrier level. Uniformly for every fixed height window `AM^2<=U<=BM^2`, for every real polynomial `P_2` of degree at most two, and for every consecutive block `0<=j<L<=M`, one has for `L>=2M^{1/3}`

\[
\boxed{
\left|
\sum_{j=0}^{L-1}
\exp\!\left(i[-U\log(M+j)+P_2(j)]\right)
\right|
\ll_{A,B}
LM^{-1/6}+L^{1/2}M^{1/6}.
}
\tag{1}
\]

Hence every supercubic block `L/M^{1/3}->infinity` has `o(L)` carrier sum, **including heights inside the sharp resonance tubes of `ANF-160` and even after arbitrary quadratic rephasing**. The scale is sharp: `ANF-159` supplies resonant blocks of length `Theta(M^{1/3})` with sum `Theta(L)`. At the minimum physical support `L_0 asymp sqrt(M/log M)` required by an endpoint threat in `ANF-158`, (1) gives only `O(M^{5/12}(log M)^{-1/4})=o(L_0)`. Thus resonance-tube membership is not the gating issue for a carrier-only explanation of a target-scale endpoint spike. The remaining obstruction is genuinely coefficient-side: the signed arithmetic residual `r_X`, or an aggregate endpoint-energy statistic, must provide any coherence that survives on the required supercubic support.

## 1. Third derivative survives every quadratic rephasing

Fix constants

\[
0<A<B<\infty.
\tag{2}
\]

Let `M` be large, let

\[
AM^2\le U\le BM^2,
\tag{3}
\]

and let `P_2` be any real polynomial of degree at most two. Put

\[
f(x)
:=
\frac{-U\log(M+x)+P_2(x)}{2\pi},
\qquad
0\le x\le M,
\tag{4}
\]

so that the exponential sum in (1) is

\[
S_L:=\sum_{j=0}^{L-1}e(f(j)),
\qquad e(t):=e^{2\pi i t}.
\tag{5}
\]

The point of allowing `P_2` is that the strongest local resonance mechanisms in `ANF-159`--`ANF-160` precisely cancel, modulo integer phases, the linear and quadratic jets of the logarithm. Any argument that depends on those two jets can therefore disappear in the resonance tubes. The third derivative cannot:

\[
f'''(x)
=
-\frac{U}{\pi(M+x)^3}.
\tag{6}
\]

For `0<=x<=M`, equations (2)--(3) give the uniform one-sign bounds

\[
\boxed{
\frac{A}{8\pi M}
\le
|f'''(x)|
\le
\frac{B}{\pi M}.
}
\tag{7}
\]

Thus the carrier has unavoidable cubic curvature of order `1/M` throughout every block of length at most `M`, no matter how accurately its lower two discrete jets resonate. This is the mechanism that upgrades the fixed-arc statement of `ANF-160` to a vector-sum estimate.

## 2. One differencing step converts cubic curvature into a second-derivative bound

We use only the elementary second-derivative estimate in the following form. If `g` is real and `C^2` on an interval containing `T` consecutive integers, `g''` has constant sign, and

\[
\lambda\le |g''(x)|\le C\lambda,
\tag{8}
\]

then

\[
\boxed{
\left|\sum e(g(n))\right|
\ll_C
T\lambda^{1/2}+\lambda^{-1/2}.
}
\tag{9}
\]

For completeness, (9) can be obtained without importing a black-box theorem. Since `g'` is monotone, split the interval according to the distance of `g'(x)` from the nearest integer. Around each integer crossing, the set where that distance is at most `eta` has length `O_C(eta/lambda)`; summing trivially over those short pieces and applying the first-derivative geometric-sum estimate on the complementary monotone pieces gives

\[
\ll_C T\eta+\eta/\lambda+\eta^{-1}.
\tag{10}
\]

Taking `eta` comparable to `lambda^{1/2}` (with the trivial estimate covering the harmless large-`lambda` endpoint) yields (9). Only the scale in (9) will be used below.

For an integer shift `1<=h<L`, define the differenced phase

\[
g_h(x):=f(x+h)-f(x).
\tag{11}
\]

Then

\[
g_h''(x)
=f''(x+h)-f''(x)
=
\int_0^h f'''(x+t)\,dt.
\tag{12}
\]

Because `f'''` has one sign and satisfies (7), for every `0<=x<=L-h` we have

\[
\frac{Ah}{8\pi M}
\le
|g_h''(x)|
\le
\frac{Bh}{\pi M}.
\tag{13}
\]

Applying (9) to the shifted correlation

\[
C_h
:=
\sum_{j=0}^{L-h-1}
e(f(j+h)-f(j))
\tag{14}
\]

gives, uniformly in `U`, `P_2`, `L`, and `h`,

\[
\boxed{
|C_h|
\ll_{A,B}
L\left(\frac hM\right)^{1/2}
+\left(\frac Mh\right)^{1/2}.
}
\tag{15}
\]

The estimate sees no resonance-tube parameter. Once one difference has removed the arbitrary quadratic correction down to a linear term, the second derivative of the differenced phase is controlled entirely by the logarithm's unavoidable cubic curvature.

## 3. Supercubic vector sums are uniformly small

The elementary van der Corput differencing inequality gives, for `1<=H<=L`,

\[
|S_L|^2
\ll
\frac{L^2}{H}
+
\frac LH
\sum_{h=1}^{H}|C_h|.
\tag{16}
\]

Insert (15). Since

\[
\sum_{h\le H}h^{1/2}\ll H^{3/2},
\qquad
\sum_{h\le H}h^{-1/2}\ll H^{1/2},
\tag{17}
\]

we obtain

\[
|S_L|^2
\ll_{A,B}
\frac{L^2}{H}
+
L^2\left(\frac HM\right)^{1/2}
+
L\left(\frac MH\right)^{1/2}.
\tag{18}
\]

Assume now `L>=2M^{1/3}` and choose

\[
H=\lfloor M^{1/3}\rfloor.
\tag{19}
\]

Then `H<=L`, and every term in (18) is bounded by a constant multiple of either `L^2M^{-1/3}` or `LM^{1/3}`. Taking square roots gives the announced uniform estimate

\[
\boxed{
|S_L|
\ll_{A,B}
LM^{-1/6}
+
L^{1/2}M^{1/6}.
}
\tag{20}
\]

Equivalently,

\[
\boxed{
\frac{|S_L|}{L}
\ll_{A,B}
M^{-1/6}
+
\left(\frac{M^{1/3}}{L}\right)^{1/2}.
}
\tag{21}
\]

Therefore, uniformly for the whole height window (3) and every quadratic rephasing,

\[
\boxed{
L/M^{1/3}\longrightarrow\infty
\quad\Longrightarrow\quad
S_L=o(L).
}
\tag{22}
\]

This is stronger than the fixed-arc ceiling in `ANF-160`. A large vector sum could in principle be assembled from phasors spread over several arcs, so fixed-arc noncoherence alone did not imply cancellation. Equation (22) does: once the physical block is supercubic, even such distributed vector coherence is uniformly destroyed by third-order curvature.

## 4. The cubic scale is sharp even for vector sums

The exponent `1/3` in (22) cannot be improved to a smaller uniform transition scale. `ANF-159` takes, for fixed integer `q>=1`,

\[
U_M=4\pi qM^2
\tag{23}
\]

and shows that the bare carrier satisfies

\[
\sum_{j<L}(M+j)^{-iU_M}
=
M^{-iU_M}L(1+o(1))
\tag{24}
\]

whenever `L=o(M^{1/3})`, while for sufficiently small fixed `c>0` it still has magnitude `Omega(L)` at

\[
L=\lfloor cM^{1/3}\rfloor.
\tag{25}
\]

`ANF-160` then shows that this is part of the full parity-quantized resonance-tube family and that fixed-arc coherence can indeed persist on `Theta(M^{1/3})` blocks. Since fixed-arc coherence implies a vector sum of size `Theta(L)` after a common rotation, (25) supplies the matching obstruction at the cubic scale.

Consequently the combined statements give a sharp carrier-only phase transition in physical block length:

\[
\boxed{
\begin{array}{ll}
L\asymp M^{1/3}:& \text{order-}L\text{ vector sums occur at resonant heights},\\[3pt]
L/M^{1/3}\to\infty:& \text{every quadratically rephased carrier sum is }o(L).
\end{array}
}
\tag{26}
\]

The resonance tubes remain mathematically real, but their role is now localized precisely: they describe where maximal coherence can survive **at the cubic scale**, not an exceptional set on which the carrier can remain coherently dangerous throughout arbitrarily longer endpoint supports.

## 5. The endpoint threat support is safely supercubic for the bare carrier

`ANF-158` gives the bow-scale comparison that makes (20) useful. A target-scale endpoint completion term forces a twisted residual prefix or suffix sum of size

\[
\Omega(\sqrt{X\log X}),
\tag{27}
\]

and the pointwise estimate `|r_X(n)|<<log X` forces any such spike to occupy at least

\[
L_0
\asymp
\sqrt{\frac{X}{\log X}}
\tag{28}
\]

physical sites, up to constants at the threat scale. With `M asymp X`, this is strongly supercubic:

\[
\frac{L_0}{M^{1/3}}
\asymp
\frac{M^{1/6}}{(\log M)^{1/2}}
\longrightarrow\infty.
\tag{29}
\]

Substituting (28) into (20), the first term is

\[
L_0M^{-1/6}
\asymp
M^{1/3}(\log M)^{-1/2},
\tag{30}
\]

while the second is

\[
L_0^{1/2}M^{1/6}
\asymp
M^{5/12}(\log M)^{-1/4}.
\tag{31}
\]

Hence

\[
\boxed{
|S_{L_0}|
\ll_{A,B}
M^{5/12}(\log M)^{-1/4}
=
o\!\left(\sqrt{\frac{M}{\log M}}\right).
}
\tag{32}
\]

In particular, even multiplying the entire carrier block by one common scalar of size `O(log M)` still gives only

\[
O\!\left(M^{5/12}(\log M)^{3/4}\right)
=
o(\sqrt{M\log M}),
\tag{33}
\]

below the endpoint threat scale (27). This comparison is deliberately **not** asserted for arbitrary coefficient sequences bounded by `log M`: variable signed coefficients can correlate with the phase and invalidate any inference from the unweighted carrier sum. Equation (33) only quantifies how far the smooth carrier itself is from producing the needed endpoint spike.

This removes one route proposed at the end of `ANF-160`. To rule out a **carrier-only** explanation at the support scale dictated by `ANF-158`, it is no longer necessary first to prove that the distinguished height stays `omega(M^{2/3})` away from the resonance tubes. Even at the center of those tubes, the cubic curvature forces cancellation once the block reaches the required supercubic support.

What remains is correspondingly sharper. For the actual source

\[
b_j
=
r_X(M+j)(M+j)^{-iU},
\tag{34}
\]

the arithmetic coefficient `r_X(M+j)` is neither constant nor known to have bounded variation of the kind that would permit a harmless summation-by-parts transfer of (20). It can change sign, be sparse, and in principle select favorable carrier phases. Thus (20) does **not** prove

\[
\sum_{j<L_0}r_X(M+j)(M+j)^{-iU}
=o(\sqrt{X\log X}),
\tag{35}
\]

and does not close the bow variance target. Instead it proves that any failure of (35) is genuinely a correlation phenomenon between the post-sieve residual and the carrier, rather than a consequence of smooth logarithmic resonance alone.

## 6. Prior-art boundary and next gate

The derivative-test mechanism surrounding (20) is classical. Olivier Robert's 2016 work on the `k`-th derivative test explicitly studies exponential sums with logarithmic phases plus polynomial corrections, including phases of the form `M^{k-1} log(M+m)+P(m)`. Rafael Arias de Reyna's 2024 explicit `d`-th derivative estimate gives another general quantitative framework in which a third derivative of order `1/M` yields cancellation on sufficiently long blocks. These are the correct prior-art neighbors of the argument above.

No external theorem is load-bearing in this finding. Equations (7), (12)--(15), and the one-step differencing calculation (16)--(20) provide a self-contained route to the scale needed here; the repository-specific content is the combination with the exact resonance geometry of `ANF-159`--`ANF-160` and the endpoint threat support from `ANF-158`. Accordingly this finding does not claim novelty for van der Corput's derivative method, and `SOURCES.md` requires no new durable dependency.

The next gate should now be weighted rather than carrier-geometric. A useful theorem would start from a dangerous endpoint event such as

\[
\left|
\sum_{j<r}r_X(M+j)(M+j)^{-iU}
\right|
\gtrsim
\sqrt{X\log X},
\qquad
r\gtrsim\sqrt{X/\log X},
\tag{36}
\]

and force an explicit structured correlation in the coefficient sequence `r_X(M+j)`: for example correlation with a carrier-adapted phase partition, a low-complexity sign pattern, or another statistic that can actually be attacked using the positive-prime minus finite-Ramanujan structure of `ANF-149`. An alternative is to bypass pointwise inverse structure and control the aggregate prefix/suffix square function appearing exactly in `ANF-157`--`ANF-158`.

The important route change is that the bare carrier is no longer the unresolved source of supercubic endpoint coherence. Its sharp vector-sum coherence ceiling is `M^{1/3}` even at resonant heights and after every quadratic smooth rephasing. Any bow-scale endpoint obstruction on the much longer support (28) must therefore use nontrivial structure of the arithmetic coefficients themselves.