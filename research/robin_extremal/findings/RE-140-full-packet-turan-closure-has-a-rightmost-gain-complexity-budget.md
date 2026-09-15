# RE-140 — full-packet Turán closure has a rightmost-gain/complexity budget

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + FULL-SUBEDGE-PACKET + LEADING-ORDER + TURAN-SECOND-MAIN-THEOREM + ABSOLUTE-ZERO-TAIL + CERTIFICATE-OBSTRUCTION + SOURCE-INFORMATION-GAP + EXTERIOR-CANCELLATION-STILL-OPEN + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-139` gives a horizontal-spread-free visibility floor for every **finite** leading Robin packet by choosing a rightmost horizontal atom and applying Turán's Second Main Theorem directly inside the observed window. `RE-123` gives the complementary uniform absolute tail estimate for the **full** subedge packet,

\[
\|\mathcal S_0-\mathcal S_{0,T}\|_{L^\infty([1,\infty))}
\ll \frac{\log(eT)}{T}.
\tag{1}
\]

The natural next splice is therefore to truncate the full packet at height `T`, use `RE-139` on the finite core, and absorb the omitted tail at the Turán witness sample. This finding makes that splice exact and identifies the first source information it still lacks.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad
0<\kappa<1,
\tag{2}
\]

in the attained finite-edge branch, and let

\[
\mathcal S_0(u)
=
2\Re
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\beta:=\Re\rho<\Theta\\
\gamma:=\Im\rho>0}}
\frac{e^{-(\Theta-\beta)u}e^{i\gamma u}}
{\rho(1-\rho)}
\tag{3}
\]

be the full leading strict-subedge packet. For `T>=2`, let `C_T` be the positive-ordinate zeros in (3) with `gamma<=T`, let `N_T=#C_T` counting multiplicity, and write `S_(0,T)` for the corresponding conjugate-paired finite packet.

Suppose `C_T` contains an algebraically strong atom

\[
\rho_0=\beta_0+i\gamma_0,
\qquad
M_0(U):=
\frac{e^{-(\Theta-\beta_0)U}}
{|\rho_0(1-\rho_0)|}
\ge cU^{-A}.
\tag{4}
\]

Choose a member

\[
\rho_*=\beta_*+i\gamma_*
\in C_T,
\qquad
\beta_*=\max_{\rho\in C_T}\Re\rho,
\tag{5}
\]

and define the exact rightmost-amplitude gain

\[
G(U,T)
:=
\frac{|a_{\rho_*,0}(U)|}{M_0(U)}.
\tag{6}
\]

Put

\[
q_\kappa:=\frac{\kappa}{16e}\in(0,1),
\qquad
\Lambda_\kappa:=2\log\frac{16e}{\kappa}>0.
\tag{7}
\]

Then the direct finite-core-plus-tail certificate is governed by one exact budget:

\[
\boxed{
G(U,T)e^{-\Lambda_\kappa N_T}M_0(U)
\gg_{\Theta,\kappa}
\frac{\log(eT)}{T}
}
\tag{8}
\]

is sufficient to force an excursion of the **full** packet on the same fixed-relative window. More precisely, there are constants `c_(Theta,kappa), C_Theta>0` such that some

\[
u_*=u_*(U,T)\in[(1-\kappa)U,U]
\]

satisfies

\[
\boxed{
|\mathcal S_0(u_*)|
\ge
c_{\Theta,\kappa}
G(U,T)e^{-\Lambda_\kappa N_T}M_0(U)
-
C_\Theta\frac{\log(eT)}{T}.
}
\tag{9}
\]

Thus exterior cancellation is not an unstructured remainder in this truncation scheme. It is reduced to whether the source can make the **rightmost-amplitude gain plus finite-core complexity** beat the reciprocal-height tail.

The useful point is that the source-generic bounds currently available do **not** do this automatically. On the fixed strip,

\[
G(U,T)
\asymp
 e^{(\beta_*-\beta_0)U}
\frac{1+\gamma_0^2}{1+\gamma_*^2},
\tag{10}
\]

so the exact logarithmic protection cost is

\[
\boxed{
\mathfrak J(U,T)
:=
-\log G(U,T)+\Lambda_\kappa N_T
=
\Lambda_\kappa N_T
-(\beta_*-\beta_0)U
+
\log\frac{1+\gamma_*^2}{1+\gamma_0^2}
+O_{\sigma_0,\Theta}(1).
}
\tag{11}
\]

For a polynomial cutoff `T=U^B`, (4) and (9) show that any fixed `epsilon>0` is enough if

\[
\boxed{
\mathfrak J(U,U^B)
\le
(B-A-\epsilon)\log U
}
\tag{12}
\]

for all sufficiently large `U`. In particular, if source information supplies

\[
G(U,U^B)\ge U^{-g+o(1)},
\qquad
N_{U^B}\le\alpha\log U+o(\log U),
\tag{13}
\]

then the splice closes whenever

\[
\boxed{
A+g+\Lambda_\kappa\alpha<B.
}
\tag{14}
\]

Equivalently, if the rightmost loss and relevant mode count are expressed on the cutoff scale as

\[
G(U,T)\ge T^{-\eta+o(1)},
\qquad
N_T\le\alpha_T\log T+o(\log T),
\qquad
T=U^B,
\tag{15}
\]

then a sufficient asymptotic budget is

\[
\boxed{
\frac AB+\eta+\Lambda_\kappa\alpha_T<1.
}
\tag{16}
\]

This exposes the exact missing source theorem. The finite-packet observability is already available; what is not available is a strong enough joint control of the **ordinate of the rightmost relevant atom** and the **effective number of modes that must accompany it** before the absolute tail is discarded.

## 1. Finite-core visibility and the full-packet tail combine at one sample

`RE-139` applied to `C_T` and `rho_*` gives a sample `u_*` in the physical window such that

\[
|\mathcal S_{0,T}(u_*)|
\ge
2c_\Theta
q_\kappa^{2N_T}
|a_{\rho_*,0}(U)|,
\qquad
c_\Theta=2\sqrt{\Theta(1-\Theta)}.
\tag{17}
\]

By (6)--(7),

\[
q_\kappa^{2N_T}|a_{\rho_*,0}(U)|
=
G(U,T)e^{-\Lambda_\kappa N_T}M_0(U).
\tag{18}
\]

`RE-123` gives, uniformly in `u>=1`,

\[
|\mathcal S_0(u)-\mathcal S_{0,T}(u)|
\le
C_\Theta\frac{\log(eT)}{T}.
\tag{19}
\]

The triangle inequality at the **same Turán witness** therefore yields (9). No phase interpolation, averaging, or second witness is introduced. If the right-hand term in (19) is at most half of the first term in (9), the full packet has a positive visibility floor of the same order as the finite core. This proves (8).

The point is narrower than a general tail theorem. Equation (19) is an absolute estimate and therefore remains valid at the witness chosen after seeing the finite core. It is exactly the kind of exterior bound needed for the splice; its weakness is quantitative, not logical.

## 2. The rightmost gain has an exact horizontal-versus-ordinate decomposition

On the fixed strip,

\[
|\rho(1-\rho)|\asymp_{\sigma_0,\Theta}1+\gamma^2.
\tag{20}
\]

Therefore

\[
\begin{aligned}
G(U,T)
&=
 e^{(\beta_*-\beta_0)U}
 \frac{|\rho_0(1-\rho_0)|}
 {|\rho_*(1-\rho_*)|}\\
&\asymp
 e^{(\beta_*-\beta_0)U}
 \frac{1+\gamma_0^2}{1+\gamma_*^2},
\end{aligned}
\tag{21}
\]

which is (10). Thus moving to the right has a favorable **exponential** effect, while moving upward costs only the reciprocal-square Robin coefficient. The finite-packet theorem does not pay for horizontal spread, but horizontal geometry can still help by protecting the amplitude of the atom used to anchor the power sum.

Taking logarithms gives (11). It is useful to keep the signs explicit:

- `Lambda_kappa N_T` is the Turán mode-complexity cost;
- `(beta_*-beta_0)U` is a favorable rightward gain and therefore enters with a minus sign;
- `log((1+gamma_*^2)/(1+gamma_0^2))` is the ordinate-inflation cost.

This is not the horizontal-spread tax of `RE-137`. There the largest real exponent appeared as a propagation penalty. Here the finite packet remains horizontal-spread-free; only the amplitude comparison between the original strong atom and the rightmost Turán anchor remembers how far to the right the source moved.

## 3. Polynomial truncation gives the explicit protection budget

Take

\[
T=U^B,
\qquad B>0.
\tag{22}
\]

From (4), the first term on the right of (9) is at least

\[
c'
U^{-A}
\exp[-\mathfrak J(U,U^B)].
\tag{23}
\]

The tail is

\[
O\!\left(\frac{\log U}{U^B}\right).
\tag{24}
\]

Hence a sufficient condition for the first term to dominate (24) is

\[
\mathfrak J(U,U^B)
\le
(B-A)\log U
-2\log\log U
-O(1).
\tag{25}
\]

The slightly stronger fixed-margin condition (12) implies (25), proving (14). Substituting (15) gives

\[
\mathfrak J(U,U^B)
\le
B(\eta+\Lambda_\kappa\alpha_T+o(1))\log U,
\tag{26}
\]

and (16) follows.

The threshold is informative because it separates three logically different ways to close the full packet: increase the truncation exponent `B`, keep the rightmost amplitude loss below one cutoff power, or prove that only logarithmically many relevant modes need to be paid for. Improving any one variable can compensate the others, but only through the explicit budget (16).

## 4. The current source-generic envelopes do not satisfy the budget

The point of (11)--(16) is not that the actual zeta zeros violate the budget. They show exactly what the current **coarse source information fails to prove**.

First ignore Turán complexity completely, which is maximally favorable. From (21) and `gamma_*<=T`, the geometry-free comparison used already in `RE-139` gives only

\[
G(U,T)
\gg
\frac{1+\gamma_0^2}{1+T^2}
\gg T^{-2}.
\tag{27}
\]

If one inserts only this lower bound into (9) and even replaces `e^{-Lambda_kappa N_T}` by the favorable value `1`, the certified finite-core scale is only

\[
\gg M_0(U)T^{-2}.
\tag{28}
\]

The available absolute exterior bound is `O(log T/T)`. Since `M_0(U)` is uniformly bounded above on the fixed strip,

\[
\frac{M_0(U)T^{-2}}
{\log(eT)/T}
\ll
\frac1{T\log(eT)}
\longrightarrow0.
\tag{29}
\]

Thus the **coarse rightmost-amplitude transfer already loses one cutoff power too many** for the `RE-123` absolute tail, before any mode-count penalty is charged. In the scale notation (15), the generic estimate has `eta=2`, while (16) requires `eta<1-A/B` even when `alpha_T=0`.

Second, Riemann--von Mangoldt gives only the global source envelope

\[
N_T\ll T\log(eT).
\tag{30}
\]

Substituting that bound into Turán yields a guaranteed factor no better than

\[
\exp[-C_\kappa T\log(eT)],
\tag{31}
\]

which is vastly smaller than the reciprocal-height tail scale. Standard fixed-strip zero-density estimates improve the **number of off-critical modes** from the global count, but remain polynomial in `T`; when inserted only as a cardinality upper bound into an exponential-in-`N_T` Turán floor, they still do not produce the logarithmic effective-complexity regime of (15).

These comparisons are certificate obstructions, not statements about the actual packet. The true `G(U,T)` can be exponentially larger than (27), the true off-critical `N_T` can be far smaller than the available upper bounds, and the signed tail can be much smaller than its absolute envelope. Any one of those source-specific improvements could change the conclusion.

## 5. What source information would actually close the splice

The exact criterion (8) isolates several genuinely different sufficient routes.

A **rightmost-height theorem** could show that the rightmost zero in a suitable polynomial-height core remains at ordinate `gamma_*` sufficiently close to the strong atom's ordinate, or that the horizontal gain `(beta_*-beta_0)U` compensates its ordinate inflation. In terms of (11), the required statement is directly quantitative and does not need a minimum zero spacing theorem.

An **effective-complexity theorem** could show that the Turán power sum need pay for only `O(log U)` target-bearing modes, with coefficient small enough for (14), even if many other zeros exist. This is stronger than ordinary one-level zero counting: `RE-135`--`RE-139` already show that raw occupancy is not the intrinsic issue, while the Turán certificate still pays exponentially for every retained mode.

A **sharper signed-tail theorem** could improve (19) at the selected witness scale. The current `log T/T` estimate discards all phase cancellation and all horizontal damping. Any source-faithful gain of more than one effective cutoff power changes the feasible region in (16).

Finally, a different observability theorem could act directly on the infinite absolutely convergent packet, or retain the original strong atom instead of replacing it by a rightmost atom. Either would evade the specific budget derived here rather than satisfying it.

## 6. Stress tests and exact boundary

### This does not prove that the exterior tail cancels the core

Equation (29) compares a **guaranteed lower bound** for the finite core with an **available upper bound** for the tail. Their unfavorable ordering means the current inequalities cannot prove that the tail is smaller. It does not imply that the actual tail attains its upper envelope, has the opposite phase, or cancels the Turán witness. No synthetic or actual counterexample to full-packet visibility is claimed.

### A favorable rightward zero can defeat the coarse `T^-2` loss

The factor discarded in (27) is

\[
e^{(\beta_*-\beta_0)U}.
\]

Even a horizontal improvement of order `(log T)/U` can compensate a polynomial ordinate ratio. Therefore the geometry-free `T^-2` comparison must not be promoted to a statement that rightmost selection actually loses two powers for zeta zeros. The live question is precisely whether the source couples rightward movement and ordinate growth strongly enough to make `G(U,T)` favorable.

### Small actual `N_T` can defeat the Riemann--von Mangoldt penalty

Equation (31) is what follows after replacing the exact off-critical packet cardinality by a global upper envelope. It is not an estimate from below for the actual number of modes. If the relevant subedge zeros are logarithmically sparse, the Turán factor can remain polynomial and (14) becomes viable.

### Height truncation is only one core selection

The proof uses `C_T={gamma<=T}` because that is the core for which `RE-123` supplies an immediate uniform exterior estimate. An amplitude-adaptive, horizontally filtered, dyadic, or otherwise source-aware core may have a better gain/complexity/tail tradeoff. This finding does not rule out such decompositions.

### Only the leading packet is treated

The exact power-sum theorem in `RE-139` is a `K=0` result. The finite-order `u^{-k}` corrections require the perturbative stability budget already isolated in `RE-137`. No unproved transfer to arbitrary fixed `K` is used here.

## 7. Prior-art and novelty boundary

The two load-bearing ingredients are already classical and already anchored in this line: Turán's Second Main Theorem in Montgomery's *Ten Lectures on the Interface Between Analytic Number Theory and Harmonic Analysis*, and the ordinary Riemann--von Mangoldt tail control used in `RE-123`. Turán's power-sum method has a long history in zeta-function zero-free and zero-distribution arguments, and polynomial or absolute truncation of explicit zero sums is likewise standard.

A targeted prior-art search found standard Turán-method applications to zeta zero-free regions, modern explicit zero-free-region work, and computational treatments of sums over zeta zeros, but no theorem asserting that the particular Robin packet considered here is protected from its infinite exterior tail by the `RE-139` finite-core witness. No novelty is claimed for Turán's theorem, Riemann--von Mangoldt, or the tail estimate individually.

The line-specific delta is the exact splice (9)--(16): it converts the previously qualitative phrase **"exterior cancellation remains open"** into a falsifiable source budget with separately visible rightmost-amplitude, mode-complexity, and tail terms. It also shows why the most naive use of the currently available geometry-free amplitude comparison and global zero count cannot close that budget.

## 8. Consequence for the Robin-extremal frontier

After `RE-139`, horizontal spread is no longer an intrinsic finite-packet observability cost. After the present calculation, the remaining full-packet problem can be stated more sharply:

\[
\boxed{
\text{find a polynomial cutoff }T
\text{ for which }
G(U,T)e^{-\Lambda_\kappa N_T}M_0(U)
\gg \frac{\log(eT)}{T},
}
\tag{32}
\]

or replace one of the three ingredients by a stronger source-aware certificate.

The current Riemann--von Mangoldt and absolute-tail envelopes do not establish (32), and the crude rightmost amplitude transfer is already too lossy before the global mode-count penalty is charged. The next useful source theorem should therefore control **rightmost ordinate inflation jointly with horizontal gain**, identify a genuinely smaller effective mode count, or exploit signed exterior cancellation. Merely sharpening the same global zero-count constant does not address the first obstruction.