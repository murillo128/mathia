# RE-148 — early-window dilation removes location synchronization but exposes a rate gap

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + LEADING-ROBIN-PACKET + POSITIVE-MEASURE + RECIPROCAL-BOX + EARLY-WINDOW-LOCALIZATION + SCALE-MAXIMAL-SPLICE + PINTZ-SHELL + EXPONENTIAL-RATE-GAP + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-145` proves a cardinality-free `exp(-O(R))` visibility floor for a positive reciprocal-box packet, but states it on the full terminal interval `[(1-kappa)U,U]`. `RE-147` makes the sufficiently-rightward exterior shell small only on an earlier subwindow `[(1-kappa)U,(1-eta)U]`, and therefore leaves witness synchronization as an explicit unresolved item.

The location part of that synchronization problem is in fact removable at no change of functional order. The positive-measure theorem of `RE-145` is covariant under dilation of the observation variable, so its witness can be forced into **any fixed nonempty early subwindow**. Splicing this localized floor with the uniform `RE-147` shell estimate puts both statements at the same observation point.

The splice does not close Robin visibility. It instead exposes a sharper obstruction: with the explicit constants currently proved, the local floor deteriorates as `e^{-C_loc R}` with `C_loc>19`, whereas the Pintz shell improves only as `e^{-c_sh R}` with `c_sh<1/2`. Thus increasing a common reciprocal radius makes the available shell-versus-floor comparison worse, not better. The unresolved synchronization is therefore quantitative rather than positional: one needs a substantially sharper local exponent, a stronger source-specific exterior exponent, or new control of the near-left / vertically remote pieces.

Fix

\[
0<\eta<\kappa<\frac12,
\qquad
J_{\kappa,\eta}:=[1-\kappa,1-\eta].
\tag{1}
\]

## 1. The `RE-145` positive-measure floor localizes to the early subwindow by exact dilation

Let `mu` be a Borel probability measure supported on

\[
\mathcal K_R
=\{\lambda\in\mathbb C:|\Re\lambda|\le R,\ |\Im\lambda|\le R\},
\tag{2}
\]

and write

\[
F_\mu(x)=\int_{\mathcal K_R}e^{\lambda x}\,d\mu(\lambda).
\tag{3}
\]

Set

\[
b:=1-\eta,
\qquad
\kappa_{\rm eff}
:=1-\frac{1-\kappa}{1-\eta}
=\frac{\kappa-\eta}{1-\eta}.
\tag{4}
\]

Because `0<eta<kappa<1/2`, one has `0<kappa_eff<1/2`. Define

\[
G_\mu(y):=F_\mu(by).
\tag{5}
\]

Pushing `mu` forward by `lambda -> b lambda` shows that `G_mu` is again the Laplace transform of a probability measure, now supported on `K_(bR)`. Moreover,

\[
y\in[1-\kappa_{\rm eff},1]
\quad\Longleftrightarrow\quad
by\in[1-\kappa,1-\eta].
\tag{6}
\]

Applying `RE-145` verbatim to `G_mu` therefore gives

\[
\boxed{
\sup_{x\in J_{\kappa,\eta}}|F_\mu(x)|
\ge
q_{\kappa,\eta}(R)
:=
\frac12
\left(
\frac{\kappa-\eta}{2e(1-\eta)}
\right)^{16(1+(1-\eta)R)}.
}
\tag{7}
\]

Equivalently,

\[
q_{\kappa,\eta}(R)
=c_{\kappa,\eta}
 e^{-C_{\kappa,\eta}R},
\tag{8}
\]

where

\[
c_{\kappa,\eta}
=
\frac12
\left(
\frac{\kappa-\eta}{2e(1-\eta)}
\right)^{16},
\tag{9}
\]

and

\[
\boxed{
C_{\kappa,\eta}
=
16(1-\eta)
\log\!\frac{2e(1-\eta)}{\kappa-\eta}.
}
\tag{10}
\]

No new interpolation theorem is being asserted here: (7) is an exact rescaling corollary of the representation-level result already proved in `RE-145`. What is new and load-bearing for the line is that its witness can be placed inside exactly the early interval on which `RE-146/147` price the rightward exterior.

## 2. The real Robin carrier also localizes to the same early window

Use the leading reciprocal-box packet and notation of `RE-145`. At scale `U`, let `rho_0=beta_0+i gamma_0` be the distinguished positive-ordinate atom, with `gamma_0>=gamma_*>0`, and let `C_U` be a finite nonempty packet satisfying

\[
|\beta-\beta_0|\le\frac{R(U)}U,
\qquad
|\gamma-\gamma_0|\le\frac{R(U)}U.
\tag{11}
\]

For the leading Robin coefficient

\[
d_\rho=\frac1{\rho(1-\rho)},
\qquad
 a_{\rho,0}(u)
=e^{-(\Theta-\beta)u}d_\rho,
\tag{12}
\]

the same coefficient comparison as `RE-145` gives, after writing `u=Ux` and dividing by `N_U=#C_U`,

\[
\frac1{N_U}
\sum_{\rho\in C_U}a_{\rho,0}(Ux)e^{i\gamma Ux}
=
e^{-(\Theta-\beta_0)Ux}
 d_{\rho_0}e^{i\gamma_0Ux}
\bigl(Q_U(x)+E_U(x)\bigr),
\tag{13}
\]

where `Q_U` is the Laplace transform of the empirical probability measure on `K_(R(U))`. On `J_(kappa,eta)` the same calculation can be kept slightly sharper than on the full interval:

\[
\|E_U\|_{L^\infty(J_{\kappa,\eta})}
\ll
\frac{(1+R(U))e^{(1-\eta)R(U)}}U,
\tag{14}
\]

and

\[
\|Q_U'\|_{L^\infty(J_{\kappa,\eta})}
\le
\sqrt2 R(U)e^{(1-\eta)R(U)}.
\tag{15}
\]

By (7), some `x_0 in J_(kappa,eta)` has `|Q_U(x_0)|>=q_(kappa,eta)(R(U))`. Exactly as in the carrier-transfer step of `RE-145`, take a one-sided neighborhood of `x_0` contained in the same fixed interval. If

\[
R(U)=o(\log U),
\tag{16}
\]

then (14) is `o(q_(kappa,eta))`, while the neighborhood on which `Q_U` changes by only a fixed fraction of `q_(kappa,eta)` still has length `U^{-o(1)}`. Since `gamma_0 U >> U`, the carrier makes many full turns on that neighborhood. Hence there is an

\[
x_U\in J_{\kappa,\eta}
\tag{17}
\]

for which the real packet satisfies the synchronized floor

\[
\boxed{
|\mathcal S_{C_U,0}(Ux_U)|
\gg_{\kappa,\eta}
 e^{-C_{\kappa,\eta}R(U)}
 N_U |a_{\rho_0,0}(Ux_U)|.
}
\tag{18}
\]

The important normalization in (18) is the anchor **at the same observation point** `Ux_U`, rather than the conservative terminal-scale normalization used in the displayed corollary of `RE-145`. This is exactly what is needed for comparison with the shell estimate of `RE-147`.

The argument uses no zero spacing and no cardinality bound. Positivity enters only through the empirical probability measure, exactly as in `RE-145`; the fast carrier and coefficient perturbation are handled after the complex floor is localized.

## 3. Pintz's rightward shell and the local floor now hold at the same point

Assume the finite edge lies in the Pintz regime

\[
\delta:=1-\Theta<\frac1{12},
\tag{19}
\]

and choose `rho_0` to be scale-maximal as in `RE-146/147`. Fix `h>delta`, put

\[
\nu:=\nu_P(h)
=3\sqrt2\,h^{3/2}+18h^2,
\tag{20}
\]

and choose `epsilon>0` and `eta` so that

\[
\frac{\nu+\varepsilon}{2}<\eta<\kappa.
\tag{21}
\]

`RE-147` then gives, uniformly for every `x in J_(kappa,eta)`,

\[
\boxed{
\frac{
\sum_{\beta\ge\beta_0+R/U}|a_{\rho,0}(Ux)|
}{|a_{\rho_0,0}(Ux)|}
\ll
U^D e^{-c_{\rm sh}R},
}
\tag{22}
\]

where

\[
D=\frac{A(\nu+\varepsilon)}2,
\qquad
c_{\rm sh}
=\eta-\frac{\nu+\varepsilon}{2}>0.
\tag{23}
\]

Because (22) is uniform on the whole early interval, it holds at the particular witness `x_U` supplied by (18). Thus the previous **location mismatch is gone**: at one and the same point,

\[
\text{local packet}
\gg
N_U e^{-C_{\kappa,\eta}R}
|a_{\rho_0,0}(Ux_U)|,
\tag{24}
\]

while

\[
\text{sufficiently-rightward shell}
\ll
U^D e^{-c_{\rm sh}R}
|a_{\rho_0,0}(Ux_U)|.
\tag{25}
\]

This is the clean splice that `RE-147` left open.

## 4. The explicit exponents show that the current splice has a rate obstruction

The synchronized inequalities are not yet quantitatively compatible. From `0<eta<kappa<1/2`,

\[
\frac{1-\eta}{\kappa-\eta}>2,
\tag{26}
\]

and `1-eta>1/2`. Therefore the explicit local exponent (10) satisfies

\[
\boxed{
C_{\kappa,\eta}
>
8\log(4e)
>19.
}
\tag{27}
\]

By contrast, from (23),

\[
\boxed{
0<c_{\rm sh}<\eta<\frac12.
}
\tag{28}
\]

Consequently the ratio of the available shell upper bound to the available local lower bound is bounded only by

\[
\frac{\text{shell upper bound}}
     {\text{local lower bound}}
\ll
\frac{U^D}{N_U}
 e^{(C_{\kappa,\eta}-c_{\rm sh})R}.
\tag{29}
\]

The exponent of `R` in (29) is strictly positive by a very large margin. Hence the standard move `R=lambda log U`, which makes the rightward shell small relative to the **single anchor**, cannot by itself make the present shell bound smaller than the present universal local floor. Increasing the common radius improves (25) but destroys the guaranteed floor (24) much faster.

This is a statement about the **strength of the current estimates**, not a theorem that actual zeta zeros realize worst-case local suppression. The constant `16` in `RE-145` was intentionally crude, while `RE-144` proves only that exponential dependence on `R` is the correct functional order in a matched formal class, not that the coefficient in (27) is sharp. A better positive-measure inequality, stronger geometry of the actual packet, or a shell estimate with a much larger decay constant could change the comparison.

Still, (29) rules out one tempting closure strategy with the bounds presently in hand: simply localize the `RE-145` witness, take a larger and larger common reciprocal box, and expect Pintz density to outrun the local loss. The witness can indeed be localized; the rates then move in the wrong relative direction.

## 5. Adversarial and representation audit

**Does the dilation change the zero geometry or the Robin scale?** No. Equation (5) rescales only the observation variable in the already-normalized Laplace transform. The original reciprocal box remains `R/U`; the pushed-forward support radius `bR` is only the representation used to invoke `RE-145`.

**Could the maximum of `Q_U` occur at the edge of the early interval and defeat the carrier step?** No. The same one-sided-neighborhood argument used in `RE-145` applies because `J_(kappa,eta)` has fixed positive length. Under `R=o(log U)` the stability neighborhood is `U^{-o(1)}`, while the carrier frequency is `gamma_0 U` with `gamma_0>=gamma_*>0`.

**Does the synchronized shell bound control every mode outside the reciprocal box?** No. Exactly as in `RE-146/147`, it controls only the sufficiently-rightward horizontal shell. The one-sided near-left cluster of `RE-144` and modes with `|beta-beta_0|<R/U` but vertically far from `gamma_0` remain separate obligations. Nothing in (24)--(29) folds them into zero density.

**Does (27) prove the true local exponent must exceed the shell exponent?** No. It proves only that the explicit `RE-145` constant is too expensive. `RE-144` establishes sharpness of the exponential *order* in `R`, not of the coefficient. Optimizing the cardinality-free positive-measure modulus remains potentially high leverage precisely because location synchronization is no longer an issue.

**Can a large local cardinality `N_U` rescue (29)?** In principle yes, but no lower bound of the required size is available or expected from the current source inputs; the reciprocal box always contains the anchor and may contain only that atom. The present line cannot use `N_U` as a uniform compensating factor.

## 6. Prior-art boundary and research effect

Classical Turán and Turán--Nazarov inequalities already propagate exponential-polynomial control between intervals or measurable subsets. Modern formulations likewise treat arbitrary local observation sets. Their usual loss, however, depends on the number/effective degree of exponential terms. That is the correct general prior-art neighborhood, and no novelty is claimed for interval localization as an abstract harmonic-analysis phenomenon.

The line-specific contribution is narrower: the cardinality-free positive-probability modulus of `RE-145` can be localized by exact dilation **without reintroducing rank**, then compared at the same Robin phase with the actual-zeta Pintz shell estimate of `RE-147`. The resulting explicit comparison (29) separates two issues that had been conflated under “synchronization”: positional synchronization is free at `exp(-O(R))` order, whereas the currently proved exponential constants are quantitatively incompatible. No external theorem is load-bearing beyond the already-canonical inputs of `RE-145` and `RE-147`, so `SOURCES.md` needs no change.

A targeted prior-art audit checked the Turán--Nazarov/Remez neighborhood, including Friedland--Yomdin's 2013 formulation and current measurable Turán--Nazarov work. Those results confirm that local-to-global interval propagation is classical; none located supplies the Robin-specific positive-measure/Pintz splice or removes the rate mismatch in (29).

The frontier is therefore sharper. There is no longer a need to “find the `RE-145` witness inside the Pintz window”: (18) does that. The useful quantitative questions are now whether the universal local exponent can be reduced enough to compete with the shell exponent, whether actual-zero geometry gives a better-than-worst-case local modulus, and how to control the near-left and vertically remote pieces at that same witness point. Merely enlarging a common reciprocal box is not a closure mechanism with the present constants.