# PF-313 — bounded source-weighted Green strength is exactly defect-scale source avoidance

**Status:** `EXACT-DERIVED + CLASSICAL-FACTORIZATION + POSITIVE/ROUTE-NARROWING`.

PF-312 removes a misleading degree of freedom from the post-low-screening problem. After the physical-low sector is shorted, inversion does not create a new normalized constant/high angle: the mixed Green block is the same normalized angle surrounded by two diagonal Green-strength factors. The remaining left-hand quantity is therefore

\[
\mathcal G_C^{1/2}J_C,
\]

where `J_C` is the actual source map into the post-low constant sector. PF-308 already proves that the coarse scalar-killing source family does **not** stay bounded after nonconstant screening, but it leaves the required selectivity of a successful physical source qualitative.

There is an exact finite-section criterion. Let

\[
\mathcal B=
\begin{pmatrix}
S&E\\
E^*&R
\end{pmatrix}>0,
\qquad
T=S^{-1/2}ER^{-1/2},
\]

be the post-low constant/high form from PF-311--PF-312, and put

\[
F_C:=S-ER^{-1}E^*
=S^{1/2}(I-TT^*)S^{1/2}.
\]

Then the constant diagonal Green block is exactly `\mathcal G_C=F_C^{-1}`. For **any** source map `J_C:\mathcal U\to\mathcal C`,

\[
\boxed{
\|\mathcal G_C^{1/2}J_C\|^2
=
\sup_{x\ne0}
\frac{\|J_C^*x\|^2}{\langle x,F_Cx\rangle}.
}
\tag{1}
\]

Consequently a depth-uniform bound `\|\mathcal G_C^{1/2}J_C\|\le K` is equivalent to the form domination

\[
\boxed{J_CJ_C^*\le K^2F_C.}
\tag{2}
\]

In whitened coordinates `\widehat J_C=S^{-1/2}J_C`, this becomes

\[
\boxed{
\widehat J_C\widehat J_C^*
\le
K^2(I-TT^*).
}
\tag{3}
\]

Thus a source may remain harmless while `\|T\|\uparrow1`, but only if it dies at the **defect scale** on the near-unit singular directions. If `Tv=\sigma u` and `T^*u=\sigma v`, then every bound in (3) forces

\[
\boxed{
\|\widehat J_C^*u\|
\le K\sqrt{1-\sigma^2}.
}
\tag{4}
\]

Conversely, any sequence of singular directions for which the left side of (4) is larger than the defect scale forces the source-weighted Green factor to diverge. The right-hand source/reassembly factor has the symmetric criterion with `R-E^*S^{-1}E` and `I-T^*T`.

Applied to the explicit PF-308 screened traces, this turns the previously qualitative phrase “the physical source must avoid the large Green directions” into a quantitative necessary condition. If `t^{(M)}` is the PF-308 trace, with

\[
\langle t^{(M)},D_Mt^{(M)}\rangle\ge cM,
\qquad
\langle t^{(M)},H_M^{\mathrm{eff}}t^{(M)}\rangle
\le C\bigl(1+\log M+MP_M^{-\eta}\bigr),
\]

then every source family with

\[
\sup_M\|(H_M^{\mathrm{eff}})^{-1/2}J_M\|<\infty
\]

must satisfy

\[
\boxed{
\frac{\|J_M^*t^{(M)}\|}
{\|D_M^{1/2}t^{(M)}\|}
\lesssim
\sqrt{\frac{1+\log M+MP_M^{-\eta}}{M}}
\longrightarrow0.
}
\tag{5}
\]

If instead that normalized source overlap is bounded below along a subsequence, the source-weighted Green strength diverges at least at the reciprocal rate. Hence any successful positive source-weighted-return route must be genuinely more selective than the PF-303 killing currency on the known screened tail witnesses.

This does not prove the final mixed response is large or small. A divergent left strength can still be killed by the middle angle, the right reassembly map, or signed cancellation. What it does prove is that **uniform source-weighted diagonal control is no longer an inverse problem**: it is exactly a source-versus-fully-shorted-energy domination problem, with an explicit defect-scale and an explicit prime-flute witness audit.

## Claim

Fix a finite canonical Galerkin section of the PF-311 post-low problem and write

\[
\mathcal B=
\begin{pmatrix}
S&E\\
E^*&R
\end{pmatrix}>0,
\tag{6}
\]

with `S>0`, `R>0`. Define

\[
T:=S^{-1/2}ER^{-1/2},
\qquad
D_C:=(I-TT^*)^{1/2},
\qquad
D_H:=(I-T^*T)^{1/2},
\tag{7}
\]

and the complementary Schur forms

\[
F_C:=S-ER^{-1}E^*=S^{1/2}D_C^2S^{1/2},
\tag{8}
\]

\[
F_H:=R-E^*S^{-1}E=R^{1/2}D_H^2R^{1/2}.
\tag{9}
\]

The diagonal blocks of `\mathcal B^{-1}` are

\[
\mathcal G_C=F_C^{-1},
\qquad
\mathcal G_H=F_H^{-1}.
\tag{10}
\]

Let `J_C:\mathcal U_C\to\mathcal C` and `J_H:\mathcal U_H\to\mathcal H` be arbitrary finite-dimensional source/reassembly maps. Then:

1. the exact variational identities are
   \[
   \boxed{
   \|\mathcal G_C^{1/2}J_C\|^2
   =
   \sup_{x\ne0}
   \frac{\|J_C^*x\|^2}{\langle x,F_Cx\rangle},
   }
   \tag{11}
   \]
   and symmetrically
   \[
   \boxed{
   \|\mathcal G_H^{1/2}J_H\|^2
   =
   \sup_{y\ne0}
   \frac{\|J_H^*y\|^2}{\langle y,F_Hy\rangle};
   }
   \tag{12}
   \]
2. for any `K\ge0`,
   \[
   \boxed{
   \|\mathcal G_C^{1/2}J_C\|\le K
   \iff
   J_CJ_C^*\le K^2F_C;
   }
   \tag{13}
   \]
3. with `\widehat J_C:=S^{-1/2}J_C`, condition (13) is equivalent to
   \[
   \boxed{
   \widehat J_C\widehat J_C^*
   \le K^2D_C^2
   =K^2(I-TT^*);
   }
   \tag{14}
   \]
   equivalently, there exists a contraction-scale factor `C_C` with `\|C_C\|\le K` such that
   \[
   \boxed{\widehat J_C=D_CC_C;}
   \tag{15}
   \]
4. if `Tv=\sigma u`, `T^*u=\sigma v` with unit vectors `u,v`, then (14) implies
   \[
   \boxed{
   \|\widehat J_C^*u\|^2
   \le K^2(1-\sigma^2),
   }
   \tag{16}
   \]
   and the symmetric right-hand estimate
   \[
   \boxed{
   \|\widehat J_H^*v\|^2
   \le K^2(1-\sigma^2),
   \qquad
   \widehat J_H:=R^{-1/2}J_H;
   }
   \tag{17}
   \]
5. conversely, for every nonzero test vector `x`,
   \[
   \boxed{
   \|\mathcal G_C^{1/2}J_C\|^2
   \ge
   \frac{\|J_C^*x\|^2}{\langle x,F_Cx\rangle},
   }
   \tag{18}
   \]
   so any explicit family with source overlap large relative to the fully shorted energy gives a quantitative lower bound on the Green strength.

For the PF-308 canonical tail witnesses `t^{(M)}` and finite cutoffs `L(M)`, let `F_M=H_{M,L(M)}^{\mathrm{eff}}`. If a source family `J_M` obeys

\[
\sup_M\|F_M^{-1/2}J_M\|\le K,
\tag{19}
\]

then

\[
\boxed{
\frac{\|J_M^*t^{(M)}\|^2}
{\langle t^{(M)},D_Mt^{(M)}\rangle}
\le
K^2\frac{C}{c}
\left(
\frac{1+\log M}{M}+P_M^{-\eta}
\right)
\longrightarrow0.
}
\tag{20}
\]

Conversely, if for some `\varepsilon>0`

\[
\|J_M^*t^{(M)}\|^2
\ge
\varepsilon^2
\langle t^{(M)},D_Mt^{(M)}\rangle
\tag{21}
\]

along a subsequence, then

\[
\boxed{
\|F_M^{-1/2}J_M\|
\gtrsim
\varepsilon
\sqrt{
\frac{M}{1+\log M+MP_M^{-\eta}}
}
\longrightarrow\infty.
}
\tag{22}
\]

Thus (20) is not merely a convenient sufficient estimate: **asymptotic avoidance of the PF-308 screened traces is necessary for every uniformly bounded left source-weighted Green factor**.

## 1. The source-weighted Green norm is a dual-energy norm

Because `F_C>0`,

\[
\|\mathcal G_C^{1/2}J_C\|
=
\|F_C^{-1/2}J_C\|
=
\|J_C^*F_C^{-1/2}\|.
\tag{23}
\]

For `z=F_C^{1/2}x`,

\[
\frac{\|J_C^*x\|^2}{\langle x,F_Cx\rangle}
=
\frac{\|J_C^*F_C^{-1/2}z\|^2}{\|z\|^2}.
\tag{24}
\]

Taking the supremum proves (11). The same calculation proves (12).

Equation (13) follows directly as well. The operator bound `\|F_C^{-1/2}J_C\|\le K` is equivalent to

\[
F_C^{-1/2}J_CJ_C^*F_C^{-1/2}\le K^2I,
\]

and congruence by `F_C^{1/2}` gives exactly

\[
J_CJ_C^*\le K^2F_C.
\tag{25}
\]

This is the finite positive-definite form of Douglas majorization/factorization. No inverse estimate remains after (25): the source must simply be continuous in the fully shorted energy with a uniform constant.

## 2. Whitening shows the exact defect scale

Using (8), congruence by `S^{-1/2}` turns (25) into

\[
S^{-1/2}J_CJ_C^*S^{-1/2}
\le K^2D_C^2,
\tag{26}
\]

which is (14). In finite dimension `D_C>0`, so one may define

\[
C_C:=D_C^{-1}\widehat J_C.
\tag{27}
\]

Then (14) is exactly `C_CC_C^*\le K^2I`, proving (15). Conversely (15) immediately gives (14).

On a singular pair of `T`,

\[
D_Cu=\sqrt{1-\sigma^2}\,u,
\qquad
D_Hv=\sqrt{1-\sigma^2}\,v.
\tag{28}
\]

Taking the quadratic form of (14) on `u` yields (16); the right-hand argument gives (17).

This is sharper than saying that a source should “avoid” a near-unit angle direction. The required scale is fixed: an overlap of order one is fatal as `\sigma\uparrow1`, an overlap of order `\sqrt{1-\sigma^2}` is exactly critical for operator-norm boundedness, and stronger decay creates margin.

A per-singular-vector estimate such as (16) is necessary but, for a general multidimensional source, should not be mistaken for the full operator-order statement (14). The complete criterion is the Loewner domination/factorization, not independent scalar tests in an arbitrarily chosen basis.

## 3. PF-308 supplies an explicit necessary source-avoidance rate

PF-308 provides physical cuff-constant traces `t^{(M)}` satisfying

\[
\langle t^{(M)},D_Mt^{(M)}\rangle\ge cM
\tag{29}
\]

and, after a finite nonconstant Galerkin cutoff `L(M)`,

\[
\langle t^{(M)},F_Mt^{(M)}\rangle
\le C\bigl(1+\log M+MP_M^{-\eta}\bigr).
\tag{30}
\]

If (19) holds, equation (11) applied to `t^{(M)}` gives

\[
\|J_M^*t^{(M)}\|^2
\le K^2\langle t^{(M)},F_Mt^{(M)}\rangle.
\tag{31}
\]

Dividing by (29) and using (30) proves (20).

Conversely, (18), (21), (29), and (30) give

\[
\|F_M^{-1/2}J_M\|^2
\ge
\frac{
\varepsilon^2 cM
}{
C(1+\log M+MP_M^{-\eta})
},
\tag{32}
\]

which is (22).

PF-308 is recovered as the special coarse source `J_M=D_M^{1/2}`: its overlap with `t^{(M)}` is exactly the killing mass and therefore cannot satisfy the vanishing condition (20). The present theorem says what a more selective physical source must do differently.

## 4. Consequence for the accepted source-weighted-return clue

`CLUE-source-weighted-return-potential-controls-mixed-response` proposes a positive occupation/return estimate as a way to neutralize long nearly conservative return paths. PF-303 proves the desired mechanism exactly in the scalar chain, while PF-308 proves that scalar killing itself is too broad once nonconstant screening is restored. PF-312 then identifies the surviving source-weighted diagonal Green factors.

Equations (13)--(20) give the clue a sharper target. A return-potential estimate on the constant side is useful for the post-low mixed response only if, after translating its physical source into `J_C`, it implies the fully shorted form domination

\[
J_CJ_C^*\lesssim F_C,
\tag{33}
\]

or a stronger ideal-valued analogue. In the PF-308 screened directions this necessarily entails the vanishing overlap (20). Therefore the next physical calculation can be audited **before** solving a full inverse problem: derive the actual source map, pair it with `t^{(M)}`, and test whether it decays at least at the required screened-energy scale.

Failure of (20) kills the uniform left-strength version of the positive route immediately. Success does not finish the problem: one still needs the right reassembly factor and either ideal control or the middle-angle/cancellation information needed for the final physical observable.

## 5. Prior art and novelty audit

The abstract equivalence between operator majorization, range inclusion, and factorization is classical. R. G. Douglas, *On Majorization, Factorization, and Range Inclusion of Operators on Hilbert Space*, Proceedings of the American Mathematical Society **17** (1966), 413--415, DOI `10.1090/S0002-9939-1966-0203464-1`, proves the general Hilbert-space factorization theorem behind (13)--(15). The variational quotient in (11) is the standard dual norm associated with a positive form, and PF-306/PF-311 already audit the surrounding Schur-complement and shorted-operator algebra. No novelty is claimed for those abstract facts.

The proof here is finite-dimensional and derives (11)--(15) directly, so Douglas' theorem is prior-art classification rather than a hidden hypothesis. A structure-directed literature search located the expected Douglas/Schur-complement framework and no prime-flute-specific theorem supplying the source-overlap estimate.

The Mathia-specific content is the combination with the **persisted PF-308 screened witnesses** and the exact PF-312 post-low factorization. That combination yields the quantitative necessity (20)--(22): a successful physical source must become asymptotically invisible on a known family that carries macroscopic PF-303 killing mass but sublinear fully shorted energy. This is the new route-level information preserved here.

## 6. Boundaries and falsification tests

1. **Finite-section statement.** All equalities are exact on finite canonical Galerkin sections. An infinite-depth theorem requires convergence/domain control for the actual source maps and closed forms.
2. **The physical source is not yet identified.** `J_C` is deliberately arbitrary here. The result supplies the exact test once the canonical `P/H` source map is derived; it does not manufacture that map.
3. **Left-factor divergence is not mixed-response divergence.** Even if (22) holds, the normalized angle, right reassembly, or signed cancellation may annihilate the dangerous source directions. The theorem closes only a proposed uniform left-strength mechanism.
4. **Operator norm is not weak trace class.** Form domination gives the correct operator-norm source gate. Endpoint ideal membership needs singular-value/counting information beyond (13).
5. **The witness rate is one-sided.** PF-308 supplies a constant-side screened trace. No symmetric physical-high witness is asserted without a separate derivation.
6. **No arithmetic discrimination is created by Douglas factorization.** The abstract criterion is universal. Prime-flute specificity enters through the canonical screened traces and their `M`, `P_M`, and killing-energy asymptotics.

A finite algebra audit is immediate: choose arbitrary positive `S,R`, a strict contraction `T`, set `E=S^{1/2}TR^{1/2}`, form `F_C`, and verify numerically that the norm in (11) equals the largest generalized quotient there and that the smallest admissible constant in (13) is the same number. The decisive project audit is more important: derive the actual canonical source `J_M` and measure `\|J_M^*t^{(M)}\|` against the PF-308 killing mass. That single overlap test now decides whether uniform left source-weighted Green control remains viable on the known screened family.