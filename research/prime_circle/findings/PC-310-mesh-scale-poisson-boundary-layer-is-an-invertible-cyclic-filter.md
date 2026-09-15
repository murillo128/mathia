# PC-310 — mesh-scale Poisson boundary layer is an invertible cyclic filter

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the most direct linear harmonic escape left open by PC-309.

PC-309 proves that the matched prime source and its one-step rotation become indistinguishable under every uniformly transport-stable single-level observable, and that their complete normalized logarithmic-potential fields collapse throughout every boundary layer wider than the polygon mesh. The first unresolved radial regime is therefore exactly `1-r=O(1/q)`.

At that scale the natural Poisson/radial-flux observable can be computed exactly. The answer is lossless but not new: after sampling on the `q` polygon angles, the complete one-step Poisson response is an invertible diagonal Fourier multiplier on the centered source space. Thus the mesh-scale field recovers all finite cyclic source data, but it does so only through a universal circulant filter. Its first non-collapsing regime is precisely the regime where the operator has paid `Theta(q)` conditioning to resolve one polygon step.

This closes the direct route

\[
\text{single-level source}
\to
\text{one-step rotation difference}
\to
\text{linear Poisson/log-potential flux at }1-r\asymp q^{-1}
\to
\text{new arithmetic carrier}.
\]

It does **not** close mixed-conductor, nonlinear, shell-dependent, or otherwise non-circulant constructions.

## 1. Canonical source and centered cyclic data

Let `q>3` be prime and use the same prime source as PC-306--PC-309. Write its weights on `Z/qZ` as

\[
a_q(x):=\frac{1}{M_q}\mathbf 1_{\{x\in P_q\}},
\qquad
P_q:=\{p:2<p<q,\ p\text{ prime}\},
\qquad
M_q:=|P_q|.
\tag{1}
\]

Thus `sum_x a_q(x)=1`. Remove the known constant mode,

\[
f_q(x):=a_q(x)-\frac1q,
\qquad
\sum_{x\bmod q}f_q(x)=0.
\tag{2}
\]

Let the one-step cyclic translation be

\[
(Tf)(x):=f(x-1).
\tag{3}
\]

Because the uniform vector is fixed by `T`,

\[
Ta_q-a_q=Tf_q-f_q.
\tag{4}
\]

Hence no information relevant to the matched source/control difference is lost by working on the centered subspace.

Use the finite Fourier convention

\[
\widehat f(h)
:=\sum_{x=0}^{q-1}f(x)e^{-2\pi i hx/q},
\qquad h\in\mathbb Z/q\mathbb Z.
\tag{5}
\]

Then

\[
\widehat{Tf}(h)
=e^{-2\pi i h/q}\widehat f(h),
\tag{6}
\]

so the matched difference contributes the familiar translation factor `e^{-2 pi i h/q}-1`.

## 2. Exact Poisson aliasing on the polygon mesh

For `0<r<1`, let

\[
P_r(t)
=\frac{1-r^2}{1-2r\cos t+r^2}
=\sum_{k\in\mathbb Z}r^{|k|}e^{ikt}
\tag{7}
\]

be the Poisson kernel of the disk. For a cyclic source `f`, define the harmonic field

\[
(\mathcal P_r f)(\theta)
:=\sum_{x=0}^{q-1}f(x)
P_r\!\left(\theta-\frac{2\pi x}{q}\right).
\tag{8}
\]

Sample this field at the polygon angles `theta_j=2 pi j/q`, and normalize the sampled DFT by

\[
\widehat g_{\rm samp}(h)
:=\frac1q\sum_{j=0}^{q-1}g(\theta_j)e^{-2\pi i hj/q}.
\tag{9}
\]

Substituting (7) into (8) and applying the roots-of-unity filter gives the exact aliasing identity

\[
\boxed{
\widehat{(\mathcal P_r f)_{\rm samp}}(h)
=
\widehat f(h)
\sum_{m\in\mathbb Z}r^{|h+mq|}.
}
\tag{10}
\]

No asymptotic estimate or prime-distribution input is involved. Equation (10) is ordinary finite cyclic Fourier analysis: sampling identifies all integer Fourier modes with the same residue class modulo `q`.

Apply (10) to the one-step difference `Tf-f`. Then

\[
\boxed{
\widehat{(\mathcal P_r(Tf-f))_{\rm samp}}(h)
=
\left(e^{-2\pi i h/q}-1\right)
\widehat f(h)
\sum_{m\in\mathbb Z}r^{|h+mq|}.
}
\tag{11}
\]

Thus the entire sampled two-dimensional harmonic response is already diagonal in the ordinary cyclic characters.

## 3. The exact `1/q` boundary layer is lossless

Take the unresolved PC-309 scale in the canonical form

\[
r=e^{-a/q},
\qquad a>0\text{ fixed}.
\tag{12}
\]

For `1\le h\le q-1`, set `x=h/q`. The aliased Poisson weight in (11) can now be summed exactly:

\[
\begin{aligned}
S_{q,a}(h)
&:=\sum_{m\in\mathbb Z}e^{-a|h/q+m|}\\
&=\frac{e^{-ah/q}+e^{-a(1-h/q)}}{1-e^{-a}}.
\end{aligned}
\tag{13}
\]

Therefore the mesh-scale matched response has multiplier

\[
\boxed{
M_{q,a}(h)
=
\left(e^{-2\pi i h/q}-1\right)
\frac{e^{-ah/q}+e^{-a(1-h/q)}}{1-e^{-a}}.
}
\tag{14}
\]

For every nonzero residue `h mod q`, both factors in (14) are nonzero. Hence

\[
M_{q,a}(h)\neq0
\qquad (h=1,\ldots,q-1).
\tag{15}
\]

The only zero multiplier is `h=0`, exactly the constant mode removed in (2). Consequently:

\[
\boxed{
 f\longmapsto
 \left(\mathcal P_{e^{-a/q}}(Tf-f)\right)\big|_{\{\zeta_q^j\}}
\text{ is invertible on }
\left\{f:\sum_x f(x)=0\right\}.
}
\tag{16}
\]

For the canonical prime source, the total mass is already known, so the sampled mesh-scale field determines the complete finite source `a_q`. The boundary layer does not reveal a smaller hidden invariant: it simply becomes a lossless encoding of the original `q`-point data.

## 4. This is the intrinsic radial flux of the logarithmic potential

The Poisson calculation is not an unrelated smoothing model imported into prime-circle. Let

\[
V_f(re^{i\theta})
:=\sum_x f(x)
\log\left|re^{i\theta}-e^{2\pi i x/q}\right|.
\tag{17}
\]

For a single boundary point,

\[
P_r(\theta-\phi)
=
1-2r\,\partial_r
\log|re^{i\theta}-e^{i\phi}|.
\tag{18}
\]

Since a centered source has zero total mass, the constant term disappears after summation and

\[
\boxed{
\mathcal P_r f
=-2r\,\partial_r V_f.
}
\tag{19}
\]

Thus PC-310 classifies the most direct singular radial-flux refinement of the logarithmic-potential field used in PC-309. Retaining this genuinely two-dimensional harmonic object at the first unresolved boundary scale does preserve information, but after mesh sampling that information is exactly the cyclic source itself passed through (14).

## 5. Conditioning lands exactly at the PC-309 threshold

For fixed `a>0` and `h=o(q)`, (14) gives

\[
|M_{q,a}(h)|
\sim
\frac{2\pi h}{q}
\frac{1+e^{-a}}{1-e^{-a}}
=
\frac{2\pi h}{q}\coth\frac a2.
\tag{20}
\]

Hence every fixed or sublinear low mode still collapses, in agreement with PC-309 and the earlier packet bounds.

By contrast, if `h/q\to x\in(0,1)`, then

\[
|M_{q,a}(h)|
\longrightarrow
2|\sin(\pi x)|
\frac{e^{-ax}+e^{-a(1-x)}}{1-e^{-a}},
\tag{21}
\]

which is positive for interior `x`. In particular, modes near `q/2` have order-one gain, whereas the smallest nonzero gain occurs at the edge of the Fourier mesh and is order `1/q`. For fixed `a`, the condition number of (16) is therefore

\[
\boxed{\kappa(M_{q,a})=\Theta(q).}
\tag{22}
\]

This is exactly the cost predicted by PC-309: the first non-collapsing harmonic regime spends linear angular conditioning and resolves the polygon mesh itself. The lossless recovery is therefore not evidence of a new stable carrier; it is the expected mesh-scale decoding transition.

## 6. Prior-art and novelty audit

The ingredients of (10)--(16) are classical. The Fourier series (7) is the standard Poisson kernel for the unit disk; finite cyclic shifts and circulant convolutions are diagonalized by the discrete Fourier transform; sampling on the `q`-th roots of unity aliases integer Fourier modes by congruence modulo `q`. The existing `SOURCES.md` Poisson/GCD and Ramanujan/Fourier anchors already place these operations inside classical harmonic and finite Fourier analysis.

As representative references, Sheldon Axler, Paul Bourdon and Wade Ramey, *Harmonic Function Theory*, 2nd ed., Springer (2001), gives the standard Poisson-integral background (author-hosted edition: https://www.axler.net/HFT.html), while Robert M. Gray, *Toeplitz and Circulant Matrices: A Review*, *Foundations and Trends in Communications and Information Theory* 2:3 (2006), 155--239, DOI `10.1561/0100000006`, gives the standard circulant/DFT diagonalization framework (https://ee.stanford.edu/~gray/toeplitz.html).

The novelty audit therefore supports **classicalization**, not a claim of a new harmonic-analysis theorem. The line-specific durable result is the exact obstruction obtained by putting those classical pieces on the PC-309 matched prime-circle experiment at the previously unresolved scale: the canonical `1/q` Poisson boundary layer is an invertible cyclic filter, so its apparent recovery of arithmetic information is algebraically equivalent to recovering the original finite source.

No independent `s`-parameter, gamma factor, functional-equation symmetry, zero-sensitive determinant, or critical-line mechanism is generated by (14). Any such structure would have to enter through an additional operation not present in this single-level linear harmonic channel.

## 7. Boundary of the negative result

PC-310 rules out interpreting the **linear single-level Poisson/radial-flux boundary layer itself** as a new arithmetic carrier. It does not say that mesh-scale information is useless as an input to a later genuinely new mechanism.

The surviving routes must add structure that is not equivalent to a universal cyclic multiplier on one conductor. In particular, this finding does not rule out mixed-conductor or cross-level couplings, nonlinear operations applied before cyclic diagonalization, shell-dependent operators, non-circulant pointed interactions, or a theorem that maps the recovered finite source into an independently justified zero-sensitive destination.

It also does not claim that every possible singular boundary observable is Poisson. The no-go is exact for the canonical linear Poisson field, equivalently the radial derivative of the centered logarithmic potential, sampled at the intrinsic polygon mesh. A different singular operator must therefore identify what information it creates or couples beyond the source data already recovered by (16), rather than taking mere mesh-scale distinguishability as progress.

## 8. Falsification hooks

This finding should be revised or withdrawn if any of the following occurs:

1. the Fourier convention (5)--(11) is shown to mismatch the canonical one-step source/control experiment of PC-306--PC-309;
2. the roots-of-unity aliasing identity (10) fails under the stated sample normalization;
3. some nonzero residue `h` makes the exact multiplier (14) vanish for fixed `a>0`;
4. the radial-flux identity (19) fails for the centered logarithmic potential under the line's normalization;
5. prior art is found that already formulates this exact prime-circle matched-control `1/q` boundary-layer obstruction, in which case the classification should be strengthened from project-local classicalization to direct prior-art recovery.

Absent such a failure, the direct mesh-scale Poisson escape from PC-309 is closed: it becomes information-theoretically lossless exactly when it becomes a universal, linearly ill-conditioned decoder of the original cyclic source.