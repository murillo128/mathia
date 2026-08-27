# PF-070 — zero systole precludes any standard strict uniformly-expanding transfer coding

**Status:** `DECISIVE-NEGATIVE` for Bowen–Series/Mayer/Pohl–Wabnitz style transfer-operator approaches that preserve the periodic-geodesic dictionary and use the geometric derivative potential.

The prime-flute contains infinitely many primitive closed geodesics \(\gamma_j\) with

\[
L_j:=\ell(\gamma_j)\to0.
\]

This was established earlier from the exact orthogonal-circle cross-ratio geometry and isolated prime-gap configurations. The consequence here is independent of how those short geodesics are produced.

## 1. Periodic multipliers equal exponential geodesic lengths

Let \(F\) be a piecewise-Möbius discretization of the geodesic flow of the usual Bowen–Series/Ruelle type. Assume that periodic orbits of \(F\) are in bijection with primitive closed geodesics and that the transfer weight is the geometric potential

\[
|F'|^{-s}.
\]

For a periodic point \(x\) of least period \(n\), let \(g\in\Gamma\) be the hyperbolic element obtained by composing the corresponding Möbius branches. The associated closed geodesic has translation length \(\ell(g)\), and at the expanding fixed point

\[
\boxed{\log |(F^n)'(x)|=\ell(g).}
\]

Equivalently, the two fixed-point multipliers of a hyperbolic Möbius element are \(e^{\pm\ell(g)}\).

This is the standard periodic-orbit dictionary behind the Selberg/Ruelle transfer formalism.

## 2. Uniform expansion forces a positive systole

A strict transfer-operator approach in the sense used in modern Selberg-zeta constructions requires a uniformly expanding discrete dynamical system after any allowed cusp acceleration. In the simplest equivalent periodic-orbit form, there is a constant \(\Lambda>1\) such that every periodic point of least period \(n\ge1\) satisfies

\[
|(F^n)'(x)|\ge \Lambda^n.
\]

Combining this with the geometric multiplier identity gives

\[
\ell(\gamma)=\log |(F^n)'(x)|\ge n\log\Lambda\ge\log\Lambda.
\]

Hence

\[
\boxed{\operatorname{sys}(X)\ge\log\Lambda>0.}
\]

Therefore any hyperbolic surface with primitive lengths accumulating at zero cannot admit such a coding while retaining the exact periodic-geodesic/derivative correspondence.

For the prime-flute,

\[
\operatorname{sys}(X_{\rm prime})=0,
\]

so

\[
\boxed{\text{no strict uniformly-expanding Bowen–Series/Mayer coding of this type exists}.}
\]

## 3. Cuspidal acceleration cannot repair this obstruction

For geometrically finite surfaces, non-uniform expansion caused by parabolic cusp excursions can be repaired by inducing/accelerating the parabolic branches. This is the mechanism used in the fast transfer operators of Mayer–Pohl and in the strict transfer-operator framework of Pohl–Wabnitz.

That mechanism does not apply to the present obstruction. The elements \(\gamma_j\) above are primitive **hyperbolic** closed geodesics with

\[
e^{L_j}\to1.
\]

Any acceleration that remains faithful to periodic geodesics must retain a periodic orbit representing every \(\gamma_j\). Its total geometric multiplier remains exactly \(e^{L_j}\), irrespective of how the word is regrouped into accelerated branches. Thus the multipliers of periodic orbits still approach \(1\), contradicting uniform expansion.

So the problem is not a slowly-coded cusp. It is a sequence of genuinely hyperbolic periodic orbits approaching the identity in multiplier.

## 4. Consequence for nuclear/Fredholm transfer operators

The standard strict transfer-operator machinery obtains nuclearity of order zero on holomorphic Banach spaces from uniform contraction of inverse branches / uniform expansion of the forward map, and then defines

\[
\det(1-\mathcal L_s)
\]

with the periodic-orbit trace expansion reproducing Selberg zeta.

PF-035 already showed that the ordinary Selberg/Ruelle Euler product of the prime-flute has no nontrivial initial half-plane because factors coming from \(L_j\to0\) fail to approach \(1\). PF-070 is logically earlier and stronger for this particular transfer framework:

\[
\boxed{
\text{the uniformly-expanding dynamical system needed to build the usual nuclear operator cannot exist at all.}
}
\]

Thus one cannot bypass the divergent Euler product by saying "construct the standard nuclear transfer operator first, then define its Fredholm determinant by analytic continuation." The standard route to that nuclear operator already fails at the expansion axiom.

## 5. Relation to earlier prime-flute results

This sharpens PF-042. There we found the dichotomy

- deterministic principal-series transport telescopes to endpoint data;
- branched periodic-orbit transfer inherits the short-orbit Selberg obstruction.

PF-070 identifies the dynamical reason for the second branch:

\[
\boxed{
L_j\to0
\Longleftrightarrow
\text{periodic multipliers }e^{L_j}\to1
\Longrightarrow
\text{no faithful uniformly-expanding coding}.
}
\]

The exact interior/exterior involution and orthogonal-circle geometry do not alter this conclusion; they conjugate the same hyperbolic elements and preserve translation lengths.

## 6. Novelty / prior-art check

Known ingredients:

- In the transfer-operator formalism for Fuchsian groups, periodic geodesics correspond to periodic symbolic orbits and the geometric derivative multiplier is \(e^{\ell(\gamma)}\).
- Strict transfer-operator approaches require uniform expansiveness and periodic-orbit fidelity; this is stated explicitly in the modern Pohl–Wabnitz framework.
- Parabolic acceleration is a standard way to repair non-uniform expansion caused by cusps on geometrically finite surfaces.

The implication "faithful uniformly-expanding geometric coding \(\Rightarrow\) positive systole" is elementary once these axioms are combined, and no novelty is claimed for it as an abstract statement. Directed searches did not reveal a treatment of the zero-systole infinitely generated flute case in the strict-transfer literature.

The substantive conclusion for this project is negative: the prime-flute lies outside the standard strict Selberg/Ruelle transfer-operator paradigm for a reason stronger than infinite generation alone.

## Research gate

Any surviving transfer-like construction must abandon at least one of the standard ingredients:

1. uniform expansion;
2. the ordinary geometric derivative potential;
3. a one-to-one periodic-orbit encoding of all primitive geodesics;
4. the ordinary Fredholm trace expansion over periodic orbits.

If such an operator exists, its renormalization of the near-identity hyperbolic sector must be part of the definition and must be forced by the prime-derived geometry, not inserted solely to restore compactness or convergence.
