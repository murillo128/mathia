# WI-048 — the full structured local singular-series main has subpolynomial prefix discrepancy

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding strengthens the deterministic-local conclusion of `WI-046`: the finite prime cutoff is not essential. On the asymptotically dominant coprime prime-power base family, the **full infinite Euler product** carried by the two structured twin shifts admits a positive divisor expansion whose prefix discrepancy from the exact Yang `E2(b1,b2)` mean is

\[
\boxed{
 \sum_{1\le k\le K}
 \bigl(F_{b_1,b_2}(k)-E_2(b_1,b_2)\bigr)
 \ll_{\eta} K^{\eta}
 \qquad(\forall\eta>0),
}
\tag{1}
\]

uniformly in the coprime prime-power bases `b1,b2`. By Abel summation the same gives `K^eta` control against every deterministic bounded-variation shift weight. Hence **no growing local Euler conductor is needed** to preserve the `S1/S2/S3` singular-series centering: after the deterministic local main has been extracted, the complete `p`-adic product is already equidistributed strongly enough on the natural Yang `k`-intervals.

This does **not** certify the Yang--Yang one-sided fourth-moment theorem, change Mathia's current unconditional simple-critical proportion, or control the prime-dependent welding residual. The remaining analytic problem is still the locally centered prime fluctuation / coupled dispersion interface isolated by `WI-037`, `WI-042`--`WI-045`, together with the final remainder ledger. The new conclusion is narrower but useful: the unresolved welding obstruction cannot be blamed on truncating the singular series at a fixed finite prime cutoff.

## 1. Exact full local object

The pinned public source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

For the equal-lock swap, `WI-045` identifies the deterministic local main produced by the two structured pair shifts as the product of ordinary Hardy--Littlewood two-point factors

\[
 F_{b_1,b_2}(k)
 :=\prod_p \tau_p(b_1k)\tau_p(b_2k),
 \qquad k\ne0,
\tag{2}
\]

where

\[
 \tau_p(h)=
 \begin{cases}
 A_p:=\dfrac p{p-1},&p\mid h,\\[2mm]
 B_p:=\dfrac{p(p-2)}{(p-1)^2},&p\nmid h.
 \end{cases}
\tag{3}
\]

The `k=0` diagonal is booked separately in the source and is deliberately excluded here.

Assume `(b1,b2)=1` and that `b1,b2` are prime powers, as on the Yang base family. For odd primes there are two cases.

If `p` divides neither base, then

\[
 \tau_p(b_1k)\tau_p(b_2k)
 =B_p^2\bigl(1+a_p1_{p\mid k}\bigr),
\qquad
 a_p=\frac{2p-3}{(p-2)^2}.
\tag{4}
\]

If `p` divides exactly one base, then

\[
 \tau_p(b_1k)\tau_p(b_2k)
 =A_pB_p\bigl(1+c_p1_{p\mid k}\bigr),
\qquad
 c_p=\frac1{p-2}.
\tag{5}
\]

At `p=2`, coprimality gives in every case

\[
 \boxed{
 \tau_2(b_1k)\tau_2(b_2k)=4\,1_{2\mid k}.
 }
\tag{6}
\]

These are the same local identities used in `WI-045`--`WI-046`, now retained for all primes rather than truncated at `p<=P`.

## 2. A convergent base times a positive divisor sum

For every odd prime define

\[
 C_p=
 \begin{cases}
 B_p^2,&p\nmid b_1b_2,\\
 A_pB_p,&p\mid b_1b_2,
 \end{cases}
\qquad
 \alpha_p=
 \begin{cases}
 a_p,&p\nmid b_1b_2,\\
 c_p,&p\mid b_1b_2.
 \end{cases}
\tag{7}
\]

and put

\[
 C(b_1,b_2):=\prod_{p\ge3}C_p,
 \qquad
 \alpha_d:=\prod_{p\mid d}\alpha_p
\tag{8}
\]

for odd squarefree `d`.

The product defining `C` converges to a positive finite number. At a generic prime,

\[
 B_p^2=
 \left(1-\frac1{(p-1)^2}\right)^2
 =1+O(p^{-2}),
\tag{9}
\]

and only the at most two odd underlying primes of the two prime-power bases can replace `B_p^2` by `A_pB_p`. Moreover

\[
 \frac{A_pB_p}{B_p^2}=\frac{p-1}{p-2}\le2,
\tag{10}
\]

so `C(b1,b2)` is bounded uniformly over this coprime prime-power family by a fixed multiple of the generic convergent product.

Expanding the positive factors in (4)--(6) gives, for every nonzero integer `k`, the **full exact divisor expansion**

\[
\boxed{
 F_{b_1,b_2}(k)
 =4C(b_1,b_2)1_{2\mid k}
 \sum_{\substack{d\mid k\\ d\ {m odd\ squarefree}}}\alpha_d.
}
\tag{11}
\]

There is no cutoff and no CRT-period completion in (11).

## 3. The exact mean is the Yang `E2` Euler product

Because

\[
 \alpha_p\ll\frac1p,
\tag{12}
\]

the series

\[
 \sum_{d\ {m odd\ squarefree}}\frac{\alpha_d}{d}
 =\prod_{p\ge3}\left(1+\frac{\alpha_p}{p}\right)
\tag{13}
\]

converges absolutely. Therefore the natural mean of (11) is

\[
 \mathcal E(b_1,b_2)
 :=2C(b_1,b_2)
 \prod_{p\ge3}\left(1+\frac{\alpha_p}{p}\right).
\tag{14}
\]

Prime by prime this is exactly the source's second local moment `E2(b1,b2)`. At a generic odd prime,

\[
 B_p^2\left(1+\frac{a_p}{p}\right)
 =\frac{p(p^2-3p+3)}{(p-1)^3}
 =1+\frac1{(p-1)^3},
\tag{15}
\]

while at an odd coefficient prime,

\[
 A_pB_p\left(1+\frac{c_p}{p}\right)
 =\frac p{p-1}.
\tag{16}
\]

The parity average of (6) contributes `2`, which is the same `p=2` factor in either local case. Hence

\[
\boxed{
 \mathcal E(b_1,b_2)=E_2(b_1,b_2).
}
\tag{17}
\]

This is the infinite-product completion of the finite CRT collision identity proved in `WI-045`.

## 4. Exact prefix formula

For `K>=2`, Tonelli's theorem applies to the nonnegative divisor expansion, and

\[
\begin{aligned}
 \sum_{1\le k\le K}F_{b_1,b_2}(k)
 &=4C\sum_d\alpha_d
 \left\lfloor\frac{K}{2d}\right\rfloor.
\end{aligned}
\tag{18}
\]

Subtracting `K E2` using (14) gives the exact identity

\[
\begin{aligned}
 \sum_{k\le K}(F(k)-E_2)
 =4C\Bigg[&
 \sum_{d\le K/2}\alpha_d
 \left(
 \left\lfloor\frac K{2d}\right\rfloor-\frac K{2d}
 \right)\\
 &-\frac K2\sum_{d>K/2}\frac{\alpha_d}{d}
 \Bigg].
\end{aligned}
\tag{19}
\]

Thus the whole infinite Euler problem has reduced to two positive elementary divisor tails.

## 5. The short-divisor error is only logarithmic

At a coefficient prime,

\[
 c_p=\frac1{p-2}
 <\frac{2p-3}{(p-2)^2}=a_p.
\tag{20}
\]

Therefore

\[
 \sum_{d\le K/2}\alpha_d
 \le
 \prod_{3\le p\le K}(1+a_p)
 =\prod_{3\le p\le K}
 \left(\frac{p-1}{p-2}\right)^2.
\tag{21}
\]

The ratio

\[
 \frac{(p-1)/(p-2)}{p/(p-1)}
 =\frac{(p-1)^2}{p(p-2)}
 =1+\frac1{p(p-2)}
\tag{22}
\]

has an absolutely convergent product. Mertens' product theorem therefore gives

\[
\boxed{
 \sum_{d\le K/2}\alpha_d\ll(\log K)^2.
}
\tag{23}
\]

The bound is uniform in `b1,b2` on the coprime prime-power family.

## 6. The infinite Euler tail is subpolynomial

Fix any `0<eta<1`. Since `alpha_p<<1/p`,

\[
 \sum_d\frac{\alpha_d}{d^\eta}
 =\prod_{p\ge3}
 \left(1+\frac{\alpha_p}{p^\eta}\right)
 <\infty,
\tag{24}
\]

uniformly in the bases: coefficient-prime values are smaller than their generic counterparts.

For `d>K/2`,

\[
 \frac1d
 \le
 \left(\frac2K\right)^{1-\eta}\frac1{d^\eta}.
\tag{25}
\]

Hence

\[
 \boxed{
 \frac K2\sum_{d>K/2}\frac{\alpha_d}{d}
 \ll_\eta K^\eta.
}
\tag{26}
\]

Combining (19), (23), and (26), and absorbing `(log K)^2` into `K^eta`, proves (1):

\[
\boxed{
 \sum_{1\le k\le K}
 (F_{b_1,b_2}(k)-E_2(b_1,b_2))
 \ll_\eta K^\eta
}
\tag{27}
\]

for every fixed `eta>0`, uniformly over the dominant coprime prime-power base family.

Because `F(-k)=F(k)`, the same estimate holds for prefixes on either sign. Differences of prefixes give `O_eta(K^eta)` discrepancy on every subinterval contained in `[-K,K]`, after the source's separate `k=0` diagonal is removed.

## 7. Bounded-variation weights need no local cutoff

Let `I` be one such shift interval and let `w_k` be a deterministic real weight on it. Write

\[
 A(t)=\sum_{k\le t}(F(k)-E_2)
\tag{28}
\]

with the appropriate one-sided origin. Equation (27) gives `|A(t)|<<_eta K^eta` throughout `I`. Discrete Abel summation yields

\[
\boxed{
 \left|
 \sum_{k\in I}w_k(F(k)-E_2)
 \right|
 \ll_\eta
 K^\eta
 \left(
 \|w\|_\infty+\operatorname{TV}(w)
 \right).
}
\tag{29}
\]

This is the full-Euler analogue of `WI-046` equation (21), but there is now **no prime cutoff `P` and no tail term to send to zero separately**.

For the deterministic overlap weights isolated in `WI-046`,

\[
 \|w\|_\infty+TV(w)=O(M),
 \qquad
 \sum_k w_k\asymp MK,
\tag{30}
\]

so the relative full-local bias is

\[
\boxed{
 O_\eta(K^{-1+\eta}).
}
\tag{31}
\]

On the interior Yang continuum, `K\asymp X/(b_1b_2)` is a positive power of `X`, so (31) is power-saving after choosing `eta<1`. Cells for which `K` is at most a fixed power of `log X` occupy only the `o(1)` boundary strip already proved in `WI-046`; on the complementary cells even a polylogarithmically growing `K` makes (31) tend to zero.

Thus the complete deterministic local singular-series product transports through the source's bounded-variation `k`-geometry with `o(1)` normalized bias on all but `o(1)` source mass.

## 8. What this closes and what remains open

The durable conclusion is

\[
\boxed{
 \text{full local }p\text{-adic main}
 +\text{Yang }k\text{-interval/BV geometry}
 \Longrightarrow
 \text{negligible deterministic residue bias}.
}
\tag{32}
\]

This removes a specific residual ambiguity in `WI-045`--`WI-046`: one does **not** need to freeze the local Euler product at `P=40`, or at any `P=(log X)^B`, to keep its residue structure under control. The full local product itself has sufficient interval cancellation.

It does **not** imply

\[
 \text{actual locally centered }(S_1-2S_2+S_3)=o(1).
\tag{33}
\]

The following remain outside the result:

1. the prime-dependent welding coefficient before the deterministic pair mains have been extracted;
2. any genuinely joint covariance of the locally centered prime-pair residuals that survives the exact `S1-2S2+S3` recombination;
3. the source's missing theorem-level shift-first consumer and the Cauchy normalization issue in `WI-042`;
4. large-coefficient major/minor-arc uniformity outside the interfaces already closed by `WI-038`;
5. diagonal/Poisson terms and the final finite `R(1)` ledger;
6. the `o(1)` noncoprime same-underlying-prime base family, which must still be charged in the exact source normalization as in `WI-045`.

The finding therefore sharpens the research target rather than proving the candidate: **whatever prevents the one-sided fourth-moment route from closing must now live in the analytic prime residual / coupled dispersion layer, not in an unbounded deterministic local singular-series conductor.**

## 9. Prior-art and novelty audit

Averaging Hardy--Littlewood singular series is classical. Gallagher's 1976 short-interval argument established the foundational mean-one law for fixed prime-tuple singular series, and Pintz later gave a simplified stronger treatment. Sun-kai Leung's 2025 `Pseudorandomness of primes at large scales`, Proposition 3.1, gives a multidimensional lattice version and explicitly uses an absolutely convergent divisor expansion of the singular series. These sources establish the general arithmetic mechanism behind (11)--(27).

Primary anchors:

- P. X. Gallagher, **On the distribution of primes in short intervals**, *Mathematika* 23 (1976), 4--9, DOI `10.1112/S0025579300016442`;
- János Pintz, **On the singular series in the prime k-tuple conjecture**, arXiv:1004.1084;
- Sun-kai Leung, **Pseudorandomness of primes at large scales**, *Quarterly Journal of Mathematics* 76:1 (2025), 251--263, DOI `10.1093/qmath/haae069`, especially Proposition 3.1;
- the pinned Yang source above, plus `WI-045`--`WI-046` for the exact source-local factor matching.

No novelty is claimed for Euler products, divisor expansions, Mertens' product theorem, Rankin-type tail bounds, Abel summation, or average singular-series philosophy. A bounded exact-phrase and structural search did not locate this precise uniform `F_{b1,b2}(k)` prefix estimate written for the Yang welding product of two twin local factors, but absence of a located match is **not** a priority claim. The Mathia contribution is the source-specific audit deduction: combine the exact Yang collision factors from `WI-045` with the positive divisor expansion to remove `WI-046`'s finite-local-cutoff caveat completely.

## 10. Decisive verification / falsification gates

Narrow or retire this finding if any of the following fails.

1. Verify from `WI-045` and the pinned source that the deterministic `S1` structured local main on the coprime family is exactly (2), with `E2(b1,b2)` as its intended `k`-average.
2. Check the odd-prime identities (4)--(5) and the parity identity (6), including coefficient primes.
3. Expand (11) and verify that each fixed nonzero `k` has only finitely many divisor corrections; do not apply the formula at `k=0`.
4. Verify the local mean identities (15)--(17) against the source's `e2_const` table.
5. Reproduce (19) directly by counting multiples of `2d` and keep the mean-tail term with its sign.
6. In (24), check convergence prime by prime: `alpha_p/p^eta=O(p^{-1-eta})` for every fixed `eta>0`.
7. Do not use (29) for the raw prime-dependent welding coefficient. It applies only after the deterministic local main has been isolated and the remaining weight is genuinely deterministic/BV in the sense audited in `WI-046`.
8. Keep the noncoprime base family and the `k=0` diagonal outside the claimed uniform main until their existing separate `o(1)` / diagonal bookings are restored.

## 11. Consequence for `weil_inertia`

The Yang one-sided route now has a cleaner arithmetic fault line. `WI-045` proves exact local `S1/S2/S3` centering prime by prime, `WI-046` proves that finite local products survive nonuniform deterministic interval weights, and this finding upgrades that statement to the **complete Euler product with `O_eta(K^eta)` prefix discrepancy**.

Accordingly, extending the deterministic local cutoff or worrying about an enormous CRT period is no longer a productive route. The shortest unresolved path remains to reconstruct the fully centered shift-first prime residual and decide whether the exact source geometry reduces it to MRT-compatible marginal errors or leaves a genuinely coupled four-prime object. That analytic fork, not the local singular-series tail, is now the evidence-changing target.