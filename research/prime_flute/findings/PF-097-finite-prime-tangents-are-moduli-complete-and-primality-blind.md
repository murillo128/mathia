# PF-097 — finite prime tangents are moduli-complete and primality-blind

**Status:** `DECISIVE-NEGATIVE` for any RH mechanism based only on the intrinsic spectral geometry of one fixed finite tangent.

## Claim

Let

\[
H=\{\eta_1<\cdots<\eta_r\},\qquad
d_i=\eta_{i+1}-\eta_i>0,
\]

and let \(Y_H\) be the cusp-side hyperbolic tangent obtained from the exact orthogonal-circle construction. The intrinsic tangent depends only on the projective gap vector

\[
[d_1:\cdots:d_{r-1}],
\]

and this parameter is not arithmetically restrictive: as the positive gap vector varies, the construction fills the entire positive moduli cell of ordered ideal \((r+1)\)-gons, equivalently the reflection-symmetric/zero-twist locus of the corresponding punctured-sphere tangents.

Consequently, no intrinsic geometric or spectral invariant of one fixed finite tangent can certify that its marked offsets came from primes. The same finite relative configuration can be translated to an all-composite constellation while leaving every gap, cross-ratio, tangent length, Laplace spectrum, resonance set and scattering invariant of the tangent unchanged.

Prime-specific information can therefore enter through finite tangents only through **how such tangents are selected and recur along the actual prime sequence**, or through finite-scale data discarded by the tangent normalization (for example the exact \(\pi\cot(\pi/p)\) Schwarzian correction of PF-082).

## 1. The gap coordinates are a complete moduli chart

The nested separating geodesics of PF-047 satisfy exactly

\[
\boxed{
\sinh^2\frac{L_k}{4}
=
R_k
:=
\frac{d_1+\cdots+d_{k-1}}{d_k}
},
\qquad k=2,\ldots,r-1.
\]

Conversely, take **arbitrary** target lengths

\[
L_2,\ldots,L_{r-1}>0
\]

and put

\[
R_k=\sinh^2(L_k/4)>0.
\]

Fix the irrelevant overall scale by \(d_1=1\), and define recursively

\[
\boxed{
 d_k=
 \frac{d_1+\cdots+d_{k-1}}{R_k},
 \qquad k=2,\ldots,r-1.
}
\]

Every \(d_k\) is positive and, by construction,

\[
\frac{d_1+\cdots+d_{k-1}}{d_k}=R_k.
\]

Hence

\[
\boxed{
\mathbb P(\mathbb R_{>0}^{r-1})
\longleftrightarrow
(0,\infty)^{r-2},
\qquad
[d_1:\cdots:d_{r-1}]
\longleftrightarrow
(L_2,\ldots,L_{r-1})
}
\]

is a bijection for this ordered pants-chain chart.

This dimension count is exactly the classical one. An ideal \((r+1)\)-gon has real moduli dimension

\[
(r+1)-3=r-2.
\]

Equivalently, normalize one vertex to \(\infty\). The remaining \(r\) ordered real vertices are then quotiented by the residual two-dimensional affine group; passing to their \(r-1\) positive gaps and quotienting by common scale leaves \(r-2\) parameters.

Thus the prime-derived gap coordinates are not cutting out a special lower-dimensional spectral locus. They are simply coordinates on the full relevant real moduli cell.

Doubling the ideal polygon across its sides gives the reflection-symmetric punctured-sphere tangent. In Fenchel--Nielsen language, the \(L_k\) are arbitrary positive length coordinates while the reflection fixes the twists to zero.

## 2. A finite prime pattern has an all-composite clone

The previous statement is already enough to show that the tangent geometry itself is generic. There is also a direct arithmetic sanity check.

Take any finite integer offset set

\[
H=\{\eta_1,\ldots,\eta_r\}.
\]

Choose pairwise distinct primes \(q_1,\ldots,q_r\). By the Chinese remainder theorem there exists \(M\) satisfying

\[
M\equiv-\eta_i\pmod{q_i}
\qquad(i=1,\ldots,r).
\]

Replacing \(M\) by a sufficiently large representative of the same residue class ensures

\[
M+\eta_i>q_i.
\]

Therefore every

\[
M+\eta_i
\]

is composite, since it is divisible by \(q_i\), while

\[
(M+\eta_j)-(M+\eta_i)=\eta_j-\eta_i.
\]

So the translated all-composite marked constellation has exactly the same finite gap vector and hence exactly the same ideal polygon and tangent surface.

One can strengthen the control by assigning distinct auxiliary primes to every integer offset in the finite interval \([\eta_1,\eta_r]\), producing by CRT a translate of the whole interval consisting entirely of composite integers. This does not mean that the original prime-selection rule selects those points; it makes the narrower obstruction precise: **once a finite marked configuration has been passed to its intrinsic tangent, the tangent has forgotten the arithmetic predicate that selected the marks.**

## 3. Spectral consequences

Anything determined solely by the isometry class of \(Y_H\) is therefore primality-blind at fixed finite depth. This includes, whenever defined in the standard finite-area setting,

- the full Laplace spectrum;
- the primitive and full length spectra;
- the resonance divisor;
- Selberg zeta;
- the physical or generalized cusp scattering data;
- Cheeger/systolic data;
- local wave invariants;
- the weighted graph limit and all inverse data reconstructing it.

This changes the interpretation of several positive findings without invalidating them:

- PF-074/PF-076 show that a four-punctured tangent converts a gap ratio into exact systolic/Cheeger geometry. The conversion is real, but it is an inverse-geometric encoding of a modulus, not a primality test.
- PF-094/PF-095 show that localized wave data or unmarked resonances can recover arbitrarily long finite projective gap vectors. PF-097 shows that recovering the vector perfectly still does not tell us why those offsets were selected.
- PF-049/PF-051/PF-052/PF-096 similarly recover increasingly resolved relative geometry. Their mathematical content survives, but any RH significance must come from relations **among many occurrences or scales**, not from inverse uniqueness of one tangent.
- PF-067 is thereby conceptually explained: generalized cusp scattering recovers the tangent because that is a standard inverse-geometry problem; no extra arithmetic content is created by making the inverse data complete.

## 4. What remains genuinely prime-specific

The negative does **not** apply to properties using the placement of infinitely many tangents along the actual prime sequence.

In particular, PF-034/PF-043 use arithmetic recurrence and isolation to turn finite surfaces into Weyl sequences of the single infinite prime-flute. A CRT clone of one finite configuration does not reproduce that global recurrence law. Likewise, PF-069 uses the actual multidimensional limit-point structure of consecutive prime gaps to force primitive-length accumulation in the global surface.

Nor does PF-097 erase finite-scale absolute information before the tangent limit. The exact endpoint map

\[
V(p)=\pi\cot(\pi/p)
\]

is not affine. PF-082 shows that after the projective tangent has removed the common scale, the first exact-circle correction reappears at order \(P^{-4}\) through

\[
S(V)(P)=\frac{2\pi^2}{P^4}.
\]

Thus the conceptual boundary is

\[
\boxed{
\text{one normalized finite tangent}
\;\Rightarrow\;
\text{relative geometry, not primality},
}
\]

whereas possible prime-specific information must involve at least one of

\[
\boxed{
\text{global selection/recurrence},\quad
\text{relations across different tangents},\quad
\text{absolute finite-scale exact-circle corrections}.
}
\]

The ambient interior/exterior inversion does not evade the obstruction: the tangent data above are built from cross-ratios and therefore survive Möbius conjugation unchanged.

## 5. Novelty / prior-art audit

No novelty is claimed for the ingredients.

- Moduli of ordered ideal \(n\)-gons modulo \(PSL_2(\mathbb R)\) are classical and have dimension \(n-3\). Modern treatments explicitly use cross-ratio coordinates on this moduli space; see Arnold--Fuchs--Izmestiev--Tabachnikov, *Cross-ratio dynamics on ideal polygons*.
- Fenchel--Nielsen length/twist coordinates and reflection-fixed zero-twist loci are standard hyperbolic geometry.
- The Chinese remainder theorem construction of a composite translate is elementary.

Directed searches did not find prior work combining these observations with prime-gap tangents or formulating the present obstruction. The substantive contribution here is therefore an **impossibility principle specific to this program**, not a new theorem about polygon moduli or CRT:

\[
\boxed{
\text{spectral completeness of a finite tangent cannot become arithmetic completeness.}
}
\]

A useful external sanity check is that the classical moduli dimension agrees exactly with the number of projective gap parameters; there is no hidden codimension in which primality could live.

## 6. Formalizable core

The following algebraic statements are natural Lean candidates and require no analytic geometry:

1. If \(R_k>0\), \(d_1>0\), and recursively
   \[
   d_k=(d_1+\cdots+d_{k-1})/R_k,
   \]
   then every \(d_k>0\) and
   \[
   (d_1+\cdots+d_{k-1})/d_k=R_k.
   \]
2. Multiplying all \(d_i\) by a common positive scalar leaves every \(R_k\) invariant.
3. Translating all marked positions by the same integer leaves the gap vector invariant.
4. The CRT lemma: for a finite integer set \(\{\eta_i\}\) and pairwise coprime \(q_i>1\), there are arbitrarily large \(M\) with \(q_i\mid M+\eta_i\) for all \(i\).

## Evidence level

`proved` for the coordinate bijection and the finite-pattern primality-blindness statement; `decisive-negative` for using the intrinsic spectrum/scattering/resonances of a single normalized finite tangent as a primality or RH mechanism.
