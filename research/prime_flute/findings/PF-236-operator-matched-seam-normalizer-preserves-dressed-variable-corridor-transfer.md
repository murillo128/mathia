# PF-236 — an operator-matched seam normalizer preserves the dressed variable-corridor transfer

**Status:** `EXACT-DERIVED + OPERATOR-MATCHED-CONTROL + SINGULAR-VALUE-ENVELOPE + POSITIVE/ROUTE-NARROWING`. PF-233 shows that the variable-width diagonal neighboring-cuff corridor becomes an exact product problem only after the noncommuting boundary-mass conjugation `y=a^{-1/2}v`. The remaining conformal-transfer clue therefore asks whether the PF-228 inverse-level `w/s` gain survives the full two-boundary inversion rather than merely the raw cross-DtN block. There is an exact positive answer for the seam normalizer naturally matched to PF-233's effective transverse operator.

Let

\[
B=M_{a^{-1}},\qquad K=T_a^{1/2},
\]

so PF-233 writes the diagonal corridor DtN matrix as

\[
\Lambda_a=\mathcal B\Lambda_0(K)\mathcal B,
\qquad
\mathcal B=\operatorname{diag}(B^{1/2},B^{1/2}),
\]

with

\[
\Lambda_0(K)=K
\begin{pmatrix}
\coth K&-\operatorname{csch}K\\
-\operatorname{csch}K&\coth K
\end{pmatrix}.
\]

Fix the nominal corridor scale `s` from PF-233 and put `r_i=w_i/s`. Define the **operator-matched symmetric seam forms**

\[
q_i^{\rm mat}=K\tanh(r_iK),
\qquad
Q_i^{\rm mat}=B^{1/2}q_i^{\rm mat}B^{1/2}.
\]

If `Q^{mat}=diag(Q_1^{mat},Q_2^{mat})` and

\[
D^{\rm mat}
=\left(I+(Q^{\rm mat})^{-1/2}\Lambda_a(Q^{\rm mat})^{-1/2}\right)^{-1},
\]

then the apparently noncommuting `B`-congruence disappears **unitarily**, not approximately. The off-diagonal block is unitarily equivalent to the scalar functional calculus

\[
\boxed{
X_{r_1,r_2}(K)
}
\]

where

\[
\boxed{
X_{r_1,r_2}(k)
=
\frac{\sqrt{\tanh(r_1k)\tanh(r_2k)}}
{\sinh k\,[1+\tanh(r_1k)\tanh(r_2k)]
+\cosh k\,[\tanh(r_1k)+\tanh(r_2k)]}.
}
\]

Consequently, without assuming that `B`, `a`, `A`, or `T_a` commute,

\[
\boxed{
0\le X_{r_1,r_2}(k)
\le
\sqrt{r_1r_2}\,\frac{k}{\sinh k}.
}
\]

Since PF-233 gives

\[
\sqrt{c_0}\,s(m+\alpha)
\le k_m:=\sqrt{\lambda_m(T_a)}
\le \sqrt{C_0}\,s(m+\alpha),
\]

with uniform canonical-tail constants, the singular values of the matched dressed crossing satisfy

\[
\boxed{
s_{m+1}\!\left((D^{\rm mat})_{21}\right)
\le
\frac{\sqrt{w_1w_2}}s\,
F\!\left(\sqrt{c_0}\,s(m+\alpha)\right),
\qquad
F(z)=\frac z{\sinh z}.
}
\]

This is exactly the PF-228 amplitude currency together with `O(s^{-1})` inverse-seam channels and exponential high-mode decay. In the constant-width case `a\equiv s`, the matched form reduces identically to PF-228's flat seam normalizer `M\tanh(w_iM)`, so PF-236 is a genuine operator-valued extension of that cancellation rather than a new model with a different scaling.

The result does **not** identify `Q_i^{mat}` with the actual PF-205 seam form transported through PF-235's fixed axis compactification. That mismatch is now the decisive local normalization gate. PF-234/PF-235 control the actual seam relative to its flat complete-axis realization up to summable quadratic prime-dependent distortion, but they do not show that the resulting operator is close to `B^{1/2}K\tanh((w_i/s)K)B^{1/2}` in the sense needed by the off-diagonal inverse. Therefore variable-width mass noncommutation and full two-boundary inversion themselves are no longer candidate obstructions; the open problem is stability under the **actual-seam versus operator-matched-seam representation mismatch**, followed by PF-232 shear, physical `P/H` projections, finite-pant completion, and global reassembly.

## Claim

Let `H` be a Hilbert space and let `K\ge k_0I>0` be positive self-adjoint with compact resolvent. Let `C` be bounded, positive, boundedly invertible, and suppose the form congruences below are well defined. Put

\[
\Lambda_0
=K
\begin{pmatrix}
\coth K&-\operatorname{csch}K\\
-\operatorname{csch}K&\coth K
\end{pmatrix}.
\tag{1}
\]

For `r_1,r_2>0`, define

\[
q_i=K\tanh(r_iK),
\qquad
Q_i=Cq_iC,
\qquad
Q=\operatorname{diag}(Q_1,Q_2),
\tag{2}
\]

and

\[
\Lambda=\operatorname{diag}(C,C)\,
\Lambda_0\,
\operatorname{diag}(C,C).
\tag{3}
\]

Then, for

\[
D=\left(I+Q^{-1/2}\Lambda Q^{-1/2}\right)^{-1},
\tag{4}
\]

there are unitaries `U_i:H\to H` such that

\[
\boxed{
D_{21}=U_2^*X_{r_1,r_2}(K)U_1,
}
\tag{5}
\]

with `X_{r_1,r_2}` given above. In particular

\[
\boxed{
s_j(D_{21})=s_j(X_{r_1,r_2}(K))
}
\tag{6}
\]

and

\[
\boxed{
X_{r_1,r_2}(k)
\le \sqrt{r_1r_2}\,F(k),
\qquad
F(k)=\frac{k}{\sinh k}.
}
\tag{7}
\]

For PF-233 take

\[
C=B^{1/2}=M_{a^{-1/2}},
\qquad K=T_a^{1/2},
\qquad r_i=\frac{w_i}s.
\tag{8}
\]

Then (5)--(7) give

\[
\boxed{
s_{m+1}(D_{21})
\le
\rho\,F(\sqrt{c_0}\,s\kappa_m),
\qquad
\rho=\frac{\sqrt{w_1w_2}}s,
\quad \kappa_m=m+\alpha.
}
\tag{9}
\]

Thus every fixed `s\kappa_m=O(1)` band contains only `O(s^{-1})` channels at amplitude `O(\rho)`, and for `s\kappa_m\gg1` the envelope decays exponentially.

## 1. The PF-233 mass congruence cancels by an exact unitary

For each boundary define

\[
U_i:=q_i^{1/2}C Q_i^{-1/2}.
\tag{10}
\]

Because `Q_i=Cq_iC`,

\[
U_i^*U_i
=Q_i^{-1/2}Cq_iCQ_i^{-1/2}=I.
\tag{11}
\]

Also `Q_i^{-1}=C^{-1}q_i^{-1}C^{-1}`, hence

\[
U_iU_i^*
=q_i^{1/2}CQ_i^{-1}Cq_i^{1/2}=I.
\tag{12}
\]

Thus `U_i` is unitary. Equivalently,

\[
Q_i^{-1/2}C=U_i^*q_i^{-1/2},
\qquad
CQ_i^{-1/2}=q_i^{-1/2}U_i.
\tag{13}
\]

With `U=diag(U_1,U_2)`, equations (1)--(3) therefore give

\[
Q^{-1/2}\Lambda Q^{-1/2}
=U^*
\left[
q^{-1/2}\Lambda_0q^{-1/2}
\right]U,
\qquad q=\operatorname{diag}(q_1,q_2).
\tag{14}
\]

Functional calculus then yields

\[
D
=U^*
\left(I+q^{-1/2}\Lambda_0q^{-1/2}\right)^{-1}
U.
\tag{15}
\]

The crucial point is that **no commutator with `C` is estimated**. The same congruence appears in the corridor DtN and in the matched seam forms, so normalization turns it into a boundary unitary. This is stronger than two-sided form comparability and survives the full inverse exactly.

For unbounded `K`, the identities may first be read on finite spectral truncations and then passed to the closed operators/forms; `K\ge k_0I` makes every `q_i^{-1}` bounded on a fixed edge. In the PF-233 application `a` is uniformly bounded above and below by positive multiples of `s`, so `C=M_{a^{-1/2}}` is bounded and invertible, and its `W^{1,\infty}` regularity preserves the relevant form domain.

## 2. The remaining two-boundary inverse is scalar functional calculus

All entries of `q^{-1/2}\Lambda_0q^{-1/2}` are functions of the same operator `K`. It is therefore enough to invert the `2\times2` scalar matrix at one spectral value `k>0`.

Put

\[
t_i=\tanh(r_ik).
\tag{16}
\]

Since `q_i(k)=kt_i`, the normalized precision is

\[
\begin{pmatrix}
1+\coth(k)/t_1&-\operatorname{csch}(k)/\sqrt{t_1t_2}\\
-\operatorname{csch}(k)/\sqrt{t_1t_2}&1+\coth(k)/t_2
\end{pmatrix}.
\tag{17}
\]

Direct inversion and

\[
\coth^2k-\operatorname{csch}^2k=1
\tag{18}
\]

give exactly

\[
X_{r_1,r_2}(k)
=
\frac{\sqrt{t_1t_2}}
{\sinh k(1+t_1t_2)+\cosh k(t_1+t_2)}.
\tag{19}
\]

This is PF-228's scalar cancellation with `k` now the spectrum of the **noncommuting variable-width effective operator** `T_a^{1/2}`. The noncommutation has already been absorbed by the exact PF-233 mass conjugation and the unitary identity (14).

## 3. The dressed envelope survives with the same `w/s` factor

All terms in the denominator of (19) are nonnegative, so

\[
X_{r_1,r_2}(k)
\le
\frac{\sqrt{t_1t_2}}{\sinh k}.
\tag{20}
\]

Using `\tanh y\le y`,

\[
\sqrt{t_1t_2}
\le \sqrt{r_1r_2}\,k,
\tag{21}
\]

which proves (7).

The function

\[
F(k)=\frac{k}{\sinh k}
\tag{22}
\]

is positive and strictly decreasing on `(0,\infty)`, with `F(k)\le1` and `F(k)\le Cke^{-k}` for `k\ge1`. PF-233 gives ordered eigenvalues

\[
k_m\ge\sqrt{c_0}\,s\kappa_m.
\tag{23}
\]

Since every spectral value of `X(K)` is pointwise bounded by `\rho F(k_m)` and the latter sequence is decreasing, rearrangement gives (9). This supplies both the amplitude gain and the high-mode damping required by the conformal-transfer clue.

In particular, if `s\kappa_m\le Z` for fixed `Z`, there are `O_Z(s^{-1})` such modes, each of size at most `\rho`. Above that band the singular values decay exponentially in `sm`. No tangential commutation assumption has entered.

## 4. The matched normalizer specializes exactly to PF-228

If the PF-233 width is constant, `a\equiv s`, then

\[
B=s^{-1}I,
\qquad
T_a=s^2A,
\qquad
K=sA^{1/2}.
\tag{24}
\]

Writing `M=A^{1/2}` and `r_i=w_i/s`,

\[
Q_i^{\rm mat}
=s^{-1/2}
\left[sM\tanh(w_iM)\right]
s^{-1/2}
=M\tanh(w_iM).
\tag{25}
\]

This is precisely the symmetric flat seam branch used in PF-228. Thus the operator-matched construction has the correct constant-width limit with no scale renormalization or hidden extra factor.

On the canonical prime-flute tail PF-228 already gives

\[
\rho_n=\frac{\sqrt{w_nw_{n+1}}}{s_n}
\le \frac{C}{G_n},
\qquad
\delta_n\rho_n\le\frac{C}{P_n^2}.
\tag{26}
\]

PF-236 therefore shows that **the exact PF-233 variable-width diagonal corridor would retain the same critical reciprocal-prime top scale if its seam normalizers were the operator-matched forms (8)**. The channel population is only the intrinsic `O(s_n^{-1})` PF-233 population before any later finite-pant/global duplication.

## 5. What this rules out, and what it does not

The result rules out a specific suspected failure mode: the noncommuting boundary-mass factor `B=a^{-1}` from PF-233 does not by itself spoil the inverse-level cancellation. When the seam energy carries the same congruence, it cancels unitarily and the full `2\times2` inverse has exactly the PF-228 profile.

But this is an **operator-matched control**, not an assertion about the actual PF-205 seam. PF-234 identifies the actual seam in its intrinsic cuff coordinate; PF-235 transports it to the complete-axis coordinate with only `O(w_i^2)` seam-dependent distortion, while leaving the fixed `tau<->theta` compactification nontrivial. Neither result identifies that transported operator with

\[
B^{1/2}K\tanh((w_i/s)K)B^{1/2}.
\tag{27}
\]

That comparison cannot be replaced by a scalar Loewner slogan: the two operators live naturally in different tangential calculi, and the desired conclusion concerns one off-diagonal block after inversion. A valid next step must therefore prove an inverse-stability theorem for replacing `Q_i^{mat}` by the actual transported seam forms, or produce a boundary sequence for which that replacement loses the `\rho F(sm)` envelope.

PF-232's shear is also absent here, as are physical boundary-density `P/H` projections, finite one-cusp-pant completion, neighboring-cell extension mass, and PF-222's nested-cut reassembly. No global weak-`S_1`, scattering, determinant, zeta-zero, or RH conclusion follows from PF-236 alone.

## Prior-art and novelty audit

The use of `2\times2` Dirichlet-to-Neumann and Robin-to-Robin boundary-data matrices on an interval is classical. Clark--Gesztesy--Mitrea, *Boundary Data Maps for Schrödinger Operators on a Compact Interval* (2010), develops such matrix-valued boundary maps and their resolvent/Krein-type relations in a much broader one-dimensional Schrödinger setting (DOI `10.1051/mmnp/20105404`). The product-cylinder formula (1), scalar hyperbolic-function inversion, and the idea that boundary conditions may be encoded through Robin data are therefore **not claimed as new operator theory**.

The project-specific content is narrower: PF-233 supplies the exact noncommuting mass congruence for this hyperbolic variable-width corridor, and (10)--(15) show that choosing the correspondingly congruent seam functional calculus makes that mass noncommutation disappear by an exact unitary before the inverse is taken. Equation (9) then imports PF-233's spectral comparison to recover the precise PF-228 `sqrt(w_1w_2)/s` singular-value envelope. The literature audit found standard boundary-data machinery, not a source establishing this prime-flute specialization or identifying the actual PF-205 transported seam with the matched operator (27).

## Consequence for the research line

The accepted conformal-transfer clue can be narrowed. Its local diagonal-corridor target is no longer “prove that some noncommuting full inverse retains the cancellation” in the abstract. There is now an exact reference inverse with the right cancellation **inside the actual PF-233 variable-width operator**. The decisive local question is whether the actual PF-205/PF-235 seam normalizer can replace `Q_i^{mat}` without losing that off-diagonal singular-value envelope. If it can, the remaining local gates are PF-232 shear and physical/pant completion; if it cannot, the counterexample identifies the representation mismatch, rather than corridor width variation or mass conjugation, as the first genuine loss mechanism.