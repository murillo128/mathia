# PF-110 — zero systole obstructs bounded ideal triangulations

**Status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`. This closes the Whitney--Šarić bounded-ideal-triangulation route that had been proposed inside the accepted prime/composite relative-operator clue. It does **not** rule out a direct pants/collar gluing, an arbitrary quasiconformal comparison between the prime flute and its composite clone, strong equivalence of their metrics, or compactness of a relative resolvent.

## Claim

Let `X` be a complete hyperbolic Riemann surface which admits a **bounded ideal triangulation** in the sense of Whitney--Šarić: the triangulation is locally finite, all ideal endpoints are punctures, puncture valence is uniformly bounded, and all edge shears are uniformly bounded.

Then

\[
\boxed{\operatorname{sys}(X)>0.}
\tag{1}
\]

Consequently, the exact prime flute cannot admit such a triangulation, because the established prime-flute short-orbit sector contains distinct primitive closed geodesics with lengths tending to zero (PF-005, strengthened and used explicitly in PF-035).

Thus the program

\[
\text{prime flute}
\longrightarrow
\text{bounded ideal triangulation}
\longrightarrow
\text{Whitney--Šarić shear coordinates}
\longrightarrow
\text{global relative metric/operator comparison}
\]

fails already at its first geometric gate.

## 1. Whitney--Šarić reduce every bounded triangulation to zero shear

Whitney--Šarić, *Bounded ideal triangulations of infinite Riemann surfaces* (J. London Math. Soc. 112 (2025), e70276; DOI `10.1112/jlms.70276`; arXiv:2502.05590), prove in Proposition 4.2 that if `X` has a bounded ideal triangulation, then there is a quasiconformal map

\[
f:X\to X_0
\]

onto a Riemann surface `X_0` carrying a bounded ideal triangulation with all shears equal to zero. They further identify the covering group of `X_0` as a subgroup

\[
\Gamma_0<\operatorname{PSL}_2(\mathbb Z).
\tag{2}
\]

This is not merely a heuristic use of their coordinate theorem: Proposition 4.2 explicitly constructs the zero-shear representative by lifting the triangulation, using the induced quasisymmetric boundary homeomorphism, and extending it quasiconformally.

Because `X_0` is a Riemann surface rather than an orbifold, its deck group is torsion-free.

## 2. A torsion-free modular subgroup has a uniform closed-geodesic floor

Let `gamma in Gamma_0` represent a nonperipheral closed geodesic. Then `gamma` is hyperbolic. Choose a lift to `SL_2(Z)`. Its trace is an integer, and hyperbolicity gives

\[
|\operatorname{tr}\gamma|>2.
\]

Hence necessarily

\[
|\operatorname{tr}\gamma|\ge3.
\tag{3}
\]

For a hyperbolic element of `PSL_2(R)`, the translation length is

\[
\ell(\gamma)
=2\operatorname{arcosh}\frac{|\operatorname{tr}\gamma|}{2}.
\]

Therefore every closed geodesic on `X_0` satisfies

\[
\boxed{
\ell_{X_0}(\gamma)
\ge
L_{\rm mod}:=2\operatorname{arcosh}\frac32
\approx1.924847.
}
\tag{4}
\]

In particular `sys(X_0)>=L_mod>0`. No finite-index assumption is needed: the integer-trace lower bound applies to every subgroup of `PSL_2(Z)`.

## 3. Quasiconformal equivalence preserves the dichotomy `sys>0` versus `sys=0`

Let `f:X->X_0` have quasiconformal dilatation `K<infinity`. The classical Wolpert length inequality, stated for hyperbolic Riemann surfaces in Shiga, *On the hyperbolic length and quasiconformal mappings* (Complex Variables 50 (2005), 123--130; DOI `10.1080/02781070412331328206`), gives for every closed geodesic `c` on `X`

\[
\frac1K\,\ell_X(c)
\le
\ell_{X_0}(f_*(c))
\le
K\,\ell_X(c).
\tag{5}
\]

Combining the right inequality in (5) with (4),

\[
\ell_X(c)
\ge
\frac{L_{\rm mod}}{K}
>0.
\tag{6}
\]

Taking the infimum over nonperipheral closed geodesics proves (1).

Equivalently, **zero systole is a quasiconformal-class obstruction to Whitney--Šarić bounded ideal triangulations**.

## 4. Application to the prime flute

PF-005 derives a sequence of multi-gap hyperbolic lengths tending to zero from the isolated small-middle-gap pattern, and PF-035 records the strengthened stable consequence used throughout the later dynamical analysis: there are infinitely many distinct primitive closed geodesics

\[
\gamma_j,
\qquad
\ell(\gamma_j)\to0.
\]

Hence

\[
\operatorname{sys}(X_{\rm prime})=0.
\tag{7}
\]

If `X_prime` admitted a bounded ideal triangulation, Sections 1--3 would force `sys(X_prime)>0`, contradicting (7). Thus

\[
\boxed{
X_{\rm prime}\text{ admits no bounded ideal triangulation in the Whitney--Šarić sense.}
}
\tag{8}
\]

This obstruction is intrinsic and does not depend on the chosen fan, pants decomposition, prime labels, or the proposed `p_n -> p_n+1` matching. Trying a more clever bounded-valence triangulation cannot evade it.

## 5. Consequence for the accepted relative-operator clue

The accepted clue had recently identified bounded ideal triangulations as a promising way around the failure of upper-bounded Fenchel--Nielsen hypotheses: if one could find a bounded-valence triangulation with bounded base shears, PF-106 would make the matched prime/composite shear defect uniformly small.

PF-110 rules out that route completely. The problem is not that the obvious infinite fan has infinite valence, nor that a suitable combinatorial triangulation has not yet been found. **No bounded ideal triangulation can exist on the zero-systole prime flute at all.**

The relative-operator clue nevertheless remains open because Whitney--Šarić bounded shear coordinates were only a proposed sufficient framework. The surviving route is to construct the common-manifold comparison directly, for example by gluing the local pants/hexagon/collar comparisons already supported by PF-107--PF-109 and Minsky's local bilipschitz lemma, and then audit strong equivalence or the stronger weighted scattering hypotheses. PF-110 gives no obstruction to such a direct map.

## 6. Prior-art / novelty audit

No novelty is claimed for any of the three ingredients:

1. Whitney--Šarić Proposition 4.2 gives the quasiconformal zero-shear representative with covering group contained in `PSL_2(Z)`;
2. integer traces and `|tr gamma|=2 cosh(ell(gamma)/2)` give the modular length floor;
3. Wolpert's quasiconformal length inequality is classical and Shiga states it for hyperbolic Riemann surfaces while generalizing the loxodromic formulation.

Directed searches did not locate the explicit corollary "bounded ideal triangulation implies positive systole" in Whitney--Šarić or a separate source stating it under that name. It is, however, an immediate literature-derived consequence rather than a claim of a new general theorem. The durable project contribution is its application as a **decisive falsification of the bounded-triangulation branch of the prime-flute operator clue**.

This result is not evidence for RH and does not distinguish primes from composite controls. It is a geometric admissibility obstruction for one proposed analytic framework.

## 7. Audit / falsification core

The proof can be falsified at four explicit gates:

1. check Whitney--Šarić Proposition 4.2 really produces a quasiconformal `X -> X_0` with `Gamma_0 < PSL_2(Z)` for every surface carrying their bounded ideal triangulation;
2. check that `X_0` is a genuine Riemann surface, so its deck group has no elliptic stabilizers, and that every nonperipheral closed class corresponds to a hyperbolic element;
3. verify the integer-trace bound (3) and translation-length formula (4);
4. apply Wolpert's inequality (5) in the direction giving (6), then combine with the independently persisted zero-systole sequence of PF-035.

Breaking any of these gates would reopen the bounded-triangulation route. Short of that, future work on the accepted relative-operator clue should not spend effort searching for a Whitney--Šarić bounded triangulation of the prime flute.

## References

- D. Šarić, C. Whitney, *Bounded ideal triangulations of infinite Riemann surfaces*, Journal of the London Mathematical Society 112 (2025), e70276. DOI `10.1112/jlms.70276`; arXiv:2502.05590.
- H. Shiga, *On the hyperbolic length and quasiconformal mappings*, Complex Variables, Theory and Application 50 (2005), 123--130. DOI `10.1080/02781070412331328206`.
- S. Wolpert, *The length spectra as moduli for compact Riemann surfaces*, Annals of Mathematics 109 (1979), 323--351.
- PF-005 and PF-035 in this research ledger.
