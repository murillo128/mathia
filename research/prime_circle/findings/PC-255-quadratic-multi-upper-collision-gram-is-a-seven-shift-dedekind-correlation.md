# PC-255 — quadratic multi-upper collision Gram is a seven-shift Dedekind correlation

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the simplest genuinely multi-upper coupling left open by PC-254. Fix distinct primes

\[
2<p<r<q,\qquad 2<p<r<s,
\]

and write

\[
D_q:=D_{p,r;q}=K_{p,q}^{*}K_{r,q}-qK_{p,r}^{T},
\qquad
D_s:=D_{p,r;s}.
\tag{1}
\]

PC-251 expresses each shared-upper defect as a weighted matching of lower path incidences, and PC-253 identifies its support with oriented modular-triangle data. The first natural way to couple *two different upper levels* is the Hilbert--Schmidt Gram entry

\[
\langle D_q,D_s\rangle_{\mathrm{HS}}
=\operatorname{tr}(D_q^{*}D_s).
\tag{2}
\]

This coupling still does not create a new nonlocal arithmetic carrier. After reindexing collisions by their determinant layer `h=ri-pj`, (2) is exactly a fixed seven-shift correlation of two scalar collision-weight sequences. The only shifts are

\[
0,\quad \pm p,\quad \pm r,\quad \pm(r-p).
\tag{3}
\]

Each scalar sequence is the piecewise-quadratic modular-residue function already implicit in PC-253. Consequently every entry of the multi-upper Hilbert--Schmidt Gram matrix is a finite generalized Dedekind/Rademacher-type weighted lattice sum. The quadratic multi-upper covariance route therefore classicalizes before any new zeta spectral parameter, functional equation, or critical normalization appears.

## 1. Determinant layers are a one-dimensional coordinate for the collision matching

For an upper level `q`, let `C_q=C_{p,r;q}` be the PC-251 collision set. A collision `(i,j)` has determinant layer

\[
h=ri-pj.
\tag{4}
\]

On the rectangle `1<=i<p`, `1<=j<r`, the map `(i,j) -> h` is injective: if two pairs have the same `h`, then

\[
r(i-i')=p(j-j'),
\]

so coprimality forces `i-i'=pt` and `j-j'=rt`, and the index ranges force `t=0`.

Let

\[
w_q(i,j)
=
pr\,G\!\left(\frac{a_i}{p},\frac{b_j}{r}\right)
\in\mathbb Z_{>0}
\tag{5}
\]

be the positive PC-251 collision weight. Define the scalar determinant-layer sequence

\[
c_q(h)=
\begin{cases}
w_q(i,j),& (i,j)\in C_q,\ h=ri-pj,\\
0,&\text{otherwise}.
\end{cases}
\tag{6}
\]

Reflection `(i,j) -> (p-i,r-j)` gives

\[
c_q(-h)=c_q(h),\qquad c_q(0)=0.
\tag{7}
\]

PC-253 also implies that every positive active layer satisfies `h<pr/q<p`, hence

\[
\operatorname{supp}c_q\subset\{-(p-1),\ldots,-1,1,\ldots,p-1\}.
\tag{8}
\]

If `delta_i^(p)=e_{i-1}-e_i` and `delta_j^(r)=e_{j-1}-e_j`, then PC-251 becomes simply

\[
\boxed{
D_q
=
-\sum_{h\in\mathbb Z}
c_q(h)\,
\delta_{i(h)}^{(p)}
\bigl(\delta_{j(h)}^{(r)}\bigr)^T,
}
\tag{9}
\]

where `i(h),j(h)` are the unique interior indices associated with an active determinant layer.

## 2. The two-upper Hilbert--Schmidt coupling has a fixed local stencil

The edge Gram matrix of a path is local:

\[
\left\langle \delta_i,\delta_{i'}\right\rangle
=
\alpha_{i'-i},
\qquad
\alpha_0=2,\quad
\alpha_{\pm1}=-1,\quad
\alpha_k=0\ (|k|>1).
\tag{10}
\]

Expanding (2) with (9),

\[
\langle D_q,D_s\rangle_{\mathrm{HS}}
=
\sum_{h,h'}
c_q(h)c_s(h')\,
\alpha_{i(h')-i(h)}
\alpha_{j(h')-j(h)}.
\tag{11}
\]

A nonzero term therefore has

\[
i(h')-i(h)=\varepsilon,\qquad
j(h')-j(h)=\eta,
\qquad
\varepsilon,\eta\in\{-1,0,1\}.
\tag{12}
\]

Using `h=ri-pj`,

\[
h'-h=r\varepsilon-p\eta.
\tag{13}
\]

Define the shifted scalar correlation

\[
C_{q,s}(d)
:=
\sum_{h\in\mathbb Z}c_q(h)c_s(h+d).
\tag{14}
\]

Equations (11)--(13) give the exact `3 x 3` incidence stencil

\[
\boxed{
\langle D_q,D_s\rangle_{\mathrm{HS}}
=
\sum_{\varepsilon,\eta=-1}^{1}
\alpha_\varepsilon\alpha_\eta\,
C_{q,s}(r\varepsilon-p\eta).
}
\tag{15}
\]

The two extreme shifts `+-(r+p)` vanish identically because of the compact support (8): their magnitude is larger than the diameter `2p-2` of that support. Hence

\[
\boxed{
\begin{aligned}
\langle D_q,D_s\rangle_{\mathrm{HS}}
={}&4C_{q,s}(0)\\
&-2\!\left[
C_{q,s}(p)+C_{q,s}(-p)
+C_{q,s}(r)+C_{q,s}(-r)
\right]\\
&+C_{q,s}(r-p)+C_{q,s}(p-r).
\end{aligned}}
\tag{16}
\]

Thus a quadratic coupling of two independent upper levels never sees an unrestricted two-matrix interaction. It sees only seven fixed translations of one scalar determinant-layer packet against the other.

For `q=s`, (16) gives the exact Frobenius norm of a single defect in terms of seven autocorrelations. For a finite set `Q` of upper levels, the complete Hilbert--Schmidt Gram matrix

\[
\Gamma_Q(q,s)=\langle D_q,D_s\rangle_{\mathrm{HS}}
\tag{17}
\]

is therefore determined entrywise by the same fixed seven-shift rule.

## 3. Each scalar packet is explicit modular-triangle data

PC-253 gives an exact closed form for the positive half of `c_q`. Put

\[
\ell_q\equiv-q r^{-1}\pmod p,
\qquad
y_q(h)=\langle \ell_q h\rangle_p\in\{1,\ldots,p-1\}.
\tag{18}
\]

For `1<=h<p`,

\[
\boxed{
c_q(h)
=
\frac{
y_q(h)\bigl(r(p-y_q(h))-qh\bigr)
}{p}\,
\mathbf 1_{\{qh+r\,y_q(h)<pr\}},
}
\tag{19}
\]

and `c_q(-h)=c_q(h)`.

Two consequences are immediate. First, for fixed `p,r`, the residue function `y_q(h)` depends on `q` only through `q mod p`. On a fixed residue class of `q`, every active weight (19) is affine in `q`, and activity changes only when `q` crosses one of the finitely many rational thresholds

\[
q=\frac{r(p-y_q(h))}{h}.
\tag{20}
\]

Second, substituting (19) into (14) shows that every `C_{q,s}(d)` is a finite sum of products of modular-residue polynomials, restricted by rational triangular inequalities. Equivalently, after splitting the signs of `h` and `h+d`, it is a polynomially weighted rational-lattice sum with periodic Bernoulli/residue data.

So, at fixed lower pair `(p,r)`, the whole quadratic upper-level kernel (17) is separately piecewise polynomial in `q` and `s` on residue classes modulo `p`, with only finitely many threshold walls. Sampling that kernel only at prime upper levels may import the classical distribution of primes in residue classes, but the matrix coupling itself has not produced a new analytic carrier.

## 4. Exact check

Take

\[
(p,r,q,s)=(7,11,13,17).
\tag{21}
\]

The nonzero determinant-layer packets are

\[
c_{13}(\pm1)=12,\qquad
c_{13}(\pm2)=4,\qquad
c_{13}(\pm4)=2,
\tag{22}
\]

and

\[
c_{17}(\pm1)=7,\qquad
c_{17}(\pm2)=6.
\tag{23}
\]

Hence

\[
C_{13,17}(0)=216,
\qquad
C_{13,17}(4)=C_{13,17}(-4)=24,
\tag{24}
\]

while all other shifts appearing in (16) vanish. Since `r-p=4`,

\[
\langle D_{13},D_{17}\rangle_{\mathrm{HS}}
=
4\cdot216+24+24
=
912.
\tag{25}
\]

Direct exact construction of the two integer defect matrices from the PC-251 overlap packets gives the same Frobenius inner product `912`.

## 5. Prior-art and novelty audit

The project-local content is the exact seven-shift reduction (16) for the Prime-Circle shared-upper defect and the observation that the multi-upper quadratic Gram kernel factors through the one-dimensional determinant-layer packets (19). The ambient arithmetic class of the resulting scalar sums is classical.

Matthias Beck and Sinai Robins, **Explicit and efficient formulas for the lattice point count in rational polygons using Dedekind-Rademacher sums**, *Discrete & Computational Geometry* 27 (2002), 443--459, DOI `10.1007/s00454-001-0082-3`, arXiv:`math/0111329`, show that rational-polygon lattice counts are built from Dedekind--Rademacher finite Fourier sums. Matthias Beck, Christian Haase and Asia R. Matthews, **Dedekind-Carlitz polynomials as lattice-point enumerators in rational polyhedra**, *Mathematische Annalen* 341 (2008), 945--961, DOI `10.1007/s00208-008-0220-9`, arXiv:`0710.1323`, place floor/residue generating functions of precisely this rational-cone type inside the classical Dedekind--Carlitz framework. Generalized Dedekind sums built from products of periodic Bernoulli functions provide a still broader classical home for correlations of the residue factors in (19).

Nothing in (15)--(19) creates a complex spectral parameter, gamma factor, `s <-> 1-s` symmetry, analytic continuation, or zero detector. If one later sums (17) over prime `q,s`, any Dirichlet-`L` information coming from prime residue classes enters through that external prime sampling, not through a new Prime-Circle operator identity.

The matched-control test is negative for source specificity at this quadratic stage. PC-251 already derives `D_q` from uniform rational partitions after the native overlap packets are formed; equations (9)--(16) then use only path incidence and determinant-layer geometry. An artificial uniform-partition model with the same lower/upper mesh parameters produces the same seven-shift reduction. The coupling therefore cannot by itself distinguish the cyclotomic source from the rational-partition carrier that represents it.

## 6. Boundary after PC-254 and PC-255

PC-254 showed that for one upper level the ordered collision pseudodeterminant collapses to the product of collision weights and elementary path-run factors, while leaving the complete nonzero singular distribution open. PC-255 now closes the most immediate *quadratic multi-upper* escape: covariance, Hilbert--Schmidt Gram matrices, and any determinant/eigenspectrum formed only after this quadratic Gram compression are functions of seven scalar modular correlations.

This is not a no-go for every multi-upper construction. It does not classify nonquadratic mixed words that retain the matrices `D_q` before Hilbert--Schmidt contraction, joint limits in which the word length or number of coupled upper levels grows with scale, or a source-forced operator that couples upper levels before the PC-251 rational-partition compression. Nor does it settle the complete singular spectrum of one `D_q`.

The surviving question is therefore narrower: whether genuinely nonquadratic/nonlocal multi-upper information survives the same determinant-layer localization and, if it does, whether its growing-scale analytic structure is more than generalized rational-lattice/Dedekind data. Merely observing nonzero covariance between two upper defects, or a nontrivial spectrum of their Hilbert--Schmidt Gram matrix, no longer crosses the novelty gate.
