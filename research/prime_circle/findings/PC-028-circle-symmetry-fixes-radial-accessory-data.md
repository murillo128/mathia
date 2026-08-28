# PC-028 — circle symmetry fixes radial accessory data and kills the common-anchor defect

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for any RH/primality mechanism that reads only the simple-pole accessory coefficient of the common vertex, and more generally for the radial component of shared unit-circle accessory data.

PC-017 left the global accessory-parameter part of the cyclotomic uniformization defect as one of the main nonlinear directions not covered by the linear/Möbius/Ramanujan no-go results. The first scalar one might try to extract from that global object is the accessory shift at the distinguished common vertex `1`. The original circle symmetry forces that shift to vanish identically for every level.

## 1. The birth surface has exact inversion and conjugation symmetry

For `n>1`, recall

\[
X_n^{\rm birth}
=\widehat{\mathbb C}\setminus
\bigl(\{0,1,\infty\}\cup\mu_n^*\bigr),
\]

and let `Q_n^{birth}` be its canonical Fuchsian projective connection in the global coordinate inherited from the prime circle.

The puncture set is invariant under

\[
J(z)=\frac1z
\qquad\text{and}\qquad
C(z)=\bar z.
\]

The first map is a holomorphic Möbius automorphism of the punctured sphere. Naturality of the uniformizing projective connection and the Schwarzian chain rule therefore give

\[
Q_n^{\rm birth}(z)
=(J'(z))^2 Q_n^{\rm birth}(J(z))+\{J,z\}.
\]

Since `J` is Möbius, `\{J,z\}=0`, hence

\[
\boxed{
Q_n^{\rm birth}(z)=z^{-4}Q_n^{\rm birth}(1/z).
}
\]

The real structure gives the companion relation

\[
\boxed{
Q_n^{\rm birth}(z)
=\overline{Q_n^{\rm birth}(\bar z)}.
}
\]

These are forced by the original unit-circle geometry; no spectral parameter or chosen gauge is involved.

## 2. Inversion fixes one real component of every unit-circle accessory coefficient

Let `alpha` be any puncture of `X_n^{birth}` on the unit circle, so

\[
\alpha\in\{1\}\cup\mu_n^*,
\qquad |\alpha|=1.
\]

Write the standard parabolic Laurent expansion

\[
Q_n^{\rm birth}(z)
=
\frac{1}{2(z-\alpha)^2}
+
\frac{c_n(\alpha)}{z-\alpha}
+O(1).
\]

Set `beta=alpha^{-1}`. Expanding the inversion identity around `z=alpha` yields exactly

\[
\boxed{
c_n(\alpha)
=-\frac1\alpha
-\frac{c_n(\beta)}{\alpha^2}.
}
\]

On the unit circle `beta=bar(alpha)`, while conjugation symmetry gives

\[
c_n(\bar\alpha)=\overline{c_n(\alpha)}.
\]

Multiplying the previous relation by `alpha^2` and then dividing by `alpha` gives

\[
\alpha c_n(\alpha)
+
\overline{\alpha c_n(\alpha)}
=-1.
\]

Therefore

\[
\boxed{
\operatorname{Re}\bigl(\alpha c_n(\alpha)\bigr)=-\frac12.
}
\]

Equivalently, there is a real number `tau_n(alpha)` such that

\[
\boxed{
\alpha c_n(\alpha)
=-\frac12+i\tau_n(\alpha),
\qquad
\tau_n(\bar\alpha)=-\tau_n(\alpha).
}
\]

Thus the radial component of the accessory coefficient is universal. Any nontrivial unit-circle accessory information can only survive in the tangential component `tau_n(alpha)` paired antisymmetrically across conjugate punctures.

## 3. The full-root model has exactly the same radial component

PC-017 derived the explicit complete-cover connection

\[
Q_n^{\rm full}(z)
=
\frac{z^{2n}+(n^2-2)z^n+1}
{2z^2(z^n-1)^2}.
\]

At every `alpha in mu_n`, its simple-pole coefficient is

\[
\boxed{
c_n^{\rm full}(\alpha)=-\frac{1}{2\alpha}.}
\]

At every puncture shared by the birth and full-root surfaces, define the simple-pole coefficient of the PC-017 defect

\[
\mathcal A_n
=Q_n^{\rm birth}-Q_n^{\rm full}
\]

by

\[
a_n(\alpha)
:=c_n(\alpha)-c_n^{\rm full}(\alpha)
=c_n(\alpha)+\frac1{2\alpha}.
\]

The symmetry constraint becomes

\[
\boxed{
\operatorname{Re}\bigl(\alpha a_n(\alpha)\bigr)=0.
}
\]

So even though `Q_n^{birth}` is obtained from a genuinely global nonlinear uniformization problem, the defect cannot alter the radial accessory component at any shared unit-circle cusp.

## 4. At the distinguished common vertex the accessory defect vanishes completely

The common vertex is the fixed point `alpha=1` of inversion. Substituting `alpha=beta=1` directly into the coefficient relation gives

\[
c_n(1)=-1-c_n(1),
\]

hence

\[
\boxed{
c_n(1)=-\frac12}
\]

for every `n>1`.

But the full-root connection has the same value,

\[
c_n^{\rm full}(1)=-\frac12.
\]

Therefore

\[
\boxed{
a_n(1)=0\qquad\text{for every }n>1.}
\]

Since PC-017 already showed that the universal double poles cancel at punctures common to the two surfaces, the new statement is stronger than a vanishing residue:

\[
\boxed{
\mathcal A_n(z)=O(1)\quad\text{as }z\to1.
}
\]

The cyclotomic uniformization defect extends holomorphically across the distinguished common vertex even when `n` is composite and the defect is globally nonzero.

This is an exact obstruction to the tempting route

\[
\text{common anchor}
\to
\text{Fuchsian accessory shift at }1
\to
\text{prime/RH-sensitive scalar}.
\]

The scalar is identically zero.

## 5. Why this matters after PC-019 and PC-020

PC-019 showed that forgetting the anchor is fatal because an unanchored shell identifies odd `n` with `2n`. PC-020 then showed that finite local jets of the cyclotomic potential at the anchor collapse to classical Jordan-totient data. PC-017 seemed to leave a more promising possibility: use a coefficient at the anchor that is local in its Laurent readout but globally determined through hyperbolic uniformization.

The present result closes that particular escape. The global nature of an accessory parameter is not enough: **the exact inversion symmetry of the original circle protects the anchor coefficient and forces its birth/full difference to vanish**.

This does not contradict the fact that the full projective defect is nonlinear and globally determined. It says that the most natural one-point anchored projection of that defect erases precisely the information one hoped to retain.

## 6. Prior art and novelty audit

The ingredients are classical:

- the Schwarzian chain rule and Möbius naturality of projective connections;
- Fuchsian uniformizing projective connections and accessory parameters on punctured spheres;
- real-analytic dependence of accessory parameters on moduli;
- Liouville-action generation of Fuchsian accessory parameters and its Weil-Petersson interpretation.

Useful literature anchors are Irwin Kra, *Accessory Parameters for Punctured Spheres*, Trans. Amer. Math. Soc. **313** (1989), 589–617, and P. Zograf–L. Takhtajan, *On Liouville's equation, accessory parameters, and the geometry of Teichmüller space for Riemann surfaces of genus 0*, Math. USSR-Sb. **60** (1988), 143–161. Takhtajan–Zograf's 2003 treatment of hyperbolic 2-spheres gives the corresponding Liouville/Kähler formulation.

Directed searches for accessory parameters of root-of-unity punctured spheres and inversion-symmetric puncture configurations did not locate the prime-circle-specific statement above. That absence is not a priority claim. The symmetry calculation is elementary once PC-017 has supplied the canonical birth/full comparison, so the mathematical novelty claimed here is only the **research obstruction for this construction**, not a new general theorem about accessory parameters.

## 7. Boundary of the no-go result

This result does **not** show that the PC-017 uniformization defect is trivial.

For a non-real primitive puncture, the tangential quantity

\[
\tau_n(\alpha)
=-i\left(\alpha c_n(\alpha)+\frac12\right)
\]

can still be nonzero, and it is globally constrained by the Fuchsian monodromy problem. Likewise, the regular part of the projective defect, monodromy representations, Liouville action, Weil-Petersson Hessians, and nonlinear interactions among several punctures are not determined by the argument above.

What is ruled out is narrower but important:

\[
\boxed{
\text{shared unit-circle radial accessory data are universal,}
}
\]

and, in particular,

\[
\boxed{
\text{the common-anchor simple-pole accessory defect carries no arithmetic information at all.}
}
\]

Future work on PC-017 should therefore test genuinely collective data—such as the tangential accessory vector modulo its symmetry constraints, monodromy, or second-variation/Liouville-Weil-Petersson quantities—rather than another scalar evaluation at the common vertex.
