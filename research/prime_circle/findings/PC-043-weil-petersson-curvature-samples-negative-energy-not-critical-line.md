# PC-043 — Weil–Petersson curvature samples negative energy, not the critical line

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for interpreting the fixed twisted resolvent in PC-042 as a direct Riemann-critical-line or zeta-zero detector. No novelty claim is made for the Tromba–Wolpert operator, positivity of the hyperbolic Laplacian, the standard automorphic spectral parameter `s(1-s)`, or the zero-free half-plane of the Selberg Euler product.

PC-042 established a genuinely nonlinear prime-circle mechanism on the full roots-of-unity cover tower: Weil–Petersson curvature couples cyclic-character birth modes through a universal twisted Green/resolvent operator on the thrice-punctured sphere. It deliberately left the operator at a fixed spectral value and did not identify that value with the Riemann critical line.

The fixed value can in fact be identified exactly. It lies at **negative Laplace energy `-2`**, uniformly inside the ordinary resolvent set of every unitary twist. In the standard automorphic parameterization it corresponds to `s=2` (equivalently `s=-1`), not to `Re(s)=1/2`. This rules out the most direct attempt to turn PC-042 itself into a Hilbert–Pólya/critical-line mechanism.

## 1. The Weil–Petersson Green operator is a positive negative-energy resolvent

Retain the sign convention of PC-042: the hyperbolic Laplacian on the unitary flat line bundle of holonomy `theta` is non-positive,

\[
\Delta_\theta\le 0,
\]

and the Tromba–Wolpert curvature operator is

\[
\mathscr D_\theta=-2(\Delta_\theta-2)^{-1}.
\]

Introduce the standard nonnegative self-adjoint Laplacian

\[
L_\theta:=-\Delta_\theta\ge0.
\]

Then, exactly,

\[
\boxed{
\mathscr D_\theta=2(L_\theta+2)^{-1}.
}
\]

This identity fixes the spectral location without any normalization ambiguity. By the spectral theorem, if `lambda >= 0` ranges over the spectral measure of `L_theta`, then `mathscr D_theta` has multiplier

\[
\boxed{
\frac{2}{\lambda+2}.
}
\]

Consequently

\[
\boxed{
0\le \mathscr D_\theta\le I,
\qquad
\|\mathscr D_\theta\|\le1
}
\]

for every unitary holonomy `theta`. In particular, the evaluation energy `-2` is separated from the nonnegative spectrum of `L_theta` by a gap of at least `2`; no pole, resonance, or threshold singularity can occur at the value selected by Weil–Petersson curvature.

The sign and positivity are classical. Wolpert's curvature formula and its punctured-surface version used in PC-042 employ this Green operator, and the standard Weil–Petersson literature writes `D=-2(Delta-2)^{-1}` with the non-positive Laplacian convention and obtains a positive self-adjoint operator. The point here is the consequence for the prime-circle spectral interpretation.

## 2. The exact automorphic spectral parameter is `s=2` or `s=-1`

For the nonnegative hyperbolic Laplacian, use the standard automorphic resolvent parameterization

\[
R_\theta(s)
:=
\bigl(L_\theta-s(1-s)\bigr)^{-1}.
\]

To identify the Weil–Petersson operator, solve

\[
s(1-s)=-2.
\]

The two solutions are

\[
\boxed{s=2\quad\text{and}\quad s=-1.}
\]

Therefore

\[
\boxed{
\mathscr D_\theta
=2R_\theta(2)
=2R_\theta(-1),
}
\]

where the two `s` values are the usual pair giving the same Laplace spectral parameter. The physically direct point is `s=2`, in the ordinary right half-plane where the resolvent is unproblematic.

This is sharply different from the critical-line parameterization

\[
s=\frac12+it,
\]

for which

\[
\boxed{
s(1-s)=\frac14+t^2\ge\frac14
\qquad(t\in\mathbb R).
}
\]

The Weil–Petersson curvature operator therefore samples the twisted Laplacian at energy `-2`, while the standard critical-line family samples positive energies at or above `1/4`. They are not two descriptions of the same evaluation.

## 3. A tempting apparent critical-line value is exactly a sign error

There is a particularly dangerous false positive. If one sees the constant `2` in

\[
-2(\Delta_\theta-2)^{-1}
\]

but forgets that PC-042 uses a **non-positive** Laplacian, one may try to solve

\[
s(1-s)=2.
\]

That gives

\[
\boxed{
s=\frac12\pm\frac{i\sqrt7}{2},
}
\]

which lies exactly on `Re(s)=1/2` and therefore looks highly suggestive.

But this solves the wrong operator. With the standard nonnegative Laplacian `L_theta=-Delta_theta`, the Weil–Petersson denominator is

\[
L_\theta+2,
\]

not `L_theta-2`. The correct equation is therefore `s(1-s)=-2`, yielding `s=2,-1` as above. Positivity of `mathscr D_theta` independently fixes the same sign: a multiplier `2/(lambda-2)` would have a pole and change sign across `lambda=2`, whereas the Weil–Petersson Green operator is positive with multiplier `2/(lambda+2)`.

Thus a direct appearance of the line `1/2` from the curvature constant `2` is not a mechanism; it is a convention error.

## 4. Consequence for the nonlinear curvature mechanism of PC-042

PC-042 showed that normalized curvature coefficients on the full-root cover satisfy

\[
R^{(N)}_{\alpha\bar\beta\gamma\bar\delta}
=
\frac1N\mathcal R(\alpha,\beta,\gamma,\delta),
\]

where the universal kernel is built from matrix elements of `mathscr D_theta` with difference holonomies such as

\[
\theta=\gamma-\alpha.
\]

The present identification means that every one of those nonlinear couplings uses the same bounded family

\[
\boxed{
\theta\longmapsto2(L_\theta+2)^{-1},
}
\]

at one fixed negative energy. Varying the prime-circle level changes the rational holonomy samples and the normalized prefactor, but it does **not** move the Laplace spectral parameter toward the continuous spectrum or toward the critical-line energies.

For the mixed bisectional component, PC-042 already gives strict negativity in the usual curvature sign convention. The underlying terms are positive matrix elements of these positive contractions. Hence the most canonical scalar curvature observable has a fixed sign rather than a zero set that could directly encode the nontrivial zeros of `zeta`.

There is also a Selberg-zeta control. For unitary twists, `s=2` lies in the standard absolute-convergence half-plane of the twisted Selberg Euler product. Every primitive-geodesic Euler factor is then nonzero, so the value of `R_theta(2)` selected by the Weil–Petersson tensor is not directly sampling a Selberg-zeta zero or resonance. Meromorphic continuation elsewhere may of course contain nontrivial spectral information, but the curvature formula does not move its argument there.

Therefore the direct chain

\[
\boxed{
\text{prime-circle WP curvature}
\longrightarrow
\text{twisted resolvent}
\longrightarrow
\text{critical-line poles/zeros}
}
\]

is blocked at the second arrow.

## 5. Why this is stronger than merely saying that the parameter is fixed

PC-042 already warned that Weil–Petersson curvature evaluates the universal twisted family at one fixed parameter and supplies no free complex `s`. The new obstruction is stronger in three ways.

First, the fixed value is now located exactly: it is a **uniformly regular negative-energy point** of every unitary twisted Laplacian, not merely an unspecified member of the spectral family.

Second, the location is separated by positivity from the critical-line energy range. Reaching `1/4+t^2` from `-2` requires changing the spectral parameter in the resolvent itself; no re-labeling of the existing operator can do it.

Third, the calculation identifies and kills a concrete false bridge that would otherwise be easy to mistake for a `1/2` mechanism: solving `s(1-s)=2` instead of the correct `s(1-s)=-2`.

So the nonlinear escape discovered in PC-042 remains mathematically real, but **its native spectral evaluation is smoothing rather than resonant**.

## 6. Prior art and novelty audit

All analytic ingredients are classical.

- Scott A. Wolpert, *Chern forms and the Riemann tensor for the moduli space of curves*, Invent. Math. 85 (1986), 119–145, is the primary curvature/Green-operator source already anchored for PC-042.
- Lin Weng, *Omega-admissible theory. II. Deligne pairings over moduli spaces of punctured Riemann surfaces*, Math. Ann. 320 (2001), 239–283, states the corresponding Weil–Petersson curvature-resolvent formula for punctured Teichmüller space.
- Standard automorphic spectral theory, as in Iwaniec's *Spectral Methods of Automorphic Forms*, uses the nonnegative Laplacian spectral parameter `s(1-s)` and the same `s <-> 1-s` two-to-one parameterization.
- The standard twisted Selberg Euler product used in PC-023 is absolutely convergent in a right half-plane containing `s=2` for the unitary twists considered here.

No novelty is claimed for any of these facts. The durable research-specific contribution is the exact obstruction obtained by combining them with PC-042:

\[
\boxed{
\text{the WP curvature coupling samples }s=2/-1,
\text{ not the Riemann critical line.}
}
\]

A directed novelty audit therefore redirects rather than upgrades the mechanism: the interesting object remains the **holonomy dependence** and nonlinear mode coupling, not the fixed spectral value at which the classical Green operator is evaluated.

## 7. Boundary of the no-go

This result does **not** say that `mathscr D_theta` contains no spectral information. A resolvent at a regular point is a smoothed functional of the complete twisted spectrum, and its dependence on `theta` can still be nontrivial.

It also does not rule out:

- derivatives with respect to the unitary holonomy `theta`;
- variation of the puncture configuration away from the symmetric roots-of-unity point;
- covariant derivatives of Weil–Petersson curvature or higher Liouville response;
- nonlinear contractions involving several curvature tensors or several levels;
- the primitive-only composite birth-surface uniformization defect of PC-017;
- an independently derived operation that genuinely introduces a variable spectral parameter rather than inserting a Mellin/Dirichlet transform by hand.

What is ruled out is narrower and decisive: **the fixed Tromba–Wolpert resolvent already present in PC-042 cannot itself be reinterpreted as a critical-line spectral operator or a direct zeta-zero detector.** Any route that moves from `-2` to critical-line energy has added a new ingredient whose origin must be justified independently from the prime-circle geometry.

## 8. Exact audit and falsification tests

The obstruction can be checked without numerical fitting:

1. verify the sign convention in PC-042, `Delta_theta <= 0`, and set `L_theta=-Delta_theta >= 0`;
2. substitute to obtain `mathscr D_theta=2(L_theta+2)^{-1}`;
3. apply the spectral theorem to recover the multiplier `2/(lambda+2)` and the bound `0 <= mathscr D_theta <= I`;
4. solve `s(1-s)=-2` and recover exactly `s=2,-1`;
5. compare with `s=1/2+it`, for which `s(1-s)=1/4+t^2`;
6. deliberately solve the incorrect equation `s(1-s)=2` to expose the spurious critical-line pair and trace it to the Laplacian-sign error;
7. check that the unitary twisted Selberg Euler product is absolutely convergent and nonzero at `s=2`.

A failure of the sign convention or of the identity `mathscr D_theta=2(L_theta+2)^{-1}` would invalidate the claim. No statement is made about analytic continuation of the twisted resolvent away from this fixed point, about zeros of a newly introduced spectral family, or about the unresolved composite uniformization branch.
