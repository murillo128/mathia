# WP-156 — Cyclotomic block log-determinant lines factor through pairwise resultants

**Status:** `EXACT-DERIVED + DECISIVE-NARROWING + PRIME-CIRCLE + CYCLOTOMIC-RESULTANT + DISCRIMINANT-LINE + BLOCK-FACTORIZATION + NO-IRREDUCIBLE-HIGHER-INTERACTION + MATCHED-POPULATION-CONTROL + PRIOR-ART-CLASSICALIZATION` for the direct univariate block-resultant/discriminant escape left after `WP-155`.

`WP-155` localizes the missing ingredient one stage before Hodge positivity: the existing normalized resultant incidence has no genuinely mixed-prime curvature, so a surviving construction must change the incidence or correspondence before applying an ordinary positive completion. A natural determinant-line attempt is to group many primitive Prime-Circle shells **before** taking the scalar invariant. Instead of the pairwise resultant `Res(Phi_m,Phi_n)`, form block polynomials

\[
F_S(z)=\prod_{n\in S}\Phi_n(z)
\]

and ask whether block resultants, Vandermonde/discriminant lines, or the full divisor-closed polynomial can create a collective mixed-prime interaction that was absent from the pairwise graph.

For the canonical univariate constructions, they do not. Resultants are multiplicative, and the discriminant of a product factors into the discriminants of its factors times the squares of all pairwise resultants. After taking the logarithm required to expose the `log p` arithmetic scale, every block determinant line is therefore a set function of interaction order at most two. Its quadratic polarization is exactly the old zero-order resultant kernel already shown conditionally indefinite in `WP-146` and to have unbounded primitive two-sided inertia in `WP-147`.

Even the self-discriminant of a single composite cyclotomic shell does not create a hidden mixed-prime term after the natural per-root normalization: it is a sum of one-prime contributions. At the opposite extreme, closing all primitive shells under divisors gives `z^N-1`, whose per-root log discriminant is simply `log N`. Any apparent higher interaction in the raw `N log N` is produced by the number of roots, not by new arithmetic incidence.

Thus the most canonical **univariate block determinant-line** completion does not supply the global finite--finite coupling demanded by `WP-155`, let alone the finite--archimedean coupling required by the branch mandate. A genuinely multivariate correspondence, a new finite--real incidence, an analytic metric on a determinant line, or another source-forced operation that is not multiplicative over the existing cyclotomic factors remains outside this finding.

## 1. Block resultants are exactly sums of the old pairwise interactions

Let `A` and `B` be finite disjoint sets of shell orders and define

\[
F_A(z)=\prod_{m\in A}\Phi_m(z),
\qquad
F_B(z)=\prod_{n\in B}\Phi_n(z).
\tag{1}
\]

Distinct cyclotomic polynomials are monic and pairwise coprime over `Q`. The classical multiplicativity of the resultant gives

\[
\boxed{
\operatorname{Res}(F_A,F_B)
=
\prod_{m\in A}\prod_{n\in B}
\operatorname{Res}(\Phi_m,\Phi_n)
}
\tag{2}
\]

up to the irrelevant conventional sign, which disappears after absolute value. Put

\[
I_{m,n}:=\log\left|\operatorname{Res}(\Phi_m,\Phi_n)\right|.
\tag{3}
\]

Then

\[
\boxed{
\log|\operatorname{Res}(F_A,F_B)|
=
\sum_{m\in A}\sum_{n\in B} I_{m,n}.
}
\tag{4}
\]

Equation (4) is exact. Grouping shells into a larger polynomial can aggregate many old edges, but it cannot create an irreducible interaction between shell labels that was absent pairwise.

For the Prime-Circle arithmetic carrier this is decisive because Apostol's cyclotomic-resultant theorem already gives

\[
I_{m,n}=0
\]

unless one shell order is a prime-power multiple of the other. Therefore a block resultant can only sum the same prime-power edges; it does not manufacture a new cell coupling distinct prime coordinates.

The conclusion is not specific to the exact Apostol values. For arbitrary pairwise numbers `I_{m,n}`, multiplicativity alone gives (4). The block operation has no mathematical place in which a new three-shell or higher interaction could enter.

## 2. The block discriminant is a quadratic set function

The discriminant is the most canonical single determinant line attached to the union of shell roots. For a finite set `S`, write

\[
D(S):=\log|\operatorname{Disc}F_S|,
\qquad
F_S=\prod_{n\in S}\Phi_n.
\tag{5}
\]

Because the root sets of distinct cyclotomic factors are disjoint, the squared Vandermonde formula gives the classical product identity

\[
\boxed{
|\operatorname{Disc}F_S|
=
\prod_{n\in S}|\operatorname{Disc}\Phi_n|
\prod_{\{m,n\}\subset S}
|\operatorname{Res}(\Phi_m,\Phi_n)|^2.
}
\tag{6}
\]

Define

\[
d_n:=\log|\operatorname{Disc}\Phi_n|.
\tag{7}
\]

Taking logarithms in (6) gives

\[
\boxed{
D(S)
=
\sum_{n\in S}d_n
+2\sum_{\{m,n\}\subset S}I_{m,n}.
}
\tag{8}
\]

Thus `D` is exactly a degree-two set function. If

\[
\Delta_a D(S):=D(S\cup\{a\})-D(S),
\qquad a\notin S,
\tag{9}
\]

then for three distinct new shell labels

\[
\boxed{
\Delta_a\Delta_b\Delta_c D(S)=0.
}
\tag{10}
\]

More generally every mixed set difference of order at least three vanishes identically. The second difference is simply

\[
\boxed{
\Delta_a\Delta_b D(S)=2I_{a,b}.
}
\tag{11}
\]

Equations (10)--(11) give a precise answer to the determinant-line escape from `WP-155`: the block discriminant has no new higher incidence. Its entire interaction content is the already-known pairwise resultant graph.

## 3. Polarizing the block determinant returns the already-indefinite resultant kernel

The factorization in (8) is stronger than a support statement. Introduce formal occupancy variables `x_n` and extend the log discriminant polynomial as

\[
\mathcal D(x)
=
\sum_n d_n x_n
+2\sum_{m<n} I_{m,n}x_mx_n.
\tag{12}
\]

Its quadratic polarization has off-diagonal coefficients proportional to `I_{m,n}` and no new higher block. After the critical shell normalization

\[
y_n=\sqrt{\varphi(n)}\,x_n,
\tag{13}
\]

the off-diagonal coefficients are proportional to

\[
J_{m,n}
=
\frac{I_{m,n}}
{\sqrt{\varphi(m)\varphi(n)}},
\tag{14}
\]

which is exactly the normalized zero-order resultant kernel studied in `WP-146`--`WP-147`.

This immediately imports their sign obstruction. `WP-146` gives the exact mixed-prime chain

\[
6\longrightarrow12\longrightarrow36
\tag{15}
\]

on which the centered critical kernel is conditionally indefinite, while `WP-147` replicates such chains to force unbounded positive and negative primitive indices. A determinant line over a union of shells therefore does not hide a different quadratic form whose polarization might acquire a Hodge sign: **its canonical logarithmic polarization is the same finite block whose sign already fails.**

Keeping only the scalar `D(S)` avoids that indefinite polarization, but then one has only a nonnegative/log-volume number attached to a finite set, not a positive semidefinite quadratic form on the test-function space required by Weil positivity.

## 4. A single cyclotomic discriminant is prime-coordinate additive after per-root normalization

One might hope that the self term `d_n` in (8), rather than the cross resultants, contains a genuinely mixed-prime invariant. The classical cyclotomic discriminant formula rules this out in its natural density normalization. For `n>1`,

\[
\boxed{
|\operatorname{Disc}\Phi_n|
=
\frac{n^{\varphi(n)}}
{\displaystyle\prod_{p\mid n}
 p^{\varphi(n)/(p-1)}}.
}
\tag{16}
\]

Hence

\[
\boxed{
\frac{d_n}{\varphi(n)}
=
\log n-
\sum_{p\mid n}\frac{\log p}{p-1}.
}
\tag{17}
\]

Writing

\[
n=\prod_p p^{a_p}
\]

gives

\[
\boxed{
\frac{d_n}{\varphi(n)}
=
\sum_{p:a_p>0}
\left(a_p-\frac1{p-1}\right)\log p.
}
\tag{18}
\]

There is no term depending jointly on two distinct primes. The self-discriminant density is a sum of one-coordinate contributions.

It also fails the finite Weil support and exponent tests directly. For example,

\[
\frac1{\varphi(6)}\log|\operatorname{Disc}\Phi_6|
=\frac12\log3>0,
\tag{19}
\]

although

\[
\Lambda(6)=0.
\tag{20}
\]

On a prime power `p^a`, (18) gives

\[
\left(a-\frac1{p-1}\right)\log p,
\tag{21}
\]

rather than the exponent-independent Mangoldt value `log p`.

The **raw** quantity `d_n` can of course have mixed finite differences because it is `varphi(n)` times (18). But that mixing comes from the multiplicative population `varphi(n)`, not from a new interaction among prime coordinates. A matched model with arbitrary independent coordinate labels and the same population law produces the same effect. It therefore does not provide the source-specific global incidence demanded by the research mandate.

## 5. The maximal divisor-closed block collapses to polygon size

There is an even more canonical block than an arbitrary finite set. Include every primitive shell whose order divides `N`. The cyclotomic factorization gives

\[
\boxed{
G_N(z)
:=\prod_{d\mid N}\Phi_d(z)
=z^N-1.
}
\tag{22}
\]

The roots are the full regular `N`-gon. Its discriminant is elementary:

\[
\boxed{
|\operatorname{Disc}(z^N-1)|=N^N.
}
\tag{23}
\]

Therefore the log discriminant per root is

\[
\boxed{
\frac1N\log|\operatorname{Disc}G_N|
=\log N
=\sum_p v_p(N)\log p.
}
\tag{24}
\]

The strongest canonical univariate closure has thus forgotten the primitive-shell selector completely. At `N=6`, for instance, (24) is `log 6>0` although the Mangoldt selector at the composite index `6` vanishes.

The raw block quantity

\[
\log|\operatorname{Disc}G_N|=N\log N
\tag{25}
\]

can display mixed finite differences in prime factors, but the extra factor is exactly the number of roots in the polygon. Dividing by that population leaves the completely additive logarithmic scale (24). This is a clean matched control for apparent determinant-induced globality: **population multiplication can mimic a mixed interaction without introducing new arithmetic incidence.**

## 6. Adversarial repairs and exact escape boundary

Several immediate repairs do not change the conclusion, but the boundary matters.

**Nonlinear degree normalization.** A readout such as `D(S)/deg(F_S)` or another nonlinear function of the total block size can create nonzero higher set differences even when (8) is quadratic. Those higher terms are generated by the chosen denominator/readout. The same phenomenon occurs for arbitrary nonarithmetic factor families with the same degrees, so it is not an intrinsic prime coupling. Its positivity and its exact Weil normalization would require a separate theorem.

**Signed ratios of discriminants.** Ratios can cancel unwanted self or pairwise terms after taking logarithms, but they use subtraction between determinant lines. The required cancellations then come from the chosen ratio rather than from inherited positivity. This is exactly the kind of selector/sign tension already exposed elsewhere in the branch.

**Taking the determinant of a matrix built from resultants.** This finding does not identify such a matrix with the polynomial discriminant. Graph Laplacians, Kron reductions, pseudodeterminants, and related collective matrices are different constructions and have already required separate audits in `WP-140`--`WP-153`. Equation (6) applies to the ordinary univariate polynomial determinant line itself.

**Differentiating the root interaction.** The positive Hessian of the logarithmic root interaction is also different from the zero-order discriminant line. `WP-145` shows that this move obtains an independent PSD sign only by destroying prime-power support and the `log p` amplitude. Block factorization does not repair that derivative-level loss.

**Möbius or primitive inversion.** One can apply a signed arithmetic inversion to a divisor-closed quantity such as (24) to recover more selective arithmetic information. That adds exactly the signed selector whose independent geometric origin is at issue; it is not positivity supplied by the determinant line.

**A genuinely new determinant line remains open.** A multivariate resultant, determinant of a source-forced correspondence complex, analytic/Quillen metric, or finite--archimedean determinant formed only after introducing new incidence can evade (2) and (6). Such a construction would be new structure in precisely the sense required by `WP-155`; it cannot be justified merely by grouping the existing cyclotomic factors.

## 7. Prior art and novelty audit

No new theorem about resultants, discriminants, or cyclotomic fields is claimed. The root-product definition and multiplicativity of the univariate resultant are classical elimination theory; the product formula (6) for discriminants is the standard squared-Vandermonde identity. Tom M. Apostol's *Resultants of cyclotomic polynomials*, Proc. Amer. Math. Soc. **24** (1970), 457--462, DOI `10.1090/S0002-9939-1970-0251010-X`, supplies the cyclotomic pairwise support law already used throughout the branch. The cyclotomic discriminant formula (16) is classical algebraic number theory; standard references include Lawrence C. Washington, *Introduction to Cyclotomic Fields*, GTM 83, Springer. The factorization `z^N-1=prod_{d|N} Phi_d` is elementary cyclotomy.

The novelty audit also searched for a known RH/Weil-positivity mechanism based specifically on cyclotomic block discriminants or resultants. The nearby literature found is ordinary resultant/discriminant theory and cyclotomic arithmetic, not an independent global Weil sign theorem. This is consistent with the branch's existing prior-art boundary: successful Weil/cohomological mechanisms use genuinely global correspondences or compressed global operators rather than merely multiplying local cyclotomic factors.

The durable Mathia-specific content is the exact synthesis

\[
\boxed{
\begin{aligned}
&\log|\operatorname{Res}(F_A,F_B)|
=\sum_{A\times B} I_{m,n},\\
&\log|\operatorname{Disc}F_S|
=\sum_S d_n+2\sum_{\binom S2}I_{m,n},\\
&\Delta_a\Delta_b\Delta_c\log|\operatorname{Disc}F_S|=0,\\
&\frac1{\varphi(n)}\log|\operatorname{Disc}\Phi_n|
\text{ is prime-coordinate additive},\\
&\frac1N\log|\operatorname{Disc}(z^N-1)|=\log N.
\end{aligned}
}
\tag{26}
\]

These identities close a concrete escape left by `WP-155`: **canonical univariate block multiplication does not create the missing mixed-prime incidence before positivity.**

## Consequence for the research line

The determinant-line/higher-cohomological frontier should no longer spend effort merely replacing individual primitive shells by products of their cyclotomic polynomials and then taking ordinary univariate resultants or discriminants. At the logarithmic level relevant to the finite Weil coefficients, that construction factorizes exactly back to self terms plus the old pairwise resultant kernel, whose normalized polarization already has unbounded two-sided sign.

The next viable candidate must change something upstream of this factorization: introduce a source-forced correspondence with genuinely non-pairwise or finite--archimedean incidence, a nonmultiplicative analytic metric/domain, or a different cohomological object on which positivity acts before the old cyclotomic product decomposition becomes the whole story. Merely making the polynomial block larger does not create the missing global geometry.