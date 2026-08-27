# PF-077 — prime-geodesic counting is already infinite at finite length

**Status:** `DECISIVE-NEGATIVE` for any standard prime-geodesic theorem, periodic-orbit counting law, or Chebyshev-style closed-geodesic counting invariant on the full prime-flute.

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

## 5. Relation to the distinguished cuffs

The bounded-window explosion is prime-specific through PF-069. Three consecutive normalized prime-gap fluctuations determine the exact cross-ratio

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

so it is precisely the **relative multi-gap / multi-cuff fluctuations**, after their common scale is removed, that force infinitely many primitive geodesics into bounded positive length windows.

This is another instance of the local-versus-relational principle already seen elsewhere: an individual cuff is locally universal, but multi-gap cross-ratios produce genuinely noncompact global orbit multiplicity.

## 6. Prior-art / novelty check

Known facts:

- the classical prime geodesic theorem and its dynamical generalizations count primitive closed geodesics on compact, finite-area, or geometrically finite hyperbolic quotients under hypotheses ensuring locally finite periodic-orbit data;
- infinite-type hyperbolic surfaces need not have discrete length spectrum; Basmajian–Kim studied when geometrically infinite surfaces do have a discrete length spectrum, and Fanoni–Fisac (2026) explicitly treat the discrete-length-spectrum infinite-type regime as a special class;
- Patterson–Sullivan and closed-orbit growth can require additional finiteness / recurrence hypotheses to be linked by standard counting theorems.

No novelty is claimed for the abstract observation that a non-discrete length spectrum can destroy a counting function. The project-specific decisive point is stronger and comes from PF-069: **the exact prime-flute has infinitely many primitive simple geodesics in every subwindow of a genuine compact positive interval**, so the standard prime-geodesic counting problem is not merely technically difficult or non-classical — it is undefined as a finite counting problem beyond a finite threshold.

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

Any meaningful replacement would first need a **spatially local, relative, or renormalized counting measure** that is canonically forced by the prime geometry. Merely subtracting the \(L\to0\) sector is insufficient, because PF-069/PF-077 show infinite multiplicity already at positive bounded lengths.
