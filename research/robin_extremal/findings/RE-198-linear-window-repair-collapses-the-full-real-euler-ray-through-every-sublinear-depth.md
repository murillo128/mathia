# RE-198 — Linear-window repair collapses the full real Euler ray through every sublinear depth

**Status:** `EXACT-DERIVED + GROWING-EULER-JET-MATCHING + FULL-REAL-EULER-RAY + SUBLINEAR-DEPTH-SUPPRESSION + LINEAR-CHEBYSHEV-WINDOWS + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-188-RE-197-SPLICE + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-188, RE-197.

`RE-197` turns the fixed-width `RE-186` repair into a full-real-axis stability theorem: exact matching through depth `K` suppresses the complete positive real Euler profile by essentially one factor `1/log p` per matched jet, uniformly while `K log log p=o(log p)`. It also identifies the obstruction to pushing the same estimate farther: the deeper `RE-188` construction must widen each logarithmic repair window to `W=4K`, so the first uncontrolled centered transport moment pays a factor of order `K^(K+1)`.

That loss does not immediately destroy full-ray near-nullity. The selector damping still contributes `(log p)^(-(K+1))`. Tracking the `RE-188` recurrence at the first omitted moment shows that the two effects balance only when `K` reaches the `log p` scale.

Put

\[
L:=\log p,
\qquad
1\le K=K(p)=o(L),
\qquad
r:=K+1,
\tag{1}
\]

and let `Q_{p,K}` be the ordinary-prime `{0,1,2}` matched control supplied by `RE-188`. Write

\[
D_Q(s)
:=
\sum_q (m_Q(q)-1)[-\log(1-q^{-s})]
\]

and

\[
d_p\asymp\frac1{\sqrt p\log p}
\]

for the canonical selector debt. Then there is an absolute constant `C>1` such that, uniformly throughout (1),

\[
\boxed{
\sup_{s\ge1}|D_Q(s)|
\ll
 d_p\,e^{C\sqrt K}K
 \left(\frac{CK}{L}\right)^{K+1}
 +p^{-1+o(1)}.
}
\tag{2}
\]

Consequently, whenever also `K\to\infty`,

\[
\boxed{
\sup_{s\ge1}|D_Q(s)|
\le
 d_p\exp\!\left(
 -(1-o(1))K\log\frac{L}{K}
 \right).
}
\tag{3}
\]

The `p^{-1+o(1)}` floor in (2) is smaller than the first term throughout the sublinear regime, because for `K=o(L)` one has

\[
K\log(L/K)=o(L).
\tag{4}
\]

All source-side conclusions of `RE-188` remain in force: support is on ordinary primes, every multiplicity lies in `{0,1,2}`, every Euler boundary derivative through order `K` matches exactly, every fixed Korobov--Vinogradov source envelope is respected, and the order-one selector-normalized Robin excursion is still present at `8p` before the repair begins.

Thus the full-real-axis near-null direction from `RE-197` extends from

\[
K=o\!\left(\frac{\log p}{\log\log p}\right)
\]

to **every sublinear depth**

\[
\boxed{K=o(\log p).}
\tag{5}
\]

The remaining transition is no longer the old scalar crossover `log p/log log p`; it begins only when the logarithmic spatial radius of the exact repair becomes comparable with the selector damping scale itself.

## 1. The real-ray Taylor mechanism needs only the first omitted absolute moment

Normalize exactly as in `RE-196`--`RE-197`:

\[
F(u):=p^uD_Q(1+u),
\qquad u\ge0.
\tag{6}
\]

The exact Euler expansion is

\[
F(u)
=
\sum_q c_q
\sum_{m\ge1}\frac{q^{-m}}m
 e^{-u\lambda_{m,q}},
\qquad
c_q:=m_Q(q)-1,
\qquad
\lambda_{m,q}:=m\log q-L.
\tag{7}
\]

Every modified prime satisfies `q>=2p`, hence every `lambda_(m,q)` is positive. Since `RE-188` matches `D_Q^(j)(1+)=0` for `0<=j<=K`, the Leibniz rule gives

\[
F^{(j)}(0)=0,
\qquad 0\le j\le K.
\tag{8}
\]

Define

\[
\mathfrak M_r
:=
\sum_q|c_q|
\sum_{m\ge1}\frac{q^{-m}}m\lambda_{m,q}^r.
\tag{9}
\]

Once this moment is finite, positivity of the damping rates and Taylor's integral remainder give

\[
|F(u)|\le\frac{\mathfrak M_r}{r!}u^r.
\tag{10}
\]

Multiplying by `p^-u` and optimizing at `u=r/L`,

\[
\sup_{s\ge1}|D_Q(s)|
\le
\frac{\mathfrak M_r}{r!}
\left(\frac r{eL}\right)^r
\asymp
\frac{\mathfrak M_r}{\sqrt r\,L^r}.
\tag{11}
\]

So the only new work relative to `RE-197` is to estimate the first omitted centered rate moment of the **linear-width** `RE-188` source.

## 2. Linear repair width costs `(CK)^r`, not enough to defeat selector damping below `log p`

Use the `RE-188` scales

\[
W=4K,
\qquad
h=e^{-a_0V(p)/8},
\qquad
x_n=16p\,e^{nh}.
\tag{12}
\]

The generation-`n` repair is supported in a logarithmic window of width `W`, so every first-harmonic rate in that generation satisfies

\[
0<\lambda_{1,q}\le C+W+nh.
\tag{13}
\]

Let `M_n` denote the exact Chebyshev-coordinate residual. `RE-188` inherits the microstep recurrence

\[
M_{n+1}
\le
\frac13M_n+O\!\left(\frac{K^2}{x_n}\right)
\tag{14}
\]

and its initial selector debt satisfies

\[
M_0\le e^{C\sqrt K}d_p.
\tag{15}
\]

The shell solve edits total absolute `H`-mass `O(KM_n)` in generation `n`, with `H(q)\asymp q^-1`. Hence the first-harmonic part of (9) obeys

\[
\mathfrak M_r^{(1)}
\ll
 d_pC^r
 +K\sum_{n\ge0}M_n(C+W+nh)^r.
\tag{16}
\]

For the selector-propagated part of (14), geometric contraction occurs long before the baseline moves by a macroscopic logarithmic distance. Since `W=4K` and `r=K+1`,

\[
\sum_{n\ge0}3^{-n}(C+W+nh)^r
\ll (CK)^r.
\tag{17}
\]

Indeed one may split `(C+W+nh)^r` into its width and displacement pieces; the latter contributes `h^r\sum 3^-n n^r`, and `hr/W=o(1)` because `h` is smaller than every negative power of `log p` in the present range.

For the quantization floor, interchange the two generation sums in (14). With `A=C+W`, for all sufficiently large `K` we have `A>=3r`, and therefore

\[
t\mapsto e^{-t}(A+t)^r
\]

is decreasing at a fixed exponential rate on `t>=0`. Thus

\[
\sum_{a\ge0}\frac{(A+ah)^r}{x_a}
\ll
\frac{(CK)^r}{ph}.
\tag{18}
\]

Combining (14)--(18),

\[
\boxed{
\mathfrak M_r^{(1)}
\ll
 d_p e^{C\sqrt K}K(CK)^r
 +\frac{K^3(CK)^r}{ph}.
}
\tag{19}
\]

Because `h^-1=p^{o(1)}` and `K=o(L)`, insertion into (11) gives

\[
\sup_{s\ge1}|D_Q^{(1)}(s)|
\ll
 d_p e^{C\sqrt K}K
 \left(\frac{CK}{L}\right)^r
 +p^{-1+o(1)}.
\tag{20}
\]

This is the main term in (2). The difference from `RE-197` is transparent: fixed-width transport contributed `C^r`, whereas the exact deep repair contributes `(CK)^r`. The selector still wins precisely while `K/L\to0`.

## 3. Exact prime powers remain below the quantization floor in the whole sublinear regime

It remains to check that the modes `m>=2` in (9) are uniformly harmless when `K` is much larger than the `RE-197` range. Since `r=o(L)`, for every modified `q>=2p` the prime-power series is still dominated by its first term beyond `m=1`:

\[
\sum_{m\ge2}
\frac{q^{-m}}m\lambda_{m,q}^r
\ll
2^r\frac{(\log q)^r}{q^2}.
\tag{21}
\]

For a repair prime in generation `n`, write `t=nh`. Then `q>=cp e^t` and

\[
\log q\le L+C+W+t.
\tag{22}
\]

After division by the `L^r` factor in (11), the extra spatial weight is controlled by

\[
e^{-t}
\left(1+\frac{C+W+t}{L}\right)^r.
\tag{23}
\]

Its logarithmic derivative is

\[
-1+\frac{r}{L+C+W+t},
\]

which is uniformly negative for `r=o(L)`. Hence (23) is largest at the first generation. There

\[
2^r
\left(1+O(K/L)\right)^r
=
\exp\!\left(O(K+K^2/L)\right)
=p^{o(1)}.
\tag{24}
\]

Using the same residual mass recurrence as above, the prime-power contribution to the full-ray bound is therefore

\[
\ll d_p p^{-1+o(1)}+p^{-2+o(1)}.
\tag{25}
\]

Equations (19) and (21)--(25) also prove absolute convergence of the exact `(K+1)`st normalized rate moment required in (10). This establishes (2).

## 4. Every sublinear depth gives superpolynomial-in-log precision

Assume now `K\to\infty` and put `f=L/K`. Then `f\to\infty`. The logarithm of the leading factor in (2) is

\[
-(K+1)\log\frac{L}{CK}+O(\sqrt K+\log K)
=
-(1-o(1))K\log\frac{L}{K}.
\tag{26}
\]

This proves (3). Moreover

\[
K\log\frac{L}{K}
=L\frac{\log f}{f}
=o(L),
\tag{27}
\]

so the absolute floor `p^-1+o(1)` is asymptotically smaller than the selector-debt term in (3).

The improvement over `RE-197` is substantial near the old boundary. For example, if

\[
K=\frac{L}{(\log L)^\alpha},
\qquad 0<\alpha<1,
\tag{28}
\]

then `RE-197` does not apply, while (3) gives

\[
\sup_{s\ge1}|D_Q(s)|
\le
 d_p\exp\!\left(
 -(\alpha+o(1))
 \frac{L\log\log L}{(\log L)^\alpha}
 \right).
\tag{29}
\]

More generally, even `K=L/f(L)` with an arbitrarily slowly diverging `f` remains a full-real-axis near-null direction, with gain

\[
\exp\!\left(-(1-o(1))\frac{L\log f}{f}\right).
\tag{30}
\]

Thus no precision theorem weaker than (3) can distinguish the ordinary source from this matched control while preserving the selector-scale Robin effect.

## Representation audit

The operative representation remains the normalized positive Laplace coordinate

\[
F(u)=p^uD_Q(1+u).
\]

The generic functional-analytic fact is elementary: if the first `K+1` moments of a positive-rate Laplace expansion vanish through order `K`, then the full transform is controlled by the first omitted absolute moment times the optimized Taylor factor `L^-(K+1)`. Nothing novel is claimed for Taylor remainder, moment matching, or Laplace inversion ill-conditioning.

The source-specific information enters through `RE-188`. Its ordinary-prime bounded-multiplicity repair supplies exact growing jet annihilation, the sharp full-window spatial width `W=4K`, geometric microstep contraction, prime-shell quantization, KV fidelity and the preserved pre-repair Robin transient. The present finding measures how that **actual arithmetic repair geometry** propagates into the first uncontrolled Laplace moment.

This audit also identifies what is lost. The estimate uses absolute centered transport moments, so it discards any signed cancellation in the `(K+1)`st moment. Therefore `K~log p` is a threshold of this representation-and-estimate pair, not a universal scalar-rigidity theorem. A better signed control of the omitted moment, or a different repair geometry whose source radius grows sublinearly in `K`, could push full-ray near-nullity farther.

Conversely, the much deeper existence theorem of `RE-188` is not contradicted. It constructs exact jet matching up to

\[
K=o\!\left(L^{5/3}(\log L)^{1/3}\right),
\]

but once `K` is comparable with or larger than `L`, the current absolute-moment bound no longer shows that the **whole** real Euler ray is small. Exact boundary matching and stable continuum near-nullity are different statements.

## Adversarial self-review

**Does the `W=4K` window make the `(K+1)`st moment so large that Taylor suppression is already lost at the old `L/log L` scale?** No. It contributes `(CK)^r`, so after selector damping the relevant ratio is `(CK/L)^r`. The old `L/log L` restriction in `RE-197` came from the *construction* used there, not from this wider-window Taylor balance.

**Could the enormous number of microsteps accumulate another exponential in `K`?** No at the scale used here. The selector-propagated residual contracts geometrically in generation number. The rounding floor sums against `x_n^-1=p^-1e^-nh`; because the base spatial offset is already `W=4K>3r`, the weighted exponential moment is boundary-dominated and costs only `h^-1(CK)^r`, with `h^-1=p^{o(1)}`.

**Are prime powers still uniform when `K` approaches `o(log p)` rather than `o(log p/log log p)`?** Yes. The only needed condition for the ratio test is `r=o(log q)`, and the spatial factor in (23) remains decreasing because `r/(L+C+W+t)=o(1)`. The resulting losses are `exp(o(L))`, swallowed by the extra factor `p^-1`.

**Does this include the arbitrary reciprocal-variation padding of `RE-195`--`RE-196`?** No. As in `RE-197`, growing-order derivative bounds for that remote padding were not established uniformly. The theorem uses the canonical `RE-188` matched control and proves a stronger depth range for full-real-ray near-nullity without claiming arbitrary unsigned variation simultaneously.

**Does (3) prove source non-identifiability?** No. `RE-174` still gives exact identification from exact data on a sufficiently rich unbounded temperature set. The result is about the absence of a Robin-scale modulus of continuity: two sources can have a macroscopic difference in the destination coordinate while their complete positive-real Euler profiles differ by the tiny amount in (3).

## Prior-art audit

Moment matching and Taylor bounds for Laplace transforms are classical, and the general inverse Laplace problem is well known to be ill-conditioned. The present proof imports no new external theorem. Its load-bearing arithmetic inputs are internal: the exact Euler resummation, linear-width Chebyshev shell construction, microstep recurrence and KV fidelity of `RE-188`, together with the normalized real-ray Taylor mechanism isolated in `RE-196`--`RE-197`. The remaining estimates are elementary exponential moments and Stirling. `SOURCES.md` therefore requires no change.

## Consequence for the research line

The full positive real Euler axis is now stably noncoercive through every jet depth `K=o(log p)` realized by the ordinary-prime `{0,1,2}` construction. The previous precision frontier at `log p/log log p` was not intrinsic; it reflected the fixed-width route used in `RE-197`.

The first unresolved continuum transition is now `K` comparable with `log p`, where the exact repair radius `W~K` and selector damping scale `L=log p` compete at order one. Beyond that, `RE-188` still supplies exact boundary matching far past `log p`, while `RE-189` predicts a different common-mode collapse near `(log p)^2`. Bridging those regimes requires either signed control of the first omitted moment, a repair representation with a smaller effective centered radius, or a genuinely complex/nonlocal observable. Merely increasing positive-real sampling density or demanding any tolerance above (3) cannot restore selector-scale rigidity.