# FD-151 — Growing anchors trade the parent tax for coefficient mass

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** growing-anchor obstruction / endpoint-mass phase diagram
- **Depends on:** FD-147, FD-148, FD-150

## Claim

FD-150 leaves a specific escape from the fixed-seed parent tax: let the Möbius anchor itself grow with the coefficient horizon. The complement-cut mechanism can be extended without any fixed-anchor hypothesis, and it gives an exact price for that escape.

Let

\[
V_T:=\{n\le T:\mu^2(n)=1\},
\qquad
\nu_T(n):=|V_T|^{-1},
\tag{1}
\]

and let `D_T\subsetneq V_T` be any nonempty divisor-closed anchor containing `1`; `D_T` may now depend arbitrarily on `T`. Let `E_T^*` be any positive directed divisibility relation on `V_T`, so every edge is of the form `(n,m)` with `n|m` and `n<m`. This includes the one-step graph of FD-148 and every bounded- or unbounded-depth ancestry relation of FD-149--FD-150. Let `eta_T` be a probability measure on `E_T^*`, write

\[
\eta_T^-(n):=\sum_{m:(n,m)\in E_T^*}\eta_T(n,m),
\tag{2}
\]

and define the anchored Cheeger constant

\[
h_{D_T,T}
:=
\inf_{\varnothing\ne A\subseteq V_T\setminus D_T}
\frac{\eta_T(\partial A)}{\nu_T(A)}.
\tag{3}
\]

Put

\[
p_T:=\nu_T(D_T)=\frac{|D_T|}{|V_T|}.
\tag{4}
\]

If the parent marginal on the anchor is pointwise dominated by the coefficient measure,

\[
\eta_T^-(d)\le P_T\nu_T(d)
\qquad(d\in D_T),
\tag{5}
\]

then, independently of the ancestry depth,

\[
\boxed{
 h_{D_T,T}
 \le
 \frac{P_Tp_T}{1-p_T}.
}
\tag{6}
\]

Therefore a uniformly positive anchored expansion

\[
h_{D_T,T}\ge c>0
\tag{7}
\]

forces the exact reciprocal-density parent tax

\[
\boxed{
P_T\ge c\,\frac{1-p_T}{p_T}.
}
\tag{8}
\]

Equivalently, if `P_T<=P<infinity`, then every such anchor must already carry a fixed positive fraction of the coefficient measure:

\[
\boxed{
p_T\ge\frac{c}{P+c}.}
\tag{9}
\]

Since `|V_T|=T/\zeta(2)+o(T)`, bounded parent distortion thus requires

\[
\boxed{|D_T|=\Omega_{c,P}(T).}
\tag{10}
\]

More generally, whenever `|D_T|=o(T)`,

\[
\boxed{
P_T
\ge
\left(\frac{c}{\zeta(2)}+o(1)\right)
\frac{T}{|D_T|}.
}
\tag{11}
\]

Hence the linear parent tax of FD-148 is not a special pathology of a fixed seed. It is the first point of a general reciprocal-anchor-mass law: a growing anchor can reduce the singular parent amplification only by directly anchoring a correspondingly larger part of the coefficient space.

There is an arithmetic phase curve for the canonical divisor-closed rank anchors

\[
D_T(r):=\{n\in V_T:\omega(n)\le r\}.
\tag{12}
\]

Write `lambda_T=log log T`. For fixed `0<alpha<1` and

\[
r_T=\lfloor\alpha\lambda_T\rfloor,
\tag{13}
\]

squarefree Sathe--Selberg gives

\[
\boxed{
 p_T
 =\nu_T(D_T(r_T))
 \asymp_\alpha
 \frac{1}{\sqrt{\lambda_T}(\log T)^{I(\alpha)}},
 \qquad
 I(\alpha)=1-\alpha+\alpha\log\alpha.
}
\tag{14}
\]

Thus positive anchored expansion forces

\[
\boxed{
P_T
\gg_{c,\alpha}
\sqrt{\log\log T}\,(\log T)^{I(\alpha)}.
}
\tag{15}
\]

This is the same large-deviation rate function that FD-150 finds on the **child** side, but with a different resource interpretation: there `alpha log log T` measures transfer depth from a fixed seed; here it measures how much multiplicative rank has already been placed inside the anchor itself.

At the central scale the transition is sharp for this complement cut. If

\[
r_T=\lambda_T+z\sqrt{\lambda_T}+o(\sqrt{\lambda_T}),
\tag{16}
\]

then squarefree Erdos--Kac gives

\[
\boxed{p_T\longrightarrow\Phi(z).}
\tag{17}
\]

Conversely, if `P_T<=P`, (7) holds, and `D_T=D_T(r_T)`, then

\[
\boxed{
\liminf_{T\to\infty}
\frac{r_T-\lambda_T}{\sqrt{\lambda_T}}
\ge
\Phi^{-1}\!\left(\frac{c}{P+c}\right).
}
\tag{18}
\]

So bounded parent distortion can evade the growing-anchor complement cut only once the anchor itself reaches the typical prime-factor depth and contains a macroscopic fraction of all squarefree coefficients. Typical transfer depth does not pay the parent bill; it can only move that bill into the anchor.

## 1. The complement cut does not require a fixed anchor

Take

\[
A_T:=V_T\setminus D_T.
\tag{19}
\]

Because `D_T` is divisor-closed, no directed divisibility edge can start in `A_T` and end in `D_T`: if `n|m` and `m\in D_T`, then divisor closure forces `n\in D_T`. Therefore every edge crossing the complement cut starts at an anchor vertex. Consequently

\[
\eta_T(\partial A_T)
\le
\sum_{d\in D_T}\eta_T^-(d).
\tag{20}
\]

Under (5),

\[
\eta_T(\partial A_T)
\le
P_T\sum_{d\in D_T}\nu_T(d)
=P_Tp_T.
\tag{21}
\]

Since

\[
\nu_T(A_T)=1-p_T,
\tag{22}
\]

testing only `A_T` in (3) proves (6). No estimate for degrees, edge counts, transfer depth, prime distribution, or the internal geometry of `D_T` is needed.

FD-147 then immediately turns (6) into a binary finite-`L^q` coercivity bound. For every fixed `1<=q<infinity`,

\[
C^{\rm bin}_{q,D_T}(T)
=h_{D_T,T}^{-1/q}
\ge
\left(\frac{1-p_T}{P_Tp_T}\right)^{1/q}.
\tag{23}
\]

Thus a vanishing anchor density is already fatal to bounded-distortion finite-`L^q` recovery, regardless of how deep or dense the positive divisibility relation becomes.

## 2. Anchor cardinality gives a universal parent-amplification law

The squarefree counting asymptotic gives

\[
|V_T|=\frac{T}{\zeta(2)}+o(T).
\tag{24}
\]

If `d_T:=|D_T|=o(T)`, then

\[
p_T
=\frac{d_T}{|V_T|}
=(\zeta(2)+o(1))\frac{d_T}{T}
=o(1).
\tag{25}
\]

Substituting (25) into (8) proves (11). In particular, if for some fixed `0<=theta<1`

\[
|D_T|\le T^{\theta+o(1)},
\tag{26}
\]

then constant anchored expansion requires

\[
\boxed{P_T\ge T^{1-\theta-o(1)}.}
\tag{27}
\]

At one endpoint, a fixed finite anchor has `theta=0` and recovers the linear amplification tax of FD-148. At the other endpoint, bounded `P_T` is possible under this cut only when the anchor cardinality is linear in `T`.

This distinction matters because a growing anchor is not a free geometric repair. Enlarging `D_T` changes the class of synthetic binary sources by forcing agreement with Möbius on every anchor coefficient. Equation (9) says that avoiding singular parent weights with this strategy requires exact anchoring on a positive-density subset of the squarefree coefficient space. The theorem does not call that circular by itself, but it makes the source-information expenditure explicit and therefore testable against the later information/reconstruction gates of the line.

## 3. Fixed-rank growing anchors already improve the parent tax only polylogarithmically

Before the proportional-rank regime, the classical fixed-rank law gives a useful interpolation between a finite seed and the Erdos--Kac scale. For every fixed integer `r>=1`,

\[
\#\{n\le T:\mu^2(n)=1,\ \omega(n)=r\}
\sim
\frac{T(\log\log T)^{r-1}}
{(r-1)!\log T}.
\tag{28}
\]

The top rank dominates the finite sum defining `D_T(r)`, so

\[
\boxed{
\nu_T(D_T(r))
\sim
\frac{\zeta(2)}{(r-1)!}
\frac{(\log\log T)^{r-1}}{\log T}.
}
\tag{29}
\]

Hence (8) forces

\[
\boxed{
P_T
\gg_{c,r}
\frac{\log T}{(\log\log T)^{r-1}}.
}
\tag{30}
\]

For `r=1`, anchoring `1` and every prime reduces the fixed-seed linear parent tax to a logarithmic one, but only because the anchor has grown to roughly `T/log T` coefficients. For every fixed `r`, bounded parent distortion still fails. The exceptional `r=0` anchor is `D_T(0)={1}` and returns the order-`T` tax directly.

This is a useful matched control on the meaning of "growing anchor": even a set that is enormous compared with a finite seed can remain sparse enough to force divergent parent amplification.

## 4. Sathe--Selberg gives the proportional-rank phase curve

Now let `r_T=floor(alpha lambda_T)` with fixed `0<alpha<1`. FD-150 already records the squarefree Sathe--Selberg lower-tail estimate

\[
\nu_T\!\left(\omega(n)\le\alpha\lambda_T+O(1)\right)
\asymp_\alpha
\frac1{\sqrt{\lambda_T}(\log T)^{I(\alpha)}}.
\tag{31}
\]

Since the rank anchor (12) is exactly this lower tail, (31) is (14). The complement-cut inequality then gives

\[
h_{D_T(r_T),T}
\ll_\alpha
\frac{P_T}
{\sqrt{\lambda_T}(\log T)^{I(\alpha)}},
\tag{32}
\]

and (15) follows under `h>=c`.

The same rate function therefore governs two different ways of spending multiplicative nonlocality. FD-150 keeps the anchor fixed and pays the rate through the child marginal until the transfer reaches rank `alpha lambda_T`. FD-151 grows the anchor itself to that rank and pays the rate through the parent marginal. The two operations are not interchangeable: transfer depth enlarges the set of descendants that can receive boundary mass, whereas anchor growth directly fixes the source orientation on more coefficients.

For `alpha=1-delta`,

\[
I(1-\delta)
=\frac{\delta^2}{2}+\frac{\delta^3}{6}+O(\delta^4),
\tag{33}
\]

so even an anchor reaching a fixed fractional distance below typical rank still requires a power of `log T` of parent amplification. At the exact exponent boundary the residual `sqrt(log log T)` factor remains necessary, just as on the child side in FD-150.

## 5. Bounded parent distortion pushes the anchor into the Erdos--Kac window

Suppose `P_T<=P` and `h_{D_T,T}>=c>0`. Equation (6) implies

\[
c
\le
\frac{Pp_T}{1-p_T},
\tag{34}
\]

which rearranges to

\[
p_T\ge\theta,
\qquad
\theta:=\frac{c}{P+c}\in(0,1).
\tag{35}
\]

For the rank anchor `D_T(r_T)`, squarefree Erdos--Kac says

\[
\frac{\omega(n)-\lambda_T}{\sqrt{\lambda_T}}
\Longrightarrow N(0,1)
\tag{36}
\]

under `nu_T`. Put

\[
z_T:=\frac{r_T-\lambda_T}{\sqrt{\lambda_T}}.
\tag{37}
\]

If some subsequence satisfied

\[
z_T\le\Phi^{-1}(\theta)-\varepsilon
\tag{38}
\]

for fixed `epsilon>0`, monotonicity of the distribution function and (36) would imply along that subsequence

\[
\limsup p_T
\le
\Phi\!\left(\Phi^{-1}(\theta)-\varepsilon\right)
<\theta,
\tag{39}
\]

contradicting (35). This proves (18).

Conversely, if (16) holds for fixed `z`, then (36) gives (17). Thus the complement-cut parent obstruction itself undergoes a genuine transition in the `sqrt(log log T)` window around typical rank. Once the anchor reaches that window it can carry constant coefficient mass, so cardinality alone cannot force a diverging parent distortion. Other anchored cuts may still do so.

## 6. The resource picture after FD-150 and FD-151

For positive divisibility-based binary coercivity, the fixed-anchor shorthand "parent concentration plus either child concentration or typical depth" can now be sharpened one step further.

With a fixed seed, FD-150 shows that ancestry depth only trades the child-side tax; the parent amplification remains order `T`. With a growing anchor, FD-151 shows that the parent tax is exactly reciprocal to the anchor's coefficient mass up to the harmless factor `1-p_T`. Therefore there are only two ways for the complement cut to stop forcing singular parent weights:

1. keep a sparse anchor and explicitly amplify its parent marginal by at least order `1/p_T`; or
2. grow the anchor until it contains a nonvanishing fraction of the coefficient space.

For the canonical low-rank anchors, option 2 reaches bounded distortion only at the same `log log T` multiplicative scale that appeared as the child-depth threshold, but it spends that scale much more aggressively: the anchor now fixes the Möbius orientation on `Theta(T)` squarefree coefficients.

This does not prove that a macroscopic source-native anchor is illegitimate. A genuinely Farey-derived observable might expose such a set without separately observing every coefficient. It does mean that the mechanism must be exhibited. Merely declaring the anchor to grow moves the missing coercivity into a macroscopic source constraint rather than solving it.

## 7. Prior-art and novelty boundary

The abstract relation between weighted cuts, Dirichlet boundary conditions, and finite-`L^q` coercivity is classical and was already delimited in FD-147. A fresh literature audit again finds the broader measured-expander and weighted-Cheeger framework; no novelty is claimed for testing a Poincare inequality on the complement of a boundary set.

The arithmetic inputs are also classical: the fixed-rank Landau law, squarefree Erdos--Kac theorem, and squarefree Sathe--Selberg local law are already anchored in `research/farey_discrepancy/SOURCES.md` and used in FD-149--FD-150. No new external theorem is load-bearing here, so `SOURCES.md` does not need a new dependency.

The line-specific contribution is the growing-anchor splice. FD-148 quantified the parent tax only for a fixed finite anchor and explicitly left growing anchors outside its scope. Equations (6)--(18) classify that escape at the complement-cut level: **the fixed-seed factor `T` is replaced by reciprocal anchor density, and a bounded-distortion rank anchor must enter the typical Erdos--Kac window, where it already fixes a positive fraction of the coefficient space.**

## 8. Boundaries and falsifiable next test

The result is a necessary-condition screen, not a sufficiency theorem. It uses positive edge weights, binary Möbius orientations, finite `L^q` through FD-147, and a divisor-closed anchor. It does not cover signed or oscillatory transfers, `L^infinity`, non-divisibility destination functionals, or an anchor whose effect is encoded through a different norm. Even when `p_T` is bounded below, another anchored cut may have vanishing boundary mass.

The rank-anchor phase curve is a specialization, not a claim that every useful growing anchor must be rank-truncated. For an arbitrary source-native anchor the universal quantity to expose is simply

\[
p_T=\nu_T(D_T).
\tag{40}
\]

A future positive ancestry proposal should therefore report the anchor mass and the parent distortion before ancestry depth is credited as a resource. If it claims `h>=c` with `P_T=O(1)` while `p_T->0`, (6) refutes it immediately. If it uses a macroscopic anchor to keep `P_T` bounded, the next audit is no longer another endpoint estimate: it is whether the Farey observable genuinely supplies that much absolute source orientation without already crossing the line's source-reconstruction/information boundary. Only after that audit should the remaining non-anchor cuts be tested.
