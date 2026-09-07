# PC-209 — cyclotomic-weighted power cover is a universal pure shift

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the simplest source-forced noncommuting shell/refinement operator left open by PC-207--PC-208: keep the cyclotomic shell multiplier and the circle power-map pullback together as one operator before taking any scalar trace, determinant, Mellin transform, or boundary evaluation.

PC-207--PC-208 show that fixed finite Fourier-leg Hardy lifts remain separated multipliers. The current Prime-Circle frontier therefore asks for a relation that couples shell data to refinement **before** that separated stage. There is a canonical candidate requiring no added kernel: the shell polynomial `Phi_n(z)` and the power map `z -> z^n` already belong to the original roots-of-unity geometry. On `H^2(D)` define

\[
(C_n f)(z)=f(z^n),
\qquad
W_n:=M_{\Phi_n}C_n,
\qquad n\ge2.
\tag{1}
\]

Thus

\[
(W_nf)(z)=\Phi_n(z)f(z^n).
\tag{2}
\]

This is genuinely pre-contraction and noncommuting: in general `C_n M_g = M_{g(z^n)}C_n`, so the shell multiplier cannot simply be moved through the covering without changing its scale. Nevertheless, the same-level operator (2) collapses much more strongly than a scalar observable does. After one intrinsic scalar normalization it is a **pure isometry of countably infinite multiplicity for every `n>=2`**. By the Wold--von Neumann theorem all such normalized operators are unitarily equivalent. Before normalization, the complete abstract operator class retains only the single coefficient-energy scalar `||Phi_n||_2`.

In particular, odd primes `p`, all prime powers `p^r`, and the controls `2p^r` have the same operator class at fixed `p`. The noncommuting weighted-cover architecture therefore does not distinguish a prime from its prime-power or doubled-prime controls and cannot by itself supply a new RH spectral mechanism.

## 1. The primitive shell fits inside one covering block

Write

\[
\Phi_n(z)=\sum_{j=0}^{d_n}a_{n,j}z^j,
\qquad
d_n=\varphi(n),
\tag{3}
\]

and put

\[
h_n:=\|\Phi_n\|_{H^2}^2
=\sum_{j=0}^{d_n}|a_{n,j}|^2.
\tag{4}
\]

For every `n>=2`,

\[
1\le d_n=\varphi(n)\le n-1.
\tag{5}
\]

Hence on the standard Hardy basis `e_k(z)=z^k`,

\[
W_ne_k
=z^{nk}\Phi_n(z)
=\sum_{j=0}^{d_n}a_{n,j}z^{nk+j}
\tag{6}
\]

is supported entirely in the length-`n` block

\[
B_k:=\operatorname{span}\{z^{nk},z^{nk+1},\ldots,z^{nk+n-1}\}.
\tag{7}
\]

Different `B_k` are mutually orthogonal. Therefore

\[
\langle W_ne_k,W_ne_\ell\rangle
=h_n\,\delta_{k\ell}
\tag{8}
\]

and, on all of `H^2`,

\[
\boxed{W_n^*W_n=h_n I.}
\tag{9}
\]

Thus

\[
\boxed{V_n:=h_n^{-1/2}W_n}
\tag{10}
\]

is an isometry. No averaging, large-`n` limit, or spectral wrapper has been used: equation (9) follows simply because the exact cyclotomic degree is strictly smaller than the exact covering degree.

This already provides a matched nonarithmetic control. The same scaled-isometry identity holds for **any** polynomial `P` of degree `<n` in place of `Phi_n`, with `h_n` replaced by the squared coefficient norm of `P`. The isometric architecture therefore comes from block geometry, not from primality.

## 2. Every cyclotomic-weighted covering is pure

The possible escape from (9) would be a nontrivial unitary part whose structure depends on `n`. It does not occur.

Iterating (10) gives

\[
V_n^r f(z)
=h_n^{-r/2}G_{n,r}(z)f(z^{n^r}),
\tag{11}
\]

where

\[
G_{n,r}(z)
:=\prod_{q=0}^{r-1}\Phi_n\!\left(z^{n^q}\right).
\tag{12}
\]

Its degree is

\[
D_{n,r}
=\varphi(n)\sum_{q=0}^{r-1}n^q
=\varphi(n)\frac{n^r-1}{n-1}
\le n^r-1.
\tag{13}
\]

Consequently `V_n^r e_k` lies entirely in the `n^r`-block

\[
\operatorname{span}\{z^{n^rk},\ldots,z^{n^r(k+1)-1}\},
\tag{14}
\]

and there is again exactly one range vector per block.

To identify the Wold unitary part, fix a monomial `z^ell`. Once `n^q>ell`, every nonconstant term of `Phi_n(z^{n^q})` has degree greater than `ell`. Hence the coefficient

\[
[z^\ell]G_{n,r}
\tag{15}
\]

stabilizes for all sufficiently large `r`. On the other hand `Phi_n` is monic of positive degree and has constant term `1` for `n>1`, so

\[
h_n\ge2.
\tag{16}
\]

The projection of a fixed basis vector onto `V_n^rH^2` is therefore bounded by a constant depending on `ell` times `h_n^{-r/2}`, and tends to zero as `r -> infinity`. Since the subspaces `V_n^rH^2` decrease with `r`, their projections converge strongly to the projection onto their intersection. They vanish on every monomial, hence by density

\[
\boxed{\bigcap_{r\ge0}V_n^rH^2=\{0\}.}
\tag{17}
\]

So `V_n` is a pure isometry.

## 3. The wandering multiplicity is always countably infinite

Equation (7) also determines the defect space exactly enough for unitary classification. The range of `V_n` contains one normalized vector in each `n`-dimensional block `B_k`. Therefore

\[
B_k\ominus V_nH^2
\]

has dimension `n-1` inside each block, and

\[
\ker V_n^*
=H^2\ominus V_nH^2
=\bigoplus_{k\ge0}\left(B_k\ominus\operatorname{span}\{z^{nk}\Phi_n\}\right).
\tag{18}
\]

Thus

\[
\boxed{\dim\ker V_n^*=\aleph_0}
\qquad(n\ge2).
\tag{19}
\]

The Wold--von Neumann decomposition now gives the complete abstract unitary class:

\[
\boxed{V_n\simeq S^{(\aleph_0)}\quad\text{for every }n\ge2,}
\tag{20}
\]

where `S` is the unilateral shift. Equivalently,

\[
\boxed{W_n\simeq \sqrt{h_n}\,S^{(\aleph_0)}.}
\tag{21}
\]

This is a full-operator statement, not a trace or determinant collapse. Once the canonical shell-cover operator is viewed up to unitary equivalence, all detailed primitive-root placement, all cyclotomic coefficients except their total square norm, and the covering degree itself disappear.

In particular

\[
\boxed{\operatorname{Spec}(W_n)=\{\lambda:|\lambda|\le\sqrt{h_n}\}.}
\tag{22}
\]

The spectrum is a disk, not a discrete divisor. The resolvent cannot be compact: if `(lambda I-W_n)^{-1}` were compact for a resolvent point, multiplication by the bounded operator `lambda I-W_n` would make the identity compact on infinite-dimensional `H^2`.

## 4. Prime, prime-power, and doubled-prime controls coincide

The one scalar surviving in (21) is itself too coarse to provide the desired prime discriminator.

For a prime `p` and `r>=1`,

\[
\Phi_{p^r}(z)
=1+z^{p^{r-1}}+\cdots+z^{(p-1)p^{r-1}},
\tag{23}
\]

so

\[
\boxed{h_{p^r}=p.}
\tag{24}
\]

Therefore every prime-power level on the same prime ray has exactly the same abstract operator class:

\[
\boxed{W_{p^r}\simeq \sqrt p\,S^{(\aleph_0)}
\quad(r\ge1).}
\tag{25}
\]

For odd `p`, the classical identity

\[
\Phi_{2p^r}(z)=\Phi_{p^r}(-z)
\tag{26}
\]

preserves coefficient squares, hence

\[
\boxed{h_{2p^r}=h_{p^r}=p}
\tag{27}
\]

and consequently

\[
\boxed{W_{2p^r}\simeq W_{p^r}.}
\tag{28}
\]

Thus even the **unnormalized** full weighted-composition operator cannot distinguish the prime level `p` from the composite level `2p`, or `p^r` from `2p^r`. This is stronger than observing that one chosen scalar statistic agrees: equations (21) and (28) identify the entire operators up to unitary equivalence.

For general composite `n`, `h_n` can vary because cyclotomic coefficient energy varies. But it remains only the ordinary finite coefficient `L^2` norm of `Phi_n`. Parseval identifies it with the boundary `L^2` norm of the cyclotomic polynomial, so it is a classical polynomial norm rather than a new spectral parameter.

## 5. Relation to the earlier Prime-Circle closures

This result addresses a different boundary from PC-200 and PC-207--PC-208.

PC-200 inserts power maps between already scalar character packets and then contracts angularly; the off-diagonal Fourier relation collapses to one rational ray. Here no angular contraction occurs at all. The shell multiplier and covering pullback remain together as the noncommuting operator `M_{Phi_n}C_n`, and the collapse is instead an exact Hardy block/Wold classification.

PC-207--PC-208 retain finitely many independent Fourier legs but obtain separated multiplication operators. Equation (2) is not a multiplication operator and is not coordinate-separable in that sense: it actively moves every Hardy mode from `k` to an `n`-adic block while multiplying by the complete shell polynomial. The fact that it nevertheless becomes the universal shift (20) therefore closes one of the most canonical **source-forced noncommuting shell/refinement** repairs explicitly left open by those findings.

PC-010 and PC-064 remain the relevant large-scale novelty warnings: the abstract roots-of-unity refinement tower is already Bost--Connes/cyclotomic dynamics, and its compatible inverse limit is the adelic solenoid. PC-209 does not replace those results. It says that decorating one canonical power-cover step by the exact primitive-shell polynomial still does not create a new spectral species before one reaches a more structured cross-level construction.

## 6. Prior-art and novelty audit

Every abstract operator ingredient is classical. Weighted composition operators `M_g C_phi` on Hardy spaces are a standard operator-theory class. The Wold--von Neumann theorem classifies an isometry as a direct sum of a unitary part and unilateral shifts; in particular a pure isometry is classified by its wandering multiplicity. A modern explicit statement is Theorem 2.1 in the literature on Wold decompositions for isometries, while standard operator texts give the classical theorem. Nordgren's classical composition-operator result that an inner symbol fixing zero induces an `H^2` isometry is neighboring background for the unweighted map `C_n`, although equation (9) here is proved directly from coefficient blocks and does not rely on it.

The cyclotomic identities (23) and (26), and the coefficient norm `h_n`, are classical. Norms of cyclotomic polynomials on the unit circle are an established subject; for example Borwein--Choi--Ferguson, *Norms of cyclotomic Littlewood polynomials*, Math. Proc. Cambridge Philos. Soc. 138 (2005), 315--326, studies cyclotomic boundary norms, and related work treats broader `L^q` behavior. No novelty is claimed for Wold decomposition, weighted composition operators, cyclotomic coefficient norms, or those identities.

A directed search of weighted-composition, composition-operator, Wold, and cyclotomic-norm literature did not reveal an RH mechanism attached to the specific source pairing `Phi_n(z) f(z^n)`. More importantly, the project-local negative conclusion does not rest on absence of literature: equations (9), (17), (19), and (21) give an exact unitary classification.

The durable Prime-Circle contribution is therefore the **boundary statement**: the most direct noncommuting operator obtained by decorating the intrinsic `n`-fold power covering with its intrinsic primitive-shell polynomial has no hidden operator spectrum beyond one classical coefficient-energy scalar, and even that scalar fails the prime-versus-`2p` and prime-power controls.

## 7. Falsification controls and surviving frontier

The theorem is intentionally not an all-purpose no-go for shell/refinement transfer.

It uses the same-level weighted cover

\[
f(z)\mapsto\Phi_n(z)f(z^n)
\tag{29}
\]

and its abstract unitary invariants. It does **not** classify operators where the covering degree and shell conductor are different in a way that makes the shell degree overlap several covering blocks; adjoints or transfer averages interleaved with shell multipliers; old/new incidence weights that couple several fibers; matrix-valued or nonlinear weights; cross-level products whose state is retained jointly rather than compressed to one weighted composition operator; or a genuinely infinite-depth algebra before unitary quotient. The canonical covariance

\[
C_mM_g=M_{g(z^m)}C_m
\tag{30}
\]

also shows why reversing or interleaving these operations changes the shell scale and can leave the present theorem.

Likewise, unitary equivalence deliberately forgets the distinguished monomial/cyclotomic coordinate algebra. A candidate whose observable is the **pair** `(W_n, diagonal/source algebra)` rather than the abstract operator `W_n` is not ruled out, but it must demonstrate that the retained extra algebra is itself forced by Prime-Circle geometry and that its invariants survive the matched composite controls rather than simply re-encoding `Phi_n`.

Global uniformization/monodromy is untouched.

## Research consequence

The phrase "source-forced noncommuting state" in the current frontier needs one refinement. Noncommutativity produced merely by combining the exact shell polynomial with its same-level power-cover pullback is not enough:

\[
\boxed{
\Phi_n(z)\times(z\mapsto z^n)
\;\longrightarrow\;
M_{\Phi_n}C_n
\;\simeq\;
\sqrt{h_n}\,S^{(\aleph_0)}.
}
\tag{31}
\]

A viable shell/refinement operator must therefore retain structure destroyed by this Wold collapse: genuinely cross-level/fiber-coupled transfer, a nontrivial source algebra together with the operator, growing/infinite-depth relations before unitary classification, or another intrinsic nonseparable mechanism. The canonical same-level weighted cover itself is a decisive negative rather than a new route to RH.
