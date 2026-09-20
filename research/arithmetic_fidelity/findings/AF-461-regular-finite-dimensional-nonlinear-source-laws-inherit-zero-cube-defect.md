# AF-461 — Regular finite-dimensional nonlinear source laws inherit zero cube defect

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-LAW`, `COMPLETED-SECANT`, `NONLINEAR-SOURCE`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-460 shows that the normalized kernel of any bounded finite-rank linear source law on an infinite atomic `ell^1` source space has zero paired-cube completion defect. Nonlinearity by itself does not escape that obstruction at a regular interior fiber: a smooth finite-dimensional source law has the same tangent kernel to first order, and a regular level-set chart realizes every tangent direction by genuine same-fiber secants.

Let `A` be an infinite alphabet and

\[
X=\ell^1_0(A)
=\left\{h\in\ell^1(A):\sum_{a\in A}h(a)=0\right\}.
\tag{1}
\]

Let `U subset X` be open, let `E` be finite dimensional, and let

\[
G:U\to E
\tag{2}
\]

be `C^1`. Fix `x_0 in U` and assume that

\[
L:=DG(x_0):X\to E
\tag{3}
\]

is surjective. For any neighborhood `W subset U` of `x_0`, define the normalized local same-fiber carrier

\[
C_W(G,x_0)
=
\left\{
\frac{x-x_0}{\|x-x_0\|_1}:
 x\in W,\ x\ne x_0,\ G(x)=G(x_0)
\right\}.
\tag{4}
\]

Then for every fixed `k>=1`, using the AF-459 cube-defect functional,

\[
\boxed{D_k\bigl(C_W(G,x_0)\bigr)=0.}
\tag{5}
\]

More strongly, for every `epsilon>0` there is one paired block `B` of `2k` distinct atoms such that every sign orientation of its ideal paired cube is `epsilon`-close in `ell^1` to an actual normalized secant of the nonlinear level set:

\[
\boxed{
\sup_{\varepsilon\in\{-1,+1\}^k}
\operatorname{dist}_1
\bigl(q^B_\varepsilon,C_W(G,x_0)\bigr)
<\epsilon.
}
\tag{6}
\]

Thus **regular finite-dimensional nonlinear curvature does not create the positive cube defect required to protect uniform TV fidelity**. At every regular point of an open Banach source model, the local physical question reduces to the finite-rank tangent kernel already ruled out by AF-460.

The statement extends immediately to any physical completed-secant carrier `C` satisfying

\[
\overline{C_W(G,x_0)}\subseteq\overline C
\tag{7}
\]

for one such regular local fiber. Then `D_k(C)=0` for every `k`. Consequently, if a bounded affine observation takes values in a Banach space of Rademacher type `p>1`, AF-459 again forces zero complexity-independent lower TV gain.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{a finite-dimensional nonlinear source law can protect bounded affine TV fidelity only through genuinely nonregular or non-tangent-complete structure, not through smooth regular curvature alone.}
}
\tag{8}
\]

In particular, the nonlinear escape left open by AF-460 narrows to singular fibers, positivity or boundary restrictions, hard support constraints, infinite-dimensional source laws, failure of local tangent completion, a different source metric, or another mechanism that invalidates the regular-level-set reduction.

## Exact derivation

Because `E` is finite dimensional and `L` is surjective, `K=ker L` is complemented in `X`. Equivalently, choose a bounded linear right inverse

\[
R:E\to X,
\qquad LR=I_E,
\tag{9}
\]

and write

\[
X=K\oplus R(E).
\tag{10}
\]

The Banach implicit-function/submersion theorem therefore gives a neighborhood `V subset K` of `0` and a `C^1` map

\[
g:V\to R(E)
\tag{11}
\]

with

\[
g(0)=0,
\qquad
Dg(0)=0,
\tag{12}
\]

such that, after shrinking if necessary, the level set through `x_0` is parametrized by

\[
\chi(v)=x_0+v+g(v),
\qquad
G(\chi(v))=G(x_0).
\tag{13}
\]

Fix a unit vector `v in K`. For sufficiently small nonzero `t`, `tv in V`, `chi(tv) in W`, and

\[
\chi(tv)-x_0
=t v+g(tv)
=t v+o(|t|)
\quad\text{in }\ell^1.
\tag{14}
\]

Hence

\[
\frac{\chi(tv)-x_0}{\|\chi(tv)-x_0\|_1}
\longrightarrow
\operatorname{sgn}(t)v.
\tag{15}
\]

Therefore the entire unit sphere of the tangent kernel lies in the closure of every local same-fiber carrier:

\[
\boxed{
\{v\in\ker L:\|v\|_1=1\}
\subseteq
\overline{C_W(G,x_0)}.
}
\tag{16}
\]

AF-460 applies to the bounded finite-rank operator `L` and says that for every `k` and every `delta>0` there is one paired block `B` such that all `2^k` ideal cube orientations lie within `delta` of the unit sphere of `ker L`.

For each sign orientation choose a unit `v_epsilon in ker L` with

\[
\|q^B_\varepsilon-v_\varepsilon\|_1<\delta.
\tag{17}
\]

By `(16)`, and because there are only finitely many sign orientations, choose actual normalized local secants `c_epsilon in C_W(G,x_0)` such that

\[
\|c_\varepsilon-v_\varepsilon\|_1<\delta
\tag{18}
\]

simultaneously for all signs. Then

\[
\|q^B_\varepsilon-c_\varepsilon\|_1<2\delta
\tag{19}
\]

for every sign vector. Taking `delta<epsilon/2` proves `(6)`, and therefore `(5)`.

No second-order estimate is used. The only nonlinear input is that a regular `C^1` level set has tangent space `ker DG(x_0)` and realizes those tangent directions by actual nearby fiber points. Curvature contributes only the `o(|t|)` term in `(14)`, which disappears after normalization.

## Consequence for bounded affine observations

Let `C` be any normalized physical completed-secant carrier whose closure contains the local regular-fiber carrier above. Let

\[
\phi:A\to Y,
\qquad
\sup_a\|\phi(a)\|_Y\le M,
\tag{20}
\]

where `Y` has Rademacher type `p>1`. AF-459 gives

\[
\kappa_C(F_\phi)
\le
M\left[T_p(Y)k^{1/p-1}+D_k(C)\right].
\tag{21}
\]

Since `(5)` and `(7)` imply `D_k(C)=0` for every `k`,

\[
\kappa_C(F_\phi)
\le
M T_p(Y)k^{1/p-1}.
\tag{22}
\]

Letting `k to infinity` yields

\[
\boxed{\kappa_C(F_\phi)=0.}
\tag{23}
\]

So replacing finitely many bounded linear source statistics by finitely many smooth nonlinear statistics does not rescue uniform TV fidelity at a regular tangent-complete fiber. The source law must obtain its protection from something that changes the feasible secant geometry itself.

## Prior art and novelty audit

The differential-geometric ingredient is classical, and this finding makes **no novelty claim** for it.

- Jinpeng An and Karl-Hermann Neeb, **“An implicit function theorem for Banach spaces and some applications,”** *Mathematische Zeitschrift* 262 (2009), 627–643, DOI `10.1007/s00209-008-0394-6`. The paper develops Banach-space implicit-function results and explicitly applies them to parametrization of fibers of differentiable maps.
- Tobias Diez and Gerd Rudolph, **“Normal form of equivariant maps in infinite dimensions,”** *Annals of Global Analysis and Geometry* 61 (2022), 159–213, DOI `10.1007/s10455-021-09777-2`. Their normal-form results recover the submersion and constant-rank theorems for maps with finite-dimensional target; the finite-dimensional-target splitting used here is a standard special case.
- AF-007 already records the regular smooth fact that vertical directions are `ker dT` and control infinitesimal information loss. AF-086 separately shows that tangent-direction coverage is the right local resource for restricted-domain fidelity. AF-461 does not replace either result: it specializes regular level-set geometry to the AF-459/AF-460 paired-cube obstruction in `ell^1` source space.
- AF-460 supplies the nontrivial source-side input `D_k(S_{ker L})=0`. AF-461 only proves that a regular nonlinear fiber has normalized secants dense enough to inherit that exact cube defect.

A fresh prior-art search found the classical Banach implicit/submersion framework above but no need for a new nonlinear-manifold theorem: the line-specific conclusion follows by composing that standard local normal form with AF-460. Accordingly the result is classified as a derived obstruction, not as a novel differential-geometric theorem.

## Boundary and falsification audit

- **Regularity is essential.** At a singular point the derivative kernel can dramatically overstate the actual fiber. On real `X=ell^1_0(A)`, the smooth scalar map
  \[
  G(h)=\sum_{a\in A}h(a)^2
  \tag{24}
  \]
  satisfies `DG(0)=0`, so its derivative kernel is all of `X`, while `G^{-1}(0)={0}`. There are no nonzero same-fiber secants at the origin. Thus one cannot apply AF-460 to `DG(x_0)` at singular points without an independent tangent-completion theorem.
- **Open-domain/interior geometry is essential to the automatic submersion conclusion.** The infinite probability simplex has empty `ell^1` interior. A positive source-law fiber may sit on a face or boundary where many algebraic tangent directions cannot be completed by physical probability laws. In that setting `(16)` must be proved from the actual feasible carrier rather than imported from the ambient signed space.
- **Hard support budgets can block the local chart.** Even when the unconstrained level set is a regular submanifold, intersecting it with an `r`-sparse model is not an open Banach constraint and may remove most tangent directions.
- **Finite-dimensional codomain is substantive.** AF-460's clustering/splitting argument need not hold for an infinite-dimensional derivative range.
- **The source metric is TV / `ell^1`.** Different normalizations can change both tangent approximation and the relevant cube defect.
- **No converse is claimed.** Singularity, boundary geometry, infinite-dimensional source laws, or support restrictions merely escape this no-go theorem; they do not automatically provide positive fidelity.

## Arithmetic specialization

Suppose an arithmetic source family is locally described by finitely many `C^1` constraints or statistics

\[
G=(G_1,\ldots,G_q)
\tag{25}
\]

on an infinite atomic `ell^1` source model. If the arithmetic point lies on a regular fiber and the physically admissible completed secants realize the local fiber directions, then the nonlinear source law inherits `D_k=0` at every finite cube scale. Therefore bounded affine compression into Hilbert space, or more generally into any target of Rademacher type `p>1`, cannot retain a complexity-independent TV discriminator there.

For a rational-prime application this sharpens the source-side frontier again. It is not enough to say that primality is encoded by finitely many nonlinear relations. The candidate protection must be traced to a **singular, boundary, support-restricted, infinite-dimensional, unbounded, or otherwise tangent-incomplete arithmetic mechanism**. If the putative prime law is regular and its local same-law secants realize the full finite-codimensional tangent kernel, smooth nonlinearity has not preserved the discriminator; it has only curved a source carrier whose normalized small-scale geometry is already fatal.