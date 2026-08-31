# WP-061 — the `q=2` Hardy Gram is positive, but the selected full-root `q=2` channel is indefinite

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE` + `DECISIVE-BOUNDARY` + `CLASSICAL-MECHANISM`. The Hilbert-space Gram argument is standard operator geometry; the durable content here is its exact Prime-Circle specialization and the operator-level comparison with the independently selected full-root `q=2` archimedean channel of `WP-048`. No theorem-level historical novelty is claimed for Gram positivity, Hilbert matrices, or trace ideals.

`PC-082` exposes a tempting route left open by `WP-051`: the order-two Hardy shell is positive, and inserting it between two arithmetic shell operators produces a positive three-factor energy. Since `WP-048` independently selects the root-tower level `q=2` as the Riemann archimedean channel, one might hope that this gives a single Mathia-native positive object coupling finite shell arithmetic to the Gamma sector.

The first half of that hope is real. The primitive order-two shell gives a canonical positive cross-shell Gram kernel on every other Hardy shell. But the second half fails exactly: the object selected by `WP-048` is the **full-root** field

\[
V_2(z)=\Log(1-z^2),
\]

not the primitive antipodal field alone. In the same Hardy realization its operator is

\[
\Gamma_1+\Gamma_2=-H+DHD,
\]

and this operator is already indefinite on the two-dimensional span of `e_0,e_1`. Moreover, the positive `Gamma_2` sandwich has strictly positive diagonal on **every** non-`2` shell, including shells where the canonical mixed-Hardy Mangoldt readout vanishes. Thus the positive primitive shell is a genuine new information carrier for this line, but it is not by itself the full-root archimedean channel and its direct shell energy does not preserve Weil finite-place locality.

## 1. The primitive order-two shell gives a genuine positive cross-shell Gram

`PC-075` defines the cyclotomic Hardy shell operators

\[
(\Gamma_n)_{jk}
=-\frac{c_n(j+k+1)}{j+k+1},
\qquad j,k\ge0.
\tag{1}
\]

With the natural base-shell convention used in `PC-080`,

\[
\Gamma_1=-H,
\qquad
H_{jk}=\frac1{j+k+1}.
\tag{2}
\]

For `n=2`, `c_2(r)=(-1)^r`. If

\[
D e_j=(-1)^j e_j,
\tag{3}
\]

then (1) gives exactly

\[
\boxed{\Gamma_2=DHD.}
\tag{4}
\]

The Hilbert matrix is positive because `H=B^*B` for the bounded monomial map

\[
Be_j(x)=x^j,
\qquad 0<x<1.
\tag{5}
\]

It is also injective: if `Bx=0` almost everywhere, the analytic power series `sum_j x_j z^j` vanishes on an interval and hence all coefficients vanish. Since `D` is unitary and self-adjoint,

\[
\boxed{\Gamma_2\succ0}
\tag{6}
\]

in the sense of a positive bounded operator with trivial kernel.

Now let `n != 2`. `PC-080` proves

\[
\Gamma_2\Gamma_n\in\mathcal S_1.
\tag{7}
\]

Therefore

\[
\Gamma_n\Gamma_2\Gamma_n
=\Gamma_n(\Gamma_2\Gamma_n)
\in\mathcal S_1,
\tag{8}
\]

and it is positive. Equivalently,

\[
X_n:=\Gamma_2^{1/2}\Gamma_n\in\mathcal S_2,
\qquad
X_n^*X_n=\Gamma_n\Gamma_2\Gamma_n.
\tag{9}
\]

For `m,n != 2` define

\[
\boxed{
K_2(m,n)
:=\operatorname{Tr}(\Gamma_m\Gamma_2\Gamma_n)
=\langle X_m,X_n\rangle_{\mathcal S_2}.
}
\tag{10}
\]

Hence every finite coefficient family satisfies the exact Gram identity

\[
\boxed{
\sum_{m,n}\overline{a_m}a_nK_2(m,n)
=\left\|\sum_n a_nX_n\right\|_{\mathcal S_2}^2
\ge0.
}
\tag{11}
\]

This is an unconditional, intrinsic cross-shell positive form. It uses no zeta zeros, analytic continuation, fitted kernel, or RH-equivalent positivity criterion. `PC-082` proved the concrete control `Tr(Gamma_3 Gamma_2 Gamma_3)>0`; (10)--(11) show that this is one diagonal entry of a canonical positive kernel on the whole separated shell family.

The diagonal is in fact strictly positive for every `n != 2`. For `n>1`,

\[
(\Gamma_n)_{n-1,0}
=-\frac{c_n(n)}n
=-\frac{\varphi(n)}n\ne0,
\tag{12}
\]

and `Gamma_1=-H` is also nonzero. Because `Gamma_2^{1/2}` is injective,

\[
X_n\ne0.
\]

Consequently

\[
\boxed{
K_2(n,n)
=\|\Gamma_2^{1/2}\Gamma_n\|_{\mathcal S_2}^2
>0
\qquad(n\ne2).
}
\tag{13}
\]

## 2. Positivity destroys the sparse first-trace shell support

The same Hardy algebra has a much sharper **signed linear** arithmetic readout. `PC-080` proves

\[
\boxed{
-\operatorname{Tr}(\Gamma_1\Gamma_n)=\Lambda(n)
\qquad(n>1).
}
\tag{14}
\]

More generally, the first mixed trace between distinct primitive shells is minus the logarithm of their cyclotomic resultant and is nonzero only across prime-power scale jumps.

Equation (13) behaves completely differently. It gives positive mass to every separated shell. In particular,

\[
K_2(6,6)>0,
\qquad
\Lambda(6)=0.
\tag{15}
\]

Already the smallest control from `PC-082` shows the same mechanism in another form:

\[
\operatorname{Tr}(\Gamma_2\Gamma_3)=0,
\qquad
\operatorname{Tr}(\Gamma_3\Gamma_2\Gamma_3)>0.
\tag{16}
\]

Thus insertion of the positive shell and passage to the Hilbert-Schmidt norm **escapes** the pairwise resultant graph, but it does so by filling in support rather than by retaining the von-Mangoldt selector.

This does not prove that every nonlocal use of `K_2` is incompatible with the Weil form. A positive kernel may acquire cancellations after a nontrivial map from Weil test functions into its feature space. What (13)--(16) rule out is the direct interpretation of the positive shell diagonal as the finite Weil coefficient measure or as a positive shell-by-shell replacement for (14).

There is also a strong matched control. The sign in (11) is generic: for any bounded self-adjoint family `A_n`, any positive operator `P`, and any domain on which `P^{1/2}A_n` are Hilbert-Schmidt,

\[
\operatorname{Tr}(A_m P A_n)
\]

is a positive Gram kernel. Therefore the **positivity theorem itself is not arithmetic**. The arithmetic content must come from an additional exact identification of the feature map and its scalar readout with the global explicit formula.

## 3. The `q=2` object selected by the archimedean mechanism is not `Gamma_2`

`WP-048` independently selects the full-root level

\[
V_2(z)=\Log(1-z^2)
\tag{17}
\]

because its singular set `mu_2={1,-1}` is the fixed locus of the canonical anchored reflection and the antipode is the unique nontrivial cycle-energy extremum. `WP-048` already warns that the full-root/primitive distinction matters: `V_2` contains both the common anchor and the primitive antipode.

The Hardy realization makes that distinction exact at operator level. Inside the disk,

\[
\Log(1-z^2)
=\Log(1-z)+\Log(1+z).
\tag{18}
\]

The first term has Taylor coefficients `-1/r` and hence Hardy operator `Gamma_1=-H`. The second has coefficients `(-1)^{r+1}/r` and hence Hardy operator `Gamma_2=DHD`. By linearity of the Hardy off-diagonal block, the selected full-root channel is therefore

\[
\boxed{
\mathcal F_2
:=\Gamma[V_2]
=\Gamma_1+\Gamma_2
=-H+DHD.
}
\tag{19}
\]

This operator is not positive. Split

\[
\ell^2=\mathcal H_{\rm even}\oplus\mathcal H_{\rm odd}
\]

and write

\[
H=
\begin{pmatrix}
H_{ee}&H_{eo}\\
H_{oe}&H_{oo}
\end{pmatrix},
\qquad
D=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix}.
\tag{20}
\]

Then

\[
\boxed{
\mathcal F_2
=
\begin{pmatrix}
0&-2H_{eo}\\
-2H_{oe}&0
\end{pmatrix}.
}
\tag{21}
\]

The cross block is nonzero; for example `H_{01}=1/2`. On the two explicit vectors

\[
u_+=e_0+e_1,
\qquad
u_-=e_0-e_1,
\]

one obtains

\[
\boxed{
\langle u_+,\mathcal F_2u_+\rangle=-2,
\qquad
\langle u_-,\mathcal F_2u_-\rangle=+2.
}
\tag{22}
\]

Hence

\[
\boxed{\mathcal F_2\text{ is indefinite}.}
\tag{23}
\]

This failure occurs before the Mellin extraction used in `WP-036`/`WP-048`. The primitive antipodal shell `Gamma_2` is positive, but the actual full-root level whose radial Mellin diagonal yields the Riemann Gamma response is not.

## 4. The tempting positive archimedean identification is therefore pinched

The exact alternatives are now:

\[
\begin{array}{ccl}
\text{primitive antipode} &:& \Gamma_2=DHD\succ0,\\[2mm]
\text{full selected root level} &:& \Gamma_1+\Gamma_2=-H+DHD\text{ indefinite}.
\end{array}
\tag{24}
\]

Using `Gamma_2` alone preserves a genuine positive theorem and gives the cross-shell Gram (11), but it drops the anchor contribution which `WP-048` explicitly says is part of the full-root `q=2` channel. Keeping the full-root object preserves the exact selected radial field but loses positivity.

The simplest apparent repair makes this transparent:

\[
\mathcal F_2+H=\Gamma_2.
\tag{25}
\]

So adding the positive Hilbert background does not prove positivity of the full-root channel; it literally removes the `Gamma_1=-H` anchor contribution and replaces the full-root field by its primitive antipodal part.

Even operations such as `|F_2|`, `F_2^2`, or a Gram sandwich can of course restore positivity, but they are nonlinear/even in the full-root operator. No identity presently shows that such an operation preserves the **linear** Mellin response producing

\[
\frac{d}{ds}\log\bigl(\pi^{-s/2}\Gamma(s/2)\bigr),
\]

or the signed finite translation term required by the Weil explicit formula. Treating those repairs as a global positivity mechanism without such an identity would repeat the absolute-value/squared-energy failure mode already encountered elsewhere in this line.

## 5. Prior-art and novelty audit

The functional-analytic ingredients here are classical. Positive Hilbert/Hankel operators, Hilbert-Schmidt Gram kernels, and trace-ideal cyclicity are standard operator theory. The literature search found no basis for claiming novelty for any of those mechanisms, and none is claimed.

The arithmetic input is likewise anchored in existing Mathia evidence rather than presented as a new classical theorem: `PC-080` identifies the first mixed Hardy trace with the cyclotomic resultant and von Mangoldt at the base shell, while `PC-082` establishes that higher separated cyclic traces contain richer cyclotomic-period data and supplies the concrete positive `3-2-3` control. The project-specific contribution of this finding is the exact synthesis with `WP-048`: the positive primitive `q=2` Hardy shell and the full-root `q=2` Gamma channel are **different operators**, and the latter is explicitly indefinite.

This also keeps the novelty boundary with classical Weil/Connes-style positivity clear. Equation (11) is an ordinary Hilbert-space Gram theorem, not a new explicit-formula trace or cohomological intersection theorem. It becomes relevant to the RH program only if a further canonical map makes the complete finite, archimedean, and polar terms emerge from the same operator identity.

## 6. Consequence for the research line

There is now a genuine Mathia-native positive cross-shell Hardy form:

\[
\boxed{
K_2(m,n)=\operatorname{Tr}(\Gamma_m\Gamma_2\Gamma_n)\succeq0
\quad(m,n\ne2).
}
\tag{26}
\]

So `WP-051`'s open cross-level escape is not empty. But the most tempting interpretation of that form is false in two independent exact ways:

1. its direct shell diagonal has full support rather than Mangoldt support; and
2. its positive anchor `Gamma_2` is only the primitive antipodal part of the selected `q=2` root level, whose full Hardy operator `Gamma_1+Gamma_2` is indefinite.

A surviving route must therefore couple the anchor and antipode **before** the sign theorem by something more structured than dropping `Gamma_1`, taking an absolute value, or reading shell diagonals. A concrete success criterion is now available: construct a canonical map from Weil test functions into a relative/graded/compressed Hardy space for which one operator identity simultaneously reproduces the sparse finite term of (14), the full-root `q=2` archimedean response of `WP-048`, and the polar counterterm, while nonnegativity follows independently from the geometry. Until that bridge is derived, the positive `q=2` Gram is an information carrier, not a global Weil-positive form.
