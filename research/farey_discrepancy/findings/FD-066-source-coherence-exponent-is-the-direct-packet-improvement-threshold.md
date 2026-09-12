# FD-066 — source-coherence exponent is the direct-packet improvement threshold

**Status:** `EXACT-DERIVED + CONDITIONAL-COHERENCE-CLASSIFICATION + RECIPROCAL-FLOOR-JACOBIAN + SOURCE-COUPLED-PACKET + SCHUR-NORMALIZATION + TWO-THIRDS-EXPLANATION + ROUTE-OBSTRUCTION`.

`FD-064` shows that moving a reciprocal-floor host outward converts spare short-interval power into a polynomial packet, but after normalization the best exponent still crosses the deterministic terminal obstruction at `Theta=2/3`. `FD-065` shows that moving the Schur head does not repair this because the denominator saving and the loss of scalar leverage carry a common penalty. Those calculations use the specific Matomäki--Teräväinen transfer budget.

The same barrier has a more invariant formulation. What matters for every **direct local packet around one source spike** is not the host exponent by itself, but the power length of the source window on which the spike stays coherent. If a zero-frontier spike of size `X^(Theta+o(1))` remains of comparable magnitude on a backward window of length `X^(ell+o(1))`, reciprocal-floor geometry converts that window into exactly `X^(lambda+ell-1+o(1))` nearby Jordan rows at a host `q=X^(lambda+o(1))`. After the generic zero-frontier denominator bound and Schur leverage are included, the resulting scalar loss exponent differs from the deterministic terminal exponent by

\[
\boxed{
\frac{2-2\Theta-\ell}{1+\lambda}.
}
\]

The host exponent and every polynomial Schur-head exponent cancel from this comparison. Consequently a direct coherent packet improves the existing terminal scalar obstruction at the power scale **if and only if**

\[
\boxed{\ell>2(1-\Theta).}
\]

The current all-short-interval transfer supplies coherence only up to exponents arbitrarily close to `Theta` on a zero-frontier spike, so this criterion recovers the `Theta=2/3` crossover of `FD-064` without optimizing over the host. More importantly, it identifies what would genuinely change the frontier: for `Theta<2/3`, one needs **super-amplitude coherence**, `ell>Theta`, and in fact the stronger threshold `ell>2(1-Theta)`. A theorem that merely lowers the minimum short-interval length while retaining only an `o(L)` or log-saving error does not change this power currency.

## 1. A source-coherence hypothesis independent of how it is proved

Retain the quotient-shell source

\[
\mathcal H(N)
=\sum_{s\le N}\frac{\mathbf M(\lfloor N/s\rfloor)}s,
\]

and the rightmost zeta-zero frontier

\[
\Theta
:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

By `FD-046`, there is an unbounded spike sequence on which

\[
A_X:=|\mathcal H(X)|=X^{\Theta+o(1)}.
\tag{1}
\]

Fix an exponent

\[
0<\ell<1
\tag{2}
\]

and suppose that, along such a spike sequence, there are lengths

\[
L_X=X^{\ell+o(1)}
\tag{3}
\]

and a fixed constant `c>0` such that

\[
\boxed{
\min_{0\le h\le L_X}
|\mathcal H(X-h)|\ge cA_X.
}
\tag{4}
\]

This is a **conditional coherence surface**, not a claim that the physical source always has such windows. It deliberately forgets how (4) is established. The window may come from an all-interval theorem, an almost-all theorem plus a localization argument, a source-specific correlation theorem, or some future mechanism. The calculation below asks only how much scalar leverage any such window can buy through the existing reciprocal-floor/Jordan packet geometry.

Choose an integer host

\[
q=X^{\lambda+o(1)},
\qquad
\lambda>1-\ell,
\tag{5}
\]

and put

\[
T=qX.
\tag{6}
\]

The inequality in (5) is exactly the condition that the coherent window contain a polynomial number of reciprocal-floor rows. Let a Schur head satisfy

\[
1\le D\le q/2,
\qquad
D=X^{\delta+o(1)},
\qquad
0\le\delta\le\lambda,
\tag{7}
\]

where `delta=0` includes every fixed or subpower head.

## 2. Reciprocal-floor geometry converts source length into row multiplicity

Choose any fixed `0<c_0<1/3` and define

\[
K_X
:=\left\lfloor c_0\frac{qL_X}{X}\right\rfloor.
\tag{8}
\]

Since `L_X=o(X)`, one has `K_X=o(q)`. From (3), (5), and (8),

\[
\boxed{
K_X=X^{\kappa+o(1)},
\qquad
\kappa=\lambda+\ell-1>0.
}
\tag{9}
\]

For `1<=d<=K_X`, set

\[
x_{q,d}:=\left\lfloor\frac{qX}{q+d}\right\rfloor.
\tag{10}
\]

Because `X` is an integer,

\[
X-x_{q,d}
=\left\lceil\frac{dX}{q+d}\right\rceil.
\tag{11}
\]

Uniformly for `d<=K_X`, equations (8) and `K_X=o(q)` give

\[
0\le X-x_{q,d}\le (c_0+o(1))L_X+1<L_X
\tag{12}
\]

for all sufficiently large `X`. Hence the coherence hypothesis (4) yields

\[
\boxed{
|\mathcal H(x_{q,d})|\ge cA_X
\qquad(1\le d\le K_X).
}
\tag{13}
\]

This is the reciprocal-floor Jacobian behind the packet budget. A backward source window of length `L` near `X` occupies row width

\[
\asymp \frac{qL}{X}
\tag{14}
\]

near the host `q`. The relation is geometric and does not depend on a short-interval theorem.

Among `q+1,...,q+K_X`, one residue class modulo `4` is divisible by `4`, so

\[
\#\{1\le d\le K_X:4\mid q+d\}
=\frac{K_X}{4}+O(1).
\tag{15}
\]

All those Jordan rows are nonsquarefree. Since `D<=q/2`, they survive the Schur cut. With

\[
w(r)=\frac{J_2(r)}{r^2}\ge\frac1{\zeta(2)},
\]

the nonsquarefree tail energy therefore satisfies

\[
\boxed{
U_{T,D}
\ge
\left(\frac{c^2}{4\zeta(2)}-o(1)\right)
K_XA_X^2
=X^{2\Theta+\lambda+\ell-1+o(1)}.
}
\tag{16}
\]

Thus the packet power is not an independent variable once a coherent source window is specified: it is the Jacobian image `lambda+ell-1` of that window.

## 3. The normalized scalar exponent has one coherence term and one common head penalty

For every fixed `sigma>Theta`, `FD-046` gives

\[
|\mathcal H(n)|\ll_\sigma n^\sigma.
\tag{17}
\]

Therefore

\[
\begin{aligned}
E_{T,D}
&=\sum_{r>D}w(r)
\mathcal H(\lfloor T/r\rfloor)^2\\
&\ll_\sigma
T^{2\sigma}\sum_{r>D}r^{-2\sigma}
\ll_\sigma T^{2\sigma}D^{1-2\sigma},
\end{aligned}
\tag{18}
\]

with the last factor interpreted as a harmless constant for fixed or subpower `D`. The Schur leverage from `FD-065` is

\[
\Delta_{T,D}=C_T-C_D=X^{-\delta+o(1)}
\tag{19}
\]

at the power scale, and the squarefree-support identity gives

\[
\varepsilon_{T,D}\ge\nu_{T,D}:=rac{U_{T,D}}{E_{T,D}},
\qquad
\mathfrak D_{T,D}
=\Delta_{T,D}\varepsilon_{T,D}.
\tag{20}
\]

Combining (1), (5)--(7), and (16)--(20), then allowing `sigma` to approach `Theta` from the right, gives the direct-coherence scalar loss exponent

\[
\boxed{
\gamma_{\rm coh}(\Theta,\lambda,\ell,\delta)
=
\frac{
1-\ell+(2\Theta-1)\lambda
+2\delta(1-\Theta)
}{1+\lambda}.
}
\tag{21}
\]

Precisely, for every `eta>0`, along the coherent spike sequence,

\[
\boxed{
T^{\gamma_{\rm coh}+\eta}
\mathfrak D_{T,D}\longrightarrow\infty.
}
\tag{22}
\]

The same calculation without the leverage factor gives the corresponding occupation bound. Equation (21) isolates the three costs that had been mixed together in `FD-064`--`FD-065`: reciprocal-floor stretching contributes `1-ell`, the horizon contributes `(2Theta-1)lambda`, and moving the Schur head contributes the already-known `2delta(1-Theta)` penalty.

## 4. Comparison with the terminal obstruction cancels both host and head choices

The deterministic terminal-row mechanism of `FD-032`, normalized exactly as in `FD-065`, has loss exponent

\[
\boxed{
\gamma_{\rm term}(\Theta,\lambda,\delta)
=(2\Theta-1)
+
\frac{2\delta(1-\Theta)}{1+\lambda}.
}
\tag{23}
\]

Subtracting (23) from (21) gives the exact identity

\[
\boxed{
\gamma_{\rm coh}-\gamma_{\rm term}
=
\frac{2-2\Theta-\ell}{1+\lambda}.
}
\tag{24}
\]

The Schur-head exponent disappears completely. More importantly, the host exponent remains only in the positive denominator and therefore cannot change the sign. Hence, among all hosts that actually produce a polynomial packet (`lambda+ell>1`), the coherent packet improves the existing terminal scalar obstruction at the power scale exactly when

\[
\boxed{
\ell>2(1-\Theta).
}
\tag{25}
\]

At equality the two mechanisms tie at the power scale, so constants and subpower factors may still differ but there is no polynomial gain. Below the threshold, moving the host farther out can enlarge the packet but cannot make its normalized scalar bound stronger than the terminal one. Growing the Schur head cannot change that conclusion either.

This gives a sharper interpretation of the normalization barrier. The relevant currency is **source-coherence length**, not raw packet cardinality. Host displacement only converts source length into row count while increasing the physical horizon by the matching amount.

## 5. The `Theta=2/3` crossover is the current coherence ceiling meeting (25)

The Matomäki--Teräväinen all-short-interval input used in `FD-048` and `FD-064` yields, after transfer to `mathcal H`, a log-saving estimate of the form

\[
|\mathcal H(X)-\mathcal H(X-h)|
\ll \frac{h}{(\log X)^c}
\tag{26}
\]

through the relevant all-interval power range, while the exact coefficient law gives the trivial one-Lipschitz control for smaller `h`. On a spike (1), these inputs certify (4) on every fixed power window

\[
L_X=X^{\ell+o(1)}
\qquad\text{with}\qquad
\ell<\Theta,
\tag{27}
\]

subject to the same all-interval threshold already recorded in `FD-064`. Because the spike itself is only specified as `X^(Theta+o(1))`, the endpoint `ell=Theta` is not asserted uniformly at the power boundary.

Combining (25) and (27), the present direct theorem can beat the terminal power exponent only if there exists

\[
2(1-\Theta)<\ell<\Theta,
\]

which is possible exactly when

\[
\boxed{\Theta>\frac23.}
\tag{28}
\]

This recovers the crossover in `FD-064` without optimizing `lambda` or `kappa`. The derivative computation there was a coordinate expression of the more basic comparison (24).

For a false frontier below two thirds, the requirement is qualitatively different:

\[
\Theta<\frac23
\quad\Longrightarrow\quad
2(1-\Theta)>\Theta.
\tag{29}
\]

Thus any direct coherent-packet improvement would require a window whose power length exceeds the spike-amplitude exponent itself:

\[
\boxed{
\ell>2(1-\Theta)>\Theta.
}
\tag{30}
\]

Near the critical line this becomes nearly a linear-scale coherence requirement: as `Theta downarrow 1/2`, the threshold `2(1-Theta)` tends to `1`.

## 6. What kind of stronger source input could actually change the frontier

Equation (25) separates two notions that are easy to conflate. Improving the **minimum interval exponent** on which cancellation is known is not enough by itself. If the estimate on an interval of length `L` is only `o(L)` or `L` times logarithmic savings, then comparing that error with a spike of size `A_X=X^(Theta+o(1))` still limits guaranteed coherence to `ell<=Theta` at the power scale. Such a theorem can make the construction available at more hosts, but it cannot cross (30) when `Theta<2/3`.

What would change the result is an estimate that controls the source variation by `o(A_X)` on windows with

\[
L_X=X^{\ell+o(1)},
\qquad
\ell>2(1-\Theta),
\tag{31}
\]

or a different quantifier mechanism that can locate such coherent windows around the actual zero-frontier spikes. This could come from a genuine power saving in the variation relative to interval length, a source-conditioned mean-square theorem strong enough to localize an adaptive spike, or a different same-horizon relation that avoids paying the reciprocal Jacobian/horizon cost altogether. Those are materially different inputs from making the present all-interval log-saving theorem valid on shorter intervals.

This is consistent with the 2026 almost-all short-interval theory already anchored in `SOURCES.md`: its much lower interval threshold is useful for localization questions, but a global exceptional-set theorem with logarithmic savings does not by itself supply the adaptive super-amplitude coherence (30). `FD-056` already records the separate exceptional-set obstruction to placing the required adaptive start.

## 7. Prior-art boundary and falsification checks

The load-bearing mathematics in (8)--(25) is internal: exact reciprocal-floor geometry, four-adic nonsquarefree density, the Jordan weight bound, the `FD-046` zero-frontier envelope, and the `FD-065` Schur leverage. No external theorem is required for the coherence-threshold classification itself. The Matomäki--Teräväinen theorem is used only in Section 5 to identify the coherence exponent currently available from the existing route, and it is already anchored in `SOURCES.md`.

A targeted literature audit across Farey discrepancy, Mertens/Möbius short intervals, reciprocal-floor hyperbola decompositions, and recent all/almost-all interval results found the expected Farey--Mertens formulas and the Matomäki--Teräväinen short-interval theorems, but no statement matching the threshold (25) for a source-coherent Jordan packet. No novelty is claimed for short-interval cancellation, hyperbola substitutions, or Schur complements in isolation, and `SOURCES.md` requires no new load-bearing anchor.

The main falsification boundary is strict. Condition (4) is an assumption about the **actual source values**, not a consequence of the spike size. Equation (25) says what follows if such a window exists; it does not prove one. The packet must satisfy `lambda+ell>1` to have positive polynomial cardinality, and `ell<1` is used so `K_X=o(q)` in the clean Jacobian form. The comparison is at the power scale only: equality in (25) leaves subpower factors unresolved. Finally, the result applies to the direct local reciprocal-floor packet mechanism. A source-coupled same-horizon denominator estimate, a host-averaging theorem exploiting numerator/denominator correlations, or a genuinely different Farey-order observable could evade this classification because it would change one of the load-bearing normalization steps rather than merely enlarge the same packet.