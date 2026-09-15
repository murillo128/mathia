# RE-139 — Turán power sums remove the horizontal-spread tax from rightmost Robin packets

**Status:** `LITERATURE+DERIVED + EXACT-SPLICE + FINITE-ZERO-EDGE + LEADING-PACKET + TURAN-SECOND-MAIN-THEOREM + RIGHTMOST-ATOM + HORIZONTAL-SPREAD-FREE + RIEMANN-VON-MANGOLD + VERTICAL-SPAN-TAX + EXTERIOR-CANCELLATION-STILL-OPEN + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-137` applies measurable Turán--Nazarov propagation from the reinforcing anchor at `u=0` to a macroscopic observation window. For an arbitrary distinguished atom, that argument pays exponentially for the scaled horizontal spread

\[
H_C(U)=U\max_{\rho\in C}|\Re\rho-\Re\rho_0|.
\]

`RE-138` then inserts the Riemann--von Mangoldt count for actual zeta zeros and obtains a three-way budget involving hiding depth, horizontal spread, and absolute vertical span.

There is a stronger route when the packet is anchored at its **rightmost horizontal atom**. Turán's Second Main Theorem for power sums works directly on a finite block of samples inside the observed window. After factoring the rightmost horizontal damping, all power-sum roots lie in the closed unit disk. The Robin coefficients have strictly positive real part, so the partial-sum term in Turán's theorem cannot collapse. No propagation from `u=0` is needed, and the horizontal spread disappears entirely.

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

For the leading Robin packet write

\[
d_\rho:=\frac1{\rho(1-\rho)},
\qquad
a_{\rho,0}(u):=e^{-(\Theta-\beta)u}d_\rho,
\tag{3}
\]

and

\[
\mathcal S_{C,0}(u)
:=2\Re\sum_{\rho\in C}a_{\rho,0}(u)e^{i\gamma u}.
\tag{4}
\]

Choose any member

\[
\rho_*=\beta_*+i\gamma_*
\tag{5}
\]

on the rightmost horizontal face,

\[
\beta_*=\max_{\rho\in C}\beta,
\tag{6}
\]

and let `N=#C`, counting multiplicity. Then

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C,0}(u)|
\ge
2c_\Theta
\left(\frac{\kappa}{16e}\right)^{2N}
|a_{\rho_*,0}(U)|,
}
\tag{7}
\]

where

\[
c_\Theta:=2\sqrt{\Theta(1-\Theta)}>0.
\tag{8}
\]

The lower bound is independent of

\[
U\max_{\rho\in C}|\beta-\beta_*|,
\qquad
U\max_{\rho\in C}|\gamma-\gamma_*|,
\tag{9}
\]

and requires no spacing, simplicity, height, or vertical-diameter hypothesis. The only packet-size cost is exponential in the number of modes.

For **actual zeta zeros**, this removes the horizontal alternative left by `RE-138`. Suppose `C_U` is a finite multiset of positive-ordinate nontrivial zeta zeros in the same fixed strip, contains a distinguished atom

\[
\rho_0=\beta_0+i\gamma_0,
\tag{10}
\]

with

\[
M_0(U):=|a_{\rho_0,0}(U)|\ge cU^{-A}
\tag{11}
\]

for fixed `A,c>0`, and define its absolute vertical half-span

\[
W_U:=\max_{\rho\in C_U}|\Im\rho-\gamma_0|.
\tag{12}
\]

Then there are constants `c_1,C_1>0`, depending only on the fixed strip, `A`, `c`, and `kappa`, such that

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,0}(u)|
\ge
\frac{c_1M_0(U)}{(1+W_U)^2}
\exp\!\left[
-C_1(1+W_U)
\bigl(\log U+\log(2+W_U)\bigr)
\right].
}
\tag{13}
\]

In particular, if `W_U=O(1)`, then for some fixed `B>0`,

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,0}(u)|
\ge U^{-B}M_0(U),
}
\tag{14}
\]

**with no horizontal-spread assumption at all**.

Define the normalized hiding depth

\[
D_U:=
\frac1{\log U}
\log_+\frac{M_0(U)}{
\sup_{(1-\kappa)U\le u\le U}|\mathcal S_{C_U,0}(u)|}.
\tag{15}
\]

Equation (13) gives

\[
D_U
\le
C_2(1+W_U)
\left(
1+\frac{\log(2+W_U)}{\log U}
\right)
+
O\!\left(\frac{\log(2+W_U)}{\log U}\right).
\tag{16}
\]

Consequently, along any sequence on which

\[
D_U\longrightarrow\infty,
\tag{17}
\]

one necessarily has

\[
\boxed{W_U\longrightarrow\infty.}
\tag{18}
\]

Thus the finite actual-zero escape from `RE-138` sharpens from

\[
\text{large horizontal spread and/or large vertical span}
\]

to

\[
\boxed{
\text{superalgebraic finite-packet hiding}
\Longrightarrow
\text{unbounded absolute vertical span}.
}
\tag{19}
\]

Horizontal drift to the left of a rightmost near-edge atom is not an independent hiding resource.

## 1. The Robin coefficient sector controls every ordered partial sum

For `rho=beta+i gamma`,

\[
\rho(1-\rho)
=
\beta(1-\beta)+\gamma^2
+i\gamma(1-2\beta).
\tag{20}
\]

As in `RE-137`, the real part of this denominator is positive, and direct maximization of the ratio of its imaginary and real parts gives

\[
\boxed{
\Re d_\rho
\ge
c_\Theta|d_\rho|,
\qquad
c_\Theta=2\sqrt{\Theta(1-\Theta)}.
}
\tag{21}
\]

The same inequality holds for `\overline{d_\rho}` because conjugation preserves the real part and modulus. The key point for the present argument is stronger than non-cancellation of the total coefficient sum: **every coefficient entering the conjugate-paired power sum has positive real part**.

Therefore, if a list of such coefficients begins with a group containing the chosen target coefficient `d_(rho_*)`, every initial partial sum `B_J` satisfies

\[
\boxed{
|B_J|
\ge
\Re B_J
\ge
\Re d_{\rho_*}
\ge
c_\Theta|d_{\rho_*}|.
}
\tag{22}
\]

This is exactly the quantity that appears in Turán's Second Main Theorem.

## 2. Rightmost horizontal normalization places every root in the unit disk

Remove the rightmost damping by defining

\[
Q_C(u)
:=
e^{(\Theta-\beta_*)u}\mathcal S_{C,0}(u).
\tag{23}
\]

Using conjugate pairing,

\[
Q_C(u)
=
\sum_{\rho\in C}
\left[
 d_\rho e^{[(\beta-\beta_*)+i\gamma]u}
+
 \overline{d_\rho}
 e^{[(\beta-\beta_*)-i\gamma]u}
\right].
\tag{24}
\]

Fix a sampling step `h>0`. At integer multiples `u=nu h`, (24) is a complex power sum. Before combining coincidences its roots are

\[
z_\rho^\pm
:=
\exp\!\left(
h[(\beta-\beta_*)\pm i\gamma]
\right).
\tag{25}
\]

Because of the rightmost choice (6),

\[
|z_\rho^\pm|
=e^{h(\beta-\beta_*)}
\le1,
\tag{26}
\]

while the two target roots have modulus one. If different terms give the same sampled root, combine them. The resulting representation has `P<=2N` distinct roots,

\[
Q_C(\nu h)=\sum_{j=1}^{P}b_jz_j^\nu,
\tag{27}
\]

and every grouped coefficient `b_j` still has positive real part. Order the roots by decreasing modulus, and among the modulus-one ties put first a group containing one target term. Then

\[
1=|z_1|\ge|z_2|\ge\cdots\ge|z_P|,
\tag{28}
\]

and (22) gives

\[
\boxed{
\min_{1\le J\le P}
\left|\sum_{j=1}^{J}b_j\right|
\ge
c_\Theta|d_{\rho_*}|.
}
\tag{29}
\]

Aliasing therefore causes no loophole: combining sampled roots can only aggregate coefficients whose real parts are already positive.

## 3. Turán's Second Main Theorem searches inside the observed window

The classical second main theorem states that, for a power sum as in (27)--(28) and any nonnegative integer `M`, there exists

\[
M+1\le\nu\le M+P
\tag{30}
\]

such that

\[
\left|Q_C(\nu h)\right|
\ge
2\left(
\frac{P}{8e(M+P)}
\right)^P
\min_{1\le J\le P}
\left|\sum_{j=1}^{J}b_j\right|.
\tag{31}
\]

Choose

\[
M:=
\left\lceil
\frac{1-\kappa}{\kappa}P
\right\rceil,
\qquad
h:=\frac{U}{M+P}.
\tag{32}
\]

Then the entire block (30) lies in the physical observation interval. Indeed,

\[
\frac{(M+1)U}{M+P}
\ge(1-\kappa)U,
\qquad
\frac{(M+P)U}{M+P}=U.
\tag{33}
\]

Moreover,

\[
\frac{P}{M+P}
\ge
\frac{\kappa}{2},
\tag{34}
\]

so (29)--(31) imply that at one of these actual samples

\[
|Q_C(\nu h)|
\ge
2c_\Theta
\left(\frac{\kappa}{16e}\right)^P
|d_{\rho_*}|.
\tag{35}
\]

Since `P<=2N` and `kappa/(16e)<1`,

\[
|Q_C(\nu h)|
\ge
2c_\Theta
\left(\frac{\kappa}{16e}\right)^{2N}
|d_{\rho_*}|.
\tag{36}
\]

Finally `nu h<=U`, so

\[
|\mathcal S_{C,0}(\nu h)|
=e^{-(\Theta-\beta_*)\nu h}|Q_C(\nu h)|
\ge
e^{-(\Theta-\beta_*)U}|Q_C(\nu h)|.
\tag{37}
\]

The last factor is exactly

\[
e^{-(\Theta-\beta_*)U}|d_{\rho_*}|
=|a_{\rho_*,0}(U)|,
\tag{38}
\]

and (7) follows.

This proof explains why the horizontal spread vanishes. `RE-137` used continuous propagation from an extrapolation anchor and therefore paid for the largest real exponent. Here the rightmost normalization makes every real exponent nonpositive, and Turán's power-sum theorem looks for a large value directly among samples in the observed window.

## 4. Actual zeta zeros convert the remaining complexity into vertical span only

Now let `C_U` consist of actual zeta zeros and retain the strong atom `rho_0` from (10)--(11). The universal leading coefficient bound

\[
|a_{\rho,0}(U)|
\ll\frac1{1+\gamma^2}
\tag{39}
\]

implies

\[
\boxed{\gamma_0\ll_A U^{A/2}.}
\tag{40}
\]

Choose a member `rho_*` of `C_U` with maximal real part. Since `beta_*>=beta_0`, the horizontal damping can only increase its coefficient relative to what it would have at `beta_0`. On the fixed strip,

\[
|\rho(1-\rho)|\asymp1+\gamma^2,
\tag{41}
\]

so

\[
\begin{aligned}
\frac{|a_{\rho_*,0}(U)|}{M_0(U)}
&=e^{(\beta_*-\beta_0)U}
  \frac{|d_{\rho_*}|}{|d_{\rho_0}|}\\
&\gg
\frac{1+\gamma_0^2}{1+\gamma_*^2}\\
&\gg
\frac1{(1+W_U)^2}.
\end{aligned}
\tag{42}
\]

For the last step, use `|gamma_*-gamma_0|<=W_U` and the elementary bound

\[
1+(\gamma_0+W_U)^2
\le
2(1+\gamma_0^2)(1+W_U)^2.
\tag{43}
\]

Thus selecting the rightmost atom costs at most a quadratic factor in the **absolute vertical span**, but nothing in horizontal distance.

The same Riemann--von Mangoldt local count used in `RE-138`, together with (40), gives

\[
\boxed{
N_U:=\#C_U
\ll
(1+W_U)
\bigl(\log U+\log(2+W_U)\bigr),
}
\tag{44}
\]

counting multiplicity. Applying (7) to `rho_*`, then inserting (42)--(44), yields (13). Taking logarithms gives (16), and (18) follows because a bounded subsequence of `W_U` would keep the right-hand side of (16) bounded.

The conclusion is source-faithful in exactly the sense missing from the formal controls: ordinary zero counting does not bound the packet cardinality absolutely, but once the absolute vertical span is bounded it bounds the cardinality by `O(log U)`, and the power-sum theorem needs no additional horizontal budget.

## 5. Stress tests and exact boundary

### The `RE-133` product control is not contradicted

The stage-`j` control in `RE-133` has a rightmost target but `N=2^j` modes. Equation (7) then gives only a floor of size

\[
\exp[-C_\kappa2^j]
\]

relative to the target. The constructed product residual is of order `q^j`, much larger than this extremely weak floor for large `j`, so the two results are fully compatible. What actual zeta zeros add in (44) is precisely the inability to place exponentially many modes in a bounded absolute vertical span near a polynomial-height target.

### Purely vertical controls also remain compatible

The pure-phase control of `RE-137` has all real parts equal, so every atom is rightmost and (7) applies. Again its hiding resource is growing cardinality. The new theorem does not claim a cardinality-free floor; it shows only that **leftward horizontal spread cannot replace cardinality** once a rightmost atom is used.

### The rightmost selection is essential to the disk geometry

For an arbitrary prescribed atom `rho_0`, factoring its horizontal damping can create roots with modulus greater than one whenever another atom lies farther right. Turán's second theorem then no longer has the required unit-disk ordering. The actual-zero corollary avoids inventing a hypothesis: every finite packet has a rightmost member, and (42) quantifies the cost of replacing an arbitrary strong target by that member.

### No finite-order `K>=1` theorem is claimed here

Equation (7) is exact for the leading packet `K=0`, where the coefficients are independent of `u` after the horizontal exponential is factored. The `u^-k` corrections for `K>=1` destroy the exact power-sum form. `RE-137` already shows how finite-order stability requires an explicit perturbative budget. This finding does not silently transfer (7) to arbitrary `K`.

### The full infinite packet and exterior cancellation remain open

The theorem controls a selected finite packet. A visible finite core may still be cancelled at its witnessing sample by the complement of the full infinite subedge packet. `RE-123` gives strong absolute control of sufficiently high ordinates for a prescribed algebraic accuracy, but choosing a core that is simultaneously vertically tight around the strong atom and immune to exterior cancellation is still a separate source problem. Nothing in (7)--(18) proves that the entire zeta packet has an algebraic excursion.

## 6. Representation, adversarial audit, and prior-art boundary

No new arithmetic coordinate is introduced. The source remains the same finite Robin zero packet. The discretization `u=nu h` is only a readout inside the already observed macroscopic interval; the theorem does not infer values outside that interval or replace actual zeros by synthetic roots. Grouping aliased sampled roots preserves the packet exactly at the selected samples.

The main failure modes were checked explicitly. Multiplicity and sampling aliases reduce the number of distinct power-sum roots and preserve positive real coefficient sums. The target group can be placed first among equal-modulus roots because Turán's ordering only constrains modulus. The sampling block is wholly contained in `[(1-kappa)U,U]`; no hidden use of `u=0` remains. The rightmost atom can be much smaller than the original strong target only because of ordinate size, and (42) accounts for that loss before zero counting is invoked. The Riemann--von Mangoldt estimate is used only after (40) places the original target at polynomial height.

The load-bearing external result is classical: Turán's Second Main Theorem for power sums, in the form recorded in Hugh L. Montgomery, *Ten Lectures on the Interface Between Analytic Number Theory and Harmonic Analysis*, CBMS **84** (1994), Chapter 5, section 5. The theorem itself is not new. Ramanujan--Nicolas zero sums with coefficient `1/[rho(1-rho)]` are likewise classical prior art already recorded in this line. A targeted search found no prior theorem combining the second main theorem with the positive Robin coefficient sector to remove horizontal spread from a finite off-critical Robin packet; no novelty is claimed beyond this line-specific splice and its actual-zero consequence. The Montgomery dependency is now anchored in `SOURCES.md`.

`RE-138` converted Turán--Nazarov's complexity cost into an absolute vertical-span tax but still retained horizontal spread as a second possible escape. `RE-139` shows that this horizontal branch is an artifact of anchoring an arbitrary atom and propagating continuously from `u=0`. For a finite packet, choose its rightmost atom and search discretely inside the observed window instead: the source-specific obstruction becomes one-dimensional.

The next live question is therefore sharper. To hide a finite actual-zero core superalgebraically, relevant cancellation must occupy an unbounded **absolute ordinate span**. To hide the full infinite packet, one must additionally explain whether the exterior tail can repeatedly cancel the visible core at the power-sum witness samples. A useful next source theorem would control that exterior cancellation or prove an absolute-vertical tightness principle for the target-bearing off-critical zero mass. Horizontal spread by itself no longer needs to be controlled.