# PF-308 — screened tail blocks force killing-normalized Schur backreaction to diverge

**Status:** `EXACT-DERIVED + ASYMPTOTIC-DERIVED + DECISIVE/ROUTE-NARROWING`.

PF-305 proves that the scalar constant-mode Green reservoir is harmless after the exact PF-303 Robin-killing normalization. PF-306 then identifies the first omitted operator: after the nonconstant boundary modes are restored and shorted, the killing-normalized constant Green block becomes

\[
\widetilde S_N
=D_N^{1/2}(H_N^{\mathrm{eff}})^{-1}D_N^{1/2}
=X_N^*(I-C_NC_N^*)^{-1}X_N,
\]

where `D_N` is the assembled scalar Robin killing, `H_N^{\mathrm{eff}}` is the constant form after optimal nonconstant relaxation, and `C_N` is the normalized constant/nonconstant Schur conversion. PF-307 shows that `\|C_N\|\to1` along canonical tail sections but deliberately leaves open whether the killing-normalized source avoids the nearly screened directions.

It does not. The explicit PF-217 screened tail blocks carry **macroscopic PF-303 killing mass** at the same time that their fully shorted energy is sublinear. More precisely, for the PF-217 block scale `M` there are physical cuff-constant traces `t^{(M)}` and finite tangential cutoffs `L(M)` such that, for some fixed `c,C,\eta>0`,

\[
\boxed{
\langle t^{(M)},D_M t^{(M)}\rangle\ge cM,
}
\]

while

\[
\boxed{
\langle t^{(M)},H_{M,L(M)}^{\mathrm{eff}}t^{(M)}\rangle
\le C\bigl(1+\log M+MP_M^{-\eta}\bigr).
}
\]

The generalized Rayleigh quotient therefore gives

\[
\boxed{
\|\widetilde S_{M,L(M)}\|
\ge
\frac{cM}{C(1+\log M+MP_M^{-\eta})}
\gtrsim
\frac{1}{(1+\log M)/M+P_M^{-\eta}}
\longrightarrow\infty.
}
\]

Thus PF-307's near-unit Schur angle is not hidden from the **canonical killing-normalized constant source family**. The scalar normalization that exactly neutralizes return depth in PF-305 cannot neutralize the subsequent nonconstant screening backreaction. Any surviving positive route must be more selective than the full killing-normalized constant sector: it must exploit the actual physical `P/H` source range, target reassembly, signed cancellation, or a counting/ideal mechanism that does not require a uniform bound on `\widetilde S_{M,L}`.

This does **not** prove that the final physical `P/H` mixed response is unbounded, noncompact, or outside weak trace class. PF-306 already separates further source and target vertices from the constant Green block. The result closes one narrower possibility: after PF-307, one cannot hope that PF-303 killing normalization by itself makes the nearly screened constant directions source-invisible.

## Claim

Use the canonical PF-205 simultaneous seam cut and the positive shifted boundary form of PF-216--PF-217. On a finite tail section, retain all cuff-constant variables and a finite set of nonconstant tangential modes, and write the positive form as in PF-306,

\[
\mathcal A_{M,L}
=
\begin{pmatrix}
H_M&B_{M,L}\\
B_{M,L}^*&J_{M,L}
\end{pmatrix}>0.
\tag{1}
\]

Here `H_M` is the PF-298/PF-303 scalar constant compression in physical cuff-constant coordinates, with

\[
H_M=L_{c,M}+D_M,
\qquad
D_M>0,
\tag{2}
\]

and the shorted constant form is

\[
H_{M,L}^{\mathrm{eff}}
:=H_M-B_{M,L}J_{M,L}^{-1}B_{M,L}^*.
\tag{3}
\]

Define

\[
C_{M,L}:=H_M^{-1/2}B_{M,L}J_{M,L}^{-1/2}
\tag{4}
\]

and

\[
X_M:=H_M^{-1/2}D_M^{1/2}.
\tag{5}
\]

Then

\[
H_{M,L}^{\mathrm{eff}}
=H_M^{1/2}(I-C_{M,L}C_{M,L}^*)H_M^{1/2}
\tag{6}
\]

and the killing-normalized full constant Green block is

\[
\boxed{
\widetilde S_{M,L}
:=D_M^{1/2}(H_{M,L}^{\mathrm{eff}})^{-1}D_M^{1/2}
=X_M^*(I-C_{M,L}C_{M,L}^*)^{-1}X_M.
}
\tag{7}
\]

There exist `\eta>0`, a sequence `M\to\infty`, finite cutoffs `L(M)\to\infty`, and nonzero cuff-constant traces `t^{(M)}` supported on the PF-217 blocks `M\le n\le2M` such that

\[
\boxed{
\langle t^{(M)},D_Mt^{(M)}\rangle\ge cM
}
\tag{8}
\]

and

\[
\boxed{
\langle t^{(M)},H_{M,L(M)}^{\mathrm{eff}}t^{(M)}\rangle
\le C\bigl(1+\log M+MP_M^{-\eta}\bigr).
}
\tag{9}
\]

Consequently

\[
\boxed{
\|\widetilde S_{M,L(M)}\|
\ge
\frac{\langle t^{(M)},D_Mt^{(M)}\rangle}
{\langle t^{(M)},H_{M,L(M)}^{\mathrm{eff}}t^{(M)}\rangle}
\gtrsim
\frac{1}{(1+\log M)/M+P_M^{-\eta}}
\to\infty.
}
\tag{10}
\]

Equivalently, the family of killing-normalized constant Green blocks has no tail-uniform operator bound once the canonical nonconstant screening sector is restored.

## 1. The PF-217 screened profile has macroscopic Robin-killing mass

PF-217 works with a block `M\le n\le2M` and chooses the discrete sine envelope

\[
z_n=
\sin\!\left(\frac{\pi(n-M)}{M}\right)
\tag{11}
\]

on that block. Its tangential bump has physical cuff mean

\[
t_n
=z_n\frac{I_\chi R_M}{L_n},
\qquad
R_M=\varepsilon\log P_M.
\tag{12}
\]

PF-217 proves uniformly on the block that

\[
\boxed{|t_n|\asymp|z_n|.}
\tag{13}
\]

For the pant between two consecutive cuff variables, PF-298 writes the exact constant response as

\[
c_n
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
+
\operatorname{diag}(\kappa_{n,L},\kappa_{n,R}),
\tag{14}
\]

and PF-216 gives the same-sign energy floor

\[
\boxed{
\kappa_{n,L}+\kappa_{n,R}
=E_{+,n}\ge c_0>0
}
\tag{15}
\]

after a finite head. When the pants are assembled, PF-303's killing form is therefore exactly

\[
\langle t,D_Mt\rangle
=
\sum_n
\left(
\kappa_{n,L}|t_n|^2
+
\kappa_{n,R}|t_{n+1}|^2
\right)
\tag{16}
\]

up to the harmless endpoint convention of the finite block.

Each summand in (16) satisfies

\[
\kappa_{n,L}|t_n|^2+
\kappa_{n,R}|t_{n+1}|^2
\ge
(\kappa_{n,L}+\kappa_{n,R})
\min\{|t_n|^2,|t_{n+1}|^2\}.
\tag{17}
\]

On any fixed central fraction of the sine block, both neighboring `|z_n|` and `|z_{n+1}|` are bounded below by an absolute positive constant. Equations (13), (15), and (17) therefore give

\[
\boxed{
\langle t^{(M)},D_Mt^{(M)}\rangle\ge cM,
}
\tag{18}
\]

which is (8). No lower bound on either individual `\kappa_{n,L}` or `\kappa_{n,R}` is needed; only their exact same-sign sum from PF-216 matters.

This is the missing source-access fact. PF-307 used the same profiles only to compare raw constant energy with shorted energy. The PF-303 killing normalization could still have suppressed them if their `D_M` mass vanished. Equation (18) shows that it does not.

## 2. The same profile has sublinear fully shorted energy

Let `x^{(M)}` denote the PF-217 low-symmetric vector in the normalized PF-205 boundary Hilbert space obtained from the physical means `t^{(M)}` by the exact strip-energy map. This is only a coordinate change on the same constant trace; the positive form value and its shorted value are unchanged.

PF-217 supplies a nonconstant tangential relaxation with

\[
\mathfrak s_{\rm low}[x^{(M)}]
\le
C\bigl(1+\log M+MP_M^{-\eta}\bigr).
\tag{19}
\]

PF-307 observes that the smooth relaxation can be approximated in the positive form norm by a finite tangential Galerkin cutoff `L(M)`, with an error `o(M)` and, after choosing the cutoff more accurately if necessary, with the right-hand side of (19) enlarged only by a fixed constant factor. In physical cuff-constant coordinates this is precisely

\[
\langle t^{(M)},H_{M,L(M)}^{\mathrm{eff}}t^{(M)}\rangle
\le
C\bigl(1+\log M+MP_M^{-\eta}\bigr),
\tag{20}
\]

proving (9).

The representation dictionary is load-bearing here. `t^{(M)}` is the physical cuff-constant trace used by PF-298/PF-303; `x^{(M)}` is the corresponding vector after PF-205 strip-energy normalization. We do not identify their coefficient arrays. We use only that congruent coordinate changes preserve the underlying quadratic-form values and generalized Rayleigh quotients.

## 3. Killing-normalized Green amplification is the generalized inverse Rayleigh quotient

For any positive finite matrices `H_{\rm eff}` and `D`,

\[
\left\|D^{1/2}H_{\rm eff}^{-1}D^{1/2}\right\|
=
\sup_{0\ne t}
\frac{\langle t,Dt\rangle}
{\langle t,H_{\rm eff}t\rangle}.
\tag{21}
\]

This is the standard generalized Rayleigh characterization: substitute `v=H_{\rm eff}^{1/2}t`, or equivalently compare the reciprocal generalized eigenvalues of the pair `(H_{\rm eff},D)`.

Applying (21) to (18) and (20) gives (10). Because

\[
\frac{1+\log M}{M}+P_M^{-\eta}\longrightarrow0,
\tag{22}
\]

the lower bound diverges.

There is also an exact PF-306 source-overlap form of the same calculation. Put

\[
u_M
:=
\frac{H_M^{1/2}t^{(M)}}
{\sqrt{\langle t^{(M)},H_Mt^{(M)}\rangle}},
\qquad
A_M:=I-C_{M,L(M)}C_{M,L(M)}^*.
\tag{23}
\]

Then

\[
\langle u_M,A_Mu_M\rangle
=
\frac{\langle t^{(M)},H_{M,L(M)}^{\mathrm{eff}}t^{(M)}\rangle}
{\langle t^{(M)},H_Mt^{(M)}\rangle},
\tag{24}
\]

while

\[
\|X_M^*u_M\|^2
=
\frac{\langle t^{(M)},D_Mt^{(M)}\rangle}
{\langle t^{(M)},H_Mt^{(M)}\rangle}.
\tag{25}
\]

Weighted Cauchy--Schwarz gives, for every positive `A_M`,

\[
\|X_M^*A_M^{-1/2}\|^2
\ge
\frac{\|X_M^*u_M\|^2}{\langle u_M,A_Mu_M\rangle}.
\tag{26}
\]

The right-hand side is exactly the quotient in (21). Thus PF-307's explicit nearly screened direction is not merely present in the unrestricted Schur norm: after the canonical PF-303 entrance normalization, its source overlap is still large enough relative to its Schur deficit to force unbounded backreaction.

## 4. What this closes in the accepted source-weighted-return route

PF-305 remains exact: **inside the scalar constant-mode chain**, the killing-normalized Green reservoir is a norm-one positive contraction and is ideal-neutral. PF-308 does not contradict that statement. It shows precisely where that protection ends. Once the nonconstant sector is restored and shorted, the effective constant form can fall far below the scalar killing scale on the PF-217 screened blocks.

PF-307 left open the possibility that the canonical killing-normalized constant source might avoid the near-unit Schur directions strongly enough for

\[
X_M^*(I-C_{M,L}C_{M,L}^*)^{-1}X_M
\tag{27}
\]

to remain uniformly bounded even though the unrestricted resolvent norm diverges. Equation (10) closes that possibility. The killing form itself assigns order-`M` mass to the explicit screened profile while the effective energy is `o(M)`.

The accepted clue `CLUE-source-weighted-return-potential-controls-mixed-response` is therefore narrowed again. Scalar return depth is not the problem, but **scalar killing normalization is also not sufficient once nonconstant screening is admitted**. The next positive argument must identify a more selective physical source/target currency than the full constant killing space, or show that later signed/reassembly structure suppresses the screened component.

## 5. Prior art and novelty audit

The abstract operator step is classical. Generalized Rayleigh quotients, inverse quadratic forms, Schur complements, and positive-operator shorting all give (21) in standard finite-dimensional operator theory. PF-306 and PF-307 already audit the relevant Schur/shorting framework against Anderson--Trapp, *Shorted Operators. II*, SIAM Journal on Applied Mathematics 28(1), 60--71 (1975), DOI `10.1137/0128007`, and Li--Mathias, *Extremal Characterizations of the Schur Complement and Resulting Inequalities*, SIAM Review 42(2), 233--246 (2000), DOI `10.1137/S0036144599337290`. A targeted structure-level check also returns the classical Cauchy--Schwarz/Kantorovich family of positive-definite inverse-form inequalities. No novelty is claimed for these abstract identities.

The Mathia-specific content is the combination of three persisted facts in one common response: PF-217 gives the explicit slowly varying screened tail trace, PF-216/PF-298 give a fixed positive same-sign Robin-killing mass on every pant, and PF-303 identifies the assembled diagonal killing `D_M` that is the canonical scalar source normalization. Together they force the divergence in (10). That source-access conclusion is not contained in the abstract Schur theory and is the new route-level result here.

The mechanism is not arithmetic by itself. A matched surrogate family with the same positive same-sign killing floor and the same long-block tangential screening would satisfy the same conclusion. Any RH-relevant arithmetic discrimination must enter through the actual physical `P/H` source/reassembly maps or a later observable.

## 6. Boundaries and falsification tests

1. **Finite sections.** The theorem proves divergence of a family of canonical finite-section killing-normalized constant Green blocks. It does not silently identify an infinite-dimensional inverse or its domain.
2. **Constant source sector, not final physical `P/H`.** `\widetilde S_{M,L}` is the full constant Green block after nonconstant shorting. The actual PF-281/PF-290 mixed response still contains physical source and target projections, nonconstant normalization, and possible signed cancellation.
3. **No counting theorem.** One screened direction on each growing block is enough for operator-norm divergence. It gives no Weyl count or weak/Schatten singular-value distribution.
4. **Positive-shift killing is load-bearing.** The lower bound (18) uses PF-216's `E_{+,n}\ge c>0` for the `\Delta+1` pant response. It must not be imported unchanged to a zero-shift or on-spectrum problem.
5. **Zero-twist screening is load-bearing.** PF-217's cheap common tangential bump uses the exact zero-twist marking. A different twist regime requires a new screening estimate.
6. **Coordinate distinction is load-bearing.** Physical cuff means `t_n` and normalized low-sector coefficients are not identified term by term. The proof uses the exact PF-205 normalization only through invariant quadratic-form values.
7. **No weak-trace failure or RH consequence.** Uniform operator-norm blowup of this intermediate normalized block does not by itself prove noncompactness of the final mixed operator, failure of `\mathcal S_{1,\infty}`, a determinant obstruction, a zeta-zero relation, the critical line, or RH.

A direct falsification audit has only three project-specific steps: recheck PF-217's uniform `|t_n|\asymp|z_n|` on the long sine block, recheck PF-216/PF-298's exact identity `\kappa_{n,L}+\kappa_{n,R}=E_{+,n}\ge c`, and verify that the PF-307 Galerkin approximation realizes the same shorted energy in the PF-306 constant/nonconstant split. If those persist, (18)--(21) force (10).

## Consequence for the research line

The source-adapted branch after PF-307 is now narrower. The canonical PF-303 killing normalization does **not** make the explicit screened constant tail directions harmless; its full constant Green backreaction after nonconstant shorting is forced to grow without a uniform bound. The next discriminating calculation should therefore derive the genuine physical `P/H` entrance and reassembly maps around this block and test whether they annihilate, sparsify, or cancel the PF-217 screened profiles strongly enough to recover the required compact/weak-Schatten behavior. Another estimate of scalar return depth, another global Schur-angle norm bound, or another killing-normalized constant Green bound cannot close that gate.