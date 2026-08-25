# PC-017 — the birth-shell sphere carries a canonical cyclotomic uniformization defect

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE`; no RH claim.

This finding upgrades PC-016 from a scalar metric defect to a canonical second-order Fuchsian differential operator. It also repairs the gauge obstruction of PC-013 in a genuinely two-dimensional way: the operator is fixed by complete hyperbolic uniformization, not by an arbitrary lift of the prime vertices.

## 1. Fuchsian projective connection of the base sphere

Let

\[
B=\widehat{\mathbb C}\setminus\{0,1,\infty\}.
\]

Write \(Q_B(w)=\{\rho_B,w\}\) for the Schwarzian derivative of a local inverse of the universal covering map, using

\[
\{f,z\}=\frac{f'''}{f'}-\frac32\left(\frac{f''}{f'}\right)^2.
\]

For the thrice-punctured sphere there are no free accessory parameters, and

\[
\boxed{
Q_B(w)=\frac{w^2-w+1}{2w^2(w-1)^2}.
}
\]

This is the standard parabolic Fuchsian projective connection with coefficient \(1/2\) at each cusp.

## 2. The full-root surface has an explicit uniformizing connection

Let

\[
Y_n=\widehat{\mathbb C}\setminus
\bigl(\{0,\infty\}\cup\mu_n\bigr),
\qquad
F_n(z)=z^n.
\]

As in PC-016, \(F_n:Y_n\to B\) is an unbranched degree-\(n\) cyclic cover. Therefore its Fuchsian projective connection is the projective pullback

\[
Q_n^{\rm full}(z)
=(F_n'(z))^2Q_B(F_n(z))+\{F_n,z\}.
\]

Since

\[
\{z^n,z\}=-\frac{n^2-1}{2z^2},
\]

a direct simplification gives the exact closed formula

\[
\boxed{
Q_n^{\rm full}(z)=
\frac{z^{2n}+(n^2-2)z^n+1}
{2z^2(z^n-1)^2}.
}
\]

Equivalently,

\[
Q_n^{\rm full}(z)
=
\frac1{2z^2}
+
\frac{n^2z^{n-2}}{2(z^n-1)^2}.
\]

At every \(\alpha\in\mu_n\),

\[
Q_n^{\rm full}(z)
=
\frac1{2(z-\alpha)^2}
-\frac1{2\alpha(z-\alpha)}+O(1).
\]

Thus even the accessory coefficient of the complete cyclic cover is explicit and independent of \(n\) after the root \(\alpha\) is fixed.

The associated canonical uniformizing ODE is

\[
\boxed{
\psi''+rac12Q_n^{\rm full}(z)\psi=0.
}
\]

It is the pullback of the hypergeometric uniformization equation of the thrice-punctured sphere.

## 3. Birth-shell uniformization and the prime equality

Define the anchored birth surface

\[
X_n^{\rm birth}
=
\widehat{\mathbb C}\setminus
\bigl(\{0,1,\infty\}\cup\mu_n^*\bigr)
\]

and let \(Q_n^{\rm birth}\) be its canonical Fuchsian projective connection.

PC-016 proved

\[
n\text{ prime}\iff X_n^{\rm birth}=Y_n.
\]

Therefore

\[
\boxed{
n\text{ prime}
\iff
Q_n^{\rm birth}=Q_n^{\rm full}.
}
\]

In particular, for a prime \(p\), the geometry of the vertices born at level \(p\) has the completely explicit canonical connection

\[
\boxed{
Q_p^{\rm birth}(z)
=
\frac{z^{2p}+(p^2-2)z^p+1}
{2z^2(z^p-1)^2}.
}
\]

No spectral parameter, closure, lift normalization, or discrete Schrödinger potential has been introduced by hand.

## 4. Composite levels generate a canonical projective defect

For every \(n>1\), restrict both projective connections to the common domain \(Y_n\subseteq X_n^{\rm birth}\) and define

\[
\boxed{
\mathcal A_n(z)\,dz^2
:=
\bigl(Q_n^{\rm birth}(z)-Q_n^{\rm full}(z)\bigr)dz^2.
}
\]

The difference of two projective connections on the same Riemann surface is a quadratic differential, so \(\mathcal A_n dz^2\) is intrinsic once the common global coordinate inherited from the original circle is fixed.

Its decisive feature is local. The inherited roots are

\[
H_n
:=
\mu_n\setminus(\{1\}\cup\mu_n^*)
=
\bigsqcup_{\substack{d\mid n\\1<d<n}}\mu_d^*.
\]

At \(\alpha\in H_n\), the point \(\alpha\) is a cusp of \(Y_n\) but an ordinary interior point of \(X_n^{\rm birth}\). Hence \(Q_n^{\rm birth}\) is regular there while the explicit full connection has a parabolic pole. Consequently

\[
\boxed{
\mathcal A_n(z)
=
-\frac1{2(z-\alpha)^2}
+\frac1{2\alpha(z-\alpha)}
+O(1)
\qquad(\alpha\in H_n).
}
\]

At the punctures common to both surfaces the universal double-pole coefficient \(1/2\) cancels; the remaining simple-pole terms are differences of genuine accessory parameters.

Therefore

\[
\boxed{
\mathcal A_n\equiv0\iff n\text{ is prime}.
}
\]

For composite \(n\), \(\mathcal A_n\) is not merely a divisor indicator: after its forced principal parts are removed, its remaining accessory data are determined by the global PSL(2,R) monodromy/uniformization problem of the primitive-root puncture configuration.

## 5. Relation to the nonlinear metric defect of PC-016

Write the two complete Poincare metrics on the common domain as

\[
ds_X^2=e^{\phi_X}|dz|^2,
\qquad
ds_Y^2=e^{\phi_Y}|dz|^2,
\]

and

\[
\mathcal D_n=\frac12(\phi_Y-\phi_X)
=\log\frac{\rho_{Y_n}}{\rho_{X_n}}.
\]

PC-016 gave the nonlinear Liouville defect equation

\[
\Delta\mathcal D_n
=\rho_{X_n}^2(e^{2\mathcal D_n}-1)
\]

away from punctures.

With the standard Liouville stress-tensor convention

\[
T(\phi)=\phi_{zz}-\frac12\phi_z^2,
\]

the Fuchsian projective connection is \(T(\phi)\). Thus the projective defect is the holomorphic/meromorphic stress tensor of the same scalar field:

\[
\boxed{
Q_n^{\rm full}-Q_n^{\rm birth}
=
2(\mathcal D_n)_{zz}
-2(\phi_X)_z(\mathcal D_n)_z
-2(\mathcal D_n)_z^2.
}
\]

So PC-016 and PC-017 are two faces of a single canonical object:

\[
\text{nonlinear hyperbolic covering defect}
\longleftrightarrow
\text{meromorphic Fuchsian projective/accessory defect}.
\]

This is important methodologically. Unlike the projective prime-path construction of PC-013, the projective connection here is fixed by the two-dimensional Poincare metric and therefore has no arbitrary alternating lift gauge.

## 6. Multiplication by a prime: exact cover versus uniformization surgery

For the primitive-shell surfaces

\[
S_n=\widehat{\mathbb C}\setminus(\{0,\infty\}\cup\mu_n^*),
\]

PC-016 proved

\[
p\mid n
\iff
z^p:S_{np}\to S_n
\text{ is a regular degree-}p\text{ cover}.
\]

Let \(Q_{S_n}\) denote the Fuchsian projective connection. In the cover case the Schwarzian chain rule gives the exact renormalization law

\[
\boxed{
Q_{S_{np}}(z)
=
p^2z^{2p-2}Q_{S_n}(z^p)
-\frac{p^2-1}{2z^2}
\qquad(p\mid n).
}
\]

When \(p\nmid n\), the same pullback uniformizes the surface in which both the old shell \(\mu_n^*\) and the new shell \(\mu_{np}^*\) are punctured. Passing to \(S_{np}\) fills the old-shell cusps, and the failure of the displayed identity is again a canonical accessory-parameter / projective-connection defect.

Thus multiplication has an exact geometric dichotomy:

\[
\boxed{
\text{old prime factor}
\to
\text{projectively exact covering renormalization},
}
\]

\[
\boxed{
\text{new prime factor}
\to
\text{cover + nonlinear uniformization surgery}.
}
\]

## 7. Serious novelty check

Known ingredients:

- Fuchsian projective connections and accessory parameters are classical.
- The Schwarzian chain rule and projective pullback under coverings are classical.
- The thrice-punctured sphere is explicitly uniformized by the hypergeometric/modular-lambda equation.
- Takhtajan-Zograf theory identifies accessory parameters as derivatives of the classical Liouville action and relates that action to Weil-Petersson geometry.
- Full root-of-unity punctured spheres and power-map constructions are known; they appear, for example, in modern work of Bishop-Rempe and in the much older cyclotomic/motivic geometry of P^1 minus roots of unity.

Directed searches for combinations of

- primitive roots of unity + Fuchsian projective connection,
- cyclotomic polynomial + accessory parameters,
- primitive-root punctured sphere + uniformization,
- cyclotomic punctures + Schwarzian uniformization

found no treatment of the specific comparison \(Q_n^{\rm birth}-Q_n^{\rm full}\) or of the cover-versus-filling renormalization law above.

This is not evidence of historical priority. The exact pullback side is elementary once the surfaces are defined, while the composite-side accessory parameters are a difficult classical uniformization problem. The candidate novelty is the **arithmetic organization of those canonical nonlinear uniformization defects by birth shells**.

## 8. Research gate

This is not yet an RH mechanism. In particular,

- using only \(\mathcal A_n\equiv0\) as a primality detector is trivial;
- summing an arbitrarily chosen norm of \(\mathcal A_n\) into a Dirichlet series would be an artificial generating function;
- the forced double-pole support alone only restates the proper-divisor decomposition of \(\mu_n\).

A substantive continuation must use the global accessory/monodromy part that remains after the forced poles are accounted for. Promising tests are:

1. whether the accessory defect has a canonical composition law under successive new-prime surgeries that contains more than the endpoint divisor lattice;
2. whether its Liouville/Weil-Petersson energy has a nontrivial scale law not reducible to \(\varphi\) or known cyclotomic resultants;
3. whether a renormalized limit over birth levels produces a forced operator/dynamics before any Mellin transform is introduced;
4. whether the exact equatorial-reflection / inversion symmetry from PC-015 constrains the monodromy strongly enough to give a positivity principle.
