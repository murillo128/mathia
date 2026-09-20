# NB-243 — Carrier pair energy controls Ford decay without an absolute phase anchor

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + CORRECTION/REFINEMENT + CARRIER-PAIR-ENERGY + DEPTH-MARKED + NB-240/NB-242-REFINEMENT + SOURCE-ONLY`.

`NB-242` proves a correct information-theoretic statement: translation-invariant correlations cannot recover the **complex phase** of the anchored Ford coefficient. Its half-period twins have identical relative correlations at every finite order while the signed Ford coefficient changes sign.

For the live source problem, however, recovering that sign is stronger than necessary. To prove that the critical Ford residue is `o(1)`, it is enough to prove that its **modulus** is `o(1)`. Squaring the exact Ford coefficient removes the absolute carrier phase automatically and produces a depth-marked two-point statistic at the carrier frequency. The half-period twins that defeated phase reconstruction do not defeat this energy observable: both have order-one carrier energy, so a theorem forcing that energy to vanish would reject both without ever deciding whether their common carrier phase is `+1` or `-1`.

Thus the route consequence of `NB-242` was too strong. An absolute phase anchor is necessary for **signed reconstruction**, but it is not necessary for **decay**. A sufficiently local, Ford-depth-marked, carrier-resolved pair-energy estimate remains a viable source theorem. The published short-interval pair-correlation theorem audited in `NB-240` still does not supply such an estimate because its height window, test family and scale are too coarse; the point here is that the missing ingredient is no longer an absolute `U(1)` phase reference.

## 1. Exact Ford coefficient and its squared modulus

Retain the Ford variables used in `NB-231`--`NB-242`:

\[
Q:=\log(10+|t|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR,
\qquad
J:=\frac RH,
\qquad
\omega:=\frac XH=YJ.
\tag{1}
\]

In the conservative transition regime, `Y` stays bounded above and below by positive constants and

\[
1\ll J\le \log Q.
\tag{2}
\]

Write

\[
\tau_j:=H(\gamma_j-t),
\qquad
 d_j:=X(1-\beta_j)-\log J,
\tag{3}
\]

for the scaled ordinate and Ford depth of each zero in the critical layer, counting multiplicity by repeating atoms. For the same smooth source profile as in `NB-231`--`NB-237`, absorb every non-carrier factor into the mark

\[
 b_{j,J}
 :=
 e^{-d_j}\,\chi(d_j)\,
 F\!\left(
 \tau_j+i\eta_{j,J}
 \right),
\qquad
\eta_{j,J}
:=
\frac{\log J+d_j+r}{YJ}.
\tag{4}
\]

Here `chi` is a fixed cutoff to the critical Ford layer and `F` is the Schwartz profile already used in the exact carrier representation. Up to the harmless fixed factor `e^{-r}`, the critical residue is

\[
\boxed{
\mathcal R_J
=
\frac{e^{-r}}J
\sum_j
 b_{j,J}e^{i\omega\tau_j}.
}
\tag{5}
\]

The carrier phase is anchored to `t` because

\[
\omega\tau_j
=
X(\gamma_j-t).
\tag{6}
\]

Now square the modulus of (5). There is no approximation:

\[
\begin{aligned}
|\mathcal R_J|^2
&=
\frac{e^{-2r}}{J^2}
\sum_{j,k}
 b_{j,J}\overline{b_{k,J}}
 e^{i\omega(\tau_j-\tau_k)} \\
&=
\frac{e^{-2r}}{J^2}
\sum_{j,k}
 b_{j,J}\overline{b_{k,J}}
 e^{iX(\gamma_j-\gamma_k)}.
\end{aligned}
\tag{7}
\]

The selected height `t` has disappeared from the **oscillatory phase**. Equation (7) is an exact depth/profile-marked two-point form factor at the Ford carrier.

This is the key correction. The source problem asks for

\[
\mathcal R_J=o(1),
\tag{8}
\]

and (7) shows that (8) is equivalent to proving that one nonnegative two-point energy tends to zero. Recovering the complex argument of `\mathcal R_J` is unnecessary.

## 2. The diagonal already vanishes at the existing population scale

The two-point reduction would be useless if the diagonal in (7) carried an order-one floor. It does not.

On the fixed Ford-depth support of `chi`, the marks `b_{j,J}` are uniformly bounded, and the Schwartz decay of `F` handles the ordinate tails. The same carrier-window population estimate used in `NB-230`--`NB-234` gives, in this regime,

\[
\sum_j |b_{j,J}|^2=O(J).
\tag{9}
\]

Therefore the diagonal contribution is

\[
\boxed{
\frac{e^{-2r}}{J^2}
\sum_j|b_{j,J}|^2
=O\!\left(\frac1J\right)
=o(1).
}
\tag{10}
\]

Consequently, the entire remaining source problem can be written as the off-diagonal condition

\[
\boxed{
\frac1{J^2}
\sum_{j\ne k}
 b_{j,J}\overline{b_{k,J}}
 e^{iX(\gamma_j-\gamma_k)}
=o(1),
}
\tag{11}
\]

with the understanding that the ordered-pair sum is real after pairing `(j,k)` with `(k,j)`.

Equation (11) is not an unweighted Montgomery statistic. It keeps exactly the information that earlier findings showed cannot be discarded: the Ford-depth marks, the source profile, the microscopic selected-height window, and the moving carrier frequency. What it does **not** require is the missing absolute phase coordinate isolated in `NB-242`.

A useful probabilistic sanity check is immediate. If `M=Theta(J)` bounded-weight atoms have decorrelated carrier phases, then the natural square-root size of the numerator in (5) is `Theta(sqrt(J))`, giving

\[
|\mathcal R_J|^2=Theta(J^{-1}).
\tag{12}
\]

The order-one obstruction arises only when the off-diagonal terms add coherently. That is exactly what (11) measures.

## 3. The half-period twins are detected, not hidden, by pair energy

Return to the matched controls of `NB-241`--`NB-242`. Put

\[
M=\lfloor\delta J\rfloor,
\qquad
 a=\frac{2\pi}{\omega},
\qquad
 h=\frac{\pi}{\omega},
\tag{13}
\]

and take one packet at

\[
\tau_j=ja
\tag{14}
\]

and its translate at

\[
\tau_j'=ja+h.
\tag{15}
\]

Ignoring only the `o(1)` profile displacement already quantified in `NB-241`, the first packet has carrier phase `+1` and the second has carrier phase `-1`. Thus their signed Ford residues differ by order one, while every statistic depending only on relative ordinates agrees.

`NB-242` interpreted that equality as a phase-anchor obstruction. For decay, however, the correct comparison is

\[
|\mathcal R_J|^2.
\]

For a common bounded depth and a profile patch on which `F` stays bounded away from zero,

\[
\begin{aligned}
|\mathcal R_J|^2
&\asymp
\frac1{J^2}
\left|
\sum_{j=1}^{M}e^{i\omega\tau_j}
\right|^2 \\
&=
\frac{M^2}{J^2}
\longrightarrow \delta^2,
\end{aligned}
\tag{16}
\]

and the translated twin has exactly the same leading energy. Hence

\[
\boxed{
\text{the twins have identical relative pair data and identical order-one Ford energy.}
}
\tag{17}
\]

That is **not** a failure of pair energy. It is precisely the desired behavior: both twins are dangerous, and a source theorem whose conclusion is (11) would exclude both. There is no need to decide which one contributes with positive or negative phase before excluding an order-one residue.

This distinguishes two logically different tasks:

\[
\text{recover }\mathcal R_J
\quad\text{versus}\quad
\text{prove }|\mathcal R_J|\to0.
\tag{18}
\]

`NB-242` gives a genuine obstruction to the first task from translation-invariant data. Equation (7) shows that the second task survives entirely inside a two-point observable.

## 4. What the viable pair theorem must actually control

The reduction does not revive ordinary pair correlation in its published form. It specifies a much narrower moving statistic.

The carrier phase in (11) is

\[
e^{iX(\gamma_j-\gamma_k)}.
\tag{19}
\]

In the usual Montgomery parameterization

\[
T^{i\alpha(\gamma_j-\gamma_k)}
=
e^{i\alpha Q(\gamma_j-\gamma_k)},
\]

this corresponds to the moving frequency

\[
\boxed{
\alpha_F=\frac XQ
\asymp
\frac RQ
=
Q^{-1/3}(\log Q)^{1/3}
\longrightarrow0.
}
\tag{20}
\]

At the same time, the zero sum must be restricted to the deterministic Ford window

\[
|\gamma-t|\lesssim\frac1H=\frac JR=o(1)
\tag{21}
\]

and to the critical horizontal layer

\[
X(1-\beta)-\log J=O(1).
\tag{22}
\]

Finally it must keep the marks in (4), or a quantitatively equivalent partition that controls them uniformly.

Thus a sufficient source theorem has the schematic form

\[
\boxed{
\frac1{J^2}
\sum_{\substack{\rho_j,\rho_k\text{ in the Ford window}\\j\ne k}}
 b_{j,J}\overline{b_{k,J}}
 e^{iX(\gamma_j-\gamma_k)}
=o(1)
}
\tag{23}
\]

uniformly in the selected block height `t` and the allowed Ford parameters.

This target retains the three requirements that survived `NB-240`: selected-height localization, Ford-depth conditioning, and carrier-scale retuning. The fourth requirement proposed by `NB-242` — an **absolute carrier phase anchor** — is not needed for the decay conclusion.

## 5. Why the published short-interval theorem still does not close (23)

The correction above does not invalidate the method boundary in `NB-240`. Biao Wang's September 2026 short-interval Montgomery theorem is genuinely local compared with classical global pair correlation, but it works in power-length intervals `(T,T+T^theta]` with a fixed smooth test. `NB-240` showed two independent mismatches with the Ford packet: a `Theta(J)` packet fits below the published error budget, and the fixed mean-spacing test suppresses the packet's off-diagonal carrier lattice rather than resolving it.

Equation (23) asks for exactly the missing regime. The test family must move so that its Fourier mode is `alpha_F=X/Q`, the height cutoff must collapse from a power of `T` to `J/R`, and the statistic must retain the horizontal depth marks. Wang's theorem, as currently stated, gives no uniform control in that combined limit. The fresh prior-art check for this pass found no theorem that supplies all three properties simultaneously. See Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals*, arXiv:2609.07918 (7 September 2026).

Classically, the conceptual identification of pair correlation with a squared exponential sum is already built into Montgomery's form factor: after smoothing/averaging one studies quantities of the shape

\[
\left|\sum_\gamma W(\gamma)e^{i\xi\gamma}\right|^2,
\tag{24}
\]

which expand into difference phases. No novelty is claimed for that harmonic identity. The line-local content is that the exact Ford residue has **precisely** the normalization for which this squared form factor is the needed source norm, with the diagonal vanishing as `1/J` and the dangerous matched packet contributing order one.

No new external theorem is load-bearing in (7)--(11), so this finding does not require a new durable `SOURCES.md` dependency.

## 6. Representation audit

The algebraic step

\[
\left|\sum_j a_je^{i\theta_j}\right|^2
=
\sum_{j,k}a_j\overline{a_k}e^{i(\theta_j-\theta_k)}
\tag{25}
\]

is completely representation-generic. It would hold for any marked point process. The arithmetic content enters through four previously established Nyman/zeta features: the Ford normalization `1/J`, the local population scale `O(J)`, the carrier `X`, and the depth/profile marks produced by the exact Euler-shell representation.

Accordingly, this is not a new theorem about the actual zeros of `zeta` and not a new lower bound for the Nyman--Beurling distance. It is a **route correction**. It identifies a weaker sufficient statistic than the anchored one-point current of `NB-237` and removes an unnecessary information requirement introduced in the interpretation of `NB-242`.

There is also no contradiction with `NB-233`. That finding showed that **unweighted** phase equidistribution can coexist with order-one residue when depth is phase-locked. Equation (23) retains the depth mark `e^{-d_j}` on both legs, so the adversarial modulation from `NB-233` appears directly in the pair energy. Replacing (23) by an unweighted carrier pair statistic would lose exactly the information `NB-233` proved necessary.

Likewise there is no contradiction with `NB-232`: a global pair average can dilute a sparse bad block. Equation (23) is deterministic at the selected `t`; no averaging over unrelated heights is allowed.

## 7. Adversarial review and falsification boundary

The strongest objection is that (7) may be merely tautological: the pair energy is exactly the square of the quantity we wanted to bound. That objection is partly correct and defines the result's scope. `NB-243` does **not** make the analytic estimate easier by itself. Its contribution is to correct the information frontier: a theorem need not reconstruct the missing complex phase, and pair-correlation methods are not ruled out by the half-period twins solely because they are translation invariant.

Second, the marks matter. A theorem for

\[
\sum_{j,k}e^{iX(\gamma_j-\gamma_k)}
\]

without Ford depth or profile weights does not imply (23). Depth-phase locking from `NB-233` is an explicit counterexample to such a simplification. Any future pair theorem must either carry these marks or control the error made by removing them.

Third, the selected-height envelope still depends on `t`. The statement here is only that **absolute carrier phase** relative to `t` is unnecessary after taking the square modulus. Localizing the correct block remains essential. Translating the entire zero packet out of the Ford window changes the observable because the source profile changes.

Fourth, the diagonal estimate (10) uses the already audited `O(J)` effective population scale. If a future representation admits superlinear critical population after weighting, the diagonal must be rechecked and may cease to vanish.

Fifth, average pair correlation in `t` is insufficient for the deterministic blockwise source problem. An exceptional set of block heights could still carry order-one pair energy. The needed theorem is uniform, or must come with an exceptional-set mechanism strong enough to be transported through the destination argument.

Sixth, if a later stage of the proof needs the **sign** or argument of `\mathcal R_J`, rather than merely its small modulus, the phase-anchor obstruction of `NB-242` returns unchanged. The correction applies specifically to the present goal of proving `\mathcal R_J=o(1)`.

A decisive falsification of this finding would be a configuration satisfying (23) while the exact residue (5) stays bounded away from zero. Equation (7) rules that out identically. The open problem is analytic, not algebraic: whether the actual zeros of `zeta` satisfy a deterministic marked carrier-energy estimate strong enough for (23).

## 8. Consequence for the live frontier

The source-side frontier after `NB-243` can be stated more economically than after `NB-242`.

We do **not** need a theorem that assigns the local zero packet an absolute Ford phase. We need a theorem that prevents order-one **coherence energy** at the carrier. In exact variables, that means controlling the depth/profile-marked off-diagonal form factor (23) in the `J/R` height window and at frequency `X`.

The hierarchy is now:

\[
\text{fixed/global pair correlation}
\quad\text{is too coarse (`NB-232`, `NB-240`),}
\]

\[
\text{carrier resolution}
\quad\text{is necessary (`NB-241`),}
\]

and

\[
\boxed{
\text{carrier-resolved marked pair ENERGY is sufficient for decay;}
\quad
\text{absolute phase recovery is not.}
}
\tag{26}
\]

This reopens a narrower pair-correlation route that `NB-242` appeared to close. The correct target is not “better pair correlation” in general, but a **deterministic microlocal form-factor bound** for the critical Ford layer.