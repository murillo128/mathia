# WI-057 — ordinary MRT does not control the `W`-local-conditioned pair covariance

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + NEEDS-AUDIT`. This finding does **not** refute the Yang--Yang one-sided fourth-moment candidate, does not weaken WI-054's doubly-small Shao--Teräväinen region, and does not change Mathia's current unconditional simple-critical proportion. It closes a narrower repair route explicitly left open in WI-054 §6: one cannot extend the Shao--Teräväinen-controlled region from the intersection

\[
4\alpha+\beta<1,
\qquad
\alpha+4\beta<1
\]

to the one-sided union merely by putting the small-coefficient pair into the Shao--Teräväinen `W`-local all-main model and invoking the **ordinary unweighted Matomäki--Radziwiłł--Tao pair-discrepancy theorem** on the other pair.

The obstruction is already present in the exact local prime factor at `p=2`. A `W`-local all-main pair carries nonconstant periodic residue modes. An opposite pair error may have uniformly `O(1)` discrepancy on every interval — much stronger marginal information than MRT supplies — while correlating linearly with one of those modes. Thus the required one-sided bridge is a **conditioned/twisted pair-correlation theorem** (or an exact source identity removing those modes before estimation), not ordinary marginal MRT. WI-049's genuine four-form local-main centering explains where these periodic modes belong in the deterministic bookkeeping, but it does not by itself supply the analytic orthogonality of the actual prime-pair error to the same local sigma-algebra.

## 1. Exact source interface

The two primary inputs are:

- Xuancheng Shao and Joni Teräväinen, *The Bombieri--Vinogradov theorem for nilsequences*, Discrete Analysis 2021:21, arXiv:2006.05954v2, DOI `10.19086/da.29048`.
- Kaisa Matomäki, Maksym Radziwiłł and Terence Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. LMS 118 (2019), 284--350, arXiv:1707.01315v3, DOI `10.1112/plms.12181`.

Shao--Teräväinen Theorem 1.3 compares `Lambda` on a progression to the explicit `W`-local model

\[
\frac{dW}{\varphi(dW)}1_{(n,W)=1},
\qquad
W=\prod_{p\le (\log x)^C}p,
\tag{1}
\]

and takes the supremum over bounded-complexity nilsequences **inside** the modulus sum. WI-054 uses that source-faithful interface plus Parseval to show that a single controlled residual leg kills the entire localized pair-frequency fiber.

MRT, on the other hand, controls the ordinary shifted-prime pair discrepancy

\[
D_Y(h)
:=
\sum_{Y<n\le2Y}\Lambda(n)\Lambda(n+h)
-\mathfrak S(h)Y
\tag{2}
\]

for almost all long shifts, and WI-034/WI-041 derive the corresponding structured/maximal `L^2` consequences. This is a **marginal pair theorem**: its main is the shift singular series after averaging over the base variable `n`.

The one-sided extension suggested but not established in WI-054 would need to control a term schematically of the form

\[
\sum_n M_{W,r,k}(n)\,B_{qk}(n),
\tag{3}
\]

where `M_{W,r,k}` is produced by the all-main `W`-local pair on the Shao--Teräväinen-controlled side and `B_{qk}` is the centered pair error on the other side. Equation (3) is **not** an unweighted interval sum of `B_{qk}`.

## 2. The `W`-local main contains genuine periodic modes

MRT itself writes the local von-Mangoldt component at a prime `p` as

\[
\Lambda_p(n)
=
\frac{p}{p-1}1_{p\nmid n}.
\tag{4}
\]

The finite `W`-local model in (1) is the product of these small-prime coprimality factors, up to the progression normalization. Therefore it is enough to inspect one local factor.

Take `p=2`. Then

\[
L(n):=\Lambda_2(n)
=2\,1_{n\text{ odd}}
=1-(-1)^n.
\tag{5}
\]

For an even shift `h`,

\[
L(n)L(n-h)
=4\,1_{n\text{ odd}}
=2-2(-1)^n.
\tag{6}
\]

Its average over one period is `2`, but its centered part is the nonzero parity mode

\[
\boxed{
C_h(n):=L(n)L(n-h)-2=-2(-1)^n.
}
\tag{7}
\]

Thus replacing the controlled prime pair by its exact `W`-local all-main model does **not** replace it by a constant weight. It leaves deterministic residue-class frequencies.

The same statement holds at every local prime. If `p|h`, then from (4)

\[
P_{p,h}(n):=\Lambda_p(n)\Lambda_p(n-h)
=
\left(\frac p{p-1}\right)^2 1_{p\nmid n},
\tag{8}
\]

whose period mean is `p/(p-1)`. The centered local mode is

\[
C_{p,h}(n)
=
\begin{cases}
\dfrac{p}{(p-1)^2},&p\nmid n,\\[2mm]
-\dfrac{p}{p-1},&p\mid n,
\end{cases}
\tag{9}
\]

and has strictly positive period energy

\[
\boxed{
\mathbb E_{n\bmod p}|C_{p,h}(n)|^2
=
\frac{p^2}{(p-1)^3}>0.
}
\tag{10}
\]

So the phenomenon is not peculiar to parity; parity is simply the smallest exact witness.

## 3. Exact no-go: arbitrarily strong marginal interval discrepancy does not control (3)

Fix `0<eta<1` and define one positive bounded base sequence

\[
a_n=1+\eta(-1)^n>0.
\tag{11}
\]

For every even shift `h'`,

\[
a_na_{n-h'}
=1+\eta^2+2\eta(-1)^n.
\tag{12}
\]

Center at its exact period mean

\[
\mu_{h'}=1+\eta^2,
\qquad
B_{h'}(n):=a_na_{n-h'}-\mu_{h'}=2\eta(-1)^n.
\tag{13}
\]

For **every** integer interval `I`,

\[
\boxed{
\left|\sum_{n\in I}B_{h'}(n)\right|
\le 2\eta.
}
\tag{14}
\]

This is far stronger than an MRT-style `o(Y)` or logarithmically saving marginal discrepancy on intervals of length `Y`.

Nevertheless, pair (13) with the exact `p=2` all-main local mode (7). On an interval of length `Y`,

\[
\begin{aligned}
\sum_n C_h(n)B_{h'}(n)
&=
\sum_n
\bigl(-2(-1)^n\bigr)
\bigl(2\eta(-1)^n\bigr)\\
&=
\boxed{-4\eta Y+O(1)}.
\end{aligned}
\tag{15}
\]

Even if one keeps the **uncentered** local pair (6), its constant part contributes only `O(1)` by (14), so

\[
\boxed{
\sum_n L(n)L(n-h)B_{h'}(n)
=-4\eta Y+O(1).
}
\tag{16}
\]

Equations (14)--(16) prove the information-theoretic obstruction:

\[
\boxed{
\text{all-main `W`-local pair}
+
\text{arbitrarily small marginal interval discrepancy}
\not\Rightarrow
\text{small locked covariance}.
}
\tag{17}
\]

The example uses one positive bounded base sequence for the opposite pair, so it is not an artifact of choosing an unrelated adversarial error vector.

## 4. Why this does not contradict WI-049

The parity term in (15) is exactly the kind of deterministic local interaction that a genuine four-form Hardy--Littlewood main must know about. WI-049 proves, for the actual Yang locked four-form system, that the true local factor centers cellwise over the shift and that the full finite-conductor/full-Euler deterministic main has `o(1)` normalized bias after the source aggregation.

Therefore (15) must **not** be read as evidence that the real Yang remainder contains a parity-sized main. Its role is different: it shows that ordinary MRT's marginal centering (2) is too coarse an interface for the proposed one-sided splice. If one first averages over the base variable and retains only `mathfrak S(h)`, the local residue modes have disappeared from the theorem statement even though an all-main `W`-local weight on the other side can still see them.

A valid one-sided proof must consequently do one of the following before invoking a marginal pair estimate:

1. subtract the genuine four-form local main at a sufficiently **conditioned/residue-resolved** level so that the remaining large-side pair error is orthogonal to every `W`-local mode that the small side can carry;
2. prove a **twisted/conditioned MRT theorem** controlling the pair discrepancy against those local periodic/Ramanujan modes;
3. derive an exact Yang `S1-2S2+S3` identity that cancels these modes before estimation; or
4. use a genuinely joint prime theorem, rather than ordinary two-point MRT, on the remaining locked covariance.

WI-049 settles the deterministic local-main identity. It does not by itself prove item 1 for the **analytic prime error** after the source's `W`-local decomposition.

## 5. Consequence for the WI-054 power region

WI-054 remains unchanged on the doubly-small region

\[
4\alpha+\beta<1,
\qquad
\alpha+4\beta<1.
\tag{18}
\]

There every non-all-main term has at least one Shao--Teräväinen-controlled residual leg, and the exact fiber/Parseval estimate kills the complete frequency sum. The all-main term is explicitly left to the deterministic `W`-local/full-local-main splice.

What is now ruled out is the **black-box** enlargement

\[
(4\alpha+\beta<1)
\ \text{or}\ 
(\alpha+4\beta<1)
\tag{19}
\]

obtained solely by saying: “use WI-054 on the small side, then ordinary MRT on the other all-main pair.” The other pair must be controlled **conditioned on the local modes carried by the first all-main pair**, not merely in the unweighted norm of WI-034/WI-041.

This is stronger than WI-043's earlier warning. WI-043 showed that two marginal pair-discrepancy processes can have a large locked covariance. Here one side has already been replaced by the **specific local-main structure used by Shao--Teräväinen**, and the obstruction still survives unless the other side is conditioned/twisted accordingly.

## 6. Prior-art and novelty audit

No novelty is claimed for the local component (4), the parity calculation, periodic Fourier modes, or the general principle that small interval discrepancy does not imply orthogonality to a fixed periodic weight. These are elementary/classical facts.

The source-backed pieces are:

- Shao--Teräväinen Theorem 1.3 supplies the explicit `W`-local main and the modulus-wise nilsequence-uniform residual used in WI-054.
- MRT Theorem 1.3(i) supplies the unweighted shifted-prime asymptotic for almost all long shifts; WI-034/WI-041 derive the `L^2` and maximal-interval forms used elsewhere in this line.
- MRT's local-factor discussion writes `Lambda_p(n)=p/(p-1) 1_(p does not divide n)` and expresses the twin-prime singular series as the product of two-form local expectations, matching the local model used in (4)--(10).

A targeted prior-art search located many results on pair correlations, Bombieri--Vinogradov distribution and nilsequence twists, but no theorem in the **cited Yang/MRT chain** that states the residue-conditioned/twisted pair estimate required above. This absence is not a priority claim and does not assert that no such theorem can be derived by extending the MRT circle method.

The Mathia contribution is the interface-level no-go: specialize the exact Shao--Teräväinen local main to a single local prime, exhibit a positive same-base pair process satisfying dramatically stronger marginal interval cancellation than MRT, and show that their locked covariance is nevertheless linear in the interval length. This converts WI-054's vague “one-sided extension may be possible” into a precise additional theorem obligation.

## 7. Decisive falsification / narrowing gate

Narrow or retire this finding if a primary/source-faithful argument supplies all of the following.

1. A decomposition of the one-sided all-main Yang term **after** the genuine WI-049 four-form local main is removed, not merely after subtracting the ordinary pair singular series.
2. A theorem controlling the remaining large-side pair error against every local periodic/Ramanujan mode produced by the source `W`-model, with uniformity sufficient for `W=P((log x)^C)` and the relevant moving interval/lock geometry.
3. The exact modulus, shift-range, Mertens-weight and boundary inequalities needed in the one-sided power-coefficient region.
4. No across-family Cauchy--Schwarz step that reintroduces the Poisson floor already isolated in WI-042.

An exact source identity annihilating the local-mode projection before any analytic estimate would also retire the obstruction.

Conversely, merely quoting ordinary MRT pair discrepancy, even in the maximal form of WI-041, cannot satisfy this gate because (14)--(16) are an exact counterexample to that information interface.

## 8. Consequence for `weil_inertia`

The live welding problem is narrowed again. The established route remains

\[
\text{exact local four-form main (WI-049)}
\to
\text{two-sided ST fiber control on (18) (WI-054)}
\to
\text{uncontrolled complementary power region}.
\]

For a one-sided extension, the next credible target is no longer “combine ST with MRT” in the abstract. It is the sharper statement

\[
\boxed{
\text{prove `W`-local-conditioned/twisted shifted-prime control}
\quad\text{or}\quad
\text{derive exact pre-estimate cancellation of those local modes}.
}
\tag{20}
\]

Until such an input is supplied, the one-sided union (19) is not an established analytic region and the Yang `0.6916` candidate remains below Mathia's evidence threshold.