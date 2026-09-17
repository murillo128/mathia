# RE-183 — Every fixed finite Euler-temperature panel remains non-rigid

**Status:** `EXACT-DERIVED + CONSTRUCTIVE-CONTROL + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + EXACT-FINITE-EULER-TEMPERATURE-MATCHING + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-174-FINITE-PANEL-BOUNDARY + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-173, RE-174, RE-181, RE-182.

`RE-174` identifies a complete exact source fingerprint: if the Euler discrepancy of a bounded ordinary-prime multiplicity perturbation vanishes on an unbounded sequence of real temperatures `sigma -> +infinity`, then every prime multiplicity is ordinary. It leaves open the opposite finite-sample question. `RE-182` shows that every fixed finite Taylor jet at the Mertens boundary can still be matched exactly, but a finite collection of values at distinct points `sigma>1` is different information and was not covered by that construction.

That finite-temperature escape is also realizable.

Fix once and for all a finite panel

\[
\Sigma=\{1=\sigma_0<\sigma_1<\cdots<\sigma_m\},
\qquad m\ge1.
\tag{1}
\]

For every sufficiently large selector scale `p` there exists an ordinary-prime-supported source `Q_{p,\Sigma}` with

\[
\boxed{m_{Q_{p,\Sigma}}(q)\in\{0,1,2\}}
\tag{2}
\]

such that, with

\[
F_\sigma(q):=-\log(1-q^{-\sigma}),
\qquad
D_Q(\sigma):=\sum_q(m_Q(q)-1)F_\sigma(q),
\tag{3}
\]

we have:

1. `Q_{p,\Sigma}` agrees with the ordinary prime source below `2p`;
2. it contains the canonical `RE-173` deletion packet `D_p subset [2p,3p]` and has no repair below `16p`;
3. the Mertens boundary value and every prescribed positive-temperature sample match exactly,
   \[
   \boxed{
   D_{Q_{p,\Sigma}}(1+)=0,
   \qquad
   D_{Q_{p,\Sigma}}(\sigma_i)=0
   \quad(1\le i\le m);
   }
   \tag{4}
   \]
4. the perturbation is absolutely summable at the boundary,
   \[
   \sum_q |m_Q(q)-1|F_1(q)<\infty,
   \tag{5}
   \]
   so every identity in (4) is obtained without conditional rearrangement;
5. its Chebyshev discrepancy satisfies
   \[
   \boxed{
   |\vartheta_{Q_{p,\Sigma}}(x)-\vartheta(x)|
   \ll_\Sigma \sqrt p+(\log x)^2,
   \qquad x\ge2p,
   }
   \tag{6}
   \]
   and hence, for every fixed `b>0`,
   \[
   |\vartheta_{Q_{p,\Sigma}}(x)-\vartheta(x)|
   \ll_{b,\Sigma}x\exp[-bV(x)],
   \qquad
   V(x)=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}};
   \tag{7}
   \]
6. before repair becomes visible, the `RE-173` normalized Robin coordinate still moves by order one,
   \[
   \boxed{
   \mathcal A_{p,8p}(Q_{p,\Sigma})-
   \mathcal A_{p,8p}(P)\asymp1;
   }
   \tag{8}
   \]
7. the first repair generation lies in a fixed `\Sigma`-dependent multiplicative window `[16p,C_\Sigma p]` and contains
   \[
   \boxed{
   \Theta_\Sigma\!\left(\frac{\sqrt p}{\log p}\right)
   }
   \tag{9}
   \]
   duplicated primes and the same order of deleted primes.

Thus **no fixed finite panel of exact Euler temperatures rigidifies the transient Robin prefix**, even after ordinary-prime support, nonnegative integer multiplicity, the hard cap `{0,1,2}`, exact Mertens matching, and every fixed KV relative envelope are imposed simultaneously. The finite side of the rigidity boundary left by `RE-174` is therefore non-rigid: exact source identification needs genuinely infinite temperature information, growing information with the selector, or another source invariant.

## 1. Normalize every temperature to one common shell mass

Retain the `RE-173` deletion packet

\[
D_p\subset[2p,3p],
\qquad
|D_p|=\left\lfloor\frac{\sqrt p}{\log p}\right\rfloor,
\tag{10}
\]

and put

\[
H(q):=F_1(q)=\log\frac q{q-1},
\qquad
b_i:=\sum_{q\in D_p}F_{\sigma_i}(q).
\tag{11}
\]

The deletion packet contributes `-b_i` to the discrepancy at `sigma_i`, so the repair must realize the vector `b=(b_0,...,b_m)`. As in `RE-173`,

\[
b_0=d_p\asymp\frac1{\sqrt p\log p}.
\tag{12}
\]

At a repair baseline `x`, scale the `i`-th coordinate by `x^(sigma_i-1)`. For shell factor `2^r`, `0<=r<=m`, define the real response matrix

\[
A_x(i,r)
:=
 x^{\sigma_i-1}
 \frac{F_{\sigma_i}(2^r x)}{H(2^r x)}.
\tag{13}
\]

For `sigma_0=1`, the row is exactly `1`. For every fixed `sigma>1`,

\[
F_\sigma(t)=t^{-\sigma}+O_\sigma(t^{-2\sigma}),
\qquad
H(t)=t^{-1}+O(t^{-2}),
\tag{14}
\]

and therefore

\[
\frac{F_\sigma(t)}{H(t)}
=t^{1-\sigma}(1+O_\Sigma(t^{-1})).
\tag{15}
\]

Consequently

\[
\boxed{
A_x(i,r)=z_i^r+O_\Sigma(x^{-1}),
\qquad
z_i:=2^{1-\sigma_i}.
}
\tag{16}
\]

The numbers

\[
1=z_0>z_1>\cdots>z_m>0
\tag{17}
\]

are distinct. Hence the limiting matrix `[z_i^r]_(i,r=0)^m` is an ordinary Vandermonde matrix and is invertible. Since the panel is fixed, there are constants `x_*(\Sigma)` and `\Lambda_\Sigma<infty` such that

\[
\boxed{
\|A_x^{-1}\|\le\Lambda_\Sigma
\qquad(x\ge x_*(\Sigma)).
}
\tag{18}
\]

This is the finite-temperature analogue of the centered Vandermonde in `RE-182`, but here no derivative recentering is needed: geometric shell factors turn distinct temperatures directly into the standard nodes `z_i`.

At the first baseline

\[
x_0:=16p,
\tag{19}
\]

the normalized deletion vector

\[
\rho_i^{(0)}:=x_0^{\sigma_i-1}b_i
\tag{20}
\]

has one common scale. Indeed, from `q in [2p,3p]`,

\[
\rho_i^{(0)}\ll_\Sigma
p^{\sigma_i-1}
\frac{\sqrt p}{\log p}p^{-\sigma_i}
\ll_\Sigma d_p,
\tag{21}
\]

while `rho_0^(0)=d_p`. Thus

\[
\|\rho^{(0)}\|_\infty\asymp_\Sigma d_p.
\tag{22}
\]

## 2. A finite-temperature ordinary-prime shell quantizer

For large `x`, let

\[
\delta_x:=(\log x)^{-4}
\tag{23}
\]

and use the disjoint shells

\[
I_{x,r}
:=
[2^r x,2^r x(1+\delta_x)],
\qquad
0\le r\le m.
\tag{24}
\]

The line's anchored KV prime-number-theorem error gives, uniformly over this fixed family of shell factors,

\[
\sum_{q\in I_{x,r}}H(q)
\asymp_\Sigma
\frac{\delta_x}{\log x}
=
\frac1{(\log x)^5}.
\tag{25}
\]

For `q in I_(x,r)`, equations (15)--(16) also give

\[
x^{\sigma_i-1}
\frac{F_{\sigma_i}(q)}{H(q)}
=
A_x(i,r)+O_\Sigma(\delta_x+x^{-1}).
\tag{26}
\]

Let `rho` be a normalized residual at baseline `x`, with `M=||rho||_infty`. Solve the real system

\[
A_xw=\rho.
\tag{27}
\]

By (18),

\[
\sum_{r=0}^m|w_r|\ll_\Sigma M.
\tag{28}
\]

Whenever `M<<_Sigma (log x)^(-6)`, every shell has much more `H`-mass than the target `|w_r|`. In shell `r`, choose distinct primes with coefficient `sgn(w_r)` until their `H`-mass is the largest one not exceeding `|w_r|`. One prime has `H(q)=O_\Sigma(1/x)`, so the scalar rounding error in each shell is `O_\Sigma(1/x)`.

Combining shell variation with this one-atom rounding gives a new residual, still normalized at `x`, satisfying

\[
\boxed{
M'
\ll_\Sigma
\delta_x M+
\frac1x.
}
\tag{29}
\]

The selected generation uses total absolute `H`-mass `O_\Sigma(M)`. Every chosen prime is fresh, so a negative coefficient deletes one ordinary copy and a positive coefficient duplicates one ordinary copy. The multiplicity therefore remains in `{0,1,2}`.

## 3. Geometric iteration makes all samples exact

Choose a fixed ratio

\[
R>2^{m+2}
\tag{30}
\]

large enough that generations are disjoint, and set

\[
x_n:=R^n x_0.
\tag{31}
\]

Let `r_i^(n)` be the remaining raw repair debt at temperature `sigma_i` before generation `n`, and define

\[
\rho_i^{(n)}:=x_n^{\sigma_i-1}r_i^{(n)},
\qquad
M_n:=\|\rho^{(n)}\|_\infty.
\tag{32}
\]

Apply the shell quantizer at `x_n`. Passing from the post-quantization normalization at `x_n` to that at `x_(n+1)` multiplies coordinate `i` by `R^(sigma_i-1)`. Since the panel is fixed, (29) yields

\[
M_{n+1}
\le
C_\Sigma R^{\sigma_m-1}
\left(
\delta_{x_n}M_n+\frac1{x_n}
\right).
\tag{33}
\]

After increasing the starting threshold `p_0(\Sigma)`, the coefficient of `M_n` is at most `R^(-2)` for every `n`. Therefore

\[
\boxed{
M_n
\ll_\Sigma
R^{-2n}d_p+
\frac1{x_{n-1}}
}
\qquad(n\ge1),
\tag{34}
\]

and the shell-capacity hypothesis `M_n<<_Sigma(log x_n)^(-6)` is preserved.

The total absolute boundary mass used at generation `n` is `O_\Sigma(M_n)`, so

\[
\sum_n M_n<\infty.
\tag{35}
\]

Hence

\[
\sum_q|m_Q(q)-1|H(q)<\infty.
\tag{36}
\]

For every `sigma>=1`, `0<F_sigma(q)<=H(q)`, so all temperature discrepancy series in the panel converge absolutely as well. Since `M_n->0`, the raw residuals satisfy

\[
|r_i^{(n)}|
=x_n^{1-\sigma_i}|\rho_i^{(n)}|
\le M_n\to0.
\tag{37}
\]

The infinite repair therefore realizes `b_i` exactly for every `i`, proving (4)--(5).

## 4. The first repair still pays the selector-scale deletion tariff

The construction does not hide the discrete tariff found in `RE-180`. In fact, any panel containing one temperature `sigma_*>1` forces both signs already in the first generation.

Let `w_r` be the real first-generation shell masses solving (27). The zeroth row gives

\[
\sum_r w_r=d_p.
\tag{38}
\]

For the row corresponding to `sigma_*`, define the normalized deletion average

\[
a_D
:=
\frac{x_0^{\sigma_*-1}}{d_p}
\sum_{q\in D_p}F_{\sigma_*}(q).
\tag{39}
\]

Using (15) and `q in [2p,3p]`,

\[
a_D
\ge
\left(\frac{16}{3}\right)^{\sigma_*-1}+o_\Sigma(1)
>1+c_\Sigma
\tag{40}
\]

for some fixed `c_\Sigma>0`. By contrast, every repair node lies at or beyond `x_0`, so its normalized response in that row is at most `1+o_\Sigma(1)` and is positive.

Write

\[
W_+:=\sum_{w_r>0}w_r,
\qquad
W_-:=-\sum_{w_r<0}w_r.
\tag{41}
\]

Then `W_+-W_-=d_p`, while the `sigma_*` equation and (40) imply

\[
(1+c_\Sigma)d_p
\le
(1+o(1))W_+.
\tag{42}
\]

Thus

\[
\boxed{
W_-\gg_\Sigma d_p,
\qquad
W_+\gg_\Sigma d_p.
}
\tag{43}
\]

The inverse bound (18) also gives `W_++W_-=O_\Sigma(d_p)`, so both are `Theta_\Sigma(d_p)`. Prime quantization changes either signed `H`-mass by only `O_\Sigma(1/p)=o(d_p)`. All first-generation primes lie between `16p` and `2^m16p(1+o(1))`, where `H(q)asymp_\Sigma1/p`. Therefore both signs use

\[
\boxed{
\Theta_\Sigma(pd_p)
=
\Theta_\Sigma\!\left(\frac{\sqrt p}{\log p}\right)
}
\tag{44}
\]

distinct primes. So the local honest-prime tariff of `RE-180` remains the correct polynomial scale even after any fixed finite number of exact temperature samples is added.

## 5. KV fidelity and the transient Robin excursion survive

At generation `n`, all selected primes are within a fixed `\Sigma`-dependent multiple of `x_n`. Since their total `H`-mass is `O_\Sigma(M_n)`, their total absolute Chebyshev mass is

\[
\ll_\Sigma x_n\log x_n\,M_n.
\tag{45}
\]

Using (34), the propagated selector-debt contribution sums to

\[
\ll_\Sigma
x_0d_p
\sum_{n\ge0}R^{-n}\log x_n
\ll_\Sigma\sqrt p,
\tag{46}
\]

while the rounding-forcing term contributes only `O_\Sigma(log x_n)` per completed generation. Summing completed generations below a height `x` gives `O_\Sigma((log x)^2)`. Together with the original deletion packet, whose Chebyshev mass is `O(sqrt p)`, this proves (6).

For every fixed `b>0`, both terms in (6) are `o(x exp[-bV(x)])` uniformly for `x>=2p` once `p` is sufficiently large, proving (7).

No repair prime occurs below `16p`, whereas the Robin observation height in `RE-173` is `8p`. Thus the finite-temperature repair cannot alter the already-created prefix excursion, and (8) follows verbatim from the `RE-173` calculation.

## 6. Representation audit and prior-art boundary

The finite-dimensional linear algebra is classical. After normalizing by `H` and the baseline power `x^(sigma-1)`, geometric shell factors `2^r` produce the ordinary Vandermonde matrix `[z_i^r]` with `z_i=2^(1-sigma_i)`. No novelty is claimed for Vandermonde interpolation, Euler-product absolute convergence in `Re s>1`, or finite-dimensional moment fitting.

The line-specific content is the constrained realization: the interpolation masses are quantized by **distinct ordinary primes with coefficients only `-1` and `+1`**, the one-prime residual is removed by an infinite geometrically separated continuation, the resulting source keeps multiplicities in `{0,1,2}`, the perturbation is absolutely summable at `s=1`, every prescribed temperature is matched exactly, the Chebyshev discrepancy stays below every fixed KV envelope, and the selector-scale Robin prefix remains displaced by order one.

A targeted prior-art search checked prescribed finite values of Dirichlet/Euler products, finite Dirichlet-series interpolation, and exponential/Vandermonde systems. It found the expected generic interpolation and Euler-product machinery but no result supplying this ordinary-prime bounded-multiplicity shell construction with simultaneous exact finite-temperature matching, KV fidelity, and transient Robin ambiguity. No new external theorem is load-bearing: the only arithmetic density input is the same KV/PNT shell supply already anchored in `SOURCES.md`, and the matrix invertibility is the elementary Vandermonde determinant. `SOURCES.md` therefore requires no new anchor.

## 7. Exact boundary of the claim

The panel `Sigma` is fixed before `p -> infinity`. Its cardinality, the largest temperature, the Vandermonde inverse norm, the generation ratio, and the threshold `p_0(Sigma)` may all deteriorate rapidly with the panel. This finding gives no uniform control for a panel whose size or temperatures grow with the selector.

The result does not contradict `RE-174`. An unbounded exact sequence `sigma_j -> infinity` exposes the smallest modified prime and is rigid. Likewise, an infinite sample set with an accumulation point inside `Re s>1` would be rigid by analyticity. The present construction establishes only the complementary finite statement. Infinite samples accumulating at the boundary `sigma=1`, and growing finite panels whose conditioning changes with `p`, remain separate questions.

Nor are the temperature equalities source-native consequences of Robin. They are deliberately strengthened matched-control data used to test sufficiency. Showing that even these exact samples can be preserved says that **finite-dimensional Euler summaries are still too weak as a source-fidelity certificate**; it does not assert that the physical prime source possesses an additional invariant of this form.

Finally, the construction is not a Robin counterexample. It is a non-rigidity control: it produces another ordinary-prime-labeled bounded-multiplicity source that agrees with increasingly strong finite Euler data while retaining the transient source ambiguity relevant to the matched-control program.

## Conclusion

`RE-174` showed that enough exact high-temperature information eventually identifies every prime multiplicity. `RE-183` shows that this rigidity cannot be approximated merely by choosing a more clever **fixed finite** set of temperatures: every such panel can still be interpolated by an honest `{0,1,2}` ordinary-prime repair at the same selector-scale discrete cost already exposed by `RE-180`.

The live boundary is therefore genuinely infinite- or growing-dimensional. A useful next obstruction must quantify how the interpolation conditioning and prime-shell cost behave when the number or range of temperatures grows with `p`, exploit an infinite boundary-accumulating family, or introduce a joint selector-conditioned arithmetic invariant that cannot be reproduced by geometrically separated prime repairs.

**Provenance:** derived against default-branch snapshot `2a3652475ec23f33fb65de7ba8e941d7b8fd15f5`; stable finding prefix `RE`; no adversarial sidecar was open; local clues were inspected; no clue-state, `mind/**`, README, graph, or source-registry mutation required.