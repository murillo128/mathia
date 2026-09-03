# MC-028 — The Huxley–Watt cutoff defect reconstructs the next Möbius block after auxiliary convolution

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/BOUNDARY`, `NO-NOVELTY-CLAIM`.

## Claim

The degree-two finite-cutoff boundary left open by `MC-026` is not an independently cheap signed carrier once the auxiliary Huxley–Watt factor is collapsed to the product variable. At equal cutoff `N`, define

\[
c_{2,N}(r)
:=
\sum_{\substack{mn=r\\m,n\le N}}
\mu(m)\mu(n),
\qquad
\mu_2:=\mu*\mu,
\tag{1}
\]

and the cutoff defect

\[
e_{2,N}(r):=c_{2,N}(r)-\mu_2(r).
\tag{2}
\]

`MC-026` already gives `e_{2,N}(r)=0` for `r\le N`. Now include the auxiliary factor `k` that appears in the Huxley–Watt quadratic identity and group by the total product `q=mnk`:

\[
d_N(q)
:=
\sum_{\substack{m,n\le N\\mn\mid q}}
\mu(m)\mu(n)
=
(c_{2,N}*1)(q).
\tag{3}
\]

Then, throughout the entire square-scale range,

\[
\boxed{
d_N(q)=
\begin{cases}
\mu(q),&q\le N,\\
-\mu(q),&N<q\le N^2.
\end{cases}}
\tag{4}
\]

Since

\[
(\mu_2*1)(q)=\mu(q),
\tag{5}
\]

equations (2)–(5) give the exact boundary-defect reflection

\[
\boxed{
(e_{2,N}*1)(q)
=
\begin{cases}
0,&q\le N,\\
-2\mu(q),&N<q\le N^2.
\end{cases}}
\tag{6}
\]

Thus the degree-two cutoff defect does contain information absent from the unrestricted convolution, but after the source-natural auxiliary convolution used by Huxley–Watt it reconstructs the full next Möbius block pointwise. In this product-collapsed channel, the boundary term has not become a weaker cancellation problem: it is an exact signed copy of the target block.

For the analytic specialization `g_t(n)=n^{-1-t}`, set

\[
F_X(t)=\sum_{n\le X}\frac{\mu(n)}{n^{1+t}}
\tag{7}
\]

and

\[
T_N(t)
:=
\sum_{\substack{m,n\le N\\mnk\le N^2}}
\frac{\mu(m)\mu(n)}{(mnk)^{1+t}}.
\tag{8}
\]

Grouping (8) by `q=mnk` and applying (4) yields

\[
\boxed{
T_N(t)=2F_N(t)-F_{N^2}(t).
}
\tag{9}
\]

Equation (9) is the coefficient-level content of the Huxley–Watt square-scale identity. It sharpens the current Mathia boundary: a proposed signed escape from `MC-026` or residual repair for `MC-027` cannot gain power merely by retaining the finite cutoff defect and then collapsing all factor coordinates into `q`. Any genuinely weaker mechanism must extract cancellation **before** that collapse, for example from individual factor cutoffs, unequal ranges, cross-degree coupling, or an unsplit analytic relation whose estimate is not a function only of the total product coefficient.

## 1. Interior coefficient is the classical Möbius convolution

For `q\le N`, every divisor of `q` is automatically at most `N`. Therefore the cutoff in (3) is inactive and

\[
\begin{aligned}
d_N(q)
&=\sum_{mnk=q}\mu(m)\mu(n)\\
&=(\mu*\mu*1)(q).
\end{aligned}
\tag{10}
\]

Because `\mu*1=\varepsilon`, the convolution identity reduces to

\[
\mu*\mu*1=\mu,
\tag{11}
\]

which proves the first case of (4). This is the same low-product interior phenomenon recorded for `c_{d,N}` in `MC-026`, now with the auxiliary `1`-factor retained.

## 2. The square annulus has the opposite Möbius coefficient

Huxley and Watt's equal-cutoff degree-two identity, specialized to a totally multiplicative `g`, can be written for `K\ge N` with `N>K^{1/2}-1` as

\[
M(g,K)
=
2M(g,N)
-
\sum_{\substack{m,n\le N\\mnk\le K}}
\mu(m)\mu(n)g(mnk),
\tag{12}
\]

where

\[
M(g,K)=\sum_{q\le K}\mu(q)g(q).
\tag{13}
\]

For every integer `q` with `N<q\le N^2`, condition (12) is valid at both terminal cutoffs `K=q` and `K=q-1`: indeed `\sqrt q\le N`, hence `N>\sqrt q-1`. Subtracting the two identities cancels the fixed term `2M(g,N)` and leaves exactly the new `q`-coefficient:

\[
\mu(q)g(q)=-g(q)d_N(q).
\tag{14}
\]

Taking the admissible choice `g\equiv1` proves

\[
d_N(q)=-\mu(q),
\qquad N<q\le N^2,
\tag{15}
\]

and therefore completes (4). No analytic continuation, asymptotic estimate, zero information, or probabilistic model is used.

Huxley and Watt explicitly note that differencing their finite identity gives a formula for `\mu(K)` itself and place the underlying special cases in the Vaughan/Linnik/Heath-Brown lineage. Equation (15) is therefore a classical coefficient mechanism, not a novelty claim.

## 3. Exact defect reflection

By definition,

\[
d_N=c_{2,N}*1.
\tag{16}
\]

The unrestricted degree-two coefficient satisfies

\[
\mu_2*1=\mu.
\tag{17}
\]

Subtracting (17) from (16) gives

\[
d_N-\mu=e_{2,N}*1.
\tag{18}
\]

For `q\le N`, both sides vanish by the interior identity. For `N<q\le N^2`, equations (15) and (18) give

\[
(e_{2,N}*1)(q)=-2\mu(q),
\tag{19}
\]

which proves (6).

This is more precise than the support statement in `MC-026`. There the defect `e_{2,N}` was identified as living only beyond the low-product interior and retained as a possible source of pre-compression signed information. Equation (19) shows what happens after one particularly natural subsequent operation: convolution with the auxiliary factor from the Huxley–Watt identity does not smooth the defect into an easier boundary remainder. It turns it into an exact reflection of the new Möbius block.

## 4. Analytic specialization is a reflection, not an independent residual estimate

For `s=1+t`, total multiplicativity gives

\[
g_t(m)g_t(n)g_t(k)=(mnk)^{-s}.
\]

Hence (8) can be grouped as

\[
T_N(t)=\sum_{q\le N^2}\frac{d_N(q)}{q^{1+t}}.
\tag{20}
\]

Using (4),

\[
\begin{aligned}
T_N(t)
&=\sum_{q\le N}\frac{\mu(q)}{q^{1+t}}
-
\sum_{N<q\le N^2}\frac{\mu(q)}{q^{1+t}}\\
&=2F_N(t)-F_{N^2}(t),
\end{aligned}
\tag{21}
\]

which proves (9) exactly for every `t` for which the finite sums are defined.

This identity does not invalidate the analytic-germ route of `MC-023`/`MC-027`. Those findings center and recombine the Huxley–Watt expression before estimating it, and `MC-027` specifically leaves open signed cancellation in the coupled residual. The present finding rules out a narrower move: **collapse the finite signed boundary to the total product coefficient first, then hope that the resulting boundary coefficient has an independently cheaper norm or partial-sum budget.** Once that collapse is performed, the square-annulus coefficient is already `-\mu(q)`.

## 5. Truncated Möbius convolution prior-art boundary

There is adjacent literature on truncated divisor convolutions. Let

\[
\mathcal M(r,N)
:=
\sum_{\substack{d\mid r\\d\le N}}\mu(d),
\tag{22}
\]

the object studied, in a different averaging problem, by Patrick Letendre. Reordering (3) gives

\[
d_N(q)
=
\sum_{\substack{m\mid q\\m\le N}}
\mu(m)\,\mathcal M(q/m,N).
\tag{23}
\]

Therefore the Huxley–Watt square annulus satisfies the pointwise correlated identity

\[
\boxed{
\sum_{\substack{m\mid q\\m\le N}}
\mu(m)\,\mathcal M(q/m,N)
=-\mu(q)
\qquad(N<q\le N^2).
}
\tag{24}
\]

Letendre proves nontrivial results about sizes and moments of truncated Möbius convolutions as the truncation parameter varies. Those results are genuine adjacent prior art, but (24) shows why marginal smallness of `\mathcal M` cannot by itself make this Huxley–Watt boundary cheap: the exact Möbius-weighted sampling relevant here reconstructs the target sign. A useful application of truncated-convolution estimates would have to control this specific correlated pairing, not only the isolated magnitude distribution of `\mathcal M(r,N)`.

## 6. Prior art and novelty assessment

The parent finite identity is due to M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`. Their paper explicitly observes that differencing the formula recovers `\mu(K)` and states that the relevant special cases are classical, with connections to Vaughan's identity, Linnik-type identities, Heath-Brown's identity, and Iwaniec–Kowalski equation (13.38). The reflection (4) is an exact specialization of that mechanism.

Patrick Letendre, *Truncated convolution of the Möbius function and multiplicative energy of an integer n*, Acta Arithmetica 195 (2020), 83–95, DOI `10.4064/aa190515-18-10`, arXiv `1903.05629`, studies the truncated divisor sum (22) and its moments. It supplies adjacent prior art for the truncated-convolution language, not the present Mathia interpretation.

Accordingly, no novelty is claimed for equations (4), (9), (23), or the underlying coefficient extraction. The durable contribution is the **mechanism audit relative to the current research frontier**: the specific finite boundary datum left open by `MC-026` becomes an exact next-block Möbius reflection after the auxiliary product convolution, so product-collapsed treatment of that boundary cannot be credited as independently weaker information.

## 7. Boundaries and decisive continuation

The obstruction is deliberately narrow. It applies to the equal-cutoff, degree-two Huxley–Watt block and to estimates that collapse `(m,n,k)` to the total product `q` before extracting their gain. It does not prove analogous reflection for every unequal-range or higher-degree boundary, and it does not rule out cancellation between different inclusion–exclusion degrees before product collapse.

It also does not rule out the unsplit analytic mechanism of `MC-027`: a direct estimate of a coupled signed germ may preserve information that the scalar coefficient `d_N(q)` forgets. Likewise, the factor-coordinate defect `e_{2,N}(r)` can still carry useful structure before convolution with `1`; equation (6) says only that this structure ceases to be weaker after the exact auxiliary convolution used above.

The next viable test should therefore retain a piece of pre-collapse structure. A candidate must identify an explicit factor-coordinate, unequal-cutoff, cross-degree, or analytic coupling and prove a fixed-power gain from information weaker than the target Möbius block. If its decisive estimate can be rewritten solely as a bound for `d_N(q)`, `(e_{2,N}*1)(q)`, or the corresponding grouped partial sums in the square annulus, equations (4)–(9) show that the target cancellation has merely been renamed.

## Consequence for the research line

`MC-026` left finite cutoff faces as one possible escape from the unrestricted convolution zero boundary. The present exact calculation removes the simplest version of that escape: after the source-natural auxiliary convolution and product collapse, the degree-two cutoff defect is pointwise equivalent to the new Möbius block.

Together with `MC-027`, this focuses the surviving Huxley–Watt route further upstream. Any genuine bootstrap must preserve and exploit signed structure **before** the triangle inequality and **before** total-product collapse. The remaining information candidates are the factor coordinates themselves, nontrivial relations among cutoff faces or degrees, and coupled analytic structure whose estimate does not reduce to a scalar Möbius reflection.