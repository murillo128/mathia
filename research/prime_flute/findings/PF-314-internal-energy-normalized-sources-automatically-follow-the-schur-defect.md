# PF-314 — internal energy-normalized sources automatically satisfy the Schur defect

**Status:** `EXACT-DERIVED + CLASSICAL-SCHUR-QUOTIENT + POSITIVE/ROUTE-NARROWING`.

PF-313 identifies the exact remaining left Green-strength gate after physical-low screening: a source map `J_C` into the post-low constant sector is uniformly harmless exactly when

\[
J_CJ_C^*\lesssim F_C,
\]

where `F_C=S-ER^{-1}E^*` is the fully shorted constant form. Equivalently, after whitening by `S`, the source must vanish on near-unit singular directions of

\[
T=S^{-1/2}ER^{-1/2}
\]

at the defect scale `(I-TT^*)^{1/2}`. PF-313 deliberately leaves the actual physical source unidentified.

There is one important source class for which this gate is automatic. Suppose the source is not an arbitrary external injection into the constant variables, but is the **residual coupling of another source sector of the same positive boundary form**. Reserve a finite source space `U`, a constant sector `C`, and a residual high sector `H`, and write the positive form as

\[
\mathcal M=
\begin{pmatrix}
A&J^*&K^*\\
J&S&E\\
K&E^*&R
\end{pmatrix}>0.
\]

Shorting `H` produces

\[
\mathcal M/H=
\begin{pmatrix}
A_H&J_H^*\\
J_H&F_C
\end{pmatrix}>0,
\]

with

\[
A_H=A-K^*R^{-1}K,
\qquad
J_H=J-ER^{-1}K,
\qquad
F_C=S-ER^{-1}E^*.
\]

Positivity of this two-block Schur complement forces

\[
\boxed{
J_HA_H^{-1}J_H^*\le F_C.
}
\tag{1}
\]

Since `0<A_H\le A`, inversion reverses the order and therefore

\[
\boxed{
J_HA^{-1}J_H^*\le F_C.
}
\tag{2}
\]

Thus an internal source normalized by its own source-sector energy already satisfies PF-313 with constant one. More generally, if `W:X\to U` is any external coefficient map whose source energy obeys

\[
\|A^{1/2}W\|\le K_0,
\]

then the induced residual constant source `J_C:=J_HW` satisfies

\[
\boxed{
J_CJ_C^*\le K_0^2F_C,
\qquad
\|F_C^{-1/2}J_C\|\le K_0.
}
\tag{3}
\]

In PF-313's whitened coordinates this becomes

\[
\boxed{
\widehat J_C\widehat J_C^*
\le K_0^2(I-TT^*),
\qquad
\widehat J_C:=S^{-1/2}J_HW,
}
\tag{4}
\]

so the required defect-scale source avoidance is not an extra estimate for this source class: it is a consequence of positivity and sequential shorting.

This gives a sharp representation test for the current prime-flute frontier. If the canonical physical forcing in the accepted source-weighted-return route is genuinely obtained by reserving an energy-normalized physical source sector of the same PF-205 positive form and shorting the remaining variables, then its **operator-norm diagonal Green strength cannot blow up independently**. If instead the physical forcing enters as a direct external injection such as the PF-308 killing source `D^{1/2}`, or through a coefficient map not uniformly bounded in the source energy, then PF-313 remains a real estimate and the missing amplification is precisely in that source map.

The distinction is visible on the PF-308 screened traces. Every internal energy-bounded source automatically obeys

\[
\|W^*J_H^*t^{(M)}\|^2
\le K_0^2\langle t^{(M)},F_Ct^{(M)}\rangle.
\]

For the canonical PF-308 witnesses the right side is sublinear while the Robin-killing mass is macroscopic, so their killing-normalized source overlap vanishes at exactly the PF-313 rate. The killing source itself fails this test because it is an external injection, not because positivity of the same three-block form has broken down.

This does not prove compactness, weak trace class, or the final mixed response estimate. It removes only one possible mechanism: **a source that is internal to the same positive form and uniformly normalized in its source energy cannot independently violate the PF-313 defect gate.** Any surviving obstruction must come from the normalized angle, multiplicity/ideal counting, target reassembly, signed structure, or from a source-coordinate map whose energy norm actually escapes.

## Claim

Let `U,C,H` be finite-dimensional Hilbert spaces and let

\[
\mathcal M=
\begin{pmatrix}
A&J^*&K^*\\
J&S&E\\
K&E^*&R
\end{pmatrix}>0
\tag{5}
\]

on `U\oplus C\oplus H`. Thus `A,S,R` are strictly positive. Define the result of shorting the `H` block by

\[
A_H:=A-K^*R^{-1}K,
\tag{6}
\]

\[
J_H:=J-ER^{-1}K,
\tag{7}
\]

\[
F_C:=S-ER^{-1}E^*.
\tag{8}
\]

Then:

1. the exact sequentially shorted form is
   \[
   \boxed{
   \mathcal M/H=
   \begin{pmatrix}
   A_H&J_H^*\\
   J_H&F_C
   \end{pmatrix}>0;
   }
   \tag{9}
   \]
2. its residual source coupling satisfies
   \[
   \boxed{
   J_HA_H^{-1}J_H^*<F_C,
   }
   \tag{10}
   \]
   and hence
   \[
   \boxed{
   \|F_C^{-1/2}J_HA_H^{-1/2}\|<1;
   }
   \tag{11}
   \]
3. because `A_H\le A`, one also has
   \[
   \boxed{
   J_HA^{-1}J_H^*\le F_C,
   \qquad
   \|F_C^{-1/2}J_HA^{-1/2}\|\le1;
   }
   \tag{12}
   \]
4. for every coefficient/source map `W:X\to U` satisfying
   \[
   \boxed{W W^*\le K_0^2A^{-1}}
   \tag{13}
   \]
   — equivalently `\|A^{1/2}W\|\le K_0` — the induced constant source `J_C:=J_HW` obeys
   \[
   \boxed{
   J_CJ_C^*\le K_0^2F_C,
   \qquad
   \|F_C^{-1/2}J_C\|\le K_0;
   }
   \tag{14}
   \]
5. defining
   \[
   T:=S^{-1/2}ER^{-1/2},
   \qquad
   \widehat J_C:=S^{-1/2}J_HW,
   \tag{15}
   \]
   one has the exact PF-313 defect domination
   \[
   \boxed{
   \widehat J_C\widehat J_C^*
   \le K_0^2(I-TT^*).
   }
   \tag{16}
   \]
   Consequently, if `Tv=\sigma u`, `T^*u=\sigma v`, then
   \[
   \boxed{
   \|\widehat J_C^*u\|
   \le K_0\sqrt{1-\sigma^2}.
   }
   \tag{17}
   \]

For any test vector `t\in C`, equation (14) also gives the source-overlap estimate

\[
\boxed{
\|W^*J_H^*t\|^2
\le K_0^2\langle t,F_Ct\rangle.
}
\tag{18}
\]

Therefore, whenever a family of PF-308 traces satisfies

\[
\langle t^{(M)},F_C^{(M)}t^{(M)}\rangle
\le C\bigl(1+\log M+MP_M^{-\eta}\bigr)
\tag{19}
\]

and

\[
\langle t^{(M)},D_Mt^{(M)}\rangle\ge cM,
\tag{20}
\]

every uniformly energy-bounded internal source family obeys

\[
\boxed{
\frac{\|W_M^*J_{H,M}^*t^{(M)}\|^2}
{\langle t^{(M)},D_Mt^{(M)}\rangle}
\lesssim
K_0^2\left(
\frac{1+\log M}{M}+P_M^{-\eta}
\right)
\longrightarrow0.
}
\tag{21}
\]

Equation (21) is exactly the kind of source-avoidance rate required by PF-313, but here it follows from the source representation rather than from a separate geometric estimate.

## 1. Sequential shorting exposes the residual source map

Fix `(u,c)\in U\oplus C`. The `H`-dependent part of the quadratic form of (5) is minimized at

\[
h_*(u,c)=-R^{-1}(Ku+E^*c).
\tag{22}
\]

Substitution gives

\[
\inf_h\langle(u,c,h),\mathcal M(u,c,h)\rangle
=
\left\langle
\binom uc,
\begin{pmatrix}
A_H&J_H^*\\
J_H&F_C
\end{pmatrix}
\binom uc
\right\rangle,
\tag{23}
\]

with exactly (6)--(8). Since the original finite form is strictly positive, its shorting is strictly positive, proving (9).

The formula for `J_H` is load-bearing. It is not the raw source/constant coupling `J`; it includes the indirect source-to-high-to-constant path

\[
-ER^{-1}K.
\tag{24}
\]

Thus the theorem applies after the same kind of residualization that PF-311 requires for the constant/high block. A candidate physical forcing cannot be declared “internal” merely because some raw local source column appears in the original matrix; the **post-elimination residual coupling** must be the actual source map used in the Green factor.

## 2. Positivity forces source domination by the fully shorted energy

Take the Schur complement of `A_H` in (9). Positivity gives

\[
F_C-J_HA_H^{-1}J_H^*>0,
\tag{25}
\]

which proves (10). Congruence by `F_C^{-1/2}` gives

\[
F_C^{-1/2}J_HA_H^{-1}J_H^*F_C^{-1/2}<I,
\tag{26}
\]

and therefore (11).

Shorting can only decrease the source-side diagonal form:

\[
0<A_H=A-K^*R^{-1}K\le A.
\tag{27}
\]

Hence inversion reverses the Loewner order,

\[
A^{-1}\le A_H^{-1}.
\tag{28}
\]

Multiplying by `J_H` and `J_H^*` preserves order, so

\[
J_HA^{-1}J_H^*
\le
J_HA_H^{-1}J_H^*
<F_C,
\tag{29}
\]

which is (12).

Now let `W` satisfy (13). Then

\[
J_HWW^*J_H^*
\le
K_0^2J_HA^{-1}J_H^*
\le
K_0^2F_C.
\tag{30}
\]

This is exactly (14). No Green inverse estimate has been used: the apparently dangerous inverse `F_C^{-1/2}` disappears because the source itself is forced by positivity to shrink with the same fully shorted energy.

This is the internal-source counterpart of PF-313. PF-313 says that **every** uniformly bounded source-weighted Green factor must satisfy a domination such as (14). The present result says that residual couplings from an energy-bounded source sector of the same positive form satisfy it automatically.

## 3. Whitening recovers the exact PF-313 defect scale

Factor the fully shorted constant form as

\[
F_C
=S^{1/2}(I-TT^*)S^{1/2},
\qquad
T=S^{-1/2}ER^{-1/2}.
\tag{31}
\]

Congruence of (30) by `S^{-1/2}` gives

\[
S^{-1/2}J_HWW^*J_H^*S^{-1/2}
\le
K_0^2(I-TT^*).
\tag{32}
\]

With `\widehat J_C=S^{-1/2}J_HW`, this is (16). On a singular pair of `T`,

\[
D_Cu=(I-TT^*)^{1/2}u
=\sqrt{1-\sigma^2}\,u.
\tag{33}
\]

Taking the quadratic form of (32) on `u` gives (17).

Thus an internal source cannot retain order-one normalized overlap with a post-low direction whose Schur defect tends to zero. If `\sigma\uparrow1`, positivity makes the source disappear from that direction at least as `\sqrt{1-\sigma^2}`. This is not an additional geometric miracle; it is the compatibility condition required for the larger three-block form itself to remain positive.

The statement is stronger than a test on one singular vector because (16) is an operator-order inequality. It controls all near-unit directions simultaneously and remains basis independent.

## 4. PF-308 becomes a representation discriminator

PF-313 turns the explicit PF-308 traces into a necessary source audit. Equations (18)--(21) show that this audit has a sharp interpretation.

If the proposed source map is of the internal form `J_HW` with `\sup_M\|A_M^{1/2}W_M\|<\infty`, then the PF-308 source-overlap condition is automatic. In particular, the source cannot see those screened traces at the macroscopic PF-303 killing scale; its overlap is bounded by the much smaller fully shorted energy.

By contrast, PF-308's killing-normalized source is the direct injection

\[
J_M=D_M^{1/2}.
\tag{34}
\]

PF-308 proves that this map does **not** obey a uniform domination `D_M\lesssim F_M`. The present theorem therefore does not rescue it. Instead it explains the distinction: `D_M^{1/2}` is an externally chosen normalization of the constant sector, not the residual coupling of an energy-normalized source sector whose positivity is coupled to `F_M`.

This gives the known screened family a new use. It is not only a counterexample to coarse killing normalization. It tests whether a proposed “physical source” has really been derived from the common positive form. If a claimed internal energy-normalized source has order-one killing-normalized overlap with `t^{(M)}`, then at least one of the following is wrong: the claimed residual source formula, the source-energy normalization, or the identification of the fully shorted form used in PF-313.

## 5. Consequence for the source-weighted-return route

The accepted `CLUE-source-weighted-return-potential-controls-mixed-response` asks whether repeated return/reassembly can populate PF-296 source rows so strongly that the normalized response escapes the positive Sobolev control. PF-303 proves a scalar deficit-potential identity; PF-308 shows that scalar killing is too broad after nonconstant screening; PF-312 separates diagonal Green strengths from the unchanged normalized angle; PF-313 converts the left diagonal strength into a source-domination problem.

The present result inserts a representation gate **before** another Green-potential estimate is attempted.

For the actual finite-section forcing, reserve the source degrees of freedom that encode the normalized physical input and perform the same eliminations used to obtain the post-low `C/H` form. Then ask whether the induced constant source is exactly a residual block `J_H W` of the resulting common positive form, with

\[
\sup\|A^{1/2}W\|<\infty.
\tag{35}
\]

If yes, the operator-norm left Green-strength problem is already closed by (14). A return-potential argument may still be needed for a **stronger currency** — for example PF-296's `\ell^1(q)` source moment, singular-value decay, multiplicity/counting, or a signed target reconstruction — but it is no longer needed merely to prevent uniform diagonal Green blow-up.

If no, the failure should be made explicit. The physical forcing must factor through an additional map not controlled by the source-side energy, or it must enter as a direct external injection. That mismatch map is then the correct object for the PF-313 overlap test and for any source-weighted return theorem. Calling the forcing “physical” does not itself provide the domination.

This is a narrower and cheaper next calculation than constructing a global return kernel first: **derive the exact source block and its source-energy normalization through the current elimination order.** Only after that classification is it clear which Green-potential problem actually remains.

## 6. Prior art and novelty audit

The abstract matrix theory is classical. Positivity of a two-block matrix and the resulting Schur-complement inequality behind (25) are standard. Sequential elimination and the identity (9) are instances of the Crabtree--Haynsworth quotient formula for Schur complements; F. Zhang, *A Matrix Identity on the Schur Complement*, Linear and Multilinear Algebra **52** (2004), 367--373, DOI `10.1080/03081080310001645172`, gives a direct modern treatment of that quotient identity. Generalized Schur-complement variants and their positivity inequalities go back at least to Carlson, Haynsworth and Markham, *A Generalization of the Schur Complement by Means of the Moore--Penrose Inverse*, SIAM Journal on Applied Mathematics **26** (1974), 169--175, DOI `10.1137/0126013`.

The factorization interpretation of (10)--(14) is also within classical Douglas majorization/range-inclusion theory; PF-313 already cites R. G. Douglas, *On Majorization, Factorization, and Range Inclusion of Operators on Hilbert Space*, Proceedings of the AMS **17** (1966), 413--415. No novelty is claimed for Schur complements, order reversal under inversion, operator majorization, or the fact that a normalized cross block of a positive matrix is contractive.

A structure-directed literature audit located exactly this classical Schur/quotient/factorization framework. It did not locate a prime-flute-specific theorem corresponding to the project-level conclusion (21). The Mathia-specific content is therefore the placement of the classical positivity identity **after the PF-311/PF-312 post-low elimination and against PF-313's explicit source gate and PF-308's screened traces**. That placement separates two physically different source classes that PF-313 intentionally left merged: internal residual couplings, for which defect avoidance is automatic, and external injections, for which it remains a genuine estimate.

## 7. Boundaries and falsification tests

1. **Finite sections.** The theorem is exact for finite positive sections. Passing to an infinite boundary form requires the usual closed-form/shorted-operator domain control and a justified limiting source map.
2. **Internal means residual after elimination.** The raw block `J` is not enough. The relevant source is `J_H=J-ER^{-1}K`. Ignoring the indirect term can produce a false source classification.
3. **The source energy is load-bearing.** A coefficient map `W` is harmless only under a uniform bound in the `A`-energy, or more strongly the `A_H`-energy. A Hilbert-norm, `q`-weight, or killing normalization is not interchangeable with this without a proved comparison.
4. **External injections remain open.** PF-308's `D^{1/2}` source is the explicit counterexample showing why arbitrary injections do not inherit (14).
5. **Operator norm is not ideal decay.** A contraction-scale source bound does not imply compactness, weak `\mathcal S_{1,\infty}`, summable source-row moments, or any multiplicity estimate.
6. **One-sided result.** The same algebra applies symmetrically to a target/reassembly sector when it is represented as an internal energy-normalized residual coupling, but no such identification is asserted here for the canonical target map.
7. **No arithmetic discrimination.** The block positivity theorem is universal. Prime-flute content enters only through the canonical elimination, the physical source identification still to be done, and the PF-308 screened witness asymptotics.

A direct finite-dimensional audit is immediate: generate any positive three-block matrix (5), compute the three residual blocks (6)--(8), and verify that the largest singular value of `F_C^{-1/2}J_HA_H^{-1/2}` is below one and that `F_C-J_HA^{-1}J_H^*` is positive. The decisive project audit is representational rather than numerical: derive the actual normalized PF source through the current `P/H` elimination and determine whether it is of the internal form covered by (14).

## Consequence for the research line

PF-313 left “prove defect-scale source avoidance” as the immediate left-strength problem. PF-314 splits that question into two cases.

For **internal energy-normalized sources**, defect-scale avoidance is automatic and the left diagonal Green-strength mechanism is closed at operator-norm level. The research effort should move to the exact source representation, target/reassembly, ideal/multiplicity control, or the normalized post-low angle.

For **external or energy-uncontrolled sources**, nothing is rescued: PF-313 remains the exact gate, and PF-308 gives a concrete family on which a source-overlap estimate must be proved or falsified.

The next discriminating calculation is therefore to derive the canonical physical forcing as an actual residual block through the same sequential shorting used in PF-311. If that derivation lands in the internal class, do not spend another pass proving an operator-norm Green bound that positivity already supplies. If it does not, isolate the precise mismatch map and test it against PF-313/PF-308.