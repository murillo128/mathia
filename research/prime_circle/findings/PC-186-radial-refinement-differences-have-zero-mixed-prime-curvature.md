# PC-186 — radial refinement differences have zero mixed-prime curvature

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for obtaining a second Prime-Circle arithmetic carrier or a mixed-prime curvature from the source-native **linear cross-level refinement law** of the cyclotomic radial potential/flux, including its natural dilation--multiplication crossed-product realization.

PC-185 leaves shell/cross-level dependence outside its theorem for fixed shell-independent refinement-equivariant filters. The first source-forced candidate in that remaining region is not an arbitrary shell-dependent operator: it is the exact child-shell law already encoded by the cyclotomic identities themselves. This candidate also collapses. New-prime birth is exactly a finite difference of the radial dilation action, repeated-prime refinement is pure dilation, and the distinct-prime directions commute identically. The entire linear radial refinement lattice is therefore flat before any Mellin transform or positive scalarization.

The same calculation gives a useful interpretation of the common-vertex von Mangoldt selector. `log p` is produced only by the **first** finite difference acting on the logarithmically singular universal seed `log(1-e^{-x})`; every later distinct-prime difference acts on a bounded profile and has zero endpoint. On the flux side, after the first difference has regularized the seed, every later distinct-prime difference has zero total mass because the flux dilation preserves the integral. Thus the prime-power support is a first-difference scale anomaly plus an invariant-functional cancellation, not curvature between distinct prime directions.

## 1. Exact cyclotomic refinement law on radial profiles

Put

\[
F_1(x):=\log(1-e^{-x}),
\qquad
F_n(x):=\log\Phi_n(e^{-x})\quad(n>1),
\]

and

\[
\rho_n(x):=-F_n'(x).
\]

For `a>0` define the potential and flux dilation actions

\[
(\alpha_a f)(x):=f(ax),
\qquad
(\beta_a g)(x):=a\,g(ax).
\tag{1}
\]

They satisfy

\[
\alpha_a\alpha_b=\alpha_{ab},
\qquad
\beta_a\beta_b=\beta_{ab}.
\tag{2}
\]

Let `p` be prime. The standard cyclotomic recursion is

\[
\Phi_{pn}(z)=
\begin{cases}
\Phi_n(z^p)/\Phi_n(z),&p\nmid n,\\
\Phi_n(z^p),&p\mid n.
\end{cases}
\tag{3}
\]

Consequently the embedded radial fields obey the exact two-case law

\[
\boxed{
F_{pn}=
\begin{cases}
(\alpha_p-I)F_n,&p\nmid n,\\
\alpha_pF_n,&p\mid n,
\end{cases}}
\tag{4}
\]

and differentiation gives

\[
\boxed{
\rho_{pn}=
\begin{cases}
(\beta_p-I)\rho_n,&p\nmid n,\\
\beta_p\rho_n,&p\mid n.
\end{cases}}
\tag{5}
\]

Thus the first appearance of a prime is a finite difference in scale, whereas increasing an existing valuation is only scale transport.

## 2. Every shell is generated from one singular seed by commuting prime differences

Let

\[
r=\operatorname{rad}(n)=\prod_{p\mid n}p,
\qquad
h=\frac nr.
\]

Iterating (4)--(5), and using commutativity of the dilation actions, gives the exact all-shell factorization

\[
\boxed{
F_n
=\alpha_h\prod_{p\mid r}(\alpha_p-I)F_1,
}
\tag{6}
\]

and

\[
\boxed{
\rho_n
=\beta_h\prod_{p\mid r}(\beta_p-I)\rho_1,
\qquad
\rho_1(x)=-\frac1{e^x-1}.
}
\tag{7}
\]

The products are independent of the order of the distinct primes. In particular, the apparent shell dependence of the canonical linear cross-level construction is exhausted by a commuting family of prime-labelled finite differences followed by the valuation dilation `h`.

This is stronger than merely observing that the abstract birth-labelled root tower is commutative. Equations (6)--(7) are identities for the actual off-boundary Prime-Circle radial fields that PC-010 deliberately kept outside its abstract Bost--Connes reduction.

## 3. Distinct-prime refinement curvature vanishes identically

Let `p` and `q` be distinct primes with `pq\nmid n` and, more specifically, `p\nmid n` and `q\nmid n`. Applying the two new-prime steps in either order gives

\[
F_{pqn}
=(\alpha_q-I)(\alpha_p-I)F_n
=(\alpha_p-I)(\alpha_q-I)F_n.
\tag{8}
\]

Hence the natural mixed finite-difference curvature is exactly

\[
\boxed{
[(\alpha_p-I),(\alpha_q-I)]F_n=0.
}
\tag{9}
\]

Likewise,

\[
\boxed{
[(\beta_p-I),(\beta_q-I)]\rho_n=0.
}
\tag{10}
\]

The same statement holds for every higher squarefree refinement cube: any permutation of the new-prime directions produces the identical profile. There is therefore no linear mixed-prime holonomy hidden in the radial refinement square.

The result is not a statement that every possible shell-dependent Prime-Circle construction is flat. It says that the **canonical shell-changing operation actually supplied by the cyclotomic radial geometry** is already an abelian finite-difference system.

## 4. The natural crossed-product commutator produces the child shell but remains flat

One might try to retain noncommutativity by representing scale transport and radial multiplication as operators before scalarizing. This still does not create mixed-prime curvature.

Fix `c>0` and use the normalized dilation representation from PC-185,

\[
(U_a^{(c)}\psi)(x)=a^c\psi(ax).
\]

For a bounded radial profile `f`, let `M_f` denote multiplication by `f`. Then

\[
U_a^{(c)}M_f(U_a^{(c)})^{-1}=M_{\alpha_af}.
\tag{11}
\]

For `n>1`, `F_n` is bounded, so `M_{F_n}` is bounded. If `p\nmid n`, equation (4) becomes

\[
\boxed{
[U_p^{(c)},M_{F_n}](U_p^{(c)})^{-1}
=M_{F_{pn}}.
}
\tag{12}
\]

Thus the most immediate noncommutative dilation--multiplication commutator is not a new carrier: it is exactly the next cyclotomic shell.

Define

\[
\delta_p:=\operatorname{Ad}(U_p^{(c)})-I.
\]

Because the dilation unitaries commute,

\[
\boxed{
\delta_p\delta_q=\delta_q\delta_p
}
\tag{13}
\]

on the whole operator algebra on which these maps are defined. In particular,

\[
\delta_q\delta_p(M_{F_n})=M_{F_{pqn}}
=\delta_p\delta_q(M_{F_n}).
\tag{14}
\]

So moving to the natural crossed-product realization does introduce noncommuting **multiplication versus dilation**, but the prime-direction connection itself is still exactly flat. A curvature or associator would require additional source-forced structure beyond this canonical covariant representation.

## 5. The von Mangoldt endpoint is a first-difference scale anomaly

The singular seed has

\[
F_1(x)=\log x+O(x)
\qquad(x\to0+).
\tag{15}
\]

For the first new prime `p`, equation (4) therefore gives

\[
\boxed{
\lim_{x\to0+}(\alpha_p-I)F_1(x)=\log p.
}
\tag{16}
\]

After that first difference, `F_p` is bounded at the common vertex. Repeated `p`-refinement only dilates it, so

\[
F_{p^a}(0+)=\log p.
\tag{17}
\]

But if `q\neq p`, then boundedness gives

\[
\boxed{
\lim_{x\to0+}(\alpha_q-I)F_{p^a}(x)=0.
}
\tag{18}
\]

The same argument applies after any first distinct-prime birth. Equations (16)--(18) recover exactly

\[
F_n(0+)=\log\Phi_n(1)=\Lambda(n).
\tag{19}
\]

This identifies where the prime-power selector enters the radial refinement hierarchy. It is not a nonzero two-prime commutator: it is the failure of the logarithmically singular seed to be scale-invariant at the boundary. Once the first difference has removed that singularity, every further distinct-prime difference has zero endpoint.

## 6. The signed-flux selector is the same anomaly seen through an invariant integral

The seed flux `rho_1=-1/(e^x-1)` is not integrable at `0`, but the first new-prime difference is. With a cutoff,

\[
\int_\varepsilon^\infty
(\beta_p-I)\rho_1(x)\,dx
=
-\int_\varepsilon^{p\varepsilon}\rho_1(x)\,dx
\longrightarrow \log p.
\tag{20}
\]

This is the flux version of (16).

Once `g` is integrable, however, the flux dilation preserves total mass exactly:

\[
\boxed{
\int_0^\infty \beta_a g(x)\,dx
=\int_0^\infty g(x)\,dx.
}
\tag{21}
\]

Therefore

\[
\boxed{
\int_0^\infty(\beta_q-I)g(x)\,dx=0.
}
\tag{22}
\]

After the first prime difference has regularized `rho_1`, every second distinct-prime birth is of the form (22), whereas repeated same-prime dilation preserves the first mass. Hence

\[
\int_0^\infty\rho_n(x)\,dx
=\Lambda(n)
\tag{23}
\]

follows directly from the refinement calculus itself.

This sharpens the interpretation of PC-179: the exact signed prime-power support is real, but at the linear cross-level level it is generated by a singular endpoint anomaly plus an invariant functional, not by an interaction between distinct prime axes.

## 7. Mellinization diagonalizes the same flat refinement calculus

For an integrable Mellin profile,

\[
\mathcal M[\beta_a g](s)
=a^{1-s}\mathcal M[g](s).
\tag{24}
\]

In the half-plane where the seed transform is initially absolutely convergent,

\[
\mathcal M\rho_1(s)=-\Gamma(s)\zeta(s).
\tag{25}
\]

Applying (7) gives

\[
\mathcal M\rho_n(s)
=-\Gamma(s)\zeta(s)
\,h^{1-s}
\prod_{p\mid r}(p^{1-s}-1).
\tag{26}
\]

Since `n=hr`, this is identically

\[
\boxed{
\mathcal M\rho_n(s)
=-\Gamma(s)\zeta(s)n^{1-s}
\prod_{p\mid n}(1-p^{s-1}),
}
\tag{27}
\]

which is exactly the PC-179 factorization.

Thus the finite shell Euler factor in PC-179 is nothing more than the scalar character of the commuting prime finite differences under Mellin diagonalization. Mellinization does not discard a hidden mixed-prime curvature here: equations (9)--(10) show that no such linear curvature existed before Mellinization.

## 8. Prior-art and novelty audit

No historical novelty is claimed for the ingredients.

- The two-case cyclotomic recursion (3), cyclotomic product formula, and `Phi_n(1)` prime-power identity are classical.
- Dilation is the abelian multiplicative action of `R_+`, and Mellin transform diagonalizes it; PC-184/PC-185 already anchor this as standard multiplicative harmonic analysis.
- PC-010 identifies the abstract roots-of-unity refinement semigroup with the Bost--Connes cyclotomic tower and records the classical Bost--Connes/endomotive references. Directed checking of neighboring endomotive literature again places roots of unity with positive-integer endomorphism actions and semigroup crossed products squarely in that established framework.
- PC-179 already identifies (27) as the classical Ramanujan/Lambert Mellin factorization of zeta.

The durable contribution is therefore a **Prime-Circle architecture obstruction**, not a new cyclotomic theorem: even after retaining the actual radial embedding and allowing the canonical shell-changing operations before Mellinization, the linear cross-level prime directions form an exact flat finite-difference system. The common-vertex Mangoldt selector is a first-difference boundary anomaly, not evidence of mixed-prime curvature.

This also explains why merely placing the radial fields inside a dilation crossed product cannot count as progress: equation (12) recovers the child shell, while equation (13) makes the prime-square defect identically zero. This is consistent with, rather than independent of, the Bost--Connes novelty boundary.

## 9. Scope, falsifiers, and surviving frontier

The negative result covers the source-native **linear** radial refinement architecture generated by the exact cyclotomic child relations, including finite compositions of new-prime differences, repeated-prime dilations, their Mellin characters, and the immediate dilation--multiplication commutator realization.

It does **not** cover:

- nonlinear products or ordered functions of several shell profiles before reduction to the dilation action;
- a second source field that is not obtained from `F_1` by the refinement calculus above;
- shell-dependent operators whose coefficients depend on embedded chord/angular/old--new geometry rather than only on the radial child law;
- source-forced sign-indefinite couplings with additional geometric data;
- cross-level constructions that mix prime directions through another noncommuting carrier before the radial dilation representation is formed;
- the nonlinear global uniformization/accessory-parameter sector.

The exact claims can be falsified by any `n,p` for which (4) or (5) fails, any pair of distinct primes for which the mixed differences in (9)--(10) do not commute, or any integrable `g` violating (21). A candidate claiming to escape this finding must identify an intrinsic Prime-Circle operation not generated by the `alpha/beta` refinement calculus, rather than merely choosing a different scalar multiplier or reweighting the same commuting prime directions.

## Research consequence

PC-185 showed that fixed bounded refinement-equivariant radial filters remain one Mellin carrier. PC-186 now tests the simplest **cross-level** escape left by that theorem and finds that the canonical cyclotomic shell-changing law itself is still only commuting scale finite differences. The accepted signed-radial-flux direction therefore remains open only after an additional geometry-forced carrier or nonlinear/ordered coupling has been introduced **before** the flat radial refinement calculus is scalarized. Nonzero mixed-prime structure cannot be inferred from the prime-power selector alone.