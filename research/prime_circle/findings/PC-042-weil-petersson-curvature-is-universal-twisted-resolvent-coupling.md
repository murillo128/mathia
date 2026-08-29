# PC-042 — Weil–Petersson curvature couples orthogonal birth sectors through a universal twisted resolvent

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CANDIDATE-NEW-STRUCTURE`; no RH claim and no novelty claim for the Tromba–Wolpert curvature formula, cyclic character decomposition, or twisted resolvents. The durable prime-circle result is that the nonlinear curvature escape left open by PC-041 is real but highly constrained: after Weil–Petersson normalization, every curvature coefficient on a full roots-of-unity cover is `1/N` times one universal four-holonomy kernel on the thrice-punctured sphere, with an exact character-conservation rule.

PC-041 proved that canonical divisor refinement is completely flat at the Weil–Petersson **metric** level: exact-order birth sectors are orthogonal, normalized pullback has identity transport, and no order-sensitive holonomy is generated. Its main surviving boundary was the nonlinear Weil–Petersson curvature tensor, whose classical Tromba–Wolpert formula contains a Green/resolvent operator acting on products of harmonic Beltrami fields.

This finding computes that boundary for the same intrinsic full-root cyclic covers.

## 1. Universal normalized Beltrami modes on the fixed base

Let

\[
B=\widehat{\mathbb C}\setminus\{0,1,\infty\},
\qquad
Y_N=\widehat{\mathbb C}\setminus\bigl(\{0,\infty\}\cup\mu_N\bigr),
\]

with covering

\[
\pi_N:Y_N\to B,
\qquad
w=z^N.
\]

As in PC-040/041, the cyclic cotangent eigenbasis is

\[
q_{N,j}(z)=\frac{z^{j-2}}{z^N-1}\,dz^2,
\qquad 1\le j<N.
\]

Put

\[
\alpha=\frac{j}{N}\in(0,1).
\]

On a local inverse branch of `w=z^N`, define the unitary-local-system quadratic differential

\[
\widetilde q_\alpha(w)
=
\frac{w^{\alpha-2}}{w-1}\,dw^2.
\]

Direct substitution gives the exact pullback identity

\[
\boxed{
q_{N,j}=N^{-2}\pi_N^*\widetilde q_\alpha.
}
\]

Let `rho_B(w)|dw|` be the complete hyperbolic metric on `B`, and let `mu_alpha` be the harmonic Beltrami differential corresponding to `widetilde q_alpha`. Since the hyperbolic metric pulls back under the unbranched cover, the corresponding Beltrami differential on `Y_N` obeys, tensorially,

\[
\boxed{
\mu_{N,j}=N^{-2}\pi_N^*\mu_\alpha.
}
\]

PC-040 computed the norm scaling

\[
\|\mu_{N,j}\|_{WP}^2=N^{-3}I(\alpha),
\]

where `I(alpha)>0` is the universal Petersson profile on `B`. Define

\[
\nu_\alpha:=I(\alpha)^{-1/2}\mu_\alpha,
\qquad
\widehat\mu_{N,j}:=rac{\mu_{N,j}}{\|\mu_{N,j}\|_{WP}}.
\]

Then the normalized tangent mode has the particularly simple exact form

\[
\boxed{
\widehat\mu_{N,j}=N^{-1/2}\pi_N^*\nu_{j/N}.
}
\]

Thus every normalized tangent direction in every full-root cover is a rational-holonomy sample of one normalized local-system family on the fixed surface `B`.

## 2. Tromba–Wolpert curvature turns products into twisted resolvents

Use the Laplacian sign convention in which the hyperbolic Laplacian is non-positive, and write

\[
\mathscr D=-2(\Delta-2)^{-1}.
\]

This is the positive self-adjoint Green/resolvent operator appearing in the Tromba–Wolpert curvature formula. With the Riemann-tensor sign convention in which Weil–Petersson holomorphic bisectional curvature is non-positive, the curvature tensor of harmonic Beltrami differentials is, up to the standard placement/conjugation convention for indices,

\[
\boxed{
-R_{i\bar j k\bar l}
=
\int \mathscr D(\mu_i\overline{\mu_j})\,
       \mu_k\overline{\mu_l}\,dA
+
\int \mathscr D(\mu_i\overline{\mu_l})\,
       \mu_k\overline{\mu_j}\,dA.
}
\]

Changing the global Riemann-tensor sign convention flips both sides and does not affect any scaling, selection, or nonvanishing statement below.

The important point for the cyclic cover is that a product of two character modes is generally **not** invariant. If the cotangent holonomy labels are `alpha` and `beta`, then the corresponding Beltrami product carries the difference character `beta-alpha` (or its inverse, depending on the tangent/cotangent convention). Consequently it descends not to an ordinary scalar function on `B`, but to a section of the unitary flat line bundle of holonomy

\[
\theta=\beta-\alpha\pmod 1.
\]

Let

\[
\Delta_\theta
\]

be the hyperbolic Laplacian on that flat line bundle over `B`, and define the fixed-energy twisted resolvent

\[
\boxed{
\mathscr D_\theta=-2(\Delta_\theta-2)^{-1}.
}
\]

Fourier decomposition of the regular cyclic cover, already used in PC-022, implies exact intertwining:

\[
\mathscr D_{Y_N}\bigl(\pi_N^*f_\theta\bigr)
=
\pi_N^*\bigl(\mathscr D_\theta f_\theta\bigr).
\]

Thus the nonlinear curvature formula does not create a new spectral family. It forces the **same universal twisted Laplacian family from PC-022**, now sampled through its resolvent at the fixed parameter selected by Weil–Petersson curvature.

## 3. Exact universal four-holonomy curvature kernel

Take indices `j_a,j_b,j_c,j_d` in `{1,...,N-1}` and set

\[
\alpha=\frac{j_a}{N},\qquad
\beta =\frac{j_b}{N},\qquad
\gamma=\frac{j_c}{N},\qquad
\delta=\frac{j_d}{N}.
\]

Insert the normalized pullback formula

\[
\widehat\mu_{N,j}=N^{-1/2}\pi_N^*\nu_{j/N}
\]

into Tromba–Wolpert. Each Beltrami product contributes `N^{-1}`, while integration over the `N` sheets contributes `N`. Therefore

\[
\boxed{
R^{(N)}_{\alpha\bar\beta\gamma\bar\delta}
=
\frac1N\,
\mathcal R(\alpha,\beta,\gamma,\delta),
}
\]

where `mathcal R` is a level-independent kernel on `B`. In the negative-bisectional-curvature sign convention, its negative is represented by

\[
\begin{aligned}
-\mathcal R(\alpha,\beta,\gamma,\delta)
={}&
\int_B
\mathscr D_{\beta-\alpha}
\bigl(\nu_\alpha\overline{\nu_\beta}\bigr)
\,\nu_\gamma\overline{\nu_\delta}\,dA\\
&+
\int_B
\mathscr D_{\delta-\alpha}
\bigl(\nu_\alpha\overline{\nu_\delta}\bigr)
\,\nu_\gamma\overline{\nu_\beta}\,dA,
\end{aligned}
\]

with the local-system tensor products understood canonically.

Deck invariance immediately gives the exact conservation law

\[
\boxed{
\mathcal R(\alpha,\beta,\gamma,\delta)=0
\quad\text{unless}\quad
\alpha+\gamma\equiv\beta+\delta\pmod1.
}
\]

Equivalently, at level `N`,

\[
\boxed{
j_a+j_c\equiv j_b+j_d\pmod N.}
\]

So the complete curvature tensor is sparse in the cyclic-character basis, and every surviving entry is a rational sample of one universal four-holonomy resolvent kernel.

This is stronger than the metric-level diagonalization of PC-040/041. The metric conserves character one pair at a time; the curvature conserves only the **total** character across a four-mode interaction, so it can couple distinct exact-order sectors.

## 4. Orthogonal birth sectors have strictly nonzero mixed curvature

The cleanest coupling is the mixed bisectional component. Set `beta=alpha` and `delta=gamma`. Then the conservation law is automatic and

\[
\begin{aligned}
-NR^{(N)}_{\alpha\bar\alpha\gamma\bar\gamma}
={}&
\int_B
\mathscr D_0(|\nu_\alpha|^2)
|\nu_\gamma|^2\,dA\\
&+
\int_B
\mathscr D_{\gamma-\alpha}
(\nu_\alpha\overline{\nu_\gamma})
\overline{(\nu_\alpha\overline{\nu_\gamma})}\,dA.
\end{aligned}
\]

Both terms are nonnegative. More importantly, the first is **strictly positive** for nonzero modes: `|nu_alpha|^2` is a nonzero nonnegative function, and the Green operator `mathscr D_0` is positivity improving on the connected hyperbolic surface `B`; multiplication by the nonzero nonnegative `|nu_gamma|^2` therefore gives a positive integral. Hence

\[
\boxed{
R^{(N)}_{\alpha\bar\alpha\gamma\bar\gamma}<0
}
\]

under the usual Weil–Petersson sign convention.

This proves that the nonlinear escape in PC-041 is not merely formal. Distinct exact-order birth sectors can be orthogonal for the Weil–Petersson metric while still interacting through strictly nonzero Weil–Petersson curvature.

For two distinct primes `p,q` embedded in the common refinement `Y_{pq}`, take

\[
\alpha=\frac ap,
\qquad
\gamma=\frac bq,
\qquad
(a,p)=(b,q)=1.
\]

PC-041 gives zero metric cross pairing between these prime birth modes. Their mixed curvature, however, contains the twisted channel

\[
\boxed{
\theta=\gamma-\alpha
=\frac{bp-aq}{pq}\pmod1,
}
\]

and is strictly nonzero. The integer `bp-aq` is the familiar determinant appearing in rational/Farey geometry, so that arithmetic appearance by itself is classical; the genuinely different object here is the resolvent-mediated nonlinear coupling of the two holonomy modes.

## 5. What this does and does not buy for RH

This result materially changes the boundary left by PC-041:

\[
\boxed{
\text{metric orthogonality does not imply nonlinear decoupling.}
}
\]

There is an intrinsic, nonseparable, two-dimensional operator mechanism in the original roots-of-unity geometry:

\[
\boxed{
(\alpha,\gamma)
\longmapsto
\mathscr D_{\gamma-\alpha}
(\nu_\alpha\overline{\nu_\gamma}),
}
\]

and cross-level prime modes interact through it after being placed in their canonical common full-root refinement.

However, the same derivation sharply limits the interpretation:

- all level dependence is only the global factor `1/N` plus rational sampling of `alpha,beta,gamma,delta`;
- the twisted operator is the universal `B`-family already present in PC-022, not a newly generated prime-specific spectrum;
- Weil–Petersson curvature evaluates that family at one fixed resolvent parameter; there is no free complex variable `s`;
- no gamma factor, zeta functional equation, Riemann zero set, or intrinsic identification with `Re(s)=1/2` has appeared;
- the difference `bp-aq` in a `p`–`q` coupling is ordinary rational/Farey determinant data and must not be counted as novelty by itself.

Therefore the existence of nonzero curvature coupling is a **surviving mechanism**, not an RH bridge. To become RH-relevant it would need an additional intrinsic operation that turns this fixed-energy universal kernel into a scale-dependent analytic object without simply inserting a Mellin/Dirichlet transform or a known automorphic zeta by hand.

## 6. Prior art and novelty audit

The analytic ingredients are classical.

- Scott A. Wolpert, *Chern forms and the Riemann tensor for the moduli space of curves*, Inventiones Mathematicae **85** (1986), 119–145, DOI `10.1007/BF01388794`, is a primary source for the Weil–Petersson Riemann tensor/Green-operator formula in the compact setting.
- Lin Weng, *Omega-admissible theory. II. Deligne pairings over moduli spaces of punctured Riemann surfaces*, Mathematische Annalen **320** (2001), 239–283, DOI `10.1007/s002080100194`, Appendix, explicitly states that the Weil–Petersson Riemann tensor for punctured Teichmüller space has the same form as in the compact case and writes the resolvent/spectral decomposition used to estimate curvature.
- PC-022 already identifies `L^2(Y_N)` with rational samples of the universal unitary-character spectral family on `B`, so the appearance of `Delta_theta` is not a new spectral discovery.
- PC-040/041 already give the normalized holonomy modes and the exact covering scalings needed for the `1/N` law.

Directed searches for Weil–Petersson curvature on these roots-of-unity cyclic special points, character eigenspaces on cyclic covers, and twisted-resolvent formulations did not locate this exact four-holonomy pushdown package. That absence is not evidence of historical priority. The pushdown is an elementary consequence of classical curvature plus covering/character theory once the prime-circle basis is fixed.

The research-specific contribution is therefore the classification and boundary:

\[
\boxed{
N\,R^{(N)}
=
\text{one universal character-conserving twisted-resolvent kernel on }B.
}
\]

## 7. Boundary of the result

This finding applies to the **full-root cover tower** `Y_N`. At prime level `Y_p` is exactly the anchored prime birth surface, so the result applies directly to the original prime layer. At composite level, the actual primitive-only birth surface from PC-017 is not `Y_N`; its uniformization defect remains outside this reduction.

The result also does not classify:

- variation of the twisted resolvent as the puncture configuration itself moves away from the symmetric roots-of-unity point;
- covariant derivatives of curvature or higher Liouville/Weil–Petersson response;
- nonlinear functionals built from repeated curvature contractions across many levels;
- the primitive-only composite birth-surface geometry;
- any mechanism that forces an independent spectral/Mellin parameter rather than inserting one externally.

Thus the live nonlinear branch is narrower but genuine: **curvature couples sectors that the metric cannot see, yet on the full-root tower that coupling is still universal holonomy data on a fixed base.**

## 8. Exact audit and falsification tests

The main statements can be checked without numerical fitting:

1. substitute `w=z^N` to verify `q_{N,j}=N^{-2}pi_N^*widetilde q_{j/N}`;
2. combine covering degree with the `N^{-2}` field scale to recover the `N^{-3}` Weil–Petersson norm and `N^{-1/2}` normalized tangent scale;
3. verify that a product of two deck eigenmodes lies in the difference-character sector and that the cover Laplacian/resolvent restricts to the corresponding twisted operator on `B`;
4. insert four normalized modes into the Tromba–Wolpert formula and check that two products contribute `N^{-2}` while the `N` sheets leave exactly `N^{-1}`;
5. apply the deck generator to a curvature integrand and recover the conservation rule `j_a+j_c=j_b+j_d mod N`;
6. for a mixed bisectional component, use positivity improvement of `-2(Delta-2)^{-1}` to verify strict nonvanishing;
7. embed prime-order modes from `Y_p` and `Y_q` into `Y_{pq}` and check that their metric pairing is zero by PC-041 while their mixed bisectional curvature is nonzero and uses twist `(bp-aq)/(pq)`.

Any failure of the `1/N` scaling, character conservation, resolvent intertwining, or mixed-curvature nonvanishing would invalidate the core classification. No claim is made that the universal kernel is historically new or that it already encodes the Riemann zeros.