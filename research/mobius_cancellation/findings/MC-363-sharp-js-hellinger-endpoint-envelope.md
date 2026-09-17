# MC-363 — Sharp Jensen--Shannon/Hellinger envelope removes the remaining logarithmic endpoint loss

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-362` closes the permanent `log 2` endpoint slack in the direct Jensen--Shannon/Hellinger comparison by passing first through total variation. That route is endpoint-sharp, but its quantitative conversion is not optimal: near exact dephasing it leaves a Hellinger deficit of order

\[
\sqrt{\varepsilon\log(1/\varepsilon)}.
\]

There is a sharper direct envelope between equal-prior Jensen--Shannon divergence and Hellinger affinity. It retains the compositional Hellinger currency of `MC-360` and improves the near-endpoint deficit to order `\sqrt\varepsilon`.

For probability laws `P,Q`, write

\[
\operatorname{Aff}(P,Q)=\int\sqrt{dP\,dQ},
\qquad
z:=H^2(P,Q)=1-\operatorname{Aff}(P,Q),
\]

and let

\[
h(p)=-p\log p-(1-p)\log(1-p)
\]

be binary entropy in nats. Define

\[
\boxed{
\Phi(z)
:=
\log2-
 h\!\left(
 \frac{1-\sqrt{1-(1-z)^2}}2
 \right),
\qquad 0\le z\le1.
}
\tag{1}
\]

Then every pair `P,Q` satisfies the sharp envelope

\[
\boxed{
\operatorname{JS}(P,Q)\le \Phi\!\left(H^2(P,Q)\right).
}
\tag{2}
\]

The function `Phi` is increasing and concave, with `Phi(0)=0` and `Phi(1)=log 2`. Equality is attained by the two-output binary-symmetric experiment, so `(2)` cannot be improved using only the Hellinger affinity.

Continue the even-rank reciprocal endpoint notation of `MC-359`--`MC-362`:

\[
m=2^R-1,
\qquad
q_R=\frac{m-1}{m},
\qquad
\mathfrak H_1=\frac2m\sum_{e\in E(S)}H^2(P_x,P_{x'}).
\tag{3}
\]

The same punctured-cube bitwise argument used in `MC-359` and `MC-360`, now with `(2)`, gives

\[
\boxed{
I(X;Y)
\le
R q_R\,
\Phi\!\left(\frac{\mathfrak H_1}{R q_R}\right)
+
\frac{2(R-1)\log2}{m}.
}
\tag{4}
\]

Thus any independent information floor `I(X;Y)>=L_R` forces a quantitative Hellinger floor. Put

\[
c_R:=\frac{2(R-1)\log2}{m},
\qquad
 y_R:=
 \min\!\left\{
 \log2,
 \frac{[L_R-c_R]_+}{R q_R}
 \right\}.
\tag{5}
\]

Let `p(y)` be the unique number in `[0,1/2]` satisfying

\[
h(p(y))=\log2-y.
\tag{6}
\]

Then inversion of `(1)` gives

\[
\boxed{
\frac{\mathfrak H_1}{R}
\ge
q_R\left[
1-2\sqrt{p(y_R)(1-p(y_R))}
\right].
}
\tag{7}
\]

This strictly strengthens the TV-mediated conversion in `MC-362` away from the endpoints. Indeed the two classical inequalities used there give

\[
\operatorname{JS}(P,Q)
\le
(\log2)\operatorname{TV}(P,Q)
\le
(\log2)\sqrt{z(2-z)}.
\tag{8}
\]

Since `Phi(z)` is the sharp upper envelope of `JS` at fixed `z`,

\[
\Phi(z)
\le
(\log2)\sqrt{z(2-z)},
\tag{9}
\]

so inversion of `Phi` can only raise the Hellinger lower bound obtained from the same information floor.

At matched-filter energy, `MC-361` proves that

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon
\]

implies

\[
L_R=\log m-Rh(\varepsilon/2).
\tag{10}
\]

For fixed `0\le\varepsilon\le1` and even `R\to\infty`, `(5)` gives

\[
y_R\longrightarrow \log2-h(\varepsilon/2).
\]

Therefore `p(y_R)->\varepsilon/2`, and `(7)` yields the explicit asymptotic endpoint tariff

\[
\boxed{
\liminf_{R\to\infty,\ R\ \mathrm{even}}
\frac{\mathfrak H_1}{R}
\ge
1-\sqrt{2\varepsilon-\varepsilon^2}.
}
\tag{11}
\]

In particular, as `epsilon downarrow 0`,

\[
1-
\liminf\frac{\mathfrak H_1}{R}
\le
\sqrt{2\varepsilon-\varepsilon^2}
\sim\sqrt{2\varepsilon}.
\tag{12}
\]

This improves the `MC-362` deficit

\[
O\!\left(\sqrt{\varepsilon\log(1/\varepsilon)}\right)
\]

to the sharp affinity scale `O(sqrt(epsilon))` while preserving the Hellinger product decomposition of `MC-360`.

For the source-independent product architecture of `MC-360`, where

\[
\mathfrak H_1\le\mathfrak A_1
\le
q_R\sum_j\sum_{i\in A_j}\alpha_{j,i},
\tag{13}
\]

the same bound transfers immediately:

\[
\boxed{
\frac1R\sum_j\sum_{i\in A_j}\alpha_{j,i}
\ge
1-2\sqrt{p(y_R)(1-p(y_R))}.
}
\tag{14}
\]

Hence near-exact matched-filter-energy dephasing forces the total component source-incidence deficit to be at most `sqrt(2 epsilon)+o(1)`. Splitting the transcript into many weak product components cannot exploit the logarithmic slack left by the TV detour.

No estimate for `M(x)` follows. This remains a finite reciprocal-endpoint admission theorem. Its role is to make the bounded compositional Hellinger tariff quantitatively sharp at the near-deterministic endpoint; the unresolved arithmetic task is still to prove a source-natural upper bound for an actual Möbius-derived transcript architecture.

## 1. Posterior representation of both divergences

Let

\[
M:=\frac{P+Q}{2}.
\]

With respect to `M`, define the equal-prior posterior

\[
\Theta(y):=\frac{dP}{d(P+Q)}(y)\in[0,1].
\tag{15}
\]

Then the standard binary-channel identities are

\[
\operatorname{JS}(P,Q)
=\log2-\mathbf E_M h(\Theta),
\tag{16}
\]

and

\[
\operatorname{Aff}(P,Q)
=\mathbf E_M\,2\sqrt{\Theta(1-\Theta)}.
\tag{17}
\]

Put

\[
U:=2\sqrt{\Theta(1-\Theta)}\in[0,1]
\]

and define

\[
G(u)
:=
 h\!\left(
 \frac{1-\sqrt{1-u^2}}2
 \right).
\tag{18}
\]

By symmetry of binary entropy,

\[
h(\Theta)=G(U)
\]

pointwise. Thus the problem is exactly to lower-bound `E G(U)` at fixed `E U`.

## 2. Convexity gives the sharp BSC envelope

Let

\[
t:=\sqrt{1-u^2}.
\]

A direct differentiation gives, for `0<u<1`,

\[
\boxed{
G''(u)
=
\frac{\operatorname{artanh}(t)-t}{t^3}
\ge0,
}
\tag{19}
\]

with continuous limit `1/3` at `t=0`. The inequality follows because `artanh(t)>=t` on `[0,1)`. Hence `G` is convex.

Jensen applied to `(16)`--`(18)` therefore gives

\[
\mathbf E_M h(\Theta)
=\mathbf E_M G(U)
\ge
G(\mathbf E_M U)
=G(\operatorname{Aff}(P,Q)).
\tag{20}
\]

Subtracting from `log 2` proves `(2)`.

Equality in Jensen occurs exactly when `U` is constant almost surely, apart from degenerate endpoint cases. A binary symmetric channel with crossover probability `p` has posterior values `p` and `1-p`, so

\[
U=2\sqrt{p(1-p)}
\]

is constant and equality holds. Thus `(2)` is the sharp distribution-free relation at fixed affinity.

Since `G` is increasing and convex, `Phi(z)=log2-G(1-z)` is increasing and concave. These are exactly the shape properties needed for the cube aggregation.

## 3. Concavity survives the punctured-cube aggregation

Restore the full source cube as in `MC-359`--`MC-360` and extend the missing vertex by copying one neighboring transcript law. For each source direction, the bitwise conditional mutual-information term is a Jensen--Shannon divergence between two suffix mixtures.

Joint convexity of Jensen--Shannon divergence lets us pair the corresponding source edges, giving the edgewise bound

\[
I(U;Y)
\le
\frac2n
\sum_{e\in E(V)}
\operatorname{JS}(P_u,P_v).
\tag{21}
\]

Applying `(2)` to each edge gives

\[
I(U;Y)
\le
\frac2n
\sum_{e\in E(V)}
\Phi(z_e).
\tag{22}
\]

On puncturing, one restored edge has cost zero while each of the other `R-1` restored edges contributes at most `Phi(1)=log2`. As in `MC-359`, `I(U;Y)>=(m/n)I(X;Y)`. Hence

\[
I(X;Y)
\le
\frac2m
\sum_{e\in E(S)}\Phi(z_e)
+c_R.
\tag{23}
\]

The punctured cube has `R(m-1)/2` surviving edges. Concavity of `Phi` therefore gives

\[
\frac2m\sum_{e\in E(S)}\Phi(z_e)
\le
R q_R\,
\Phi\!\left(
\frac{\mathfrak H_1}{R q_R}
\right),
\tag{24}
\]

which proves `(4)`.

The order of the two concavity steps is important. We first use joint convexity of Jensen--Shannon divergence to reduce each conditional bit channel to actual source-edge pairs; only then do we apply the sharp one-dimensional `JS`--affinity envelope and average its Hellinger costs. No independence or product assumption is needed for `(4)`.

## 4. Inversion and comparison with MC-362

For `0<=y<=log2`, write `p(y)` as in `(6)`. Solving `(1)` gives

\[
\boxed{
\Phi^{-1}(y)
=1-2\sqrt{p(y)(1-p(y))}.
}
\tag{25}
\]

This proves `(7)` from `(4)`.

The previous `MC-362` route first converted the information floor to total variation and then used

\[
\operatorname{TV}(P,Q)
\le
\sqrt{H^2(P,Q)(2-H^2(P,Q))}.
\]

At the scalar level that is exactly the looser upper envelope on the right of `(9)`. Thus `MC-363` is not a different endpoint assumption: it is a strict tightening of the metric-conversion step using the same transcript information and the same edge laws.

The endpoint check is exact. If `y=log2`, then `p(y)=0` and `Phi^{-1}(y)=1`; mutually singular rows pay full Hellinger cost. If `y=0`, then `p(y)=1/2` and the lower bound vanishes.

## 5. General bounded-energy form

`MC-361` also supplies a non-asymptotic information floor for

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad
\tau:=\max\left\{\frac1m,\frac\eta{\sqrt C}\right\}:
\]

\[
L_R
:=
H(X)-R h\!\left(\frac{1+\tau}{2}\right).
\tag{26}
\]

Substituting this `L_R` into `(5)`--`(7)` gives a single bounded compositional tariff for the entire endpoint-energy curve. The matched-filter statement `(11)` is only its cleanest closed-form asymptotic specialization.

## Prior art and novelty boundary

The statistical/information-theoretic mechanism is classical. A targeted literature audit on 18 September 2026 found the relevant neighborhood in the classical theory of capacities, Bhattacharyya/Hellinger affinity, and inequalities among information divergences.

F. Topsøe, *Some inequalities for information divergence and related measures of discrimination*, IEEE Transactions on Information Theory **46** (2000), 1602--1609, DOI `10.1109/18.850703`, treats inequalities connecting capacitory discrimination (equal-prior Jensen--Shannon divergence), Hellinger distance, triangular discrimination, and related `f`-divergences. E. Arıkan, *Channel polarization: A method for constructing capacity-achieving codes for symmetric binary-input memoryless channels*, IEEE Transactions on Information Theory **55** (2009), 3051--3073, arXiv `0807.3917`, uses the Bhattacharyya parameter as a binary-channel reliability coordinate and records the standard capacity bounds in that parameter. The broader coding literature also treats the binary symmetric and erasure channels as extremal representatives for multiple BMS-channel functionals.

No novelty is claimed for the abstract envelope `(2)`, binary posterior representation, Jensen's inequality, Bhattacharyya parameter, or BSC extremality. The proof is included in full, so no external theorem is load-bearing. The durable Mathia-specific delta is the insertion of the sharp affinity envelope into the already-derived punctured reciprocal source-edge tariff, producing `(7)` and the endpoint law `(11)` while retaining the product/latent Hellinger architecture bound of `MC-360`.

## Boundaries and falsification tests

- **Even rank is load-bearing for the displayed punctured-cube aggregation.** Odd rank has the parity-constrained source image and requires the corresponding pair-flip aggregation rather than silently importing `(4)`.
- **The complete transcript laws must be used.** Hellinger costs of a downstream statistic cannot be substituted unless the complete transcript genuinely factors through that statistic.
- **The envelope is sharp only at fixed affinity.** It does not make Hellinger sufficient for dephasing; it only gives the strongest Jensen--Shannon upper bound available from that one scalar distance.
- **Product compositionality still requires a genuine architecture.** The transfer to `mathfrak A_1` inherits the latent/product hypotheses of `MC-360`; an artificial refactorization does not supply an arithmetic upper theorem.
- **Near-maximal Hellinger is necessary, not sufficient.** A channel can pay the required source-edge distance without implementing the desired coefficient map.
- **Analog precision remains outside this metric.** As in `MC-359`--`MC-362`, distributional distinguishability does not by itself price arbitrarily precise deterministic transcript values.
- **No arithmetic upper bound is supplied.** The decisive next step is unchanged in kind: expose a concrete Möbius-derived transcript and prove that its native source-edge Hellinger/affinity incidence is subcritical, or identify the component that necessarily pays the tariff.
- **No RH input is used.** The derivation is finite and information-theoretic; it uses no `1/zeta`, contour shift, zero-free region, or RH-scale estimate for `M(x)`.

## Consequence for the research line

The generic metric-conversion problem is now quantitatively closed at the even-rank reciprocal endpoint. `MC-359` supplied bounded endpoint-sharp total variation, `MC-360` supplied compositional Hellinger affinity, `MC-361` supplied the sharp binary-source information floor, and `MC-362` joined those pieces with a nonoptimal TV-to-Hellinger conversion. The direct sharp envelope above removes that last logarithmic loss.

Further generic work on replacing one bounded statistical distance by another is unlikely to move the frontier. The useful next result must be **architecture-specific**: an upper theorem for the actual arithmetic transcript in Hellinger/affinity currency, or a proof that one concrete source-dependent component already carries the near-maximal cost forced by `(11)`.