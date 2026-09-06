# XF-066 — fourth-difference ratio converts slow-band concentration into a local state criterion

**Status:** `EXACT-DERIVED` + `STATE-SPACE-BAND-CERTIFICATE` + `PHYSICAL-SPACE-REFINEMENT` + `STRUCTURAL/REPAIR`. XF-065 turns the exact nonlinear moving-line selector into a state-space theorem, but still leaves one explicitly Fourier-side hypothesis: the third-difference energy must be concentrated in the shrinking slow band. That spectral hypothesis has a simple deterministic sufficient condition in physical index space. One additional discrete derivative controls the ultraviolet tail, while bounded displacement oscillation controls the infrared tail.

Use the XF-062--XF-065 scales

\[
q\asymp\log^2 T,
\qquad
M=q^2,
\qquad
N=2M,
\tag{1}
\]

and let `a` be any real `N`-periodic displacement. Remove its exact translation mode as in XF-065,

\[
c:=\frac1N\sum_j a_j,
\qquad
b_j:=a_j-c,
\qquad
A:=\|b\|_{\ell^\infty}.
\tag{2}
\]

For principal frequencies `xi_ell in (-pi,pi]`, put

\[
m(\xi):=e^{i\xi}-1
\tag{3}
\]

and define the full third-difference energy

\[
\boxed{
Q_3(b)
:=M^3\|\Delta^3 b\|_2^2
=M^3\sum_\ell |m(\xi_\ell)|^6|\widehat b_\ell|^2.
}
\tag{4}
\]

Whenever `Q_3(b)>0`, define the local fourth/third smoothness ratio

\[
\boxed{
R_4(b)
:=\frac{\|\Delta^4b\|_2}{\|\Delta^3b\|_2}.
}
\tag{5}
\]

Fix the same constant `C>0` as in the XF-063--XF-065 frame and write the symmetric inner band as

\[
B_T^{\rm in}
:=
\left\{
\xi:
2q^{-3/2}\le |\xi|\le
\theta_+
\right\},
\qquad
\theta_+:=\frac{C\log\log T}{q}.
\tag{6}
\]

Then for all sufficiently large `T`,

\[
\boxed{
\frac{\mathcal Q_M(( -\pi,\pi]\setminus B_T^{\rm in};b)}{Q_3(b)}
\le
\frac{128A^2}{q\,Q_3(b)}
+
\left(
\frac{\pi R_4(b)}{2\theta_+}
\right)^2.
}
\tag{7}
\]

Here `mathcal Q_M` is exactly the XF-065 energy, so `Q_3(b)=mathcal Q_M(( -pi,pi];b)`. Consequently,

\[
\boxed{
\frac{A^2}{qQ_3(b)}=o(1),
\qquad
R_4(b)=o\!\left(\frac{\log\log T}{q}\right)
}
\tag{8}
\]

imply the relative band-concentration hypothesis of XF-065:

\[
\mathcal Q_M(( -\pi,\pi]\setminus B_T^{\rm in};b)
=o\!\left(\mathcal Q_M(B_T^{\rm in};b)\right).
\tag{9}
\]

In particular, the following is a completely state-based sufficient package for the exact nonlinear selector frame:

\[
\boxed{
A=O(1),
\qquad
D:=\|\Delta b\|_\infty
=o\!\left((\log\log T)^{-2}\right),
\qquad
\liminf_{T\to\infty}Q_3(b)>0,
\qquad
R_4(b)=o\!\left(\frac{\log\log T}{q}\right).
}
\tag{10}
\]

Under (10), XF-065 gives

\[
\boxed{
\|\mathcal N_{M,a}\|_{X_T}^2
\ge
\left(\frac{C_g}{4}+o(1)\right)Q_3(b),
}
\tag{11}
\]

where `mathcal N_{M,a}` and `X_T` are the exact finite-displacement selector and weighted selector norm of XF-065. Thus the remaining Fourier projector in the nonlinear destination theorem can be replaced by sup-norm gap geometry plus the local finite-difference quantities `Delta^3 b` and `Delta^4 b`.

This still does **not** show that an actual Xi transition slice satisfies (10), that nontrivial transition mass survives until it does, or that the real-simple description crosses a collision or complex-root interval. The result only converts the destination-side slow-band condition into a concrete local smoothness target.

## 1. One additional derivative controls the ultraviolet tail

For principal `|xi|<=pi`,

\[
|m(\xi)|
=2\sin\frac{|\xi|}{2}
\ge \frac{2}{\pi}|\xi|.
\tag{12}
\]

Hence every mode with `|xi|>theta_+` satisfies

\[
|m(\xi)|^{-2}
\le
\frac{\pi^2}{4\theta_+^2}.
\tag{13}
\]

Therefore Parseval gives

\[
\begin{aligned}
\mathcal Q_M(|\xi|>\theta_+;b)
&=M^3\sum_{|\xi_\ell|>\theta_+}
|m(\xi_\ell)|^6|\widehat b_\ell|^2\\
&\le
\frac{\pi^2}{4\theta_+^2}
M^3\sum_\ell
|m(\xi_\ell)|^8|\widehat b_\ell|^2\\
&=
\left(\frac{\pi R_4(b)}{2\theta_+}\right)^2Q_3(b).
\end{aligned}
\tag{14}
\]

No evolution equation, periodic tangent semigroup, spectral-support assumption, or pointwise Fourier estimate enters (14). It is simply the exact spectral Markov estimate associated with one more discrete derivative.

The scale in (8) is natural. For a single Fourier mode `b_j=A_0 e^{i\xi j}` (or its real cosine),

\[
R_4(b)=|m(\xi)|.
\tag{15}
\]

Thus a mode at wavelength `asymp q` has `R_4=asymp q^{-1}` and lies safely below the `log log T/q` ultraviolet threshold, while a mode sitting at the upper frame edge has `R_4=asymp log log T/q` and cannot satisfy the little-`o` condition. The criterion does not gain its conclusion by hiding a larger frequency scale in constants.

## 2. Bounded displacement oscillation controls the infrared tail

At the lower edge of (6), `|m(xi)|<=|xi|` gives

\[
\begin{aligned}
\mathcal Q_M(|\xi|<2q^{-3/2};b)
&\le
M^3(2q^{-3/2})^6\|b\|_2^2\\
&\le
64M^3q^{-9}\,NA^2.
\end{aligned}
\tag{16}
\]

Since `N=2M` and `M=q^2`, this is exactly

\[
\boxed{
\mathcal Q_M(|\xi|<2q^{-3/2};b)
\le
\frac{128A^2}{q}.
}
\tag{17}
\]

Combining (14) and (17) yields (7). If the two terms on the right of (7) are `o(1)`, then

\[
\mathcal Q_M(B_T^{\rm in};b)
=(1-o(1))Q_3(b),
\tag{18}
\]

which is equivalent to (9).

The infrared estimate also explains why a nontriviality hypothesis is needed. A sequence may satisfy an excellent derivative ratio while its entire third-difference energy tends to zero. Condition `A^2/(qQ_3)=o(1)` separates spectral concentration from survival of the transition-scale quantity. The convenient source-scale specialization `A=O(1)` and `liminf Q_3>0` makes this automatic.

## 3. XF-065 then removes the measurement nonlinearity

XF-065 proves that for bounded displacement oscillation it is enough to have

\[
D=o\!\left((\log\log T)^{-2}\right)
\tag{19}
\]

to make its three nonlinear measurement parameters `alpha+beta+gamma` tend to zero. Equations (8)--(9) supply the other hypothesis of that theorem without mentioning Fourier projections in the assumptions.

Thus (10) has a useful division of labor. `A` and `D` control finite-amplitude evaluation of the moved points; `Q_3` says that the transition-scale third-difference content has not disappeared; and `R_4` says that this content has become sufficiently smooth in index space that an order-one fraction cannot remain above the source-controlled selector cone. The exact selector lower frame (11) follows immediately.

The new target is therefore compatible with genuinely nonlinear methods. A direct gap-flow estimate, entropy inequality, or collision-safe coordinate argument need not identify individual Fourier modes if it can instead prove a scale-sharp differential smoothing estimate of the form

\[
\|\Delta^4b\|_2
=o\!\left(\frac{\log\log T}{q}\right)
\|\Delta^3b\|_2
\tag{20}
\]

while preserving `Q_3` and the small-distortion geometry long enough to apply XF-065.

## 4. The sparse static escape is rejected for the right reason

XF-061's static obstruction moves a single root by an amount of order `M^{-1}`. After subtracting the irrelevant mean, its discrete derivatives are those of a point mass. Away from the harmless periodic wrap,

\[
\|\Delta^3\delta_0\|_2^2
=1+9+9+1=20,
\tag{21}
\]

and

\[
\|\Delta^4\delta_0\|_2^2
=1+16+36+16+1=70.
\tag{22}
\]

Hence its smoothness ratio is amplitude-independent and exactly

\[
\boxed{
R_4(\delta_0)=\sqrt{\frac72}.
}
\tag{23}
\]

This is vastly larger than `log log T/q`. The physical-space certificate therefore excludes the same sparse high-frequency escape that forced XF-062 to introduce positive-time smoothing, without merely assuming that the defect has no high-frequency mass.

Conversely, for a coherent mode at `|xi|=asymp q^{-1}`, equation (15) gives `R_4=asymp q^{-1}=o(log log T/q)`. The criterion distinguishes the sparse and coherent regimes exactly through local discrete smoothness.

## 5. Prior-art and novelty boundary

The derivative-to-spectral-tail implication in (14) belongs to classical Fourier/Bernstein and reverse-Bernstein/Poincare territory: high-frequency mass is controlled by paying an additional derivative. A targeted audit of standard Bernstein inequalities and modern reverse-Bernstein formulations on the circle found no reason to treat that analytic principle as new. Here no external theorem is load-bearing because (12)--(14) are a one-line Parseval calculation on the finite cyclic group.

The line-specific content is the scale match. The `q^2` selector window of XF-063--XF-065, its `M^3 H^3` normalization, the unusual infrared edge `q^{-3/2}`, and the source-controlled ultraviolet edge `log log T/q` combine to give the quantitative certificate (7) and the fully physical state package (10). No broad novelty claim is made for derivative tail inequalities themselves, and no new `SOURCES.md` anchor is required.

## 6. Consequence for `xi_flow`

After XF-065, the main unresolved destination hypothesis was a relative Fourier-band concentration statement. Equation (7) replaces it by a local fourth/third-difference ratio plus an explicit infrared error. This narrows the nonlinear transport problem: it is enough to prove that a hypothetical positive-`Lambda` transition reaches a real-simple slice with small relative gap distortion, nonvanishing third-difference energy, and the scale separation (20) before the relevant defect disappears.

The hard implication is still dynamical and Xi-specific. Nothing here proves such a slice exists, controls exterior replenishment in a nonperiodic block, or carries the state through a collision. But a future smoothing theorem can now target a concrete finite-difference ratio rather than the full moving spectral projector of XF-065, and the target is sharp enough to separate the known sparse static obstruction from memory-scale coherent structure.