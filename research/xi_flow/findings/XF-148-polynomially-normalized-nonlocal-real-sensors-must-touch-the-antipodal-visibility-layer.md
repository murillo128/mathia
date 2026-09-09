# XF-148 — polynomially normalized nonlocal real sensors must touch the antipodal visibility layer

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/NONLOCAL-REAL-SENSOR-CONDITIONING` + `MATCHED-CONTROL` + `UNIT-CIRCLE-ADMISSIBLE` + `REAL-AXIS-OBSERVATION` + `TRANSITION-TIME` + `SHARP-SUPPORT-THRESHOLD`. XF-147 leaves one target-side escape deliberately open: a sparse or disconnected nonlocal observation might reach the near-antipodal region without scanning the whole real interval. For the same maximal-contact pair, the exact pointwise envelope resolves the geometric part of that question. Probe density, disconnectedness, and arbitrarily long heat time do not matter at the exponential scale: what matters is the closest spatial approach of the observation support to the antipodal point. Polynomially many bounded linear sensors with polynomially bounded weights cannot aggregate away this barrier.

## Claim

Use the maximal-contact matched pair of XF-141--XF-147,

\[
R_1(x,s),\qquad R_{\lambda_\rho}(x,s),
\tag{1}
\]

with fixed `rho>0` and

\[
\Lambda_{\rm per}(E_1)=0,
\qquad
\Lambda_{\rm per}(E_{\lambda_\rho})=-\rho.
\tag{2}
\]

Write the real period as the circle

\[
\mathbb T_L:=\mathbb R/L\mathbb Z
\]

and let `x_anti=L/2 mod L` be the antipodal point to the center `x=0`. For an arbitrary nonempty **predetermined** space-time observation set

\[
\Omega_N\subset \mathbb T_L\times[0,\infty),
\tag{3}
\]

define its antipodal reach by

\[
d_N:=
\inf_{(x,s)\in\Omega_N}
\operatorname{dist}_{\mathbb T_L}(x,x_{\rm anti})
\in[0,L/2]
\tag{4}
\]

and

\[
B_N:=\max\!\left\{
\frac12,
\cos\frac{\pi d_N}{L}
\right\}.
\tag{5}
\]

Then the complete raw-trace separation on that geometry satisfies

\[
\boxed{
\sup_{(x,s)\in\Omega_N}
|R_1(x,s)-R_{\lambda_\rho}(x,s)|
\le 4 B_N^{N-2}.
}
\tag{6}
\]

Thus arbitrary sparse, disconnected, multitime, or moving-probe observation geometry inherits the same exponential blindness whenever all of its spatial support stays a fixed positive distance from the antipode. In particular, if `d_N/L >= delta>0`,

\[
\liminf_{N\to\infty}
-\frac1N
\log
\sup_{\Omega_N}|R_1-R_{\lambda_\rho}|
\ge
\min\!\left\{
\log2,
-\log\cos(\pi\delta)
\right\}.
\tag{7}
\]

The statement persists after polynomially normalized nonlocal linear sensing. Let `mu_{j,N}`, `1<=j<=m_N`, be finite complex Borel measures supported on `Omega_N`, and define

\[
\mathcal O_N(R)
:=
\left(
\int_{\Omega_N} R\,d\mu_{j,N}
\right)_{j=1}^{m_N}.
\tag{8}
\]

If

\[
W_N:=\max_j\|\mu_{j,N}\|_{\rm TV},
\tag{9}
\]

then

\[
\boxed{
\|\mathcal O_N(R_1)-\mathcal O_N(R_{\lambda_\rho})\|_{\ell^2}
\le
4\sqrt{m_N}\,W_N B_N^{N-2}.
}
\tag{10}
\]

Consequently every decoder `F_N` that recovers `Lambda_per` on both matched controls and is Lipschitz in this observation norm has condition number `K_N` satisfying

\[
\boxed{
K_N
\ge
\frac{\rho}
{4\sqrt{m_N}\,W_N B_N^{N-2}}.
}
\tag{11}
\]

If `m_N` and `W_N` grow at most polynomially, then the only way this family stops forcing superpolynomial conditioning is for the support itself to enter the near-antipodal layer

\[
\boxed{
d_N
=O\!\left(
L\sqrt{\frac{\log N}{N}}
\right).}
\tag{12}
\]

More precisely, when `d_N/L -> 0`,

\[
\log K_N
\ge
\left(\frac{\pi^2}{2}+o(1)\right)
\frac{N d_N^2}{L^2}
-O(\log N),
\tag{13}
\]

so

\[
\frac{N d_N^2}{L^2\log N}\longrightarrow\infty
\tag{14}
\]

forces superpolynomial transition conditioning.

For this matched pair the spatial scale is sharp at the raw-trace level whenever the initial slice is actually sampled. At a point whose circle distance from the antipode is `d`, XF-147 gives exactly

\[
|R_1(x,0)-R_{\lambda_\rho}(x,0)|
=
2(1-\lambda_\rho)
\cos\!\left(\frac{\pi d}{L}\right)^{N-2}.
\tag{15}
\]

Hence the antipode itself has order-one pairwise separation at `s=0`, while

\[
d_N=C L\sqrt{\frac{\log N}{N}}
\tag{16}
\]

gives

\[
|R_1-R_{\lambda_\rho}|
=
N^{-\pi^2C^2/2+o(1)}
\tag{17}
\]

at the deepest initial-slice point. Thus `(12)` is not merely an artifact of the upper bound: it is the exact support scale where this particular adversary changes from superpolynomial to polynomial raw-trace visibility.

## 1. Arbitrary observation geometry collapses to nearest antipodal reach

XF-147 proves the pointwise all-future envelope

\[
|R_1(x,s)-R_{\lambda_\rho}(x,s)|
\le
4e^{-(N-1)as}
\max\!\left\{
2^{-(N-2)},
\left|\sin\frac{\pi x}{L}\right|^{N-2}
\right\}.
\tag{18}
\]

The heat factor is at most one. On the real circle, if

\[
d(x):=\operatorname{dist}_{\mathbb T_L}(x,x_{\rm anti}),
\]

then exactly

\[
\left|\sin\frac{\pi x}{L}\right|
=
\cos\frac{\pi d(x)}{L}.
\tag{19}
\]

Every point of `Omega_N` has `d(x)>=d_N`, and cosine is decreasing on `[0,pi/2]`. Therefore

\[
\left|\sin\frac{\pi x}{L}\right|
\le
\cos\frac{\pi d_N}{L}.
\tag{20}
\]

Substitution into `(18)` proves `(6)` immediately.

This proof uses no connectedness, sampling density, cardinality, or time-window hypothesis. A finite cloud of probes, a union of disjoint arcs, a moving curve, or the complete future history of any such predetermined set all have the same ceiling if their closest spatial reach `d_N` is the same. For the centered strip of XF-147, `d_N/L=1/2-c`; its crossover `c=1/6` is exactly the present threshold `d_N/L=1/3`, where `cos(pi d_N/L)=1/2`.

## 2. Polynomial sensor multiplicity and weighting cannot buy back the exponential loss

For one finite complex measure supported on `Omega_N`, total variation gives

\[
\left|
\int(R_1-R_{\lambda_\rho})\,d\mu
\right|
\le
\|\mu\|_{\rm TV}
\sup_{\Omega_N}|R_1-R_{\lambda_\rho}|.
\tag{21}
\]

Combining `(21)` with `(6)` and then taking the Euclidean norm over `m_N` sensors proves `(10)`. Since the two controls have transition times separated by `rho`, any Lipschitz inverse must satisfy

\[
\rho
\le
K_N
\|\mathcal O_N(R_1)-\mathcal O_N(R_{\lambda_\rho})\|_{\ell^2},
\]

which is `(11)`.

If `m_N<=N^A` and `W_N<=N^B`, their entire contribution to `log K_N` is only `O(log N)`. They therefore cannot compensate a `B_N^{N}` loss. When `d_N/L -> 0`,

\[
-\log\cos z=\frac{z^2}{2}+O(z^4),
\tag{22}
\]

so `(11)` gives `(13)` and `(14)`. This makes the normalization issue explicit: exponentially large sensor weights could trivially amplify the matched difference, but that amplification is itself an exponentially ill-conditioned preconditioning step and lies outside the polynomially normalized observation class.

The same pointwise statement can also be read in `ell^infinity` over any number of probes, even a continuum: cardinality then contributes nothing at all. The `sqrt(m_N)` factor in `(10)` is only the price of aggregating polynomially many coordinates in `ell^2`.

## 3. The support threshold is sharp for the matched pair, not a sufficiency theorem for Lambda

At `s=0`, XF-147 has the exact identity `(15)`, and for fixed `rho>0` its matching parameter satisfies `lambda_rho<=exp(-a(N-1)rho)`. Hence `1-lambda_rho=1+o(1)`. Expanding `log cos` at a point with `d_N/L -> 0` gives

\[
\log |R_1-R_{\lambda_\rho}|
=
-\frac{\pi^2}{2}\frac{N d_N^2}{L^2}
+O\!\left(
\frac{N d_N^4}{L^4}+1
\right).
\tag{23}
\]

Equation `(17)` follows at the critical `sqrt(log N/N)` scale. Therefore a sparse sensor does **not** need to scan almost the whole period to defeat this particular pair: one raw initial-slice sample placed inside the visibility layer is enough to make the pairwise separation merely polynomial, and the exact antipodal sample makes it order one.

That is only a falsification boundary for the maximal-contact adversary. It does not prove that near-antipodal access stably determines `Lambda_per` on a broader admissible class, much less that an analogous observable is available source-faithfully for Xi. A different matched family could remain blind there. The theorem therefore identifies the minimum spatial reach required to escape this obstruction, not a reconstruction theorem.

## 4. Prior-art and boundary audit

The broad phenomenon that sparse or finite observation sets can still norm finite-dimensional polynomial or exponential-polynomial spaces is classical. Y. Yomdin, *Remez-type inequality for discrete sets*, Israel J. Math. 186 (2011), 45--60, DOI `10.1007/s11856-011-0131-4`, replaces positive measure by a geometric invariant that may remain nonzero for finite sets. O. Friedland and Y. Yomdin, *An observation on the Turan--Nazarov inequality*, Studia Math. 218 (2013), 27--39, gives an analogous metric-entropy refinement for exponential polynomials. Those results are useful prior-art controls here: mere discreteness or small measure of an observation set is not itself an obstruction to state recovery.

No external theorem is load-bearing in `(6)`--`(23)`. The new statement is the specialization of the exact XF-147 matched-pair envelope to arbitrary observation support and bounded linear functionals, where transition conditioning depends on nearest antipodal reach rather than on connected aperture. Therefore no new `SOURCES.md` dependency is required, and no novelty claim is made for Remez/Turan--Nazarov norming theory itself.

The result is deliberately restricted in four ways. First, it concerns the **raw real heat trace**; the logarithmic/reference quotient cannot be extended blindly across a macroscopic circle containing zeros of the common carrier. Second, `(8)` covers finite-measure linear sensors, not derivative evaluations or other distributional functionals. Third, the polynomial-conditioning conclusion assumes polynomial sensor count and total-variation normalization; exponentially many coordinates or exponentially large weights require their own cost model. Fourth, `Omega_N` is fixed independently of which member of the matched pair generated the data. A genuinely data-adaptive sensing policy whose future support diverges between the two inputs is a different observation model and is not claimed here.

## Research implication

XF-147 showed that a contiguous centered scan has to approach the antipode before polynomial transition visibility is even possible. XF-148 shows that **sparsity and nonlocality do not evade that geometry by themselves**. A target-side raw real observable built from polynomially many polynomially normalized finite-measure sensors must actually place support inside the `L sqrt(log N/N)` antipodal layer; adding probes elsewhere, disconnecting the support, or observing for all future heat time cannot compensate.

This narrows the next target-side question to source-faithful access rather than generic tomography: can an Xi-derived observable genuinely sample or weight that visibility layer without reintroducing a global inverse problem or an exponentially normalized functional? If not, the remaining escape is source-side—prove that the Xi heat flow excludes the maximal-contact packet or an equivalent transition-sharp direction.