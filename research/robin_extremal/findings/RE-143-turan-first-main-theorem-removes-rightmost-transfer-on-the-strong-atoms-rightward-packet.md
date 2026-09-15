# RE-143 — Turán's First Main Theorem removes the rightmost transfer on the strong atom's rightward packet

**Status:** `LITERATURE+DERIVED + EXACT-SPLICE + TURAN-FIRST-MAIN-THEOREM + TARGET-ANCHORED + RIGHTWARD-SUBPACKET + NO-RIGHTMOST-GAIN + THIN-LEFT-REMAINDER + FULL-PACKET-BUDGET + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-140`--`RE-142` isolate a stubborn loss in the finite-core/full-tail certificate based on Turán's **Second** Main Theorem. That theorem is naturally applied after normalizing by the rightmost horizontal atom. The resulting finite-core floor is

\[
G(U,T)e^{-\Lambda_\kappa N_T}M_0(U),
\]

and `RE-142` proves that the coarse source envelopes currently available cannot improve the generic transfer `G(U,T)=T^{-2+o(1)}` to a fixed exponent strictly below `2`.

That loss is not intrinsic to every Turán power-sum certificate. There is a target-anchored use of Turán's **First** Main Theorem which keeps the original algebraically strong atom and pays no rightmost-amplitude transfer at all. The price is different: the theorem sees only the part of the finite packet lying **on or to the right of the target atom**. The left-of-target packet becomes an explicit cancellation remainder.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad 0<\kappa<1,
\tag{1}
\]

and let `C` be any finite multiset of positive-ordinate points

\[
\rho=\beta+i\gamma,
\qquad \sigma_0\le\beta<\Theta,
\qquad \gamma>0.
\tag{2}
\]

For the leading Robin coefficient write

\[
d_\rho:=\frac1{\rho(1-\rho)},
\qquad
a_{\rho,0}(u):=e^{-(\Theta-\beta)u}d_\rho,
\tag{3}
\]

and choose a distinguished atom

\[
\rho_0=\beta_0+i\gamma_0\in C.
\tag{4}
\]

Define the rightward subpacket

\[
C^+(\rho_0):=\{\rho\in C:\beta\ge\beta_0\},
\qquad N_+:=\#C^+(\rho_0),
\tag{5}
\]

counting multiplicity, and let

\[
\mathcal S^+_0(u)
:=2\Re\sum_{\rho\in C^+(\rho_0)}
a_{\rho,0}(u)e^{i\gamma u}.
\tag{6}
\]

Put

\[
q^{(1)}_\kappa:=\frac{\kappa}{4e},
\qquad
\Lambda^{(1)}_\kappa:=2\log\frac{4e}{\kappa}.
\tag{7}
\]

Then

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S^+_0(u)|
\ge
2c_\Theta
\left(q^{(1)}_\kappa\right)^{2N_+}
|a_{\rho_0,0}(U)|,
}
\tag{8}
\]

where

\[
c_\Theta:=2\sqrt{\Theta(1-\Theta)}>0.
\tag{9}
\]

The lower bound is independent of the ordinate of every farther-right atom, independent of their horizontal displacement, and contains **no analogue of the rightmost gain `G(U,T)`**. It also pays only for `N_+`, not for left-of-target modes.

For the full finite packet, write

\[
\mathcal S^-_0(u)
:=2\Re\sum_{\substack{\rho\in C\\\beta<\beta_0}}
a_{\rho,0}(u)e^{i\gamma u}.
\tag{10}
\]

At the same witness supplied by (8),

\[
\boxed{
|\mathcal S_0(u_*)|
\ge
2c_\Theta e^{-\Lambda^{(1)}_\kappa N_+}
|a_{\rho_0,0}(U)|
-
\|\mathcal S^-_0\|_{L^\infty([(1-\kappa)U,U])}.
}
\tag{11}
\]

Thus the rightmost-transfer obstruction of `RE-142` can be bypassed inside the same classical power-sum technology, but only by converting it into a **one-sided cancellation problem immediately to the left of the strong atom**.

## 1. Normalize at the strong atom and the rightward roots expand

Define

\[
Q^+_{\rho_0}(u)
:=
e^{(\Theta-\beta_0)u}\mathcal S^+_0(u).
\tag{12}
\]

Using conjugate pairing,

\[
Q^+_{\rho_0}(u)
=
\sum_{\rho\in C^+(\rho_0)}
\left[
 d_\rho e^{[(\beta-\beta_0)+i\gamma]u}
+
 \overline{d_\rho}e^{[(\beta-\beta_0)-i\gamma]u}
\right].
\tag{13}
\]

At integer samples `u=nu h`, this is a power sum whose ungrouped roots are

\[
z_\rho^\pm
:=
\exp\!\left(h[(\beta-\beta_0)\pm i\gamma]\right).
\tag{14}
\]

Because every member of `C^+(rho_0)` satisfies `beta>=beta_0`,

\[
\boxed{|z_\rho^\pm|\ge1.}
\tag{15}
\]

This is exactly the hypothesis of Turán's First Main Theorem. If sampled roots coincide, combine them. The number `P` of distinct roots satisfies

\[
1\le P\le2N_+,
\tag{16}
\]

and grouping does not alter the zeroth power sum.

The important contrast with `RE-139` is structural. The Second Main Theorem wants roots contracted into the unit disk and therefore naturally orders the packet from the **rightmost horizontal face**. The First Main Theorem works with roots outside the unit disk and controls later power sums directly from the coherent zeroth sum. Anchoring at `beta_0` therefore keeps the target coefficient itself.

## 2. The Robin coefficient sector makes the zeroth sum target-bearing

For every point in the fixed strip,

\[
\rho(1-\rho)
=
\beta(1-\beta)+\gamma^2
+i\gamma(1-2\beta),
\tag{17}
\]

and the same sector estimate used in `RE-137` and `RE-139` gives

\[
\boxed{
\Re d_\rho
\ge
c_\Theta|d_\rho|.
}
\tag{18}
\]

Therefore the zeroth power sum in (13) is real and positive:

\[
Q^+_{\rho_0}(0)
=
2\sum_{\rho\in C^+(\rho_0)}\Re d_\rho
\ge
2\Re d_{\rho_0}
\ge
2c_\Theta|d_{\rho_0}|.
\tag{19}
\]

No ordering of coefficient partial sums is needed. This is the second key difference from the Second Main Theorem: farther-right atoms may have arbitrarily small Robin coefficients, but they cannot erase the target from `Q^+_{rho_0}(0)` because all coefficient real parts have the same sign.

Aliasing creates no loophole. Combining coincident sampled roots preserves both the condition `|z|>=1` and the total zeroth sum (19). Multiplicity is therefore harmless.

## 3. Turán's First Main Theorem searches inside the physical window

The classical first theorem for a power sum

\[
s_\nu=\sum_{j=1}^{P}b_jz_j^\nu,
\qquad |z_j|\ge1,
\tag{20}
\]

states that for every nonnegative integer `M`, some

\[
M+1\le\nu\le M+P
\tag{21}
\]

satisfies the standard weaker bound

\[
|s_\nu|
\ge
\left(
\frac{P}{2e(M+P)}
\right)^{P-1}
|s_0|.
\tag{22}
\]

Choose

\[
M:=
\left\lceil
\frac{1-\kappa}{\kappa}P
\right\rceil,
\qquad
h:=\frac{U}{M+P}.
\tag{23}
\]

As in the sampling geometry of `RE-139`, every index in (21) lands inside the physical observation window:

\[
(1-\kappa)U
\le
(M+1)h
\le
\nu h
\le U.
\tag{24}
\]

Moreover,

\[
\frac{P}{M+P}\ge\frac\kappa2,
\tag{25}
\]

so (19), (22), and (25) give a sample `u_*=nu h` such that

\[
|Q^+_{\rho_0}(u_*)|
\ge
2c_\Theta
\left(\frac{\kappa}{4e}\right)^{P-1}
|d_{\rho_0}|.
\tag{26}
\]

Because `u_*<=U`, returning to the Robin normalization loses no more than the target's own damping:

\[
\begin{aligned}
|\mathcal S^+_0(u_*)|
&=
e^{-(\Theta-\beta_0)u_*}
|Q^+_{\rho_0}(u_*)|\\
&\ge
2c_\Theta
\left(\frac{\kappa}{4e}\right)^{P-1}
 e^{-(\Theta-\beta_0)U}|d_{\rho_0}|.
\end{aligned}
\tag{27}
\]

Since `P<=2N_+` and `q^(1)_kappa<1`, (27) implies (8). The triangle inequality then gives (11).

The mechanism is exact: the coherent anchor is at `u=0`, but unlike Turán--Nazarov propagation it introduces no real-exponent spread penalty. Root growth is the favorable side of the First Main Theorem rather than a quantity that must be bounded away.

## 4. In the full zeta packet, only a logarithmically thin left slab is generically dangerous

The left remainder in (11) is not automatically small. Nevertheless, an algebraically strong target localizes the part of that remainder which can matter at an algebraic scale.

Now let the points be actual zeta zeros in the full strict-subedge packet, and suppose

\[
M_0(U)
:=|a_{\rho_0,0}(U)|
=
e^{-(\Theta-\beta_0)U}|d_{\rho_0}|
\ge cU^{-A}
\tag{28}
\]

for fixed `A,c>0`. Put

\[
\delta_0:=\Theta-\beta_0.
\tag{29}
\]

The fixed-strip coefficient law gives a uniform upper bound on `|d_rho|`, so (28) implies

\[
\boxed{\delta_0U\le A\log U+O(1).}
\tag{30}
\]

Also `e^{-delta_0U}<=1`, hence

\[
|d_{\rho_0}|\ge M_0(U)\ge cU^{-A}.
\tag{31}
\]

Finally the full leading coefficient mass is absolutely summable,

\[
\sum_{\substack{\zeta(\rho)=0\\\gamma>0}}
|d_\rho|<\infty,
\tag{32}
\]

by Riemann--von Mangoldt and `|d_rho|<<gamma^-2`.

Fix `H>0` and let the far-left packet consist of zeros satisfying

\[
\beta
\le
\beta_0-H\frac{\log U}{U}.
\tag{33}
\]

Uniformly for `u in [(1-kappa)U,U]`, equations (30)--(32) give

\[
\begin{aligned}
|\mathcal S^{\mathrm{far}-}_0(u)|
&\ll
 e^{-(\Theta-\beta_0)(1-\kappa)U}
 U^{-(1-\kappa)H}\\
&=
 M_0(U)|d_{\rho_0}|^{-1}
 e^{\kappa\delta_0U}
 U^{-(1-\kappa)H}\\
&\ll
M_0(U)
U^{A(1+\kappa)-(1-\kappa)H}.
\end{aligned}
\tag{34}
\]

Consequently, for every prescribed `L>0`, choosing

\[
H>
\frac{A(1+\kappa)+L}{1-\kappa}
\tag{35}
\]

forces

\[
\boxed{
\|\mathcal S^{\mathrm{far}-}_0\|_\infty
\ll M_0(U)U^{-L}.
}
\tag{36}
\]

Thus the price for abandoning the rightmost atom is not an arbitrary left half-plane packet. Up to any fixed algebraic accuracy, only zeros in the shrinking strip

\[
\boxed{
\beta_0-H\frac{\log U}{U}<\beta<\beta_0
}
\tag{37}
\]

can cancel the target-anchored rightward witness. This is a one-sided horizontal localization theorem. It uses no zero spacing, simplicity, or local zero-density estimate.

The width `O(log U/U)` is not claimed optimal. Earlier Gevrey arguments such as `RE-131` obtain thinner locking under the stronger hypothesis that the **full** packet is already hidden on a macroscopic window. Equation (37) serves a different purpose: it is an unconditional remainder reduction inside a prospective full-packet visibility certificate.

## 5. The full finite-core/tail budget loses `eta` and gains a thin-left term

Return to the actual full leading packet `S_0` of `RE-140`--`RE-141`, truncate at height `T`, and let

\[
C_T^+(\rho_0)
:=
\{\rho:\gamma\le T,\ \beta\ge\beta_0\},
\qquad
N_+(U,T):=\#C_T^+(\rho_0).
\tag{38}
\]

For a fixed `H` define the near-left core

\[
C_{T,H}^-(\rho_0)
:=
\left\{
\rho:\gamma\le T,
\ \beta_0-H\frac{\log U}{U}<\beta<\beta_0
\right\}
\tag{39}
\]

and its packet norm

\[
\mathfrak L_{T,H}(U)
:=
\sup_{(1-\kappa)U\le u\le U}
\left|
2\Re\sum_{\rho\in C_{T,H}^-(\rho_0)}
a_{\rho,0}(u)e^{i\gamma u}
\right|.
\tag{40}
\]

Apply (8) to the rightward core, then subtract (40), the far-left estimate (36), and the high-height tail of `RE-141`. For every fixed `epsilon>0`, some `u_*` in the physical window satisfies

\[
\boxed{
\begin{aligned}
|\mathcal S_0(u_*)|
\ge{}&
2c_\Theta
 e^{-\Lambda^{(1)}_\kappa N_+(U,T)}M_0(U)
-
\mathfrak L_{T,H}(U)\\
&-
O(M_0(U)U^{-L})\\
&-
O\!\left(
T^{-2+\nu_I(\Theta)+\epsilon}(\log T)^C
+e^{-c_\epsilon U}\frac{\log T}{T}
\right).
\end{aligned}
}
\tag{41}
\]

This is the target-anchored analogue of the `RE-140`/`RE-141` certificate. Its finite-core term contains **no `G(U,T)`** and therefore no rightmost transfer exponent `eta`.

If

\[
T=U^B,
\qquad
N_+(U,T)\le\alpha\log T+o(\log T),
\tag{42}
\]

and the near-left term is negligible relative to the first term in (41), then the polynomial part of the high tail is absorbed whenever

\[
\boxed{
\frac AB
+
\Lambda^{(1)}_\kappa\alpha
<
2-\nu_I(\Theta).
}
\tag{43}
\]

Compare this with `RE-141`, whose Second-Main-Theorem certificate requires

\[
\frac AB+
\eta+
\Lambda_\kappa\alpha
<2-\nu_I(\Theta).
\tag{44}
\]

The term `eta` has disappeared. The complexity constant is also smaller at the crude level used here,

\[
\Lambda^{(1)}_\kappa
=2\log\frac{4e}{\kappa}
<
2\log\frac{16e}{\kappa}
=\Lambda_\kappa,
\tag{45}
\]

although the two certificates pay for different mode sets and should not be compared by constants alone.

## 6. What this does to the `RE-142` obstruction

`RE-142` remains correct: current upper zero-density, zero-free-region, symmetry, and Riemann--von Mangoldt envelopes do not force a rightmost gain exponent below `2`. What changes is the inference drawn from that fact.

The `T^-2` transfer is a bottleneck of the **whole-core Second-Main-Theorem architecture**, not a universal obstruction to power-sum observability. On the matched spectrum of `RE-142`, the strong atom and its farther-right high atom already lie in `C_T^+(rho_0)`. The First Main Theorem retains the strong atom in the coherent zeroth sum, so the high ordinate of the farther-right atom causes no amplitude loss in (8). Earlier lacunary stages lie farther left and are exponentially damped on the later windows. Thus the specific matched control that makes `G=T^{-2+o(1)}` does not recreate the same obstruction against (41).

The live source problem is therefore redirected. A target-anchored closure now needs two kinds of information:

1. enough control of the **effective rightward complexity** `N_+(U,T)` (or a replacement which pays for fewer target-bearing modes); and
2. enough control of cancellation from the **logarithmically thin left slab** (37).

Neither follows from current global zero-density estimates. In particular, a polynomial bound for `N_+` is still useless inside the exponential Turán factor, and (37) is a shrinking horizontal strip for which the existing fixed-strip density bounds give no local arrangement theorem.

This is nevertheless a strictly different frontier from the rightmost-height recurrence demanded after `RE-142`: one can avoid proving that a farther-right zero has controlled ordinate if one can instead price rightward complexity and the thin-left cancellation layer.

## 7. Adversarial and representation audit

The target-anchored theorem does not obtain a full-packet floor by silently discarding leftward zeros. Equation (11) keeps their exact norm, and equations (34)--(37) remove only the part whose extra horizontal damping is enough to be negligible at a stated algebraic scale. The near-left packet remains explicit in (41).

The coherent anchor at `u=0` is representation-faithful. Every coefficient is the actual Robin coefficient `1/[rho(1-rho)]`; no free signs or synthetic amplitudes are introduced. The positive-real-part sector is exactly the same source property already used in `RE-137` and `RE-139`. The First Main Theorem then transports the actual zeroth sum; it does not assume phase alignment in the observation window.

The theorem is leading-order (`K=0`) just like the full-packet budget in `RE-140`--`RE-142`. No claim is made that the higher-order Robin coefficient polynomial preserves the same sector uniformly without an additional stability budget.

The bound also does not assume simple zeros. Multiplicity merely repeats terms before grouping. Nor does it assume a minimum vertical spacing: the First Main Theorem is insensitive to how the roots are arranged in argument, and exact sampled aliases are absorbed by coefficient grouping.

Finally, (43) is only a sufficient conditional budget. It does not prove `N_+=O(log T)`, does not prove the near-left term is small, and does not imply Robin's inequality. Its content is that **rightmost amplitude transfer is no longer among the necessary unknowns of this alternative certificate**.

## 8. Prior-art boundary and next step

Turán's First Main Theorem is classical. The exact power-sum inequality (22) is the standard companion to the Second Main Theorem already anchored through Montgomery's *Ten Lectures on the Interface Between Analytic Number Theory and Harmonic Analysis*, Chapter 5, section 5. A targeted literature check found the usual generic power-sum statement but no source-specific Robin theorem corresponding to the split (5), the coefficient-sector anchor (19), or the full-packet budget (41). No novelty is claimed for Turán's theorem itself.

No new bibliographic family is introduced, so `SOURCES.md` need not acquire another source entry. The durable line-specific delta is the exact splice: **use the First Main Theorem on the target's rightward subpacket, keep the strong atom in `s_0`, and move the unresolved source burden into rightward complexity plus a thin left cancellation slab**.

The next useful test is correspondingly concrete. Instead of seeking another upper theorem that improves the rightmost transfer exponent, ask whether actual zeta zeros can support, at the polynomial height forced by an algebraically strong Robin atom, either

\[
N_+(U,U^B)\gg\log U
\]

at the coefficient-bearing scale relevant to (41), or order-`M_0(U)` cancellation inside

\[
\beta_0-O\!\left(\frac{\log U}{U}\right)<\beta<\beta_0.
\]

A source theorem excluding both would close the target-anchored finite-core/tail splice without ever selecting a rightmost atom. A matched actual-source-compatible control realizing either mechanism would instead identify the next genuine obstruction.