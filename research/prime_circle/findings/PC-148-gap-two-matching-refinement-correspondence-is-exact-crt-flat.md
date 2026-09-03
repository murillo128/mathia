# PC-148 — gap-two matching refinement correspondence is exact CRT-flat

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-SIEVE-BOUNDARY` + `DECISIVE-BOUNDARY`. PC-142--PC-147 isolate the gap-two matching as the canonical finite-local skeleton of the primorial primitive-shell inverse-square chord top band. In particular, PC-147 leaves cross-level transport as one of the few places where organization not visible in a single local projector could still survive.

For the matching skeleton itself, the canonical cross-level correspondence is completely rigid. If `6|N` and `m` is coprime to `N`, the intrinsic power map `z -> z^m` sends every primitive gap-two edge at level `Nm` to a primitive gap-two edge at level `N`. Every parent edge has exactly

\[
\boxed{
S_2(m)=m\prod_{\ell\mid m}\left(1-\frac2\ell\right)
}
\]

children, and no other multiplicity occurs. Consequently the full fine-to-coarse incidence has one nonzero singular value `sqrt(S_2(m))` over each parent edge and zero on the orthogonal fiber fluctuations. For distinct new primes the normalized transports commute **exactly**, not merely asymptotically. The only scale mismatch of the selected inverse-square edge Laplacian is the scalar ratio `beta_{Nm}/beta_N`, which is an endpoint coboundary and has zero curvature around every refinement square.

Thus the dominant gap-two top-band skeleton does not acquire a Hecke-like or Berry-like prime curvature by being transported through the roots-of-unity refinement tower. Its multiplicity is the same classical two-point reduced-residue/Schemmel factor already visible in PC-139. Any genuinely new cross-level mechanism must involve the residual top-band geometry `Q_N-P_N`, nonconstant data not captured by the canonical edge projection, or a different intrinsically forced correspondence.

## 1. The matching edge set is functorial under the power map

Assume `6|N` and define the oriented gap-two starts

\[
M_N:=\{a\bmod N:(a,N)=1,\ (a+2,N)=1\}.
\tag{1}
\]

Because `3|N`, every unoriented primitive gap-two edge has a unique orientation with start `a congruent 5 (mod 6)`, so `M_N` indexes the exact matching of PC-139 without a sign ambiguity. Put

\[
u_a:=\frac{e_a-e_{a+2}}{\sqrt2},
\qquad
V_N:=\operatorname{span}\{u_a:a\in M_N\}.
\tag{2}
\]

The vectors `u_a` are orthonormal because the gap-two edges are disjoint.

Let `m>=1` satisfy `(m,N)=1`. Since `6|N`, every prime divisor of `m` is at least `5`. For `b in M_{Nm}`, the two endpoints of its primitive edge are

\[
\zeta_{Nm}^b,\qquad \zeta_{Nm}^{b+2}.
\]

Under the intrinsic power map

\[
\pi_m:z\longmapsto z^m
\]

they go to

\[
\zeta_N^b,\qquad\zeta_N^{b+2}.
\]

Reduction `b mod N` therefore defines a canonical surjection

\[
\boxed{\pi_{N,m}:M_{Nm}\longrightarrow M_N.}
\tag{3}
\]

No auxiliary embedding or spectral normalization has been introduced: (3) is just the action of the roots-of-unity refinement map on the actual shortest primitive chords.

## 2. Every parent edge has the same classical two-point reduced-residue fiber

Fix `a in M_N`. Its lifts have the form

\[
b=a+Nt,\qquad t\bmod m.
\tag{4}
\]

Because `a` and `a+2` are already units modulo `N`, such a lift belongs to `M_{Nm}` exactly when

\[
(a+Nt,m)=1,
\qquad
(a+2+Nt,m)=1.
\tag{5}
\]

For a prime power `ell^e || m`, `N` is invertible modulo `ell`. The two forbidden congruence classes of `t mod ell` coming from (5) are distinct because `ell>=5` and their difference is `2N^{-1} not\equiv0 (mod ell)`. Hence there are

\[
\ell^{e-1}(\ell-2)
\]

admissible classes modulo `ell^e`. CRT gives the exact uniform fiber size

\[
\boxed{
|\pi_{N,m}^{-1}(a)|
=\prod_{\ell^e\parallel m}\ell^{e-1}(\ell-2)
=m\prod_{\ell\mid m}\left(1-\frac2\ell\right)
=:S_2(m).
}
\tag{6}
\]

For a new prime `p`, this is simply

\[
\boxed{|\pi_{N,p}^{-1}(a)|=p-2.}
\tag{7}
\]

The product in (6) is the standard second Schemmel/reduced-residue-pair factor after an affine change of the odd fiber coordinate. Pabhapote and Laohakosol, **Combinatorial Aspects of the Generalized Euler's Totient**, *International Journal of Mathematics and Mathematical Sciences* 2010, Article 648165, DOI `10.1155/2010/648165`, record Schemmel totients as classical multiplicative counts of simultaneous coprimality conditions. PC-144 already places the corresponding fixed-offset reduced-residue tuple products in the Montgomery--Vaughan/Aryan sieve boundary.

Equation (6) immediately recovers the primorial multiplicity of PC-139. If `N_x=prod_{p<=x}p`, then starting from `N=6` and adjoining the primes `p>=5`,

\[
|M_{N_x}|=\prod_{3\le p\le x}(p-2)=E_x.
\tag{8}
\]

Thus the celebrated macroscopic-tail multiplicity is not only multiplicative as a scalar count; its entire edge-preimage correspondence factorizes prime by prime.

## 3. The full linear refinement incidence has trivial singular spectrum

Let

\[
\mathcal H_N:=\ell^2(M_N)
\]

and identify it isometrically with `V_N` by `delta_a -> u_a`. Define the canonical fine-to-coarse incidence

\[
(R_{N,m}f)(a)
:=\sum_{b\in\pi_{N,m}^{-1}(a)}f(b),
\qquad
R_{N,m}:\mathcal H_{Nm}\to\mathcal H_N.
\tag{9}
\]

The fibers in (3) are disjoint and all have cardinality `S_2(m)`. Therefore

\[
\boxed{
R_{N,m}R_{N,m}^*=S_2(m)I_{\mathcal H_N}.
}
\tag{10}
\]

Equivalently, the normalized pullback

\[
\boxed{
J_{N,m}:=\frac1{\sqrt{S_2(m)}}R_{N,m}^*
}
\tag{11}
\]

is an isometry from the parent matching space into the child matching space. The complete singular spectrum of the unnormalized correspondence is consequently

\[
\boxed{
\operatorname{Sing}(R_{N,m})
=\{\sqrt{S_2(m)}\text{ with multiplicity }|M_N|\},
}
\tag{12}
\]

with `R_{N,m}^*R_{N,m}` equal on each child fiber to the all-ones block. Its remaining `|M_{Nm}|-|M_N|` directions are exactly the zero-mean fiber fluctuations and have singular value zero.

So keeping the **whole rectangular parent/child matching incidence**, rather than only its cardinality, creates no hidden spectral distribution. It is a direct sum of identical rank-one fiber blocks.

## 4. Distinct-prime refinement squares are exactly flat

Let `p` and `q` be distinct primes, both coprime to `N`. Reduction of residues gives the literal identity of maps

\[
\pi_{N,pq}
=\pi_{N,p}\circ\pi_{Np,q}
=\pi_{N,q}\circ\pi_{Nq,p}.
\tag{13}
\]

Because the classical fiber count is multiplicative,

\[
S_2(pq)=(p-2)(q-2)=S_2(p)S_2(q),
\tag{14}
\]

the normalized pullbacks satisfy

\[
\boxed{
J_{Np,q}J_{N,p}
=J_{Nq,p}J_{N,q}
=J_{N,pq}.
}
\tag{15}
\]

Thus the most direct discrete curvature of the matching bundle vanishes identically:

\[
\boxed{
J_{Np,q}J_{N,p}-J_{Nq,p}J_{N,q}=0.
}
\tag{16}
\]

The unnormalized downward incidences also compose exactly,

\[
R_{N,p}R_{Np,q}=R_{N,q}R_{Nq,p}=R_{N,pq}.
\]

Equivalently, their adjoint two-step pullbacks coincide and equal `sqrt((p-2)(q-2)) J_{N,pq}`. The same functoriality extends from prime steps to arbitrary pairwise-coprime composite refinement factors. Hence the flatness is not a consequence of declaring a step to be prime; it is forced by CRT functoriality of the two-point reduced-residue fibers.

As a finite control, the matching dimensions and fiber sizes are

\[
E_{30}=3,
\qquad
E_{210}=3(7-2)=15,
\qquad
E_{2310}=15(11-2)=135.
\tag{17}
\]

The direct `30 -> 2310` refinement has fiber size

\[
S_2(77)=(7-2)(11-2)=45,
\]

exactly the same as either route `30 -> 210 -> 2310` through the two prime factors.

## 5. The inverse-square matching energy contributes only an endpoint gauge

PC-142 writes the selected gap-two edge Laplacian as

\[
A_N=\beta_NP_N,
\qquad
\beta_N=\frac1{2\sin^2(2\pi/N)},
\tag{18}
\]

where `P_N` is the orthogonal projector onto `V_N`. On the matching coefficient space this is simply `beta_N I`. Consequently

\[
A_{Nm}J_{N,m}=\beta_{Nm}J_{N,m},
\qquad
J_{N,m}A_N=\beta_NJ_{N,m}.
\tag{19}
\]

The only failure of exact intertwining is therefore the scalar

\[
c_m(N):=\frac{\beta_{Nm}}{\beta_N}.
\tag{20}
\]

But this scalar is an endpoint coboundary. Around a distinct-prime square,

\[
\boxed{
c_p(N)c_q(Np)
=\frac{\beta_{Npq}}{\beta_N}
=c_q(N)c_p(Nq).}
\tag{21}
\]

Equivalently,

\[
\log c_m(N)=\log\beta_{Nm}-\log\beta_N
\]

is the discrete gradient of the level potential `log beta_N`. After the intrinsic normalization

\[
\widehat A_N:=\beta_N^{-1}A_N=P_N,
\tag{22}
\]

the refinement is exactly intertwined by (15). Thus neither the edge weight nor the fiber multiplicity supplies a nonzero refinement curvature.

## 6. Prior-art and RH audit

The proof uses only the roots-of-unity power map, CRT, and the exact matching geometry already established in PC-139/PC-142. The arithmetic fiber factor (6) is classical simultaneous-coprimality data; Schemmel/generalized totient theory supplies an established name and multiplicative framework for precisely this type of product. A directed novelty check across Schemmel totients, reduced-residue tuple counts, unitary-Cayley/CRT graph products, cyclotomic refinement dynamics, and Bost--Connes-style prime semigroup actions did not expose this exact Prime-Circle matching-bundle formulation. That absence is not evidence of historical priority.

The durable point is therefore a **negative structural classification**, not a novelty claim for CRT. The currently dominant single-level top-band skeleton from PC-142--PC-147 cannot become an RH mechanism merely by transporting its gap-two edges through successive prime refinements. Its child multiplicities are the classical local factors `p-2`; its rectangular incidence has a one-point singular law; its normalized prime-step maps commute exactly; and its unnormalized inverse-square scale is a telescoping endpoint gauge.

No spectral parameter `s`, functional equation, gamma factor, critical-line involution, or zeta-zero divisor is generated. In particular, wrapping (9)--(22) in a transfer determinant would only repackage the finite products `prod(p-2)` and the elementary endpoint factors `beta_N`.

This does **not** classicalize the actual isolated top-band projectors `Q_N`. PC-143 and PC-147 show that `Q_N-P_N` contains sparse bounded-radius defect directions even though the band is average-matching and operator-local. Cross-level transport of those residual directions remains outside the theorem, as do correspondences that mix matching and nonmatching local motifs before projection. The result says that any such surviving cross-level effect must come from that residual geometry, not from the canonical gap-two backbone itself.

## 7. Falsification surface

1. For every `6|N` and `(m,N)=1`, direct enumeration must show that reduction `M_{Nm}->M_N` is surjective with constant fiber size (6).
2. For every prime power `ell^e || m`, the local fiber count must be `ell^{e-1}(ell-2)`; failure would invalidate the CRT product.
3. The incidence Gram must satisfy (10) exactly. Hence every nonzero singular value of `R_{N,m}` must equal `sqrt(S_2(m))`.
4. For distinct new primes `p,q`, direct residue reduction must verify the two composition identities in (13), and normalized pullbacks must agree entrywise as in (15).
5. The inverse-square scale cocycle must telescope exactly as in (21); any nonzero square curvature extracted solely from `beta_N` is therefore a normalization artifact.
6. No claim is made that cross-level transport of the full projectors `Q_N` is flat. A counterexample involving `Q_N-P_N`, a nonmatching local motif, or a genuinely different intrinsic correspondence would lie outside this finding rather than refute it.
