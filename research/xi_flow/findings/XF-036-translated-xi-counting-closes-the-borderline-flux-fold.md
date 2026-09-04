# XF-036 — translated Xi counting closes the borderline flux-fold loophole

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `SOURCE-SPECIFIC` + `STRUCTURAL/STABILITY`. XF-035 identified `1/M` as the sharp static scale for turning variation of the normalized-triple flux into geometric stability **when only two nested span constraints are retained**: a fixed-amplitude tent has `V_M=Theta(1/M)` and passes those two spans exactly. The full Xi source package is stronger. XF-020's global counting law applies to every translated super-mesoscopic subwindow inside the buffer, and those translated averages exclude the tent and every other macroscopic fold at the borderline scale.

Let `t` lie in the real-simple regime `Lambda<t<=0`, let `x_j(t)\asymp T`, and let

\[
M=R(T)\log^2T,
\qquad
R(T)\to\infty,
\qquad
R(T)=o(T/\log T).
\tag{1}
\]

Write the next `2M` gaps as

\[
g_k=x_{j+k+1}(t)-x_{j+k}(t)>0,
\qquad
0\le k<2M,
\tag{2}
\]

and set

\[
y_k=\log g_k,
\qquad
d_k=y_{k+1}-y_k,
\qquad
\phi_k=F'(d_k),
\tag{3}
\]

where `F` is the normalized three-root discriminant of XF-030. Define the total triple-flux variation

\[
V_M:=\sum_{k=0}^{2M-3}|\phi_{k+1}-\phi_k|.
\tag{4}
\]

If

\[
\boxed{M V_M=O(1),}
\tag{5}
\]

then, with the source mean spacing

\[
h_T:=\frac{4\pi}{\log T},
\tag{6}
\]

one has the uniform flattening

\[
\boxed{
\max_{0\le k<2M}\left|\log\frac{g_k}{h_T}\right|=o(1).
}
\tag{7}
\]

Thus **bounded inverse-buffer flux variation already forces every gap in the entire super-mesoscopic block to be asymptotically equal to the source mean spacing**. The little-`o` condition `M V_M=o(1)` from XF-035 is sufficient if one compresses the source to two spans, but it is not the true source-side threshold once the full translated counting information of XF-020 is retained.

The conclusion deliberately stops short of

\[
\max_k M|d_k|=o(1).
\]

Under (5) one obtains only `max_k |d_k|=O(1/M)` from the argument below. Microscopic `O(1/M)` contrast oscillations may survive while the gaps themselves converge uniformly to `h_T`. The result therefore removes the fixed-amplitude folded profile as a source-compatible obstruction but does not yet prove the sign or coercivity needed for a Xi-flow Lyapunov theorem.

## 1. The global count is uniform on translated fixed-fraction subwindows

XF-020 derives from Rodgers--Tao's global count that, uniformly in the real-simple regime and for `0<D<=U/2`,

\[
N_t([U,U+D])
=
\frac{D}{4\pi}\log\frac{U}{4\pi}
+O\!\left(\log^2U+\frac{D^2}{U}\right).
\tag{8}
\]

It also derives the corresponding index-spacing law at super-mesoscopic length. For the present use we need the translated version across one `2M`-gap buffer.

First apply XF-020 with length `2M`. It gives

\[
x_{j+2M}-x_j
=\frac{8\pi M}{\log T}(1+o(1))
=O(R(T)\log T)
=o(T).
\tag{9}
\]

Hence every root `x_{j+q}`, `0<=q<=2M`, lies at height `T+o(T)`, so its logarithm is `log T+o(1)` uniformly in `q`.

Fix any `delta in (0,1]` and put

\[
L=L_\delta:=\lfloor\delta M\rfloor.
\tag{10}
\]

Then

\[
L=(\delta R(T)+o(1))\log^2T,
\]

and `delta R(T)->infinity`. Applying the same global-count inversion with starting height `x_{j+q}=T+o(T)` therefore gives, uniformly for all starts whose interval remains inside the `2M` block,

\[
\boxed{
\sum_{k=q}^{q+L-1}g_k
=x_{j+q+L}-x_{j+q}
=h_T L\,(1+o_\delta(1)),
}
\tag{11}
\]

for

\[
0\le q\le2M-L.
\]

The uniformity is elementary from (8): relative to the `Theta(delta R log^2 T)` main count, the global `O(log^2 T)` error is `O(1/(delta R))`, the logarithmic-density change across the whole buffer is `o(1)`, and the curvature term is also lower order under (1). No bounded-`alpha` local zero theorem is being extrapolated here.

Equation (11) is the extra source information absent from the tent stress test of XF-035. It says that **every fixed-fraction translated block**, not merely the first `M` gaps and the full `2M` gaps, has the same asymptotic mean spacing `h_T`.

## 2. Bounded `M V_M` makes the log-gap profile equi-Lipschitz on the index scale

XF-035 introduces the compact contrast coordinate

\[
s_k:=\tanh(d_k/2)\in(-1,1)
\tag{12}
\]

and proves the exact flux law

\[
\phi_k=P(s_k),
\qquad
P(s)=\frac{s(s^2-9)}{s^2+3},
\tag{13}
\]

together with the global inverse-Lipschitz estimate

\[
|s_k-s_\ell|\le2|\phi_k-\phi_\ell|.
\tag{14}
\]

By (4)--(5),

\[
\operatorname{osc}_k s_k
\le2V_M
=O(1/M).
\tag{15}
\]

The common contrast must tend to zero. Indeed, (11) with `delta=1` gives both half-spans

\[
S_0:=\sum_{k=0}^{M-1}g_k=h_TM(1+o(1)),
\qquad
S_1:=\sum_{k=M}^{2M-1}g_k=h_TM(1+o(1)),
\tag{16}
\]

so `S_1/S_0=1+o(1)`. If along a subsequence the almost-common `s_k` stayed above a fixed positive number, all `d_k` would be bounded below by a fixed positive constant and

\[
\frac{g_{M+k}}{g_k}
=
\exp\!\left(\sum_{r=k}^{M+k-1}d_r\right)
\tag{17}
\]

would grow exponentially in `M`, forcing `S_1/S_0->infinity`. A fixed negative common contrast would similarly force the ratio to zero. Together with (15), this proves

\[
\max_k|s_k|=o(1).
\tag{18}
\]

For large `T`, therefore, all `|s_k|<=1/2`. Since `d=2\operatorname{artanh}s` has bounded derivative there, (15) yields

\[
\operatorname{osc}_k d_k=O(1/M).
\tag{19}
\]

Write `d_-:=min_k d_k` and `d_+:=max_k d_k`. Equation (17) gives for every `0<=k<M`

\[
e^{Md_-}\le\frac{g_{M+k}}{g_k}\le e^{Md_+}.
\tag{20}
\]

After weighting by `g_k` and summing,

\[
e^{Md_-}
\le\frac{S_1}{S_0}
\le e^{Md_+}.
\tag{21}
\]

Since `log(S_1/S_0)=o(1)` lies between `M d_-` and `M d_+`, while (19) gives `M(d_+-d_-)=O(1)`, both endpoints are bounded. Hence

\[
\boxed{
\max_k|d_k|=O(1/M).
}
\tag{22}
\]

If

\[
z_k:=\log\frac{g_k}{h_T},
\tag{23}
\]

then (22) is exactly a discrete equi-Lipschitz estimate on the macroscopic index coordinate:

\[
\boxed{
|z_k-z_\ell|
\le C\frac{|k-\ell|}{M}
}
\tag{24}
\]

for some constant `C` depending only on the bound in (5), for all sufficiently large `T`.

## 3. Translated source averages upgrade equi-Lipschitz control to uniform flattening

Fix `delta in (0,1)`. For each index `k` choose an interval

\[
I_k=\{q,\ldots,q+L_\delta-1\}
\]

of `L_delta` consecutive gaps that contains `k` and remains inside `0,...,2M-1`. By (24), every `ell in I_k` satisfies

\[
|z_\ell-z_k|\le C\delta+o(1).
\tag{25}
\]

On the other hand, the translated count (11) says

\[
\frac1{L_\delta}
\sum_{\ell\in I_k}e^{z_\ell}
=
\frac1{h_TL_\delta}
\sum_{\ell\in I_k}g_\ell
=1+o_\delta(1),
\tag{26}
\]

uniformly in `k`. Combining (25) and (26),

\[
e^{z_k-C\delta+o(1)}
\le1+o_\delta(1)
\le e^{z_k+C\delta+o(1)}.
\tag{27}
\]

Therefore

\[
\sup_k|z_k|
\le C\delta+o_\delta(1).
\tag{28}
\]

For each fixed `delta`, let `T->infinity`; then let `delta downarrow0`. This gives

\[
\sup_k|z_k|=o(1),
\]

which is (7).

Conceptually, the mechanism is simple but stronger than the two-span argument: bounded `M V_M` prevents the logarithmic gap profile from changing by more than `O(delta)` across a `delta M` subwindow, while the source says the exponential of that profile has mean `1+o(1)` on **every** such translated subwindow. The only possible macroscopic limit is therefore the constant zero profile.

## 4. The XF-035 tent fails the translated count by an order-one amount

The sharpness example in XF-035 takes, before common rescaling,

\[
g_k=e^{a_Mk},
\qquad0\le k<M,
\qquad
a_M=\frac{c}{M-1},
\tag{29}
\]

and reverses the same sequence on the second half. Its two half-spans are exactly equal, so the first/full nested constraint is passed, and

\[
V_M\sim\frac{3c}{M}.
\tag{30}
\]

But take two adjacent subblocks of length `L=floor(M/2)` inside the increasing flank. Their spans satisfy

\[
\frac{\sum_{k=L}^{2L-1}e^{a_Mk}}
{\sum_{k=0}^{L-1}e^{a_Mk}}
=e^{a_ML}
\longrightarrow e^{c/2}
\qquad(c>0),
\tag{31}
\]

up to the harmless single-index rounding when `M` is odd. XF-020 instead forces both translated half-flank blocks to have asymptotic span `h_TL`, so their ratio must tend to one. No common normalization can repair (31).

Thus the tent remains a correct **matched control for the reduced two-span data package** used to prove sharpness in XF-035, but it is not compatible with the complete translated super-mesoscopic Xi counting law. The apparent borderline obstruction came from discarding source information, not from a source-admissible Xi geometry.

## 5. Boundary conditions and stress tests

The hypothesis (5) is still substantive. If `M V_M` diverges, (24) need not have a uniform macroscopic Lipschitz constant, and fixed-fraction source averages alone do not control arbitrary microscopic or increasingly sharp structure. This finding does not claim that Xi dynamics supplies (5); deriving such a bound from the XF-031 `L_lambda`/`L_w` interaction remains an open coercivity problem.

Nor does (7) imply that the contrast field vanishes faster than `1/M`. A profile may have adjacent log-gap changes of order `1/M` while its total amplitude tends to zero because positive and negative changes cancel on finer scales. The theorem is a **zeroth-order uniform lattice-rigidity statement**, not a first-derivative estimate strong enough by itself to sign the full tapered derivative.

Collision control remains separate. The hypothesis `M V_M=O(1)` does not bound `y_i'`, and an eventual dynamical proof must still use the covered-collision positivity of XF-028 rather than estimate singular log-gap velocities by absolute value.

The result also does not cross `t=Lambda` or assume RH at `t=0`. It uses only the real-simple regime in which the ordered zero configuration and Rodgers--Tao count are source-valid.

Finally, the argument is not an Xi-specific selector in isolation. Any matched real-zero flow with the same translated super-mesoscopic counting law and the same bound (5) would satisfy (7). Its role is to show that the actual source information is stronger than the reduced static control used in XF-035.

## 6. Prior-art and novelty boundary

Rodgers and Tao, **The de Bruijn--Newman constant is non-negative**, *Forum of Mathematics, Pi* 8 (2020), e6, are the only external load-bearing source. Their global zero count is already anchored in `research/xi_flow/SOURCES.md` and specialized in XF-020. No new source entry is required.

The analytic implication “uniform local averages plus a uniform discrete Lipschitz bound force uniform convergence to the common mean” is elementary compactness/Poincare-type structure, and no general novelty is claimed for it. Likewise, the inverse-Lipschitz flux coordinate is already established internally in XF-035. The durable line-specific content is the **source-resolution correction**: using all translated fixed-fraction windows available from XF-020 upgrades the two-span condition `M V_M=o(1)` to the borderline bounded condition `M V_M=O(1)` for uniform gap flattening, and explicitly removes the XF-035 tent as an Xi-compatible obstruction.

## 7. Consequence for `xi_flow`

The overlap/discriminant route no longer needs to beat the inverse-buffer scale by a little-`o` factor merely to rule out macroscopic folded gap profiles. It is enough, on the source side, to obtain

\[
V_M=O(1/M)
\]

on the active `M=R(T)log^2T` buffer; translated Xi counting then forces the whole block to be uniformly lattice-like at zeroth order.

The next constructive gate is therefore dynamical: can the exact finite-gap product rule of XF-031, the positive collision coverage of XF-028, and the long-range `L_w` flow yield a bound of order `1/M` for the total variation of the triple flux, or an equivalent compactness estimate? If yes, the geometric/folded null-mode obstruction is removed without demanding `o(1/M)`. If not, a decisive negative continuation should now target a **near-lattice microscopic misalignment** of `L_lambda h` and `L_w h`, rather than reuse a fixed-amplitude tent that the source count already excludes.