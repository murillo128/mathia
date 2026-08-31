# WP-058 — Prym Hodge determinant norm exports `log p`, while the polarization spectrum is flat

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + CANDIDATE-LOCAL-BRIDGE + DECISIVE-BOUNDARY + PRIOR-ART-REDIRECT` for the strongest intrinsic escape from the torsion obstruction of `WP-057`. `WP-056` found the old-prime scale `log p` in the finite kernel/discriminant of the induced Prym polarization, while `WP-057` showed that this torsion carrier itself admits no nonzero ordered real quadratic pairing. The same discriminant can nevertheless be exported canonically to a non-torsion positive object: the determinant line of the Prym homology lattice equipped with the polarization Hodge metric has covolume exactly `p^{g_n}`. Hence

\[
\boxed{
\log p
=\frac1{g_n}\log\operatorname{covol}_{g_E}H_1(P_{n,p},\mathbf Z)
}
\qquad(g_n>0).
\]

This is a genuine strengthening of the local bridge. It places the prime scale inside an honest positive metric norm rather than only in the cardinality of a finite group. It also shows that one scalar determinant-line invariant, together with the refinement depth `k`, numerically contains both factors of the interior finite Weil ray,

\[
(\log p)p^{-k/2}.
\]

But the same calculation exposes a sharp obstruction. With the metric induced by the polarization itself, the real polarization map is an exact isometry from the Prym Hodge space to its metric dual. Its positive operator is therefore the identity:

\[
(E^\flat)^*E^\flat=I.
\]

The prime does **not** occur as a singular-value scale of the canonical positive operator. It occurs only through the position/covolume of the integral lattice inside that metric space. Extracting `log p` therefore still requires a logarithm of a determinant-line norm. Declaring an integral basis orthonormal makes `p` appear in a positive matrix spectrum, but that spectrum fails the basis/gauge test; only the determinant/index survives unimodular changes. Thus the Prym route has moved the arithmetic signal from torsion cardinality to a canonical positive determinant-line norm, but it has not turned that signal into the value of the linear positive quadratic pairing required by a Weil criterion.

## 1. Setup: the `WP-056` Prym polarization

Keep the old-prime cover from `WP-055` and `WP-056`,

\[
f:C_{pn}\longrightarrow C_n,
\qquad (x,y)\longmapsto(x^p,y),
\qquad p\mid n,
\tag{1}
\]

and assume the base genus

\[
g_n=\frac{\varphi(n)-2}{2}
\tag{2}
\]

is positive. Let

\[
P=P_{n,p}=\operatorname{Prym}(C_{pn}/C_n)
\]

have complex dimension

\[
d=d_{n,p}=(p-1)(g_n+1).
\tag{3}
\]

Write

\[
\Lambda=H_1(P,\mathbf Z),
\qquad
V=\Lambda\otimes_{\mathbf Z}\mathbf R,
\]

so `rank_Z Lambda=2d`, and let `J:V->V` be the complex structure. The induced Prym polarization has integral Riemann form

\[
E:\Lambda\times\Lambda\longrightarrow\mathbf Z.
\tag{4}
\]

By `WP-056` and the cyclic-cover polarization formula already anchored in `SOURCES.md`, its elementary-divisor type is

\[
\boxed{
D_{n,p}=
\left(1^{\,d-g_n},p^{\,g_n}\right).
}
\tag{5}
\]

Equivalently, in an integral symplectic basis the matrix of `E` has Frobenius form

\[
[E]=
\begin{pmatrix}
0&D\\
-D&0
\end{pmatrix},
\qquad
D=\operatorname{diag}(1,\ldots,1,p,\ldots,p),
\tag{6}
\]

with `p` occurring `g_n` times. Therefore

\[
\boxed{
\det[E]=(\det D)^2=p^{2g_n}.
}
\tag{7}
\]

This is the same integer already seen in `WP-056` as

\[
|\ker\lambda_{n,p}|=p^{2g_n}.
\tag{8}
\]

## 2. The positive polarization metric has exact lattice covolume `p^{g_n}`

The Riemann form and complex structure canonically define the positive real polarization metric

\[
\boxed{
g_E(v,w):=E(v,Jw).}
\tag{9}
\]

The Riemann bilinear relations imply that `g_E` is symmetric positive definite and that `J` is `g_E`-orthogonal.

Choose any integral basis of `Lambda`. If `[J]` denotes the real matrix of the complex structure in that basis, then

\[
[g_E]=[E][J].
\tag{10}
\]

Since `J^2=-I` on the `2d`-dimensional real space, its real determinant is

\[
\det[J]=1.
\tag{11}
\]

Combining (7), (10), and (11),

\[
\boxed{
\det[g_E]=p^{2g_n}.
}
\tag{12}
\]

If `e_1,...,e_{2d}` is any integral basis and

\[
\omega_\Lambda=e_1\wedge\cdots\wedge e_{2d}
\in\det\Lambda,
\]

then the determinant-line norm induced by `g_E` satisfies

\[
\|\omega_\Lambda\|_{\det g_E}^2
=\det[g_E].
\tag{13}
\]

A different integral basis changes `omega_Lambda` only by sign because the change-of-basis determinant is `+-1`. Hence its norm is intrinsic, and (12)--(13) give

\[
\boxed{
\operatorname{covol}_{g_E}(\Lambda)
=\|\omega_\Lambda\|_{\det g_E}
=p^{g_n}.
}
\tag{14}
\]

Consequently

\[
\boxed{
\log p
=\frac1{g_n}\log\|\omega_\Lambda\|_{\det g_E}
=\frac1{2g_n}\log\|\omega_\Lambda\|_{\det g_E}^2.
}
\tag{15}
\]

Equation (15) is the main positive refinement of `WP-056`. The prime scale is not confined to the finite quotient `ker lambda`: it is also the logarithm of the norm of a canonical primitive integral vector in a one-dimensional determinant line carrying an ordinary positive-definite metric.

This does not contradict `WP-057`. That finding forbids a nonzero real quadratic form **on the finite torsion kernel itself**. Here the vector being measured lives in the non-torsion lattice determinant line `det Lambda`.

## 3. The polarization map is nevertheless an exact Hodge isometry

The determinant-line volume might suggest that the positive operator associated with the polarization has nontrivial singular values carrying `p`. Intrinsically it does not.

Let

\[
E^\flat:V\longrightarrow V^*,
\qquad
E^\flat(v)(w)=E(v,w),
\tag{16}
\]

and let

\[
g_E^\flat:V\longrightarrow V^*
\]

be the metric identification. From the `J`-invariance of the Riemann form,

\[
E(Jv,Jw)=E(v,w),
\tag{17}
\]

we have

\[
g_E(Jv,w)
=E(Jv,Jw)
=E(v,w).
\tag{18}
\]

Therefore

\[
\boxed{
E^\flat=g_E^\flat\circ J.
}
\tag{19}
\]

Equip `V^*` with the dual metric. The map `g_E^flat` is then an isometry, and `J` is an isometry by the Riemann relations. Hence `E^flat` itself is an isometry:

\[
\boxed{
(E^\flat)^*E^\flat=I_V,
\qquad
E^\flat(E^\flat)^*=I_{V^*}.
}
\tag{20}
\]

All singular values are exactly `1`. In particular,

\[
\boxed{
\det\bigl((E^\flat)^*E^\flat\bigr)=1,
\qquad
\operatorname{Tr}\log\bigl((E^\flat)^*E^\flat\bigr)=0.
}
\tag{21}
\]

The normalized spectral measure is the point mass at `1`, independently of the polarization type. An unnormalized trace can still see the dimension `2d`, and `d=(p-1)(g_n+1)` itself contains the cover degree, but that is only another counting invariant. Recovering `log p` from it again requires a nonlinear dimension readout; there is no `log p` singular-value scale in the canonical positive operator.

Thus the same polarized Hodge object has two sharply different faces:

\[
\boxed{
\text{real positive operator spectrum: flat at }1,
\qquad
\text{integral determinant-line volume: }p^{g_n}.
}
\tag{22}
\]

The arithmetic information is in the **integral structure**, not in a nontrivial positive real spectrum.

## 4. The lattice-index formula explains exactly where the discriminant lives

Equation (22) can be sharpened without choosing any basis. The integral polarization map satisfies

\[
E^\flat(\Lambda)\subset\Lambda^*:=\operatorname{Hom}(\Lambda,\mathbf Z),
\tag{23}
\]

and its quotient is the finite discriminant group underlying the polarization kernel. Under the dual metric,

\[
\operatorname{covol}_{g_E^*}(\Lambda^*)
=\operatorname{covol}_{g_E}(\Lambda)^{-1}
=p^{-g_n}.
\tag{24}
\]

Because `E^flat` is an isometry by (20),

\[
\operatorname{covol}_{g_E^*}(E^\flat\Lambda)
=\operatorname{covol}_{g_E}(\Lambda)
=p^{g_n}.
\tag{25}
\]

Therefore

\[
\boxed{
[\Lambda^*:E^\flat\Lambda]
=
\frac{\operatorname{covol}(E^\flat\Lambda)}
{\operatorname{covol}(\Lambda^*)}
=p^{2g_n}.
}
\tag{26}
\]

This recovers (8) geometrically and locates the exact source of the prime scale: an isometry between real metric spaces maps the integral lattice to a finite-index sublattice of the integral dual. The metric map is flat; the lattice embedding is not unimodular.

Equivalently,

\[
\boxed{
|\ker\lambda_{n,p}|
=\operatorname{covol}_{g_E}(\Lambda)^2.
}
\tag{27}
\]

So `WP-056`'s torsion cardinality and the present Hodge determinant norm are not two independent pieces of arithmetic. They are the discrete and metric descriptions of the same integral defect.

## 5. One determinant-line scalar numerically contains both finite Weil factors

Let

\[
\mathcal V_{n,p}
:=\operatorname{covol}_{g_E}(\Lambda)
=p^{g_n}.
\tag{28}
\]

Then

\[
\boxed{
\log p
=\frac1{g_n}\log\mathcal V_{n,p},
\qquad
p^{-k/2}
=\mathcal V_{n,p}^{-k/(2g_n)}.
}
\tag{29}
\]

Consequently the exact interior finite Riemann-Weil ray coefficient can be written solely in terms of this one-step determinant-line scalar and the refinement depth:

\[
\boxed{
(\log p)p^{-k/2}
=
\left(\frac{1}{g_n}\log\mathcal V_{n,p}\right)
\mathcal V_{n,p}^{-k/(2g_n)}.
}
\tag{30}
\]

This strengthens the numerical synthesis in `WP-056`. There, `log p` came from the polarization discriminant while `p^{-k/2}` came from normalized pull-push transfer. Equation (30) shows that the same one-step positive determinant-line norm already determines both scalars numerically once the tower distance `k` is known.

But this is **functional calculus of a positive scalar**, not a new bilinear pairing. The actual local quadratic norm is

\[
Q_{\det}(z)=\|z\|_{\det g_E}^2>0,
\tag{31}
\]

whereas the arithmetic coefficient is obtained only after applying `log`, dividing by `g_n`, and then applying a negative power. Positivity of (31) does not by itself imply positivity of any Weil autocorrelation form built from (30).

## 6. Gauge test: making the integral matrix spectral is noncanonical

There is an easy way to make `p` appear as an ordinary positive eigenvalue: choose the Frobenius integral basis in (6), declare that basis orthonormal by hand, and form

\[
[E]^T[E].
\tag{32}
\]

Its eigenvalues are the squares of the elementary divisors, so `p^2` occurs. This repair fails the canonicality test.

A different integral basis `U in GL(2d,Z)` replaces the alternating matrix by

\[
[E]\longmapsto U^T[E]U.
\tag{33}
\]

If the new basis is again declared Euclidean-orthonormal, the singular-value spectrum of (32) changes for a general non-orthogonal unimodular `U`. Hence that spectrum is a basis artifact. What survives every such change is the determinant/index because `|det U|=1`:

\[
|\det(U^T[E]U)|=|\det[E]|.
\tag{34}
\]

The canonical polarization metric removes the arbitrary Euclidean choice, and then (20) forces the spectrum to be flat. Thus the basis/gauge audit leaves exactly the invariant already identified in (14)--(27): **lattice covolume/discriminant, not positive spectral scale**.

This is closely analogous to `WP-043`, where a positive cycle Laplacian remembers `Lambda(n)` through a shell log-determinant while its positive spectral pairing is the wrong one. Here the positive geometry is much stronger—an honest polarized abelian variety—but the logarithmic arithmetic signal again sits in a determinant-level invariant rather than in the relevant quadratic form.

## 7. Three matched controls sharply limit the bridge

### Direct `p^k` cover

`WP-056` already observed that the single direct cover

\[
F^{(k)}:C_{p^kn}\to C_n
\tag{35}
\]

has polarization type with elementary divisor `p^k` on each of the `g_n` inherited base directions. The same determinant-line calculation therefore gives

\[
\operatorname{covol}(\Lambda_{F^{(k)}})
=p^{kg_n},
\qquad
\frac1{g_n}\log\operatorname{covol}(\Lambda_{F^{(k)}})
=k\log p.
\tag{36}
\]

But `Lambda(p^k)=log p`, not `k log p`. The correct coefficient therefore requires the **filtered one-prime-step tower**, not merely the final polarized direct cover. Compressing `k` refinements into one map destroys the Mangoldt normalization.

### Genus-zero base

If `g_n=0`, as for `n in {3,4,6}`, `WP-056` shows that the Prym is simply the covering Jacobian with principal polarization. Then

\[
\operatorname{covol}_{g_E}(\Lambda)=1,
\tag{37}
\]

so the determinant-line mechanism contains no `p` at all even though the finite Weil coefficient on the corresponding prime ray is nonzero. This remains an exact internal obstruction to a uniform local realization.

### Arbitrary cyclic-cover control

Nothing in (9)--(27) uses cyclotomy beyond the polarization type. An arbitrary ramified cyclic degree-`q` cover with the same base genus and branching type has elementary divisor `q` on the same number of polarization directions and therefore

\[
\operatorname{covol}_{g_E}(\Lambda)=q^g.
\tag{38}
\]

Thus the determinant-line positivity is universal cyclic-cover geometry. Prime Circle supplies the arithmetic fact that the old-prime refinement step has degree `p`; the positive Hodge determinant norm itself does not distinguish arithmetic primes from unrelated covering degrees.

These controls rule out interpreting (15) as an RH-specific positivity mechanism. They preserve it only as a strong Mathia-native **local carrier**.

## 8. Why this still stops before global Weil positivity

Equation (15) improves the local story in an important way: the prime scale can be read from an actual positive norm on a canonical non-torsion line. Nevertheless the mandate requires a single global form whose nonnegativity is proved before the arithmetic consequence is extracted.

If one turns each local scalar from (30) into a diagonal positive form by hand, one returns to the separable local positivity already ruled out in `WP-001` and `WP-005`. The Weil finite term is obtained after autocorrelation/translation assembly; the exact Prime-Lattice weights become an indefinite translation form rather than a sum of local squares. A positive determinant line at each prime does not change that assembly problem.

The archimedean side also remains separate. `WP-048` gives an intrinsic Prime-Circle selector for the `q=2` radial Mellin channel and hence the exact `Gamma_R` logarithmic derivative, but only after an affine extraction from a positive-real response. Nothing in the Prym determinant line produces the Mellin variable, digamma response, polar term, or the subtraction required there. Conversely, merely tensoring or summing the local positive determinant norms with an independent archimedean positive object would preserve place-separability, not provide the missing cross-place sign theorem.

A genuinely surviving determinant-line route would therefore need more structure than (15): a **global, nonseparable determinant/cohomological object formed before scalar logarithms are taken**, with a canonical pairing or second-variation theorem whose sign yields the assembled finite, archimedean, and polar Weil functional. The present result neither constructs nor rules out such an object.

## 9. Prior-art and novelty boundary

No historical novelty is claimed for the underlying polarization linear algebra. The elementary-divisor description of a Riemann form, the positive metric `g_E(v,w)=E(v,Jw)`, the degree/kernel formula for a polarization, and determinant-line covolumes are standard complex-abelian-variety theory. The only literature input specific to the old-prime Prym is the cyclic-cover polarization type already audited and anchored for `WP-056` in `SOURCES.md`.

The Mathia-specific content is the collision of those standard facts with the exact `WP-055`--`WP-057` old-prime tower:

1. the same induced Prym polarization whose finite kernel stores `p` also gives a canonical positive determinant-line norm `p^{g_n}`;
2. the real polarization operator is simultaneously an exact Hodge isometry, so the `p`-dependence is lattice-volume data rather than positive spectral scale;
3. the single determinant-line scalar numerically determines both `log p` and the critical half-density once the refinement depth is known;
4. direct-cover compression, genus-zero levels, and arbitrary cyclic-cover controls prevent that local bridge from being mistaken for a global Riemann-specific positivity theorem.

This is distinct from `WP-043`: there the logarithm is a shell determinant of a cycle Laplacian; here it is the norm of the primitive integral generator of the determinant line of an honest polarized Prym Hodge lattice. It is also distinct from `WP-057`: the torsion no-go is genuinely bypassed at the level of the carrier, because the determinant vector is non-torsion, but the logarithmic/nonlinear readout obstruction remains.

## 10. Consequence for the search

The old-prime Hodge/Prym route should no longer be summarized as saying that positive Hodge geometry completely erases `log p`. The sharper statement is

\[
\boxed{
\text{positive Hodge operator spectrum is flat,}
\qquad
\text{positive Hodge determinant-line volume remembers }p.
}
\tag{39}
\]

Accordingly, a surviving Mathia-native route may legitimately use **integral determinant-line geometry**, but only if it avoids scalarizing each place separately. The next successful mechanism would have to couple prime-step determinant lines, refinement/correspondence data, and the independently forced archimedean channel into one global object before taking logarithms or traces, and obtain its sign from geometry rather than from the known Weil criterion.

Until such a coupling theorem exists, the local identity

\[
\log p
=\frac1{g_n}\log\operatorname{covol}_{g_E}H_1(P_{n,p},\mathbf Z)
\]

is an exact positive-geometric carrier of the finite prime scale, **not** a proof or reformulation of global Weil positivity.