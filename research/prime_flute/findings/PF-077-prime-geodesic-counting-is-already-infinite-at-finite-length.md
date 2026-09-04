# PF-077 — prime-geodesic counting is already infinite at finite length

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE/PRIME-GEODESIC-COUNTING + MATCHED-CONTROL-BLIND-AS-SELECTOR`. PF-069 supplies the positive primitive-length accumulation interval on the prime flute. PF-167 later shows that the exact all-composite shift clone inherits the same interval and the same finite-length counting explosion, so this obstruction kills the ordinary prime-geodesic branch but does not distinguish primality.

PF-069 proves that there is a nondegenerate compact interval

\[
I_L\Subset(0,\infty)
\]

such that every point of \(I_L\) is an accumulation point of lengths of explicit **primitive simple separating geodesics** of the prime-flute. This immediately has a stronger counting consequence which should be stated separately because it closes the prime-geodesic-theorem branch itself, not only Selberg trace/zeta constructions.

## 1. The primitive counting function becomes infinite at finite length

Let

\[
L_*:=\inf I_L.
\]

For any \(T>L_*\), choose a nonempty open interval

\[
J\Subset I_L\cap(0,T).
\]

By PF-069, \(J\) contains infinitely many distinct primitive simple separating geodesics. Hence

\[
\boxed{
\pi_X(T)
:=\#\{\gamma:\gamma\text{ primitive closed geodesic},\ \ell(\gamma)\le T\}
=\infty
}
\]

for every \(T>L_*\).

In fact the same is true after restricting to primitive **simple** geodesics:

\[
\boxed{
\pi_X^{\rm simple}(T)=\infty
\qquad(T>L_*).
}
\]

Thus the obstruction is not caused by self-intersections, iterates, or the short-orbit sector \(L\to0\). It is already present among simple primitive curves whose lengths stay inside a fixed compact positive interval.

PF-167 proves the identical conclusion for the exact all-composite shift clone `X_+`:

\[
\boxed{
\pi_{X_+}^{\rm simple}(T)=\pi_{X_+}(T)=\infty
\qquad(T>L_*).
}
\tag{1}
\]

The equality symbols in (1) assert only that both cardinalities are infinite, not equality of finite truncations, length multisets, or multiplicities.

## 2. Every ordinary weighted prime-geodesic count also diverges

Let \(w:(0,\infty)\to[0,\infty)\) be any weight which is bounded below by a positive constant on some nonempty open subinterval \(J\Subset I_L\). Then for every \(T>\sup J\),

\[
\boxed{
\sum_{\substack{\gamma\ \mathrm{primitive}\\\ell(\gamma)\le T}}
w(\ell(\gamma))
=+\infty.
}
\]

This applies in particular to the usual prime-geodesic / Chebyshev weights on compact positive length windows. Therefore neither counting by norm \(N(\gamma)=e^{\ell(\gamma)}\) nor the usual logarithmic weights can produce a finite counting function after any fixed positive threshold.

Because PF-167 transports the whole accumulation interval `I_L` to `X_+`, the same weighted divergence holds on the exact all-composite shift clone for every weight satisfying the same positive lower-bound condition on a subinterval of `I_L`.

## 3. There is no standard prime-geodesic theorem to salvage

For compact or finite-area hyperbolic surfaces, the classical prime geodesic theorem starts from the elementary finiteness fact that

\[
\#\{\gamma\text{ primitive}:\ell(\gamma)\le T\}<\infty
\]

for every finite \(T\), and then studies its asymptotic growth (classically \(\sim e^T/T\) in the compact finite-area setting). Analogous counting/equidistribution theorems for geometrically finite infinite-volume quotients likewise work in a regime where bounded length windows contain finitely many relevant primitive closed orbits.

The prime-flute violates this prerequisite before asymptotics are even considered:

\[
\boxed{
\text{bounded positive length window}
\Longrightarrow
\text{infinitely many primitive periodic orbits}.
}
\]

Hence there is no ordinary function \(\pi_X(T)\) with finite values for large \(T\), and therefore no statement of the form

\[
\pi_X(T)\sim \frac{e^{hT}}{hT}
\]

or any finite weighted variant can hold for the full surface.

PF-167 shows that this failure is not repaired by the exact all-composite shift control: its ordinary primitive-geodesic counting function also becomes infinite beyond the same finite threshold `L_*`. Thus the failure of a standard prime-geodesic theorem is a structural property shared by the matched pair, not evidence that the orbit-counting pathology detects prime labels.

## 4. Critical exponent and periodic-orbit growth decouple completely

PF-023 proved

\[
\delta(\Gamma_{\rm prime})=1
\]

and that the normalized Patterson–Sullivan measure is ordinary Lebesgue measure. In geometrically finite / finite-measure hyperbolic dynamics, one often relates \(\delta\), orbit growth, Bowen–Margulis dynamics, and primitive closed-geodesic growth.

PF-077 shows that this bridge cannot be imported here. The critical exponent remains the perfectly finite universal value \(1\), while primitive periodic-orbit counting is already infinite at finite length.

Thus, for the prime-flute,

\[
\boxed{
\delta=1
\quad\text{does not encode a finite exponential prime-geodesic growth law}.
}
\]

This is not a contradiction with Patterson–Sullivan theory: the group is infinitely generated, the Bowen–Margulis/Liouville measure is infinite, and the primitive length spectrum is non-discrete. It is a warning that the usual geometric-finiteness hypotheses connecting these quantities are doing essential work.

The matched-control result does not require a separate critical-exponent calculation for the clone. PF-167 concerns only the positive-window primitive length accumulation/counting pathology and shows that this particular obstruction already survives replacement of the prime labels by exact composites.

## 5. Relation to the distinguished cuffs and the matched control

Three consecutive normalized prime-gap fluctuations determine the exact cross-ratio

\[
\chi=\frac{Y(X+Y+Z)}{XZ}
\]

and hence the primitive separating length

\[
L=4\operatorname{arsinh}\sqrt\chi.
\]

The distinguished cuffs satisfy

\[
\ell_n=2\log\frac{4p_n}{g_n}+o(1),
\]

so the **relative multi-gap / multi-cuff fluctuations**, after their common scale is removed, force infinitely many primitive geodesics into bounded positive length windows on the prime flute.

The later control changes the interpretation of that fact. PF-166 proves that the exact `p_n -> p_n+1` all-composite clone has asymptotically the same complete marked tail translation-length function, and PF-167 applies this to the escaping PF-069 separator sequences. Therefore the bounded-window explosion is **not prime-specific**: the clone inherits the same interval `I_L`. The relational geometry is genuinely encoded, but the encoded data survive this exact all-composite replacement.

## 6. Prior-art / novelty check

Known facts:

- the classical prime geodesic theorem and its dynamical generalizations count primitive closed geodesics on compact, finite-area, or geometrically finite hyperbolic quotients under hypotheses ensuring locally finite periodic-orbit data;
- infinite-type hyperbolic surfaces need not have discrete length spectrum; Basmajian–Kim studied when geometrically infinite surfaces do have a discrete length spectrum, and Fanoni–Fisac (2026) explicitly treat the discrete-length-spectrum infinite-type regime as a special class;
- Patterson–Sullivan and closed-orbit growth can require additional finiteness / recurrence hypotheses to be linked by standard counting theorems;
- transport of marked length accumulation under an asymptotically bilipschitz marking is elementary/classical and is classified in PF-166 against infinite-type length-spectrum Teichmuller theory.

No novelty is claimed for the abstract observation that a non-discrete length spectrum can destroy a counting function. The project-specific decisive point from PF-069 is that the exact prime flute has infinitely many primitive simple geodesics in every subwindow of a genuine compact positive interval. PF-167 adds the equally important matched-control classification: the exact all-composite shift clone has the same accumulation interval and hence the same failure of finite primitive counting.

## 7. Research consequence

Close the branch

\[
\boxed{
\text{prime-flute}
\to
\text{ordinary primitive-geodesic counting}
\to
\text{prime geodesic theorem / periodic-orbit entropy}
\to
\text{prime-gap spectral law}.
}
\]

The first failure is already fatal to the standard counting architecture, and PF-167 shows that the failure itself is **matched-control-blind**. Any meaningful replacement would need a spatially local, relative, renormalized, or operator-level counting object that is canonically forced by the geometry and can distinguish the prime flute from the all-composite shift clone. Merely subtracting the `L -> 0` sector, or merely observing infinite positive-window primitive multiplicity, is insufficient.