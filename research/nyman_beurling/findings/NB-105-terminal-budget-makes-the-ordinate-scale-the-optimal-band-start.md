# NB-105 — terminal budget makes the ordinate scale the optimal band start

**Status:** `EXACT-DERIVED + NYMAN-FINITE-WINDOW-GRAM + BOUNDARY-DOUBLE-SCALING + TERMINAL-BUDGET + BAND-PLACEMENT-OPTIMIZATION + FIXED-MULTIPLICITY`.

`NB-104` identifies two boundary-scale quantities for a fixed confluent packet,

\[
x=2a\log q,
\qquad
y=2a\log^+\!\frac{|\Gamma|}{m},
\]

and shows that the normalized finite-window determinant volume tends to `e^{-dy} Delta_d(x-y)` when `0<=y<x`. It also leaves an apparent placement escape: increasing the band start `m` can make the ordinate delay `y` vanish. That observation treats the ratio `q` as independent of the band start. A finite Nyman section has a terminal natural-index budget, so moving `m` upward necessarily shortens the available logarithmic window.

Under that terminal constraint the tradeoff is exact. Let

\[
\lambda_j=a_j+i\Gamma_j,
\qquad a_j\downarrow0,
\]

with fixed multiplicity `d`, and put

\[
G_j:=\max(1,|\Gamma_j|).
\]

Let `B_j` be a terminal natural-index budget and assume

\[
L_j:=2a_j\log\frac{B_j}{G_j}\longrightarrow L\in(0,\infty).
\tag{1}
\]

For any admissible integer band

\[
1\le m_j,
\qquad q_j\ge2,
\qquad m_jq_j\le B_j,
\tag{2}
\]

define the **radial start offset** and **unused terminal slack**

\[
s_j:=2a_j\log\frac{m_j}{G_j},
\qquad
\tau_j:=2a_j\log\frac{B_j}{m_jq_j}\ge0.
\tag{3}
\]

Suppose first that

\[
s_j\to s\in\mathbb R,
\qquad
\tau_j\to\tau\in[0,\infty).
\tag{4}
\]

Then the analytic confluent continuation of the `NB-103`/`NB-104` normalized volume has the exact terminal-budget profile

\[
\boxed{
\mathcal V^{\mathrm{conf}}_{d,m_j,q_j}(\lambda_j)
\longrightarrow
\mathcal F_{d,L}(s,\tau),
}
\tag{5}
\]

where, with `T=L-tau`,

\[
\boxed{
\mathcal F_{d,L}(s,\tau)=
\begin{cases}
 e^{ds}\,\Delta_d(T),&s\le0<T,\\[1mm]
 \Delta_d(T-s),&0\le s<T,\\[1mm]
 0,&T\le\max(s,0).
\end{cases}
}
\tag{6}
\]

(The two nonzero formulas agree at `s=0`.) Consequently

\[
\boxed{
\mathcal F_{d,L}(s,\tau)\le\Delta_d(L),
}
\tag{7}
\]

with equality **only** at

\[
\boxed{s=0,\qquad\tau=0.}
\tag{8}
\]

Thus the optimal finite-window placement starts at the ordinate scale on the radial `1/a` scale and uses the terminal budget completely on that same scale. Moving the band start upward does remove the `NB-104` delay, but it removes exactly the same radial depth from the window. Moving it downward preserves the residual interval length but pays an exponential volume factor. There is no free placement repair.

## 1. Terminal coordinates turn the placement problem into one interval

The three scaled quantities satisfy the exact identity

\[
2a_j\log q_j
=L_j-s_j-\tau_j.
\tag{9}
\]

For `|Gamma_j|>=1`, the `NB-104` delay is

\[
y_j=2a_j\log^+\frac{|\Gamma_j|}{m_j}
=\max(-s_j,0).
\tag{10}
\]

When `|Gamma_j|<1`, `G_j=1` and every integer `m_j>=1` has `s_j>=0`, while the delay is already zero, so `(10)` remains valid. Hence the threshold `s=0` is the boundary between starting below and above the ordinate-resolution scale without needing a separate low-ordinate convention.

If one inserts `(9)` and `(10)` directly into the `NB-104` law, the two finite-`s` cases already give `(6)`. For `s<0`,

\[
x-y
=(L-s-\tau)-(-s)
=L-\tau,
\]

so the surviving Laguerre interval keeps its length but acquires the prefactor `e^{ds}`. For `s>=0`, the delay vanishes but

\[
x=L-s-\tau,
\]

so moving the start upward shortens the Laguerre interval itself.

There is a useful coordinate form of the same calculation which makes the tradeoff intrinsic rather than a substitution into the previous theorem. In the exact cell Gram `(NB-104, (9))`, replace the polynomial coordinate

\[
u=2a\log(t/m)
\]

by the ordinate-centered coordinate

\[
v=2a\log(t/G)=u+s.
\tag{11}
\]

Translation of the degree `<d` polynomial basis is unit triangular and therefore does not change the determinant. Replacing the common factor `m^lambda` by `G^lambda` contributes exactly

\[
\left|\frac{m}{G}\right|^{2ad}=e^{ds}
\tag{12}
\]

to the `d x d` Gram determinant. In the `v` coordinate the phase-resolution transition is fixed at `v=0`, while the band runs from `v=s` to

\[
v=T:=L-\tau.
\tag{13}
\]

Repeating the resolved/unresolved cell split of `NB-104` therefore gives the centered limiting moment matrix

\[
\left[
\int_{\max(s,0)}^{T}v^{r+t}e^{-v}\,dv
\right]_{r,t=0}^{d-1}
\tag{14}
\]

when `T>max(s,0)`, and the zero matrix otherwise, together with the prefactor `(12)`. If `s<=0`, `(14)` is the ordinary truncated Laguerre Gram on `[0,T]`. If `s>0`, translating `v=s+w` contributes `e^{-ds}` to its determinant and leaves a unit-triangular polynomial change of basis; this cancels `(12)` and leaves `Delta_d(T-s)`. This proves `(6)` without assigning independent meaning to `x` and `y`.

The same centered-cell estimates also dispose of an exponentially early start. If `s_j->-infinity` while `L_j` remains bounded and the terminal endpoint `T_j=L_j-tau_j` has a finite upper limit, the resolved centered Gram stays bounded after the same transition-strip estimate, whereas `(12)` tends to zero. If the terminal endpoint itself remains below the resolution threshold, all cells are in the oscillatory region and the determinant tends to zero. Thus moving the start exponentially far below the ordinate scale is not an additional high-volume escape.

## 2. Strict monotonicity makes the optimum unique

`NB-103` identifies

\[
\Delta_d(X)
=
\frac{
\det\left[\int_0^X u^{r+t}e^{-u}\,du\right]_{r,t=0}^{d-1}
}{\prod_{k=0}^{d-1}(k!)^2}
\tag{15}
\]

and proves that `Delta_d` is strictly increasing on `(0,infinity)`, with values in `(0,1)`.

The optimization is then rigid. If `s<0` and `T>0`,

\[
\mathcal F_{d,L}(s,\tau)
=e^{ds}\Delta_d(L-\tau)
<\Delta_d(L)
\tag{16}
\]

unless `s=0` and `tau=0`. If `s>=0` and `s<T`,

\[
\mathcal F_{d,L}(s,\tau)
=\Delta_d(L-s-\tau)
\le\Delta_d(L),
\tag{17}
\]

again with equality only at `s=tau=0`. Degenerate cases have zero limit. Hence `(7)`--`(8)`.

The optimum is attainable by integer bands. Take, for example,

\[
m_j=\lceil G_j\rceil,
\qquad
q_j=\left\lfloor\frac{B_j}{m_j}\right\rfloor.
\tag{18}
\]

Because `L>0`, `(1)` implies `B_j/G_j=exp((L+o(1))/(2a_j))`, so `q_j->infinity`. The integer roundings contribute only `o(1)` in the scaled logarithmic coordinates, giving

\[
s_j\to0,
\qquad
\tau_j\to0,
\]

and therefore

\[
\mathcal V^{\mathrm{conf}}_{d,m_j,q_j}(\lambda_j)
\longrightarrow\Delta_d(L).
\tag{19}
\]

Importantly, `s_j->0` does **not** require `m_j/G_j->1`; it requires only

\[
\log(m_j/G_j)=o(1/a_j).
\]

The optimum is an equality of radial scales, not a claim that the two integer indices must be multiplicatively adjacent.

## 3. The finite-section resource is terminal resolution depth

For a nontrivial zeta zero `rho=beta+i gamma`, write

\[
a=\beta-\tfrac12,
\qquad G=|\gamma|.
\]

Under a terminal natural-index budget `B`, the fixed-multiplicity determinant resource is therefore not nominal band depth `2a log q` and not ordinate delay separately. After optimal placement it is

\[
\boxed{
L=2(\beta-\tfrac12)\log\frac{B}{|\gamma|}.
}
\tag{20}
\]

In particular, because `Delta_d` is continuous and strictly increasing from `0` to `1`, for every fixed `eta in (0,1)` let

\[
L_{d,\eta}:=\Delta_d^{-1}(\eta).
\]

Any boundary sequence that retains optimally placed confluent volume at least `eta+o(1)` must pay

\[
\boxed{
B
\ge
|\gamma|\,
\exp\!\left(
\frac{L_{d,\eta}+o(1)}{2(\beta-1/2)}
\right).
}
\tag{21}
\]

Conversely the ordinate-scale placement `(18)` attains the coefficient dictated by this depth. Thus a zero approaching the critical boundary requires exponentially increasing terminal section depth, measured relative to its ordinate, to keep any fixed positive fraction of the confluent determinant volume.

At small terminal resolution depth, `NB-103` gives

\[
\boxed{
\sup_{\text{radially admissible placements}}
\mathcal V^{\mathrm{conf}}_d
\sim
c_d L^{d^2},
\qquad
c_d=
\frac{\prod_{k=0}^{d-1}(k!)^2}
     {\prod_{k=0}^{2d-1}k!}.
}
\tag{22}
\]

Here the supremum is over the boundary-scaled placement regimes classified above. The exponent `d^2` is therefore not repaired by sliding the finite window: terminal resolution depth is the resource that remains after placement has been optimized.

## 4. Controls, prior-art boundary, and what this does not prove

Several controls prevent the optimization from being mistaken for an RH argument.

First, the theorem concerns the analytic confluent continuation of a **fixed-multiplicity determinant volume**. It does not control the canonical state condition number; the Menger-curvature obstruction of `NB-102` remains independent. It also does not treat growing packet size or the causal Jordan realization of a genuine repeated zeta zero.

Second, determinant volume is not target distance. A finite section may have a healthy normalized state volume while the actual Nyman target pairing lies in a weak direction, and conversely a determinant loss need not by itself give a normed dual obstruction. The target-aware finite-section/dual-certificate problem remains separate.

Third, the terminal budget `B` is essential. Without fixing how far the arithmetic section is allowed to extend, one can always enlarge `q` after moving `m`, so there is no meaningful placement optimization. The theorem says that **at fixed terminal scale** the `NB-104` delay cannot be removed for free.

Fourth, the optimum `s=0` is a scaled statement. Ordinary multiplicative perturbations of `m` around `G` disappear after multiplication by `2a`; there is a broad subexponential family of asymptotically equivalent starts.

A targeted prior-art audit across the classical Nyman--Beurling/Baez--Duarte finite-section literature, Burnol's zero-sensitive approximation results, recent Gram-spectral work, Mellin discretization, and truncated Laguerre/Hankel determinants did not identify this terminal-budget placement law. The Laguerre determinant and its monotonicity are classical objects, and no novelty is claimed for them. The line-local contribution is the exact budget identity `(9)`, the ordinate-centered cell reduction `(11)`--`(14)`, and the resulting optimization `(6)`--`(8)`. No new external theorem is load-bearing, so `SOURCES.md` needs no additional dependency.

## 5. Consequence for the research line

`NB-104` left open whether target-aware choice of the band start could simply erase the ordinate delay. Under a finite terminal section budget, `NB-105` closes that placement degree of freedom at fixed multiplicity: starting above the ordinate scale trades delay one-for-one for lost radial depth, while starting below it pays an exponential determinant penalty. The best possible coefficient is exactly `Delta_d(L)` with `L=2a log(B/G)`.

This narrows the next source-to-target bridge. A useful Nyman obstruction no longer needs to control the arbitrary pair `(m,q)` separately at the determinant-volume level; it can ask whether the **terminal resolution depth relative to the zero ordinate** available in the actual finite section is large enough, and then separately determine whether that volume resource couples to the target. Growing multiplicity, Jordan states, diagonal normalization, and target conversion remain genuine new problems rather than band-placement artifacts.
