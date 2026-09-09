# XF-132 — central heat-spectrum clustering makes zero-delay one-trace inversion exponentially ill-conditioned

**Status:** `EXACT-DERIVED` + `NEGATIVE/CONDITIONING-BOUNDARY` + `TEMPORAL-OBSERVABILITY` + `UNIT-CIRCLE-ADMISSIBLE` + `CROSS-SCALE`. XF-130 shows that a single off-circle heat trace determines the complete periodic unit-circle divisor exactly, and XF-131 shows that delaying that trace beyond the microscopic heat clock exponentially suppresses collision-sensitive central-shell information. There is a second, independent conditioning barrier: **even with zero delay and the entire exact future trace available, the temporal spectral inversion can be exponentially ill-conditioned in the degree**.

Let `N=2M` and use the XF-067 normalized coefficient heat flow

\[
E(w,s)=\sum_{k=0}^{2M}E_k e^{-\delta_k s}w^k,
\qquad
\delta_k=a k(2M-k),
\qquad
a=\frac{4\pi^2}{L^2}.
\tag{1}
\]

Fix a root-spacing off-circle probe

\[
\zeta_N=-e^{\sigma/N},
\qquad \sigma\ne0\ \text{fixed},
\tag{2}
\]

and write the one-point trace in reflected-shell amplitudes as in XF-130,

\[
Q_\zeta(s)
=\sum_{k=0}^{M}B_k e^{-\delta_k s}.
\tag{3}
\]

For every integer

\[
1\le r\le \frac M2,
\tag{4}
\]

there is a real-palindromic coefficient direction supported only on the `r+1` central shells `k=M,M-1,...,M-r` such that, after normalizing its reflected-shell amplitude vector to have `ell^infinity` norm one, its **entire** trace on `[0,infinity)` has size at most

\[
\boxed{
 r!\left(\frac{r}{e(M^2-r^2)}\right)^r
\le
\left(\frac{r^2}{e(M^2-r^2)}\right)^r.
}
\tag{5}
\]

In particular, for `r<=M/2`,

\[
\boxed{
\|\Delta Q\|_{L^\infty([0,\infty))}
\le
(3e)^{-r}\,\|\Delta B\|_{\ell^\infty}.
}
\tag{6}
\]

Taking `r=floor(M/2)` gives a local inverse condition number at least

\[
\boxed{
(3e)^{\lfloor M/2\rfloor}
=
\exp(cN+O(1)),
\qquad
c=\frac14\log(3e)>0.
}
\tag{7}
\]

This bad direction is not an ambient coefficient artifact. It can be realized by arbitrarily small perturbations of the simple unit-circle polynomial `1+w^{2M}` that remain **simple and unit-circle-rooted**. Thus XF-130's `O(N)` spatial reflected-pair inversion is not the dominant worst-case conditioning of its one-channel tomography. The temporal decoder itself has exponentially small singular directions already at `s=0`.

The result is deliberately about reconstruction of the Vieta/reflected-shell state. It does **not** prove that the periodic Newman transition time is exponentially ill-conditioned at zero delay; XF-131 remains the transition-sharp delayed-trace obstruction. A direct transition observable could in principle bypass complete coefficient recovery.

## 1. Central heat rates form an exact quadratic cluster

For `j=0,...,r`, the central shells satisfy

\[
\delta_{M-j}
=a(M-j)(M+j)
=a(M^2-j^2).
\tag{8}
\]

Put

\[
y_j=j^2
\tag{9}
\]

and define the barycentric weights for the nodes `0^2,1^2,...,r^2` by

\[
\omega_j
:=
\frac{1}{\prod_{0\le \ell\le r,\ \ell\ne j}(j^2-\ell^2)}.
\tag{10}
\]

They are explicit:

\[
\omega_0=\frac{(-1)^r}{(r!)^2},
\tag{11}
\]

and for `1<=j<=r`,

\[
\boxed{
\omega_j
=
\frac{2(-1)^{r-j}}{(r-j)!(r+j)!}.
}
\tag{12}
\]

Let

\[
W_r:=\max_{0\le j\le r}|\omega_j|,
\qquad
c_j:=\frac{\omega_j}{W_r}.
\tag{13}
\]

Then `max_j |c_j|=1`. Since `W_r>=|omega_0|=(r!)^{-2}`,

\[
\frac1{W_r}\le (r!)^2.
\tag{14}
\]

The defining property of barycentric divided-difference weights gives

\[
\sum_{j=0}^r\omega_j p(j^2)=0
\tag{15}
\]

for every polynomial `p` of degree `<r`. Hence the central packet

\[
F_r(s)
:=
\sum_{j=0}^r c_j e^{-a(M^2-j^2)s}
\tag{16}
\]

annihilates the first `r` time jets at the target slice:

\[
\boxed{
F_r^{(m)}(0)=0,
\qquad 0\le m<r.
}
\tag{17}
\]

This is already stronger than a generic statement that nearby exponentials are difficult to separate. The exact quadratic heat spectrum supplies a length-`r+1` central packet whose first `r` temporal moments cancel identically.

## 2. Divided differences control the complete future trace, not only its initial jet

Set

\[
x=as\ge0.
\tag{18}
\]

Equation `(16)` becomes

\[
F_r(s)
=
\frac{e^{-M^2x}}{W_r}
\sum_{j=0}^r\omega_j e^{j^2x}.
\tag{19}
\]

The sum is exactly the order-`r` divided difference of the function `y -> e^{xy}` at the nodes `0^2,...,r^2`. The elementary divided-difference mean-value formula therefore gives, for some point between `0` and `r^2`,

\[
\left|
\sum_{j=0}^r\omega_j e^{j^2x}
\right|
\le
\frac{x^r}{r!}e^{r^2x}.
\tag{20}
\]

Combining `(14)`, `(19)`, and `(20)` yields the global estimate

\[
|F_r(s)|
\le
r!\,x^r e^{-(M^2-r^2)x}.
\tag{21}
\]

The right-hand side is maximized at

\[
x_*=rac{r}{M^2-r^2},
\tag{22}
\]

so

\[
\boxed{
\|F_r\|_{L^\infty([0,\infty))}
\le
r!\left(\frac{r}{e(M^2-r^2)}\right)^r.
}
\tag{23}
\]

Using `r!<=r^r` gives the second bound in `(5)`. If `r<=M/2`, then

\[
r^2\le\frac{M^2}{4},
\qquad
M^2-r^2\ge\frac{3M^2}{4},
\tag{24}
\]

and `(6)` follows.

The scale factor `a=4pi^2/L^2` disappears from the condition estimate because the observation interval contains all `s>=0`: it only reparametrizes the time variable `x=as`. Thus this is not a small-`a` artifact of the current Xi period choice.

Equation `(17)` explains why taking more derivatives at `s=0` does not cheaply repair the problem. A packet of depth `r` is invisible to every derivative of order `<r`; resolving it by an `r`th or higher jet necessarily enters the same high-order inverse problem. Equation `(23)` strengthens that local statement by showing that waiting for later heat times does not rescue the signal either.

## 3. The exponentially small trace direction lies inside the simple unit-circle class

It remains to exclude the possibility that `(16)` is merely an inadmissible amplitude direction. Start from

\[
E_*(w)=1+w^{2M}.
\tag{25}
\]

All of its `2M` roots are simple and lie on the unit circle. For the physical radial probe `(2)`, choose real coefficients `A_j` so that

\[
\Delta E(w)
=A_0w^M
+
\sum_{j=1}^r A_j\left(w^{M-j}+w^{M+j}\right)
\tag{26}
\]

produces exactly the reflected-shell amplitudes `c_j`. Namely,

\[
A_0=\frac{c_0}{\zeta_N^M},
\tag{27}
\]

and for `1<=j<=r`,

\[
A_j
=
\frac{c_j}
{\zeta_N^{M-j}+\zeta_N^{M+j}}.
\tag{28}
\]

The denominators are nonzero and satisfy

\[
\zeta_N^{M-j}+\zeta_N^{M+j}
=
2(-1)^{M-j}e^{\sigma/2}
\cosh\!\left(\frac{\sigma j}{N}\right).
\tag{29}
\]

For fixed `sigma` and `j<=M/2`, these factors are bounded above and below by positive constants depending only on `sigma`. Hence there is no hidden exponential spatial amplification in `(27)`--`(28)`.

For real `epsilon`, set

\[
E_\epsilon(w)=E_*(w)+\epsilon\Delta E(w).
\tag{30}
\]

This is real-palindromic with constant and terminal coefficients still equal to one. Divide by `w^M` and put

\[
z=w+w^{-1}.
\tag{31}
\]

Using `w^j+w^{-j}=2T_j(z/2)`, one obtains

\[
w^{-M}E_\epsilon(w)
=
R_\epsilon(z),
\tag{32}
\]

where

\[
R_\epsilon(z)
=
2T_M(z/2)
+
\epsilon\left(
A_0+2\sum_{j=1}^r A_jT_j(z/2)
\right).
\tag{33}
\]

At `epsilon=0`, the `M` roots of `R_0` are

\[
z_q
=2\cos\frac{(2q-1)\pi}{2M},
\qquad 1\le q\le M,
\tag{34}
\]

and are simple and strictly inside `(-2,2)`. For each fixed `M`, simplicity and strict interior location persist under all sufficiently small real coefficient perturbations. Therefore, for all sufficiently small nonzero `epsilon`, `R_epsilon` still has `M` simple roots in `(-2,2)`. Each such root lifts under `(31)` to two distinct conjugate points on the unit circle, so

\[
\boxed{
E_\epsilon
\text{ has }2M\text{ simple unit-circle roots.}
}
\tag{35}
\]

By construction, the trace difference between `E_epsilon` and `E_*` is exactly

\[
Q_{\zeta,\epsilon}(s)-Q_{\zeta,*}(s)
=\epsilon F_r(s),
\tag{36}
\]

while

\[
\max_{0\le j\le r}
|B_{M-j}(E_\epsilon)-B_{M-j}(E_*)|
=|\epsilon|.
\tag{37}
\]

Combining `(23)`, `(36)`, and `(37)` proves `(5)`--`(7)` **inside an open simple unit-circle neighborhood**. The small admissible radius may depend on `M`; that does not affect the local condition ratio because both the state and trace differences scale by the same `epsilon`.

## 4. What this changes after XF-130 and XF-131

XF-130 separated two possible conditioning costs. Moving only one root spacing off the unit circle breaks each reflected pair with worst spatial amplification `O(N)`, but the finding explicitly left the extraction of the amplitudes `B_k` from the heat trace as a separate problem. XF-132 now gives an exact worst-case lower bound for that missing temporal decoder:

\[
\boxed{
\text{zero-delay full-history temporal inversion}
\quad\text{can cost}\quad
\exp(cN).
}
\tag{38}
\]

This mechanism is distinct from XF-131. In the single central-shell family of XF-131, the central coefficient is visible at order one when `s_0=0`; the exponential loss appears only after a positive delay. Here many nearby central rates are combined so that they cancel to high order at `s=0` and remain uniformly tiny for **all** later times. The new obstruction therefore survives even when the source interface reaches the target slice exactly.

For the source-facing route, exact identifiability is no longer enough to justify reconstructing an unrestricted periodic divisor from one noisy or approximate Xi trace. A polynomially accurate source-to-periodic trace cannot support a uniformly stable inversion of all Vieta shells in the `L^infinity([0,infinity))` observation norm. To use the single-channel architecture quantitatively, one needs at least one genuinely new ingredient: exponentially accurate relative trace control on the relevant degree scale, a preconditioned/weighted observation norm that measures the high temporal jets with commensurate accuracy, additional independent spatial channels, or Xi-specific structure excluding the central divided-difference directions.

The accepted Gaussian-reference clue remains live but becomes more demanding. A source-normalized estimate for one off-circle value must now be compared not only with the `O(N)` spatial inversion of XF-130 and the delayed central-shell threshold of XF-131, but also with the exponential zero-delay temporal condition `(7)` if the intended downstream step reconstructs the complete divisor.

There is also an important escape boundary. A theorem that goes directly from an Xi-specific trace statistic to a transition inequality need not reconstruct every `B_k`, and this finding does not rule it out. Likewise, an observation available for negative heat time, or several coupled spatial probes, lies outside the exact one-sided single-trace norm used here.

## 5. Prior-art and novelty boundary

Severe conditioning of exponential fitting, Prony systems, and Vandermonde inversion is classical. In particular, Batenkov--Yomdin, *On the Accuracy of Solving Confluent Prony Systems* (SIAM J. Appl. Math. 73 (2013), 134--154, DOI `10.1137/110836584`), studies local error amplification in Prony-type reconstruction, and the modern close-exponent literature analyzes sharp stability loss when exponential nodes cluster. Classical real-Vandermonde work likewise gives exponential condition growth in many node geometries.

Those results delimit the general numerical-analysis phenomenon; they are not load-bearing for `(10)`--`(37)`. The present proof is the explicit divided-difference packet for the **known quadratic Xi-flow heat rates** together with the real-palindromic perturbation `(26)`--`(35)` showing that the bad direction survives inside the exact simple unit-circle divisor class used by XF-130. No external theorem is needed beyond elementary divided differences and continuity of simple polynomial roots, so `SOURCES.md` acquires no new dependency.

The line-specific mathematical delta is therefore not a claim that exponential-sum inversion can be ill-conditioned. It is the exact compatibility of an exponentially small temporal singular direction with all three structures that matter here: the XF-067 heat spectrum, the one-root-spacing XF-130 probe, and unit-circle root admissibility.

## 6. Consequence for `xi_flow`

The periodic **identifiability** statement of XF-130 remains exact, but its one-channel compression is not a polynomially stable tomography theorem. Together XF-130--XF-132 now separate three different gates:

- spatial reflected-pair inversion costs only `O(N)` at one-root-spacing displacement;
- positive heat delay can cost `exp(delta_M s_0)` even for a transition-sharp single-shell family;
- even at zero delay, decoding a growing central packet from the complete future trace can cost `exp(cN)`.

The next source-faithful step should therefore avoid treating complete divisor reconstruction as a free intermediate operation. A useful positive theorem must either transport a much stronger norm than pointwise trace accuracy, exploit enough extra source structure to rule out the divided-difference packet, or connect the accessible Xi trace directly to a transition-coercive quantity without inverting the full central heat spectrum.