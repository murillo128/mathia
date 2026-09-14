# MC-283 — Siegel–Walfisz shell universality forces super-polylogarithmic Christoffel conductor

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the localized Legendre-shell and empirical-Christoffel notation of `MC-252`, `MC-268`, and `MC-281`. Let

\[
\mathcal P_y=\{p\le y:p\text{ odd prime}\},
\qquad
\mathcal R_y=\{r:y<r\le2y,\ r\text{ prime}\}.
\]

For a finite coordinate set `U\subseteq\mathcal P_y`, put

\[
Q(U):=4\prod_{p\in U}p,
\qquad d:=|U|.
\tag{1}
\]

Fix `A>0`. Uniformly over all `U=U_y` satisfying

\[
Q(U)\le (\log y)^A,
\tag{2}
\]

and all sign vectors `\varepsilon=(\varepsilon_p)_{p\in U}\in\{\pm1\}^U`, define

\[
R_y(\varepsilon;U)
:=
\#\left\{
 r\in\mathcal R_y:
 r\equiv1\pmod4,
 \ \left(\frac pr\right)=\varepsilon_p\ \forall p\in U
\right\}.
\tag{3}
\]

Then the Siegel–Walfisz theorem gives the uniform asymptotic

\[
\boxed{
R_y(\varepsilon;U)
=
\left(1+o_A(1)\right)
\frac{\operatorname{Li}(2y)-\operatorname{Li}(y)}{2^{d+1}}.
}
\tag{4}
\]

In particular,

\[
R_y(\varepsilon;U)
\gg_A
\frac{y}{2^d\log y}
\gg_A
\frac{y}{(\log y)^{A+1}}.
\tag{5}
\]

Thus tight localization to the actual shell `(y,2y]` does **not** constrain any Legendre sign pattern carried by a lower-prime block of polylogarithmic product conductor.

More strongly, let `t=t_y` satisfy

\[
1\le t=o\!\left(\frac{y}{(\log y)^{A+1}}\right),
\tag{6}
\]

which includes the live blind-support scale

\[
t=\left(\frac1{\log2}+o(1)\right)\log\log y.
\tag{7}
\]

For every desired product-sign vector `\eta\in\{\pm1\}^U`, there exists a set of `t` distinct shell primes `T\subset\mathcal R_y` such that

\[
\boxed{
\prod_{r\in T}\left(\frac pr\right)=\eta_p
\qquad(p\in U).
}
\tag{8}
\]

Hence the projection of the actual fixed-weight arithmetic row image onto `U` is the **entire Boolean cube**:

\[
\boxed{
\left\{
\left(\prod_{r\in T}(p/r)\right)_{p\in U}:
T\in\binom{\mathcal R_y}{t}
\right\}
=
\{\pm1\}^U.
}
\tag{9}
\]

This has a direct consequence for the empirical Christoffel escape isolated in `MC-281`. Let

\[
p_a(x)=\sum_{S\in\mathcal B_m}a_Sx_S,
\qquad
\mathcal B_m=\{S\subseteq\mathcal P_y:|S|\le m\},
\tag{10}
\]

with endpoint normalization

\[
\sum_{S\in\mathcal B_m}a_S=p_a(1,1,\ldots)=1.
\tag{11}
\]

Define the effective lower-prime coordinate support

\[
U(a):=\bigcup_{a_S\ne0}S
\tag{12}
\]

and its product conductor

\[
Q(a):=4\prod_{p\in U(a)}p.
\tag{13}
\]

If `Q(a)\le(\log y)^A`, then `(4)` supplies

\[
R_+(a)
:=R_y((+1)_{p\in U(a)};U(a))
\gg_A\frac{y}{(\log y)^{A+1}}.
\tag{14}
\]

Every `t`-subset of these all-positive shell primes has

\[
\prod_{r\in T}\left(\frac pr\right)=1
\qquad(p\in U(a)),
\tag{15}
\]

so the corresponding row evaluates exactly at the virtual endpoint and therefore

\[
p_a(x(T))=1.
\tag{16}
\]

Consequently the empirical energy from `MC-281` obeys the exact lower bound

\[
\boxed{
\sum_{T\in\binom{\mathcal R_y}{t}}
|p_a(x(T))|^2
\ge
\binom{R_+(a)}{t}.
}
\tag{17}
\]

At the live scale `(7)` the right side is much larger than one. Therefore no endpoint-normalized coefficient vector whose effective coordinate conductor is bounded by any fixed power of `\log y` can realize the desired Christoffel certificate `<1`.

Equivalently, if along a sequence `y\to\infty` an admissible family `a_y` satisfies

\[
\sum_T|p_{a_y}(x(T))|^2<1,
\tag{18}
\]

then for every fixed `A>0`, eventually

\[
\boxed{
Q(a_y)>(\log y)^A.
}
\tag{19}
\]

Thus any successful image-adaptive Christoffel separator at the current frontier must have **super-polylogarithmic effective lower-prime conductor**. Shell localization alone begins to have a chance to create the missing endpoint leverage only after the certificate couples coordinates beyond the whole Siegel–Walfisz conductor regime.

This does not exclude such high-conductor certificates, does not show that the full shell row image is a full Boolean cube, and gives no bound for `M(x)` by itself.

## 1. Prescribed signs become residue classes modulo the product conductor

Fix `U` and `\varepsilon`. Because every target prime in `(3)` is required to satisfy `r\equiv1\pmod4`, quadratic reciprocity gives for every odd `p\in U`

\[
\left(\frac pr\right)=\left(\frac rp\right).
\tag{20}
\]

For each `p`, exactly `(p-1)/2` nonzero residue classes modulo `p` have prescribed Legendre sign `\varepsilon_p`. The Chinese remainder theorem therefore converts `(3)` into a union of

\[
J(U)
=
\prod_{p\in U}\frac{p-1}{2}
=
\frac{\varphi(Q(U))}{2^{d+1}}
\tag{21}
\]

reduced residue classes modulo `Q(U)`. The factor `2` in the denominator beyond `2^d` comes from fixing the single class `1 mod 4` among the two reduced classes modulo `4`.

This is the same finite prescribed-Legendre mechanism audited in `MC-252`; the difference is that `(2)` keeps the CRT modulus inside a range where primes in every resulting class can be counted **inside the moving shell itself**.

## 2. Siegel–Walfisz survives summation over all prescribed classes

`MC-S15` records the standard prime-number theorem in arithmetic progressions and its Siegel–Walfisz uniform form. For every fixed `A,B>0`, uniformly for

\[
q\le(\log y)^A,
\qquad (a,q)=1,
\tag{22}
\]

one may write

\[
\pi(2y;q,a)-\pi(y;q,a)
=
\frac{\operatorname{Li}(2y)-\operatorname{Li}(y)}{\varphi(q)}
+O_{A,B}\!\left(\frac{y}{(\log y)^B}\right).
\tag{23}
\]

The constants are ineffective in the usual Siegel–Walfisz sense; only asymptotic existence is used here.

Apply `(23)` to each of the `J(U)` classes from `(21)`. The total main term is exactly

\[
J(U)\frac{\operatorname{Li}(2y)-\operatorname{Li}(y)}{\varphi(Q(U))}
=
\frac{\operatorname{Li}(2y)-\operatorname{Li}(y)}{2^{d+1}}.
\tag{24}
\]

The aggregate error is at most

\[
J(U)O_{A,B}\!\left(\frac{y}{(\log y)^B}\right)
=O_{A,B}\!\left(\frac{y(\log y)^A}{(\log y)^B}\right),
\tag{25}
\]

because `J(U)\le\varphi(Q(U))\le Q(U)\le(\log y)^A`.

Meanwhile

\[
2^d\le\prod_{p\in U}p\le(\log y)^A,
\tag{26}
\]

so the main term in `(24)` is at least of order `y/(\log y)^{A+1}`. Choosing `B>2A+2` makes `(25)` little-oh of that lower scale, uniformly over all allowed `U` and all prescribed sign vectors. This proves `(4)` and `(5)`.

The argument is deliberately confined to fixed-power polylogarithmic conductor. `MC-067` shows that some **single-character positive-feedback** obstructions can be pushed much farther, into a Page/Siegel stretched-exponential regime. That extension does not apply automatically here: `(4)` requires simultaneous lower bounds for every prescribed residue-pattern family, whereas exceptional-character terms can create severe bias once one leaves the Siegel–Walfisz uniform regime. No stretched-exponential universality is claimed.

## 3. Every projected fixed-weight sign vector occurs

Let `\eta\in\{\pm1\}^U`. By `(5)`, for large `y` there are many shell primes with individual sign pattern `\eta`, and many with the all-positive pattern `\mathbf1`.

If `\eta\ne\mathbf1`, choose one shell prime `r_0` with pattern `\eta` and choose `t-1` distinct shell primes with pattern `\mathbf1`. Their classes are disjoint, so all selected primes are distinct. If `\eta=\mathbf1`, choose any `t` distinct primes from the all-positive class family. Condition `(6)` and `(5)` guarantee enough choices in either case.

For the resulting set `T`, multiplicativity of the Legendre symbol gives

\[
\prod_{r\in T}\left(\frac pr\right)
=
\eta_p
\qquad(p\in U),
\]

which proves `(8)` and `(9)`.

This is stronger than the separated-prime universality of `MC-252` in one precise direction: the target primes now remain in the exact Mathia shell `(y,2y]`. It is weaker in another equally important direction: the lower coordinate family is restricted by `(2)`. The result therefore identifies a quantitative boundary rather than eliminating localization altogether.

## 4. Christoffel leverage cannot come from a polylogarithmic coordinate block

For a target set `T`, write as in `MC-281`

\[
\sigma_p(T):=\prod_{r\in T}\left(\frac pr\right).
\tag{27}
\]

Then the matrix entry associated with a source support `S` is

\[
A_{T,S}
=
\prod_{p\in S}\sigma_p(T).
\tag{28}
\]

If `a_S\ne0`, every coordinate on which `(28)` depends belongs to `U(a)`. Hence whenever `(15)` holds,

\[
A_{T,S}=1
\qquad\text{for every }S\text{ with }a_S\ne0.
\tag{29}
\]

The endpoint normalization `(11)` then gives `(16)` exactly. Summing the unit contribution over all `t`-subsets of the `R_+(a)` all-positive shell primes proves `(17)`.

This is not a generic operator-norm obstruction like `MC-270`. It is directional and arithmetic-image specific: it shows that the virtual endpoint is not merely close to the projected row image on a polylogarithmic-conductor coordinate block; it is realized by a very large collection of actual fixed-weight shell rows on that entire block.

Accordingly, a low-energy separator cannot be repaired by changing coefficients while keeping the same small effective coordinate conductor. It must import at least one genuinely high-conductor lower-prime interaction, or otherwise use a coefficient support whose union product escapes every fixed polylogarithmic scale.

The conclusion concerns the **effective coordinate support of the chosen separator**, not the formal ambient feature set `\mathcal B_m`. Even when `m=t+1`, a sparse polynomial could in principle touch a large lower prime and immediately have super-polylogarithmic `Q(a)`. The theorem does not bound such a certificate.

## 5. Prior art and novelty boundary

No novelty is claimed for any analytic-number-theory ingredient. Prescribing finitely many Legendre symbols by CRT and quadratic reciprocity is classical and was already audited in `MC-252`, including Hanson–Vaughan–Zhang's work on the quantitative problem of least realizers of prescribed Legendre vectors. `MC-252` used Dirichlet's theorem only after allowing the realizing primes to move arbitrarily far away.

The new input relative to that finding is the classical Siegel–Walfisz uniform prime-number theorem retained in `MC-S15`. Once the combined CRT modulus is at most a fixed power of `\log y`, that theorem places every prescribed sign family with its expected density inside `(y,2y]`. Equations `(21)`–`(26)` are the direct specialization and error audit.

A targeted novelty audit against prescribed-Legendre-symbol constructions, primes in arithmetic progressions, Siegel–Walfisz, and the Christoffel/leverage literature retained in `MC-268` and `MC-281` gives no basis for claiming a new standalone theorem in any of those classical subjects. The durable Mathia-specific delta is their combination at the active frontier: **the shell-localized row image is already fully universal on every coordinate block whose product conductor is polylogarithmic, so the empirical-Christoffel route can only gain leverage through super-polylogarithmic coordinate coupling.**

## 6. Boundaries and falsification checks

- **Full-coordinate check.** Nothing here says that the shell image on all primes `p\le y` is the full cube. For that family, the product modulus is exponential in `y`, far outside `(2)`.
- **Conductor-not-cardinality check.** The relevant quantity is `Q(U)=4\prod_{p\in U}p`, not merely `|U|`. A single sufficiently large lower prime already escapes the theorem even when `|U|=1`.
- **Fixed-weight check.** Equation `(9)` is genuinely about `t`-subsets of shell primes, not individual primes only. The construction uses one desired-pattern prime plus `t-1` all-positive primes.
- **Distinctness check.** Condition `(5)` supplies far more than `t` primes in every required pattern family at `(7)`, so the fixed-weight construction never reuses a prime.
- **Reciprocity-sign check.** The auxiliary restriction `r\equiv1 mod4` is essential to turn `(p/r)` into `(r/p)` with no reciprocity sign. It costs exactly the extra factor `2` in `(21)`.
- **Uniform-error check.** The Siegel–Walfisz error must be summed over all `J(U)` CRT classes. Equation `(25)` performs that summation explicitly; choosing `B>2A+2` leaves it negligible even when `Q(U)` reaches the top of `(2)`.
- **Exceptional-zero check.** No effective uniform constant is claimed. The ordinary Siegel–Walfisz theorem is enough in the polylogarithmic range; the larger Page range from `MC-067` is not imported into this simultaneous-pattern statement.
- **Christoffel-support check.** Equation `(19)` is a necessary condition only for certificates with empirical energy below one. It does not say that super-polylogarithmic support is sufficient or that `MC-281` can be closed positively there.
- **RH-circularity check.** The proof uses only classical unconditional distribution of primes in arithmetic progressions in the Siegel–Walfisz range. No zero-free region for the Riemann zeta function near `1/2`, no continuation of `1/\zeta(s)`, and no Mertens estimate enters.

## Consequence for the active frontier

`MC-252` showed that arbitrary Legendre-code geometry can be realized when shell localization is discarded, leaving localization as a plausible source of extra rigidity. `MC-281` then isolated the exact directional object needed for progress: orientation of the blind endpoint against the actual arithmetic row span, or equivalently an empirical Christoffel/leverage gain. `MC-282` showed that generic separated-prime arithmetic realizability does not force that gain.

The present result closes the most immediate remaining loophole at small conductor. **The exact shell `(y,2y]` still realizes every Boolean sign pattern on every lower-prime coordinate block whose CRT conductor is only polylogarithmic.** Thus no bounded- or polylog-conductor local view of the arithmetic image can supply the missing endpoint leverage.

The positive frontier is correspondingly narrower: a successful `MC-281` certificate must exploit genuinely global lower-prime coupling whose effective product conductor escapes every fixed power of `\log y`, and must then prove that this large-conductor coupling is sufficiently well-conditioned to drive empirical Christoffel energy below one. The theorem does not solve that problem; it identifies where it can first begin.