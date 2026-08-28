# PF-096 — the first non-universal scattering correction measures discrete cuff curvature

**Status:** `POSITIVE / DERIVED TWO-TERM PHYSICAL-SCATTERING ASYMPTOTIC IN THE GRADED BURGER WINDOW + CONDITIONAL PRIME-REALIZATION GATE`. No RH claim, no global scattering matrix for the infinite flute, and no novelty claim for the finite-dimensional graph expansion by itself.

PF-079 proved that physical cusp scattering of a strongly hierarchical finite prime tangent has a universal tropical profile at each neck scale. PF-090/PF-091 then showed that the first correction to an individual small Laplace eigenvalue remembers the immediately preceding neck through `w_j^2/w_{j-1}` whenever Burger's quantitative error is small enough to resolve it.

These two facts fit together more tightly than previously recorded. In the same graded Burger window, the **full first correction of one physical scattering channel** exists, is an explicit universal rational function of the rescaled spectral parameter, and has coefficient

\[
\boxed{
 r_j:=\frac{w_j}{w_{j-1}}
 \sim
 \frac{d_j}{\sqrt{d_{j-1}d_{j+1}}}
 \sim
 \exp\!\left(\frac{\ell_{j-1}-2\ell_j+\ell_{j+1}}4\right).
}
\]

Thus, after the universal PF-079 leading profile is subtracted, physical scattering detects a **discrete second difference of the distinguished cuff profile**, equivalently a three-gap geometric-mean defect. This is stronger than reading the same information only from the displacement of a pole: the whole one-channel meromorphic profile has a controlled first correction.

## 1. Hierarchical necks and the scale to be resolved

Let a finite prime tangent have `N` limiting pants components and weighted-path necks

\[
G=\sum_{i=1}^{N-1}w_i(e_i-e_{i+1})(e_i-e_{i+1})^*,
\qquad
w_1\gg w_2\gg\cdots\gg w_{N-1}>0.
\]

For `i>=2`, put

\[
r_i=\frac{w_i}{w_{i-1}}.
\]

Fix a scale `j>=2`. We assume the graded hierarchy used in PF-091, in the local form needed here:

\[
\boxed{
r_j\to0,\qquad r_{j+1}=o(r_j),\qquad r_{j-1}\to0,}
\tag{1}
\]

(with the obvious omission of the `r_{j+1}` condition at the last edge), together with the Burger-resolution condition

\[
\boxed{
\sqrt{w_1}=o(r_j).
}
\tag{2}
\]

The first condition says that at the `w_j` scale the immediately preceding edge is very strong, all earlier finite-contraction corrections are smaller than `r_j`, and the next weak edge is also smaller than `r_j`. The second condition ensures that the quantitative surface-to-graph error is below the correction we want to resolve.

PF-091 used precisely this scale separation to resolve the eigenvalue correction

\[
\frac{w_j^2}{w_{j-1}}=w_jr_j.
\]

## 2. Exact finite-dimensional correction before taking the surface limit

At scale `w_j`, divide the graph by `w_j`. For the leading PF-079 limit, all edges `i<j` are contracted and all edges `i>j` deleted. To resolve the first correction, retain the immediately preceding edge `j-1` with weight `1/r_j`, while still contracting `i<j-1` and deleting `i>j`.

Let

\[
k=j-1,
\qquad
u=\frac1{\sqrt{k}}\sum_{i=1}^{k}e_i.
\]

On the three-dimensional space spanned by

\[
\{\nu,e_j,e_{j+1}\},
\]

the two retained edge vectors are

\[
v=\left(-\frac1{\sqrt{k}},1,0\right),
\qquad
q=(0,1,-1),
\]

and the reduced operator is

\[
A_{j,r}=\frac1r vv^*+qq^*,
\qquad r=r_j.
\]

The endpoint vector `e_1` projects to `nu/sqrt(k)`. Hence its reduced Weyl function is

\[
 m_{j,r}(z)
 =\frac1k\left\langle
 \nu,(A_{j,r}-zI)^{-1}\nu
 \right\rangle.
\]

A direct `3 x 3` inversion gives the exact rational function

\[
\boxed{
 m_{j,r}(z)
 =-
 \frac{r z^2-2rz-z+1}
 {z\big((j-1)rz^2-2(j-1)rz-jz+j+1\big)}.
}
\tag{3}
\]

Expanding at `r=0`, locally uniformly away from `z=0` and `z=(j+1)/j`, gives

\[
\boxed{
 m_{j,r}(z)
 =m_j^{(0)}(z)+r\,m_j^{(1)}(z)+O(r^2),
}
\tag{4}
\]

where

\[
\boxed{
 m_j^{(0)}(z)
 =\frac{1-z}{jz\left(z-\frac{j+1}{j}\right)}
}
\tag{5}
\]

is exactly the universal PF-079 tropical profile, and

\[
\boxed{
 m_j^{(1)}(z)
 =\frac{(z-2)^2}{\big(jz-(j+1)\big)^2}.
}
\tag{6}
\]

The simplicity of (6) is useful: all dependence on the prime-derived geometry has collapsed to the single coefficient `r_j`; the spectral shape of the first correction is universal.

### Pole-shift consistency check

The nonzero finite pole of (3) satisfies

\[
(j-1)rz(z-2)-jz+j+1=0.
\]

Therefore

\[
\boxed{
 z_j(r)
 =\frac{j+1}{j}
 -\frac{(j+1)(j-1)^2}{j^3}r
 +O(r^2).
}
\tag{7}
\]

Multiplying by `w_j/(2 pi^2)` recovers exactly the PF-091 eigenvalue correction

\[
-\frac{(j+1)(j-1)^2}{2\pi^2j^3}
\frac{w_j^2}{w_{j-1}}.
\]

Thus the new scattering formula is consistent with the independently derived Laplace-pole displacement.

## 3. Promotion to the physical hyperbolic scattering matrix

Let `Phi_nu^mark(s)` be the persistent-cusp physical scattering block of the actual finite hyperbolic tangent, as in PF-078/PF-079, and choose the persistent cusp in the first pants component. Define

\[
\boxed{
\mathcal S_{j,\nu}(z)
:=
\frac{w_j^{(\nu)}}{\pi}
\Phi_{11,\nu}^{\rm mark}
\!\left(
1-\frac{w_j^{(\nu)}z}{2\pi^2}
\right).
}
\tag{8}
\]

PF-078 gives a low/high Feshbach decomposition: every singularity on the `1/w_j` scale comes from the finite-dimensional small-mode sector, while the pole-subtracted physical scattering remainder is uniformly `O(1)`. PF-079 used this to obtain only the leading contracted-graph limit.

To retain one more order, the quantitative estimates already present in Burger's proof are sufficient under (2):

1. **Eigenvalue locations.** Burger's Theorem 1.1 gives relative error `O(sqrt(w_1))` for every small graph eigenvalue. At the `w_j` scale this produces an `O(sqrt(w_1))=o(r_j)` error in the rescaled weak pole location. For stronger modes the resulting scattering contribution is already `O(r_j)`, so their relative `O(sqrt(w_1))` error contributes only `o(r_j)`.

2. **Low-mode projectors / cusp amplitudes.** Burger's Lemma 5 controls the component-average map on the full low eigenspace. Since the largest collapsing eigenvalue is `O(w_1)` while the next spectral band stays uniformly separated from zero, a normalized low eigenfunction differs in `L^2` from its componentwise-constant part by `O(sqrt(w_1))`. The finite-dimensional quadratic-form comparison then gives the same order for the low spectral projectors after identifying component averages with graph coordinates. On a fixed persistent cusp annulus, the eigenfunction minus its component average solves an elliptic equation with `O(w_1)` forcing; standard interior elliptic estimates therefore transfer the `O(sqrt(w_1))` control to the outgoing zero-mode amplitudes. Via the Maaß--Selberg residue identity used in PF-078,

   \[
   2\pi R_{q,\nu}
   =P_{q,G_\nu}+O(\sqrt{w_1})
   \]

   on the marked cusp block, after grouping any modes below the current scale. Under (2), this is `o(r_j)`.

3. **Holomorphic physical remainder.** PF-078 gives `H_nu(s)=O(1)`. Multiplication by `w_j` makes this `O(w_j)=o(r_j)` because `w_j/r_j=w_{j-1}->0`.

4. **The nonlinear map `s -> s(1-s)`.** At `s=1-w_j z/(2 pi^2)` its quadratic correction is `O(w_j^2)`, hence `O(w_j)=o(r_j)` after rescaling by `w_j`.

5. **Other graph scales.** Earlier finite contractions contribute first at

   \[
   \frac{w_j}{w_{j-2}}=r_jr_{j-1}=o(r_j),
   \]

   while the next weak edge contributes `r_{j+1}=o(r_j)` by (1).

Combining these estimates with the exact reduced resolvent (3) yields, for every compact

\[
K\Subset\mathbb C\setminus\left\{0,\frac{j+1}{j}\right\},
\]

\[
\boxed{
\mathcal S_{j,\nu}(z)
=
\frac{1-z}{jz\left(z-\frac{j+1}{j}\right)}
+
\frac{w_j}{w_{j-1}}
\frac{(z-2)^2}{\big(jz-(j+1)\big)^2}
+
o\!\left(\frac{w_j}{w_{j-1}}\right)
}
\tag{9}
\]

uniformly for `z in K`.

Equation (9) is the first **non-universal** term of the physical scattering tropicalization.

## 4. Exact prime-gap geometry turns the coefficient into a three-gap invariant

For the exact orthogonal-circle prime tangent, PF-047/PF-054 give

\[
 w_j
 =4\operatorname{arsinh}
 \sqrt{\frac{d_1+\cdots+d_j}{d_{j+1}}}
\]

with the corresponding index shift from the nested separators. In the strongly hierarchical regime this simplifies to

\[
\boxed{
 w_j\sim4\sqrt{\frac{d_j}{d_{j+1}}}.
}
\tag{10}
\]

Therefore

\[
\boxed{
 r_j=\frac{w_j}{w_{j-1}}
 \sim
 \frac{d_j}{\sqrt{d_{j-1}d_{j+1}}}.
}
\tag{11}
\]

This is not a one-gap statistic. It compares the middle gap with the geometric mean of its two neighbours.

For the original distinguished prime-flute cuffs,

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1),
\]

so the common divergent scale cancels twice and

\[
\boxed{
 r_j
 \sim
 \exp\!\left[
 \frac{\ell_{j-1}-2\ell_j+\ell_{j+1}}4
 \right].
}
\tag{12}
\]

Thus the coefficient of the first scattering correction is the exponential of a **discrete second difference of the distinguished cuff lengths**.

Combining (9) and (12), for every generic fixed `z` with

\[
z\notin\left\{0,2,\frac{j+1}{j}\right\},
\]

the physical scattering channel asymptotically recovers

\[
\boxed{
\ell_{j-1}-2\ell_j+\ell_{j+1}
=
4\log\left|
\frac{\mathcal S_j(z)-m_j^{(0)}(z)}{m_j^{(1)}(z)}
\right|
+o(1),
}
\tag{13}
\]

where the equality is understood along the graded pinching family and with the sign/phase fixed by the positive real ratio `r_j`. Equivalently, the same residual recovers `d_j/sqrt(d_{j-1}d_{j+1})`.

This is the first place in the physical-scattering analysis where a **second discrete derivative of the prime-derived cuff profile** appears directly as an amplitude coefficient rather than only indirectly through an individual pole.

## 5. Relation to earlier positives and negatives

The formula sharpens several earlier conclusions without contradicting them:

- **PF-079:** after factoring the correct neck scale, the leading scattering profile is universal. Equation (9) identifies the first term that survives after subtracting that universal control.
- **PF-090/PF-091:** the upstream-memory term in a small eigenvalue is exactly the pole displacement contained in (9). Scattering retains more resolved information: the same coefficient controls both pole movement and residue/profile deformation.
- **PF-089:** a scalar determinant cancels the `w_j^2/w_{j-1}` redistribution. Equation (9) shows why one should keep a marked matrix element / Weyl function instead of taking a determinant.
- **PF-049/PF-078:** the endpoint Weyl function is the correct inverse object. Here its first multiscale correction already has a closed universal shape.
- **PF-092:** none of this creates an absolute global scattering theory near `s=1` for the infinite flute. The statement is for finite tangents and, through PF-050/PF-094, for localized spectral limits inside the single infinite surface.

## 6. Interior/exterior duality

All necks `w_i` are functions of exact ordered cross-ratios from the orthogonal-circle construction. Ambient inversion exchanging the prime-circle interior and exterior pictures preserves these cross-ratios and therefore preserves `r_j`, the discrete cuff curvature in (12), and the scattering law (9).

As in PF-017, this does not produce two independent intrinsic scattering matrices; it proves that the coefficient is independent of which ambient side is used to represent the same hyperbolic geometry.

## 7. Prior-art / novelty audit

Known ingredients, with no novelty claim:

1. **Burger (1990)** gives the quantitative weighted-graph comparison for small eigenvalues of degenerating finite-type hyperbolic surfaces. Theorem 1.1 has relative `O(sqrt(epsilon))` control, and Lemma 5 quantitatively controls the component-average map on the low eigenspace. This is the analytic error budget used above.
2. **Schulze (2006)** proves resolvent convergence for degenerating finite-geometry hyperbolic surfaces and constructs approximate Eisenstein functions/scattering matrices. His result is a convergence theorem, not the singular multiscale two-term physical-scattering profile (9).
3. **Obitsu (2001)** studies asymptotics of Eisenstein series under hyperbolic degeneration using collar and elliptic estimates, but does not identify a weighted-path resolvent correction of the form (6).
4. **Levitin--Strohmaier (2021)** express the cusp scattering matrix through the compact-core Neumann-to-Dirichlet map; this supplies a standard physical-scattering framework but no hierarchical graph asymptotic.
5. Strong-edge contraction and Schur-complement expansions of finite weighted graphs are elementary finite-dimensional operator theory. Formulae (3)--(6) should not be advertised as new graph theory in isolation.

Directed searches for combinations of `degenerating hyperbolic surface + physical cusp scattering + weighted graph resolvent`, `multiscale pinching + scattering matrix + graph contraction`, `Eisenstein + weighted graph + degeneration`, and `second-order scattering + pinching geodesic` found the adjacent theories above but not the two-term limit (9), the rational correction (6), or its identification with the discrete cuff curvature (12).

The potentially new content is therefore narrow and compositional but mathematically concrete:

\[
\boxed{
\text{exact prime-derived multiscale necks}
\to
\text{physical cusp scattering}
\to
\text{universal leading tropical profile}
\to
\text{first residual coefficient}
=
\exp\!\left(\frac{\Delta^2\ell_j}{4}\right).
}
\]

No historical-priority claim is made.

## 8. Falsification / audit points

The argument should be rejected if any of the following fails under an independent proof audit:

1. Burger's Lemma 5 plus the low-space form comparison does not yield `O(sqrt(w_1))` control of the relevant grouped graph projectors after the component-average identification.
2. Local elliptic regularity on a fixed persistent cusp annulus fails to transfer that rate to the residual zero-mode amplitudes used in the Maaß--Selberg residue matrix.
3. PF-078's pole-subtracted physical scattering remainder is not uniform under the graded multiscale family.
4. A supposedly smaller graph scale contributes at order `r_j`; conditions (1) are chosen precisely to exclude this.

The finite-dimensional formula (3) and its expansion (4)--(7) are exact and provide an easy independent algebraic check.

## 9. Arithmetic gate

As in PF-090/PF-091, the hyperbolic theorem is strongest in a **moderate graded hierarchy** where the desired graph correction dominates Burger's `O(sqrt(w_1))` surface error. The current PF-046/PF-054 prime-pattern machinery guarantees arbitrarily strong recurrent hierarchies but does not yet guarantee the upper control represented by (2) for a prescribed fixed `j`.

Therefore (9)--(13) should not yet be stated as an unconditional infinitely recurrent prime theorem. The arithmetic gate is now especially transparent: realize recurrent isolated consecutive-prime blocks for which

\[
\boxed{
\sqrt{w_1}\ll\frac{w_j}{w_{j-1}}\ll1,
\qquad
\frac{w_{j+1}}{w_j}=o\!\left(\frac{w_j}{w_{j-1}}\right).
}
\]

If that gate is closed, the single prime-flute contains infinitely many isolated regions whose **physical scattering residuals directly measure discrete second differences of its distinguished cuff profile**.

## References

- Marc Burger, *Small eigenvalues of Riemann surfaces and graphs*, Math. Z. 205 (1990), 395--420. DOI `10.1007/BF02571251`.
- Michael Schulze, *On the resolvent of the Laplacian on functions for degenerating surfaces of finite geometry*, J. Funct. Anal. 236 (2006), 120--160. DOI `10.1016/j.jfa.2006.01.005`; arXiv `math/0410434`.
- Kunio Obitsu, *The Asymptotic Behavior of Eisenstein Series and a Comparison of the Weil--Petersson and the Zograf--Takhtajan Metrics*, Publ. RIMS 37 (2001), 459--478. DOI `10.2977/prims/1145477232`.
- Michael Levitin and Alexander Strohmaier, *Computations of eigenvalues and resonances on perturbed hyperbolic surfaces with cusps*, IMRN 2021, 4003--4050. DOI `10.1093/imrn/rnz157`.
