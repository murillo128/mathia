# PC-293 — diffuse source averaging suppresses square-root residue bands

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL-OBSTRUCTION` + `DECISIVE-BOUNDARY` for the source-averaged mesoscopic residue-band frontier left open by PC-292.

PC-291 shows that residue bands of width `T=o(N/log q)` are uniformly invisible for every source pair after the natural `1/N` matrix normalization, while PC-292 proves that this threshold is sharp in worst-case operator norm: the same-source configuration `p=r=1` already has order-one norm when `T~N/log q` at `N~sqrt(q)`. The remaining question is whether that worst-case Hankel transition survives the actual source averaging used by the Prime-Circle spectral laws.

It does not. More strongly, **no positional information about a diffuse source measure can be carried at order one by any residue band of width `T=O(N)` at square-root resolution**. The suppression is purely combinatorial and does not use prime equidistribution.

Let `q` be an odd prime,

\[
H_B=\{-B,\ldots,B\},\qquad N=2B+1\le q,
\]

and use the exact PC-291/PC-292 boundary-log kernel

\[
k_q(0)=-\log q,
\qquad
k_q(t)=\log\!\left(2\sin\frac{\pi |t|_q}{q}\right)\quad(t\ne0).
\]

For `0<=T<=q/4` define

\[
K_{q,B}^{p,r,\le T}(h,k)
:=k_q(ph+rk)\,\mathbf 1_{\{|ph+rk|_q\le T\}}.
\tag{1}
\]

Let `mu` be **any** probability measure on `(Z/qZ)^x`, choose `p,r` independently with law `mu`, and put

\[
\beta(\mu):=\|\mu\|_\infty,
\qquad
E_q(T):=(\log q)^2+2\sum_{a=1}^{T}
\left|\log\!\left(2\sin\frac{\pi a}{q}\right)\right|^2.
\tag{2}
\]

Then

\[
\boxed{
\mathbb E_{p,r\sim\mu}
\left\|\frac{K_{q,B}^{p,r,\le T}}{N}\right\|_F^2
\le
\beta(\mu)E_q(T)+\frac{(\log q)^2}{N^2}.
}
\tag{3}
\]

Consequently, if `Sigma(A)` denotes the decreasing ordered singular-value vector and `K^{>T}=K-K^{\le T}`, the coupling using the same source pair gives

\[
\boxed{
\mathbb E_{p,r\sim\mu}
\left\|
\Sigma(K_{q,B}^{p,r}/N)-
\Sigma(K_{q,B}^{p,r,>T}/N)
\right\|_{\ell^\infty}
\le
\left(
\beta(\mu)E_q(T)+\frac{(\log q)^2}{N^2}
\right)^{1/2}.
}
\tag{4}
\]

For `1<=T<=q/4`,

\[
E_q(T)
\ll
(\log q)^2+T\left(1+\log^2\frac qT\right).
\tag{5}
\]

Hence if `N~sqrt(q)` and `beta(mu)=O(log q/q)`, then uniformly for every fixed `C>0`,

\[
\boxed{
T\le CN
\quad\Longrightarrow\quad
\mathbb E
\left\|
\Sigma(K/N)-\Sigma(K^{>T}/N)
\right\|_{\ell^\infty}
\ll_C
\frac{(\log q)^{3/2}}{q^{1/4}}
\longrightarrow0.
}
\tag{6}
\]

At the precise PC-292 worst-case threshold `T~alpha N/log q`, the stronger rate

\[
\boxed{
\mathbb E
\left\|
\Sigma(K/N)-\Sigma(K^{>T}/N)
\right\|_{\ell^\infty}
\ll_\alpha
\frac{\log q}{q^{1/4}}
\longrightarrow0
}
\tag{7}
\]

holds.

The prime source has `beta=1/M_q~log q/q`. The count-matched Li-grid control of PC-290 also has maximal atom `O(log q/q)`. Therefore (6) applies to **both sides without using any source-position information whatsoever**. PC-292's order-one Hankel example is a genuine worst-case finite-section phenomenon, but it is washed out by the diffuse source averaging relevant to the one-profile spectral law.

## 1. One linear residue has at most one partner per source point

Fix `(h,k)!=(0,0)` in `H_B^2` and a residue `a mod q`.

If `k!=0`, then for every fixed `p` the congruence

\[
hp+kr\equiv a\pmod q
\tag{8}
\]

determines exactly one residue class

\[
r\equiv k^{-1}(a-hp)\pmod q.
\tag{9}
\]

Therefore

\[
\begin{aligned}
\mathbb P_{p,r\sim\mu}(hp+kr=a)
&=
\sum_p \mu(p)\,\mu\!\left(k^{-1}(a-hp)\right)\\
&\le \|\mu\|_\infty\sum_p\mu(p)
=\beta(\mu).
\end{aligned}
\tag{10}
\]

If `k=0`, then necessarily `h!=0` and the same conclusion follows directly because `p=h^{-1}a` is uniquely determined. Thus for every nonzero coefficient pair,

\[
\boxed{
\mathbb P(hp+kr=a)\le\beta(\mu).
}
\tag{11}
\]

This is the entire source-averaging mechanism. It is an elementary finite-field incidence bound: a fixed affine linear equation contains at most one partner after one source coordinate is fixed. No distributional property of the support of `mu` is used.

## 2. Exact Hilbert-Schmidt averaging

For a fixed `(h,k)!=(0,0)`, equations (1), (2), and (11) give

\[
\begin{aligned}
\mathbb E
\left|K_{q,B}^{p,r,\le T}(h,k)\right|^2
&=
\sum_{|a|_q\le T}|k_q(a)|^2
\mathbb P(hp+kr=a)\\
&\le
\beta(\mu)E_q(T).
\end{aligned}
\tag{12}
\]

At the single exceptional coefficient pair `(h,k)=(0,0)`, the residue is identically zero and

\[
\left|K_{q,B}^{p,r,\le T}(0,0)\right|^2=(\log q)^2.
\tag{13}
\]

Summing (12) over the remaining `N^2-1` entries, adding (13), and dividing by `N^2` gives the slightly sharper exact estimate

\[
\mathbb E
\left\|\frac{K^{\le T}}N\right\|_F^2
\le
\left(1-\frac1{N^2}\right)\beta(\mu)E_q(T)
+\frac{(\log q)^2}{N^2},
\tag{14}
\]

of which (3) is the convenient form.

For singular values,

\[
\|\Sigma(A)-\Sigma(B)\|_{\ell^\infty}
\le\|A-B\|_{op}
\le\|A-B\|_F.
\tag{15}
\]

Apply (15) with `A=K/N` and `B=K^{>T}/N`, then average and use Cauchy--Schwarz/Jensen. This proves (4).

The same result holds for the uniform law on **distinct** ordered elements of a source set `S` with `|S|=M>=2`. Conditioning the independent uniform product law on `p!=r` can increase the expectation of a nonnegative quantity by at most `M/(M-1)`. Hence (3)--(4) remain valid with the right side multiplied by that asymptotically harmless factor and `beta=1/M`.

## 3. Size of the log-sine band energy

For `1<=a<=T<=q/4`, the elementary small-angle comparison gives

\[
|k_q(a)|
\le C+\log\frac qa.
\tag{16}
\]

Therefore

\[
E_q(T)
\ll
(\log q)^2+
\sum_{a=1}^{T}\left(1+\log^2\frac qa\right).
\tag{17}
\]

Writing `log(q/a)=log(q/T)+log(T/a)` and comparing the last two logarithmic moments with their integrals gives

\[
\sum_{a=1}^{T}\log^2\frac qa
\ll
T\left(1+\log^2\frac qT\right),
\tag{18}
\]

which proves (5).

Now take `N~sqrt(q)` and `beta(mu)=O(log q/q)`. If `T<=CN`, then `log(q/T)=O(log q)` and

\[
\beta E_q(T)
\ll_C
\frac{\log q}{q}\,N(\log q)^2
\ll_C
\frac{(\log q)^3}{\sqrt q}.
\tag{19}
\]

The anchored `(0,0)` term contributes only `O((log q)^2/q)`. Taking square roots proves (6).

At `T~alpha N/log q`, equation (5) improves (19) to

\[
\beta E_q(T)
\ll_\alpha
\frac{(\log q)^2}{\sqrt q},
\tag{20}
\]

which gives (7).

A broader formulation is immediate from (4): whenever

\[
\beta(\mu)E_q(T)\to0,
\qquad
\frac{\log q}{N}\to0,
\tag{21}
\]

the entire residue band is invisible in the source-averaged normalized ordered singular spectrum. Thus `T=O(N)` is only the range needed for the square-root frontier, not the maximal range of the argument.

## 4. Reconciliation with PC-292

There is no contradiction with the sharp worst-case result. PC-292 constructs one source pair for which

\[
\left\|K_{q,B}^{1,1,\le T}/N\right\|_{op}\to\alpha
\]

when `T~alpha N/log q`. Equation (3) does not bound each source pair: it bounds their average under a diffuse source law.

The difference is structural. In the same-source Hankel configuration, `~T` adjacent residue classes line up coherently along long anti-diagonals, so their individual logarithmic weights add at the operator-norm level. Under source averaging, a fixed nonzero coefficient entry can hit each prescribed residue through at most one partner for each first source coordinate. The total **squared** local-band mass is therefore diluted by the maximal source atom `beta(mu)` before any spectral summary is taken.

For the actual prime-source law, this dilution is already enough. It does not require PNT equidistribution inside intervals, character cancellation, RH, or comparison with individual Li-grid locations. Only the cardinality-scale fact `M_q~q/log q` is needed to identify `beta~log q/q`; the geometric estimate itself holds for every source support of that size.

## 5. Matched-control consequence

PC-290 reaches every `B=o(sqrt(q))` by transporting the complete boundary-log singular-spectrum law from the prime source to a count-matched Li-grid control, but stops at `B~sqrt(q)`. PC-291 then shows that microscopic residue bands cannot explain that stop, while PC-292 proves that a mesoscopic `N/log q` band can be large for a single exceptional pair.

Equations (6)--(7) now remove that exceptional mechanism from the **source-averaged** frontier. Both the uniform prime measure and the PC-290 count-matched grid control are diffuse at scale `O(log q/q)`, so deleting every residue with

\[
|ph+rk|_q\le C\sqrt q
\]

changes either normalized complete ordered singular-spectrum law by `o(1)` in the natural `ell^infinity` Wasserstein coupling.

This does **not** prove prime-versus-control collapse at `B~sqrt(q)`: the complement `|ph+rk|_q>C\sqrt q` is untouched. It proves something more specific and falsifiable: **the local logarithmic singularity, including the first order-one worst-case Hankel band of PC-292, cannot be the missing source-averaged critical-scale carrier.** Any surviving order-one discrepancy at square-root coefficient resolution must be assembled from nonlocal residues, from a non-averaged/extremal statistic, or from information discarded before the one-profile singular-spectrum law is formed.

## 6. Prior-art and novelty audit

No new theorem in finite-field incidence geometry, matrix analysis, or Hankel theory is claimed. The ingredients of (3)--(4) are elementary: uniqueness of one variable in a nondegenerate linear congruence, Hilbert-Schmidt summation, the standard operator/Frobenius norm inequality, and singular-value perturbation. The PC-292 Hankel finite-section mechanism is already explicitly classicalized there.

Targeted external checks covered finite-field point-line incidence bounds, large-sieve/Plancherel viewpoints, cyclic-convolution finite sections, sparse resonant perturbations, and classical Hankel operators. Those literatures contain much stronger structured incidence and operator results, but no such theorem is needed here: the relevant line-local estimate is the trivial one-partner bound (11). No external novelty claim or load-bearing new literature dependency is introduced, so `SOURCES.md` does not need an addition.

The durable project-local delta is the combination of that elementary incidence fact with the exact PC-291 boundary-log residue decomposition and the source-averaged singular-spectrum observable already used by PC-281--PC-290. PC-292 establishes a real worst-case transition; PC-293 shows that this transition disappears under every sufficiently diffuse matched source law, independently of the source locations.

## 7. Falsification and boundary tests

The claim has direct failure tests.

1. For `(h,k)!=(0,0)`, exhibit a residue `a` for which the product-source probability of `hp+kr=a` exceeds `||mu||_infty`. Equation (9), or its symmetric version when `k=0`, rules this out.
2. Exhibit a source measure for which the averaged normalized squared Frobenius mass of the band exceeds (14). Entrywise summation of (12)--(13) rules this out.
3. Take `N~sqrt(q)`, `||mu||_infty=O(log q/q)`, and `T=O(N)` but keep an order-one mean singular-spectrum perturbation after band deletion. Equations (4)--(6) rule this out.
4. Keep a fixed exceptional pair instead of averaging, let the source measure develop atoms much larger than `log q/q`, take a band outside the condition (21), retain raw residue support/direction/phase, or couple several levels before spectral compression. These operations lie outside the theorem and remain legitimate continuations.

The main boundary is therefore sharper than after PC-292: **the square-root frontier is not controlled by the local singular residue sector even though that sector has order-one worst-case operator norm. The unresolved source-averaged information, if any, is necessarily nonlocal or representation-richer.**