# PF-095 — hierarchical prime tangents are resonance-rigid modulo overall gap scale

**Status:** `POSITIVE / EXACT-RESTRICTED-RESONANCE-RIGIDITY + CLASSICAL-RESONANCE-TO-LENGTH INPUT`. No RH claim and no claim of a global resonance divisor for the infinite flute.

PF-063 showed that the full unmarked resonance set of a hierarchical four-punctured prime tangent recovers one adjacent-gap ratio through its unique systole. PF-094 then proved a stronger geometric fact for arbitrarily large finite tangents: once every canonical internal cuff is shorter than `log 2`, the entire primitive length spectrum below the universal threshold `4 asinh 1` consists exactly of those cuffs, and a strong hierarchy orders them. Combining that exact barcode with the resonance/length theorem of Borthwick--Judge--Perry removes the complexity-one restriction from PF-063.

The result is an exact restricted inverse theorem: on the hierarchical prime-tangent family, the ordinary Laplace resonance set determines the full finite projective consecutive-gap vector.

## 1. Exact prime-tangent family

Let

\[
H=\{\eta_1<\cdots<\eta_r\},
\qquad
d_j=\eta_{j+1}-\eta_j>0,
\qquad j=1,\ldots,r-1,
\]

be one of the isolated patterns of PF-034/PF-046. Its exact cusp-side tangent is a complete finite-area genus-zero hyperbolic surface

\[
Y_H\simeq S_{0,r+1}.
\]

The canonical zero-twist pants decomposition coming from the orthogonal-circle construction has internal separating cuffs

\[
\gamma_k,
\qquad k=2,\ldots,r-1,
\]

with exact lengths

\[
\boxed{
\sinh^2\frac{L_k}{4}
=R_k
:=\frac{d_1+\cdots+d_{k-1}}{d_k}.
}
\tag{1}
\]

This is a cross-ratio identity, hence Möbius invariant. Ambient inversion exchanging the prime-circle interior/exterior pictures preserves every `L_k`; the statement below is therefore intrinsic to the common hyperbolic tangent, not to a chosen side of the embedding.

For occurrences near large prime scale `P`, the distinguished prime-flute cuffs satisfy

\[
\ell_j(P)=2\log\frac{4P}{d_j}+o(1),
\]

so

\[
\boxed{
\frac{d_j}{d_1}
=
\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_j(P)-\ell_1(P)}2\right].
}
\tag{2}
\]

Thus the projective gap vector is exactly the finite information surviving after the common divergent cuff scale is removed.

## 2. The universal short barcode

Put

\[
c_*:=4\operatorname{arsinh}1=2\operatorname{arccosh}3.
\]

PF-094 combines Yamada's shortest-nonsimple-geodesic theorem with the collar lemma and the exact identity

\[
2w(\log2)=c_*,
\qquad
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)},
\]

to prove the following.

If

\[
\boxed{L_k<\log2\quad\text{for every }k,}
\tag{3}
\]

then

\[
\boxed{
\mathcal L_{\rm prim}(Y_H)\cap(0,c_*)
=
\{L_2,\ldots,L_{r-1}\}
}
\tag{4}
\]

with multiplicity. No non-cuff primitive geodesic can enter this window: a nonsimple one is excluded by Yamada, while a simple non-cuff curve must cross a cuff and is excluded by its collar.

For the super-hierarchical patterns of PF-054 one eventually has, strictly,

\[
0<L_{r-1}<\cdots<L_3<L_2<\log2.
\tag{5}
\]

Hence the **unmarked** short length spectrum itself supplies the labels: the largest primitive length below `c_*` is `L_2`, the next is `L_3`, and so on.

## 3. Classical resonance-to-length theorem

Borthwick--Judge--Perry, *Selberg's zeta function and the spectral geometry of geometrically finite hyperbolic surfaces*, Comment. Math. Helv. 80 (2005), Corollary 1.2, prove that for a geometrically finite hyperbolic surface the full resolvent resonance set, with multiplicities, determines

- the length spectrum;
- the Euler characteristic; and
- the number of cusps.

Their result applies directly to every finite tangent `Y_H`. In particular,

\[
\boxed{
\mathcal R(Y_H)
\Longrightarrow
\mathcal L_{\rm prim}(Y_H),\ n_C(Y_H),\ \chi(Y_H).
}
\tag{6}
\]

The same theorem is equivalently the standard Selberg-zeta bridge: the resonance divisor determines the Selberg-zeta divisor and hence the primitive length spectrum. This is a natural spectral/dynamical object, not a prime-gap generating function introduced by hand.

Primary source:

- D. Borthwick, C. Judge, P. A. Perry, *Selberg's zeta function and the spectral geometry of geometrically finite hyperbolic surfaces*, Comment. Math. Helv. 80 (2005), 483--515, especially Corollary 1.2. DOI `10.4171/CMH/23`.

## 4. Exact resonance rigidity of the projective gap vector

Assume `Y_H` lies in the hierarchical barcode regime (3)--(5). From the resonance set, (6) first recovers `r`: since `Y_H\simeq S_{0,r+1}`, the number of cusps is `r+1`.

It then recovers the primitive length multiset. Restricting to `(0,c_*)` and using (4) gives exactly the `r-2` canonical cuffs. The strict ordering (5) labels them as `L_2,...,L_{r-1}`.

Now define

\[
R_k:=\sinh^2(L_k/4).
\]

Equation (1) is triangular. Fix the unavoidable common scale by setting `d_1=1`; recursively,

\[
\boxed{
 d_k
 =
 \frac{d_1+\cdots+d_{k-1}}{R_k},
 \qquad k=2,\ldots,r-1.
}
\tag{7}
\]

Therefore

\[
\boxed{
\mathcal R(Y_H)
\quad\Longrightarrow\quad
[d_1:d_2:\cdots:d_{r-1}]
}
\tag{8}
\]

**exactly** at tangent level.

Equivalently, on this family the map

\[
[d_1:\cdots:d_{r-1}]
\longmapsto
\mathcal R(Y_H)
\]

is injective. More explicitly, if two hierarchical exact prime tangents satisfy

\[
\mathcal R(Y_H)=\mathcal R(Y_{H'})
\]

with multiplicity, then Borthwick--Judge--Perry forces the same cusp number and the same primitive length spectrum; the barcode and triangular inversion then force

\[
\boxed{
[d_1:\cdots:d_{r-1}]
=
[d'_1:\cdots:d'_{r-1}].
}
\tag{9}
\]

This remains true even though resonance data does **not** determine a general geometrically finite hyperbolic surface uniquely up to isometry. Borthwick--Judge--Perry explicitly note isoresonant non-isometric examples. The rigidity here is only for the prime-derived projective gap coordinate, and comes from the exact short-barcode structure of this thin family.

Combining with (2) gives the direct statement in the original distinguished-cuff variables:

\[
\boxed{
\mathcal R(Y_H)
\Longrightarrow
\left(
\lim_{P\to\infty}e^{-(\ell_2-\ell_1)/2},
\ldots,
\lim_{P\to\infty}e^{-(\ell_{r-1}-\ell_1)/2}
\right).
}
\tag{10}
\]

Thus arbitrarily long finite vectors of **relative cuff fluctuations**, equivalently consecutive-prime-gap shapes, are exact invariants of the unmarked Laplace resonance divisor of the corresponding hierarchical tangent.

## 5. Why this is not the already-known full inverse-scattering theorem

PF-067 gave a decisive novelty downgrade for the generalized operator-valued cusp S-matrix: Isozaki--Kurylev--Lassas already prove that one generalized cusp scattering component determines the whole geometrically finite surface. Merely composing that full inverse theorem with the gap coordinates is not new.

PF-095 uses materially weaker data. A resonance set is only a divisor/pole set with multiplicities; it contains no cusp-channel labels, generalized Fourier-mode response, boundary Green kernel, norming constants, or scattering matrix values. General resonance data is not isometrically rigid.

The new composition therefore survives PF-067's gate:

\[
\boxed{
\text{unmarked resonance divisor}
\to
\text{unmarked primitive short barcode}
\to
\text{ordered canonical cuffs}
\to
\text{full projective gap vector}.
}
\]

PF-063 established exactly this mechanism only for `S_{0,4}`, where one unique systole carries one ratio. PF-095 removes that topology-one limitation and gives arbitrary finite depth.

## 6. Relation to the infinite prime flute

This does **not** restore an absolute global resonance theory for the infinite surface.

- PF-035/PF-036/PF-077 show that primitive-orbit accumulation destroys the ordinary global Selberg/Ruelle Euler product and even local finiteness of the classical orbital measure.
- PF-092 shows that infinitely many sub-quarter essential spectral points accumulate at `s=1`, preventing a standard meromorphic-Fredholm `L^2` resolvent in any full neighborhood of `s=1`.

The finite tangent is different: it is geometrically finite and has an ordinary Selberg zeta and a discrete resonance divisor. PF-034 realizes such tangents as genuine pointed limits of recurrent isolated regions of the *single* infinite prime flute, while PF-094 shows that a spatially localized wave observable of that global Laplacian converges to the same short barcode.

So there are now two complementary statements:

\[
\boxed{
\begin{aligned}
\text{finite tangent resonance set}
&\Longrightarrow
\text{projective gap vector exactly},\\
\text{localized wave data of }X_{\rm prime}
&\Longrightarrow
\text{the same vector in the tangent limit},\\
\text{absolute global resonance divisor of }X_{\rm prime}
&\text{ is obstructed.}
\end{aligned}
}
\tag{11}
\]

This local-versus-global separation is structural rather than a missing regularization trick.

## 7. Serious novelty audit

Known ingredients, with no novelty claim:

1. Borthwick--Judge--Perry: resonance set determines the length spectrum, Euler characteristic, and cusp number of a geometrically finite hyperbolic surface.
2. Selberg's trace/zeta formalism relating resonances and primitive geodesic lengths.
3. Yamada's universal lower bound for nonsimple closed geodesics.
4. The collar lemma and elementary pants-decomposition topology.
5. General inverse scattering from a full generalized cusp S-matrix, which is strictly stronger data and was already accounted for in PF-067.

Directed searches for `resonance set + Fenchel-Nielsen`, `resonance rigidity + punctured sphere + pants decomposition`, `resonances + pinching parameters`, and `prime gaps + hyperbolic resonances` found the general resonance/length and inverse-spectral theories but not this prime-derived restricted rigidity statement.

No priority claim is made for any classical ingredient. The candidate-specific content is the exact composition

\[
\boxed{
\text{hierarchical consecutive-prime shape}
\to
\text{orthogonal-circle tangent}
\to
\text{universal short primitive barcode}
\to
\text{ordinary unmarked resonance divisor}
}
\]

and its inverse injectivity (9).

## 8. Limits and falsification checks

- The theorem uses the **full** resonance set of each finite tangent, not finitely many resonances and not merely the near-`s=1` germ.
- The full tangent resonance set is not asserted to occur as a discrete set of poles of the global infinite-flute resolvent; PF-092 explains why that inference is false in ordinary `L^2` theory.
- The hierarchy is used to label the unordered cuff barcode. Without it, (4) still identifies the cuff multiset but may not identify the nesting order needed by (7).
- The unavoidable overall scale of `(d_j)` is absent from the tangent by Möbius scaling; projective recovery is therefore the maximal possible statement.
- If Borthwick--Judge--Perry's resonance set failed to determine primitive length multiplicities in the finite-area cusped case, or if a non-cuff primitive geodesic entered `(0,c_*)` under (3), the argument would fail. Their Corollary 1.2 and the PF-094 Yamada+collar argument rule out those two failure modes.

## Research consequence

The finite-tangent resonance question is now closed at arbitrary finite depth in the strongly hierarchical regime: unmarked resonances already recover the full relative gap shape. The genuinely harder remaining problem is not another inverse theorem for a finite tangent, but whether one can construct a **canonical, non-ad-hoc localization or relative spectral object on the single infinite flute** whose spectral data decomposes into these resonance/short-wave fingerprints without being destroyed by the global essential spectrum and orbit accumulation.
