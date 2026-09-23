# AF-521 — Inward transport promotes the first log moment to leading curvature

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `INWARD-TRANSPORT` · `THREE-MOMENT-COMPRESSION` · `MATCHED-COMPOSITE-CONTROL` · `MESOSCOPIC-CURVATURE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=(\log P(s))'',
\qquad s>1.
\]

For any positive Dirichlet source

\[
Q(s)=\sum_x a_xx^{-s},\qquad a_x>0,
\]

define its first three raw logarithmic moments at `s` by

\[
M_j^Q(s)=\sum_xa_x(\log x)^j x^{-s},
\qquad
M_j^P(s)=\sum_p(\log p)^jp^{-s},
\qquad j=0,1,2,
\]

and put

\[
\rho_j(s)=\frac{M_j^Q(s)}{M_j^P(s)},
\qquad
r(s)=\frac{(M_1^P(s))^2}{M_0^P(s)M_2^P(s)}.
\]

Then

\[
\boxed{
\frac{\kappa_Q(s)}{\kappa_P(s)}
=
\frac{
\rho_2(s)/\rho_0(s)-r(s)(\rho_1(s)/\rho_0(s))^2
}{1-r(s)}.
}
\tag{1}
\]

This identity is exact and uses no transport-direction hypothesis.

At the prime-zeta boundary `s=1+t`, set

\[
L=\log\frac1t.
\]

The classical prime-zeta expansion gives

\[
P(1+t)=L+O(1),\qquad
M_1^P(1+t)=\frac1t+O(1),\qquad
M_2^P(1+t)=\frac1{t^2}+O(1),
\]

so

\[
r(1+t)=\frac1L(1+o(1)).
\tag{2}
\]

Consequently, if

\[
\rho_0(1+t)\to c_0>0,
\qquad
\rho_2(1+t)\to c_2,
\qquad
\frac{\rho_1(1+t)}{\sqrt L}\to c_1,
\]

then

\[
\boxed{
\frac{\kappa_Q(1+t)}{\kappa_P(1+t)}
\longrightarrow
\frac{c_2}{c_0}-\left(\frac{c_1}{c_0}\right)^2.
}
\tag{3}
\]

Thus the two-moment law in AF-520 extends beyond outward transport precisely when the normalized first-moment contribution is negligible:

\[
r(1+t)\left(\frac{\rho_1(1+t)}{\rho_0(1+t)}\right)^2\to0.
\tag{4}
\]

When `\rho_0` stays bounded below, `\rho_1=o(\sqrt L)` is sufficient. AF-520's outwardness hypothesis enforces the stronger bound `\rho_1=O(1)`; inward transport can violate it and promote the first logarithmic moment to leading order.

There are also literal simple unit-weight arithmetic controls showing that this third coordinate is necessary. For every fixed `a>0`, one can obtain two sources `Q_t^{(A)}` and `Q_t^{(B)}` by moving finitely many sufficiently remote rational primes strictly inward to distinct even composites, leaving every other prime unchanged, such that

\[
\rho_0^{(A)},\rho_0^{(B)}\to1+a,
\qquad
\rho_2^{(A)},\rho_2^{(B)}\to1+a,
\tag{5}
\]

but

\[
\frac{\rho_1^{(A)}}{\sqrt L}\to a,
\qquad
\frac{\rho_1^{(B)}}{\sqrt L}\to\frac{7a}{8}.
\tag{6}
\]

Therefore the two controls match the AF-520 leading pair `(\rho_0,\rho_2)` while their leading curvature remains separated:

\[
\boxed{
\frac{\kappa_{Q_t^{(A)}}}{\kappa_P}
\to
1-\left(\frac{a}{1+a}\right)^2
=
\frac{1+2a}{(1+a)^2},
}
\tag{7}
\]

\[
\boxed{
\frac{\kappa_{Q_t^{(B)}}}{\kappa_P}
\to
1-\left(\frac{7a}{8(1+a)}\right)^2,
}
\tag{8}
\]

and hence

\[
\boxed{
\frac{\kappa_{Q_t^{(B)}}-\kappa_{Q_t^{(A)}}}{\kappa_P}
\to
\frac{15a^2}{64(1+a)^2}>0.
}
\tag{9}
\]

So `(\rho_0,\rho_2)` is not a sufficient leading carrier once the first-moment domination supplied by outwardness is removed. For scalar curvature at one observation point, the universal exact carrier is instead the triple `(\rho_0,\rho_1,\rho_2)`.

## Derivation

For every positive source,

\[
\kappa_Q
=
\frac{M_2^Q}{M_0^Q}
-
\left(\frac{M_1^Q}{M_0^Q}\right)^2,
\]

whereas

\[
\kappa_P
=
\frac{M_2^P}{M_0^P}(1-r).
\]

Substituting `M_j^Q=\rho_jM_j^P` proves `(1)`. Combining `(1)` with `(2)` immediately yields `(3)` and the threshold `(4)`. This also identifies exactly what AF-520's outward-support condition was buying: eventual monotonicity of `y e^{-sy}` on the moved remote tail gives `M_1^Q\le M_1^P`, hence `\rho_1\le1`, so the first-moment square is uniformly lower by a factor `1/L`.

To realize the critical `\sqrt L` amplification with ordinary composites, put

\[
y=\frac1{t\sqrt L}
\]

and, for fixed `c,w>0`, define the finite block

\[
B_t(c,w)=
\{n\in2\mathbb N:e^{cy}<n\le e^{cy+2awL}\}.
\tag{10}
\]

For `j=0,1,2`, let

\[
S_j(c,w;t)
=
\sum_{n\in B_t(c,w)}(\log n)^jn^{-1-t}.
\]

Since even integers have spacing two, standard sum-integral comparison gives

\[
S_j(c,w;t)
\sim
\frac12\int_{e^{cy}}^{e^{cy+2awL}}(\log x)^jx^{-1-t}\,dx
=
\frac12\int_{cy}^{cy+2awL}u^je^{-tu}\,du.
\tag{11}
\]

Here `2awL=o(y)` and `tu=c/\sqrt L+o(1)` uniformly on the integration interval. Therefore

\[
\boxed{S_j(c,w;t)\sim awL(cy)^j.}
\tag{12}
\]

In particular,

\[
S_0\sim awL,
\qquad
S_1\sim awc\frac{\sqrt L}{t},
\qquad
S_2\sim awc^2\frac1{t^2}.
\tag{13}
\]

Now take

\[
\mathcal B_t^{(A)}=B_t(1,1)
\]

and

\[
\mathcal B_t^{(B)}
=B_t\left(\frac12,\frac58\right)
\sqcup
B_t\left(\frac32,\frac38\right).
\]

The two blocks in system `B` are disjoint for sufficiently small `t` because their logarithmic separation is order `y`, while their widths are only `O(L)=o(y)`. The weights satisfy

\[
\frac58+\frac38=1,
\qquad
\frac58\left(\frac12\right)^2+
\frac38\left(\frac32\right)^2=1,
\]

but

\[
\frac58\left(\frac12\right)+
\frac38\left(\frac32\right)=\frac78.
\]

Hence `(12)` gives

\[
S_0^{(A)}\sim S_0^{(B)}\sim aL,
\qquad
S_2^{(A)}\sim S_2^{(B)}\sim\frac a{t^2},
\]

while

\[
S_1^{(A)}\sim a\frac{\sqrt L}{t},
\qquad
S_1^{(B)}\sim\frac{7a}{8}\frac{\sqrt L}{t}.
\tag{14}
\]

It remains to embed these finite composite blocks into a genuine prime transport. For each system and each fixed `t`, let `N_t` be the number of target composites. Choose `R_t` larger than every target and sufficiently large that, for `j=0,1,2`,

\[
\sum_{p>R_t}(\log p)^jp^{-1-t}
=o(M_j^P(1+t)).
\tag{15}
\]

This is possible because all three prime Dirichlet moment series converge for fixed `t>0`. Choose `N_t` distinct primes above `R_t`, map them bijectively to the target composites, and leave every other prime fixed. Every moved prime is larger than every target, so all moves are strictly inward; all targets are distinct even composites, so the resulting source remains simple and unit-weight.

The removed prime moments are bounded by `(15)`, hence negligible. Adding `(14)` to the prime moments from `(2)` proves `(5)`--`(6)`, and the exact curvature law then gives `(7)`--`(9)`.

## Fidelity and matched-control audit

AF-520 showed that arbitrary outward, source-surviving transport is compressed at one moving boundary scale to `(\rho_0,\rho_2)`. AF-521 identifies the hidden gate behind that reduction. Without first-moment domination, the exact factorization is

\[
(\rho_0,\rho_1,\rho_2)
\longmapsto
\frac{\rho_2/\rho_0-r(\rho_1/\rho_0)^2}{1-r}.
\]

The paired composite controls prove that the extra coordinate is not formal bookkeeping: two sources can match the retained leading zeroth and second moments and still have an order-one curvature gap solely through the first logarithmic moment.

This does **not** make curvature prime-faithful. The controls themselves replace prime atoms by composites, and scalar curvature still sees only three tilted moments at one point. Arithmetic incidence beyond those moments can disappear completely.

## Representation audit

For the tilted probability measure

\[
\mu_{Q,s}(x)=\frac{a_xx^{-s}}{Q(s)},
\]

one has the classical identities

\[
-(\log Q)'(s)=\mathbb E_{\mu_{Q,s}}[\log x],
\qquad
(\log Q)''(s)=\operatorname{Var}_{\mu_{Q,s}}(\log x).
\]

Thus `(1)` is ordinary cumulant mathematics rewritten relative to the prime source. The line-specific content is the boundary scaling: a term that is lower order for the reference source need not remain lower order after compression or transport. Its normalized moment can be amplified enough to cancel the reference suppression.

## Prior art and novelty assessment

No novelty is claimed for the standard ingredients.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187--202, DOI `10.1007/BF01933420`, is the classical source for the prime-zeta singular behavior at `s=1`.
- M. J. Wainwright and M. I. Jordan, **“Graphical Models, Exponential Families, and Variational Inference,”** *Foundations and Trends in Machine Learning* 1(1--2) (2008), 1--305, DOI `10.1561/2200000001`, is standard background for log-partition functions, cumulants, and the mean/covariance derivative identities used here.
- The even-composite block estimate is elementary sum-integral comparison.

A focused literature search located the standard prime-zeta boundary expansion and the classical cumulant/log-partition framework, but did not identify a standard result formulated as the `\sqrt{\log(1/t)}` first-moment gate for transported prime-zeta curvature or the matched inward prime-to-composite construction above. The result is therefore recorded as an exact internal classification with `NO-NOVELTY-CLAIM`, not as a claim of external theorem novelty.

## Boundaries and failure modes

1. **One moving scale only.** The exact identity is pointwise, but the asymptotic classification concerns one real sequence `s=1+t`. A continuum of scales may retain additional information through the scale dependence of the three moments.
2. **Positive sources only.** Signed or complex coefficients can introduce cancellation not represented by the positive tilted variance used here.
3. **Near-extinction remains open.** Formula `(3)` assumes `\rho_0\to c_0>0`; when `\rho_0\to0`, all normalized moment layers can be amplified differently.
4. **The controls are intentionally nonlocal.** They prove that outwardness is mathematically essential to AF-520's two-moment law, not that every natural arithmetic mechanism admits remote-to-mesoscopic inward relocation.
5. **Moment matching is asymptotic.** The controls match the leading normalized zeroth and second moments, not exact finite-`t` values. This is sufficient to refute two-moment sufficiency for the leading asymptotic, not to give an exact finite-parameter collision.
6. **Three moments are sufficient only for scalar curvature at one point.** They do not recover the source, determine its full curvature profile, identify the rational primes, or preserve information required by another operator.
7. **No RH consequence follows.** This classifies a compression boundary and supplies a matched arithmetic control; it is not evidence for RH.

## Research consequence

AF-520 left mixed/inward transport as the first escape from its universal two-defect law. AF-521 closes the basic version of that escape: **inward transport does not immediately require a measure-valued leading carrier; it promotes exactly one previously suppressed scalar, the first logarithmic moment, at the threshold `\rho_1\asymp\sqrt{\log(1/t)}`.**

The one-scale hierarchy is now explicit. Under outward domination the leading carrier is `(\rho_0,\rho_2)`; without that domination the exact scalar curvature carrier is `(\rho_0,\rho_1,\rho_2)`. The remaining genuinely different frontiers are source extinction `\rho_0\to0`, lower-order/full-profile stability, multi-scale observation, signed/complex sources, and richer observables capable of retaining arithmetic provenance rather than only tilted moments.