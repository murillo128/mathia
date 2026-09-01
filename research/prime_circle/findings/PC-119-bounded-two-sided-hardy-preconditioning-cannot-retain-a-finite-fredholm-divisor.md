# PC-119 — bounded two-sided Hardy preconditioning cannot retain a finite Fredholm divisor

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-117 proves that the canonically normalized arbitrary-conductor one-new-prime Hardy corrector

\[
X_{p,q}:=\frac{G_{p,q}}{\sqrt{\varphi(q)}},
\qquad p\nmid q,
\]

satisfies, along every joint path `p,q -> infinity` with `p` prime,

\[
\boxed{\|X_{p,q}\|\longrightarrow0},
\qquad
\boxed{\|X_{p,q}\|_{\mathcal S_2}^2\longrightarrow
\gamma-4+5\log2}.
\]

PC-118 then closes every genuine coordinate change of this finite corrector but deliberately leaves **operator-changing** non-similarity left/right weights and non-invertible compressions outside its similarity argument. The bounded part of that escape also closes. Let `A_{p,q}:\mathcal H_{p,q}\to\mathcal K_{p,q}` and `B_{p,q}:\mathcal K_{p,q}\to\mathcal H_{p,q}` be arbitrary conductor-dependent bounded maps satisfying

\[
\boxed{
\sup_{p,q}\|A_{p,q}\|\,\|B_{p,q}\|<\infty,
}
\]

and form the genuinely new operator

\[
\boxed{Y_{p,q}:=A_{p,q}X_{p,q}B_{p,q}.}
\]

No invertibility, positivity, diagonality, locality, arithmetic regularity, or convergence of `A_{p,q},B_{p,q}` is assumed. Then

\[
\boxed{\|Y_{p,q}\|\longrightarrow0},
\qquad
\boxed{\sup_{p,q}\|Y_{p,q}\|_{\mathcal S_2}<\infty}.
\]

Consequently every eigenvalue of `Y_{p,q}` tends uniformly to zero in modulus and every zero of

\[
\det(I-zY_{p,q})
\quad\text{or}\quad
\det{}_2(I-zY_{p,q})
\]

escapes every fixed compact subset of the `z`-plane. More precisely, every locally uniform subsequential limit of the regularized determinants is a zero-free Gaussian

\[
\boxed{
\exp\!\left(-\frac{\tau}{2}z^2\right)
}
\]

for some bounded subsequential limit `tau` of `Tr(Y_{p,q}^2)`. Thus uniformly bounded symmetric preconditioning, arbitrary bounded two-sided residue weights, primitive-mode projections, finite-rank truncations, and bounded compressions/quotients cannot turn the PC-117 corrector into an RH-relevant finite Fredholm divisor at the canonical joint normalization. A surviving repair must cross a genuinely singular boundary: its effective left/right norm must grow enough to prevent the transformed operator norm from vanishing, or it must change the construction before the PC-117 infinitesimal-corrector regime is reached.

No historical novelty is claimed for the operator-ideal estimates, spectral-radius bound, Fredholm determinant zeros, or regularized trace expansion. Those are standard trace-ideal/operator theory, with Barry Simon's *Trace Ideals and Their Applications* already anchored in `research/prime_circle/SOURCES.md`. The durable Prime-Circle content is the closure of two explicit operator-changing escape classes left open by PC-118 for the exact geometry-forced Hardy corrector.

## 1. Two-sided bounded maps preserve the infinitesimal operator scale

PC-117 supplies a family `X_{p,q}` that is trace class at every finite conductor and whose operator norm tends to zero on every joint arbitrary-conductor path. Since trace and Hilbert--Schmidt ideals are two-sided ideals, `Y_{p,q}=A_{p,q}X_{p,q}B_{p,q}` remains trace class and Hilbert--Schmidt. If

\[
M:=\sup_{p,q}\|A_{p,q}\|\,\|B_{p,q}\|<\infty,
\]

then the ideal inequalities give immediately

\[
\boxed{
\|Y_{p,q}\|
\le M\|X_{p,q}\|
\longrightarrow0,
}
\]

and

\[
\boxed{
\|Y_{p,q}\|_{\mathcal S_2}
\le M\|X_{p,q}\|_{\mathcal S_2}
=O(1).
}
\]

This argument is indifferent to how arithmetically complicated the bounded maps are. They may depend on every prime factor of `q`, mix all residue coordinates, be highly discontinuous in the conductor, or have nontrivial kernels. Only their effective two-sided operator norm matters.

The distinction from PC-118 is important. If `B=A^{-1}`, this is merely a similarity and PC-118 preserves the divisor **exactly**, even when the condition number diverges. Here `A` and `B` need not be related and the spectrum may change at every finite stage. Nevertheless bounded operator-changing maps still cannot overcome the vanishing spectral scale inherited from PC-117.

## 2. Every bounded Fredholm zero escapes to infinity

Let `lambda` be any eigenvalue of `Y_{p,q}`. The elementary spectral-radius estimate gives

\[
|\lambda|\le\|Y_{p,q}\|\longrightarrow0.
\]

A zero `z` of either the ordinary or regularized Fredholm determinant satisfies

\[
1/z\in\sigma(Y_{p,q})\setminus\{0\};
\]

the regularizing exponential in `det_2` is never zero. Hence, for every fixed `R<infinity`, eventually

\[
R\|Y_{p,q}\|<1,
\]

so `I-zY_{p,q}` is invertible for all `|z|\le R`. Therefore

\[
\boxed{
\forall R<\infty,\quad
\det(I-zY_{p,q})\ne0
\quad\text{and}\quad
\det{}_2(I-zY_{p,q})\ne0
\quad (|z|\le R)
}
\]

for all sufficiently large conductors along the joint path.

This is already enough to rule out convergence of the finite-stage determinant zero set to the nontrivial zeros of `zeta`: no nonzero bounded spectral location survives at all.

## 3. The only possible `det_2` cluster functions are zero-free Gaussians

The Hilbert--Schmidt bound gives a sharper description of what remains after all individual eigenvalues collapse. For every `k>=3`,

\[
\begin{aligned}
|\operatorname{Tr}(Y_{p,q}^k)|
&\le
\|Y_{p,q}\|^{k-2}\,\|Y_{p,q}^2\|_{\mathcal S_1}\\
&\le
\boxed{
\|Y_{p,q}\|^{k-2}\,\|Y_{p,q}\|_{\mathcal S_2}^2
}
\longrightarrow0.
\end{aligned}
\]

For a fixed disk `|z|<=R`, eventually `R\|Y_{p,q}\|<1`, so the standard regularized trace expansion is uniformly valid there:

\[
\log\det{}_2(I-zY_{p,q})
=-\sum_{k\ge2}\frac{z^k}{k}\operatorname{Tr}(Y_{p,q}^k).
\]

The tail satisfies

\[
\sup_{|z|\le R}
\left|
\sum_{k\ge3}\frac{z^k}{k}\operatorname{Tr}(Y_{p,q}^k)
\right|
\longrightarrow0.
\]

Thus, locally uniformly,

\[
\boxed{
\log\det{}_2(I-zY_{p,q})
=-\frac{z^2}{2}\operatorname{Tr}(Y_{p,q}^2)+o(1).
}
\]

Moreover

\[
|\operatorname{Tr}(Y_{p,q}^2)|
\le\|Y_{p,q}\|_{\mathcal S_2}^2=O(1).
\]

Every conductor sequence therefore has a subsequence on which `Tr(Y_{p,q}^2)->tau`, and along that subsequence

\[
\boxed{
\det{}_2(I-zY_{p,q})
\longrightarrow
\exp(-\tau z^2/2)
}
\]

locally uniformly on `C`. The limit is entire and zero-free for every complex `tau`. If the transformation is symmetric, for example

\[
Y_{p,q}=W_{p,q}^{1/2}X_{p,q}W_{p,q}^{1/2},
\qquad W_{p,q}\ge0,
\]

then `Y_{p,q}` is self-adjoint and `tau` is a nonnegative subsequential limit of `\|Y_{p,q}\|_{\mathcal S_2}^2`.

Thus bounded preconditioning can change the Gaussian variance, possibly in an arithmetic conductor-dependent way, but cannot create a nontrivial finite zero divisor.

## 4. The result includes non-similarity weights and non-invertible compressions

Two escape classes named explicitly in PC-118 now fall inside the same estimate.

### Bounded symmetric or asymmetric weighting

If `L_{p,q}` and `R_{p,q}` are any uniformly bounded conductor-dependent weights or mixing operators, then

\[
Y_{p,q}=L_{p,q}X_{p,q}R_{p,q}
\]

satisfies the theorem. In particular this covers bounded anchored chord weights, bounded Fourier/Ramanujan multipliers, bounded primitive/composite masks, and bounded positive preconditioners. Their finite spectra may differ from that of `X_{p,q}`, so this is not the similarity invariance of PC-118; the obstruction is instead the vanishing operator scale.

### Compression and quotient maps

Let `J_{p,q}:\mathcal K_{p,q}\to\mathcal H_{p,q}` be an isometry and form the compression

\[
Y_{p,q}=J_{p,q}^*X_{p,q}J_{p,q}.
\]

Then `\|J_{p,q}\|=\|J_{p,q}^*\|=1`, so the same conclusion holds. Orthogonal projections `P_{p,q}X_{p,q}P_{p,q}`, including conductor-dependent primitive-mode or finite-rank projections, are the ambient-space version of this case. Bounded coisometric quotient constructions are identical analytically. Therefore non-invertibility alone does not rescue the divisor.

This does not say that every conceivable projection of every Prime-Circle operator is trivial. It says that projecting the **already normalized PC-117 infinitesimal Hardy corrector** cannot restore finite spectral locations when the projection/quotient maps stay bounded.

## 5. Sharp analytic boundary for a surviving repair

The proof reveals the exact analytic condition that matters. The Gaussian-only conclusion does not fundamentally depend on a factorization `Y=AXB`. Any transformed family satisfying

\[
\boxed{
\|Y_{p,q}\|\to0,
\qquad
\sup_{p,q}\|Y_{p,q}\|_{\mathcal S_2}<\infty
}
\]

has only zero-free Gaussian `det_2` cluster functions by Section 3. Consequently a proposed repair of this Hardy branch must violate at least one of these conditions if it is to retain a finite Fredholm divisor.

For a two-sided transformation `A X B`, a uniformly bounded product `\|A\|\|B\|` cannot do so. A necessary possibility is therefore a genuinely singular/unbounded conductor dependence strong enough that the transformed operator norm need not vanish. That is only a **necessary boundary**, not a positive mechanism: unbounded weights can just as easily manufacture arbitrary spectral scales and must be independently forced by the Prime-Circle geometry, survive matched non-arithmetic controls, and avoid becoming an arbitrary spectral wrapper under the canonical README mandate.

Likewise, changing the spectral variable by a conductor-dependent divergent rescaling after the fact is not covered by the bounded theorem; it is a new normalization choice and requires its own intrinsic justification rather than being inferred from the present corrector.

## 6. Falsification checks

1. **Joint-limit hypothesis:** the result uses the PC-117 operator-norm collapse and therefore applies to its joint `p,q -> infinity` regime. It does not claim the same for fixed `q` and `p -> infinity`, where PC-113/114 exhibit a different microlocal boundary.
2. **Boundedness is essential:** taking a scalar `A_{p,q}=a_{p,q}I` with `a_{p,q}->infinity` can defeat the simple norm estimate. Such a transformation crosses the singular boundary rather than contradicting the theorem.
3. **Non-normal maps are allowed:** self-adjointness is unnecessary for the zero-escape statement or the Gaussian cluster argument. The quadratic coefficient `tau` may then be complex, but `exp(-tau z^2/2)` is still zero-free.
4. **Compression is not similarity:** a projection can genuinely move or delete finite-stage eigenvalues, yet its norm is at most that of the original operator, so it cannot prevent spectral collapse.
5. **The ordinary determinant need not have the same function limit:** `det_2(I-zY)=det(I-zY)e^{z\operatorname{Tr}Y}` at finite stage. The exponential factor may affect convergence of the function but never its zeros, so the divisor conclusion is shared by both determinants.
6. **No hidden arithmetic regularity assumption:** the proof never averages the weights over residues and does not use continuity, periodicity, or equidistribution of `A,B`; conductor-dependent primitive masks and other discontinuous bounded arithmetic selections are included.

## 7. Prior-art and novelty audit

The mathematical ingredients are standard operator theory. Schatten classes are two-sided ideals under bounded multiplication; the spectral radius is bounded by the operator norm; ordinary Fredholm and Hilbert--Schmidt regularized determinants have zeros exactly at reciprocal nonzero eigenvalues; and the `det_2` trace expansion begins at the quadratic trace. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., AMS (2005), already present in `research/prime_circle/SOURCES.md` for the Hardy determinant branch, is the appropriate standard reference.

Directed literature checks against trace-ideal/Fredholm-determinant references found only this classical framework; there is no theorem-level novelty claim for the abstract bounded-preconditioning lemma. The research contribution is instead a line-specific boundary result: PC-118 explicitly left actual non-similarity weights and compression/quotient operations as candidate escapes from the exact PC-117 corrector. The PC-117 norm and Hilbert--Schmidt asymptotics show that **every uniformly bounded realization of those escapes remains spectrally infinitesimal and Gaussian-only**.

The surviving Hardy frontier is therefore narrower than after PC-118:

\[
\boxed{
\text{bounded operator-changing repair}
\;\Longrightarrow\;
\text{no finite Fredholm zero divisor}.}
\]

What remains requires singular/unbounded geometry-forced amplification, a nonlinear organization before the PC-113/117 corrector limit, or a genuinely different intrinsic Prime-Circle operator family.