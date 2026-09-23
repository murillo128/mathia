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
\tag{1}
\]

For any positive Dirichlet source

\[
Q(s)=\sum_x a_x x^{-s},
\qquad a_x>0,
\tag{2}
\]

whose first two logarithmic moments converge at the observation point, define

\[
M_j^P(s)=\sum_p(\log p)^j p^{-s},
\qquad
M_j^Q(s)=\sum_x a_x(\log x)^j x^{-s},
\qquad j=0,1,2,
\tag{3}
\]

so that `M_0^P=P`, `M_1^P=-P'`, `M_2^P=P''`, and similarly for `Q`. Put

\[
\rho_j(s)=\frac{M_j^Q(s)}{M_j^P(s)},
\qquad
r(s)=\frac{(M_1^P(s))^2}{M_0^P(s)M_2^P(s)}.
\tag{4}
\]

Then the curvature ratio has the exact three-moment identity

\[
\boxed{
\frac{\kappa_Q(s)}{\kappa_P(s)}
=
\frac{
\rho_2(s)/\rho_0(s)
-r(s)\bigl(\rho_1(s)/\rho_0(s)\bigr)^2
}
{1-r(s)}.
}
\tag{5}
\]

At the prime-zeta boundary `s=1+t`, write

\[
L=\log\frac1t.
\tag{6}
\]

The classical singular expansion gives

\[
P(1+t)=L+O(1),
\qquad
M_1^P(1+t)=\frac1t+O(1),
\qquad
M_2^P(1+t)=\frac1{t^2}+O(1),
\tag{7}
\]

and therefore

\[
r(1+t)=\frac1L\bigl(1+o(1)\bigr).
\tag{8}
\]

Consequently, along any sequence `t\downarrow0` for which

\[
\rho_0(1+t)\to c_0>0,
\qquad
\rho_2(1+t)\to c_2,
\qquad
\frac{\rho_1(1+t)}{\sqrt L}\to c_1,
\tag{9}
\]

one has

\[
\boxed{
\frac{\kappa_Q(1+t)}{\kappa_P(1+t)}
\longrightarrow
\frac{c_2}{c_0}-\left(\frac{c_1}{c_0}\right)^2.
}
\tag{10}
\]

Thus the two-moment law of AF-520 survives beyond outward transport exactly when the normalized first-moment term is negligible:

\[
r(1+t)
\left(\frac{\rho_1(1+t)}{\rho_0(1+t)}\right)^2
\longrightarrow0.
\tag{11}
\]

When `\rho_0` stays bounded below, the transparent sufficient condition is

\[
\rho_1(1+t)=o(\sqrt L).
\tag{12}
\]

AF-520's outward-support hypothesis enforces the much stronger estimate `\rho_1=O(1)`. Inward transport can violate this gate and promote the first logarithmic moment to leading order.

Moreover, this promotion occurs for literal simple unit-weight arithmetic controls. For every fixed `a>0`, there are two families `Q_t^{(A)}` and `Q_t^{(B)}` obtained from the rational-prime support by moving finitely many sufficiently remote primes **inward to distinct even composite integers**, leaving all other primes unchanged, such that

\[
\rho_0^{(A)},\rho_0^{(B)}\longrightarrow1+a,
\qquad
\rho_2^{(A)},\rho_2^{(B)}\longrightarrow1+a,
\tag{13}
\]

while

\[
\frac{\rho_1^{(A)}}{\sqrt L}\longrightarrow a,
\qquad
\frac{\rho_1^{(B)}}{\sqrt L}\longrightarrow\frac{7a}{8}.
\tag{14}
\]

Hence the two controls are asymptotically indistinguishable by the AF-520 leading pair `(\rho_0,\rho_2)` but have different leading curvatures:

\[
\boxed{
\frac{\kappa_{Q_t^{(A)}}}{\kappa_P}
\longrightarrow
1-\left(\frac{a}{1+a}\right)^2
=
\frac{1+2a}{(1+a)^2},
}
\tag{15}
\]

whereas

\[
\boxed{
\frac{\kappa_{Q_t^{(B)}}}{\kappa_P}
\longrightarrow
1-\left(\frac{7a}{8(1+a)}\right)^2.
}
\tag{16}
\]

Their limiting curvature gap is therefore

\[
\boxed{
\lim_{t\downarrow0}
\frac{
\kappa_{Q_t^{(B)}}(1+t)-\kappa_{Q_t^{(A)}}(1+t)
}{\kappa_P(1+t)}
=
\frac{15a^2}{64(1+a)^2}>0.
}
\tag{17}
\]

So `(\rho_0,\rho_2)` is not a sufficient leading carrier once the first-moment domination supplied by outwardness is removed. At one boundary scale, the exact scalar curvature still factors through finitely many quantities, but the correct universal carrier is the **three raw logarithmic moments** rather than the AF-520 two-moment quotient.

## Derivation

### 1. Curvature is exactly a three-raw-moment observable

For any positive source `Q`,

\[
\kappa_Q
=
\frac{M_2^Q}{M_0^Q}
-
\left(\frac{M_1^Q}{M_0^Q}\right)^2.
\tag{18}
\]

Likewise,

\[
\kappa_P
=
\frac{M_2^P}{M_0^P}
\left(
1-
\frac{(M_1^P)^2}{M_0^P M_2^P}
\right)
=
\frac{M_2^P}{M_0^P}(1-r).
\tag{19}
\]

Using `M_j^Q=\rho_jM_j^P` in `(18)` gives

\[
\kappa_Q
=
\frac{M_2^P}{M_0^P}
\left[
\frac{\rho_2}{\rho_0}
-r\left(\frac{\rho_1}{\rho_0}\right)^2
\right].
\tag{20}
\]

Division by `(19)` proves `(5)` exactly. No transport direction, support ordering, or asymptotic assumption enters this identity.

This already identifies the role of AF-520's outwardness. The curvature observable itself always contains the first-moment square. AF-520 did not remove that coordinate algebraically; it proved that outward transport keeps it uniformly below the prime-zeta leading scale.

### 2. The first-moment visibility threshold is `sqrt(log(1/t))`

From the classical prime-zeta expansion `(7)`,

\[
r(1+t)
=
\frac{t^{-2}(1+o(1))}
{(L+O(1))t^{-2}(1+o(1))}
=
\frac1L(1+o(1)).
\tag{21}
\]

Substitute `(9)` and `(21)` into the exact identity `(5)`. Since `1-r\to1`,

\[
\frac{\rho_2}{\rho_0}\to\frac{c_2}{c_0},
\tag{22}
\]

while

\[
r\left(\frac{\rho_1}{\rho_0}\right)^2
=
\frac1L(1+o(1))
\left(
\frac{c_1\sqrt L+o(\sqrt L)}{c_0+o(1)}
\right)^2
\longrightarrow
\left(\frac{c_1}{c_0}\right)^2.
\tag{23}
\]

This proves `(10)`. It also makes the three first-moment regimes explicit. If `\rho_1=o(\sqrt L)` the first moment disappears at leading order; if `\rho_1\asymp\sqrt L` it contributes at order one; if it grows faster than `\sqrt L`, then finite nondegenerate limits of the other normalized moments cannot by themselves control the curvature ratio.

For AF-520 outward transport, eventual monotonicity of `y e^{-sy}` on the remote tail gives

\[
M_1^Q(1+t)\le M_1^P(1+t),
\tag{24}
\]

so `\rho_1\le1`. The threshold `(12)` is then automatic. The outwardness assumption is therefore an exact **first-moment suppression mechanism**, not merely a convenient ordering convention.

### 3. Composite blocks can prescribe zeroth, first, and second boundary moments at different weights

Fix `a>0`. Let `t\downarrow0`, put

\[
L=\log\frac1t,
\qquad
y=\frac1{t\sqrt L}.
\tag{25}
\]

For fixed constants `c>0` and `w>0`, define a finite even-composite block

\[
B_t(c,w)
=
\left\{
 n\in2\mathbb N:
 e^{cy}<n\le e^{cy+2awL}
\right\}.
\tag{26}
\]

For `j=0,1,2`, write

\[
S_j(c,w;t)
=
\sum_{n\in B_t(c,w)}
(\log n)^j n^{-1-t}.
\tag{27}
\]

Since the even integers have spacing two, standard monotone sum-integral comparison gives

\[
S_j(c,w;t)
\sim
\frac12
\int_{e^{cy}}^{e^{cy+2awL}}
(\log x)^j x^{-1-t}\,dx.
\tag{28}
\]

With `u=\log x`, the integral becomes

\[
\frac12
\int_{cy}^{cy+2awL}
u^j e^{-tu}\,du.
\tag{29}
\]

The interval width is negligible relative to its logarithmic location:

\[
\frac{2awL}{y}=2aw\,tL^{3/2}\longrightarrow0,
\tag{30}
\]

and uniformly on this interval

\[
tu=\frac{c}{\sqrt L}+o(1)\longrightarrow0.
\tag{31}
\]

Therefore `e^{-tu}=1+o(1)` and `u^j=(cy)^j(1+o(1))` uniformly, so

\[
\boxed{
S_j(c,w;t)
\sim
awL(cy)^j.
}
\tag{32}
\]

In particular,

\[
S_0(c,w;t)\sim awL,
\tag{33}
\]

\[
S_1(c,w;t)\sim awc\frac{\sqrt L}{t},
\tag{34}
\]

and

\[
S_2(c,w;t)\sim awc^2\frac1{t^2}.
\tag{35}
\]

Thus the block's zeroth and second moments depend on `w` and `wc^2`, while its first moment depends on the independent combination `wc`.

### 4. Two block systems match moments zero and two but not moment one

Define system `A` by the single block

\[
\mathcal B_t^{(A)}=B_t(1,1).
\tag{36}
\]

Define system `B` by two blocks

\[
\mathcal B_t^{(B)}
=
B_t\!\left(\frac12,\frac58\right)
\sqcup
B_t\!\left(\frac32,\frac38\right).
\tag{37}
\]

The blocks in `(37)` are disjoint for sufficiently small `t` because their logarithmic separation is of order `y`, whereas each logarithmic width is only `O(L)=o(y)`.

The weights satisfy

\[
\frac58+\frac38=1,
\tag{38}
\]

\[
\frac58\left(\frac12\right)^2
+
\frac38\left(\frac32\right)^2
=1,
\tag{39}
\]

but

\[
\frac58\left(\frac12\right)
+
\frac38\left(\frac32\right)
=\frac78.
\tag{40}
\]

Applying `(32)` blockwise therefore gives

\[
S_0^{(A)}\sim S_0^{(B)}\sim aL,
\tag{41}
\]

\[
S_2^{(A)}\sim S_2^{(B)}\sim\frac{a}{t^2},
\tag{42}
\]

but

\[
S_1^{(A)}\sim a\frac{\sqrt L}{t},
\qquad
S_1^{(B)}\sim\frac{7a}{8}\frac{\sqrt L}{t}.
\tag{43}
\]

This is the required matched two-moment pair before embedding it into a transported prime source.

### 5. The blocks are realizable by genuine inward prime-to-composite transport

For either system `X\in\{A,B\}`, let `N_t^{(X)}` be its finite number of target composite atoms. All targets are distinct even composites and tend to infinity with `t\downarrow0`.

Choose a cutoff `R_t^{(X)}` larger than every target and so large that, for `j=0,1,2`,

\[
\sum_{p>R_t^{(X)}}
(\log p)^j p^{-1-t}
=
o\!\left(M_j^P(1+t)\right).
\tag{44}
\]

Such a cutoff exists for every fixed `t>0` because all three prime Dirichlet moment series converge absolutely at `1+t`; choose the relative error in `(44)` to tend to zero with `t`.

Now choose `N_t^{(X)}` distinct primes above `R_t^{(X)}` and map them bijectively to the target block atoms. Leave every other rational prime fixed. Since every source prime exceeds every target, every moved atom is strictly inward. Since the targets are distinct even composites greater than two, they collide neither with each other nor with an unchanged prime. The resulting support is therefore a simple unit-weight arithmetic source.

The moments removed with the selected source primes are bounded by the complete tail in `(44)` and are negligible on the corresponding prime moment scale. Thus the transported source satisfies

\[
M_j^{Q_t^{(X)}}(1+t)
=
M_j^P(1+t)
+S_j^{(X)}(t)
+o\!\left(M_j^P(1+t)\right),
\qquad j=0,1,2.
\tag{45}
\]

Using `(7)` together with `(41)`--`(43)` yields `(13)`--`(14)`. Substitution into `(10)` proves `(15)`--`(17)`.

The construction is deliberately adversarial: the control does not attempt to imitate local primality. It matches exactly the **leading information layer retained by the AF-520 two-defect description** and then varies the first moment that AF-520 was able to suppress only because its transport was outward.

## Fidelity and matched-control audit

AF-520 showed that arbitrary outward, source-surviving transport is compressed at one moving boundary scale to the pair

\[
(\rho_0,\rho_2).
\tag{46}
\]

AF-521 identifies the precise hypothesis behind that reduction. Without first-moment domination, the universal exact factorization is instead

\[
(\rho_0,\rho_1,\rho_2)
\longmapsto
\frac{
\rho_2/\rho_0-r(\rho_1/\rho_0)^2
}{1-r}.
\tag{47}
\]

The matched controls `(36)`--`(45)` show that the third coordinate is not formally redundant. Two simple unit-weight sources can match the leading zeroth and second moments and still remain separated by an order-one curvature gap solely because their first logarithmic moments differ at the `\sqrt L` threshold.

This is a stronger falsification test than merely exhibiting an inward transport whose curvature changes. It shows **why** the AF-520 quotient ceases to be faithful and identifies the minimal additional scalar coordinate required by this particular one-scale curvature observable before any richer displacement profile is considered.

The result does not make curvature prime-faithful. The controls themselves are obtained by replacing prime atoms with composites, and the exact carrier `(47)` sees only three tilted moments. Arithmetic incidence beyond those moments can still disappear completely.

## Representation audit

For the tilted probability measure

\[
\mu_{Q,s}(x)
=
\frac{a_xx^{-s}}{Q(s)},
\tag{48}
\]

one has the classical cumulant identity

\[
-(\log Q)'(s)
=
\mathbb E_{\mu_{Q,s}}[\log x],
\qquad
(\log Q)''(s)
=
\operatorname{Var}_{\mu_{Q,s}}(\log x).
\tag{49}
\]

Thus `(5)` is not a new representation of curvature: it is the ordinary variance formula rewritten relative to the prime source. What is line-specific is the boundary scaling audit. The singular prime reference makes the squared mean term smaller by `1/L`, but an inward transport can increase the normalized mean by `\sqrt L`, exactly cancelling that suppression.

This gives a useful general warning for Arithmetic Fidelity. A term that is lower order in the reference object is not automatically lower order after a transformation. One must control the **relative amplification of the corresponding normalized moment**, not merely its coefficient in the reference asymptotic.

## Prior art and novelty assessment

No novelty is claimed for the standard ingredients.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187--202, DOI `10.1007/BF01933420`, is the classical source for the prime-zeta singular behavior at `s=1` used in `(7)`--`(8)`.
- M. J. Wainwright and M. I. Jordan, **“Graphical Models, Exponential Families, and Variational Inference,”** *Foundations and Trends in Machine Learning* 1(1--2) (2008), 1--305, DOI `10.1561/2200000001`, is standard background for log-partition functions, cumulants, and the mean/covariance derivative identities represented here by `(49)`.
- The even-integer block estimate `(28)`--`(35)` uses only elementary sum-integral comparison and a fixed-spacing density calculation.

A focused literature search located the standard prime-zeta boundary asymptotics and classical cumulant/log-partition interpretation, but did not identify a standard theorem formulated as the `\sqrt{\log(1/t)}` first-moment gate for transported prime-zeta curvature or the matched inward prime-to-composite construction above. AF-521 is therefore stored as an exact internal classification result with `NO-NOVELTY-CLAIM`, not as a claim of external theorem novelty.

## Boundaries and failure modes

1. **This is a one-scale statement.** The exact identity `(5)` holds pointwise, but the asymptotic classification `(10)` concerns one moving real boundary scale `s=1+t`. A continuum of scales can encode additional structure through the scale dependence of all three moments.
2. **Positive source mass is used.** The variance representation and the composite-block construction use positive coefficients. Signed or complex sources can have cancellation and require a different normalization audit.
3. **Near-extinction remains separate.** Equation `(10)` assumes `\rho_0\to c_0>0`. When the transformed source value tends to zero relative to `P`, division by `\rho_0` can amplify all moment layers and the present threshold no longer classifies the regime.
4. **The construction is inward and highly nonlocal.** It proves that outwardness is mathematically essential to AF-520's two-moment reduction. It does not assert that every natural arithmetic transformation admits such remote-to-mesoscopic relocation.
5. **Matching is asymptotic at the retained layer.** The controls match the leading normalized zeroth and second moments, not their exact finite-`t` values. This is sufficient to refute two-moment sufficiency for the leading curvature asymptotic, but it is not an exact finite-parameter collision theorem.
6. **Three moments suffice only for scalar curvature at one point.** Equation `(5)` does not imply that three moments recover the source, identify the rational primes, determine the full curvature profile, or retain information needed by another downstream operator.
7. **No RH consequence follows.** The result classifies a compression boundary and a matched arithmetic control. It neither proves a prime-specific discriminator nor supplies evidence for the Riemann hypothesis.

## Research consequence

AF-520 left mixed/inward transport as the first escape from its universal two-defect law. AF-521 closes the basic version of that escape: **inward transport does not force an immediately measure-valued leading carrier; it promotes exactly one previously suppressed scalar, the first logarithmic moment, at the threshold `\rho_1\asymp\sqrt{\log(1/t)}`.**

The one-scale hierarchy is now explicit. Under outward domination the leading carrier is `(\rho_0,\rho_2)`; without that domination the exact scalar curvature carrier is `(\rho_0,\rho_1,\rho_2)`. The remaining genuinely different frontiers are source extinction `\rho_0\to0`, lower-order/full-profile stability, multi-scale observation, signed/complex sources, and richer observables whose retained information can distinguish arithmetic provenance rather than only tilted moments.