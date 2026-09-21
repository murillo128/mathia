# PL-405 — The PL-404 singular-series source is a critical infinite-energy Ramanujan covariance

**Evidence/status:** `EXACT-DERIVED + LITERATURE-BASED + SOURCE-IDENTIFICATION + PRIOR-ART-REDIRECT + CRITICAL-ENERGY-OBSTRUCTION`.

**Parent findings:** `PL-403`, `PL-404`.

## Claim

The Hardy--Littlewood pair singular series inserted as the arithmetic source in `PL-403`--`PL-404` is not an arbitrary local-density model from the point of view of harmonic analysis. It is exactly the formal Ramanujan power spectrum of Hardy's modified von Mangoldt function

\[
\Lambda_1(n):=\frac{\phi(n)}n\Lambda(n),
\]

whose classical Ramanujan expansion is

\[
\Lambda_1(n)
=\sum_{q\ge1}\frac{\mu(q)}{\phi(q)}c_q(n).
\tag{1}
\]

For the finite spectral truncation

\[
L_Q(n):=\sum_{q\le Q}\frac{\mu(q)}{\phi(q)}c_q(n),
\tag{2}
\]

Ramanujan orthogonality gives the exact Cesaro covariance identity

\[
\boxed{
\lim_{X\to\infty}\frac1X\sum_{n\le X}
L_Q(n)L_Q(n+h)
=
\mathfrak S_Q(h)
:=\sum_{q\le Q}
\frac{\mu(q)^2}{\phi(q)^2}c_q(h).
}
\tag{3}
\]

For every fixed nonzero integer `h`, the right side converges absolutely as `Q -> infinity` to the standard Hardy--Littlewood pair singular series

\[
\boxed{
\mathfrak S(h)
=\sum_{q\ge1}\frac{\mu(q)^2}{\phi(q)^2}c_q(h).
}
\tag{4}
\]

This harmonic identification is classical prior art: Gadiyar--Padma explicitly used (1), Wiener--Khintchine, and (4) in their prime-pair program. The important line-specific point is what happens at the endpoint needed to replace the `PL-404` model source by actual prime data.

The spectrum in (1) is **not finite-energy**. At lag zero,

\[
\mathfrak S_Q(0)
=\sum_{q\le Q}\frac{\mu(q)^2}{\phi(q)}
\sim\log Q,
\tag{5}
\]

and independently

\[
\frac1X\sum_{n\le X}|\Lambda_1(n)|^2
\sim\log X.
\tag{6}
\]

Thus `Lambda_1` does not belong to the ordinary finite-energy Besicovitch `B^2` class in which Parseval/Wiener--Khintchine would justify passage from (1) to the autocorrelation of the actual arithmetic function. This is the analytic obstruction behind the limit interchange that Gadiyar--Padma explicitly leave unjustified.

There is a canonical way to approach the endpoint from inside `B^2`. For every `delta>0`, define

\[
L_\delta(n)
:=\sum_{q\ge1}
\frac{\mu(q)}{\phi(q)q^\delta}c_q(n).
\tag{7}
\]

Then `L_delta` is a genuine `B^2` Ramanujan series and

\[
\boxed{
\lim_{X\to\infty}\frac1X\sum_{n\le X}
L_\delta(n)L_\delta(n+h)
=
\mathfrak S_\delta(h)
:=\sum_{q\ge1}
\frac{\mu(q)^2}{\phi(q)^2q^{2\delta}}c_q(h).
}
\tag{8}
\]

Its spectral energy is

\[
E(\delta)
:=\sum_{q\ge1}\frac{\mu(q)^2}{\phi(q)q^{2\delta}}
\sim\frac1{2\delta}
\qquad(\delta\downarrow0).
\tag{9}
\]

For every fixed `h != 0`, meanwhile,

\[
\mathfrak S_\delta(h)\longrightarrow\mathfrak S(h)
\qquad(\delta\downarrow0).
\tag{10}
\]

So the source of `PL-404` is the **off-diagonal critical boundary** of a rigorous finite-energy covariance family, while the diagonal energy diverges exactly when the regulator is removed.

For the shifted Abel weight already fixed in `PL-404`,

\[
w_\eta^{[2]}(u)
=u e^{-\eta u^3}\sin(\pi u^3/6),
\]

put

\[
A_{\eta,\delta}^{[2]}(H)
:=\frac1H\sum_{d\ge1}
\mathfrak S_\delta(d)w_\eta^{[2]}(d/H).
\tag{11}
\]

For every fixed `delta>0`, (8) and absolute summability of the `d`-weight give the exact harmonic realization

\[
\boxed{
A_{\eta,\delta}^{[2]}(H)
=
\lim_{X\to\infty}\frac1X\sum_{n\le X}
L_\delta(n)
\left[
\frac1H\sum_{d\ge1}
w_\eta^{[2]}(d/H)L_\delta(n+d)
\right].
}
\tag{12}
\]

Moreover, for every fixed `H`,

\[
A_{\eta,\delta}^{[2]}(H)
\longrightarrow
A_\eta^{[2]}(H)
\qquad(\delta\downarrow0),
\tag{13}
\]

where `A_eta^[2]` is exactly the singular-series source entering `PL-404`. Thus the remaining arithmetic bridge can be stated as a **joint critical-endpoint problem** rather than as the vague task of somehow deriving the singular series from prime data: one must remove the Ramanujan spectral regulator while controlling an actual arithmetic correlation, uniformly strongly enough in the growing cubic scale `H` to preserve the `H^-7/4` zero-sensitive layer of `PL-404`.

This does **not** prove such a bridge. In particular, (12) is a covariance theorem for the regulated Ramanujan function `L_delta`, not for `Lambda_1`. The fixed-shift identity obtained by formally putting `delta=0` and replacing `L_delta` by `Lambda_1` is already the classical Hardy--Littlewood prime-pair difficulty.

## 1. Finite Ramanujan truncations give the singular series exactly

Write

\[
c_q(n)=\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}
e^{2\pi ian/q}.
\]

For fixed `q,r,h`, ordinary periodic Fourier orthogonality gives

\[
\lim_{X\to\infty}\frac1X\sum_{n\le X}
c_q(n)c_r(n+h)
=
\mathbf 1_{q=r}\,c_q(h).
\tag{14}
\]

Since (2) is finite, inserting it twice and using (14) proves (3) with no convergence issue.

For fixed `h != 0`, the series in (4) is absolutely convergent. Because `mu(q)^2` restricts to square-free `q`, its local factors are

\[
1+\frac{c_p(h)}{(p-1)^2}.
\]

If `p` does not divide `h`, then `c_p(h)=-1`, giving an `O(p^-2)` perturbation; only finitely many primes divide `h`. Hence the Euler product converges absolutely. At `delta=0`, the `p=2` factor kills odd `h`, and for even `h` the remaining factors are exactly the standard Hardy--Littlewood pair singular series.

This is the precise sense in which the `mathfrak S(d)` used in `PL-404` is a Ramanujan spectral covariance: it is the `Q -> infinity` limit of exact finite-dimensional covariance kernels away from the diagonal.

## 2. The endpoint has logarithmically infinite energy

At zero lag, `c_q(0)=phi(q)`, so (3) becomes

\[
\|L_Q\|_{B^2}^2
=\sum_{q\le Q}\frac{\mu(q)^2}{\phi(q)}.
\tag{15}
\]

Consider

\[
D(s)
:=\sum_{q\ge1}\frac{\mu(q)^2}{\phi(q)q^s}
=\prod_p\left(1+\frac{p^{-s}}{p-1}\right).
\tag{16}
\]

Factor

\[
D(s)=\zeta(s+1)G(s),
\]

with

\[
G(s)
:=\prod_p
\left(1+\frac{p^{-s}}{p-1}\right)
\left(1-p^{-s-1}\right).
\tag{17}
\]

The local factor in (17) is

\[
1+\frac{p^{-s}-p^{-2s}}{p(p-1)},
\]

so the product is analytic in a neighborhood of `s=0` and

\[
G(0)=1.
\]

Thus `D(s)` has a simple pole at `s=0` with residue `1`, and the standard Tauberian consequence for its nonnegative coefficients is (5).

The arithmetic function itself has the same energy divergence. Since `Lambda_1` is supported on prime powers and

\[
\Lambda_1(p^k)=(1-p^{-1})\log p,
\]

PNT and partial summation give

\[
\sum_{p\le X}(1-p^{-1})^2(\log p)^2
\sim X\log X,
\]

while prime powers with `k>=2` contribute `o(X log X)`. Dividing by `X` gives (6).

Consequently there is no ordinary finite `B^2` norm for the critical function. The failure is not merely that the Ramanujan expansion is inconveniently conditional: its formal spectral energy and the actual arithmetic mean-square both diverge on the same logarithmic scale.

## 3. A positive spectral regulator makes Wiener--Khintchine rigorous

For `delta>0`, Ramanujan orthogonality gives

\[
\|L_\delta\|_{B^2}^2
=
\sum_{q\ge1}\phi(q)
\left|\frac{\mu(q)}{\phi(q)q^\delta}\right|^2
=E(\delta)<\infty.
\tag{18}
\]

Therefore the series (7) converges in `B^2`, and continuity of translations and of the `B^2` inner product proves (8). No Hardy--Littlewood conjecture is being used here.

Equation (16) also gives

\[
E(\delta)=D(2\delta)
\sim\frac1{2\delta},
\]

which proves (9). The endpoint is therefore quantitatively singular, not merely excluded by a technical hypothesis.

For fixed nonzero `h`, the local Euler factors of `mathfrak S_delta(h)` are

\[
1+\frac{c_p(h)}{(p-1)^2p^{2\delta}}.
\tag{19}
\]

They converge absolutely even at `delta=0`, so dominated convergence proves (10). More usefully for the `d`-average, for all `delta>=0`,

\[
0\le \mathfrak S_\delta(d)
\le \prod_{p\mid d}\left(1+\frac1{p-1}\right)
=\frac d{\phi(d)}.
\tag{20}
\]

The cubic Abel factor in `w_eta^[2](d/H)` beats this bound exponentially. Hence (13) follows by dominated convergence for every fixed `H`.

The two limits are nevertheless very different. Equation (13) first fixes `H` and then removes `delta`; `PL-404` needs information as `H -> infinity` at the much finer normalized scale `H^-7/4`. Nothing above supplies the required joint uniformity.

## 4. The exact remaining bridge is a two-regulator uniformity problem

`PL-404` already uses the cubic Abel regulator `eta>0` to control the continuation-kernel transition in the gap variable `d/H`. Equation (7) introduces a different regulator, `delta>0`, in the **Ramanujan modulus/frequency** variable `q`. They solve different problems:

- `eta` controls the mesoscopic cubic transition and Mellin inversion in `d/H`;
- `delta` makes the arithmetic Ramanujan spectrum finite-energy.

For every fixed pair `(eta,delta)` the harmonic statistic (12) is rigorous. For fixed `H`, removing `delta` recovers the exact `PL-404` model source. The missing theorem must instead control a joint regime in which the arithmetic observable becomes the actual modified Mangoldt data while `delta -> 0` and `H -> infinity`, with aggregate replacement error below the already-audited `H^-7/4` layer.

A sufficient target, stronger than what is formally needed but mathematically clean, would be a uniform asymptotic for the actual weighted correlation

\[
P_\eta(X,H)
:=\frac1{XH}\sum_{n\le X}\sum_{d\ge1}
\Lambda_1(n)\Lambda_1(n+d)
 w_\eta^{[2]}(d/H)
\tag{21}
\]

that recovers `A_eta^[2](H)` with an error `o(H^-7/4)` in some controlled joint range `X=X(H)`. This is **not asserted** to be necessary, nor is it asserted to be equivalent to the fixed-gap twin-prime conjecture: averaging over a growing family of shifts can be strictly easier than controlling every fixed shift. It is recorded only as one concrete source-replacement target compatible with `PL-404`.

The critical warning is that one may not justify (21) by simply substituting (1) and applying Parseval. That move is exactly the infinite-energy endpoint at which (18) fails.

## 5. Prior-art and novelty audit

The Ramanujan source identification itself is classical and is **not** claimed as new.

Gadiyar and Padma, *Physica A* **269** (1999), 503--510, DOI `10.1016/S0378-4371(99)00171-5`, write the modified von Mangoldt expansion (1), derive the coefficient-square series (4), and explicitly frame the prime-pair problem as a Wiener--Khintchine/autocorrelation problem.

Their later peer-reviewed paper, “Ramanujan-Fourier series and the conjecture D of Hardy and Littlewood,” *Czechoslovak Mathematical Journal* **64** (2014), 251--267, DOI `10.1007/s10587-014-0098-5`, explicitly labels the argument heuristic and identifies the unjustified interchange of limits as the failure point.

Murty and Saha, “On the error term in a Parseval type formula in the theory of Ramanujan expansions,” *Journal of Number Theory* **156** (2015), 125--134, DOI `10.1016/j.jnt.2015.04.026`, prove rigorous shifted-convolution/Parseval formulae under absolute-convergence and quantitative coefficient-decay hypotheses. Those hypotheses deliberately sit on the finite-energy side and do not make the critical coefficients `mu(q)/phi(q)` harmless.

There are also arXiv papers by John Washburn using Abel summation of Ramanujan-Fourier series, including arXiv:1309.2716 and arXiv:1506.07822. They are relevant prior art for **summability** of the formal covariance, but they do not change the guardrail used here: an Abel-summed Ramanujan expression is not, without a Tauberian/uniformity theorem, the ordinary Cesaro prime-pair correlation required to replace the `PL-404` source by actual arithmetic data. The 2014 peer-reviewed Gadiyar--Padma paper still records precisely that ordinary limit-interchange problem.

The safe Mathia contribution is therefore narrower:

1. connect the exact source isolated in `PL-404` to this classical Ramanujan/Wiener picture;
2. quantify the endpoint as simultaneous logarithmic divergence of the formal spectral energy and the actual `Lambda_1` mean-square;
3. embed the source in the rigorous family (7)--(13), where the energy blow-up is `1/(2 delta)`; and
4. reformulate the live `PL-404` source replacement as a joint `H -> infinity`, `delta -> 0` uniformity problem rather than another special-function refinement.

Targeted literature searches found the classical Ramanujan prime-pair program, Abel-summability variants, and rigorous Parseval theorems under stronger decay, but no source making this specific `PL-404` exact-kernel / `H^-7/4` connection or the two-regulator formulation.

## 6. Matched control

The regulator itself supplies the required control. For every fixed `delta>0`, the coefficient energy in (18) is finite, Wiener--Khintchine is rigorous, and the covariance kernel is exactly (8). There is no mysterious arithmetic failure in the Ramanujan basis away from the endpoint.

At `delta=0`, the off-diagonal kernel still has a perfectly good limit for each fixed `h != 0`, while the diagonal energy diverges. Hence the obstruction is specifically an **endpoint interchange/uniformity problem**, not failure of the finite Ramanujan geometry or of the singular-series Euler product.

An even stronger generic control is supplied by the standard Parseval theory of absolutely convergent Ramanujan expansions: coefficients with a fixed extra power of decay satisfy rigorous shifted-convolution theorems of the Murty--Saha type. The modified von Mangoldt coefficients sit exactly outside that easy regime.

## 7. Boundaries and falsification tests

1. **No prime-pair theorem is proved.** Equation (3) concerns finite Ramanujan truncations; (8) concerns the regulated function `L_delta`; neither is the autocorrelation of `Lambda_1` at `delta=0`.

2. **Abel summability is not ordinary correlation.** A summability prescription for the formal Ramanujan covariance cannot be substituted for the Cesaro arithmetic limit without a separate Tauberian/uniformity argument.

3. **The `B^2` divergence is a guardrail, not an impossibility theorem.** Infinite energy rules out the naive finite-energy Wiener--Khintchine passage. It does not rule out a renormalized distributional covariance, an averaged-shift theorem, or another arithmetic argument.

4. **The weighted source problem may be easier than fixed-gap Hardy--Littlewood.** `PL-404` needs a particular growing, Abel-smoothed `d`-average. Failure of the fixed-`h` method does not prove that this averaged source replacement is inaccessible.

5. **The critical energy asymptotic is independently checkable.** Replacing (9) by any bounded endpoint energy would contradict the Euler product (16)--(17) and the pole of `zeta(s+1)` at `s=0`.

6. **The arithmetic mean-square is independently checkable.** The prime contribution alone has order `X log X`, while higher prime powers are lower order. Thus any claimed `B^2` realization of `Lambda_1` with finite norm is false.

7. **The `PL-404` zero layer is not proved stable under a joint regulator removal.** Equation (13) is a fixed-`H` statement. Preserving the `H^-7/4` Mellin zero layer while `H` grows is exactly what remains to be established.

## Consequence for the line

The singular-series source in `PL-404` should no longer be treated as merely an externally inserted Hardy--Littlewood heuristic. It is the critical off-diagonal Ramanujan covariance naturally associated with the modified von Mangoldt observable, and it is approached by a completely rigorous finite-energy family.

But this does **not** complete the arithmetic bridge. It identifies why the obvious harmonic route stops: the actual modified Mangoldt observable sits at the `delta=0` endpoint where the Ramanujan spectral energy and its arithmetic mean-square both diverge logarithmically. The next useful work is therefore not another refinement of the incomplete-gamma kernel or of the singular-series Mellin transform. It is a quantitative joint-endpoint theorem -- or a different continuation-faithful arithmetic observable -- that crosses this source boundary with error below the `H^-7/4` scale already transferred in `PL-404`.
