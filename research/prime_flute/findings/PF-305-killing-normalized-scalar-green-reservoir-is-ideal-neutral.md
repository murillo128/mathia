# PF-305 — killing-normalized scalar Green reservoir is symmetric-ideal neutral

**Status:** `EXACT-DERIVED + CLASSICAL-IDEAL-SANDWICH + DECISIVE/ROUTE-NARROWING`.

PF-303 identifies the exact scalar killed-conductance Green currency on a finite prime-flute pant chain,

\[
H_N=L_{c,N}+D_N,\qquad G_N=H_N^{-1},\qquad G_Nd=\mathbf 1,
\]

with `D_N=diag(d_j)>0`. PF-304 sharpens this to reversible Markov averaging: `G_ND_N` is Markov and the Green response is contractive in the natural killing-weighted `L^p` scales. The remaining accepted source-weighted-return clue is no longer a scalar lifetime question; it asks whether the actual physical `P/H` mixed forcing and reassembly enter and leave that scalar currency with enough control.

There is an exact Hilbert-space form of this reduction. Put

\[
\boxed{S_N:=D_N^{1/2}G_ND_N^{1/2}.}
\]

Then

\[
\boxed{0<S_N\le I,\qquad \|S_N\|=1.}
\]

For arbitrary Hilbert spaces `X,Y` and arbitrary bounded entrance/reassembly maps

\[
F_N:X\to\mathbb C^{N+1},\qquad R_N:\mathbb C^{N+1}\to Y,
\]

every scalar-mediated response

\[
M_N:=R_NG_NF_N
\]

factors exactly as

\[
\boxed{
M_N
=\widehat R_N\,S_N\,\widehat F_N,
\qquad
\widehat F_N:=D_N^{-1/2}F_N,
\qquad
\widehat R_N:=R_ND_N^{-1/2}.
}
\]

Consequently the scalar Green reservoir cannot worsen the compactness or symmetric-ideal class supplied by either **killing-normalized conversion vertex**. For every singular index `j`,

\[
\boxed{
s_j(M_N)\le \|\widehat R_N\|\,s_j(\widehat F_N)}
\]

whenever `\widehat F_N` is compact, and

\[
\boxed{
s_j(M_N)\le \|\widehat F_N\|\,s_j(\widehat R_N)}
\]

whenever `\widehat R_N` is compact. Hence, for every two-sided symmetric operator ideal `\mathcal J`,

\[
\boxed{
\widehat F_N\in\mathcal J,\ \widehat R_N\in\mathcal B
\Longrightarrow M_N\in\mathcal J,
}
\]

and symmetrically with entrance and exit interchanged.

The unit norm is equally important. `S_N` has the exact unit eigenvector `D_N^{1/2}\mathbf1`, so the scalar Green middle supplies **no strict Hilbert contraction and no automatic compactifying gain**. Thus after killing normalization it is ideal-neutral: it neither amplifies an already controlled conversion map nor manufactures the missing ideal decay. Any failure of a scalar-mediated route to the PF-281/PF-290 mixed target must occur in the normalized entrance map, the normalized reassembly map, or in the fact that the true nonconstant `P/H` response does not factor through this scalar chain at all.

This moves the live gate one step closer to the actual geometry. It is no longer useful to ask whether a long nearly conservative scalar return can by itself destroy a weak-Schatten or compactness estimate after the correct killing normalization. The discriminating calculation is to derive the true finite `P/H` source/reassembly maps and test `D_N^{-1/2}F_N` and `R_ND_N^{-1/2}` in the physical energy spaces.

## Claim

Use the scalar constant-mode pant chain of PF-303. Thus

\[
H_N=L_{c,N}+D_N,
\qquad
D_N=\operatorname{diag}(d_0,\ldots,d_N),
\qquad d_j>0,
\tag{1}
\]

where `L_{c,N}\ge0` is the weighted path Laplacian, and put

\[
G_N:=H_N^{-1}.
\tag{2}
\]

Define

\[
S_N:=D_N^{1/2}G_ND_N^{1/2}.
\tag{3}
\]

Then:

1. `S_N` is positive self-adjoint and
   \[
   \boxed{0<S_N\le I.}
   \tag{4}
   \]
2. the vector
   \[
   v_N:=D_N^{1/2}\mathbf1
   \tag{5}
   \]
   is nonzero and satisfies
   \[
   \boxed{S_Nv_N=v_N,}
   \tag{6}
   \]
   so
   \[
   \boxed{\|S_N\|=1.}
   \tag{7}
   \]
3. for arbitrary Hilbert spaces `X,Y` and bounded maps
   \[
   F_N:X\to\mathbb C^{N+1},
   \qquad
   R_N:\mathbb C^{N+1}\to Y,
   \tag{8}
   \]
   define
   \[
   \widehat F_N:=D_N^{-1/2}F_N,
   \qquad
   \widehat R_N:=R_ND_N^{-1/2}.
   \tag{9}
   \]
   Then
   \[
   \boxed{
   R_NG_NF_N
   =\widehat R_NS_N\widehat F_N.
   }
   \tag{10}
   \]
4. if `\widehat F_N` is compact, then for every `j>=1`,
   \[
   \boxed{
   s_j(R_NG_NF_N)
   \le \|\widehat R_N\|\,s_j(\widehat F_N).
   }
   \tag{11}
   \]
   If `\widehat R_N` is compact, then
   \[
   \boxed{
   s_j(R_NG_NF_N)
   \le \|\widehat F_N\|\,s_j(\widehat R_N).
   }
   \tag{12}
   \]
5. therefore every two-sided symmetric ideal `\mathcal J` obeys
   \[
   \boxed{
   \widehat F_N\in\mathcal J,
   \ \widehat R_N\in\mathcal B
   \Longrightarrow
   R_NG_NF_N\in\mathcal J,
   }
   \tag{13}
   \]
   and the symmetric implication with `F_N,R_N` interchanged.

The inequalities are dimension-free. If a family of finite sections has a uniform bound on the ordinary normalized conversion vertex and a uniform ideal bound on the other normalized vertex, the same uniform ideal bound propagates through the scalar Green middle with no factor depending on return depth.

## 1. Killing normalization turns the Green operator into a positive contraction

Because

\[
H_N=L_{c,N}+D_N\ge D_N>0,
\tag{14}
\]

operator monotonicity of inversion gives

\[
0<G_N=H_N^{-1}\le D_N^{-1}.
\tag{15}
\]

Conjugating by `D_N^{1/2}` yields immediately

\[
0<S_N\le I,
\tag{16}
\]

which is (4).

PF-303 proves

\[
G_Nd=\mathbf1,
\qquad d=D_N\mathbf1.
\tag{17}
\]

Therefore

\[
S_ND_N^{1/2}\mathbf1
=D_N^{1/2}G_ND_N\mathbf1
=D_N^{1/2}\mathbf1.
\tag{18}
\]

Thus `1` is an eigenvalue of `S_N`. Combined with (16), this proves (6)--(7).

This is the Hilbert-space counterpart of PF-304's reversible Markov statement. Indeed `G_ND_N` is similar to `S_N` via `D_N^{1/2}`, so the Markov fixed vector becomes the unit-energy direction (5). The normalization removes the apparent long-lifetime amplification but does not create a spectral gap.

## 2. Every scalar-mediated mixed response has two conversion vertices and a neutral middle

Equation (3) is equivalent to

\[
G_N=D_N^{-1/2}S_ND_N^{-1/2}.
\tag{19}
\]

Substituting (19) into `M_N=R_NG_NF_N` gives

\[
M_N
=(R_ND_N^{-1/2})
S_N
(D_N^{-1/2}F_N),
\tag{20}
\]

which is exactly (10).

The factors have a direct interpretation for the accepted clue. `D_N^{-1/2}F_N` measures whether the physical source enters the scalar chain at a scale compatible with the local Robin killing. `R_ND_N^{-1/2}` measures whether a scalar response can be reassembled into the desired physical output without paying more than the same killing scale. The complete scalar recurrence sits between them as the contraction `S_N`.

No assumption that the actual PF response has this factorization is made. Equation (20) says what follows **if and only if** a proposed part of the physical response has genuinely been reduced to the PF-303 scalar killed chain. It therefore gives a falsification test for any such reduction: an uncontrolled factor of `D_N^{-1/2}` cannot be hidden inside the phrase “the scalar Green function is bounded.”

## 3. Symmetric-ideal decay cannot be lost inside the scalar reservoir

For compact `A` and bounded `B,C`, the elementary singular-value inequality

\[
s_j(BAC)\le\|B\|\,\|C\|\,s_j(A)
\tag{21}
\]

applies. Taking `A=\widehat F_N`, `B=\widehat R_NS_N`, `C=I`, and using `\|S_N\|=1` gives (11). Taking `A=\widehat R_N`, `C=S_N\widehat F_N` gives (12).

Every two-sided symmetric ideal is stable under bounded left and right multiplication, so (13) follows. In particular the conclusion applies to compact operators, Schatten classes, and weak/Lorentz Schatten ideals such as `\mathcal S_{1,\infty}`.

This is exactly the kind of stability needed to compare the scalar return mechanism with the PF-281/PF-282 mixed-frequency target. A long scalar reservoir may make the unnormalized maps `F_N` or `R_N` look badly conditioned because `d_j` can be small, but after exposing the canonical `D_N^{-1/2}` factors the middle Green operator contributes no further loss of ideal class.

## 4. The scalar Green middle also supplies no hidden ideal gain

The contraction estimate must not be overread. Equation (6) gives an exact unit singular direction for every finite section. Hence one cannot obtain a strict contraction factor from `S_N`, and no argument may assign a uniform factor `<1` to each scalar Green passage merely because killing is present.

There is also no abstract compactifying mechanism in the middle. The degenerate calibration `L_{c,N}=0` gives `H_N=D_N` and `S_N=I` exactly. The actual PF chain has nonzero conductances, but (6) shows that the conservative direction survives exactly after killing normalization. Any decay in singular values of a scalar-mediated mixed map must therefore come from the conversion vertices or from additional physical structure outside the scalar compression.

This complements PF-297 and PF-298. PF-297 removes the fixed-axis Robin normalization as a source of `q`-moment amplification but also rules out a uniform Robin contraction gap. PF-298 removes a uniform one-pant scalar contraction gap. PF-303/PF-304 then show that accumulated scalar killing has a perfectly controlled Green potential. The present result says that, in the natural Hilbert killing currency, that complete scalar potential is **neutral for operator ideals**.

## 5. Consequence for the actual `P/H` gate

The accepted source-weighted-return clue ultimately serves PF-290/PF-281: control the physical low/high mixed response strongly enough to force the local high-band shorting deficits to vanish, or expose a persistent heavy-angle obstruction.

PF-305 reduces the scalar-mediated part of that task to a concrete map-level test. If a contribution to the actual finite `P/H` response can be written

\[
M_N=R_NG_NF_N,
\tag{22}
\]

then the scalar return depth is no longer an independent obstruction after killing normalization. One must determine instead whether

\[
D_N^{-1/2}F_N
\tag{23}
\]

and

\[
R_ND_N^{-1/2}
\tag{24}
\]

are uniformly bounded/compact/in the required symmetric ideal in the **actual physical energy spaces**.

A positive result for either conversion vertex, with the other uniformly bounded, propagates through the full scalar Green response by (11)--(13). A negative result is equally informative: if one normalized conversion blows up or retains a noncompact tail, then the obstruction has been localized to source injection or nonconstant physical reassembly rather than to a vague “nearly conservative return.”

The cheapest next calculation is therefore not another estimate of `G_N`. It is to derive the genuine finite-section `P/H` source map and scalar-to-physical reassembly map, if such a scalar factorization exists, and inspect the two `D_N^{-1/2}`-normalized vertices. If the physical response cannot be factored through the scalar chain because nonconstant modes are inseparable, that failure itself identifies the first operator that must replace the scalar model.

## 6. Prior art and novelty audit

The abstract operator ingredients are classical. Loewner order under inversion, singular-value inequalities under bounded multiplication, and two-sided symmetric-ideal stability are standard functional/trace-ideal theory; PF-280 already uses the same ideal-sandwich principle in a different `P/H` block-resolvent setting. PF-303/PF-304 identify the killed-network/Markov structure of the scalar prime-flute chain.

No novelty is claimed for (21), for symmetric ideals, for reversible Markov contractions, or for the algebraic factorization of a positive Green operator by `D_N^{\pm1/2}`. A structure-directed literature check found the expected trace-ideal and Markov/operator background and no reason to treat the abstract lemma as new.

The Mathia-specific contribution is the placement of those classical facts at the current PF-296/PF-303/PF-304 junction: the exact Robin killing `D_N` is the normalization that makes the **entire accumulated scalar Green reservoir** an ideal-neutral contraction, so any remaining PF-281/PF-290 difficulty in a scalar-mediated route is forced onto the physical entrance/reassembly maps. That route-level statement is derived from the persisted PF identities rather than imported as a new general theorem.

## 7. Boundaries and falsification tests

1. **Scalar constant-mode chain only.** PF-305 does not prove that constants form an invariant or reducing sector of the full one-cusp-pant boundary problem. PF-298 explicitly warns that nonconstant modes and physical `P/H` projections remain.
2. **A conditional factorization, not the physical response.** The theorem does not construct `F_N` or `R_N`. A claim that the actual mixed response equals (22) must be proved separately.
3. **Small killing can move the difficulty to the vertices.** Although `S_N` is uniformly contractive, `D_N^{-1/2}` may be large where the Robin killing is small. The result exposes this cost; it does not remove it.
4. **Finite sections do not automatically assemble globally.** Uniform finite-section ideal bounds are useful, but a global direct-sum or overlapping-window operator still requires the counting/summability/localization argument appropriate to the target ideal.
5. **No converse.** Failure to place either normalized vertex in one chosen sufficient ideal does not prove that the full mixed response fails that ideal; cancellation between more complete non-scalar terms may remain.
6. **No arithmetic discrimination.** The proof uses only the positive killed-conductance structure. Matched surrogate pant chains with the same structural hypotheses obey the same statement. Any RH-relevant arithmetic content must enter through the actual conversion/reassembly maps or later observable.
7. **Direct falsification.** An error must occur in the PF-303 identity `G_ND_N\mathbf1=\mathbf1`, the order `H_N\ge D_N`, or the elementary factorization/singular-value inequalities. No additional prime-distribution theorem is used.

## Consequence for the research line

The scalar-return subproblem is now sharply separated from the physical mixed-conversion subproblem. PF-303/PF-304 already show that scalar killing compensates long return lifetime. PF-305 adds that after the same canonical killing normalization, the scalar Green reservoir cannot degrade a compactness or weak-Schatten estimate carried by a conversion vertex and cannot create such decay on its own.

The live question is therefore concrete: **what are the actual `D_N^{-1/2}`-normalized entrance and reassembly maps for the finite `P/H` response, and do they remain controlled in the physical energy/Sobolev currencies required by PF-296, PF-292, and PF-290?**