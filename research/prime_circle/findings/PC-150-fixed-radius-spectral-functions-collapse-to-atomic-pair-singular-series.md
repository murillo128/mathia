# PC-150 — fixed-radius spectral functions collapse to an atomic pair-singular-series law

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-SIEVE-BOUNDARY` + `DECISIVE-BOUNDARY`. PC-147 proves that the primorial primitive-shell inverse-square top-band projector is uniformly approximable in operator norm by finite chord-radius truncations. PC-149 then proves that every fixed polynomial moment of every such finite-radius operator is a finite combination of classical Lucas-totient / Hardy--Littlewood singular-series data, while explicitly leaving **non-polynomial spectral observables** outside its theorem.

For fixed chord radius `H`, that remaining escape also collapses at the first nonzero arithmetic scale. After normalization by `N_x^2`, the radius-`H` primitive-shell graph has only `Theta(phi(N_x)/log x)` edges. More strongly, vertices incident to two or more retained edges have density `O_H(1/log^2 x)`, because every such collision forces a fixed three-point reduced-residue constellation. Deleting those collisions changes the normalized Laplacian by trace norm `O_H(phi(N_x)/log^2 x)` and leaves a disjoint union of isolated weighted edges.

Hence every fixed-radius spectral function is, to first Mertens order, just the sum of the one-edge spectra. If

\[
N_x=\prod_{p\le x}p,
\qquad
A_{x,H}:=N_x^{-2}L_{N_x}^{(H)},
\]

then for every fixed `H` and every Lipschitz function `f` on the common spectral interval,

\[
\boxed{
\frac{\log x}{\varphi(N_x)}
\left(
\operatorname{Tr}f(A_{x,H})-\varphi(N_x)f(0)
\right)
\longrightarrow
 e^{-\gamma}
\sum_{\substack{1\le h\le H\\2\mid h}}
\mathfrak S_2(h)
\left[
 f\!\left(\frac1{2\pi^2h^2}\right)-f(0)
\right],
}
\tag{1}
\]

where `mathfrak S_2(h)` is the classical prime-pair singular series for the offset pair `{0,h}`. Thus heat traces, resolvent traces, shifted log-determinants, and all other fixed analytic spectral probes have an explicit **finite atomic Mertens correction** supported only at the isolated-edge eigenvalues `1/(2 pi^2 h^2)`.

This closes the fixed-radius non-polynomial loophole left by PC-149. No zeta-zero divisor, functional equation, gamma factor, or critical-line involution appears: the first nontrivial spectral correction is already exhausted by ordinary two-point sieve densities. What remains outside the theorem requires chord radius / interaction complexity growing with the conductor, or genuinely cross-level organization not captured by a single fixed local operator.

## 1. Fixed-radius primitive chord graphs are asymptotically matchings at Mertens order

Fix `H>=1`. For `N>2H`, let

\[
U_N=(\mathbb Z/N\mathbb Z)^\times
\]

and put an undirected edge of type `h`, `1<=h<=H`, between `a` and `a+h` whenever both residues are in `U_N`. For fixed positive `h<N/2`, each such unordered edge has a unique start `a`; its reverse uses offset `-h`, not another positive-`h` start.

Let

\[
J_h(N):=\#\{a\bmod N:(a,N)=(a+h,N)=1\}.
\tag{2}
\]

PC-149 gives the exact generalized-totient product. Along primorials,

\[
\frac{J_h(N_x)}{\varphi(N_x)}
\sim
\frac{e^{-\gamma}\mathfrak S_2(h)}{\log x},
\tag{3}
\]

where

\[
\mathfrak S_2(h)
:=
\prod_p
\frac{1-\nu_p(\{0,h\})/p}{(1-1/p)^2}.
\tag{4}
\]

For odd `h`, the local obstruction modulo `2` gives `mathfrak S_2(h)=0` and in fact `J_h(N_x)=0` once `2|N_x`. For even `h`,

\[
\boxed{
\mathfrak S_2(h)
=2C_2
\prod_{\substack{p\mid h\\p>2}}
\frac{p-1}{p-2},
\qquad
C_2=\prod_{p>2}\frac{p(p-2)}{(p-1)^2},
}
\tag{5}
\]

which is the standard Hardy--Littlewood prime-pair local factor.

Now let `B_{x,H}` be the set of primitive vertices incident to at least two radius-`H` edges. If `a in B_{x,H}`, there are two distinct signed shifts

\[
s,t\in\{\pm1,\ldots,\pm H\},
\qquad s\ne t,
\]

such that `a`, `a+s`, and `a+t` are all primitive. For each fixed pair `(s,t)`, PC-149's three-point formula gives either an exact local obstruction or

\[
\#\{a:\ a,a+s,a+t\in U_{N_x}\}
=O_{s,t}\!\left(\frac{\varphi(N_x)}{(\log x)^2}\right).
\tag{6}
\]

There are only `O(H^2)` signed pairs. Therefore

\[
\boxed{
|B_{x,H}|
=O_H\!\left(\frac{\varphi(N_x)}{(\log x)^2}\right).
}
\tag{7}
\]

Every vertex has degree at most `2H`. Delete every edge touching `B_{x,H}`. The number of deleted edges is consequently

\[
O_H\!\left(\frac{\varphi(N_x)}{(\log x)^2}\right),
\tag{8}
\]

and the retained graph is a disjoint union of isolated edges and isolated vertices. If `\widehat J_h(N_x)` denotes the number of retained isolated edges of type `h`, then

\[
\boxed{
\widehat J_h(N_x)
=J_h(N_x)
+O_H\!\left(\frac{\varphi(N_x)}{(\log x)^2}\right).
}
\tag{9}
\]

Thus multi-edge local geometry is one full Mertens power smaller than pair geometry. At the first nonzero `1/log x` scale, every fixed-radius component is spectrally indistinguishable from an isolated weighted edge.

## 2. Removing the collisions is negligible for every Lipschitz spectral function

For the inverse-square chord operator, write

\[
w_h(N)=\frac1{4\sin^2(\pi h/N)}.
\tag{10}
\]

An isolated edge of type `h` contributes the `2x2` Laplacian block

\[
\frac{w_h(N)}{N^2}
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix},
\tag{11}
\]

whose eigenvalues are `0` and

\[
\lambda_{h,N}:=\frac{2w_h(N)}{N^2}.
\tag{12}
\]

For fixed `h`,

\[
\boxed{
\lambda_{h,N_x}
\longrightarrow
\lambda_h:=\frac1{2\pi^2h^2}.
}
\tag{13}
\]

Let `\widehat A_{x,H}` be the normalized Laplacian after deleting all collision edges. Since every deleted edge Laplacian is positive semidefinite,

\[
D_{x,H}:=A_{x,H}-\widehat A_{x,H}\succeq0.
\tag{14}
\]

For fixed `H`, equation (10) gives a uniform bound on the normalized trace contribution of one deleted edge. Combining with (8),

\[
\boxed{
\operatorname{Tr}D_{x,H}
=O_H\!\left(\frac{\varphi(N_x)}{(\log x)^2}\right).
}
\tag{15}
\]

Order the eigenvalues increasingly. Weyl monotonicity applied to (14) gives

\[
\lambda_j(A_{x,H})\ge\lambda_j(\widehat A_{x,H})
\]

for every `j`, while the sum of all eigenvalue differences is exactly `Tr D_{x,H}`. Therefore, for every real Lipschitz `f`,

\[
\left|
\operatorname{Tr}f(A_{x,H})
-
\operatorname{Tr}f(\widehat A_{x,H})
\right|
\le
\operatorname{Lip}(f)\operatorname{Tr}D_{x,H}
=
O_{H,f}\!\left(\frac{\varphi(N_x)}{(\log x)^2}\right).
\tag{16}
\]

Complex-valued `f` follows by applying the estimate to real and imaginary parts. PC-147 gives the convenient common bound

\[
0\preceq A_{x,H}\preceq \frac18 I,
\tag{17}
\]

so one may take `f` Lipschitz on `[0,1/8]` independently of `x`.

The matching operator `\widehat A_{x,H}` has an exact block spectrum. Hence

\[
\operatorname{Tr}f(\widehat A_{x,H})
-
\varphi(N_x)f(0)
=
\sum_{h=1}^{H}
\widehat J_h(N_x)
\bigl[f(\lambda_{h,N_x})-f(0)\bigr].
\tag{18}
\]

Substitute (3), (9), and (13) into (18), then use (16). This proves the boxed limit (1).

## 3. The whole fixed-radius spectral displacement is an explicit finite atomic law

Equation (1) can be read as convergence of the first nontrivial spectral displacement away from the zero bulk. Formally, define the signed spectral displacement measure

\[
\eta_{x,H}
:=
\frac{\log x}{\varphi(N_x)}
\left(
\sum_j\delta_{\lambda_j(A_{x,H})}
-
\varphi(N_x)\delta_0
\right).
\tag{19}
\]

Its action on every Lipschitz test function converges to

\[
\boxed{
\eta_H
=
 e^{-\gamma}
\sum_{\substack{1\le h\le H\\2\mid h}}
\mathfrak S_2(h)
\left(
\delta_{1/(2\pi^2h^2)}-\delta_0
\right).
}
\tag{20}
\]

Thus the ordinary empirical spectral measure has the trivial local limit `delta_0`; the first nonzero correction is already an explicit finite atomic measure whose coefficients are classical pair singular series. Higher connected local constellations enter only at `1/log^2 x` or smaller.

This sharpens PC-149. Its fixed moments know all finite chord words but leave open whether a genuinely non-polynomial spectral probe could combine them in a new way. Equation (20) shows that no such combination survives at the leading arithmetic scale for fixed radius: all spectral functions see only the isolated-edge pair layer.

For example, for every fixed `k>=1`, taking `f(t)=t^k` gives

\[
\boxed{
\frac{\log x}{\varphi(N_x)}
\operatorname{Tr}(A_{x,H}^k)
\longrightarrow
 e^{-\gamma}
\sum_{\substack{h\le H\\2\mid h}}
\mathfrak S_2(h)
\left(\frac1{2\pi^2h^2}\right)^k.
}
\tag{21}
\]

So at first Mertens order the entire PC-149 word expansion is dominated by repeated traversal of one isolated primitive chord; genuinely multi-edge words are lower-order tuple corrections.

## 4. Resolvents, heat traces, and log-determinants acquire no new spectral divisor

Because the spectrum lies in `[0,1/8]`, equation (1) applies directly to standard analytic spectral probes away from that interval.

For the heat trace, `f(t)=e^{-ut}` with fixed `u>=0` gives

\[
\boxed{
\frac{\log x}{\varphi(N_x)}
\left(
\operatorname{Tr}e^{-uA_{x,H}}-\varphi(N_x)
\right)
\to
 e^{-\gamma}
\sum_{\substack{h\le H\\2\mid h}}
\mathfrak S_2(h)
\left(e^{-u/(2\pi^2h^2)}-1\right).
}
\tag{22}
\]

For `z` off `[0,1/8]`, the normalized resolvent trace satisfies

\[
\boxed{
\frac{\log x}{\varphi(N_x)}
\left(
\operatorname{Tr}(zI-A_{x,H})^{-1}
-
\frac{\varphi(N_x)}z
\right)
\to
 e^{-\gamma}
\sum_{\substack{h\le H\\2\mid h}}
\mathfrak S_2(h)
\left(
\frac1{z-1/(2\pi^2h^2)}-\frac1z
\right).
}
\tag{23}
\]

Choosing one analytic branch of `log(z-t)` on the same domain gives the shifted log-determinant law

\[
\boxed{
\frac{\log x}{\varphi(N_x)}
\left[
\log\det(zI-A_{x,H})
-
\varphi(N_x)\log z
\right]
\to
 e^{-\gamma}
\sum_{\substack{h\le H\\2\mid h}}
\mathfrak S_2(h)
\log\left(1-\frac1{2\pi^2h^2z}\right).
}
\tag{24}
\]

The right side is a **finite** sum with explicitly known positive sieve coefficients. Exponentiating it produces a finite product with fixed edge locations, not an Euler product over spectral zeros. In particular, passing from moments to a determinant or resolvent at fixed radius does not manufacture an RH mechanism that was invisible in PC-149.

## 5. Exact controls and prior-art audit

The pair and triple counts used above are not conjectural prime-tuple counts. They are exact counts inside the reduced residue system modulo the primorial. PC-149 identifies the general formula with Lucas/generalized Euler totients as recorded by Nittiya Pabhapote and Vichian Laohakosol, **Combinatorial Aspects of the Generalized Euler's Totient**, *International Journal of Mathematics and Mathematical Sciences* 2010, Article 648165, DOI `10.1155/2010/648165`. The `1/log x` and `1/log^2 x` scales arise only after applying ordinary Mertens asymptotics to those exact finite CRT products. PC-143/PC-144 already place the corresponding reduced-residue pair/triple factors next to the classical Montgomery--Vaughan and Aryan literature.

Broad searches across reduced-residue graphs, unitary Cayley graphs, primorial-wheel gap graphs, sparse-graph spectral convergence, Benjamini--Schramm limits, and matching/spectral measures found extensive classical graph-spectral frameworks but not this exact first-Mertens-order spectral-displacement formula for the primitive induced fixed-shift graph. That absence is **not** a historical novelty claim. General sparse graph convergence also explains why an ordinary fixed-radius empirical spectral measure can degenerate to the isolated-vertex law; the Prime-Circle-specific durable point is the exact next correction (20), whose coefficients are forced by the same classical pair singular series already visible arithmetically.

The RH audit is therefore negative. The fixed-radius determinant, resolvent, and heat trace acquire only finitely many geometric edge atoms with classical local-density weights. There is no intrinsic complex parameter tied to analytic continuation, no `s <-> 1-s` symmetry, no gamma factor, and no zero set capable of matching the nontrivial zeros of `zeta`.

As finite controls, for `N=2310` the exact positive-offset pair counts are

\[
J_2(2310)=135,
\qquad
J_4(2310)=135,
\qquad
J_6(2310)=270,
\tag{25}
\]

exactly as the local product (2)--(4) predicts. For the corresponding pair-density asymptotics,

\[
(\log x)\frac{J_2(N_x)}{\varphi(N_x)}
\to e^{-\gamma}\mathfrak S_2(2)\approx0.7413,
\]

while the `h=6` limit is twice that value because of the extra local collision modulo `3`. These numerics are checks only; the proof is the exact CRT counting plus Mertens.

## 6. Boundary and falsification surface

1. The theorem is for **fixed** `H`. If `H=H_x` grows with the conductor, the number of pair and triple patterns also grows and the `O_H` collision estimate does not provide a uniform asymptotic. PC-145--PC-147 show that growing radii matter for approximating the full top-band projector, so this is a genuine remaining boundary.
2. The first correction is a pair law because every multi-edge component contains at least one three-point primitive constellation. A counterexample must exhibit degree at least two without three distinct primitive vertices, which is impossible for `N_x>2H`, or invalidate the PC-149 tuple count.
3. The coefficient of an even offset `h` must equal `e^{-gamma} mathfrak S_2(h)`. Odd offsets must vanish exactly once `2|N_x`.
4. Removing collision edges must change `A_{x,H}` by a positive semidefinite operator with trace `O_H(phi(N_x)/log^2 x)`. Direct finite enumeration provides an independent check of this bound's combinatorial input.
5. Equation (1) concerns the first nonzero Mertens scale. It does **not** claim that the `1/log^2 x` correction is pairwise; that next layer contains genuine three-point constellations and then higher tuple data, all still inside PC-149's classical Lucas-totient hierarchy for fixed complexity.
6. The result does not classify spectral projectors or determinants when chord radius, word length, or functional complexity grows with `x`, nor does it classify cross-level transport of those growing objects. Any surviving local spectral mechanism must enter through such growing complexity rather than through a fixed non-polynomial probe of a fixed-radius operator.