# PL-462 — Narrow-window phase coherence transfers a modulated raw-moment ceiling to the mod-5 zero-free gate

**Evidence/status:** EXACT-DERIVED + CLASSICAL POSITIVE-PHASE GEOMETRY / CONDITIONAL ZERO-FREE OBSTRUCTION.

**Parent findings:** PL-431 (dyadic carrier phase-locking), PL-446 (finite vertical phase/mean boundary), PL-459 (integrated first-moment gate), PL-461 (single identity-residue raw-moment gate).

## Precise statement

For real \(X\ge 3\), integer \(1\le H\le X/2\), real \(t\), and \(y\in[X,2X]\), define the *uncentered* identity-residue window
\[
P_{1,t}(y)=
\sum_{\substack{y<n\le y+H\\n\equiv1\pmod5}}
\Lambda(n)n^{-it},
\qquad
Q_t(X,H)=\int_X^{2X}|P_{1,t}(y)|^2\,dy.
\]
Write \(\Delta_X=|t|\log(1+H/X)\). Whenever \(0\le\Delta_X\le\pi\), the following comparison holds **unconditionally**, for the actual von Mangoldt source:
\[
\boxed{\cos^2(\Delta_X/2)\,Q_0(X,H)\ \le\
Q_t(X,H)\ \le\ Q_0(X,H).}\tag{1}
\]
No hypothesis about prime distribution or zeros enters (1).

Fix \(0<\theta\le1/2\), put \(H=\lfloor X^\theta\rfloor\), and suppose there are constants \(K_\theta,C_\theta>0\) such that **for every sufficiently large real \(X\)** one can choose *one* real number \(t_X\), with no consistency requirement between scales, satisfying
\[
|t_X|\le K_\theta\frac{X\sqrt{\log(2X)}}{H^{3/2}},
\qquad
Q_{t_X}(X,H)\le\frac{XH^2}{16}
       +C_\theta XH\log(2X).\tag{2}
\]
Then the *unmodulated* one-channel hypothesis of [[research/prime_lattice/findings/PL-461-single-identity-residue-moment-zero-free-gate|PL-461]] follows:
\[
\boxed{Q_0(X,H)\le\frac{XH^2}{16}
               +O_{\theta,K_\theta,C_\theta}(XH\log(2X)).}\tag{3}
\]
Consequently, by PL-461's Landau/Dirichlet argument, **all Dirichlet \(L(s,\chi)\) modulo \(5\) are zero-free in \(\Re s>1-\theta\)**. For \(\theta=1/2\), (2) would imply joint GRH modulo \(5\), including RH; a family of fixed exponents tending to \(1/2\) would have the same implication.

These are deductions **from the unproved prime-moment ceiling in (2)**. Neither (2), GRH nor RH is proved here. The unconditional contribution is the exact transfer (1) and its quantitative precision band (2)--(3).

## Exact positive-arc inequality

Fix \(y\in[X,2X]\). All contributing integers \(n\) lie in \((y,y+H]\). After multiplying \(P_{1,t}(y)\) by the unit phase
\[
e^{itc_y},\qquad c_y=\tfrac12(\log y+\log(y+H)),
\]
the argument of each nonzero term lies in
\[
[-\Delta_y/2,\Delta_y/2],
\qquad
\Delta_y=|t|\log(1+H/y)\le\Delta_X.
\]
Since each coefficient \(\Lambda(n)\) is nonnegative and \(\Delta_X\le\pi\),
\[
\Re(e^{itc_y}P_{1,t}(y))
=\sum_{y<n\le y+H\atop n\equiv1(5)}
\Lambda(n)\cos(t(\log n-c_y))
\ge\cos(\Delta_X/2)P_{1,0}(y)\ge0.
\]
Thus \(|P_{1,t}(y)|\ge\cos(\Delta_X/2)P_{1,0}(y)\). The reverse inequality
\(|P_{1,t}(y)|\le P_{1,0}(y)\) is the triangle inequality.
Squaring and integrating over \(y\) proves (1), including windows with no prime-power terms.

The sector bound is elementary and sharp **as a local positive-coefficient inequality**: two equal masses placed at the endpoints of a phase arc have modulus ratio \(\cos(\Delta_y/2)\). This sharpness control is not a model of primes and does not claim an attained global \(Q_t/Q_0\) ratio.

## The covariance-scale frequency band

For the selected frequencies in (2),
\[
\Delta_X\le |t_X|H/X
\le K_\theta\sqrt{\frac{\log(2X)}{H}}=o(1)
\quad (X\to\infty).
\]
Hence \(\sec^2(\Delta_X/2)=1+O_{K_\theta}(\log(2X)/H)\).
By (1) and (2),
\[
\begin{aligned}
Q_0
&\le\sec^2(\Delta_X/2)\,Q_{t_X}\\
&\le\left(1+O_{K_\theta}\left(\frac{\log(2X)}{H}\right)\right)
  \left(\frac{XH^2}{16}+C_\theta XH\log(2X)\right)\\
&=\frac{XH^2}{16}
  +O_{\theta,K_\theta,C_\theta}(XH\log(2X)).
\end{aligned}
\]
In the last step \(H=\lfloor X^\theta\rfloor\gg_\theta\log X\) for every fixed \(\theta>0\). This proves (3) without requiring the modulation to be fixed, small in absolute size, or available uniformly on an interval of frequencies.

The admitted frequency size is
\[
|t_X|=O_\theta\bigl(X^{1-3\theta/2}\sqrt{\log X}\bigr).
\]
At square-root window length \(H=\lfloor\sqrt X\rfloor\), this allows
\[
\boxed{|t_X|=O(X^{1/4}\sqrt{\log X}).}\tag{4}
\]
The relevant small parameter is the **relative within-window phase spread**
\(|t_X|H/X\), not \(|t_X|\) itself or the large common carrier phase
\(t_X\log y\).

For a generic positive two-atom window, the local loss from (1) is of order
\(\Delta_X^2Q_0\) as \(\Delta_X\to0\). When \(Q_0\) is of leading size
\(XH^2\), keeping this deterministic loss at or below the
\(XH\log X\) tolerance therefore naturally demands
\(\Delta_X^2=O(\log X/H)\), which is precisely the scale used in (2).
This is a sharpness statement for **the positivity-only transfer method**,
not a necessity theorem about actual prime moments.

## Arithmetic implication and audit boundaries

The arithmetic step is exactly PL-461, not an additional theorem about primes: its single identity-residue uncentered moment ceiling implies a one-sided bound for \(\psi_1(x)-x/4\), and Landau positivity plus the Dedekind-zeta factorization
\[
\prod_{\chi\bmod5}L(s,\chi)
=(1-5^{-s})\zeta_{\mathbb Q(\zeta_5)}(s)
\]
excludes zeros in the stated half-plane. That step relies on the special modulus-\(5\) real-axis nonvanishing check and on the bound holding for every sufficiently large real \(X\). It should not be transplanted to an arbitrary residue, modulus or generalized-prime system without new hypotheses.

The phase inequality itself applies to any nonnegative source weights supported on multiplicatively narrow windows and is therefore **not** a new prime-lattice spectral selector. The distinguished-prime consequence appears only after importing the assumed arithmetically precise upper moment in (2) and the already established PL-461 zero-free bridge. In particular:

- A **centered** or signed window may have cancellations in its coefficients, so (1) does not bound its moment from below. A centered variance or a lower-frame estimate is not a substitute for (2).
- A moment ceiling merely at sparse \(X\)-scales does not give PL-461's dyadic zero-free implication. The frequency \(t_X\) may vary with \(X\), but the ceiling must hold on *all* sufficiently large real scales.
- Frequencies at which \(|t|H/X\) stays bounded away from zero can lose a leading-order fraction of the raw energy. The present precision transfer no longer follows from (1) in that regime, although different arithmetic information might still be usable.
- Ordinary prime short-interval equidistribution, universal Bohr-phase dephasing, and positivity of a Gram matrix do not prove the ceiling in (2).

Positive-coefficient arc geometry and narrowband carrier separation are classical; PL-431 already uses a different dyadic phase-locking estimate, while PL-446 exposes the noncommutation of vertical averaging and polynomial-window limits. The Mellin/Landau implication is inherited from PL-460--PL-461 (sources 120--122 in SOURCES.md). Targeted prior-art comparison with standard Dirichlet-polynomial phase estimates and short-interval prime moment literature gave no reason to label the sector inequality itself novel. The line-specific result is the quantitative logical restriction on **one arbitrarily selected mesoscopic twisted raw-moment estimate per scale**: within (2), such an estimate is already GRH-strength at the square-root endpoint and cannot provide an independent shortcut around the zero-free obstruction.