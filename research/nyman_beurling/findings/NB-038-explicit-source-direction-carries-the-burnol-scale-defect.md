# NB-038 — an explicit source direction carries the Burnol-scale weighted-skeleton defect

**Status:** `EXACT-DERIVED + PRINCIPAL-ANGLE-NORMAL-FORM + EXPLICIT-SOURCE-DIRECTION + BURNOL-SCALE-SHARPENING + TARGET-ORACLE-BOUNDARY`. `NB-036` identifies the weighted-skeleton upper-section dependence with the defect pair `(Z_{M,N},eta_{M,N})`, and `NB-037` proves that this pair cannot be negligible at the Burnol scale. The defect is in fact much more localized: after whitening the explicit Vasyunin duals, the relative Gram defect is exactly the compression of the orthogonal-complement projector to the early-shell space, and one fully explicit Möbius/Vasyunin source direction already sees a scalar defect asymptotic to the complete finite Nyman distance squared.

Use the notation of `NB-034`--`NB-037`. Thus

\[
V:=V_N,
\qquad
P:=P_V,
\qquad
R:=I-P,
\qquad
E:=E_M=\operatorname{span}\{\mathbf 1_{I_t}:1\le t<M\},
\]

\[
B:=B_M,
\qquad
Z:=Z_{M,N},
\qquad
S:=B^{1/2}ZB^{1/2},
\qquad
r:=r_N=Re,
\qquad
d:=d_N=\|r\|.
\tag{1}
\]

Let `Lambda` be the synthesis operator whose columns are the explicit skeleton duals `lambda_j^(M)` of `NB-036`, indexed by `2<=j<=M`. Their Gram matrix is `B^{-1}` and their span is exactly `E`. Therefore

\[
F:=\Lambda B^{1/2}:\mathbb R^{M-1}\longrightarrow E
\tag{2}
\]

is an isometry onto `E`. The normalized defect has the exact projector form

\[
\boxed{S=F^*RF.}
\tag{3}
\]

Hence `0\preceq S\prec I`; equivalently, the eigenvalues of `S` are the squared sines of the principal angles between `E_M` and `V_N`, while those of `I-S=F^*PF` are the corresponding squared cosines. This is a finite identity, not an asymptotic analogy.

Now define the explicit source direction and whitened target-correlation defect

\[
\boxed{
a:=B^{1/2}u_M=F^*e,
\qquad
q:=B^{1/2}\eta_{M,N}=F^*r.
}
\tag{4}
\]

Then

\[
\|a\|^2=1-\frac1M,
\tag{5}
\]

and, writing

\[
e_E:=P_Ee=\mathbf 1_{(1/M,1]},
\qquad
e_T:=e-e_E=\mathbf 1_{(0,1/M]},
\qquad\|e_T\|=M^{-1/2},
\tag{6}
\]

one has the exact directional identities

\[
\boxed{
a^*Sa=\|Re_E\|^2,}
\qquad
\boxed{
a^*q=\langle e_E,r\rangle.}
\tag{7}
\]

Consequently

\[
\boxed{
\left|\sqrt{a^*Sa}-d\right|\le\frac1{\sqrt M},
}
\tag{8}
\]

and

\[
\boxed{
|a^*q-d^2|\le\frac d{\sqrt M}.
}
\tag{9}
\]

In particular,

\[
\boxed{
\frac{(d-M^{-1/2})_+^2}{1-1/M}
\le
\frac{a^*Sa}{a^*a}
\le
\frac{(d+M^{-1/2})^2}{1-1/M}.
}
\tag{10}
\]

Thus the large relative Gram defect of `NB-037` is not forced only in some unknown eigenvector. It is already visible in the known arithmetic direction `a=B_M^{1/2}u_M`.

For every predeclared moving cutoff with

\[
\frac{M}{\log N}\longrightarrow\infty,
\tag{11}
\]

Burnol's unconditional lower bound `d_N^2\gg1/\log N` gives `Md_N^2\to\infty`. Equations (8)--(10) therefore sharpen `NB-037` to

\[
\boxed{
a^*S_{M,N}a=(1+o(1))d_N^2,}
\tag{12}
\]

\[
\boxed{
\frac{a^*S_{M,N}a}{\|a\|^2}
=(1+o(1))d_N^2,
}
\tag{13}
\]

and

\[
\boxed{
a^*B_M^{1/2}\eta_{M,N}=(1+o(1))d_N^2.}
\tag{14}
\]

Hence

\[
\boxed{
\|S_{M,N}\|_{\mathrm{op}}
\ge(1-o(1))d_N^2
\gg\frac1{\log N},
}
\tag{15}
\]

and

\[
\boxed{
\|B_M^{1/2}\eta_{M,N}\|_2
\ge(1-o(1))d_N^2
\gg\frac1{\log N}.
}
\tag{16}
\]

The constants `1/4` and `1/2` in the corresponding norm lower bounds of `NB-037` can therefore be replaced asymptotically by `1` along this explicit direction. More importantly, the missing upper-section correction contains a multiplicatively accurate copy of the original finite Nyman distance in a source direction known before the upper section is solved.

## 1. Whitening the Vasyunin duals gives the principal-angle defect exactly

`NB-036` proves

\[
\Lambda^*\Lambda=B^{-1}
\tag{17}
\]

and defines

\[
z_j=R\lambda_j^{(M)},
\qquad
Z=(\langle z_i,z_j\rangle).
\tag{18}
\]

Thus

\[
F^*F
=B^{1/2}\Lambda^*\Lambda B^{1/2}
=I,
\tag{19}
\]

while

\[
F^*RF
=B^{1/2}\Lambda^*R\Lambda B^{1/2}
=B^{1/2}ZB^{1/2}
=S,
\tag{20}
\]

which proves (3). Since `F` is an isometry onto `E`, `F^*PF=I-S` is the finite compression of the projection onto `V_N`. The usual singular-value characterization of principal angles gives the interpretation stated above. No principal-angle theorem is needed for the quantitative conclusions; (20) is the load-bearing identity.

This also recovers the exact relative-metric quantity of `NB-037`:

\[
\left\|
\widehat H_{M,N}^{-1/2}
(B_M-\widehat H_{M,N})
\widehat H_{M,N}^{-1/2}
\right\|_{\mathrm{op}}
=\|S\|_{\mathrm{op}}.
\tag{21}
\]

The new point is that (20) supplies a geometrically canonical coordinate system in which a distinguished arithmetic direction can be tested directly.

## 2. The distinguished direction is the early-shell target itself

From `NB-036`,

\[
\Lambda^*e=u_M.
\tag{22}
\]

Hence `a=F^*e=B^{1/2}u_M`. Because `FF^*=P_E`,

\[
Fa=FF^*e=P_Ee=e_E.
\tag{23}
\]

Combining (3) and (23) yields

\[
a^*Sa
=\langle Fa,RFa\rangle
=\langle e_E,Re_E\rangle
=\|Re_E\|^2,
\tag{24}
\]

since `R` is an orthogonal projection. This proves the first identity in (7). Equation (5) follows at once from

\[
\|a\|^2=\|e_E\|^2=1-1/M,
\tag{25}
\]

and agrees with the source-vector identity of `NB-037`.

Likewise, because `r\in V_N^\perp`,

\[
\eta_j
=\langle r,z_j\rangle
=\langle r,R\lambda_j^{(M)}\rangle
=\langle r,\lambda_j^{(M)}\rangle.
\tag{26}
\]

Therefore `q=F^*r`, and

\[
a^*q=\langle Fa,r\rangle=\langle e_E,r\rangle,
\tag{27}
\]

proving the second identity in (7).

There is also an exact vector coupling between the two defects:

\[
\boxed{
q=Sa+F^*Re_T,
\qquad
\|q-Sa\|\le\sqrt{\frac{\|S\|_{\mathrm{op}}}{M}}.
}
\tag{28}
\]

Indeed `r=R(e_E+e_T)` and `e_E=Fa`, while

\[
\|F^*R\|^2=\|F^*RF\|=\|S\|_{\mathrm{op}}.
\tag{29}
\]

Thus `eta` and `Z` are not independent nuisance parameters after whitening: their target-relevant parts are coupled by the explicit early-shell source direction plus a geometric tail of norm `M^{-1/2}`.

## 3. The tail of the constant target is the only finite error

Because `r=Re=Re_E+Re_T`, contraction of an orthogonal projection gives

\[
\bigl|\|Re_E\|-\|r\|\bigr|
\le\|Re_T\|
\le\|e_T\|
=\frac1{\sqrt M},
\tag{30}
\]

which is (8). Squaring and using (25) gives (10).

For the target-correlation scalar, orthogonality of the best residual gives

\[
\langle e,r\rangle
=\langle Pe+r,r\rangle
=d^2.
\tag{31}
\]

Hence

\[
a^*q
=\langle e_E,r\rangle
=d^2-\langle e_T,r\rangle,
\tag{32}
\]

and Cauchy--Schwarz gives (9). These estimates are exact finite-section consequences of the early-shell decomposition and do not assume RH, density of the Nyman span, a Möbius asymptotic, or a model for the spectrum of `S`.

Under (11), Burnol gives

\[
\frac{1}{d\sqrt M}
\ll\sqrt{\frac{\log N}{M}}
\longrightarrow0.
\tag{33}
\]

Dividing (8) by `d` and (9) by `d^2` proves (12)--(14). Equations (15)--(16) follow by the Rayleigh and Cauchy--Schwarz inequalities.

## 4. Consequence for the weighted-skeleton oracle

The accepted clue `CLUE-weighted-skeleton-target-data-without-full-section-oracle` asks whether the well-conditioned quotient can be populated to RH-scale accuracy without an `N`-scale projection solve or `d_N` itself as an oracle. `NB-037` already rules out the zero-defect shortcut `H_tilde=B_M`. The present result makes the obstruction source-aligned.

At every cutoff satisfying (11), the single explicit scalar

\[
\boxed{
\mathfrak d_{M,N}:=
(B_M^{1/2}u_M)^*
(B_M^{1/2}Z_{M,N}B_M^{1/2})
(B_M^{1/2}u_M)
}
\tag{34}
\]

satisfies

\[
\boxed{
\mathfrak d_{M,N}=(1+o(1))d_N^2.
}
\tag{35}
\]

Thus a reduced construction that reconstructs the leading upper-section metric correction **along this known source direction** has already reconstructed the original finite Nyman distance to multiplicative `1+o(1)` accuracy. This is an information-localization statement, not an algorithmic lower bound: (35) does not prove that `mathfrak d_{M,N}` is expensive to compute, nor that every useful one-sided certificate must estimate it.

The boundary is nevertheless sharper than in `NB-037`. The missing source information cannot be blamed on an unknown bad eigenvector of the retained Gram geometry. A canonical Möbius/Vasyunin direction known from the early shells carries a Burnol-scale correction whose leading magnitude is the full finite distance itself. Any proposed `o(1/log N)` full-metric oracle must therefore explain how it obtains this particular directional correction without importing equivalent finite-distance information.

## 5. Prior-art and falsification boundary

The external inputs used quantitatively are already anchored in `SOURCES.md`: Vasyunin supplies the explicit finite-support biorthogonal system used in `NB-036`, and Burnol supplies the unconditional `d_N^2\gg1/\log N` scale. The projector whitening (3), directional identities (7), and asymptotics (12)--(16) are finite Hilbert-space consequences of those persisted structures.

Principal/Friedrichs-angle language is not novel in the Nyman--Beurling setting. Jongho Yang, *A Friedrichs angle between the Nyman-Beurling spaces and the Riemann hypothesis*, J. Math. Anal. Appl. 560 (2026), 130494, DOI `10.1016/j.jmaa.2026.130494`, studies a Friedrichs angle between two Nyman--Beurling subspaces. The present claim is narrower and different: it concerns the specific finite early-shell compression arising from the `NB-034` weighted quotient and the explicit source-direction identities (7)--(14). The available bibliographic record and abstract-level description do not supply this finite weighted-skeleton statement. This is not a priority claim; principal-angle theory itself is standard.

The decisive falsification test for (12)--(14) is entirely finite: verify (17), form the orthogonal projector `R`, check `S=F^*RF`, and compare `Fa` with `P_Ee`. Any failure of one of these exact identities invalidates the asymptotic conclusion. The result does not prove `d_N\to0`, does not improve Burnol's lower bound, does not give a computable upper bound for `d_N`, and does not close the accepted weighted-skeleton clue. It identifies a specific source-aligned quantity that any successful reduced oracle must confront rather than an additional route around the Nyman distance.