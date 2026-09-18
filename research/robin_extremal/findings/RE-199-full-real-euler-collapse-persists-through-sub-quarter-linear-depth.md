# RE-199 — Full-real Euler collapse persists through sub-quarter linear depth

**Status:** `EXACT-DERIVED + FULL-REAL-EULER-RAY + LINEAR-DEPTH-SUPPRESSION + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-188-RE-198-STRENGTHENING + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-188, RE-198.

`RE-198` proves full-real-axis near-nullity for every sublinear jet depth `K=o(log p)` by combining the exact `RE-188` ordinary-prime repair with a selector-centered Laplace Taylor bound. Its proof leaves the first omitted absolute moment in the coarse form `(C K)^(K+1)`, so it deliberately stops before the regime `K asymp log p`.

Keeping the exact width `W=4K` from `RE-188` instead of hiding it inside `C K` shows that the same construction already penetrates a fixed positive fraction of the logarithmic scale. Put

\[
L:=\log p,
\qquad r:=K+1,
\qquad 0<\eta<\frac14,
\qquad 1\le K\le \eta L,
\tag{1}
\]

and let `Q_{p,K}` be the ordinary-prime `{0,1,2}` source constructed in `RE-188`. Write

\[
D_Q(s)
:=
\sum_q (m_Q(q)-1)[-\log(1-q^{-s})],
\qquad
 d_p\asymp\frac1{\sqrt p\log p}.
\tag{2}
\]

Then, uniformly under (1),

\[
\boxed{
\sup_{s\ge1}|D_Q(s)|
\ll
 d_p\,e^{C\sqrt K}K
 \left(\frac{4K+O(1)}{L}\right)^{K+1}
 +d_p\,p^{-1+o(1)}.
}
\tag{3}
\]

Consequently, for every fixed `eta<1/4` there is `c_eta>0` such that whenever `K=K(p)\to\infty` and `K\le eta log p`,

\[
\boxed{
\sup_{s\ge1}|D_Q(s)|
\le
 d_p e^{-c_\eta K}
}
\tag{4}
\]

for all sufficiently large `p`. More precisely, if

\[
\frac K{\log p}\longrightarrow\kappa
\qquad
\left(0<\kappa<\frac14\right),
\]

then

\[
\boxed{
\sup_{s\ge1}|D_Q(s)|
\le
 d_p\exp\!\left(
 -(1-o(1))K\log\frac1{4\kappa}
 \right).
}
\tag{5}
\]

All source-side properties of `RE-188` remain unchanged: exact Euler boundary matching through depth `K`, ordinary-prime support, multiplicities in `{0,1,2}`, every fixed Korobov--Vinogradov source envelope, and the order-one selector-normalized Robin excursion at `8p` before repair begins.

Thus the `K~log p` scale identified in `RE-198` is not itself an onset of scalar rigidity. The existing linear-window repair remains continuum-near-null throughout a genuine linear-depth wedge. The constant `1/4` is a threshold of the present `W=4K` absolute-moment estimate, not a universal rigidity constant.

## 1. The selector-centered Taylor reduction remains exact at linear depth

Normalize as in `RE-198`,

\[
F(u):=p^uD_Q(1+u),
\qquad u\ge0.
\tag{6}
\]

Writing `c_q=m_Q(q)-1` and expanding the Euler factors gives

\[
F(u)
=
\sum_q c_q
\sum_{m\ge1}\frac{q^{-m}}m
 e^{-u\lambda_{m,q}},
\qquad
\lambda_{m,q}:=m\log q-L.
\tag{7}
\]

Every modified prime satisfies `q>=2p`, hence every `lambda_(m,q)>0`. Exact matching of `D_Q^(j)(1+)` for `0<=j<=K` implies

\[
F^{(j)}(0)=0,
\qquad 0\le j\le K.
\tag{8}
\]

Define the first omitted absolute centered moment

\[
\mathfrak M_r
:=
\sum_q|c_q|
\sum_{m\ge1}\frac{q^{-m}}m\lambda_{m,q}^r.
\tag{9}
\]

The estimates below prove that this moment is finite in the whole range (1), so Taylor's integral remainder is legitimate. Positivity of the damping rates gives

\[
|F(u)|
\le
\frac{\mathfrak M_r}{r!}u^r.
\tag{10}
\]

Since `D_Q(1+u)=p^-u F(u)`, optimization at `u=r/L` and Stirling yield

\[
\boxed{
\sup_{s\ge1}|D_Q(s)|
\ll
\frac{\mathfrak M_r}{\sqrt r\,L^r}.
}
\tag{11}
\]

No `K=o(L)` hypothesis has entered. The issue is only how large the first omitted centered moment actually is.

## 2. The first-harmonic moment sees the exact width `4K`, not an unspecified `C K`

Use the `RE-188` microstep scales

\[
h=e^{-a_0V(p)/8},
\qquad
x_n=16p\,e^{nh},
\qquad
W=4K.
\tag{12}
\]

Let `M_n` be the exact Chebyshev-coordinate residual in generation `n`. `RE-188` supplies

\[
M_{n+1}
\le
\frac13M_n+O\!\left(\frac{K^2}{x_n}\right),
\qquad
M_0\le e^{C\sqrt K}d_p,
\tag{13}
\]

and the shell solve edits total absolute `H`-mass `O(KM_n)` in that generation, where `H(q)\asymp q^-1` on the modified support.

For the first Euler harmonic, every generation-`n` rate lies below

\[
\lambda_{1,q}
\le
A+nh+o(1),
\qquad
A:=4K+\log16+O(1).
\tag{14}
\]

Iterating (13), the selector-propagated part of the weighted generation sum contains

\[
\sum_{n\ge0}3^{-n}(A+nh)^r.
\tag{15}
\]

Since `r/A=1/4+o(1)` and `h=o(1)`,

\[
(A+nh)^r
\le
A^r\exp\!\left(\frac{rnh}{A}\right)
\le
A^r e^{nh/3}
\]

for all sufficiently large `p`. Hence (15) is `O(A^r)`.

For the quantization floor, interchange the two generation sums coming from (13). The same geometric estimate reduces the contribution to

\[
\sum_{a\ge0}\frac{(A+ah)^r}{x_a}
=
\frac1{16p}
\sum_{a\ge0}e^{-ah}(A+ah)^r.
\tag{16}
\]

Because

\[
\frac d{dt}\log\bigl(e^{-t}(A+t)^r\bigr)
=-1+\frac r{A+t}
\le-\frac23
\]

for large `p`, the sum in (16) is boundary-dominated and

\[
\sum_{a\ge0}\frac{(A+ah)^r}{x_a}
\ll
\frac{A^r}{ph}.
\tag{17}
\]

Including the fixed selector deletion packet therefore gives

\[
\boxed{
\mathfrak M_r^{(1)}
\ll
 d_p e^{C\sqrt K}K A^r
 +\frac{K^3A^r}{ph}
 +d_p C_0^r,
}
\tag{18}
\]

for an absolute `C_0`. Inserting (18) into (11), using `h^-1=p^{o(1)}`, gives

\[
\sup_{s\ge1}|D_Q^{(1)}(s)|
\ll
 d_p e^{C\sqrt K}K
 \left(\frac{4K+O(1)}L\right)^r
 +p^{-1+o(1)}
 \left(\frac{4K+O(1)}L\right)^r.
\tag{19}
\]

This is the step hidden by the generic `(C K)^r` notation in `RE-198`. Once `K/L` has a fixed limit, the actual constant carried by this representation matters.

## 3. Prime powers retain a full extra factor `p^-1` at small linear depth

The `m>=2` modes need a separate check because the `RE-198` estimate used the assumption `r=o(L)`. In fact the centered rate makes them uniformly cheaper throughout the present linear wedge.

Put

\[
x:=\frac{\log(q/p)}L\ge0.
\]

For `m>=2`,

\[
\frac{\lambda_{m,q}}L
=(m-1)+mx,
\]

and therefore

\[
q^{-(m-1)}
\left(\frac{\lambda_{m,q}}L\right)^r
=
\exp\!\left\{
L\left[
-(m-1)(1+x)
+\frac rL\log((m-1)+mx)
\right]
\right\}.
\tag{20}
\]

Fix `eta<1/4`. The derivative of the bracket in (20) with respect to `x` is at most

\[
-(m-1)+\eta\frac m{m-1}<0.
\tag{21}
\]

Thus the worst case is `x=0`. At that endpoint the exponent is

\[
-(m-1)L+r\log(m-1).
\tag{22}
\]

Since `r/L<1` and `-y+(r/L)log y` is decreasing for `y>=1`, summing over `m>=2` gives the uniform bound

\[
\boxed{
\sum_{m\ge2}
\frac{q^{-m}}m\lambda_{m,q}^r
\ll
p^{-1}q^{-1}L^r.
}
\tag{23}
\]

This is stronger than the crude `2^r` majorant once `r` is a fixed fraction of `L`.

The total reciprocal variation of the matched source satisfies, by (13) and the shell `H`-mass bound,

\[
\mathcal H
:=
\sum_q\frac{|c_q|}{q}
\ll
 d_p+K\sum_{n\ge0}M_n
\ll
 d_p e^{C\sqrt K}K
 +\frac{K^3}{ph}
=
 d_p p^{o(1)}
\tag{24}
\]

uniformly for `K=O(L)`. Hence (23) gives

\[
\mathfrak M_r^{(\ge2)}
\ll
p^{-1}L^r\mathcal H,
\]

and (11) yields

\[
\boxed{
\sup_{s\ge1}|D_Q^{(\ge2)}(s)|
\ll
 d_p p^{-1+o(1)}.
}
\tag{25}
\]

So the exact prime powers do not create a new linear-depth obstruction before the first-harmonic spatial radius does.

## 4. Every fixed ratio below `1/4` gives exponential-in-depth continuum suppression

Combining (19) and (25) proves (3). If `K/L -> kappa<1/4`, then

\[
\frac{4K+O(1)}L=4\kappa+o(1)<1,
\]

while `C sqrt(K)+log K=o(K)`. Therefore the first term in (3) is

\[
d_p\exp\!\left(
-(1-o(1))K\log\frac1{4\kappa}
\right).
\tag{26}
\]

The prime-power floor is smaller. Indeed

\[
\kappa\log\frac1{4\kappa}
\le\frac1{4e}<1,
\tag{27}
\]

so even at the largest allowed depth the relative factor in (26) decays much more slowly than `p^-1`. This proves (5), and the uniform version (4) follows by replacing `kappa` with any fixed `eta<1/4`.

For example, `K=(1/8)log p` gives a full-real Euler discrepancy smaller than the selector debt by

\[
\exp\!\left(-(\log2+o(1))K\right)
=p^{-\log2/8+o(1)},
\]

while the Robin transient before repair remains order one after selector normalization.

Thus a polynomial-in-`p` continuum precision gap can coexist with exact matching of a linear number of Euler boundary jets and with an unchanged selector-scale Robin excursion.

## Representation audit

The generic statement used here is elementary Laplace moment cancellation: after `K+1` derivatives vanish at the boundary, the whole positive real transform is controlled by the first omitted absolute centered moment. Severe conditioning of Laplace inversion and rapid compressibility of truncated Laplace channels are classical phenomena already reflected in `RE-190`--`RE-193`; no novelty is claimed for Taylor remainder, moment matching, or transform ill-conditioning.

The source-specific content is the arithmetic size of that omitted moment. `RE-188` supplies an actual ordinary-prime `{0,1,2}` repair with exact window width `4K`, geometric microstep contraction, quantized prime shells, fixed-KV fidelity and a preserved pre-repair Robin excursion. The present calculation shows that the exact `4K` radius, rather than an unspecified constant multiple of `K`, survives all the way to the continuum estimate, and that centered prime-power modes still pay an additional factor `p^-1` at linear depth.

The number `1/4` therefore belongs to this representation: it is where the absolute first-harmonic factor `(4K/L)^(K+1)` stops decaying. It is **not** a theorem that scalar Euler data become rigid at `K=(1/4)log p`, and it is not a lower bound on what another repair frame can achieve.

## Adversarial self-review

**Does `RE-188` itself permit `K` proportional to `log p`?** Yes. Its construction is valid throughout `K=o((log p)^(5/3)(log log p)^(1/3))`, so every fixed linear depth lies well inside the source-fidelity range. The shell spacing and KV estimates used there remain stronger than required here.

**Was `K=o(L)` hidden in the weighted generation sums?** No. Those sums only require `r/A<1`, and here `A=4K+O(1)` gives `r/A=1/4+o(1)`. Geometric contraction controls the selector-propagated generations, while the quantization tail is integrated against `e^-t` and is boundary-dominated for the same reason.

**Can prime powers explode because `r` is now linear in `L`?** Equation (20) keeps the exact centered rate instead of replacing it by `m log q`. For `r/L<1/4`, every `m>=2` contribution decreases as the prime is moved outward, and the discrete `m`-sum is maximized at `m=2`. This leaves the full extra factor `p^-1` in (23).

**Is the quarter threshold sharp?** Only for the displayed absolute-moment upper bound in the `W=4K` frame. `RE-188` proves merely that a linear width is necessary for its full-window Gauss--Chebyshev representation once `K` is much larger than `L`; it does not prove that the coefficient `4` is optimal. Signed cancellation in the first omitted moment, a narrower nonuniform frame, or a different scalar representation could cross `1/4`.

**Does this approach `RE-174` source rigidity?** No. `RE-174` is exact infinite-precision identification from an unbounded Euler-temperature family. The present theorem goes in the opposite direction: it constructs finite-depth arithmetic sources whose entire positive real Euler ray is exponentially close while their Robin transient differs by order one. It is a stable non-identifiability statement, not an exact equality statement.

## Prior-art audit

A targeted search against moment-matching and truncated/inverse-Laplace literature found the expected general results on severe inverse-Laplace ill-conditioning and rapidly decaying singular information. Those results concern generic transforms and do not supply the ordinary-prime bounded-multiplicity control, the `4K` arithmetic repair radius, KV fidelity, or the preserved Robin excursion used here.

No new external theorem is load-bearing. The only arithmetic source input remains the Korobov--Vinogradov prime-number-theorem control already anchored in `research/robin_extremal/SOURCES.md`; all additional estimates above are elementary consequences of `RE-188` and the exact Euler expansion. `SOURCES.md` therefore requires no change.

## Consequences

`RE-198` left `K~log p` as the first unresolved continuum scale because its theorem required `K/log p -> 0`. The present finding shows that this boundary was too coarse: **the same source remains full-ray near-null for every fixed depth ratio below `1/4`**.

The next scalar question is correspondingly narrower. Either improve the signed or absolute control of the first omitted moment enough to cross the `4K/L=1` balance, reduce the effective repair radius below `4K`, or prove that some source-native quantity absent from the current scalar Euler ray becomes coercive there. Merely invoking the fact that `K` is of order `log p` is no longer sufficient evidence for a rigidity transition.