# XF-143 — two half-spacing real heat traces determine the full periodic polynomial state

**Status:** `EXACT-DERIVED` + `STRUCTURAL/POSITIVE-BOUNDARY` + `TWO-POINT-OBSERVABILITY` + `REAL-AXIS` + `ROOT-SPACING-LOCAL` + `TARGET-GENERAL`. XF-130 compresses all reflected Vieta shells into one heat trace by moving one root-spacing off the real axis, but it needs unit-circle self-inversivity to separate the paired rates `k` and `N-k`. XF-142 then shows that same-slice heat-time derivatives do not add a genuinely new observation axis. A different local repair is available: use two spatial samples, both on the real axis, separated by only half a mean root spacing. Their full heat histories determine every polynomial coefficient exactly, with no root-location or self-inversive hypothesis.

## Result / observations

Let

\[
E(w,s)=\sum_{k=0}^N E_k e^{-\delta_k s}w^k,
\qquad
\delta_k=a k(N-k),
\qquad a>0,
\tag{1}
\]

be an arbitrary degree-`N` polynomial state under the exact XF-067 coefficient heat flow. No assumption is made that the roots lie on the unit circle. Choose any `zeta_*` with `|zeta_*|=1` and define two nearby real-axis sampling phases

\[
\zeta_\pm
:=
\zeta_*\exp\!\left(\pm\frac{i\pi}{2(N+1)}\right).
\tag{2}
\]

Observe only the two complex scalar histories

\[
\boxed{
Q_\pm(s):=E(\zeta_\pm,s),
\qquad s\ge0.
}
\tag{3}
\]

Then the pair `(Q_+,Q_-)` determines every coefficient `E_0,...,E_N`, hence the complete polynomial state and its root multiset with multiplicity. More precisely, once the distinct heat-rate amplitudes have been extracted from the two traces, every reflected pair `(E_k,E_{N-k})` is recovered by a `2x2` spatial system whose inverse amplification is `O(N)`. This `O(N)` order is unavoidable for any two probes separated by `O(L/N)` because the reflected pair nearest the central shell has phase gap `1` or `2`.

In the physical periodic coordinate of XF-067, `(2)` corresponds to two **real** positions symmetric about one center and separated by

\[
\boxed{
\Delta x=\frac{L}{2(N+1)}
=\left(\frac12+o(1)\right)\frac LN.
}
\tag{4}
\]

Thus exact target-state identifiability requires neither an off-real evaluation nor `Theta(N)` separate harmonic channels: two real heat traces inside a window of asymptotically half one mean root spacing suffice.

## 1. Heat time isolates reflected Vieta pairs

The heat rates obey

\[
\delta_k=\delta_{N-k}
\tag{5}
\]

and are strictly increasing for

\[
0\le k\le\lfloor N/2\rfloor.
\tag{6}
\]

Therefore each trace in `(3)` has the finite spectral decomposition

\[
Q_\pm(s)
=
\sum_{k=0}^{\lfloor N/2\rfloor}
B_{\pm,k}e^{-\delta_k s},
\tag{7}
\]

where, for `k<N/2`,

\[
\boxed{
B_{\pm,k}
=
E_k\zeta_\pm^k
+
E_{N-k}\zeta_\pm^{N-k},
}
\tag{8}
\]

and, when `N=2c`, the central shell is unpaired:

\[
B_{\pm,c}=E_c\zeta_\pm^c.
\tag{9}
\]

Because the rates in `(7)` are known and distinct, exact knowledge of either full trace determines all of its amplitudes. One may use successive tail peeling, or equivalently the first `floor(N/2)+1` heat-time derivatives at one time and the resulting finite Vandermonde system. Equality of traces on any nonempty open heat-time interval is also enough by analyticity.

The only exact degeneracy left by heat time is therefore the pair `(k,N-k)`. Unlike XF-130, we do not resolve it by imposing self-inversivity. The second spatial sample resolves it directly.

## 2. Half-spacing phase separation uniformly breaks every reflected pair

For each `k<N/2`, equation `(8)` gives

\[
\begin{pmatrix}
B_{+,k}\\
B_{-,k}
\end{pmatrix}
=
\begin{pmatrix}
\zeta_+^k & \zeta_+^{N-k}\\
\zeta_-^k & \zeta_-^{N-k}
\end{pmatrix}
\begin{pmatrix}
E_k\\
E_{N-k}
\end{pmatrix}.
\tag{10}
\]

Let

\[
\omega_N:=\frac{\zeta_+}{\zeta_-}
=e^{i\pi/(N+1)}.
\tag{11}
\]

Since both sampling points have unit modulus, the determinant in `(10)` has magnitude

\[
\begin{aligned}
|\Delta_k|
&=
\left|
\omega_N^{N-k}-\omega_N^k
\right|\\
&=
2\left|
\sin\!\left(
\frac{(N-2k)\pi}{2(N+1)}
\right)
\right|.
\end{aligned}
\tag{12}
\]

For `k<N/2`, the integer `d=N-2k` satisfies `1<=d<=N`, so the angle in `(12)` lies strictly between `0` and `pi/2`. Consequently

\[
\boxed{
|\Delta_k|
\ge
2\sin\!\left(\frac{\pi}{2(N+1)}\right)
\ge
\frac{2}{N+1}.
}
\tag{13}
\]

Every reflected pair is therefore uniquely recoverable. Since all entries of the matrix in `(10)` have modulus one, its inverse has operator norm at most `C(N+1)` for an absolute constant `C`. The even central coefficient in `(9)` is recovered from either trace with unit modulus. Hence

\[
\boxed{
(Q_+(\cdot),Q_-(\cdot))
\quad\Longrightarrow\quad
(E_0,\ldots,E_N)
}
\tag{14}
\]

exactly, for arbitrary complex coefficients.

This removes both structural assumptions used by XF-130. The probes remain on `|zeta|=1`, and no relation between `E_k` and `E_{N-k}` is required.

## 3. The `O(N)` spatial conditioning is the correct local order

The linear loss in `(13)` is not an artifact of the particular half-spacing choice. Suppose two unit-circle probes have phase separation

\[
\phi_N=O(1/N).
\tag{15}
\]

For the reflected pair nearest the center, `d=N-2k` equals `1` when `N` is odd and `2` when `N` is even. Its determinant is

\[
2|\sin(d\phi_N/2)|=O(1/N).
\tag{16}
\]

Thus any two-probe demixing scheme confined to root-spacing spatial separation has worst inverse amplification at least `Omega(N)` on the raw reflected-pair coordinates. The construction `(2)` attains the matching `O(N)` upper bound simultaneously for every pair. In this precise sense its spatial conditioning is order-optimal among two real-axis probes that remain `O(L/N)` apart.

This statement concerns only the **spatial reflected-pair inversion** after the heat-rate amplitudes `B_{\pm,k}` are known. It does not claim that extracting all amplitudes from noisy finite-time traces is polynomially stable. The distinct rates near the central heat spectrum can still be difficult to separate; XF-132 already shows exponential ill-conditioning for the corresponding one-trace zero-delay spectral inversion. Whether two real traces admit a direct stable transition decoder that avoids full spectral tomography remains open.

## 4. Physical realization uses two points inside one root-spacing window

XF-067 writes the normalized periodic heat representative in the form

\[
G(z,s)
=A_0(s)e^{\pi iNz/L}
E\!\left(-e^{-2\pi iz/L},s\right).
\tag{17}
\]

For real `z=x`, the polynomial sampling variable

\[
\zeta(x)=-e^{-2\pi ix/L}
\tag{18}
\]

lies exactly on the unit circle. Choose a real center `x_*` and the symmetric points

\[
x_\pm
=
x_*\mp\frac{L}{4(N+1)}.
\tag{19}
\]

Then

\[
\frac{\zeta(x_+)}{\zeta(x_-)}
=e^{i\pi/(N+1)},
\tag{20}
\]

which is exactly `(11)`, while

\[
|x_+-x_-|
=
\frac{L}{2(N+1)}.
\tag{21}
\]

After dividing out the known nonzero outer carrier `A_0(s)e^{pi i N x/L}`, the two real physical heat traces are precisely `Q_+` and `Q_-`. If the mean periodic root spacing is `ell=L/N`, each sample is only

\[
\frac{L}{4(N+1)}
=\left(\frac14+o(1)\right)\ell
\tag{22}
\]

from the common center. The complete observation aperture has asymptotic diameter `ell/2`.

This is materially more source-facing than the positive interface of XF-130: the latter needs one complex value at imaginary height `Theta(L/N)`, whereas `(19)` stays entirely on the real axis and replaces the missing self-inversive relation by one additional nearby sample.

## 5. Consequence for collision and transition identifiability

Suppose two degree-`N` periodic target states `E` and `\widetilde E` satisfy

\[
Q_\pm(s)=\widetilde Q_\pm(s)
\qquad
\text{for all }s\ge0
\tag{23}
\]

at the two phases `(2)`. Section 1 gives equality of every spectral amplitude `B_{\pm,k}`, and section 2 then gives

\[
E_k=\widetilde E_k
\qquad(0\le k\le N).
\tag{24}
\]

Hence the two polynomials agree exactly, including all roots and multiplicities. Their coefficient heat trajectories agree for every heat time, so in particular

\[
\boxed{
(Q_+(\cdot),Q_-(\cdot))
=(\widetilde Q_+(\cdot),\widetilde Q_-(\cdot))
\Longrightarrow
\Lambda_{\rm per}(E)=\Lambda_{\rm per}(\widetilde E).
}
\tag{25}
\]

The matched collision-blind controls from the negative frontier therefore cannot reproduce these two complete real traces unless they reproduce the entire polynomial state. This is a genuine positive boundary after XF-142: adding instantaneous time derivatives at one point is redundant, but adding a second **spatially separated** point breaks the reflected-shell degeneracy exactly.

## 6. Prior-art boundary and next Xi-specific gate

The literature audit found the expected classical neighborhood: finite-sensor observability for parabolic equations goes back at least to work such as Sakawa's observability criteria, later point-sensor work studies heat observability from moving or scanning point measurements, and generalized Prony methods recover finite exponential sums from suitable samples. These establish that finite spatial sensing and exponential-mode recovery are standard themes. No external theorem is load-bearing here: equations `(7)`--`(13)` are the explicit finite spectrum of XF-067 followed by a two-by-two phase inversion, and `(19)` is the internal periodic coordinate map. `SOURCES.md` therefore needs no new anchor.

The remaining issue is quantitative and source-specific rather than algebraic. The true Xi source must provide two normalized real traces at separation `Theta(L/N)` over enough positive heat time, with errors small enough to survive whatever temporal decoder is used. The present theorem deliberately avoids claiming that the full spectral Vandermonde is stable. A sharper next target is to find a **direct two-trace transition observable** on a positive heat interval that uses the spatial demixing in `(10)` without reconstructing every central heat mode individually, or else to prove a relative Xi-to-periodic transport estimate for these two real traces and quantify the resulting conditioning.

This narrows the positive side of the frontier cleanly: after XF-142, a richer instantaneous jet is not new information; after XF-143, one additional real sample only half a root spacing away is already enough for exact full-state identifiability. What remains is to turn that exact two-point observability into a quantitatively stable Xi-scale certificate.