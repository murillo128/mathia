# AF-180 — Euler-product prime-norm fidelity has a sharp scale–bandwidth stability barrier

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-017 proves that an exact Euler-product function in its absolute-convergence half-plane determines the unordered generator-norm multiset. That exact injectivity is not uniformly stable when the generator scale escapes to infinity.

Let

\[
\mathcal P=\{p_1<p_2<\cdots\}
\]

be the rational primes. For an odd prime `p=p_n`, define the matched generalized-prime system

\[
\mathcal Q_p
=\{p_1,\ldots,p_{n-1},p+1,p_{n+1},\ldots\}.
\tag{1}
\]

Because `p+1<p_{n+1}` for every odd prime, this is still an increasing locally finite norm sequence. It differs from the rational-prime system by exactly one unit at one generator. Write

\[
P_{\mathcal Q}(s)=\sum_{q\in\mathcal Q}q^{-s},
\qquad
Z_{\mathcal Q}(s)=\prod_{q\in\mathcal Q}(1-q^{-s})^{-1},
\tag{2}
\]

in `Re(s)>1`, and use the analytic logarithm normalized by positive real values there.

Fix `sigma>1`. For a vertical bandwidth `0\le T\le\infty`, define the boundary observation metrics

\[
d^P_{\sigma,T}(\mathcal P,\mathcal Q_p)
=
\sup_{|t|\le T}
\left|
P_{\mathcal Q_p}(\sigma+it)-P_{\mathcal P}(\sigma+it)
\right|,
\tag{3}
\]

and

\[
d^Z_{\sigma,T}(\mathcal P,\mathcal Q_p)
=
\sup_{|t|\le T}
\left|
\log Z_{\mathcal Q_p}(\sigma+it)-\log\zeta(\sigma+it)
\right|.
\tag{4}
\]

Let

\[
\delta_p=\log\frac{p+1}{p}=\log(1+1/p),
\qquad
r_p=e^{-\sigma\delta_p}=\left(\frac p{p+1}\right)^\sigma.
\tag{5}
\]

Then the single-generator prime-sum discrepancy has the exact bandwidth profile

\[
\boxed{
 d^P_{\sigma,T}
 =p^{-\sigma}
 \left[
 (1-r_p)^2
 +4r_p\sin^2\!\left(\frac{\min\{T\delta_p,\pi\}}2\right)
 \right]^{1/2}.
}
\tag{6}
\]

The Euler-product logarithm differs from this first-order profile only by the higher prime-power tail:

\[
\boxed{
\left|d^Z_{\sigma,T}-d^P_{\sigma,T}\right|
\le
\frac{p^{-2\sigma}}{1-p^{-\sigma}}
+
\frac{(p+1)^{-2\sigma}}{1-(p+1)^{-\sigma}}.
}
\tag{7}
\]

Consequently:

1. for every fixed finite `T`,
   \[
   \boxed{
   d^Z_{\sigma,T}
   =\sqrt{\sigma^2+T^2}\;p^{-(\sigma+1)}(1+o(1));
   }
   \tag{8}
   \]
2. with the full vertical line,
   \[
   \boxed{
   d^Z_{\sigma,\infty}
   =2p^{-\sigma}(1+o(1));
   }
   \tag{9}
   \]
3. in the unweighted generator-norm bottleneck metric the source systems stay a fixed distance apart,
   \[
   d_{\rm abs}(\mathcal P,\mathcal Q_p)=1,
   \tag{10}
   \]
   while `(9)` tends to zero. Therefore the exact inverse from Euler-product boundary data to generator norms is **not uniformly continuous** on this escaping-scale family, even when every vertical frequency is retained;
4. in the logarithmic generator metric,
   \[
   d_{\log}(\mathcal P,\mathcal Q_p)=\delta_p\sim p^{-1}.
   \tag{11}
   \]
   Hence no uniform inverse Hölder estimate
   \[
   d_{\log}\le C(d^Z_{\sigma,T})^\gamma
   \tag{12}
   \]
   can hold along these controls for `gamma>1/(sigma+1)` at fixed finite bandwidth, while with full vertical bandwidth no such estimate can hold for `gamma>1/sigma`;
5. vertical frequency and Laplace amplitude are separate fidelity resources. If `T_p=o(p)`, then the unit generator displacement remains in the small-phase regime and
   \[
   d^Z_{\sigma,T_p}
   =p^{-\sigma}\delta_p\sqrt{\sigma^2+T_p^2}\,(1+o(1)).
   \tag{13}
   \]
   To make the phase term order one requires `T_p` of order `p`, because `delta_p\sim1/p`. Even then the best discrepancy remains only order `p^{-sigma}` because the right-half-plane Laplace weight has already attenuated that generator.

Thus exact Euler-product fidelity has a concrete two-factor conditioning barrier:

\[
\boxed{
\text{generator at scale }p
\quad\Longrightarrow\quad
\begin{cases}
\text{amplitude }\asymp p^{-\sigma},\\
\text{frequency needed for unit-shift phase resolution }\asymp p.
\end{cases}
}
\tag{14}
\]

This is a genuinely arithmetic matched-control instance of the distinction developed in AF-168--AF-179: an exact representation can preserve the object set-theoretically while its inverse loses every scale-uniform modulus in a natural source geometry.

## Derivation

### The matched control changes one generator by exactly one unit

For odd prime `p=p_n`, the next prime satisfies `p_{n+1}\ge p+2`, so

\[
p<p+1<p_{n+1}.
\tag{15}
\]

Thus replacing `p` by `p+1` preserves the monotone index order. Under monotone bottleneck matching, every other generator matches itself and the changed generator moves by exactly one:

\[
d_{\rm abs}=1.
\tag{16}
\]

After taking logarithms the same matching gives

\[
d_{\log}
=\log(p+1)-\log p
=\delta_p
=\frac1p+O(p^{-2}).
\tag{17}
\]

The modified system remains in the same absolute-convergence class as the rational primes because only one Euler factor has changed.

### Exact finite-bandwidth profile for the prime sum

Put

\[
s=\sigma+it,
\qquad
q=p+1.
\]

The two prime sums differ only in one term:

\[
P_{\mathcal Q_p}(s)-P_{\mathcal P}(s)
=q^{-s}-p^{-s}.
\tag{18}
\]

Factoring out `p^{-s}` gives

\[
q^{-s}-p^{-s}
=p^{-s}\left(r_p e^{-it\delta_p}-1\right),
\tag{19}
\]

and hence

\[
|q^{-s}-p^{-s}|^2
=p^{-2\sigma}
\left[
(1-r_p)^2+4r_p\sin^2(t\delta_p/2)
\right].
\tag{20}
\]

On `|t|\le T`, the sine term increases up to its first maximum at `|t|\delta_p=\pi`; after that value the full maximum `1` is already available. Taking the supremum proves `(6)`.

This formula cleanly separates radial attenuation from phase resolution. The factor `p^{-sigma}` is present before frequency is considered. The only role of the vertical variable is to rotate the two nearby exponentials relative to one another through phase difference `t delta_p`.

### Euler-product logarithms have the same leading profile

Absolute convergence gives

\[
\log Z_{\mathcal Q_p}(s)-\log\zeta(s)
=\log(1-p^{-s})-\log(1-q^{-s}).
\tag{21}
\]

Expanding both logarithms,

\[
\log(1-p^{-s})-\log(1-q^{-s})
=-(p^{-s}-q^{-s})
-
\sum_{m\ge2}\frac{p^{-ms}-q^{-ms}}m.
\tag{22}
\]

For `Re(s)=sigma`, the tail is bounded uniformly in `t` by

\[
\begin{aligned}
\left|
\sum_{m\ge2}\frac{p^{-ms}-q^{-ms}}m
\right|
&\le
\sum_{m\ge2}\frac{p^{-m\sigma}+q^{-m\sigma}}m\\
&\le
\frac{p^{-2\sigma}}{1-p^{-\sigma}}
+
\frac{q^{-2\sigma}}{1-q^{-\sigma}}.
\end{aligned}
\tag{23}
\]

For two functions `f,g`, the elementary inequality

\[
\left|\sup|f|-\sup|g|\right|
\le\sup|f-g|
\tag{24}
\]

then turns `(23)` into `(7)`.

### Fixed bandwidth loses an additional factor `1/p`

For fixed `T`, equations `(5)` give

\[
\delta_p=p^{-1}+O(p^{-2}),
\qquad
1-r_p=\sigma\delta_p+O(\delta_p^2).
\tag{25}
\]

Also `T delta_p ->0`, so

\[
4r_p\sin^2(T\delta_p/2)
=T^2\delta_p^2+O(\delta_p^3).
\tag{26}
\]

Substituting `(25)`--`(26)` into `(6)`,

\[
d^P_{\sigma,T}
=p^{-\sigma}\delta_p
\sqrt{\sigma^2+T^2}\,(1+o(1))
=
\sqrt{\sigma^2+T^2}\;p^{-(\sigma+1)}(1+o(1)).
\tag{27}
\]

Because `sigma>1`, the Euler-log remainder in `(7)` is `O(p^{-2sigma})=o(p^{-(sigma+1)})`. This proves `(8)`.

The same argument remains valid for `T_p=o(p)`, yielding `(13)` with the declared growing bandwidth.

### Full bandwidth recovers phase contrast but not amplitude

If `T=infinity`, choose

\[
t_p=\frac{\pi}{\delta_p}.
\tag{28}
\]

Then the two first-order terms are exactly opposite in phase, and `(6)` becomes

\[
d^P_{\sigma,\infty}
=p^{-\sigma}(1+r_p)
=p^{-\sigma}+(p+1)^{-\sigma}.
\tag{29}
\]

Since `r_p->1`, this is `2p^{-sigma}(1+o(1))`. The remainder `(7)` is lower order, proving `(9)`.

Equation `(28)` is also the exact frequency scale behind the phase-resolution statement:

\[
t_p
=\frac{\pi}{\log(1+1/p)}
=\pi p+O(1).
\tag{30}
\]

Thus unbounded vertical frequency repairs the extra derivative-scale loss seen at fixed bandwidth, but cannot undo the base factor `p^{-sigma}`.

### Uniform inverse moduli fail in two natural source geometries

In the absolute norm metric, `(16)` and `(9)` give

\[
d_{\rm abs}=1,
\qquad
d^Z_{\sigma,\infty}\to0.
\tag{31}
\]

If a uniform inverse modulus `omega(u)->0` existed with

\[
d_{\rm abs}\le\omega(d^Z_{\sigma,\infty}),
\tag{32}
\]

then `(31)` would imply `1\le0` in the limit. Hence no such modulus exists.

For logarithmic source geometry, suppose `(12)` held uniformly. With fixed `T`, equations `(8)` and `(17)` would force

\[
p^{-1+o(1)}
\lesssim
p^{-(\sigma+1)\gamma}.
\tag{33}
\]

This is impossible when `(sigma+1)gamma>1`. With full bandwidth, `(9)` instead gives the necessary condition `sigma gamma<=1`. This proves the two Hölder upper barriers stated above. These are **necessary bounds only**: the finding does not claim that the endpoint exponents `1/(sigma+1)` or `1/sigma` are globally attainable on a larger generalized-prime class.

## Exact controls

### Same output category, non-prime generator

The control changes `p` to the composite integer `p+1` while leaving every other generator untouched. It therefore changes the rational-prime norm system at exactly the information layer AF-017 studies, without changing the definition of the Euler-product destination.

Moreover,

\[
p\le p+1\le p_{n+1},
\tag{34}
\]

so it lies inside the interval-by-interval generalized-prime perturbation class used by Grosswald--Schnitzer. Their same-zero theorem is not needed for the present estimates; only the legitimacy of such matched generator systems is relevant here.

### Exact injectivity is not contradicted

For every fixed `p`, the analytic functions are different. In fact `(21)` is nonzero, and AF-017's Möbius/Dirichlet-sum argument recovers the changed norm exactly from exact function data.

The obstruction is therefore purely quantitative:

\[
\text{pointwise exact recovery}
\not\Rightarrow
\text{scale-uniform recovery}.
\tag{35}
\]

There is no same-output collision in this finding.

### Frequency-only repair is insufficient

The full line `t in R` is a deliberately generous control. It permits frequency `t_p~pi p`, enough to rotate the two nearby norm exponentials by `pi`. Yet `(9)` still tends to zero. Therefore the instability cannot be blamed only on truncating the vertical-frequency window.

Conversely, fixed bandwidth introduces a second loss because `t delta_p` remains small. The distinction between `(8)` and `(9)` is exactly the distinction between **phase resolution** and **Laplace amplitude attenuation**.

## Prior art and novelty assessment

No theorem-level novelty is claimed for the underlying analytic ingredients.

- Carl-Erik Fröberg, **“On the prime zeta function,”** *BIT Numerical Mathematics* 8 (1968), 187--202, is classical prior art for the prime Dirichlet sum, Euler-product logarithm, and Möbius inversion used in AF-017.
- Emil Grosswald and Franz J. Schnitzer, **“A class of modified ζ and L-functions,”** *Pacific Journal of Mathematics* 74(2) (1978), 357--362, DOI `10.2140/pjm.1978.74.357`, supply the classical generalized-prime interval controls `p_n<=q_n<=p_{n+1}` and show how much analytic zero data can survive such perturbations.
- Pierre Maréchal, Faouzi Triki, and Walter C. Simo Tao Lee, **“Regularization of the inverse Laplace transform by mollification,”** *Inverse Problems* 40(2) (2024), 025010, DOI `10.1088/1361-6420/ad1609`, gives modern inverse-problem context for the severe instability of Laplace inversion and derives global logarithmic stability estimates in a broader function-space setting.

The exact formulas `(6)`--`(13)` are elementary consequences of a one-generator Dirichlet/Laplace perturbation and the Euler logarithm expansion. The contribution here is the **Arithmetic Fidelity placement**: it supplies a source-matched rational-prime control showing exactly how scale and observation bandwidth enter the stability of the same Euler-product representation that AF-017 already proved to be set-theoretically faithful.

The prior-art search did not identify this specific prime-by-prime scale--bandwidth formula as a named result, but that is not treated as evidence of novelty. It is best regarded as an exact calibration extracted from classical Dirichlet/Laplace mathematics.

## Boundaries and failure modes

1. **The metric is part of the theorem.** Non-uniform continuity in `(31)` uses the unweighted absolute norm metric on generators. Reweighting a generator at scale `p` by `p^{-sigma}` can absorb the amplitude decay by construction. The logarithmic metric `(11)` gives a less severe but still explicit Hölder barrier instead of a fixed-distance failure.

2. **The observation is on `Re(s)=sigma>1`.** This is the honest absolute-convergence region. The argument does not transport the metric through analytic continuation to the critical strip. At `sigma=1` the full Euler product is on its convergence boundary and the stated estimates are not the declared destination.

3. **The logarithm is essential only for additive comparison.** In `Re(s)>=sigma>1`, Euler products are nonzero and uniformly bounded away from zero and infinity in the elementary absolute-product sense, so the normalized logarithm is a natural local multiplicative metric. The finding does not claim that every other norm on raw function values has identical constants.

4. **Only one generator is perturbed.** This is a strength for falsification: no accumulation of many small changes is needed to destroy uniform inverse stability. It is not a classification of arbitrary many-generator perturbations.

5. **Bandwidth thresholds concern this unit-shift control.** A different source displacement `q/p` has phase scale `1/|log(q/p)|`. The linear `T~p` threshold comes specifically from `q=p+1`, where `log(q/p)~1/p`.

6. **No RH conclusion follows.** This finding neither locates zeros nor proves that an RH mechanism must use a particular vertical bandwidth. It constrains what can be inferred stably from right-half-plane Euler-product data about high-scale rational-prime norms.

## Consequences for Arithmetic Fidelity

AF-017 established a qualitative boundary: the full Euler-product function retains the norm multiset while the zero divisor need not. AF-180 shows that even the faithful side of that boundary has a second, quantitative hierarchy.

For a generator at scale `p`, three questions are distinct:

\[
\begin{array}{rcl}
\text{exact fidelity} &:& \text{does the full analytic function determine the norm?}\\
\text{amplitude fidelity} &:& \text{how large is the analytic change caused by moving it?}\\
\text{resolution fidelity} &:& \text{what vertical frequency is needed to resolve the displacement phase?}
\end{array}
\tag{36}
\]

The present control answers all three in one concrete arithmetic setting: exact fidelity is yes; amplitude decays like `p^{-sigma}` even with unlimited frequency; and resolving a unit displacement in phase requires frequency of order `p`.

This gives a practical audit rule for any proposed RH representation that starts from right-half-plane Euler/local-factor data and then compresses further. It is not enough to prove that prime norms are theoretically encoded. The proposal must state the **source metric, analytic normalization, vertical-frequency budget, and scale dependence of the inverse modulus**. Otherwise exact recoverability can coexist with asymptotically invisible unit changes in the rational-prime norm system.