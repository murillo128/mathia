# PF-178 — support-controlled Moser removes the qualitative global volume-gauge gluing obstruction

**Status:** `LITERATURE+DERIVED + EXACT-EXISTENCE + BOUNDARY`. PF-176 proves pant-local area-preserving correction with prescribed boundary values but deliberately leaves a smooth-gluing concern: a boundary-fixed Moser correction need not preserve normal derivatives. PF-177 then shows that the dangerous short-collar Jacobian defect can be kept out of collapsing cores, but still does not claim a global `rho=1` marking. The missing qualitative gluing step is classical once the *initial* pant comparison is chosen area preserving on full boundary neighborhoods. A support-controlled pullback/Moser correction can then be chosen **identically equal to the identity near the boundary**, not merely pointwise on it. Explicit area-preserving Fermi germs exist at every matched finite cuff and the normalized deep cusp already has a common exact isometric germ. Choosing the same two-sided cuff germ from both adjacent pants and applying the support-controlled correction only in each pant interior produces a smooth label-preserving global prime/shift marking whose pulled-back hyperbolic area form agrees exactly with the prime area form. Thus qualitative existence of a smooth global `rho=1` gauge is no longer an obstruction. The unresolved PF-175/PF-177 gate is quantitative: this argument supplies no degeneration-uniform quasi-isometry, derivative, inverse-unit-ball weighted metric-defect, Schatten, scattering, or RH conclusion.

## Claim

Let `X` be the exact zero-twist prime flute and `X_+` the exact all-composite shift clone of PF-125, with corresponding one-cusp pants

\[
P_n=P(\ell_n,\ell_{n+1},0),
\qquad
P_n^+=P(\ell_n^+,\ell_{n+1}^+,0).
\tag{1}
\]

Use PF-125's common normalized cusp model and truncate every cusp above one fixed horocycle `y=Y>1`. Write

\[
K_n=P_n\setminus C_Y,
\qquad
K_n^+=P_n^+\setminus C_Y,
\tag{2}
\]

and let `omega_n,omega_n^+` be their hyperbolic area forms.

There are smooth orientation-preserving diffeomorphisms

\[
\widetilde F_n:K_n\longrightarrow K_n^+
\tag{3}
\]

with all of the following properties:

1. `\widetilde F_n^*\omega_n^+=\omega_n` exactly;
2. near each finite cuff, `\widetilde F_n` agrees with an explicit area-preserving Fermi collar germ depending only on the matched source/target cuff lengths;
3. near the truncating horocycle it is the identity in the common normalized cusp coordinates;
4. the cuff germs are two-sided and commute with the zero-twist gluing involution, so the corrected maps from adjacent pants agree on a whole neighborhood of every shared cuff, not only on the cuff itself.

Consequently the `\widetilde F_n` and the exact deep-cusp identities assemble to one smooth marked diffeomorphism

\[
\boxed{
\widetilde F:X\longrightarrow X_+
}
\tag{4}
\]

such that

\[
\boxed{
\widetilde F^*d\mu_{X_+}=d\mu_X.
}
\tag{5}
\]

Equivalently, after transporting the clone metric by `\widetilde F`, the volume ratio in PF-175 is

\[
\boxed{\rho\equiv1.}
\tag{6}
\]

This is an existence statement only. It does **not** assert that `\widetilde F` is globally quasi-isometric, that its tail distortion tends to one, or that the two-sided weighted `delta^r` integral in PF-175 is finite.

## 1. Every matched cuff has an exact area-preserving two-sided germ

Let a source cuff have length `L>0` and its matched target cuff length `L'>0`. In signed Fermi coordinates around the source geodesic, use arclength `s in R/LZ` along the core and signed normal distance `r`. The metric and area form are

\[
g_L=dr^2+\cosh^2r\,ds^2,
\qquad
\omega_L=\cosh r\,dr\wedge ds.
\tag{7}
\]

Use analogous coordinates `(r',s')` for the target cuff. On a sufficiently small two-sided collar define

\[
\boxed{
s'=\frac{L'}L s,
\qquad
r'=\operatorname{arsinh}\!\left(\frac L{L'}\sinh r\right).
}
\tag{8}
\]

The map is smooth across `r=0`. Differentiating the second identity gives

\[
\cosh r'\,\frac{dr'}{dr}
=\frac L{L'}\cosh r,
\tag{9}
\]

while `ds'=(L'/L)ds`. Hence

\[
\boxed{
\cosh r'\,dr'\wedge ds'
=\cosh r\,dr\wedge ds,
}
\tag{10}
\]

so the germ is exactly area preserving.

The canonical zero-twist cuff involution is `s -> -s` modulo the cuff length. Equation (8) commutes with this involution. Therefore one can choose a **single signed germ across each shared cuff** and use its two half-collars as the boundary germs for the two adjacent pants. If subsequent corrections are the identity on those half-collars, smooth gluing across the cuff is automatic to every derivative order.

No short-collar assumption is used here. For existence one may shrink the source collar until (8) lies inside any chosen target collar. This is intentionally weaker than PF-177, whose fixed area-coordinate core is designed for quantitative degeneration control.

## 2. The cusp supplies the third area-preserving boundary germ for free

PF-125 identifies, in every source and target one-cusp pant, the same normalized deep cusp strip with metric

\[
ds^2=\frac{dx^2+dy^2}{y^2}.
\tag{11}
\]

Choose the truncating horocycle inside that common model and use the identity on a whole slab around it. This is an exact isometry and therefore exactly area preserving. Extending by the identity farther into the cusp will later give the complete global map.

Thus each compact truncated pant has prescribed area-preserving diffeomorphism germs on neighborhoods of all three boundary components: two Fermi germs at its finite cuffs and the common cusp identity at its horocycle.

## 3. Extend the boundary germs before solving the Jacobian equation

The source and target `K_n,K_n^+` are labeled compact oriented pairs of pants. The three prescribed boundary-neighborhood germs are orientation preserving and respect the boundary labels. Shrink their collars if necessary so they are disjoint. Standard collar extension on a pair of pants then gives some smooth orientation-preserving diffeomorphism

\[
F_n:K_n\longrightarrow K_n^+
\tag{12}
\]

that agrees with all three prescribed germs on smaller boundary neighborhoods. No metric estimate is asserted for this interior extension.

By construction,

\[
\boxed{
F_n^*\omega_n^+=\omega_n
\quad\text{on an open neighborhood of }\partial K_n.
}
\tag{13}
\]

This is precisely the stronger input that PF-176 did not require. Merely fixing `F_n` on the boundary gives no jet control after Moser; arranging equality of the two volume forms on a *boundary neighborhood* lets the volume correction itself be supported away from every gluing interface.

## 4. Equal total area makes the interior support correction possible

PF-176 computes, by Gauss--Bonnet and the common normalized cusp truncation,

\[
\int_{K_n}\omega_n
=2\pi-\frac1Y
=\int_{K_n^+}\omega_n^+.
\tag{14}
\]

Therefore

\[
\int_{K_n}F_n^*\omega_n^+
=
\int_{K_n}\omega_n.
\tag{15}
\]

Together with (13), the difference

\[
F_n^*\omega_n^+-\omega_n
\tag{16}
\]

is a smooth compactly supported top-degree form in the interior with integral zero.

The relative/support-controlled form of the Moser--Dacorogna pullback theorem now applies: for two positive smooth volume forms of equal total volume that coincide near the boundary, there is a diffeomorphism

\[
\phi_n:K_n\longrightarrow K_n
\tag{17}
\]

which is the identity on a whole neighborhood of the boundary and satisfies

\[
\boxed{
\phi_n^*(F_n^*\omega_n^+)=\omega_n.
}
\tag{18}
\]

Set

\[
\widetilde F_n:=F_n\circ\phi_n.
\tag{19}
\]

Then (18) gives exact area preservation, while `\phi_n=id` near `\partial K_n` means that `\widetilde F_n` retains the full Fermi and cusp germs of Sections 1--2, including all normal derivatives.

For completeness, on a surface this support statement also follows directly from the usual Moser flow. Because (16) is compactly supported in the interior and has zero integral, it has a compactly supported primitive `alpha_n`. Along the positive path of volume forms between `omega_n` and `F_n^*omega_n^+`, solve `i_{V_t}\omega_t=-alpha_n`. The vector field is compactly supported in the interior, so its flow is identically the identity near the boundary. The external support-control theorems below are therefore prior art for the mechanism rather than a new project theorem.

## 5. The infinite assembly is smooth because the corrections vanish near every interface

At a shared cuff, the two neighboring pant maps both equal the two halves of the same signed map (8) on an open collar. They therefore glue to a smooth diffeomorphism across that cuff. The zero-twist marking is preserved because (8) commutes with the cuff involution.

At every cusp truncation, the corrected pant map equals the common cusp identity on an open slab, so it glues smoothly to the exact identity on the entire deeper cusp.

The pants decomposition is locally finite. Hence the assembled map (4) is a smooth local diffeomorphism everywhere. It maps each labeled pant and each cusp to its matched clone piece, so the inverse is obtained by assembling the corresponding inverses and is smooth by the same argument. Equation (5) holds on every piece and on their common neighborhoods, hence globally.

Thus the qualitative chain is now

\[
\boxed{
\text{area-preserving boundary germs}
+\text{ equal pant areas}
+\text{ support-controlled Moser}
\Longrightarrow
\text{smooth global }\rho=1\text{ marking}.
}
\tag{20}
\]

The point is not that a volume-preserving diffeomorphism exists in abstract topology; the useful project-specific fact is that it can be assembled while retaining explicit common cuff/cusp germs, so **Moser correction itself no longer creates a smooth-gluing obstruction**.

## 6. Why this does not yet trigger PF-175

PF-175 needs substantially more than (5). For some `r>1` it assumes complete quasi-isometric metrics and the two-sided weighted bound

\[
\int_X W_g\,\delta_{g,\widetilde F^*g_+}^{\,r}d\mu_g
+
\int_X W_{\widetilde F^*g_+}\,\delta_{g,\widetilde F^*g_+}^{\,r}d\mu_{\widetilde F^*g_+}
<\infty.
\tag{21}
\]

The construction above gives no uniform estimate on `D\phi_n`, let alone on the full multiplicative metric distortion after infinitely many pants are assembled. The boundary collars available at some decomposition cuffs may become geometrically narrow, and an arbitrary interior extension (12) has no tail-uniform norm bound.

This limitation is not cosmetic. Pedro Teixeira's support-control analysis explicitly notes that the available `C^{r+1,alpha}` estimates for support-preserving Dacorogna--Moser constructions depend on the distance from the forcing support to the boundary; the method does not provide a constant uniform as that distance collapses. Therefore support control should not be silently upgraded to the degeneration-independent metric estimate needed here.

PF-177 remains relevant precisely because it provides much stronger quantitative information on the genuinely collapsing short-collar sector: there the density forcing is already confined to a uniformly thick rim with a summable budget. PF-178 says that the remaining global issue is no longer *whether* the density can be corrected smoothly, but whether one can choose that correction with the required **uniform thick-region metric cost**.

## 7. Prior art and novelty audit

The support-controlled volume-form theorem is prior art.

Pedro Teixeira, *Addendum to: Dacorogna-Moser theorem on the Jacobian determinant equation with control of support*, arXiv:1705.01416 (2017), states the pullback result for two prescribed volume forms of equal total volume which coincide near the boundary, with the solution diffeomorphism equal to the identity near the boundary. This explicitly upgrades pointwise boundary fixing to support control in the setting needed above.

Olivier Kneuss, *Optimal Regularity and Control of the Support for the Pullback Equation*, Journal of Partial Differential Equations 30 (2017), no. 4, 317--328, DOI `10.4208/jpde.v30.n4.3`, independently treats support-controlled pullback for volume forms (and symplectic forms) on bounded Euclidean domains with optimal regularity.

Teixeira's earlier paper, *Dacorogna-Moser theorem on the Jacobian determinant equation with control of support*, Discrete and Continuous Dynamical Systems 37 (2017), 4071--4089, DOI `10.3934/dcds.2017173`, proves the `g=1` prescribed-Jacobian support-control case and records the important non-uniformity of the available norm estimates with respect to support-to-boundary distance.

Banyaga's boundary Moser theorem and Dacorogna--Moser's original prescribed-Jacobian theorem were already audited in PF-176. No novelty is claimed for Moser theory, support control, relative de Rham exactness, or extension of compatible boundary maps on a pair of pants.

The durable project-specific deduction is the gate closure (20) for the exact prime/shift decomposition: explicit area-preserving cuff germs plus common cusp germs let support-controlled correction survive the infinite zero-twist gluing. This removes **qualitative global smooth `rho=1` existence** from the unresolved Schatten route while leaving the quantitative weighted problem fully open.

## 8. Audit / falsification core

A later adversary can check PF-178 through the following short chain:

1. in signed Fermi coordinates verify equations (8)--(10), including commutation with `s -> -s`;
2. verify that the normalized prime/shift cusp models agree exactly near the chosen truncation horocycle;
3. choose an orientation-preserving pant diffeomorphism extending those three boundary-neighborhood germs and check (13);
4. verify the equal-area identity (14);
5. apply the support-controlled pullback theorem, or equivalently the compactly supported Moser-flow argument, to obtain (18) with `phi_n=id` near every boundary component;
6. check that neighboring corrected pants equal the same signed cuff germ on an open set, hence glue smoothly to all orders, and that cusp pieces glue to the exact identity;
7. do **not** infer any uniform bound on `D\phi_n`, global quasi-isometry, weighted `delta^r` summability, or PF-175's Schatten conclusion from this existence argument.

A refutation of the main claim would require failure of the explicit area calculation, failure of equal total pant area, or a failure of support-controlled Moser under smooth positive equal-volume forms coinciding near the boundary. Demonstrating that quantitative constants blow up along the tail would not refute PF-178; it would instead confirm the exact boundary recorded in Section 6.