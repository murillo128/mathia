# XF-035 — Xi counting has a sharp inverse-buffer flux-variation threshold for geometric stability

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `SOURCE-SPECIFIC` + `NEGATIVE/OBSTRUCTION` + `STRUCTURAL/THRESHOLD`. XF-034 shows that an exact or uniformly `o(1)`-near geometric gap ramp must flatten on a super-mesoscopic Xi buffer. The missing bridge was whether small triple-discriminant bulk force forces that uniform near-geometricity. There is a sharp scale boundary: if the total variation of the XF-031 triple flux is `o(1/M)`, then the bridge closes; at the borderline `Theta(1/M)` there are bounded-dynamic-range tent profiles satisfying the two nested Xi span constraints exactly while remaining a fixed distance from every affine log-gap profile.

Let a block contain `2M` positive gaps
\[
g_0,\ldots,g_{2M-1}>0,
\qquad
y_k=\log g_k,
\qquad
d_j=y_{j+1}-y_j
\quad(0\le j\le 2M-2),
\]
and let
\[
\phi_j:=F'(d_j)
\]
be the normalized-triple flux from XF-030/031. Define
\[
\boxed{
V_M:=\sum_{j=0}^{2M-3}|\phi_{j+1}-\phi_j|.
}
\tag{1}
\]
For a source-valid Xi block at height `T` with
\[
M=R(T)\log^2T,
\qquad R(T)\to\infty,
\qquad R(T)=o(T/\log T),
\]
XF-034 gives the nested span law
\[
\boxed{
\frac{\sum_{k=0}^{2M-1}g_k}{\sum_{k=0}^{M-1}g_k}
=2+o(1).
}
\tag{2}
\]
Then
\[
\boxed{
M V_M=o(1)
\quad\Longrightarrow\quad
\max_{0\le j\le2M-2} M|d_j|=o(1),
}
\tag{3}
\]
and consequently
\[
\boxed{
\max_{0\le k<2M}\left|\log\frac{g_k}{g_0}\right|=o(1).
}
\tag{4}
\]
Thus `o(1/M)` total variation of the nonlinear triple flux is sufficient to turn the XF-031/033 near-null information into the uniformly near-geometric hypothesis of XF-034, after which Xi counting forces the affine slope itself to vanish.

The scale `1/M` cannot be improved by a static argument using only the nested spans and small triple bulk force. For every fixed `c>0` there is a positive `2M`-gap tent profile with
\[
\frac{\sum_{k=0}^{2M-1}g_k}{\sum_{k=0}^{M-1}g_k}=2
\tag{5}
\]
exactly,
\[
V_M\sim\frac{3c}{M},
\tag{6}
\]
all unweighted `ell^p` norms of `L_\lambda h` tending to zero, and total triple shape deficit tending to zero, yet
\[
\inf_{A,B}\max_k|y_k-(A+Bk)|\ge\frac c2.
\tag{7}
\]
The profile has bounded gap dynamic range `max g_k/min g_k=e^c`, so this obstruction does not use a collision or an exponentially large geometric ramp.

## 1. A compact contrast coordinate gives a global inverse-Lipschitz flux law

Write
\[
t=\tanh(d/2)=\frac{e^d-1}{e^d+1}\in(-1,1).
\tag{8}
\]
Substituting `r=e^d=(1+t)/(1-t)` into the exact XF-030 formula gives
\[
\boxed{
\phi=P(t):=\frac{t(t^2-9)}{t^2+3}.
}
\tag{9}
\]
Differentiating,
\[
P'(t)=\frac{t^4+18t^2-27}{(t^2+3)^2}<0.
\tag{10}
\]
Moreover, for `|t|<=1`,
\[
-P'(t)-\frac12
=
\frac{3(1-t^2)(t^2+15)}{2(t^2+3)^2}
\ge0.
\tag{11}
\]
Hence `P` is globally inverse-Lipschitz on the compactified contrast interval:
\[
\boxed{
|t_j-t_k|\le2|\phi_j-\phi_k|\le2V_M.
}
\tag{12}
\]
This removes a possible finite-gap loophole in a stability argument. Small variation of `phi` really does force all adjacent gap ratios to have almost the same compactified contrast; no degeneration of `F''` at very large or very small raw ratios can defeat (12).

## 2. `M V_M=o(1)` closes the XF-034 stability bridge

Assume (2) and `M V_M=o(1)`. By (12),
\[
\operatorname{osc}(t_j)=o(1/M).
\tag{13}
\]
First, the common contrast must tend to zero. If along a subsequence all `t_j` stayed above some fixed `eta>0`, then every `d_j` would be at least a fixed `delta>0`, and for `0<=k<M`,
\[
\frac{g_{M+k}}{g_k}
=\exp\left(\sum_{j=k}^{M+k-1}d_j\right)
\ge e^{\delta M}.
\tag{14}
\]
Therefore the second half-span would be at least `e^(delta M)` times the first, contradicting (2). If all `t_j<=-eta`, the same comparison gives a second-to-first half-span ratio at most `e^(-delta M)`, so the total-to-first ratio tends to one, again contradicting (2). Since (13) makes all `t_j` asymptotically equal, it follows that
\[
\max_j|t_j|=o(1).
\tag{15}
\]

For large `M`, therefore, `|t_j|<=1/2`. On this interval the inverse map `d=2 artanh(t)` has derivative at most `8/3`, so (12) gives
\[
\operatorname{osc}(d_j)
\le\frac{16}{3}V_M
=o(1/M).
\tag{16}
\]
Fix `d_*=d_0`. Then for every `k`,
\[
y_k=y_0+kd_*+\varepsilon_k,
\qquad
|\varepsilon_k|
\le k\operatorname{osc}(d_j)
\le2M\operatorname{osc}(d_j)
=o(1).
\tag{17}
\]
Thus the entire block is uniformly `o(1)`-multiplicatively close to the geometric progression `g_0 e^{kd_*}`. This is exactly the stable near-geometric hypothesis proved sufficient in XF-034. Applying that finding to (17) yields
\[
M d_*=o(1).
\tag{18}
\]
Together with (16),
\[
\max_j M|d_j|
\le M|d_*|+M\operatorname{osc}(d_j)
=o(1),
\]
which proves (3), and summing the contrasts proves (4).

The factor `M` is not a proof artifact: it is the accumulation length needed to turn control of contrast variation into uniform control of the log-gap profile.

## 3. A symmetric tent saturates the `1/M` scale while passing the nested count exactly

Fix `c>0` and put
\[
a_M:=\frac{c}{M-1}.
\tag{19}
\]
Before an arbitrary common rescaling, define
\[
\widetilde g_k=e^{a_Mk}
\qquad(0\le k\le M-1),
\tag{20}
\]
and
\[
\widetilde g_{M+k}=e^{a_M(M-1-k)}
\qquad(0\le k\le M-1).
\tag{21}
\]
The second half is the reverse of the first, so
\[
\sum_{k=0}^{M-1}\widetilde g_k
=
\sum_{k=M}^{2M-1}\widetilde g_k,
\]
and (5) holds exactly. A common factor can therefore normalize the first half-span to the Xi main term `4 pi M/log T`; the full span then equals `8 pi M/log T` exactly. For `M=R(T)log^2 T` this block has the same two nested main-term spans used in XF-034 and total spatial size `o(T)` under the same condition `R(T)=o(T/log T)`.

Its log gaps form a tent:
\[
y_k=a_Mk\quad(0\le k<M),
\qquad
y_{M+k}=a_M(M-1-k).
\tag{22}
\]
Hence
\[
d_j=
\begin{cases}
 a_M,&0\le j\le M-2,\\
 0,&j=M-1,\\
 -a_M,&M\le j\le2M-2.
\end{cases}
\tag{23}
\]
Since `phi` is odd in `d`, the flux sequence is constant on each flank and changes only at the two folds. Therefore
\[
\boxed{
V_M=2|\phi(e^{a_M})|
=3a_M+O(a_M^3)
\sim\frac{3c}{M}.
}
\tag{24}
\]
Using the XF-031 identity
\[
(L_\lambda h)_i=\phi_{i-1}-\phi_i,
\tag{25}
\]
there are only two nonzero bulk-force entries, each of magnitude `|phi(e^{a_M})|`. Thus for every fixed `1<=p<infinity`,
\[
\|L_\lambda h\|_{\ell^p}
=2^{1/p}|\phi(e^{a_M})|
=O(1/M),
\tag{26}
\]
and the `ell^infinity` norm is also `O(1/M)`. Every such unweighted norm tends to zero.

The local shape deficit vanishes even more strongly. XF-030 gives
\[
F(d)=F(0)-\frac34d^2+O(d^4),
\qquad F(0)=-\log2,
\tag{27}
\]
so
\[
\sum_{j=0}^{2M-2}\bigl(F(0)-F(d_j)\bigr)
=(2M-2)\left(\frac34a_M^2+O(a_M^4)\right)
=O(1/M).
\tag{28}
\]
Thus neither vanishing unweighted bulk force nor vanishing total triple-shape deficit forces the profile close to a single geometric ramp.

Nevertheless the tent stays a fixed distance from every affine log-gap profile. Its endpoints satisfy `y_0=y_{2M-1}=0`, while `y_{M-1}=y_M=c`. For any affine `ell(k)=A+Bk`, let
\[
E=\max_k|y_k-\ell(k)|.
\]
The endpoint bounds give `|ell(0)|<=E` and `|ell(2M-1)|<=E`; affine interpolation therefore gives `|ell(M-1)|<=E`. Hence
\[
c
\le |c-\ell(M-1)|+|\ell(M-1)|
\le2E,
\]
which proves (7).

Finally,
\[
\frac{\max_k g_k}{\min_k g_k}=e^c.
\tag{29}
\]
After normalization to the Xi span, all gaps remain comparable to `1/log T` by constants depending only on `c`. The construction is therefore a regular-gap matched control, not a collision singularity or an exponentially wide geometric ramp.

## 4. What the threshold does and does not establish

The positive implication (3) is source-specific because it uses the nested Xi span law from XF-034. The inverse-Lipschitz step (9)--(12) and the tent obstruction are universal finite-gap algebra. Together they identify the scale that a future coercive estimate must beat: a control that can deliver
\[
M\,\mathrm{TV}(\phi)=o(1)
\tag{30}
\]
on the super-mesoscopic buffer is strong enough to remove the geometric null mode completely.

By contrast, it is not enough to prove only `TV(phi)->0`, `||L_lambda h||_{ell^p}->0` for a fixed unweighted `p`, or vanishing summed triple-shape deficit. The tent satisfies all of those statements while passing the two nested count constraints exactly. Any use of such weaker quantities must bring in additional structure — for example the long-range `L_w` dynamics, a stronger weighted coercivity, endpoint flux information, or further source statistics — rather than infer uniform geometricity from them alone.

The tent is **not** claimed to be an actual Xi zero block or a solution of the logarithmic-particle evolution. It is a matched static falsification control for the specific stability implication left open by XF-034. A dynamical theorem coupling `L_lambda h` to `L_w h`, or a stronger Xi-specific statistic excluding folded slopes, can still beat this obstruction.

Nor does (30) assert necessity for every possible proof. It is sufficient and order-sharp for a route based only on total variation of the triple flux plus the nested span law. The borderline constant `M V_M=Theta(1)` can support non-affine tents; additional hypotheses may distinguish them.

## 5. Prior-art and novelty boundary

The analytic skeleton is classical: bounded variation controls oscillation, a second discrete difference controls distance to an affine profile only after paying the interval length, and nested-span comparisons are elementary. A targeted search of discrete Poincare/BV approximation literature found only this broad neighboring structure, not a theorem needed as a load-bearing input here. No general novelty is claimed for those estimates.

The only external source input is the Rodgers--Tao zero-counting law already anchored in `SOURCES.md` and already specialized to the nested super-mesoscopic span statement in XF-020/034. Equations (9)--(29) are exact algebra from XF-030/031 plus the explicit matched control above. No `SOURCES.md` change is required.

The durable Mathia-local content is the **sharp scale interface** between the active nonlinear triple-discriminant bulk and the source constraint: `o(1/M)` flux variation closes the geometric-stability bridge, while `Theta(1/M)` already permits smooth, bounded-dynamic-range folded profiles that evade uniform affine approximation without violating the two nested counts.

## 6. Consequence for `xi_flow`

The next positive target is now quantitative rather than qualitative. The overlap/taper program should seek an estimate strong enough to make `M V_M=o(1)` — or another norm that implies the same uniform affine control — on the active super-mesoscopic buffer, while retaining XF-028 collision coverage. Merely showing that the triple bulk force tends to zero as `M` grows will not suffice.

Conversely, a stronger negative result must use more than the static tent. To kill the taper route itself, one would need a source-compatible family that also respects the relevant `L_w` dynamics or full tapered derivative and still sustains a folded log-gap profile. XF-035 therefore narrows the open problem to whether the actual Xi-flow coercivity beats the inverse-buffer `1/M` variation threshold identified here.