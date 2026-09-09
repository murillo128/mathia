# XF-129 — upper-half heat histories determine unit-circle divisors up to central rotation

**Status:** `EXACT-DERIVED` + `STRUCTURAL/POSITIVE-BOUNDARY` + `TERMINAL-WINDOW` + `FULL-HISTORY-OBSERVABILITY` + `SHARP-HALF-THRESHOLD`. XF-128 shows that a consecutive terminal window containing any fixed fraction `theta<1/2` of the harmonic histories can remain exactly blind to positive-density double collisions. Its two-shell construction also shows that the missing information is phase-bearing Vieta data below the blind window. The complementary question is whether the half-spectrum scale is merely where that particular adversary breaks, or whether a universal positive boundary appears there.

A universal boundary does appear. Let

\[
E(z,0)=\prod_{j=1}^N(1+\nu_jz)
      =\sum_{k=0}^N E_k z^k,
\qquad |\nu_j|=1,
\tag{1}
\]

and evolve by the exact XF-067 periodic coefficient heat flow

\[
E_k(s)=E_k e^{-\delta_k s},
\qquad
\delta_k=\alpha k(N-k),
\qquad
\alpha:=\frac{4\pi^2}{L^2},
\qquad s\ge0.
\tag{2}
\]

Write `P_m(s)` for the power sums through Newton's logarithmic identity. Then the complete histories

\[
\boxed{
\mathcal H_{>1/2}(E)
:=\{P_m(s):N/2<m\le N,\ s\ge0\}
}
\tag{3}
\]

determine the unit-circle target completely when `N` is odd. When `N` is even they determine it completely except for one exceptional twofold ambiguity: if every proper Vieta shell other than the central shell vanishes, then `E_{N/2}` may be replaced by `-E_{N/2}`. The two exceptional targets are related by a rigid circle rotation, so they have identical root multiplicities, collision geometry, and periodic transition time.

Consequently,

\[
\boxed{
\mathcal H_{>1/2}(E)=\mathcal H_{>1/2}(\widetilde E)
\Longrightarrow
\Lambda_{\rm per}(E)=\Lambda_{\rm per}(\widetilde E)
}
\tag{4}
\]

for unit-circle target slices. Combined with XF-128, this makes `1/2` an asymptotically sharp information threshold for **contiguous terminal blocks of complete harmonic heat histories**: every fraction strictly below `1/2` can be nonidentifying, while the full upper half is universally identifying modulo a harmless rotation.

## 1. Every proper harmonic heat tail directly recovers its own Vieta coefficient

Newton's logarithmic identity gives

\[
A_m(s):=\frac{(-1)^{m-1}}mP_m(s)
=[z^m]\log E(z,s).
\tag{5}
\]

For `m<N`, the linear contribution is

\[
E_m e^{-\delta_m s}.
\tag{6}
\]

Every nonlinear contribution corresponds to a composition

\[
k_1+\cdots+k_j=m,
\qquad j\ge2,
\qquad k_i\ge1,
\tag{7}
\]

and has heat exponent `delta_{k_1}+...+delta_{k_j}`. The quadratic identity used in XF-126 has the exact multi-part form

\[
\boxed{
\sum_{i=1}^j\delta_{k_i}-\delta_m
=2\alpha\sum_{1\le p<q\le j}k_pk_q>0.
}
\tag{8}
\]

Thus every nonlinear partition decays strictly faster than the linear shell `m`. Since there are only finitely many compositions at fixed `m`,

\[
\boxed{
E_m
=
\lim_{s\to\infty}
e^{\delta_m s}
\frac{(-1)^{m-1}}mP_m(s),
\qquad 1\le m<N.
}
\tag{9}
\]

This simple inversion is stronger than the terminal spectroscopy of XF-126 in one important respect: a proper harmonic history carries the **complex phase** of its matching Vieta shell in its slowest heat tail, not merely a magnitude.

At `m=N`, the terminal coefficient has zero heat exponent and every proper composition has positive exponent, so similarly

\[
\boxed{
E_N
=
\lim_{s\to\infty}
\frac{(-1)^{N-1}}N P_N(s).
}
\tag{10}
\]

Hence the upper-half histories in `(3)` recover `E_N` and every coefficient `E_m` with `N/2<m<N` directly.

## 2. Unit-circle self-inversivity reflects the recovered upper half into the lower half

Because every target root lies on the unit circle and `E_0=1`, the Vieta coefficients satisfy the exact self-inversive relation already used in XF-126,

\[
\boxed{
E_{N-k}=E_N\overline{E_k},
\qquad 0\le k\le N.
}
\tag{11}
\]

Therefore every recovered coefficient with `m>N/2` gives the complementary coefficient below `N/2`:

\[
E_k=E_N\overline{E_{N-k}},
\qquad k<N/2.
\tag{12}
\]

If `N` is odd there is no central shell. Equations `(9)`, `(10)`, and `(12)` recover all coefficients `E_0,...,E_N`, hence the complete target polynomial and its root multiset. In particular two unit-circle targets with identical upper-half histories are identical.

This explains why the XF-128 adversary must stop strictly before the half-spectrum boundary. Its first phase-bearing shell `d` lies above `N/2`; once the entire upper half is observed, `(9)` reads that shell directly from its slowest exponential tail.

## 3. For even degree the central coefficient is also forced unless it is the only proper shell

Let

\[
N=2c.
\tag{13}
\]

Suppose two unit-circle targets `E` and `\widetilde E` have the same upper-half histories. By Sections 1--2 they have identical coefficients at every index except possibly `c`; write

\[
C:=E_c,
\qquad
\widetilde C:=\widetilde E_c.
\tag{14}
\]

Assume first that some lower-half proper coefficient is nonzero, and let

\[
r:=\min\{1\le k<c:E_k\ne0\}.
\tag{15}
\]

The harmonic

\[
m=c+r
\tag{16}
\]

belongs to the observed upper half. Compare its logarithmic coefficients for the two targets. Every term not containing the central shell cancels because all other Vieta coefficients agree. A term containing `E_c` can contain it only once because `2c=N>m`; the remaining Vieta indices must sum to `r`. By the minimality of `r`, no nontrivial composition of `r` is supported. Hence the **only** surviving difference is the quadratic pair `(c,r)`:

\[
\boxed{
A_{c+r}(s)-\widetilde A_{c+r}(s)
=-(C-\widetilde C)E_r
e^{-(\delta_c+\delta_r)s}.
}
\tag{17}
\]

Equality of the observed histories and `E_r\ne0` force

\[
\boxed{C=\widetilde C.}
\tag{18}
\]

Thus every even-degree target with at least one noncentral proper shell is reconstructed **exactly** from its upper-half heat histories.

## 4. The sole ambiguity is a rigid rotation of a central-only target

The remaining case is

\[
E_1=\cdots=E_{c-1}=0.
\tag{19}
\]

Self-inversivity then also gives

\[
E_{c+1}=\cdots=E_{N-1}=0,
\tag{20}
\]

so

\[
E(z,0)=1+Cz^c+E_Nz^N.
\tag{21}
\]

The only degree-`N` proper composition is `(c,c)`. Therefore the terminal history is exactly

\[
\frac{(-1)^{N-1}}N P_N(s)
=E_N-\frac12C^2e^{-2\delta_c s}.
\tag{22}
\]

Two targets with the same upper-half histories have the same `E_N`, and `(22)` forces

\[
C^2=\widetilde C^2.
\tag{23}
\]

Hence either `\widetilde C=C` or `\widetilde C=-C`. The second possibility is geometrically harmless. Choose

\[
\omega=e^{i\pi/c},
\qquad
\omega^c=-1,
\qquad
\omega^N=1.
\tag{24}
\]

Then

\[
\widetilde E(z,0)=E(\omega z,0).
\tag{25}
\]

At the root level this is a rigid rotation of the complete divisor. Moreover the diagonal heat flow commutes with this rotation:

\[
\widetilde E(z,s)=E(\omega z,s)
\tag{26}
\]

at every real heat time at coefficient level. Thus the two trajectories have the same root multiplicities and the same real/unit-circle-rooted time set, in particular the same `Lambda_per`.

The ambiguity is therefore an actual symmetry of the periodic problem rather than a loss of transition information.

## 5. The half-spectrum boundary is asymptotically sharp for terminal windows

XF-128 constructs, for every fixed `theta<1/2`, arbitrarily large degrees `N` with a colliding and an all-simple unit-circle target whose complete histories agree on a contiguous terminal block of at least `theta N` coordinates. Those controls have different transition status at the target slice.

XF-129 supplies the converse at the limiting density. Observing

\[
P_m(s),
\qquad N/2<m\le N,
\qquad s\ge0,
\tag{27}
\]

recovers the target polynomial exactly except for the central rotation `(25)`, which preserves all transition geometry. Hence no colliding/simple matched pair can survive the entire upper-half history interface.

So, within the finite periodic model and for **contiguous terminal windows**, the information-theoretic picture is now sharp:

\[
\boxed{
\begin{array}{ll}
\text{every density }\theta<1/2
&\text{can remain collision/transition blind},\\[1mm]
\text{the full upper half}
&\text{determines collision geometry and }\Lambda_{\rm per}.
\end{array}
}
\tag{28}
\]

This does not contradict XF-124--XF-125: those results concern sparse or sublinear collections, while `(27)` uses a structured linear family whose heat tails expose a complete half of the Vieta coordinates and self-inversivity supplies the other half.

## 6. Prior-art and source-specific boundary

The proof uses three algebraic ingredients already present in this line: Newton's logarithmic identity, XF-067's diagonal periodic coefficient heat flow, and unit-circle self-inversivity. The literature audit checked classical Newton-sum reconstruction, self-inversive polynomial theory, and recent polynomial/backward-heat work. Classical theory explains the coefficient symmetry and the ordinary relation between a full prefix of power sums and polynomial coefficients, but I did not find a result matching `(9)`--`(28)`: reconstruction from the **upper half of power-sum heat histories**, with the heat-rate ordering converting high harmonic trajectories into their matching high Vieta coefficients and the even-degree ambiguity classified as a rigid rotation.

No external theorem is load-bearing for the new inversion, and the relevant backward-heat/self-inversive background is already represented in `SOURCES.md`; no source-ledger change is required.

The result is still a periodic observability theorem, not a source theorem for Xi. Current Xi source control in XF-118--XF-123 reaches only `K=o(N)`, far below the half-degree interface `(27)`. Therefore XF-129 does not bound the actual de Bruijn--Newman constant. It does, however, close the purely algebraic question left by XF-128: **cross-shell phase information becomes universally sufficient once the observed terminal histories cover the entire upper half.** The next source-specific gate is whether Xi exposes any compressed observable that recovers comparable upper-half Vieta information without requiring `Theta(N)` independently controlled harmonics.